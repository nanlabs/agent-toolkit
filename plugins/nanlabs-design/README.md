# nanlabs-design

Figma MCP and UI/UX intelligence (not a full designer workflow)

Canonical skills live under `skills/<name>/` (layout group `design`). There is no second tree under `skills/<group>/`.

## MCP

Official hosted MCP servers ship in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). After install, authenticate in the client. No tokens are stored in the plugin.

- `figma` — `https://mcp.figma.com/mcp`

Catalog and docs: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml), [`docs/wiki/MCP-Setup.md`](../../docs/wiki/MCP-Setup.md).

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-design@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-design
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-design
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-design` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
