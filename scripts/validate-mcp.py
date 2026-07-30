#!/usr/bin/env python3
"""Validate MCP template stubs (config.template.json + README)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRETISH = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|"
    r"AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH )?PRIVATE KEY)",
    re.I,
)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def walk_for_literals(obj: object, path: str = "$") -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk_for_literals(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_for_literals(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        if SECRETISH.search(obj):
            fail(f"{path}: looks like a committed secret literal")
        # Allow ${ENV} and public URLs / command names only — flag long opaque tokens
        if re.fullmatch(r"[A-Za-z0-9_\-]{40,}", obj) and "${" not in obj:
            fail(f"{path}: suspicious long opaque string (use ${{ENV}} placeholders)")


def main() -> None:
    root = ROOT / "mcp" / "templates"
    templates = sorted(p for p in root.iterdir() if p.is_dir())
    if not templates:
        fail("no MCP templates under mcp/templates/")
    for tmpl in templates:
        cfg_path = tmpl / "config.template.json"
        readme = tmpl / "README.md"
        rel = tmpl.relative_to(ROOT)
        if not cfg_path.is_file():
            fail(f"{rel}: missing config.template.json")
        if not readme.is_file():
            fail(f"{rel}: missing README.md")
        try:
            data = json.loads(cfg_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{cfg_path.relative_to(ROOT)}: invalid JSON ({exc})")
        if not isinstance(data, dict) or "name" not in data:
            fail(f"{cfg_path.relative_to(ROOT)}: must be object with name")
        if data["name"] != tmpl.name:
            fail(
                f"{cfg_path.relative_to(ROOT)}: name {data['name']!r} "
                f"must match directory {tmpl.name!r}"
            )
        walk_for_literals(data)
        print(f"OK: {rel}")
    print(f"OK: validated {len(templates)} MCP template(s)")


if __name__ == "__main__":
    main()
