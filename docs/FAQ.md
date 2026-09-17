> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# FAQ

## Is this only for Claude Code?

No. Equal priority: **Claude · Claude Code · Cursor IDE · Cursor Agent CLI · GitHub Copilot**.

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
| Skills-only / packs | [Agent Skills](https://agentskills.io/specification) + `npx skills` | Nested `skills/<group>/<name>/SKILL.md`. Packs are catalog aliases, not packages. |
| Agent Plugins v1 | [Agent Plugins](https://agent-plugins.org/specification) | Closed root `plugin.json` plus **immediate** `plugins/<id>/skills/<name>/SKILL.md`. Agents are not portable in v1. This repo ships no `mcp.json`. |
| Claude Code / Cursor plugins | Native marketplaces | Agents, commands, hooks, doctor. Native manifests live under `.claude-plugin/` / `.cursor-plugin/`. |

Domain packs (`npx skills add nanlabs/agent-toolkit/skills/delivery`) are documented in [PACKS.md](PACKS.md). Portable vs native plugins: [AGENT_PLUGINS.md](AGENT_PLUGINS.md).

## How do I share a skill?

Open a GitHub issue with the Propose skill template and a pull request. Maintainers approve; merge makes it installable. See [CONTRIBUTION.md](CONTRIBUTION.md).

## Cursor Agent CLI vs IDE?

Separate runtimes, equal **product** priority. Track evidence in [CURSOR_CLI.md](CURSOR_CLI.md).
