#!/usr/bin/env python3
"""Validate Claude + Cursor marketplace/plugin manifests for agent-toolkit.

Cursor manifests are checked against pinned official schemas under
schemas/cursor/ (from cursor/plugins). Claude checks remain structural.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

try:
    import jsonschema
except ImportError:  # pragma: no cover
    print(
        "ERROR: jsonschema is required. Install with: pip install jsonschema",
        file=sys.stderr,
    )
    raise SystemExit(1)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def expect_dict(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def expect_str(obj: dict, key: str, label: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}.{key} must be a non-empty string")
    return value


def validate_claude_marketplace() -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    data = expect_dict(load_json(path), str(path.relative_to(ROOT)))
    expect_str(data, "name", "claude marketplace")
    owner = expect_dict(data.get("owner"), "claude marketplace.owner")
    expect_str(owner, "name", "claude marketplace.owner")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("claude marketplace.plugins must be a non-empty array")
    for idx, entry in enumerate(plugins):
        plugin = expect_dict(entry, f"claude marketplace.plugins[{idx}]")
        name = expect_str(plugin, "name", f"claude marketplace.plugins[{idx}]")
        source = expect_str(plugin, "source", f"claude marketplace.plugins[{idx}]")
        source_path = (ROOT / source).resolve()
        if not source_path.is_dir():
            fail(f"claude plugin source missing for {name}: {source}")
        manifest = source_path / ".claude-plugin" / "plugin.json"
        plugin_data = expect_dict(load_json(manifest), str(manifest.relative_to(ROOT)))
        expect_str(plugin_data, "name", str(manifest.relative_to(ROOT)))
        if plugin_data["name"] != name:
            fail(
                f"claude plugin name mismatch: marketplace={name} "
                f"plugin.json={plugin_data['name']}"
            )


def validate_cursor_official_schemas() -> None:
    marketplace_schema = expect_dict(
        load_json(ROOT / "schemas" / "cursor" / "marketplace.schema.json"),
        "schemas/cursor/marketplace.schema.json",
    )
    plugin_schema = expect_dict(
        load_json(ROOT / "schemas" / "cursor" / "plugin.schema.json"),
        "schemas/cursor/plugin.schema.json",
    )
    marketplace_path = ROOT / ".cursor-plugin" / "marketplace.json"
    marketplace = load_json(marketplace_path)
    try:
        jsonschema.validate(marketplace, marketplace_schema)
    except jsonschema.ValidationError as exc:
        fail(
            f"Cursor marketplace fails official schema "
            f"({marketplace_path.relative_to(ROOT)}): {exc.message}"
        )

    data = expect_dict(marketplace, str(marketplace_path.relative_to(ROOT)))
    expect_str(data, "name", "cursor marketplace")
    metadata = expect_dict(data.get("metadata") or {}, "cursor marketplace.metadata")
    plugin_root = metadata.get("pluginRoot", "plugins")
    if not isinstance(plugin_root, str):
        fail("cursor marketplace.metadata.pluginRoot must be a string when set")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("cursor marketplace.plugins must be a non-empty array")
    for idx, entry in enumerate(plugins):
        plugin = expect_dict(entry, f"cursor marketplace.plugins[{idx}]")
        name = expect_str(plugin, "name", f"cursor marketplace.plugins[{idx}]")
        source = expect_str(plugin, "source", f"cursor marketplace.plugins[{idx}]")
        source_path = (ROOT / plugin_root / source).resolve()
        if not source_path.is_dir():
            fail(f"cursor plugin source missing for {name}: {plugin_root}/{source}")
        manifest = source_path / ".cursor-plugin" / "plugin.json"
        plugin_data = load_json(manifest)
        try:
            jsonschema.validate(plugin_data, plugin_schema)
        except jsonschema.ValidationError as exc:
            fail(
                f"Cursor plugin.json fails official schema "
                f"({manifest.relative_to(ROOT)}): {exc.message}"
            )
        plugin_obj = expect_dict(plugin_data, str(manifest.relative_to(ROOT)))
        expect_str(plugin_obj, "name", str(manifest.relative_to(ROOT)))
        if plugin_obj["name"] != name:
            fail(
                f"cursor plugin name mismatch: marketplace={name} "
                f"plugin.json={plugin_obj['name']}"
            )


def main() -> None:
    validate_claude_marketplace()
    validate_cursor_official_schemas()
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate-copilot-manifests.py")],
        check=True,
    )
    print(
        "OK: marketplace and plugin manifests validated "
        "(Claude, Cursor, and Copilot surfaces)"
    )


if __name__ == "__main__":
    main()
