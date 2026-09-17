# 🎯 Scope

What this repository **is** and **is not**. Inspired by broader agent-toolkit ecosystems, but intentionally smaller for NaNLABS production use.

## In scope (production surfaces)

| Surface | Role |
| --- | --- |
| Agent Plugins roster | VS Code, Copilot, Cursor, ChatGPT/Codex, Kiro, Grok Bot, Hermes, OpenClaw, NanoClaw |
| Claude Code | Native marketplace (not on the AP roster) |

## In scope (content)

- Agent Skills (`SKILL.md`) under `plugins/nanlabs-<group>/skills/`
- Agent personas under `agents/`
- Nine group plugins plus optional `nanlabs-agents`
- GitHub Copilot CLI manifests + `.github/` repository surface
- `nanlabs-pyrightination` as a report-only typing skill in `nanlabs-core`
- Official hosted MCP servers (`mcp.json` on design / forge / integrations)
- Validation scripts + CI gates
- Domain pack catalog (`catalogs/pack-catalog.yaml`) and GitHub contribution flow
- Dependency contracts for setup/doctor

## Explicitly out of scope (plugin targets)

OpenCode, Windsurf, Gemini CLI, Pi, and similar — portable skills may still work via `npx skills`; we do **not** maintain plugin/profile targets for them.

## Explicitly out of scope (product features)

Compared to larger personal forks, NaNLABS **does not** ship here:

- Consumer CLI (`agent-toolkit install` / multi-tool compiler)
- Loop engineering runtime / scheduled loops
- Multi-tool profile matrix (6+ IDEs)
- Org RAG / telemetry backends (L1 / Part III)
- Workstation provisioning (chezmoi) — that stays in `internal-workstation`

## Layers

| Layer | Repo | Owns |
| --- | --- | --- |
| L1 | `internal-workstation` | OS tools, secrets (`env.d`), doctor fleet, machine identity |
| L1.5 | **this repo** | Public skills, agents, plugins, MCP stubs, catalogs |

Dual-rail until workstation cutover (Waves 3–4). See epic tracking on [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12).
