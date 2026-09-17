# nanlabs-integrations

ClickUp, Slack, Linear, Shortcut, Notion, and Atlassian (Jira/Confluence) MCP plus CLI skills

Canonical skills live under `skills/<name>/` (layout group `integrations`). There is no second tree under `skills/<group>/`.

## MCP

Official hosted MCP servers ship in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). After install, authenticate in the client. No tokens are stored in the plugin.

- `atlassian` — `https://mcp.atlassian.com/v2/mcp`
- `clickup` — `https://mcp.clickup.com/mcp`
- `linear` — `https://mcp.linear.app/mcp`
- `notion` — `https://mcp.notion.com/mcp`
- `shortcut` — `https://mcp.shortcut.com/mcp`
- `slack` — `https://mcp.slack.com/mcp`

Catalog and docs: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml), [`docs/wiki/MCP-Setup.md`](../../docs/wiki/MCP-Setup.md).

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-integrations@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-integrations
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-integrations
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-integrations` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
