> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-05**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Scope

NaNLABS production distribution for AI coding assistants — **smaller** than multi-tool personal forks (no consumer CLI, no loop runtime, no 6-IDE profile compiler).

## Equal-priority surfaces

| Surface | Support |
| --- | --- |
| Claude | Skills path where plugins unavailable |
| Claude Code | Marketplace plugins + skills |
| Cursor IDE | Plugins (local / team marketplace) |
| Cursor Agent CLI | Equal priority; certify in [CURSOR_CLI.md](CURSOR_CLI.md) |

## In scope

- Agent Skills (`skills/<group>/`)
- Agent personas (`agents/`) + flat plugin assembly (`gen-surfaces`)
- Plugins: `nanlabs-core`, `nanlabs-agents`
- MCP **docs-only** templates
- CI validators, contracts, catalogs, release policy docs

## Out of scope (plugin targets)

OpenCode, GitHub Copilot, Windsurf, Gemini CLI, Pi, etc. Portable skills may still work via `npx skills`.

## Out of scope (product)

- Consumer CLI / multi-target compiler
- Loop engineering runtime / scheduled loops
- Org RAG / telemetry backends (L1 / Part III)
- Workstation chezmoi provisioning (`internal-workstation`)

## Layers

| Layer | Repo |
| --- | --- |
| L1 provisioner | `nanlabs/internal-workstation` |
| L1.5 content | **this repository** |

See also: [FAQ.md](FAQ.md) · wiki Scope page (after wiki sync merges).
