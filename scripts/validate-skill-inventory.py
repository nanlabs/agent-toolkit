#!/usr/bin/env python3
"""Validate the single skill inventory (one SKILL.md per layout entry).

Canonical location: plugins/nanlabs-<group>/skills/<name>/SKILL.md
Legacy copies under skills/<group>/ or .github/skills/ are errors.
"""

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
LAYOUT = ROOT / "catalogs" / "skills-layout.json"
PRODUCTS = ROOT / "products" / "plugins.yaml"
PLUGINS_ROOT = ROOT / "plugins"
LEGACY_SKILLS = ROOT / "skills"
GITHUB_SKILLS = ROOT / ".github" / "skills"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_layout() -> dict[str, Any]:
    if not LAYOUT.is_file():
        fail(f"missing {LAYOUT.relative_to(ROOT)}")
    data = json.loads(LAYOUT.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("skills-layout.json must be an object")
    return data


def load_products() -> dict[str, Any]:
    if not PRODUCTS.is_file():
        fail(f"missing {PRODUCTS.relative_to(ROOT)}")
    data = yaml.safe_load(PRODUCTS.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("products/plugins.yaml must be a mapping")
    return data


def group_plugin_map(products: dict[str, Any]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for plugin_id, cfg in (products.get("plugins") or {}).items():
        if not isinstance(cfg, dict):
            continue
        group = cfg.get("skills_group")
        if group is None:
            continue
        if group in mapping:
            fail(f"skills_group {group!r} is claimed by {mapping[group]} and {plugin_id}")
        mapping[str(group)] = str(plugin_id)
    return mapping


def iter_skill_md(base: Path) -> list[Path]:
    if not base.exists():
        return []
    return sorted(p for p in base.rglob("SKILL.md") if p.is_file())


def main() -> None:
    layout = load_layout()
    products = load_products()
    group_to_plugin = group_plugin_map(products)
    groups = layout.get("groups")
    if not isinstance(groups, dict) or not groups:
        fail("skills-layout.json groups must be a non-empty mapping")

    if LEGACY_SKILLS.exists():
        leftover = iter_skill_md(LEGACY_SKILLS)
        if leftover:
            rels = ", ".join(str(p.relative_to(ROOT)) for p in leftover[:8])
            fail(f"legacy skills/ tree still has SKILL.md files: {rels}")
        fail("legacy skills/ directory must be removed (skills live in plugins/)")

    if GITHUB_SKILLS.exists():
        fail(".github/skills/ must not exist (Copilot no longer mirrors skill trees)")

    seen_names: dict[str, Path] = {}
    expected_paths: set[Path] = set()

    for group, names in groups.items():
        plugin_id = group_to_plugin.get(str(group))
        if not plugin_id:
            fail(f"layout group {group!r} has no products/plugins.yaml skills_group")
        if not isinstance(names, list) or not names:
            fail(f"layout group {group!r} must list skills")
        for name in names:
            skill_dir = PLUGINS_ROOT / plugin_id / "skills" / str(name)
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.is_file():
                fail(f"missing inventory skill: {skill_md.relative_to(ROOT)}")
            if name in seen_names:
                fail(f"duplicate layout skill {name!r}")
            seen_names[str(name)] = skill_md
            expected_paths.add(skill_md.resolve())

    extras: list[Path] = []
    if PLUGINS_ROOT.is_dir():
        for skill_md in iter_skill_md(PLUGINS_ROOT):
            if skill_md.resolve() not in expected_paths:
                extras.append(skill_md)
    if extras:
        rels = ", ".join(str(p.relative_to(ROOT)) for p in extras[:8])
        fail(f"SKILL.md outside layout inventory: {rels}")

    for plugin_id, group in ((pid, g) for g, pid in group_to_plugin.items()):
        skills_dir = PLUGINS_ROOT / plugin_id / "skills"
        if not skills_dir.is_dir():
            fail(f"missing {skills_dir.relative_to(ROOT)}")
        expected_names = {str(n) for n in groups[group]}
        actual_names = {
            p.parent.name
            for p in skills_dir.glob("*/SKILL.md")
            if p.is_file()
        }
        extra_names = sorted(actual_names - expected_names)
        missing_names = sorted(expected_names - actual_names)
        if extra_names or missing_names:
            fail(
                f"{plugin_id} skill inventory mismatch: "
                f"extra={extra_names} missing={missing_names}"
            )

    print(
        f"OK: skill inventory ({len(seen_names)} skills, "
        f"{len(group_to_plugin)} group plugins)"
    )


if __name__ == "__main__":
    main()
