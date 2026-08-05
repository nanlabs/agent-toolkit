# Scope

What this repository **is** and **is not**. Inspired by broader agent-toolkit ecosystems, but intentionally smaller for NaNLABS production use.

## In scope (equal priority)

| Surface | Role |
| --- | --- |
| Claude | Skills where plugins are unavailable |
| Claude Code | Marketplace plugins + skills |
| Cursor IDE | Plugins (local / team marketplace) |
| Cursor Agent CLI | Same priority; certify via matrix (`docs/CURSOR_CLI.md`) |

## In scope (content)

- Agent Skills (`SKILL.md`) under `skills/<group>/`
- Agent personas under `agents/`
- Claude + Cursor plugin bundles (`nanlabs-core`, `nanlabs-agents`)
- MCP **templates** (docs-only stubs)
- Validation scripts + CI gates
- Dependency contracts for setup/doctor

## Explicitly out of scope (plugin targets)

OpenCode, GitHub Copilot, Windsurf, Gemini CLI, Pi, and similar — portable skills may still work via `npx skills`; we do **not** maintain plugin/profile targets for them.

## Explicitly out of scope (product features)

Compared to larger personal forks, NaNLABS **does not** ship here:

- Consumer CLI (`agent-toolkit install` / multi-tool compiler)
- Loop engineering runtime / scheduled loops
- Multi-tool profile matrix (6+ IDEs)
- Forge-as-separate marketplace plugin (forge skills live in the skills tree)
- Org RAG / telemetry backends (L1 / Part III)
- Workstation provisioning (chezmoi) — that stays in `internal-workstation`

## Layers

| Layer | Repo | Owns |
| --- | --- | --- |
| L1 | `internal-workstation` | OS tools, secrets (`env.d`), doctor fleet, machine identity |
| L1.5 | **this repo** | Public skills, agents, plugins, MCP stubs, catalogs |

Dual-rail until workstation cutover (Waves 3–4). See epic tracking on [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12).
