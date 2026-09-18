# nanlabs-integrations

ClickUp, Slack, Linear, Shortcut, Notion, and Atlassian (Jira/Confluence) MCP plus CLI skills

Canonical skills live under `skills/<name>/` (layout group `integrations`). There is no second tree under `skills/<group>/`.

## Skills

`clickup-cli`, `linear`, `nan-slack-assistant`, `slack-cli`

## MCP

Official hosted MCP servers ship in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). After install, authenticate in the client. No tokens are stored in the plugin.

- `atlassian` — `https://mcp.atlassian.com/v2/mcp`
- `clickup` — `https://mcp.clickup.com/mcp`
- `linear` — `https://mcp.linear.app/mcp`
- `notion` — `https://mcp.notion.com/mcp`
- `shortcut` — `https://mcp.shortcut.com/mcp`
- `slack` — `https://mcp.slack.com/mcp`

Catalog: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml) · [MCP setup](../../docs/wiki/MCP-Setup.md).

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-integrations@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-integrations
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-integrations ~/.cursor/plugins/local/nanlabs-integrations
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-integrations
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-integrations` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
