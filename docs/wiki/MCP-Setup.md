# 🔗 MCP templates

Templates live under [`mcp/templates/`](https://github.com/nanlabs/agent-toolkit/tree/main/mcp/templates).

**Important:** these are **docs-only**. Installing `nanlabs-core` / `nanlabs-agents` does **not** register MCP servers.

## Providers (stubs)

Typical set (see repo for current list): GitHub, Slack, Linear, Notion, Figma, ClickUp — each with env placeholders only. Never commit tokens.

## How to use

1. Copy a template into your client’s MCP config path.
2. Replace `${ENV_VAR}` placeholders via local env / `env.d` (workstation) — not git.
3. Restart the client and verify tools appear.

GitHub stub uses the official `npx @modelcontextprotocol/server-github` pattern with `GITHUB_PERSONAL_ACCESS_TOKEN`.
