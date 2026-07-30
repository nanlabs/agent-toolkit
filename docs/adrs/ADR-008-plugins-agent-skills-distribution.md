# ADR-008 — Plugins and Agent Skills as NaN AI asset distribution

- **Status:** Accepted (draft frozen for H0/H1; amend via PR)
- **Date:** 2026-07-30
- **Deciders:** Architecture / M&I (NaNLABS Technology)
- **Related:** `docs/PUBLIC_CONTENT_POLICY.md`, `docs/WAVE0_INVENTORY.md`, migration plan §3–§6

## Context

NaNLABS AI assets historically lived under `internal-workstation` (chezmoi-managed paths, `skill.json` sync, IDE symlink matrices). Clients and IDEs now expect **Agent Skills** (`SKILL.md`), **Claude/Cursor plugins**, and **marketplaces**. Machine provisioning must stay separate from distributable skills/agents/MCP stubs.

## Decision

1. **`nanlabs/agent-toolkit` is the L1.5 source of truth** for public skills, agents, plugins, MCP stubs, catalogs, and dependency contracts.
2. **Distribution primitives** are Agent Skills + Claude/Cursor plugins (marketplaces), not home-dir symlink farms in this repo.
3. **Workstation remains L1** for OS tools, secrets (`env.d`), doctor, and machine identity. Do not delete workstation copies until cutover pilots pass.
4. **Visibility:** the repo is **public**. Content must pass `docs/PUBLIC_CONTENT_POLICY.md`. Private/internal corpus stays on workstation and/or L2 packs; a private companion marketplace is **deferred** (see policy § Companion marketplace).
5. **Telemetry** adapters/hooks are **out of band for H0** — L1 owns policy/secrets; L1.5 may later ship versioned adapters (#18 / #30) without embedding endpoints or keys here.
6. **Knowledge RAG / Onyx-class backends** are **post-cutover / Part III** (#31 family) — stubs only if a backend is selected.

## Consequences

### Positive

- One public install path: `/plugin marketplace add nanlabs/agent-toolkit` and `npx skills add nanlabs/agent-toolkit`.
- Clear scrub gate and CI validators before merge.
- Setup can grow against `contracts/requirements/` without inventing per-skill installers ad hoc.

### Negative / follow-ups

- Dual-rail temporarily (workstation + agent-toolkit) until cutover (#23).
- `nanlabs-tech-assistant` skill corpus remains workstation-only; agent persona may ship without the procedure pack.
- Full `/setup` autoconfig still needs Wave 2 implementation against these contracts (#20).

## Alternatives considered

| Option | Why not |
| --- | --- |
| Keep SoT only in workstation | Blocks marketplace / `npx skills` native flows |
| Make agent-toolkit private | Loses discoverability; public scrub already required |
| Ship private companion marketplace now | Premature — volume of private content fits workstation + L2 for now |

## References

- Migration plan: `nanlabs/internal-workstation` → `docs/AI_ASSETS_MIGRATION_PLAN.md`
- Issues: program epic #4; Wave 0 #16; visibility #13; contracts #12
