#!/usr/bin/env python3
"""Validate catalogs/pack-catalog.yaml and emit npx install argument lists."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("pyyaml required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
PACK_CATALOG = ROOT / "catalogs" / "pack-catalog.yaml"
SKILL_CATALOG = ROOT / "catalogs" / "skill-catalog.yaml"
AGENT_CATALOG = ROOT / "catalogs" / "agent-catalog.yaml"
PLUGINS_ROOT = ROOT / "plugins"
AGENTS_ROOT = ROOT / "agents"

PACK_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KINDS = {"group", "domain"}
COVERAGE = {"high", "medium", "low", "n/a"}
CLOUD = {"skills-only"}
CODE_CURSOR = {"skills-only", "skills-and-agents"}
SOURCE = "nanlabs/agent-toolkit"
# Packs are Agent Skills aliases, not Agent Plugins packages.
FORBIDDEN_PACK_KEYS = {"plugin", "plugin.json", "plugins", "$schema", "mcp.json"}


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


def expect_str(obj: dict[str, Any], key: str, label: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}.{key} must be a non-empty string")
    return value.strip()


def expect_list(obj: dict[str, Any], key: str, label: str) -> list[Any]:
    value = obj.get(key, [])
    if value is None:
        return []
    if not isinstance(value, list):
        fail(f"{label}.{key} must be a list")
    return value


def skill_names_on_disk() -> dict[str, Path]:
    found: dict[str, Path] = {}
    if not PLUGINS_ROOT.is_dir():
        fail("plugins/ is missing")
    for path in sorted(PLUGINS_ROOT.glob("*/skills/*/SKILL.md")):
        name = path.parent.name
        if name in found:
            fail(
                f"duplicate skill {name!r}: {found[name].relative_to(ROOT)} and "
                f"{path.parent.relative_to(ROOT)}"
            )
        found[name] = path.parent
    return found


def agent_names_on_disk() -> dict[str, Path]:
    found: dict[str, Path] = {}
    if not AGENTS_ROOT.is_dir():
        fail("agents/ is missing")
    for path in sorted(AGENTS_ROOT.glob("*/AGENT.md")):
        found[path.parent.name] = path.parent
    return found


def catalog_skill_names(skill_catalog: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    skills = skill_catalog.get("skills")
    if not isinstance(skills, list) or not skills:
        fail("catalogs/skill-catalog.yaml skills must be a non-empty list")
    for idx, entry in enumerate(skills):
        if not isinstance(entry, dict):
            fail(f"skill-catalog.skills[{idx}] must be a mapping")
        names.add(expect_str(entry, "name", f"skill-catalog.skills[{idx}]"))
    return names


def catalog_agent_names(agent_catalog: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    agents = agent_catalog.get("agents")
    if not isinstance(agents, list) or not agents:
        fail("catalogs/agent-catalog.yaml agents must be a non-empty list")
    for idx, entry in enumerate(agents):
        if not isinstance(entry, dict):
            fail(f"agent-catalog.agents[{idx}] must be a mapping")
        names.add(expect_str(entry, "name", f"agent-catalog.agents[{idx}]"))
    return names


def group_skill_names(group_path: Path) -> list[str]:
    names = sorted(
        p.parent.name for p in group_path.glob("*/SKILL.md") if p.is_file()
    )
    return names


def resolve_pack_skills(pack: dict[str, Any], label: str) -> list[str]:
    kind = pack["kind"]
    if kind == "group":
        path = ROOT / pack["path"]
        return group_skill_names(path)
    skills = expect_list(pack, "skills", label)
    names: list[str] = []
    for idx, item in enumerate(skills):
        if not isinstance(item, str) or not item.strip():
            fail(f"{label}.skills[{idx}] must be a non-empty string")
        names.append(item.strip())
    return names


def resolve_pack_agents(pack: dict[str, Any], label: str) -> list[str]:
    agents = expect_list(pack, "agents", label)
    names: list[str] = []
    for idx, item in enumerate(agents):
        if not isinstance(item, str) or not item.strip():
            fail(f"{label}.agents[{idx}] must be a non-empty string")
        names.append(item.strip())
    return names


def npx_args_for_pack(pack: dict[str, Any], skills: list[str]) -> list[str]:
    if pack["kind"] == "group":
        return ["skills", "add", f"{SOURCE}/{pack['path']}"]
    args = ["skills", "add", SOURCE]
    for name in skills:
        args.extend(["--skill", name])
    return args


def print_install_command(pack: dict[str, Any], skills: list[str]) -> None:
    args = npx_args_for_pack(pack, skills)
    quoted = " ".join(args)
    print(f"npx {quoted}")


def validate_pack(
    pack: dict[str, Any],
    idx: int,
    seen_ids: set[str],
    disk_skills: dict[str, Path],
    disk_agents: dict[str, Path],
    catalog_skills: set[str],
    catalog_agents: set[str],
) -> tuple[list[str], list[str]]:
    label = f"packs[{idx}]"
    if not isinstance(pack, dict):
        fail(f"{label} must be a mapping")

    pack_id = expect_str(pack, "id", label)
    if not PACK_ID_RE.fullmatch(pack_id):
        fail(f"{label}.id must be kebab-case, got {pack_id!r}")
    if pack_id in seen_ids:
        fail(f"duplicate pack id: {pack_id}")
    seen_ids.add(pack_id)
    label = f"pack {pack_id}"

    kind = expect_str(pack, "kind", label)
    if kind not in KINDS:
        fail(f"{label}.kind must be one of {sorted(KINDS)}")
    for key in FORBIDDEN_PACK_KEYS:
        if key in pack:
            fail(
                f"{label}: packs are not Agent Plugins packages; remove {key!r} "
                "(see https://agent-plugins.org/specification)"
            )

    expect_str(pack, "description", label)
    coverage = expect_str(pack, "coverage", label)
    if coverage not in COVERAGE:
        fail(f"{label}.coverage must be one of {sorted(COVERAGE)}")

    domains = expect_list(pack, "domains", label)
    if not domains:
        fail(f"{label}.domains must be a non-empty list")
    for d_idx, domain in enumerate(domains):
        if not isinstance(domain, str) or not domain.strip():
            fail(f"{label}.domains[{d_idx}] must be a non-empty string")

    cloud = expect_str(pack, "cloud", label)
    if cloud not in CLOUD:
        fail(f"{label}.cloud must be one of {sorted(CLOUD)}")
    code_cursor = expect_str(pack, "code_cursor", label)
    if code_cursor not in CODE_CURSOR:
        fail(f"{label}.code_cursor must be one of {sorted(CODE_CURSOR)}")

    if kind == "group":
        rel_path = expect_str(pack, "path", label)
        if not rel_path.startswith("plugins/nanlabs-") or not rel_path.endswith("/skills"):
            fail(
                f"{label}.path must be plugins/nanlabs-<group>/skills, got {rel_path!r}"
            )
        if "/../" in rel_path:
            fail(f"{label}.path must not traverse parent directories")
        path = ROOT / rel_path
        if not path.is_dir():
            fail(f"{label}.path does not exist: {rel_path}")
        if pack.get("skills"):
            fail(f"{label}: group packs must not list skills (discovered from path)")
        if pack.get("agents"):
            fail(f"{label}: group packs must not list agents")
        if code_cursor != "skills-only":
            fail(f"{label}: group packs are skills-only on every surface")
    else:
        if "path" in pack:
            fail(f"{label}: domain packs must not set path (use skills/agents lists)")

    skills = resolve_pack_skills(pack, label)
    agents = resolve_pack_agents(pack, label)
    if not skills and not agents:
        fail(f"{label} is empty: list skills and/or agents, or point path at SKILL.md files")

    for name in skills:
        if name not in disk_skills:
            fail(f"{label}: skill {name!r} has no plugins/*/skills/{name}/SKILL.md")
        if name not in catalog_skills:
            fail(f"{label}: skill {name!r} is missing from catalogs/skill-catalog.yaml")

    for name in agents:
        if name not in disk_agents:
            fail(f"{label}: agent {name!r} has no agents/{name}/AGENT.md")
        if name not in catalog_agents:
            fail(f"{label}: agent {name!r} is missing from catalogs/agent-catalog.yaml")

    if agents and code_cursor != "skills-and-agents":
        fail(f"{label}: packs with agents must set code_cursor: skills-and-agents")
    if not agents and code_cursor == "skills-and-agents":
        fail(f"{label}: skills-and-agents requires a non-empty agents list")
    if kind == "domain" and not skills:
        fail(f"{label}: domain packs must include at least one skill for Cloud installs")

    return skills, agents


def load_packs() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = load_yaml(PACK_CATALOG)
    version = data.get("version")
    if version != 1:
        fail("pack-catalog.version must be 1")
    source = expect_str(data, "source", "pack-catalog")
    if source != SOURCE:
        fail(f"pack-catalog.source must be {SOURCE!r}")
    packs = data.get("packs")
    if not isinstance(packs, list) or not packs:
        fail("pack-catalog.packs must be a non-empty list")
    return data, packs


def collect_packs() -> list[tuple[dict[str, Any], list[str], list[str]]]:
    _data, packs = load_packs()
    skill_catalog = load_yaml(SKILL_CATALOG)
    agent_catalog = load_yaml(AGENT_CATALOG)
    disk_skills = skill_names_on_disk()
    disk_agents = agent_names_on_disk()
    catalog_skills = catalog_skill_names(skill_catalog)
    catalog_agents = catalog_agent_names(agent_catalog)

    seen_ids: set[str] = set()
    resolved: list[tuple[dict[str, Any], list[str], list[str]]] = []
    for idx, pack in enumerate(packs):
        skills, agents = validate_pack(
            pack,
            idx,
            seen_ids,
            disk_skills,
            disk_agents,
            catalog_skills,
            catalog_agents,
        )
        resolved.append((pack, skills, agents))
    return resolved


def find_pack(pack_id: str) -> tuple[dict[str, Any], list[str], list[str]]:
    for pack, skills, agents in collect_packs():
        if pack["id"] == pack_id:
            return pack, skills, agents
    fail(f"unknown pack id: {pack_id}")
    raise AssertionError


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--list",
        action="store_true",
        help="print pack ids after validation",
    )
    parser.add_argument(
        "--npx-args",
        metavar="PACK_ID",
        help="print npx skills arguments for a pack (one per line)",
    )
    parser.add_argument(
        "--print-install",
        metavar="PACK_ID",
        help="print a copy-paste npx skills command for a pack",
    )
    args = parser.parse_args()

    if args.npx_args:
        pack, skills, _agents = find_pack(args.npx_args)
        for item in npx_args_for_pack(pack, skills):
            print(item)
        return
    if args.print_install:
        pack, skills, _agents = find_pack(args.print_install)
        print_install_command(pack, skills)
        return

    resolved = collect_packs()
    if args.list:
        print("id\tkind\tskills\tagents")
        for pack, skills, agents in resolved:
            print(f"{pack['id']}\t{pack['kind']}\t{len(skills)}\t{len(agents)}")
        return
    for pack, skills, agents in resolved:
        print(
            f"OK: pack {pack['id']} ({pack['kind']}, "
            f"{len(skills)} skills, {len(agents)} agents)"
        )
    print(f"OK: validated {len(resolved)} pack(s)")


if __name__ == "__main__":
    main()
