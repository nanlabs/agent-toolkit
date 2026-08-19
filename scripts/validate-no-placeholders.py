#!/usr/bin/env python3
"""Fail on empty directories or placeholder-only directories in the repo."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_FILENAMES = {"README.md", "DEPRECATION.md", ".gitkeep", "overlay.yaml"}
SKIP_DIR_NAMES = {
    ".git",
    ".cursor",
    ".pytest_cache",
    "__pycache__",
    ".venv",
}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in path.parts)


def iter_dirs() -> list[Path]:
    dirs: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_dir():
            continue
        if should_skip(path.relative_to(ROOT)):
            continue
        dirs.append(path)
    return sorted(dirs)


def validate_dir(path: Path) -> None:
    rel = path.relative_to(ROOT)
    entries = sorted(path.iterdir(), key=lambda p: p.name)
    if not entries:
        fail(f"empty directory not allowed: {rel}")

    files = [p.name for p in entries if p.is_file()]
    subdirs = [p for p in entries if p.is_dir()]
    if files and not subdirs and set(files).issubset(PLACEHOLDER_FILENAMES):
        fail(
            "placeholder-only directory not allowed: "
            f"{rel} contains only {sorted(files)}"
        )


def main() -> None:
    for path in iter_dirs():
        validate_dir(path)
    print("OK: no empty or placeholder-only directories found")


if __name__ == "__main__":
    main()
