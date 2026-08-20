# Agents

Canonical agent / subagent personas for Claude Code, Cursor, OpenCode, and compatible clients.

Machine-readable index: [`catalogs/agent-catalog.yaml`](../catalogs/agent-catalog.yaml).

## Bundled (18)

| Agent | Role |
| --- | --- |
| `nanlabs-assistant` | Orchestrator / repo discovery / routing |
| `nanlabs-architect` | System design and trade-offs |
| `nanlabs-planner` | Scope breakdown and delivery plans |
| `nanlabs-code-reviewer` | Code quality / security / maintainability |
| `nanlabs-security-reviewer` | Vulnerability-focused review |
| `nanlabs-typescript-reviewer` | TypeScript / type-safety review |
| `nanlabs-database-reviewer` | PostgreSQL / schema / ORM review |
| `nanlabs-tdd-guide` | Tests-first guidance |
| `nanlabs-refactor-cleaner` | Dead code / simplification |
| `nanlabs-performance-optimizer` | Perf / memory / benchmarks |
| `nanlabs-build-error-resolver` | Build / lint / CI failures |
| `nanlabs-e2e-runner` | Playwright E2E |
| `nanlabs-docs-lookup` | Framework / API docs lookup |
| `nanlabs-reference-lookup` | NaNLABS examples / starters |
| `nanlabs-client-workflow-bootstrap` | Client workflow onboarding |
| `nanlabs-devcompanion-lead` | Dev-companion queue / plan lead |
| `nanlabs-forge-pr` | Draft PR / MR from current branch |
| `nanlabs-data-validator` | Data / ETL contract checks |

Each agent directory contains `AGENT.md` (YAML frontmatter: `name` + `description` only), optional `references/`, and `NOTICE.txt`. Target-specific fields (Claude `tools`, OpenCode/Cursor UI metadata) live in [`catalogs/agent-target-map.yaml`](../catalogs/agent-target-map.yaml) and are applied by `scripts/gen-surfaces.py` when building plugin agent files.

## Install notes

- **Claude Code / Cursor plugins:** install `nanlabs-agents` for the full set, or use `nanlabs-core` (includes `nanlabs-code-reviewer` only). Plugin layout is flat `plugins/<id>/agents/<name>.md` with references under `plugins/<id>/resources/agents/<name>/`.
- **Direct copy:** point your client at `agents/<name>/AGENT.md` per tooling docs.
- Plugin agent files and core skills are generated — edit `agents/` and `skills/core/`, then run `python3 scripts/gen-surfaces.py`.

## Provenance

Canonical source is this repository. Plugin surfaces are generated — see each agent's `NOTICE.txt` for provenance.
