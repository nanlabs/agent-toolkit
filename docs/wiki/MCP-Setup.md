# Official MCP servers

Catalog: [`catalogs/mcp-catalog.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/catalogs/mcp-catalog.yaml).
Templates: [`mcp/templates/`](https://github.com/nanlabs/agent-toolkit/tree/main/mcp/templates).

Installing **`nanlabs-design`**, **`nanlabs-forge`**, or **`nanlabs-integrations`** registers these hosted servers. Authenticate in the client (OAuth). Plugins never contain tokens.

`nanlabs-core` / `nanlabs-agents` do **not** ship MCP. Skills-only (`npx skills`) does not either.

## What ships where

| Server | Plugin | Official URL | Auth |
| --- | --- | --- | --- |
| Atlassian (Jira + Confluence) | `nanlabs-integrations` | `https://mcp.atlassian.com/v2/mcp` | OAuth 2.1 |
| ClickUp | `nanlabs-integrations` | `https://mcp.clickup.com/mcp` | OAuth (no API tokens) |
| Slack | `nanlabs-integrations` | `https://mcp.slack.com/mcp` | OAuth; no DCR — admin approval |
| Linear | `nanlabs-integrations` | `https://mcp.linear.app/mcp` | OAuth 2.1 |
| Shortcut | `nanlabs-integrations` | `https://mcp.shortcut.com/mcp` | OAuth |
| Notion | `nanlabs-integrations` | `https://mcp.notion.com/mcp` | OAuth |
| GitHub | `nanlabs-forge` | `https://api.githubcopilot.com/mcp/` | OAuth (some Cursor setups still use a user PAT) |
| GitLab.com | `nanlabs-forge` | `https://gitlab.com/api/v4/mcp` | OAuth / DCR |
| Figma | `nanlabs-design` | `https://mcp.figma.com/mcp` | OAuth; client allowlist |

Jira and Confluence are **one** Atlassian Rovo MCP, not two URLs.

## Client files

| Client | File | Transport field |
| --- | --- | --- |
| Agent Plugins / Cursor / Copilot | `plugins/<id>/mcp.json` | `type: streamable-http` |
| Claude Code | `plugins/<id>/.mcp.json` | `type: http` |

After install: reload the client, then complete the browser OAuth prompt. Slack workspace admins must approve MCP; if URL-only OAuth fails, use Slack’s own MCP plugin for that client.

Official vendor docs:

- [ClickUp](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1)
- [Shortcut](https://www.shortcut.com/help/integrations/mcp-server/)
- [Linear](https://linear.app/docs/mcp)
- [Atlassian Rovo](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/)
- [Notion](https://developers.notion.com/guides/mcp/get-started-with-mcp)
- [Slack](https://docs.slack.dev/ai/slack-mcp-server/)
- [GitHub](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- [GitLab](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)
- [Figma](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
