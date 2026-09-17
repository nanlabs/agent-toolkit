#!/usr/bin/env python3
"""Deterministically assemble portable Agent Plugins and Copilot surfaces.

Generated artifacts:
  plugins/<id>/plugin.json                       # Agent Plugins v1.0.0 portable manifest
  plugins/<id>/agents/<name>.agent.md            # Copilot CLI agent files
  plugins/<id>/com.github.copilot/agents/        # VS Code Copilot agent files
  .github/copilot-instructions.md                # Repository customization surface
  .github/agents/<name>.agent.md                 # Repository agent files

Skills are not copied. Canonical skill bodies live under
plugins/<id>/skills/<name>/ (see catalogs/skills-layout.json).

Usage:
  python3 scripts/gen-copilot-surfaces.py
  python3 scripts/gen-copilot-surfaces.py --check
"""

from __future__ import annotations

import argparse
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
PRODUCTS = ROOT / "products" / "plugins.yaml"
PLUGINS_ROOT = ROOT / "plugins"
AGENTS_ROOT = ROOT / "agents"
TARGET_MAP = ROOT / "catalogs" / "agent-target-map.yaml"
LAYOUT = ROOT / "catalogs" / "skills-layout.json"
REPO_GITHUB = ROOT / ".github"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
OWNER_NAME = "NaNLABS"
OWNER_EMAIL = "technology@nanlabs.com"
REPOSITORY_URL = "https://github.com/nanlabs/agent-toolkit"
LICENSE = "MIT"
REPO_SURFACE_PRODUCT = "nanlabs-core"
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


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


def plugin_cfg(products: dict[str, Any], plugin_id: str) -> dict[str, Any]:
    cfg = ((products.get("plugins") or {}).get(plugin_id)) or {}
    if not cfg:
        fail(f"products/plugins.yaml missing plugin config for {plugin_id!r}")
    return cfg


def plugin_ids(products: dict[str, Any]) -> list[str]:
    ids = list((products.get("plugins") or {}).keys())
    if not ids:
        fail("products/plugins.yaml defines no plugins")
    return ids


def plugin_keywords(cfg: dict[str, Any]) -> list[str]:
    raw = cfg.get("keywords") or []
    if not isinstance(raw, list):
        fail("plugin keywords must be a list")
    return [str(item) for item in raw]


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
    return out


def rewrite_copilot_reference_paths(body: str, agent_name: str) -> str:
    prefix = f"${{PLUGIN_ROOT}}/resources/agents/{agent_name}/"
    body = re.sub(
        r"(?m)^(\s*-\s*)`references/",
        rf"\1`{prefix}",
        body,
    )
    body = re.sub(
        r"Read `references/",
        f"Read `{prefix}",
        body,
    )
    return body


def render_copilot_plugin_agent(
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
    rewritten = rewrite_copilot_reference_paths(body, name).lstrip("\n")
    return normalize_text("\n".join(lines) + "\n" + rewritten)


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


def canonical_agent_path(agent_name: str) -> Path:
    path = ROOT / "agents" / agent_name / "AGENT.md"
    if not path.is_file():
        fail(f"missing canonical agent source: {path.relative_to(ROOT)}")
    return path


def normalize_text(content: str) -> str:
    return content.rstrip("\n") + "\n"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalize_text(content), encoding="utf-8")


def ensure_file_equals(path: Path, expected: str) -> None:
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    current = normalize_text(path.read_text(encoding="utf-8"))
    if current != normalize_text(expected):
        fail(f"drift: {path.relative_to(ROOT)}")


def build_portable_manifest(plugin_id: str, cfg: dict[str, Any]) -> dict[str, Any]:
    """Closed Agent Plugins v1.0.0 plugin.json (no skills/agents/mcp path fields)."""
    manifest: dict[str, Any] = {
        "$schema": AGENT_PLUGINS_SCHEMA,
        "name": plugin_id,
        "version": cfg.get("version"),
        "description": cfg.get("description"),
        "author": {
            "name": OWNER_NAME,
            "email": OWNER_EMAIL,
            "url": REPOSITORY_URL,
        },
        "homepage": REPOSITORY_URL,
        "repository": REPOSITORY_URL,
        "license": LICENSE,
    }
    keywords = plugin_keywords(cfg)
    if keywords:
        manifest["keywords"] = keywords
    return {key: value for key, value in manifest.items() if value is not None}


def sync_agent_files(
    plugin_root: Path,
    dest_dir: Path,
    agent_names: list[str],
    rendered: dict[str, str],
    *,
    suffix: str,
    check: bool,
) -> None:
    expected = {f"{name}{suffix}" for name in agent_names}
    if check:
        existing = {p.name for p in dest_dir.glob(f"*{suffix}")} if dest_dir.is_dir() else set()
        if existing != expected:
            fail(
                f"{plugin_root.name} agent drift in {dest_dir.relative_to(ROOT)}: "
                f"extra={sorted(existing - expected)} "
                f"missing={sorted(expected - existing)}"
            )
        for name in agent_names:
            ensure_file_equals(dest_dir / f"{name}{suffix}", rendered[name])
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    for existing in dest_dir.glob(f"*{suffix}"):
        if existing.name not in expected:
            existing.unlink()
    for name in agent_names:
        write_text(dest_dir / f"{name}{suffix}", rendered[name])


