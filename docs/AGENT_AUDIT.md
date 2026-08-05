# Agent content audit (production)

Inventory for issue [#62](https://github.com/nanlabs/agent-toolkit/issues/62). Update when agents change.

| Agent | Keep in core? | Keep in nanlabs-agents? | Notes |
| --- | --- | --- | --- |
| nanlabs-assistant | yes (via skill) | yes | Orchestrator |
| nanlabs-code-reviewer | yes | yes | Baseline reviewer |
| nanlabs-architect | no | yes | |
| nanlabs-planner | no | yes | |
| nanlabs-security-reviewer | no | yes | |
| nanlabs-tdd-guide | no | yes | |
| nanlabs-refactor-cleaner | no | yes | |
| nanlabs-build-error-resolver | no | yes | |
| nanlabs-typescript-reviewer | no | yes | |
| nanlabs-database-reviewer | no | yes | |
| nanlabs-performance-optimizer | no | yes | |
| nanlabs-e2e-runner | no | yes | |
| nanlabs-docs-lookup | no | yes | |
| nanlabs-reference-lookup | no | yes | |
| nanlabs-client-workflow-bootstrap | no | yes | |
| nanlabs-tech-assistant | no | yes | Persona public; procedure skill may stay workstation-only |

## Skills gate

All canonical skills under `skills/` must pass `npx skills-ref validate` in CI.

## Frontmatter

Canonical agents should not carry OpenCode-only fields after #54; target mappings belong in the assembler.
