# MCP templates

Official hosted MCP endpoints, documented here and **shipped** in the matching
group plugin (`mcp.json` + `.mcp.json`). Source of truth:
[`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml).

Installing `nanlabs-design`, `nanlabs-forge`, or `nanlabs-integrations`
registers these servers. The user authenticates in the client (OAuth). Plugins
never contain tokens.

| Server | Plugin | Official URL |
| --- | --- | --- |
| Atlassian (Jira + Confluence) | `nanlabs-integrations` | `https://mcp.atlassian.com/v2/mcp` |
| ClickUp | `nanlabs-integrations` | `https://mcp.clickup.com/mcp` |
| Slack | `nanlabs-integrations` | `https://mcp.slack.com/mcp` |
| Linear | `nanlabs-integrations` | `https://mcp.linear.app/mcp` |
| Shortcut | `nanlabs-integrations` | `https://mcp.shortcut.com/mcp` |
| Notion | `nanlabs-integrations` | `https://mcp.notion.com/mcp` |
| GitHub | `nanlabs-forge` | `https://api.githubcopilot.com/mcp/` |
| GitLab.com | `nanlabs-forge` | `https://gitlab.com/api/v4/mcp` |
| Figma | `nanlabs-design` | `https://mcp.figma.com/mcp` |

Agent Plugins portable config uses `type: streamable-http`. Claude Code native
`.mcp.json` uses `type: http` with the same URL. Auth is client-managed — see
[Agent Plugins MCP](https://agent-plugins.org/plugin-authors/mcp-servers).

Skills-only (`npx skills`) does **not** install MCP. `clickup-cli` / `gh` remain
available as CLI alternatives.
