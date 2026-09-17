#!/usr/bin/env python3
"""Deterministically assemble plugin surfaces from canonical sources.

Canonical sources:
  agents/<name>/AGENT.md (+ references/, NOTICE.txt)
  plugins/<id>/skills/<name>/          # skill bodies (not copied)
  products/plugins.yaml (versions + plugin metadata)
  catalogs/skills-layout.json (skills_group membership)
  catalogs/agent-target-map.yaml (Claude/Cursor frontmatter overlays)

Generated surfaces (manifests only — skill trees are never copied):
  plugins/<id>/plugin.json             # Agent Plugins portable manifest
  plugins/<id>/.claude-plugin/plugin.json
  plugins/<id>/.cursor-plugin/plugin.json
  plugins/<id>/LICENSE
  plugins/<id>/README.md               # scaffolded only when missing
  plugins/<id>/agents/<name>.md        # flat agent files (when agents: is set)
  plugins/<id>/resources/agents/<name>/
  .claude-plugin/marketplace.json
  .cursor-plugin/marketplace.json
  .agents/plugins/marketplace.json     # ChatGPT desktop / Codex

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
LAYOUT = ROOT / "catalogs" / "skills-layout.json"
LICENSE_SRC = ROOT / "LICENSE"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FORBIDDEN_CANONICAL_KEYS = frozenset(
    {"opencode_mode", "opencode_color", "cursor_title", "tools"}
)
OWNER_NAME = "NaNLABS"
OWNER_EMAIL = "technology@nanlabs.com"
REPOSITORY_URL = "https://github.com/nanlabs/agent-toolkit"
LICENSE = "MIT"
MARKETPLACE_NAME = "nanlabs-agent-toolkit"
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR_MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"
AGENTS_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


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


def load_layout_groups() -> dict[str, list[str]]:
    if not LAYOUT.is_file():
        fail(f"missing required file: {LAYOUT.relative_to(ROOT)}")
    data = json.loads(LAYOUT.read_text(encoding="utf-8"))
    groups = data.get("groups")
    if not isinstance(groups, dict) or not groups:
        fail("catalogs/skills-layout.json groups must be a non-empty mapping")
    out: dict[str, list[str]] = {}
    for group, names in groups.items():
        if not isinstance(names, list) or not names:
            fail(f"skills-layout groups.{group} must be a non-empty list")
        out[str(group)] = [str(name) for name in names]
    return out


def dump_json(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=2) + "\n"


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_json(data), encoding="utf-8")


def ensure_text_equals(path: Path, expected: str) -> None:
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)} — run scripts/gen-surfaces.py")
    current = path.read_text(encoding="utf-8")
    if current != expected:
        fail(f"drift: {path.relative_to(ROOT)}")


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
    # OpenCode fields are intentionally not emitted (out of NaNLABS production scope).
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
    for key in ("name", "description", "tools"):
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
            out[plugin_id] = [str(name) for name in agents_cfg]
        else:
            out[plugin_id] = []
    return out


def plugin_keywords(cfg: dict[str, Any]) -> list[str]:
    raw = cfg.get("keywords") or []
    if not isinstance(raw, list):
        fail("plugin keywords must be a list")
    return [str(item) for item in raw]


def build_portable_manifest(plugin_id: str, cfg: dict[str, Any]) -> dict[str, Any]:
    """Closed Agent Plugins v1.0.0 plugin.json (no skills/agents/mcp path fields)."""
    author: dict[str, str] = {
        "name": OWNER_NAME,
        "email": OWNER_EMAIL,
        "url": REPOSITORY_URL,
    }
    manifest: dict[str, Any] = {
        "$schema": AGENT_PLUGINS_SCHEMA,
        "name": plugin_id,
        "version": cfg.get("version"),
        "description": cfg.get("description"),
        "author": author,
        "homepage": REPOSITORY_URL,
        "repository": REPOSITORY_URL,
        "license": LICENSE,
    }
    keywords = plugin_keywords(cfg)
    if keywords:
        manifest["keywords"] = keywords
    return {key: value for key, value in manifest.items() if value is not None}


def build_native_manifest(plugin_id: str, cfg: dict[str, Any]) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "name": plugin_id,
        "version": cfg.get("version"),
        "description": cfg.get("description"),
        "author": {
            "name": OWNER_NAME,
            "email": OWNER_EMAIL,
        },
        "homepage": REPOSITORY_URL,
        "repository": REPOSITORY_URL,
        "license": LICENSE,
    }
    keywords = plugin_keywords(cfg)
    if keywords:
        manifest["keywords"] = keywords
    return {key: value for key, value in manifest.items() if value is not None}


def plugin_readme(plugin_id: str, cfg: dict[str, Any]) -> str:
    description = str(cfg.get("description") or "").strip()
    group = cfg.get("skills_group")
    skills_note = (
        f"Canonical skills live under `skills/<name>/` (layout group `{group}`)."
        if group
        else "This plugin ships agent personas; skill bodies live in the group plugins."
    )
    return (
        f"# {plugin_id}\n"
        f"\n"
        f"{description}\n"
        f"\n"
        f"{skills_note} There is no second tree under `skills/<group>/`.\n"
        f"\n"
        f"## Install\n"
        f"\n"
        f"See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.\n"
        f"\n"
        f"### Claude Code\n"
        f"\n"
        f"```text\n"
        f"/plugin marketplace add nanlabs/agent-toolkit\n"
        f"/plugin install {plugin_id}@nanlabs-agent-toolkit\n"
        f"```\n"
        f"\n"
        f"### GitHub Copilot CLI\n"
        f"\n"
        f"```bash\n"
        f"copilot plugin install nanlabs/agent-toolkit:plugins/{plugin_id}\n"
        f"```\n"
        f"\n"
        f"### Cursor\n"
        f"\n"
        f"```bash\n"
        f"agent --plugin-dir /path/to/agent-toolkit/plugins/{plugin_id}\n"
        f"```\n"
        f"\n"
        f"### Agent Plugins folder import\n"
        f"\n"
        f"Point the client at `plugins/{plugin_id}` (`plugin.json` + `skills/<name>/SKILL.md`).\n"
        f"Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.\n"
    )


def scaffold_plugin(plugin_id: str, cfg: dict[str, Any], *, check: bool) -> None:
    plugin_root = ROOT / "plugins" / plugin_id
    license_dst = plugin_root / "LICENSE"
    readme_dst = plugin_root / "README.md"
    portable = build_portable_manifest(plugin_id, cfg)
    native = build_native_manifest(plugin_id, cfg)
    portable_text = dump_json(portable)
    native_text = dump_json(native)
    license_text = LICENSE_SRC.read_text(encoding="utf-8") if LICENSE_SRC.is_file() else ""
    if not license_text:
        fail("missing repo LICENSE")

    manifests = {
        plugin_root / "plugin.json": portable_text,
        plugin_root / ".claude-plugin" / "plugin.json": native_text,
        plugin_root / ".cursor-plugin" / "plugin.json": native_text,
    }

    if check:
        if not plugin_root.is_dir():
            fail(f"missing {plugin_root.relative_to(ROOT)} — run scripts/gen-surfaces.py")
        for path, expected in manifests.items():
            ensure_text_equals(path, expected)
        if not license_dst.is_file() or license_dst.read_text(encoding="utf-8") != license_text:
            fail(f"drift: {license_dst.relative_to(ROOT)}")
        if not readme_dst.is_file():
            fail(f"missing {readme_dst.relative_to(ROOT)}")
        return

    plugin_root.mkdir(parents=True, exist_ok=True)
    for path, expected in manifests.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8")
    license_dst.write_text(license_text, encoding="utf-8")
    if not readme_dst.is_file():
        readme_dst.write_text(plugin_readme(plugin_id, cfg), encoding="utf-8")
        print(f"scaffolded {readme_dst.relative_to(ROOT)}")
    print(f"synced manifests for plugins/{plugin_id}")


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
        actual_md = {
            p.name for p in agents_dir.glob("*.md") if not p.name.endswith(".agent.md")
        }
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
            elif (
                path.suffix == ".md"
                and not path.name.endswith(".agent.md")
                and path.name not in expected_md
            ):
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


def marketplace_meta(products: dict[str, Any]) -> tuple[str, str]:
    meta = (products.get("marketplace") or {}).get("metadata") or {}
    version = meta.get("version")
    description = meta.get("description")
    if not isinstance(version, str) or not version.strip():
        fail("products/plugins.yaml: marketplace.metadata.version required")
    if not isinstance(description, str) or not description.strip():
        fail("products/plugins.yaml: marketplace.metadata.description required")
    return version, description


def build_claude_marketplace(products: dict[str, Any]) -> dict[str, Any]:
    version, description = marketplace_meta(products)
    plugins: list[dict[str, Any]] = []
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        entry: dict[str, Any] = {
            "name": plugin_id,
            "source": f"./plugins/{plugin_id}",
            "description": cfg.get("description"),
            "version": cfg.get("version"),
            "category": "productivity",
        }
        keywords = plugin_keywords(cfg)
        if keywords:
            entry["tags"] = keywords
        plugins.append(entry)
    return {
        "name": MARKETPLACE_NAME,
        "owner": {"name": OWNER_NAME, "email": OWNER_EMAIL},
        "metadata": {
            "description": description,
            "version": version,
            "pluginRoot": "./plugins",
        },
        "plugins": plugins,
    }


def build_cursor_marketplace(products: dict[str, Any]) -> dict[str, Any]:
    version, description = marketplace_meta(products)
    plugins: list[dict[str, Any]] = []
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        plugins.append(
            {
                "name": plugin_id,
                "source": plugin_id,
                "description": cfg.get("description"),
            }
        )
    return {
        "name": MARKETPLACE_NAME,
        "owner": {"name": OWNER_NAME, "email": OWNER_EMAIL},
        "metadata": {
            "description": description,
            "version": version,
            "pluginRoot": "plugins",
        },
        "plugins": plugins,
    }


def build_agents_marketplace(products: dict[str, Any]) -> dict[str, Any]:
    plugins: list[dict[str, Any]] = []
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        plugins.append(
            {
                "name": plugin_id,
                "description": cfg.get("description"),
                "source": {"path": f"./plugins/{plugin_id}"},
            }
        )
    return {"name": MARKETPLACE_NAME, "plugins": plugins}


def sync_marketplaces(products: dict[str, Any], *, check: bool) -> None:
    expected = {
        CLAUDE_MARKETPLACE: build_claude_marketplace(products),
        CURSOR_MARKETPLACE: build_cursor_marketplace(products),
        AGENTS_MARKETPLACE: build_agents_marketplace(products),
    }
    for path, data in expected.items():
        text = dump_json(data)
        if check:
            ensure_text_equals(path, text)
        else:
            write_json(path, data)
            print(f"synced {path.relative_to(ROOT)}")


def check_surfaces() -> None:
    products = load_yaml(PRODUCTS)
    target_map = load_yaml(TARGET_MAP)
    layout_groups = load_layout_groups()
    agents_by_plugin = plugin_agent_names(products)

    for plugin_id, cfg in (products.get("plugins") or {}).items():
        group = cfg.get("skills_group")
        if group is not None and group not in layout_groups:
            fail(f"products/plugins.yaml {plugin_id}: unknown skills_group {group!r}")
        scaffold_plugin(plugin_id, cfg, check=True)
        names = agents_by_plugin.get(plugin_id) or []
        if names:
            sync_agent_surfaces(plugin_id, names, target_map, check=True)

    sync_marketplaces(products, check=True)

    total_agents = sum(len(v) for v in agents_by_plugin.values())
    print(
        f"OK: gen-surfaces check passed ({total_agents} plugin agent file(s); "
        f"manifests only — skill trees are not generated)"
    )


def write_surfaces() -> None:
    products = load_yaml(PRODUCTS)
    target_map = load_yaml(TARGET_MAP)
    layout_groups = load_layout_groups()
    agents_by_plugin = plugin_agent_names(products)

    for plugin_id, cfg in (products.get("plugins") or {}).items():
        group = cfg.get("skills_group")
        if group is not None and group not in layout_groups:
            fail(f"products/plugins.yaml {plugin_id}: unknown skills_group {group!r}")
        scaffold_plugin(plugin_id, cfg, check=False)
        names = agents_by_plugin.get(plugin_id) or []
        if names:
            sync_agent_surfaces(plugin_id, names, target_map, check=False)

    sync_marketplaces(products, check=False)
    print("OK: gen-surfaces wrote plugin manifests (skills were not copied)")


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
