# Linear MCP template (stub)

Connects an AI client to Linear via the official remote MCP server
(`https://mcp.linear.app/mcp`, OAuth — no API token in this stub).

## Required environment variables

None for the default OAuth path. Authentication is prompted by the AI client on first call.

## Usage

Transport is **streamable HTTP** — there is no local `command` / `wrapper.sh` for the primary path.

1. Copy the URL / auth shape from `config.template.json` into your client MCP config.
2. Restart the AI client.
3. The first Linear tool call should open an OAuth window; the session is cached by the client.

| AI tool | Typical config path |
| --- | --- |
| Claude Code | `~/.claude/mcp.json` |
| Cursor | `~/.cursor/mcp.json` |
| OpenCode | `~/.config/opencode/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |

`config.template.json` also documents an optional Windows/WSL `mcp-remote` fallback under `_comment_windows_wsl_fallback` (not active by default).

## Provenance

Adapted from `nanlabs/internal-workstation` MCP templates for public distribution in `agent-toolkit`.
