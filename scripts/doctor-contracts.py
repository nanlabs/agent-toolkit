#!/usr/bin/env python3
"""Read-only doctor: evaluate contracts/requirements against the local machine.

Never installs software. Prints a Markdown change/gap report for /setup.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts" / "requirements"


def load_contracts(names: list[str] | None) -> list[tuple[Path, dict]]:
    paths = sorted(CONTRACTS.glob("*.yaml"))
    if names:
        wanted = set(names)
        paths = [p for p in paths if p.stem in wanted]
        missing = wanted - {p.stem for p in paths}
        if missing:
            print(f"ERROR: unknown contract(s): {sorted(missing)}", file=sys.stderr)
            raise SystemExit(1)
    out: list[tuple[Path, dict]] = []
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        out.append((path, data))
    return out


def run_verify(cmd: str) -> bool:
    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
        return proc.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def check_binary(entry: dict) -> tuple[str, str]:
    name = entry["name"]
    required = bool(entry.get("required"))
    verify = entry.get("verify")
    present = shutil.which(name) is not None
    if verify and isinstance(verify, str):
        present = present or run_verify(verify)
    if present:
        return "pass", "found"
    if required:
        return "fail", "missing (required)"
    return "warn", "missing (optional)"


def check_env(entry: dict) -> tuple[str, str]:
    name = entry["name"]
    required = bool(entry.get("required", False))
    # Never print values — only presence
    present = bool(os.environ.get(name))
    if present:
        return "pass", "set"
    if required:
        return "fail", "unset (required)"
    return "warn", "unset (optional)"


def installer_hint(entry: dict) -> str:
    installers = entry.get("installers") or {}
    if not isinstance(installers, dict) or not installers:
        return "_(no installer hint — workstation / manual)_"
    # Prefer platform-ish keys without detecting OS aggressively
    parts = [f"`{os_name}`: `{cmd}`" for os_name, cmd in sorted(installers.items())]
    return "; ".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--contract",
        action="append",
        dest="contracts",
        help="Limit to contract id (repeatable). Default: all.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of Markdown.",
    )
    args = parser.parse_args()
    contracts = load_contracts(args.contracts)
    if not contracts:
        print("ERROR: no contracts found", file=sys.stderr)
        raise SystemExit(1)

    report_rows: list[dict] = []
    for path, data in contracts:
        meta = data.get("metadata") or {}
        spec = data.get("spec") or {}
        cid = meta.get("name", path.stem)
        setup = spec.get("setup") or {}
        never_auto = bool(setup.get("never_auto_install", False))

        binaries = ((spec.get("requirements") or {}).get("binaries")) or []
        for binary in binaries:
            if not isinstance(binary, dict):
                continue
            status, detail = check_binary(binary)
            report_rows.append(
                {
                    "contract": cid,
                    "kind": "binary",
                    "name": binary.get("name"),
                    "status": status,
                    "detail": detail,
                    "required": bool(binary.get("required")),
                    "installed_by": binary.get("installed_by"),
                    "never_auto_install": never_auto,
                    "install_hint": installer_hint(binary),
                }
            )

        for env in spec.get("env") or []:
            if not isinstance(env, dict):
                continue
            status, detail = check_env(env)
            report_rows.append(
                {
                    "contract": cid,
                    "kind": "env",
                    "name": env.get("name"),
                    "status": status,
                    "detail": detail,
                    "required": bool(env.get("required", False)),
                    "installed_by": "user",
                    "never_auto_install": True,
                    "install_hint": env.get("purpose") or "set in local env (never commit)",
                }
            )

    if args.json:
        import json

        print(json.dumps({"rows": report_rows}, indent=2))
        fails = sum(1 for r in report_rows if r["status"] == "fail")
        raise SystemExit(1 if fails else 0)

    print("# Setup doctor report")
    print()
    print("Read-only check against `contracts/requirements/`. **No installs performed.**")
    print()
    print("| Contract | Kind | Name | Status | Detail | Next |")
    print("| --- | --- | --- | --- | --- | --- |")
    for row in report_rows:
        nxt = "—"
        if row["status"] != "pass":
            if row["never_auto_install"] or row["installed_by"] == "workstation":
                nxt = "manual / workstation (ask before any install)"
            else:
                nxt = f"ask approval → {row['install_hint']}"
        print(
            f"| `{row['contract']}` | {row['kind']} | `{row['name']}` | "
            f"**{row['status']}** | {row['detail']} | {nxt} |"
        )

    fails = [r for r in report_rows if r["status"] == "fail"]
    warns = [r for r in report_rows if r["status"] == "warn"]
    print()
    print("## Summary")
    print()
    print(f"- Pass: {sum(1 for r in report_rows if r['status'] == 'pass')}")
    print(f"- Warn: {len(warns)}")
    print(f"- Fail: {len(fails)}")
    print()
    print("## Change report template")
    print()
    print("After approved installs (if any), record:")
    print()
    print("1. What changed (packages / plugins enabled)")
    print("2. Commands run (no secrets)")
    print("3. Verification results")
    print("4. Proposed next packs (`nanlabs-core`, `nanlabs-agents`, integrations)")
    print()
    if fails:
        print("**Blocking gaps remain** — do not claim setup complete.")
        raise SystemExit(1)
    print("No required gaps. Optional warnings may remain.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
