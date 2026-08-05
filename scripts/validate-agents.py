#!/usr/bin/env python3
"""Validate agent folders (AGENT.md frontmatter basics)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    agents_root = ROOT / "agents"
    paths = sorted(agents_root.glob("*/AGENT.md"))
    if not paths:
        print("OK: no agents yet (optional)")
        return
    for path in paths:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        match = FRONTMATTER_RE.match(text)
        if not match:
            fail(f"{rel}: missing YAML frontmatter")
        name_match = NAME_RE.search(match.group(1))
        if not name_match:
            fail(f"{rel}: frontmatter missing name")
        name = name_match.group(1).strip().strip("\"'")
        if name != path.parent.name:
            fail(f"{rel}: name {name!r} must match directory {path.parent.name!r}")
        if "description:" not in match.group(1):
            fail(f"{rel}: frontmatter missing description")
        forbidden = ("opencode_mode", "opencode_color", "cursor_title", "tools")
        for key in forbidden:
            if re.search(rf"^{re.escape(key)}:", match.group(1), re.MULTILINE):
                fail(
                    f"{rel}: canonical frontmatter must not include {key!r} "
                    f"(use catalogs/agent-target-map.yaml)"
                )
        print(f"OK: {rel}")
    print(f"OK: validated {len(paths)} agent file(s)")


if __name__ == "__main__":
    main()
