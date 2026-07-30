#!/usr/bin/env python3
"""Validate contracts/requirements/*.yaml against the v1 RequirementContract shape."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print(
        "ERROR: PyYAML is required (pip install pyyaml)",
        file=sys.stderr,
    )
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts" / "requirements"

API_VERSION = "nanlabs.dev/v1"
KIND = "RequirementContract"
INSTALLED_BY = {"workstation", "plugin", "user"}
CAPABILITIES = {
    "filesystem.read",
    "filesystem.write",
    "subprocess.execute",
    "network.outbound",
    "mcp.client",
    "secrets.env",
}
NAME_RE_OK = __import__("re").compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def expect_dict(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        fail(f"{label} must be a mapping")
    return value


def expect_str(obj: dict, key: str, label: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}.{key} must be a non-empty string")
    return value.strip()


def validate_binary(entry: object, label: str) -> None:
    bin_ = expect_dict(entry, label)
    name = expect_str(bin_, "name", label)
    if not NAME_RE_OK.match(name) and name not in {"python3"}:
        # allow common binary names with digits
        if not __import__("re").match(r"^[A-Za-z0-9._+-]+$", name):
            fail(f"{label}.name has invalid characters: {name!r}")
    required = bin_.get("required")
    if not isinstance(required, bool):
        fail(f"{label}.required must be a boolean")
    installed_by = expect_str(bin_, "installed_by", label)
    if installed_by not in INSTALLED_BY:
        fail(f"{label}.installed_by must be one of {sorted(INSTALLED_BY)}")
    if "installers" in bin_:
        installers = expect_dict(bin_["installers"], f"{label}.installers")
        for os_name, cmd in installers.items():
            if os_name not in {"macos", "linux", "windows"}:
                fail(f"{label}.installers key must be macos|linux|windows, got {os_name!r}")
            if not isinstance(cmd, str) or not cmd.strip():
                fail(f"{label}.installers.{os_name} must be a non-empty string")
            if any(tok in cmd.lower() for tok in ("ghp_", "xox", "begin private")):
                fail(f"{label}.installers.{os_name}: looks secret-like")


def validate_env(entry: object, label: str) -> None:
    env = expect_dict(entry, label)
    name = expect_str(env, "name", label)
    if not __import__("re").match(r"^[A-Z][A-Z0-9_]*$", name):
        fail(f"{label}.name must look like an ENV_VAR, got {name!r}")
    required = env.get("required")
    if required is not None and not isinstance(required, bool):
        fail(f"{label}.required must be a boolean when set")
    # forbid literal values
    for banned in ("value", "token", "secret", "default"):
        if banned in env:
            fail(f"{label}: do not set {banned!r} — names only")


def validate_contract(path: Path) -> None:
    rel = path.relative_to(ROOT)
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{rel}: invalid YAML ({exc})")
    root = expect_dict(data, str(rel))
    if root.get("apiVersion") != API_VERSION:
        fail(f"{rel}: apiVersion must be {API_VERSION!r}")
    if root.get("kind") != KIND:
        fail(f"{rel}: kind must be {KIND!r}")
    meta = expect_dict(root.get("metadata"), f"{rel}.metadata")
    name = expect_str(meta, "name", f"{rel}.metadata")
    if name != path.stem:
        fail(f"{rel}: metadata.name {name!r} must match filename stem {path.stem!r}")
    if not NAME_RE_OK.match(name):
        fail(f"{rel}: metadata.name must be kebab-case")
    expect_str(meta, "description", f"{rel}.metadata")
    if "appliesTo" in meta:
        applies = meta["appliesTo"]
        if not isinstance(applies, list) or not all(isinstance(x, str) for x in applies):
            fail(f"{rel}.metadata.appliesTo must be a list of strings")

    spec = expect_dict(root.get("spec"), f"{rel}.spec")
    requirements = expect_dict(spec.get("requirements"), f"{rel}.spec.requirements")
    binaries = requirements.get("binaries")
    if not isinstance(binaries, list):
        fail(f"{rel}.spec.requirements.binaries must be a list")
    for idx, binary in enumerate(binaries):
        validate_binary(binary, f"{rel}.spec.requirements.binaries[{idx}]")

    capabilities = spec.get("capabilities")
    if not isinstance(capabilities, list):
        fail(f"{rel}.spec.capabilities must be a list")
    for idx, cap in enumerate(capabilities):
        if not isinstance(cap, str) or cap not in CAPABILITIES:
            fail(
                f"{rel}.spec.capabilities[{idx}] must be one of "
                f"{sorted(CAPABILITIES)}, got {cap!r}"
            )

    if "env" in spec:
        env_list = spec["env"]
        if not isinstance(env_list, list):
            fail(f"{rel}.spec.env must be a list")
        for idx, env in enumerate(env_list):
            validate_env(env, f"{rel}.spec.env[{idx}]")

    if "setup" in spec:
        setup = expect_dict(spec["setup"], f"{rel}.spec.setup")
        if "interactive" in setup and not isinstance(setup["interactive"], bool):
            fail(f"{rel}.spec.setup.interactive must be a boolean")
        if "never_auto_install" in setup and not isinstance(
            setup["never_auto_install"], bool
        ):
            fail(f"{rel}.spec.setup.never_auto_install must be a boolean")
        if "verification_command" in setup:
            cmd = setup["verification_command"]
            if not isinstance(cmd, str) or not cmd.strip():
                fail(f"{rel}.spec.setup.verification_command must be a non-empty string")

    print(f"OK: {rel}")


def main() -> None:
    if not CONTRACTS.is_dir():
        fail("missing contracts/requirements/")
    paths = sorted(CONTRACTS.glob("*.yaml"))
    if not paths:
        fail("no contracts found under contracts/requirements/")
    for path in paths:
        validate_contract(path)
    print(f"OK: validated {len(paths)} requirement contract(s)")


if __name__ == "__main__":
    main()
