# nanlabs-forge

GitHub and GitLab CLI automation plus official GitHub and GitLab MCP

Canonical skills live under `skills/<name>/` (layout group `forge`). There is no second tree under `skills/<group>/`.

## MCP

Official hosted MCP servers ship in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). After install, authenticate in the client. No tokens are stored in the plugin.

- `github` — `https://api.githubcopilot.com/mcp/`
- `gitlab` — `https://gitlab.com/api/v4/mcp`

Catalog and docs: [`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml), [`docs/wiki/MCP-Setup.md`](../../docs/wiki/MCP-Setup.md).

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-forge@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-forge
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-forge
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-forge` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
