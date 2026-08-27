#!/usr/bin/env python3
"""Reject tracked public content that exposes internal ClickUp URLs."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Keys are (repository-relative path, forbidden-pattern) pairs. Every entry
# must include a reason. Keep this empty unless a reviewed exception is
# genuinely required.
ALLOWLIST: dict[tuple[str, str], str] = {}

FORBIDDEN_PATTERNS = (
    re.compile(r"app\.clickup\.com", re.IGNORECASE),
    re.compile(r"clickup\.com/459857", re.IGNORECASE),
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def tracked_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(f"could not list tracked files with git: {exc}")

    return [
        ROOT / name
        for name in result.stdout.decode("utf-8").split("\0")
        if name
    ]


def validate_allowlist() -> None:
    known_patterns = {pattern.pattern for pattern in FORBIDDEN_PATTERNS}
    for key, reason in ALLOWLIST.items():
        if (
            not isinstance(key, tuple)
            or len(key) != 2
            or not all(isinstance(value, str) and value.strip() for value in key)
        ):
            fail("every allowlist key must be a (path, pattern) pair")
        if key[1] not in known_patterns:
            fail(f"allowlist uses an unknown forbidden pattern: {key[1]}")
        if not isinstance(reason, str) or not reason.strip():
            fail(f"allowlist entry {key!r} must include a documented reason")


def validate_content() -> int:
    findings: list[tuple[str, int, str]] = []
    scanned = 0

    for path in tracked_files():
        if not path.is_file():
            continue
        raw = path.read_bytes()
        if b"\0" in raw:
            continue
        scanned += 1
        text = raw.decode("utf-8", errors="replace")
        relative = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(text.splitlines(), start=1):
            for pattern in FORBIDDEN_PATTERNS:
                if pattern.search(line) and (relative, pattern.pattern) not in ALLOWLIST:
                    findings.append((relative, line_number, pattern.pattern))

    if findings:
        for path, line_number, pattern in sorted(findings):
            print(
                f"ERROR: {path}:{line_number}: forbidden public-content "
                f"pattern {pattern!r}",
                file=sys.stderr,
            )
        raise SystemExit(1)

    return scanned


def main() -> None:
    validate_allowlist()
    scanned = validate_content()
    print(
        "OK: public-content validator scanned "
        f"{scanned} tracked text files (allowlist entries: {len(ALLOWLIST)})"
    )


if __name__ == "__main__":
    main()
