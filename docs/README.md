> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-05**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Documentation

Consumer-facing and maintainer docs for `nanlabs/agent-toolkit` (**L1.5**). Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation).

**Production surfaces:** Claude · Claude Code · Cursor IDE · Cursor Agent CLI · GitHub Copilot.

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
| [wiki/Home.md](wiki/Home.md) | Wiki landing (synced) |

## Operators / certification

| Doc | Topic |
| --- | --- |
| [RELEASE.md](RELEASE.md) | Version SoT, tags, changelog |
| [PILOT_CHECKLIST.md](PILOT_CHECKLIST.md) | Production pilots (#9) |
| [P0_FINDINGS.md](P0_FINDINGS.md) | Feasibility + lifecycle matrix |
| [WAVE0_INVENTORY.md](WAVE0_INVENTORY.md) | H0 inventory + privacy |

## Authors / maintainers

| Doc | Topic |
| --- | --- |
| [AUTHORING.md](AUTHORING.md) | Add skills / plugins |
| [SKILLS.md](SKILLS.md) | Skill groups index |
| [AGENT_AUDIT.md](AGENT_AUDIT.md) | Core vs optional agents |
| [PUBLIC_CONTENT_POLICY.md](PUBLIC_CONTENT_POLICY.md) | What may be published |
| [OVERLAY_GOVERNANCE.md](OVERLAY_GOVERNANCE.md) | Project overlays |
| [TELEMETRY_CONTRACT.md](TELEMETRY_CONTRACT.md) | L1 policy vs L1.5 adapters |
| [adrs/ADR-008-plugins-agent-skills-distribution.md](adrs/ADR-008-plugins-agent-skills-distribution.md) | Distribution ADR |

## Related trees

| Path | Topic |
| --- | --- |
| [`../catalogs/`](../catalogs/) | Skill / agent / MCP indexes |
| [`../contracts/`](../contracts/) | Dependency contracts |
| GitHub issues `#24`, `#25`, `#28` | Future outcome-pack discovery and implementation |
| [`../mcp/templates/`](../mcp/templates/) | MCP docs-only stubs |

## GitHub Wiki

Human-browsable mirror synced from [`wiki/`](wiki/) via [`.github/workflows/wiki-sync.yml`](../.github/workflows/wiki-sync.yml) (initialize the wiki once on GitHub). Prefer editing `docs/wiki/` in PRs.
