#!/usr/bin/env python3
"""Validate Agent Plugins v1.0.0 manifests and component discovery."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:  # pragma: no cover
    print(
        "ERROR: jsonschema is required. Install with: pip install jsonschema",
        file=sys.stderr,
    )
    raise SystemExit(1)


ROOT = Path(__file__).resolve().parents[1]
PLUGINS_ROOT = ROOT / "plugins"
SCHEMAS_ROOT = ROOT / "schemas" / "agent-plugins" / "1.0.0"
PLUGIN_SCHEMA_PATH = SCHEMAS_ROOT / "plugin.schema.json"
MCP_SCHEMA_PATH = SCHEMAS_ROOT / "mcp.schema.json"
PLUGIN_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
PLUGIN_NAME_RE = re.compile(
    r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$"
)
SCHEMA_VERSION_RE = re.compile(r"/schemas/([^/]+)/")
WINDOWS_ABSOLUTE_PATH_RE = re.compile(r"^[A-Za-z]:[\\/]")
SHELL_LIKE_COMMAND_CHARS = frozenset("|&;<>$`'\"()\\")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def load_schema(path: Path) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must be a JSON object")
    return data


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def ensure_not_symlink(path: Path, label: str) -> None:
    if path.is_symlink():
        fail(f"{label} must not be a symlink")


def ensure_contained(path: Path, plugin_root: Path, label: str) -> Path:
    resolved = Path(os.path.realpath(path))
    try:
        resolved.relative_to(plugin_root)
    except ValueError:
        fail(f"{label} resolves outside {plugin_root}: {resolved}")
    return resolved


def ensure_regular_file(path: Path, plugin_root: Path, label: str) -> None:
    ensure_not_symlink(path, label)
    if not path.is_file():
        fail(f"{label} must be a regular file")
    ensure_contained(path, plugin_root, label)


def ensure_directory(path: Path, plugin_root: Path, label: str) -> None:
    ensure_not_symlink(path, label)
    if not path.is_dir():
        fail(f"{label} must be a directory")
    ensure_contained(path, plugin_root, label)


def schema_version(schema_url: str, label: str) -> str:
    match = SCHEMA_VERSION_RE.search(schema_url)
    if not match:
        fail(f"{label} must use a versioned Agent Plugins schema URL")
    return match.group(1)


def validate_manifest(
    manifest_path: Path,
    plugin_root: Path,
    manifest: object,
    plugin_schema: dict[str, Any],
) -> str:
    if not isinstance(manifest, dict):
        fail(f"{relative(manifest_path)} must be a JSON object")
    name = manifest.get("name")
    if (
        not isinstance(name, str)
        or not (1 <= len(name) <= 64)
        or not PLUGIN_NAME_RE.fullmatch(name)
    ):
        fail(
            f"{relative(manifest_path)}.name must match Agent Plugins naming "
            "requirements (1-64 chars, lowercase letters, digits, '.', '-', "
            "alphanumeric ends, and no '--' or '..')"
        )
    if name != plugin_root.name:
        fail(
            f"{relative(manifest_path)}.name {name!r} must match "
            f"plugin directory {plugin_root.name!r}"
        )

    try:
        jsonschema.validate(manifest, plugin_schema)
    except jsonschema.ValidationError as exc:
        fail(f"{relative(manifest_path)} fails Agent Plugins schema: {exc.message}")

    if manifest.get("$schema") != PLUGIN_SCHEMA_URL:
        fail(f"{relative(manifest_path)}.$schema must equal {PLUGIN_SCHEMA_URL}")

    return name


def validate_skills(plugin_root: Path) -> None:
    skills_dir = plugin_root / "skills"
    if skills_dir.is_symlink():
        fail(f"{relative(skills_dir)} must not be a symlink")
    if not skills_dir.exists():
        return
    ensure_directory(skills_dir, plugin_root, relative(skills_dir))
    for skill_dir in sorted(skills_dir.iterdir(), key=lambda path: path.name):
        if not skill_dir.is_dir():
            continue
        ensure_directory(skill_dir, plugin_root, relative(skill_dir))
        skill_file = skill_dir / "SKILL.md"
        ensure_regular_file(skill_file, plugin_root, relative(skill_file))


def resolve_plugin_path(value: str, plugin_root: Path, label: str) -> None:
    if value.startswith("./"):
        suffix = value[2:]
        candidate = plugin_root / suffix
    elif value.startswith("${PLUGIN_ROOT}"):
        suffix_with_separator = value[len("${PLUGIN_ROOT}") :]
        if suffix_with_separator and not suffix_with_separator.startswith("/"):
            fail(f"{label} uses an invalid ${{PLUGIN_ROOT}} path")
        suffix = value[len("${PLUGIN_ROOT}") :].lstrip("/")
        candidate = plugin_root / suffix
    elif value.startswith("${PLUGIN_DATA}"):
        suffix_with_separator = value[len("${PLUGIN_DATA}") :]
        if suffix_with_separator and not suffix_with_separator.startswith("/"):
            fail(f"{label} uses an invalid ${{PLUGIN_DATA}} path")
        suffix = value[len("${PLUGIN_DATA}") :].lstrip("/")
        # PLUGIN_DATA is runtime-defined. Normalize its suffix against the
        # plugin root so traversal beyond the placeholder root is rejected.
        candidate = plugin_root / suffix
    else:
        fail(
            f"{label} path must start with './', '${{PLUGIN_ROOT}}', or "
            "'${PLUGIN_DATA}'"
        )
    ensure_contained(candidate, plugin_root, label)


def validate_stdio_command(command: str, plugin_root: Path, label: str) -> None:
    """Validate the v1 stdio command grammar and resolve plugin paths."""
    if command.startswith(("./", "${PLUGIN_ROOT}", "${PLUGIN_DATA}")):
        if not command.startswith("./"):
            fail(
                f"{label} must be a bare executable token or a plugin-relative "
                "path beginning with './'; PLUGIN_ROOT/PLUGIN_DATA placeholders "
                "are valid only for cwd"
            )
        if any(char.isspace() for char in command):
            fail(
                f"{label} must be a single executable token; pass arguments "
                "through args instead of command"
            )
        if any(char in SHELL_LIKE_COMMAND_CHARS for char in command):
            fail(f"{label} must not contain shell syntax; pass arguments through args")
        resolve_plugin_path(command, plugin_root, label)
        return

    if command.startswith("/") or WINDOWS_ABSOLUTE_PATH_RE.match(command):
        fail(
            f"{label} must not be an absolute path; use a bare executable token "
            "or a plugin-relative path beginning with './'"
        )
    if command == ".." or command.startswith("../"):
        fail(
            f"{label} must not traverse with '../'; use a plugin-relative path "
            "beginning with './'"
        )
    if any(char.isspace() for char in command):
        fail(
            f"{label} must be a single bare executable token; pass arguments "
            "through args instead of command"
        )
    if "/" in command:
        fail(
            f"{label} paths must begin with './'; bare commands must be executable "
            "tokens without '/'"
        )
    if any(char in SHELL_LIKE_COMMAND_CHARS for char in command):
        fail(f"{label} must not contain shell syntax; pass arguments through args")


def validate_mcp_paths(mcp: dict[str, Any], plugin_root: Path) -> None:
    servers = mcp.get("mcpServers")
    if not isinstance(servers, dict):
        return
    for server_name, server in sorted(servers.items()):
        if not isinstance(server, dict) or "command" not in server:
            continue
        label = f"{relative(plugin_root / 'mcp.json')}.mcpServers[{server_name!r}]"
        command = server["command"]
        if not isinstance(command, str):
            continue
        validate_stdio_command(command, plugin_root, f"{label}.command")
        cwd = server.get("cwd")
        if isinstance(cwd, str):
            resolve_plugin_path(cwd, plugin_root, f"{label}.cwd")


def validate_mcp(plugin_root: Path, mcp_schema: dict[str, Any]) -> None:
    mcp_path = plugin_root / "mcp.json"
    if mcp_path.is_symlink():
        fail(f"{relative(mcp_path)} must not be a symlink")
    if not mcp_path.exists():
        print(f"OK: {relative(plugin_root)} (mcp.json absent; no MCP shipped)")
        return

    ensure_regular_file(mcp_path, plugin_root, relative(mcp_path))
    mcp = load_json(mcp_path)
    try:
        jsonschema.validate(mcp, mcp_schema)
    except jsonschema.ValidationError as exc:
        fail(f"{relative(mcp_path)} fails Agent Plugins MCP schema: {exc.message}")
    if not isinstance(mcp, dict):
        fail(f"{relative(mcp_path)} must be a JSON object")
    if mcp.get("$schema") != MCP_SCHEMA_URL:
        fail(f"{relative(mcp_path)}.$schema must equal {MCP_SCHEMA_URL}")
    validate_mcp_paths(mcp, plugin_root)


def validate_plugin(
    plugin_root: Path,
    plugin_schema: dict[str, Any],
    mcp_schema: dict[str, Any],
) -> None:
    ensure_not_symlink(plugin_root, relative(plugin_root))
    if not plugin_root.is_dir():
        fail(f"{relative(plugin_root)} must be a directory")
    resolved_root = Path(os.path.realpath(plugin_root))
    manifest_path = plugin_root / "plugin.json"
    ensure_regular_file(manifest_path, resolved_root, relative(manifest_path))
    manifest = load_json(manifest_path)
    validate_manifest(manifest_path, resolved_root, manifest, plugin_schema)

    plugin_schema_value = manifest.get("$schema") if isinstance(manifest, dict) else ""
    plugin_version = schema_version(str(plugin_schema_value), relative(manifest_path))
    if plugin_version != "1.0.0":
        fail(f"{relative(manifest_path)} targets unsupported Agent Plugins version")

    validate_skills(plugin_root)
    validate_mcp(plugin_root, mcp_schema)
    mcp_path = plugin_root / "mcp.json"
    if mcp_path.is_file():
        mcp = load_json(mcp_path)
        if isinstance(mcp, dict):
            mcp_version = schema_version(str(mcp.get("$schema", "")), relative(mcp_path))
            if mcp_version != plugin_version:
                fail(
                    f"{relative(mcp_path)} schema version {mcp_version!r} does not "
                    f"match plugin.json version {plugin_version!r}"
                )
    print(f"OK: {relative(manifest_path)}")


def main() -> None:
    plugin_schema = load_schema(PLUGIN_SCHEMA_PATH)
    mcp_schema = load_schema(MCP_SCHEMA_PATH)
    if not PLUGINS_ROOT.is_dir():
        fail("missing plugins/ directory")

    plugin_roots = sorted(
        path for path in PLUGINS_ROOT.iterdir() if path.is_dir() or path.is_symlink()
    )
    manifests = [
        path
        for path in plugin_roots
        if (path / "plugin.json").exists() or (path / "plugin.json").is_symlink()
    ]
    if not manifests:
        fail("no plugins/*/plugin.json manifests found")
    for plugin_root in manifests:
        validate_plugin(plugin_root, plugin_schema, mcp_schema)
    print(f"OK: validated {len(manifests)} Agent Plugins manifest(s)")


if __name__ == "__main__":
    main()
