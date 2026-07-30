#!/usr/bin/env python3
"""Deterministically sync canonical agents into plugin surface trees.

Canonical source of truth:
  agents/<name>/AGENT.md (+ references/, NOTICE.txt)

Generated / mirrored surfaces:
  plugins/nanlabs-agents/agents/<name>/...
  plugins/nanlabs-core/agents/nanlabs-code-reviewer/...

Usage:
  python3 scripts/gen-surfaces.py          # write surfaces
  python3 scripts/gen-surfaces.py --check  # exit 1 on drift
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS_ROOT = ROOT / "agents"
PLUGIN_AGENTS = ROOT / "plugins" / "nanlabs-agents" / "agents"

# Keep core lean: only the baseline reviewer lives in nanlabs-core.
CORE_AGENT_NAMES = ("nanlabs-code-reviewer",)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def agent_dirs() -> list[Path]:
    dirs = sorted(
        p
        for p in AGENTS_ROOT.iterdir()
        if p.is_dir() and (p / "AGENT.md").is_file()
    )
    if not dirs:
        fail("no agents found under agents/")
    return dirs


def mirror_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def trees_equal(a: Path, b: Path) -> bool:
    """Deep compare (content, not just size/mtime)."""
    if not a.is_dir() or not b.is_dir():
        return False
    cmp = filecmp.dircmp(a, b, shallow=False)
    if cmp.left_only or cmp.right_only or cmp.funny_files or cmp.diff_files:
        return False
    for sub in cmp.common_dirs:
        if not trees_equal(a / sub, b / sub):
            return False
    return True


def expected_plugin_agents() -> dict[str, Path]:
    return {p.name: p for p in agent_dirs()}


def check_surfaces() -> None:
    expected = expected_plugin_agents()
    if not PLUGIN_AGENTS.is_dir():
        fail("missing plugins/nanlabs-agents/agents/ — run scripts/gen-surfaces.py")
    actual = {
        p.name: p
        for p in PLUGIN_AGENTS.iterdir()
        if p.is_dir() and (p / "AGENT.md").is_file()
    }
    if set(actual) != set(expected):
        fail(
            "nanlabs-agents plugin agent set drift: "
            f"extra={sorted(set(actual) - set(expected))} "
            f"missing={sorted(set(expected) - set(actual))}"
        )
    for name, src in expected.items():
        if not trees_equal(src, actual[name]):
            fail(f"drift: plugins/nanlabs-agents/agents/{name} != agents/{name}")
    for name in CORE_AGENT_NAMES:
        src = AGENTS_ROOT / name
        dst = ROOT / "plugins" / "nanlabs-core" / "agents" / name
        if not trees_equal(src, dst):
            fail(f"drift: plugins/nanlabs-core/agents/{name} != agents/{name}")
    print(
        f"OK: gen-surfaces check passed "
        f"({len(expected)} agents in nanlabs-agents; "
        f"{len(CORE_AGENT_NAMES)} in nanlabs-core)"
    )


def write_surfaces() -> None:
    PLUGIN_AGENTS.parent.mkdir(parents=True, exist_ok=True)
    PLUGIN_AGENTS.mkdir(parents=True, exist_ok=True)
    expected = expected_plugin_agents()
    # remove stale agent dirs
    for existing in list(PLUGIN_AGENTS.iterdir()) if PLUGIN_AGENTS.exists() else []:
        if existing.is_dir() and existing.name not in expected:
            shutil.rmtree(existing)
            print(f"removed stale {existing.relative_to(ROOT)}")
    for name, src in expected.items():
        dst = PLUGIN_AGENTS / name
        mirror_tree(src, dst)
        print(f"synced agents/{name} -> plugins/nanlabs-agents/agents/{name}")
    for name in CORE_AGENT_NAMES:
        src = AGENTS_ROOT / name
        dst = ROOT / "plugins" / "nanlabs-core" / "agents" / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        mirror_tree(src, dst)
        print(f"synced agents/{name} -> plugins/nanlabs-core/agents/{name}")
    print(f"OK: gen-surfaces wrote {len(expected)} agent surface(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if plugin agent surfaces drift from agents/",
    )
    args = parser.parse_args()
    if args.check:
        check_surfaces()
    else:
        write_surfaces()


if __name__ == "__main__":
    main()
