# Scope

What this repository **is** and **is not**. Intentionally smaller than multi-tool personal forks.

## In scope (clients)

| Surface | Role |
| --- | --- |
| Agent Plugins roster | VS Code, Copilot, Cursor, ChatGPT/Codex, Kiro, Grok Bot, Hermes, OpenClaw, NanoClaw |
| Claude Code | Native marketplace (not on the AP roster) |
| `npx skills` | Skills-only from `plugins/nanlabs-<group>/skills` |

## In scope (content)

- Agent Skills under `plugins/nanlabs-<group>/skills/`
- Agent personas under `agents/`
- Group plugins plus optional `nanlabs-agents`
- Official hosted MCP (`mcp.json` / `.mcp.json` on design, forge, integrations)
- GitHub Copilot CLI manifests + `.github/` repository surface
- Validation scripts, catalogs, contribution flow

## Out of scope (plugin targets)

OpenCode, Windsurf, Gemini CLI, Pi, and similar — portable skills may still work via `npx skills`.

## Out of scope (product)

- Consumer CLI / multi-target compiler
- Loop engineering runtime
- Org RAG / telemetry backends
- Workstation provisioning (chezmoi) — `internal-workstation`

## Layers

| Layer | Repo | Owns |
| --- | --- | --- |
| L1 | `internal-workstation` (private) | OS tools, secrets, doctor fleet |
| L1.5 | **this repo** (public) | Skills, agents, plugins, official MCP, catalogs |
