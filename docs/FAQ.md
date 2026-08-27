> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-27**
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

## Skills-only vs plugins?

Skills-only installs skills alone. Plugins add agents, commands, and the bundled setup doctor. Neither path installs MCP.

## Cursor Agent CLI vs IDE?

Separate runtimes, equal **product** priority. Track evidence in [CURSOR_CLI.md](CURSOR_CLI.md).
