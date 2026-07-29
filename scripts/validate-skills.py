#!/usr/bin/env python3
"""Validate Agent Skills folders (SKILL.md frontmatter + public-safety basics)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*>-?\s*(.+?)(?=\n[a-zA-Z_]+:|\n---|\Z)", re.DOTALL | re.MULTILINE)

# Conservative patterns — fail CI if someone commits obvious secrets.
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"(?i)secret\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def iter_skill_files() -> list[Path]:
    paths: list[Path] = []
    for base in (ROOT / "skills", ROOT / "plugins"):
        if not base.exists():
            continue
        paths.extend(sorted(base.rglob("SKILL.md")))
    return paths


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{rel}: missing YAML frontmatter")
    front = match.group(1)
    name_match = NAME_RE.search(front)
    if not name_match:
        fail(f"{rel}: frontmatter missing name")
    name = name_match.group(1).strip().strip("\"'")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"{rel}: name must be kebab-case alphanumeric, got {name!r}")
    if len(name) > 64:
        fail(f"{rel}: name exceeds 64 characters")
    # Agent Skills: name must match parent directory (skip plugin mirror copies).
    parent = path.parent.name
    if path.parts[-3] != "plugins" and name != parent:
        fail(f"{rel}: frontmatter name {name!r} must match directory {parent!r}")
    if "description:" not in front:
        fail(f"{rel}: frontmatter missing description")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"{rel}: matched forbidden secret-like pattern: {pattern.pattern}")


def main() -> None:
    skills = iter_skill_files()
    if not skills:
        fail("no SKILL.md files found under skills/ or plugins/")
    for path in skills:
        validate_skill(path)
        print(f"OK: {path.relative_to(ROOT)}")
    print(f"OK: validated {len(skills)} skill file(s)")


if __name__ == "__main__":
    main()
