# Agents

Canonical agent / subagent personas for Claude Code, Cursor, OpenCode, and compatible clients.

Machine-readable index: [`catalogs/agent-catalog.yaml`](../catalogs/agent-catalog.yaml).

## Bundled (16)

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
| `nanlabs-tech-assistant` | Internal ops procedures (skill corpus may be host-only) |

Each agent directory contains `AGENT.md` (YAML frontmatter + instructions), optional `references/`, and `NOTICE.txt`.

## Install notes

- **Claude Code / Cursor plugins:** ship selected agents under a plugin `agents/` tree (see `plugins/nanlabs-core` for `nanlabs-code-reviewer`).
- **Direct copy:** point your client at `agents/<name>/AGENT.md` per tooling docs.
- Catalog handoffs may reference skills that live under `skills/` in this repo.

## Provenance

Copy-forward from `nanlabs/internal-workstation` with public-safe path scrubbing. Workstation copies remain until cutover. See each agent's `NOTICE.txt`.