def sync_plugin_cli_surfaces(products: dict[str, Any], *, check: bool) -> None:
    target_map = load_yaml(TARGET_MAP)
    agents_by_plugin = plugin_agent_names(products)
    for plugin_id in plugin_ids(products):
        cfg = plugin_cfg(products, plugin_id)
        plugin_root = PLUGINS_ROOT / plugin_id
        if not plugin_root.is_dir():
            fail(f"missing plugin root: {plugin_root.relative_to(ROOT)}")

        manifest_path = plugin_root / "plugin.json"
        manifest_text = json.dumps(build_portable_manifest(plugin_id, cfg), indent=2) + "\n"
        if check:
            ensure_file_equals(manifest_path, manifest_text)
        else:
            write_text(manifest_path, manifest_text)

        agent_names = agents_by_plugin.get(plugin_id, [])
        if not agent_names:
            continue
        rendered: dict[str, str] = {}
        for name in agent_names:
            canonical = canonical_agent_path(name)
            front, body = parse_agent(canonical)
            description = front.get("description")
            if not description:
                fail(f"agents/{name}/AGENT.md: missing description")
            rendered[name] = render_copilot_plugin_agent(name, description, body, target_map)

        sync_agent_files(
            plugin_root,
            plugin_root / "agents",
            agent_names,
            rendered,
            suffix=".agent.md",
            check=check,
        )
        sync_agent_files(
            plugin_root,
            plugin_root / "com.github.copilot" / "agents",
            agent_names,
            rendered,
            suffix=".agent.md",
            check=check,
        )


def repo_surface_skill_names(products: dict[str, Any]) -> list[str]:
    cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    group = cfg.get("skills_group")
    if not isinstance(group, str) or not group:
        fail(f"{REPO_SURFACE_PRODUCT} must declare skills_group")
    names = load_layout_groups().get(group)
    if not names:
        fail(f"skills-layout has no group {group!r}")
    return list(names)


def repo_surface_agent_names(products: dict[str, Any]) -> list[str]:
    cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    names = {str(name) for name in (cfg.get("agents") or [])}
    if not names:
        fail("no repository-surface agents resolved from products/plugins.yaml")
    return sorted(names)


def build_repo_instructions(products: dict[str, Any]) -> str:
    core_cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    skills = repo_surface_skill_names(products)
    agents = repo_surface_agent_names(products)
    lines = [
        "# NaNLABS Copilot Instructions",
        "",
        "Portable repository customization surface for `nanlabs/agent-toolkit`.",
        "",
        "## Scope",
        "",
        f"- Baseline product: `{REPO_SURFACE_PRODUCT}`",
        f"- Repository: `{REPOSITORY_URL}`",
        f"- Product description: {core_cfg.get('description')}",
        "",
        "## Public repository rules",
        "",
        "- Follow `AGENTS.md` and `docs/PUBLIC_CONTENT_POLICY.md` on every change.",
        "- Never commit secrets, private URLs, client data, or credentials.",
        "- Prefer official scripts under `scripts/` and CI workflows under `.github/workflows/`.",
        "- Do not invent install flags; document only real platform flows already present in this repo.",
        "",
        "## Available baseline skills",
        "",
        "Canonical copies live under `plugins/nanlabs-core/skills/<name>/`.",
        "",
    ]
    lines.extend(f"- `{name}`" for name in skills)
    lines.extend(
        [
            "",
            "## Available agents",
            "",
        ]
    )
    lines.extend(f"- `{name}`" for name in agents)
    lines.extend(
        [
            "",
            "## Source files",
            "",
            "- `README.md`",
            "- `AGENTS.md`",
            "- `docs/ADOPTION.md`",
            "- `docs/AGENT_PLUGINS.md`",
            "- `docs/LIFECYCLE.md`",
            "- `products/plugins.yaml`",
        ]
    )
    return normalize_text("\n".join(lines))


def sync_repo_surface(products: dict[str, Any], *, check: bool) -> None:
    instructions = build_repo_instructions(products)
    instructions_path = REPO_GITHUB / "copilot-instructions.md"
    if check:
        ensure_file_equals(instructions_path, instructions)
    else:
        write_text(instructions_path, instructions)

    agent_names = repo_surface_agent_names(products)
    agents_dir = REPO_GITHUB / "agents"
    expected_agents = {f"{name}.agent.md" for name in agent_names}
    if check:
        actual_agents = {p.name for p in agents_dir.glob("*.agent.md")} if agents_dir.is_dir() else set()
        if actual_agents != expected_agents:
            fail(
                "repository Copilot agent drift: "
                f"extra={sorted(actual_agents - expected_agents)} "
                f"missing={sorted(expected_agents - actual_agents)}"
            )
    else:
        agents_dir.mkdir(parents=True, exist_ok=True)
        for existing in agents_dir.glob("*.agent.md"):
            if existing.name not in expected_agents:
                existing.unlink()

    for name in agent_names:
        content = canonical_agent_path(name).read_text(encoding="utf-8")
        out_path = agents_dir / f"{name}.agent.md"
        if check:
            ensure_file_equals(out_path, content)
        else:
            write_text(out_path, content)

    skills_dir = REPO_GITHUB / "skills"
    if skills_dir.exists():
        if check:
            fail("legacy .github/skills/ must be removed (skills live in plugins/)")
        shutil.rmtree(skills_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if generated Copilot surfaces drift from canonical sources",
    )
    args = parser.parse_args()

    products = load_yaml(PRODUCTS)
    sync_plugin_cli_surfaces(products, check=args.check)
    sync_repo_surface(products, check=args.check)

    if args.check:
        print("OK: Copilot surfaces are in sync")
    else:
        print("OK: Copilot surfaces generated")


if __name__ == "__main__":
    main()
