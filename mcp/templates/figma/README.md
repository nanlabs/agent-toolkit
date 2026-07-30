# Figma MCP template (stub)

Connects an AI client to the remote Figma MCP server
(`https://mcp.figma.com/mcp`, streamable HTTP with bearer-token auth).

Public-safe stub. **No secrets** — use env-var substitution only.

## Required environment variables

| Variable | Purpose |
| --- | --- |
| `FIGMA_OAUTH_TOKEN` | Personal access token or OAuth token (read + assets scopes) |
| `FIGMA_REGION` | Figma region header (default `us-east-1`) |

Store tokens in a local env file outside git (mode `600`). Never commit tokens or paste quoted values from the Figma UI with surrounding quotes.

## Usage

Transport is **streamable HTTP** — there is no local `command` / `wrapper.sh`.

1. Copy values from `config.template.json` into your client MCP config.
2. Substitute `${FIGMA_OAUTH_TOKEN}` and `${FIGMA_REGION}` from the environment.
3. Restart the AI client so it reloads MCP config.
4. Call `whoami` on the Figma MCP to verify identity.

| AI tool | Typical config path |
| --- | --- |
| Claude Code | `~/.claude/mcp.json` |
| Cursor | `~/.cursor/mcp.json` |
| OpenCode | `~/.config/opencode/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |

## Related

- `figma` / `figma-*` skills under `skills/` (see `catalogs/skill-catalog.yaml`)

## Provenance

Adapted from `nanlabs/internal-workstation` MCP templates for public distribution in `agent-toolkit`.
