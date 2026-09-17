> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# FAQ

## Is this only for Claude Code?

No. Production is the [Agent Plugins roster](https://agent-plugins.org/compatible-clients) (VS Code, Copilot, Cursor, ChatGPT/Codex, Kiro, Grok Bot, Hermes, OpenClaw, NanoClaw) **plus** Claude Code.

## How does this differ from `ulises-jeremias/agent-toolkit`?

That project is a broad multi-tool toolkit (CLI, loops, many targets). **This repo** is NaNLABS L1.5 production distribution for Claude, Claude Code, Cursor IDE, Cursor Agent CLI, and GitHub Copilot, with a skills-only packaging path and no consumer CLI/loops compiler.

## Do I need `internal-workstation`?

Not to install public plugins/skills. Yes for NaNLABS machine provisioning and secrets. See [SCOPE.md](SCOPE.md).

## Why no MCP tools after plugin install?

[`mcp/templates/`](../mcp/templates/) are docs-only. Plugins do not install MCP servers.

## Where is `nanlabs-setup`?

Merged into **`nanlabs-core`** (v0.3.0+). Use `/nanlabs-core:setup`.

## Skills-only vs plugins vs packs?

Three different layouts:

| Path | Spec | What you get |
| --- | --- | --- |
| Skills-only / domain packs | [Agent Skills](https://agentskills.io/specification) + `npx skills` | `plugins/nanlabs-<group>/skills/<name>/SKILL.md`. Domain packs are `--skill` aliases. |
| Agent Plugins v1 | [Agent Plugins](https://agent-plugins.org/specification) | Closed root `plugin.json` plus **immediate** `plugins/<id>/skills/<name>/SKILL.md`. Agents are not portable in v1. This repo ships no `mcp.json`. |
| Claude Code / Cursor plugins | Native marketplaces | Agents, commands, hooks, doctor. Native manifests live under `.claude-plugin/` / `.cursor-plugin/`. |

Group packs (`npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills`) match group plugins. See [PACKS.md](PACKS.md). Portable vs native: [AGENT_PLUGINS.md](AGENT_PLUGINS.md).

## How do I share a skill?

Open a GitHub issue with the Propose skill template and a pull request. Maintainers approve; merge makes it installable. See [CONTRIBUTION.md](CONTRIBUTION.md).

## Cursor Agent CLI vs IDE?

Separate runtimes, equal **product** priority. Track evidence in [CURSOR_CLI.md](CURSOR_CLI.md).
