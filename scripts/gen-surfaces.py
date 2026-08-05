#!/usr/bin/env python3
"""Deterministically assemble plugin surfaces from canonical sources.

Canonical sources:
  agents/<name>/AGENT.md (+ references/, NOTICE.txt)
  skills/core/<skill>/...
  products/plugins.yaml (versions + plugin metadata)
  catalogs/agent-target-map.yaml (Claude/Cursor/OpenCode frontmatter overlays)

Generated surfaces:
  plugins/<id>/agents/<name>.md          # flat agent files (Claude + Cursor discovery)
  plugins/<id>/resources/agents/<name>/  # references + NOTICE (not scanned as agents)
  plugins/<id>/skills/<skill>/           # mirrored from skills/core
  .claude-plugin/marketplace.json        # version fields synced
  .cursor-plugin/marketplace.json        # schema-safe entries + version in metadata only
  plugins/*/.claude-plugin/plugin.json
  plugins/*/.cursor-plugin/plugin.json

Usage:
  python3 scripts/gen-surfaces.py          # write surfaces
  python3 scripts/gen-surfaces.py --check  # exit 1 on drift
"""

from __future__ import annotations

import argparse
import filecmp
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("pyyaml required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
AGENTS_ROOT = ROOT / "agents"
PRODUCTS = ROOT / "products" / "plugins.yaml"
TARGET_MAP = ROOT / "catalogs" / "agent-target-map.yaml"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
FORBIDDEN_CANONICAL_KEYS = frozenset(
    {"opencode_mode", "opencode_color", "cursor_title", "tools"}
)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must be a mapping")
    return data


def agent_dirs() -> list[Path]:
    dirs = sorted(
        p
        for p in AGENTS_ROOT.iterdir()
        if p.is_dir() and (p / "AGENT.md").is_file()
    )
    if not dirs:
        fail("no agents found under agents/")
    return dirs


def parse_agent(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    body = text[match.end() :]
    front: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        front[key.strip()] = value.strip().strip("\"'")
    return front, body


def merge_target_frontmatter(name: str, target_map: dict[str, Any]) -> dict[str, str]:
    defaults = target_map.get("defaults") or {}
    claude_defaults = defaults.get("claude") or {}
    agent_overrides = (target_map.get("agents") or {}).get(name) or {}
    claude = {**claude_defaults, **(agent_overrides.get("claude") or {})}
    out: dict[str, str] = {"name": name}
    if "description" in claude:
        out["description"] = str(claude["description"])
    if tools := claude.get("tools"):
        out["tools"] = str(tools)
    if mode := claude.get("opencode_mode"):
        out["opencode_mode"] = str(mode)
    if color := claude.get("opencode_color"):
        out["opencode_color"] = str(color)
    return out


def rewrite_reference_paths(body: str, agent_name: str) -> str:
    prefix = f"${{CLAUDE_PLUGIN_ROOT}}/resources/agents/{agent_name}/"
    return body.replace("references/", prefix)


def render_plugin_agent(
    name: str,
    description: str,
    body: str,
    target_map: dict[str, Any],
) -> str:
    front = merge_target_frontmatter(name, target_map)
    front["name"] = name
    front["description"] = description
    lines = ["---"]
    for key in ("name", "description", "tools", "opencode_mode", "opencode_color"):
        if key in front:
            lines.append(f"{key}: {front[key]}")
    lines.append("---")
    lines.append("")
    rewritten = rewrite_reference_paths(body, name).lstrip("\n")
    return "\n".join(lines) + "\n" + rewritten


def mirror_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def trees_equal(a: Path, b: Path) -> bool:
    if not a.is_dir() or not b.is_dir():
        return False
    a_files = {p.relative_to(a): p for p in a.rglob("*") if p.is_file()}
    b_files = {p.relative_to(b): p for p in b.rglob("*") if p.is_file()}
    if set(a_files) != set(b_files):
        return False
    for rel, left in a_files.items():
        if not filecmp.cmp(left, b_files[rel], shallow=False):
            return False
    return True


def files_equal(a: Path, b: Path) -> bool:
    return a.is_file() and b.is_file() and filecmp.cmp(a, b, shallow=False)


def plugin_agent_names(products: dict[str, Any]) -> dict[str, list[str]]:
    all_agents = [p.name for p in agent_dirs()]
    out: dict[str, list[str]] = {}
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        agents_cfg = cfg.get("agents")
        if agents_cfg == "all":
            out[plugin_id] = all_agents
        elif isinstance(agents_cfg, list):
            out[plugin_id] = agents_cfg
        else:
            out[plugin_id] = []
    return out


def skill_sources(products: dict[str, Any], plugin_id: str) -> list[Path]:
    cfg = (products.get("plugins") or {}).get(plugin_id) or {}
    sources = cfg.get("skills") or []
    return [ROOT / str(s) for s in sources]


def sync_agent_surfaces(
    plugin_id: str,
    agent_names: list[str],
    target_map: dict[str, Any],
    *,
    check: bool,
) -> None:
    plugin_root = ROOT / "plugins" / plugin_id
    agents_dir = plugin_root / "agents"
    resources_root = plugin_root / "resources" / "agents"

    expected_md = {f"{name}.md" for name in agent_names}

    if check:
        if not agents_dir.is_dir():
            fail(f"missing {agents_dir.relative_to(ROOT)} — run scripts/gen-surfaces.py")
        actual_md = {p.name for p in agents_dir.glob("*.md")}
        stale = actual_md - expected_md
        missing = expected_md - actual_md
        if stale or missing:
            fail(
                f"{plugin_id} agent file drift: extra={sorted(stale)} missing={sorted(missing)}"
            )
        for stale_dir in agents_dir.iterdir():
            if stale_dir.is_dir():
                fail(
                    f"{plugin_id} stale nested agent dir (use flat .md): "
                    f"{stale_dir.relative_to(ROOT)}"
                )
    else:
        agents_dir.mkdir(parents=True, exist_ok=True)
        resources_root.mkdir(parents=True, exist_ok=True)
        for path in list(agents_dir.iterdir()):
            if path.is_dir():
                shutil.rmtree(path)
            elif path.suffix == ".md" and path.name not in expected_md:
                path.unlink()
        for path in list(resources_root.iterdir()):
            if path.is_dir() and path.name not in agent_names:
                shutil.rmtree(path)

    for name in agent_names:
        src_dir = AGENTS_ROOT / name
        canonical = src_dir / "AGENT.md"
        front, body = parse_agent(canonical)
        for key in front:
            if key in FORBIDDEN_CANONICAL_KEYS:
                fail(
                    f"agents/{name}/AGENT.md: canonical frontmatter must not include {key!r}"
                )
        description = front.get("description") or ""
        if not description:
            fail(f"agents/{name}/AGENT.md: missing description")
        rendered = render_plugin_agent(name, description, body, target_map)
        agent_md = agents_dir / f"{name}.md"
        resource_dir = resources_root / name

        if check:
            if not agent_md.is_file() or agent_md.read_text(encoding="utf-8") != rendered:
                fail(f"drift: {agent_md.relative_to(ROOT)}")
            src_refs = src_dir / "references"
            notice = src_dir / "NOTICE.txt"
            notice_dst = resource_dir / "NOTICE.txt"
            if src_refs.is_dir():
                if not resource_dir.is_dir():
                    fail(f"missing {resource_dir.relative_to(ROOT)}")
                ref_files = {p.name: p for p in src_refs.iterdir() if p.is_file()}
                for fname, src_file in ref_files.items():
                    dst_file = resource_dir / fname
                    if not files_equal(src_file, dst_file):
                        fail(f"drift: {dst_file.relative_to(ROOT)}")
                extra = {
                    p.name
                    for p in resource_dir.iterdir()
                    if p.is_file() and p.name not in ref_files and p.name != "NOTICE.txt"
                }
                if extra:
                    fail(f"unexpected files in {resource_dir.relative_to(ROOT)}: {sorted(extra)}")
            elif resource_dir.is_dir():
                leftover = [
                    p.name
                    for p in resource_dir.iterdir()
                    if p.is_file() and p.name != "NOTICE.txt"
                ]
                if leftover:
                    fail(f"unexpected {resource_dir.relative_to(ROOT)}")
            if notice.is_file():
                if not files_equal(notice, notice_dst):
                    fail(f"drift: {notice_dst.relative_to(ROOT)}")
            elif notice_dst.is_file():
                fail(f"unexpected {notice_dst.relative_to(ROOT)}")
        else:
            agent_md.write_text(rendered, encoding="utf-8")
            if (src_dir / "references").is_dir():
                mirror_tree(src_dir / "references", resource_dir)
            elif resource_dir.exists():
                shutil.rmtree(resource_dir)
                resource_dir.mkdir(parents=True, exist_ok=True)
            notice = src_dir / "NOTICE.txt"
            if notice.is_file():
                resource_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(notice, resource_dir / "NOTICE.txt")
            print(f"synced agent {name} -> plugins/{plugin_id}/agents/{name}.md")


def sync_skill_surfaces(plugin_id: str, sources: list[Path], *, check: bool) -> None:
    skills_dest = ROOT / "plugins" / plugin_id / "skills"
    expected = {src.name: src for src in sources}

    if check:
        if not skills_dest.is_dir() and expected:
            fail(f"missing {skills_dest.relative_to(ROOT)}")
        actual = {p.name: p for p in skills_dest.iterdir() if p.is_dir()} if skills_dest.is_dir() else {}
        if set(actual) != set(expected):
            fail(
                f"{plugin_id} skills drift: extra={sorted(set(actual)-set(expected))} "
                f"missing={sorted(set(expected)-set(actual))}"
            )
        for name, src in expected.items():
            if not trees_equal(src, actual[name]):
                fail(f"drift: plugins/{plugin_id}/skills/{name}")
    else:
        skills_dest.mkdir(parents=True, exist_ok=True)
        for existing in list(skills_dest.iterdir()):
            if existing.is_dir() and existing.name not in expected:
                shutil.rmtree(existing)
        for name, src in expected.items():
            dst = skills_dest / name
            mirror_tree(src, dst)
            print(f"synced {src.relative_to(ROOT)} -> plugins/{plugin_id}/skills/{name}")


def sync_versions(products: dict[str, Any], *, check: bool) -> None:
    meta_version = (products.get("marketplace") or {}).get("metadata", {}).get("version")
    if not meta_version:
        fail("products/plugins.yaml: marketplace.metadata.version required")

    claude_marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    cursor_marketplace = ROOT / ".cursor-plugin" / "marketplace.json"

    if check:
        _check_versions(products, claude_marketplace, cursor_marketplace, meta_version)
    else:
        _write_versions(products, claude_marketplace, cursor_marketplace, meta_version)


def _check_versions(
    products: dict[str, Any],
    claude_path: Path,
    cursor_path: Path,
    meta_version: str,
) -> None:
    claude = json.loads(claude_path.read_text(encoding="utf-8"))
    cursor = json.loads(cursor_path.read_text(encoding="utf-8"))
    if claude.get("metadata", {}).get("version") != meta_version:
        fail("drift: .claude-plugin/marketplace.json metadata.version")
    if cursor.get("metadata", {}).get("version") != meta_version:
        fail("drift: .cursor-plugin/marketplace.json metadata.version")
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        version = cfg.get("version")
        for marketplace, path in (("claude", claude_path), ("cursor", cursor_path)):
            data = claude if marketplace == "claude" else cursor
            entry = next((p for p in data.get("plugins", []) if p.get("name") == plugin_id), None)
            if not entry:
                fail(f"missing marketplace entry for {plugin_id} in {path.name}")
            if marketplace == "claude" and entry.get("version") != version:
                fail(f"drift: {path.name} plugin {plugin_id} version")
        for manifest_name in (".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"):
            manifest = ROOT / "plugins" / plugin_id / manifest_name
            if not manifest.is_file():
                continue
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if data.get("version") != version:
                fail(f"drift: {manifest.relative_to(ROOT)} version")


def _write_versions(
    products: dict[str, Any],
    claude_path: Path,
    cursor_path: Path,
    meta_version: str,
) -> None:
    claude = json.loads(claude_path.read_text(encoding="utf-8"))
    cursor = json.loads(cursor_path.read_text(encoding="utf-8"))

    claude.setdefault("metadata", {})["version"] = meta_version
    cursor.setdefault("metadata", {})["version"] = meta_version
    meta_desc = (products.get("marketplace") or {}).get("metadata", {}).get("description")
    if meta_desc:
        claude["metadata"]["description"] = meta_desc
        cursor["metadata"]["description"] = meta_desc

    for plugin_id, cfg in (products.get("plugins") or {}).items():
        version = cfg.get("version")
        description = cfg.get("description")
        for data in (claude, cursor):
            entry = next((p for p in data.get("plugins", []) if p.get("name") == plugin_id), None)
            if entry and description:
                entry["description"] = description
            if entry and data is claude and version:
                entry["version"] = version
        for manifest_name in (".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"):
            manifest = ROOT / "plugins" / plugin_id / manifest_name
            if manifest.is_file():
                data = json.loads(manifest.read_text(encoding="utf-8"))
                if version:
                    data["version"] = version
                if description:
                    data["description"] = description
                manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    claude_path.write_text(json.dumps(claude, indent=2) + "\n", encoding="utf-8")
    cursor_path.write_text(json.dumps(_cursor_marketplace_schema_safe(cursor), indent=2) + "\n", encoding="utf-8")
    print("synced plugin versions from products/plugins.yaml")


def _cursor_marketplace_schema_safe(data: dict[str, Any]) -> dict[str, Any]:
    """Cursor marketplace entries allow only name, source, description, minClientVersions."""
    cleaned = dict(data)
    plugins = []
    for entry in data.get("plugins") or []:
        safe = {
            k: entry[k]
            for k in ("name", "source", "description", "minClientVersions")
            if k in entry
        }
        plugins.append(safe)
    cleaned["plugins"] = plugins
    return cleaned


def check_surfaces() -> None:
    products = load_yaml(PRODUCTS)
    target_map = load_yaml(TARGET_MAP)
    agents_by_plugin = plugin_agent_names(products)

    for plugin_id, names in agents_by_plugin.items():
        if names:
            sync_agent_surfaces(plugin_id, names, target_map, check=True)

    for plugin_id, cfg in (products.get("plugins") or {}).items():
        sources = skill_sources(products, plugin_id)
        if sources:
            sync_skill_surfaces(plugin_id, sources, check=True)

    sync_versions(products, check=True)

    total_agents = sum(len(v) for v in agents_by_plugin.values())
    print(
        f"OK: gen-surfaces check passed ({total_agents} plugin agent file(s); "
        f"versions synced from products/plugins.yaml)"
    )


def write_surfaces() -> None:
    products = load_yaml(PRODUCTS)
    target_map = load_yaml(TARGET_MAP)
    agents_by_plugin = plugin_agent_names(products)

    for plugin_id, names in agents_by_plugin.items():
        if names:
            sync_agent_surfaces(plugin_id, names, target_map, check=False)

    for plugin_id in (products.get("plugins") or {}):
        sources = skill_sources(products, plugin_id)
        if sources:
            sync_skill_surfaces(plugin_id, sources, check=False)

    sync_versions(products, check=False)
    print("OK: gen-surfaces wrote plugin surfaces")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if plugin surfaces drift from canonical sources",
    )
    args = parser.parse_args()
    if args.check:
        check_surfaces()
    else:
        write_surfaces()


if __name__ == "__main__":
    main()
