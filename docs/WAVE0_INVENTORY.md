# Wave 0 inventory — agent-toolkit

Snapshot for H0 (baseline decisions). Living document; update when slices change.

## Path ownership

| Path | Owner layer | Notes |
| --- | --- | --- |
| `skills/` | L1.5 (this repo) | Agent Skills canonical tree |
| `agents/` | L1.5 | Personas; mirrored to `plugins/nanlabs-agents` via `gen-surfaces` |
| `mcp/templates/` | L1.5 | Public stubs only |
| `plugins/` | L1.5 | Claude/Cursor bundles |
| `contracts/` | L1.5 | Dependency/permission contracts for setup |
| `catalogs/` | L1.5 | Skill / agent / MCP indexes |
| `internal-workstation` AI home paths | L1 | Until cutover; copy-forward only so far |
| Secrets / `env.d` | L1 | Never in this repo |

## Privacy classification (corpus)

| Class | Examples | Where it lives |
| --- | --- | --- |
| **Public** | Generic skills, agents, MCP stubs, setup/core plugins | `agent-toolkit` |
| **Internal process** | ClickUp procedure corpus (`nanlabs-tech-assistant` skill) | Workstation only (for now) |
| **Client / NDA** | Client packs, credentials, private URLs | L2 / L3 overlays — never public |
| **Machine secret** | Tokens, PATs | L1 env — names only in contracts/MCP stubs |

## Acceptance / rollback triggers

| Gate | Pass | Rollback trigger |
| --- | --- | --- |
| Secret scan + validators | CI green on `main` | Revert merge; rotate any leaked credential |
| Public scrub | Policy checklist on PR | Remove content; keep on workstation |
| Pilot install (#8/#9) | Documented smoke | Pin previous plugin version; disable marketplace auto-update |
| Cutover (#23) | L1.5 SoT confirmed | Keep dual-rail; do not delete workstation yet |

## H0 unresolved → proposed resolutions

| Choice | Resolution |
| --- | --- |
| Repo name | Keep **`nanlabs/agent-toolkit`** |
| Visibility | **Public** + scrub policy |
| Slices | Skills → agents/MCP → plugins → contracts (done through Wave 1 foundation) |
| Telemetry boundary | L1 policy; L1.5 adapters later — no endpoints/keys here |
| Knowledge RAG | Post-cutover / Part III |
| Private companion marketplace | **Deferred** — see `PUBLIC_CONTENT_POLICY.md` |

## DAG (simplified)

```text
P0 scaffold → skill corpus → CI bar → agents+MCP → gen-surfaces
        ↘ contracts (#12) → nanlabs-setup autoconfig (#20)
        ↘ pilots (#8/#9) → cutover notice (#23)
```

## ADR

See [`adrs/ADR-008-plugins-agent-skills-distribution.md`](adrs/ADR-008-plugins-agent-skills-distribution.md).
