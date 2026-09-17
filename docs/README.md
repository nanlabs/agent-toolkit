> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.
>
> [!IMPORTANT]
> **L1 ↔ L1.5** — This **public** repo is L1.5 (skills, agents, plugins). **L1 machine provisioning** (`chezmoi`, `nan-*` CLI, internal-only skills) is in **`nanlabs/internal-workstation`** — **private**; NaNLABS GitHub org access required. Workstation bridge: [`docs/ADOPTION.md`](ADOPTION.md#workstation-cutover-internal-workstation).

---

# Documentation

Consumer-facing and maintainer docs for `nanlabs/agent-toolkit` (**L1.5**). Machine provisioning stays in **`nanlabs/internal-workstation`** (**private**).

**Production surfaces:** Agent Plugins roster + Claude Code.

## Documentation model

| Location | Purpose |
| --- | --- |
| `docs/` | Adoption, scope, lifecycle, authoring, certification |
| `docs/wiki/` | GitHub Wiki source (synced on `main`) |
| `docs/adrs/` | Architecture Decision Records |
| `static/` | README artwork |

## Start here

| Doc | Audience |
| --- | --- |
| [ADOPTION.md](ADOPTION.md) | Install by surface |
| [SCOPE.md](SCOPE.md) | In / out of product scope |
| [FAQ.md](FAQ.md) | Common questions |
| [LIFECYCLE.md](LIFECYCLE.md) | Update / pin / rollback |
| [CURSOR_CLI.md](CURSOR_CLI.md) | Cursor Agent CLI certification matrix |
| [AGENT_PLUGINS.md](AGENT_PLUGINS.md) | Portable versus native plugin surfaces |
| [wiki/Home.md](wiki/Home.md) | Wiki landing (synced) |

## Operators / certification

| Doc | Topic |
| --- | --- |
| [RELEASE.md](RELEASE.md) | Version SoT, tags, changelog |
| [PILOT_CHECKLIST.md](PILOT_CHECKLIST.md) | Production pilots (closed #9 checklist) |
| [P0_FINDINGS.md](P0_FINDINGS.md) | Feasibility + lifecycle matrix |
| [WAVE0_INVENTORY.md](WAVE0_INVENTORY.md) | H0 inventory + privacy |

## Authors / maintainers

| Doc | Topic |
| --- | --- |
| [AUTHORING.md](AUTHORING.md) | Add skills / plugins |
| [PACKS.md](PACKS.md) | Domain and group pack install |
| [HANDOFFS.md](HANDOFFS.md) | Planner / reviewer output contracts |
| [COVERAGE.md](COVERAGE.md) | Roles vs skills, honest gaps |
| [CONTRIBUTION.md](CONTRIBUTION.md) | Propose a skill via GitHub PR |
| [SKILLS.md](SKILLS.md) | Skill groups index |
| [AGENT_AUDIT.md](AGENT_AUDIT.md) | Core vs optional agents |
| [PUBLIC_CONTENT_POLICY.md](PUBLIC_CONTENT_POLICY.md) | What may be published |
| [OVERLAY_GOVERNANCE.md](OVERLAY_GOVERNANCE.md) | Project overlays |
| [TELEMETRY_CONTRACT.md](TELEMETRY_CONTRACT.md) | L1 policy vs L1.5 adapters |
| [adrs/ADR-008-plugins-agent-skills-distribution.md](adrs/ADR-008-plugins-agent-skills-distribution.md) | Distribution ADR |

## Related trees

| Path | Topic |
| --- | --- |
| [`../catalogs/`](../catalogs/) | Skill / agent / pack / MCP indexes |
| [`../contracts/`](../contracts/) | Dependency contracts |
| GitHub issues `#24`, `#25`, `#28` | Remaining outcome-pack content (catalog is in `pack-catalog.yaml`) |
| [`../mcp/templates/`](../mcp/templates/) | Official MCP URL docs (shipped via plugin `mcp.json`) |

## GitHub Wiki

Human-browsable mirror synced from [`wiki/`](wiki/) via [`.github/workflows/wiki-sync.yml`](../.github/workflows/wiki-sync.yml) (initialize the wiki once on GitHub). Prefer editing `docs/wiki/` in PRs.
