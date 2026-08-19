#!/usr/bin/env python3
"""Deterministically assemble GitHub Copilot surfaces from canonical sources.

Generated artifacts:
  plugins/<id>/plugin.json                  # Copilot CLI plugin manifest
  plugins/<id>/agents/<name>.agent.md       # Copilot CLI agent files
  .github/copilot-instructions.md           # Repository customization surface
  .github/agents/<name>.agent.md            # Repository agent files
  .github/skills/<name>/SKILL.md            # Repository skills

Usage:
  python3 scripts/gen-copilot-surfaces.py
  python3 scripts/gen-copilot-surfaces.py --check
"""

from __future__ import annotations

import argparse
import filecmp
import json
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
REPO_GITHUB = ROOT / ".github"
OWNER_NAME = "NaNLABS"
OWNER_EMAIL = "technology@nanlabs.com"
REPOSITORY_URL = "https://github.com/nanlabs/agent-toolkit"
LICENSE = "MIT"
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


def plugin_cfg(products: dict[str, Any], plugin_id: str) -> dict[str, Any]:
    cfg = ((products.get("plugins") or {}).get(plugin_id)) or {}
    if not cfg:
        fail(f"products/plugins.yaml missing plugin config for {plugin_id!r}")
    return cfg


def plugin_ids(products: dict[str, Any]) -> list[str]:
    ids = sorted((products.get("plugins") or {}).keys())
    if not ids:
        fail("products/plugins.yaml defines no plugins")
    return ids


def skill_source_paths(cfg: dict[str, Any]) -> list[Path]:
    out: list[Path] = []
    for raw in cfg.get("skills") or []:
        path = ROOT / str(raw)
        if not path.is_dir():
            fail(f"missing skill source: {path.relative_to(ROOT)}")
        out.append(path)
    return out


def plugin_agent_markdown_paths(plugin_id: str) -> list[Path]:
    agents_dir = PLUGINS_ROOT / plugin_id / "agents"
    if not agents_dir.is_dir():
        return []
    return sorted(
        p
        for p in agents_dir.glob("*.md")
        if p.is_file() and p.suffix == ".md" and not p.name.endswith(".agent.md")
    )


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


def copy_skill_tree(src: Path, dst: Path) -> None:
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


def build_plugin_manifest(plugin_id: str, cfg: dict[str, Any]) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "name": plugin_id,
        "version": cfg.get("version"),
        "description": cfg.get("description"),
        "author": {
            "name": OWNER_NAME,
            "url": REPOSITORY_URL,
        },
        "repository": REPOSITORY_URL,
        "license": LICENSE,
    }
    if cfg.get("skills"):
        manifest["skills"] = "skills/"
    if cfg.get("agents"):
        manifest["agents"] = "agents/"
    return manifest


def sync_plugin_cli_surfaces(products: dict[str, Any], *, check: bool) -> None:
    for plugin_id in plugin_ids(products):
        cfg = plugin_cfg(products, plugin_id)
        plugin_root = PLUGINS_ROOT / plugin_id
        if not plugin_root.is_dir():
            fail(f"missing plugin root: {plugin_root.relative_to(ROOT)}")

        manifest_path = plugin_root / "plugin.json"
        manifest_text = json.dumps(build_plugin_manifest(plugin_id, cfg), indent=2) + "\n"
        if check:
            ensure_file_equals(manifest_path, manifest_text)
        else:
            write_text(manifest_path, manifest_text)

        md_agents = plugin_agent_markdown_paths(plugin_id)
        expected_agent_files = {f"{p.stem}.agent.md" for p in md_agents}
        if check:
            existing = {p.name for p in plugin_root.glob("agents/*.agent.md")}
            if existing != expected_agent_files:
                fail(
                    f"{plugin_id} Copilot agent drift: "
                    f"extra={sorted(existing - expected_agent_files)} "
                    f"missing={sorted(expected_agent_files - existing)}"
                )
        else:
            for existing in plugin_root.glob("agents/*.agent.md"):
                if existing.name not in expected_agent_files:
                    existing.unlink()

        for md_path in md_agents:
            copilot_path = md_path.with_name(f"{md_path.stem}.agent.md")
            content = md_path.read_text(encoding="utf-8")
            if check:
                ensure_file_equals(copilot_path, content)
            else:
                write_text(copilot_path, content)


def repo_surface_skill_sources(products: dict[str, Any]) -> list[Path]:
    core_cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    return skill_source_paths(core_cfg)


def repo_surface_agent_names(products: dict[str, Any]) -> list[str]:
    cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    names = {str(name) for name in (cfg.get("agents") or [])}
    if not names:
        fail("no repository-surface agents resolved from products/plugins.yaml")
    return sorted(names)


def build_repo_instructions(products: dict[str, Any]) -> str:
    core_cfg = plugin_cfg(products, REPO_SURFACE_PRODUCT)
    skills = [src.name for src in repo_surface_skill_sources(products)]
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
    skills = repo_surface_skill_sources(products)

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
    expected_skill_names = {src.name for src in skills}
    if check:
        actual = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
        if actual != expected_skill_names:
            fail(
                "repository Copilot skills drift: "
                f"extra={sorted(actual - expected_skill_names)} "
                f"missing={sorted(expected_skill_names - actual)}"
            )
    else:
        skills_dir.mkdir(parents=True, exist_ok=True)
        for existing in list(skills_dir.iterdir()):
            if existing.is_dir() and existing.name not in expected_skill_names:
                shutil.rmtree(existing)

    for src in skills:
        dst = skills_dir / src.name
        if check:
            if not trees_equal(src, dst):
                fail(f"drift: {dst.relative_to(ROOT)}")
        else:
            copy_skill_tree(src, dst)


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
