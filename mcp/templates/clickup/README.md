# ClickUp MCP template (legacy stub)

> **Deprecated for new setups** — Prefer the [`clickup` CLI](https://triptechtravel.github.io/clickup-cli/) and the `clickup-cli` skill in this repo (`skills/` catalog) over the ClickUp MCP server.

This directory keeps a **legacy** config stub for reference only. Public-safe: env placeholders only.

## Why the CLI is preferred

| | ClickUp MCP | `clickup` CLI |
| --- | --- | --- |
| Token cost | High — verbose JSON blobs | Lower — structured `--json` / `--jq` |
| Auth | Server process + API token in config | Keyring / `--with-token` for CI |
| Git integration | None | Task IDs from branch names |
| Maintenance | External daemon | Single binary |

## Legacy environment variables

| Variable | Purpose |
| --- | --- |
| `CLICKUP_API_TOKEN` | ClickUp personal API token (legacy MCP only) |

## Usage (legacy only)

1. Prefer installing the CLI and the `clickup-cli` skill instead of this MCP.
2. If you must use the MCP: copy `config.template.json`, export `CLICKUP_API_TOKEN`, optionally run `./wrapper.sh`.
3. Never commit the token.

## Provenance

Adapted from `nanlabs/internal-workstation` MCP templates for public distribution in `agent-toolkit`.
