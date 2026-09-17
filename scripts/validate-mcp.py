#!/usr/bin/env python3
"""Validate official MCP catalog, templates, and generated plugin mcp.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("pyyaml required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalogs" / "mcp-catalog.yaml"
TEMPLATES = ROOT / "mcp" / "templates"
PLUGINS = ROOT / "plugins"
AP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
SECRETISH = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|"
    r"AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH )?PRIVATE KEY)",
    re.I,
)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def walk_for_literals(obj: object, path: str = "$") -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk_for_literals(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_for_literals(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        if SECRETISH.search(obj):
            fail(f"{path}: looks like a committed secret literal")
        if re.fullmatch(r"[A-Za-z0-9_\-]{40,}", obj) and "${" not in obj:
            fail(f"{path}: suspicious long opaque string (use ${{ENV}} placeholders)")


def load_catalog() -> dict[str, dict]:
    if not CATALOG.is_file():
        fail(f"missing {CATALOG.relative_to(ROOT)}")
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("mcp-catalog.yaml must be a mapping")
    servers = data.get("servers")
    if not isinstance(servers, dict) or not servers:
        fail("mcp-catalog.yaml servers must be a non-empty mapping")
    return servers


def main() -> None:
    servers = load_catalog()
    templates = sorted(p for p in TEMPLATES.iterdir() if p.is_dir()) if TEMPLATES.is_dir() else []
    template_names = {p.name for p in templates}
    catalog_names = set(servers)

    missing_templates = sorted(catalog_names - template_names)
    extra_templates = sorted(template_names - catalog_names)
    if missing_templates:
        fail(f"mcp/templates missing dirs for catalog servers: {missing_templates}")
    if extra_templates:
        fail(f"mcp/templates dirs not in catalogs/mcp-catalog.yaml: {extra_templates}")

    plugin_urls: dict[str, dict[str, str]] = {}
    for name, cfg in sorted(servers.items()):
        if not isinstance(cfg, dict):
            fail(f"servers.{name} must be a mapping")
        url = cfg.get("url")
        plugin_id = cfg.get("plugin")
        if not isinstance(url, str) or not url.startswith("https://"):
            fail(f"servers.{name}.url must be an https URL")
        if not isinstance(plugin_id, str) or not plugin_id.strip():
            fail(f"servers.{name}.plugin required")
        plugin_urls.setdefault(plugin_id, {})[name] = url

        tmpl = TEMPLATES / name
        cfg_path = tmpl / "config.template.json"
        readme = tmpl / "README.md"
        rel = tmpl.relative_to(ROOT)
        if not cfg_path.is_file():
            fail(f"{rel}: missing config.template.json")
        if not readme.is_file():
            fail(f"{rel}: missing README.md")
        wrapper = tmpl / "wrapper.sh"
        if wrapper.exists():
            fail(f"{wrapper.relative_to(ROOT)}: official servers are remote; do not ship wrappers")
        try:
            data = json.loads(cfg_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{cfg_path.relative_to(ROOT)}: invalid JSON ({exc})")
        if not isinstance(data, dict) or "name" not in data:
            fail(f"{cfg_path.relative_to(ROOT)}: must be object with name")
        if data["name"] != name:
            fail(
                f"{cfg_path.relative_to(ROOT)}: name {data['name']!r} "
                f"must match directory {name!r}"
            )
        if data.get("url") != url:
            fail(
                f"{cfg_path.relative_to(ROOT)}: url {data.get('url')!r} "
                f"must match catalog {url!r}"
            )
        if data.get("type") != "streamable-http":
            fail(f"{cfg_path.relative_to(ROOT)}: type must be streamable-http")
        walk_for_literals(data)
        print(f"OK: {rel}")

    for plugin_id, urls in sorted(plugin_urls.items()):
        mcp_path = PLUGINS / plugin_id / "mcp.json"
        if not mcp_path.is_file():
            fail(f"missing {mcp_path.relative_to(ROOT)} — run scripts/gen-surfaces.py")
        mcp = json.loads(mcp_path.read_text(encoding="utf-8"))
        walk_for_literals(mcp)
        if mcp.get("$schema") != AP_SCHEMA:
            fail(f"{mcp_path.relative_to(ROOT)}.$schema must equal {AP_SCHEMA}")
        shipped = mcp.get("mcpServers")
        if not isinstance(shipped, dict):
            fail(f"{mcp_path.relative_to(ROOT)}: mcpServers must be an object")
        expected = set(urls)
        actual = set(shipped)
        if expected != actual:
            fail(
                f"{mcp_path.relative_to(ROOT)} servers {sorted(actual)} "
                f"!= catalog {sorted(expected)}"
            )
        for server_name, url in urls.items():
            entry = shipped[server_name]
            if not isinstance(entry, dict):
                fail(f"{mcp_path.relative_to(ROOT)}.{server_name} must be an object")
            if entry.get("type") != "streamable-http":
                fail(f"{mcp_path.relative_to(ROOT)}.{server_name}.type must be streamable-http")
            if entry.get("url") != url:
                fail(
                    f"{mcp_path.relative_to(ROOT)}.{server_name}.url "
                    f"{entry.get('url')!r} != catalog {url!r}"
                )
            if "headers" in entry:
                fail(
                    f"{mcp_path.relative_to(ROOT)}.{server_name}: headers are not allowed "
                    "(auth is client-managed; no secrets in plugins)"
                )
        print(f"OK: {mcp_path.relative_to(ROOT)}")

    print(f"OK: validated {len(servers)} official MCP server(s)")


if __name__ == "__main__":
    main()
