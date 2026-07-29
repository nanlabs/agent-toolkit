#!/usr/bin/env python3
"""Validate Claude + Cursor marketplace/plugin manifests for agent-toolkit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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


def validate_cursor_marketplace() -> None:
    path = ROOT / ".cursor-plugin" / "marketplace.json"
    data = expect_dict(load_json(path), str(path.relative_to(ROOT)))
    expect_str(data, "name", "cursor marketplace")
    owner = expect_dict(data.get("owner"), "cursor marketplace.owner")
    expect_str(owner, "name", "cursor marketplace.owner")
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
        plugin_data = expect_dict(load_json(manifest), str(manifest.relative_to(ROOT)))
        expect_str(plugin_data, "name", str(manifest.relative_to(ROOT)))
        if plugin_data["name"] != name:
            fail(
                f"cursor plugin name mismatch: marketplace={name} "
                f"plugin.json={plugin_data['name']}"
            )


def main() -> None:
    validate_claude_marketplace()
    validate_cursor_marketplace()
    print("OK: marketplace and plugin manifests validated")


if __name__ == "__main__":
    main()
