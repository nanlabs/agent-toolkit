# MCP templates

Public MCP config **stubs** — env-var placeholders only. Never commit tokens, PATs, or private hosts.

Machine-readable index: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml).

## Bundled (6)

| Template | Path | Required env | Notes |
| --- | --- | --- | --- |
| GitHub | `mcp/templates/github/` | `GITHUB_TOKEN` | Local command + wrapper |
| Notion | `mcp/templates/notion/` | `NOTION_API_TOKEN` | Local command + wrapper |
| Slack | `mcp/templates/slack/` | `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN` | Local command + wrapper |
| Figma | `mcp/templates/figma/` | `FIGMA_OAUTH_TOKEN`, `FIGMA_REGION` | Remote streamable HTTP |
| Linear | `mcp/templates/linear/` | _(OAuth)_ | Remote streamable HTTP |
| ClickUp | `mcp/templates/clickup/` | `CLICKUP_API_TOKEN` | **Legacy** — prefer `clickup-cli` skill |

Each stub includes:

- `config.template.json` — client-agnostic shape with `${ENV_VAR}` substitution
- `README.md` — how to wire it
- Optional `wrapper.sh` — local launcher example

## Rules

1. Secrets stay in the environment or a secret manager — not in git.
2. Prefer least-privilege tokens.
3. Document every required variable in the template README.

See [`docs/PUBLIC_CONTENT_POLICY.md`](../../docs/PUBLIC_CONTENT_POLICY.md).
