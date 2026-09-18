# nanlabs-design

Figma MCP and UI/UX intelligence (not a full designer workflow)

Canonical skills live under `skills/<name>/` (layout group `design`). There is no second tree under `skills/<group>/`.

## Skills

`figma`, `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-implement-design`, `ui-ux-pro-max`

## MCP

Official hosted MCP servers ship in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). After install, authenticate in the client. No tokens are stored in the plugin.

- `figma` — `https://mcp.figma.com/mcp`

Catalog: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml) · [MCP setup](../../docs/wiki/MCP-Setup.md).

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-design@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-design
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-design ~/.cursor/plugins/local/nanlabs-design
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-design
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-design` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
