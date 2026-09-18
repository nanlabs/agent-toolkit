# Installation

Canonical long-form: [`docs/ADOPTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/ADOPTION.md) · complete copy-paste: [Plugin marketplace](Plugin-Marketplace) · lifecycle: [Lifecycle](Lifecycle).

Production = [Agent Plugins roster](https://agent-plugins.org/compatible-clients) **plus** Claude Code.

## Prerequisites

- **git** (clone / marketplace fetch)
- At least one target client
- For skills-only: **Node.js** + `npx`
- For local validation (maintainers): **Python 3.10+**

## Complete install

The generated plugin list and copy-paste blocks live on [Plugin marketplace](Plugin-Marketplace). They are assembled from [`products/plugins.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/products/plugins.yaml).

Recommended first plugin: **`nanlabs-core`**. Then install the other group plugins. Optional: **`nanlabs-agents`**.

After Claude Code install, run **`/nanlabs-core:setup`**.

## Cursor IDE

1. **Local:** symlink each `plugins/nanlabs-*` under `~/.cursor/plugins/local/` and reload (see [Plugin marketplace](Plugin-Marketplace)).
2. **Team:** org admin imports `nanlabs/agent-toolkit` as a Team Marketplace.

See [Cursor plugins](https://cursor.com/docs/plugins).

## Cursor Agent CLI

Equal product priority with Cursor IDE.

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

`marketplace add` registers the catalog; it does not install a plugin. Parity matrix: [Cursor Agent CLI](Cursor-Agent-CLI).

## Other clients

| Client | How |
| --- | --- |
| VS Code | `"chat.plugins.marketplaces": ["nanlabs/agent-toolkit"]` then install each `nanlabs-*` |
| ChatGPT / Codex | `codex plugin marketplace add nanlabs/agent-toolkit` |
| Kiro | Powers → Import from folder → `plugins/nanlabs-<group>` (not repo root) |
| Grok / Hermes / OpenClaw / NanoClaw | Point at `plugins/nanlabs-<group>/` |

## Skills-only

```bash
npx skills add nanlabs/agent-toolkit -g
```

Does **not** install plugins, agents, MCP, or `/nanlabs-core:setup`. Packs: [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md).

## MCP

Install `nanlabs-design`, `nanlabs-forge`, and/or `nanlabs-integrations`, reload, complete OAuth. Details: [Official MCP](MCP-Setup).

## Verify

| Path | Check |
| --- | --- |
| Claude Code | Ask “what NaNLABS skills are available?” after `nanlabs-core` |
| Cursor IDE | Skills / MCP discoverable after local or team install |
| Copilot CLI | `copilot plugin list` shows `nanlabs-*` |
| Skills-only | `npx skills check` lists nested skills |
