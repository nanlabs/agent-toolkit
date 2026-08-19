#!/usr/bin/env python3
"""Validate GitHub Copilot plugin and repository-customization surfaces."""

from __future__ import annotations

import json
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
REPO_GITHUB = ROOT / ".github"
REPO_SURFACE_PRODUCT = "nanlabs-core"


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


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must be a JSON object")
    return data


def expect_str(obj: dict[str, Any], key: str, label: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}.{key} must be a non-empty string")
    return value


def plugin_cfgs(products: dict[str, Any]) -> dict[str, dict[str, Any]]:
    cfgs = products.get("plugins") or {}
    if not isinstance(cfgs, dict) or not cfgs:
        fail("products/plugins.yaml must define at least one plugin")
    return cfgs


def repo_surface_agent_names(cfgs: dict[str, dict[str, Any]]) -> list[str]:
    cfg = cfgs.get(REPO_SURFACE_PRODUCT)
    if not isinstance(cfg, dict):
        fail(f"missing repository-surface product {REPO_SURFACE_PRODUCT!r}")
    names = {str(name) for name in (cfg.get("agents") or [])}
    if not names:
        fail("no agents resolved for Copilot repository surface")
    return sorted(names)


def repo_surface_skills(cfgs: dict[str, dict[str, Any]]) -> list[Path]:
    cfg = cfgs.get(REPO_SURFACE_PRODUCT)
    if not isinstance(cfg, dict):
        fail(f"missing repository-surface product {REPO_SURFACE_PRODUCT!r}")
    out: list[Path] = []
    for raw in cfg.get("skills") or []:
        path = ROOT / str(raw)
        if not path.is_dir():
            fail(f"missing skill source: {path.relative_to(ROOT)}")
        out.append(path)
    return out


def resolved_plugin_agent_names(cfg: dict[str, Any]) -> list[str]:
    agents_cfg = cfg.get("agents")
    if agents_cfg == "all":
        return sorted(p.name for p in (ROOT / "agents").iterdir() if (p / "AGENT.md").is_file())
    if isinstance(agents_cfg, list):
        return sorted(str(name) for name in agents_cfg)
    return []


def validate_plugin_cli_surfaces(cfgs: dict[str, dict[str, Any]]) -> None:
    for plugin_id, cfg in sorted(cfgs.items()):
        plugin_root = PLUGINS_ROOT / plugin_id
        if not plugin_root.is_dir():
            fail(f"missing plugin root: {plugin_root.relative_to(ROOT)}")

        manifest = load_json(plugin_root / "plugin.json")
        if expect_str(manifest, "name", f"{plugin_root.relative_to(ROOT)}/plugin.json") != plugin_id:
            fail(f"{plugin_root.relative_to(ROOT)}/plugin.json.name must match {plugin_id}")
        expect_str(manifest, "version", f"{plugin_root.relative_to(ROOT)}/plugin.json")
        expect_str(manifest, "description", f"{plugin_root.relative_to(ROOT)}/plugin.json")

        author = manifest.get("author")
        if not isinstance(author, dict):
            fail(f"{plugin_root.relative_to(ROOT)}/plugin.json.author must be an object")
        expect_str(author, "name", f"{plugin_root.relative_to(ROOT)}/plugin.json.author")
        expect_str(author, "url", f"{plugin_root.relative_to(ROOT)}/plugin.json.author")
        if "skills" in manifest:
            if manifest.get("skills") != "skills/":
                fail(f"{plugin_root.relative_to(ROOT)}/plugin.json.skills must equal 'skills/'")
            if not (plugin_root / "skills").is_dir():
                fail(f"{plugin_root.relative_to(ROOT)}/plugin.json declares skills/ but directory is missing")
        if "agents" in manifest:
            if manifest.get("agents") != "agents/":
                fail(f"{plugin_root.relative_to(ROOT)}/plugin.json.agents must equal 'agents/'")
            if not (plugin_root / "agents").is_dir():
                fail(f"{plugin_root.relative_to(ROOT)}/plugin.json declares agents/ but directory is missing")

        agent_names = resolved_plugin_agent_names(cfg)
        for name in agent_names:
            dst = plugin_root / "agents" / f"{name}.agent.md"
            if not dst.is_file():
                fail(f"missing Copilot agent file: {dst.relative_to(ROOT)}")


def validate_repo_surface(cfgs: dict[str, dict[str, Any]]) -> None:
    instructions = REPO_GITHUB / "copilot-instructions.md"
    text = instructions.read_text(encoding="utf-8") if instructions.is_file() else ""
    if not text.strip():
        fail("missing or empty .github/copilot-instructions.md")

    for agent_name in repo_surface_agent_names(cfgs):
        path = REPO_GITHUB / "agents" / f"{agent_name}.agent.md"
        if not path.is_file():
            fail(f"missing repository Copilot agent: {path.relative_to(ROOT)}")

    for skill_dir in repo_surface_skills(cfgs):
        path = REPO_GITHUB / "skills" / skill_dir.name / "SKILL.md"
        if not path.is_file():
            fail(f"missing repository Copilot skill: {path.relative_to(ROOT)}")


def main() -> None:
    products = load_yaml(PRODUCTS)
    cfgs = plugin_cfgs(products)
    validate_plugin_cli_surfaces(cfgs)
    validate_repo_surface(cfgs)
    print("OK: Copilot plugin and repository surfaces validated")


if __name__ == "__main__":
    main()
