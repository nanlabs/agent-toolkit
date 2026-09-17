> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Scope

NaNLABS production distribution for AI coding assistants — **smaller** than multi-tool personal forks (no consumer CLI, no loop runtime, no 6-IDE profile compiler).

## Production surfaces

| Surface | Support |
| --- | --- |
| VS Code | Agent Plugins marketplace / from-source folders |
| GitHub Copilot | CLI `OWNER/REPO:PATH` + VS Code Copilot agents |
| Cursor IDE / Agent CLI | Native marketplace + `--plugin-dir` |
| ChatGPT & Codex | `.agents/plugins/marketplace.json` + Claude/Cursor catalogs |
| Kiro | Folder import of `plugins/nanlabs-*` |
| Grok Bot, Hermes, OpenClaw, NanoClaw | Agent Plugins plugin directory |
| Claude Code | Native `.claude-plugin/` marketplace (not on the AP roster) |
| `npx skills` | Skills-only from `plugins/nanlabs-<group>/skills` |

## In scope

- Agent Skills under `plugins/nanlabs-<group>/skills/<name>/`
- Agent personas (`agents/`) + generated plugin agent files (`gen-surfaces`)
- Nine group plugins plus optional `nanlabs-agents`
- Agent Plugins v1.0.0 portable manifests; Copilot `com.github.copilot/agents/`
- `nanlabs-pyrightination` as a report-only typing skill in `nanlabs-core`
- Official hosted MCP servers in group plugins (`mcp.json` / `.mcp.json`)
- CI validators, contracts, catalogs (including domain packs), release policy docs
- Contribution flow for proposing skills via GitHub pull request
- Domain packs (`catalogs/pack-catalog.yaml`) as `npx skills --skill` aliases

## Out of scope (plugin targets)

Gemini, Antigravity, OpenCode, Windsurf, Pi, etc. Portable skills may still work via `npx skills`.

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
