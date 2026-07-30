# Solution packs

Outcome-oriented packs (plan §4.3). **Names are provisional** pending product
discovery (#25).

Platform capabilities (`nanlabs-setup`, `nanlabs-core`, `nanlabs-agents`, …
integrations) are technical building blocks. Packs compose those capabilities
into user-visible outcomes.

| Pack (provisional) | Path | Composes (intent) |
| --- | --- | --- |
| Reports | `packs/reports/` | integrations + docs skills |
| Documents | `packs/documents/` | docs / PRD / writing skills |
| Presentations | `packs/presentations/` | templates + evidence gathering |
| Meeting Follow-up | `packs/meeting-follow-up/` | notes → actions / risks |
| Delivery Discipline | `packs/delivery-discipline/` | ticket hygiene / traceability |
| Daily Routines | `packs/daily-routines/` | board / inbox hygiene |
| Engineering Workflow | `packs/engineering-workflow/` | issues, PRs, review agents |
| Project Harness | `packs/project-harness/` | overlay composition stub |

Machine index: [`catalogs/pack-catalog.yaml`](../catalogs/pack-catalog.yaml).

## Rules

1. Packs do **not** store credentials — L1 only.
2. Prefer depending on existing skills/agents/MCP stubs over copying them.
3. Overlay governance: [`docs/OVERLAY_GOVERNANCE.md`](../docs/OVERLAY_GOVERNANCE.md).
