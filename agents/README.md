# Agents

Canonical agent / subagent personas for Claude Code, Cursor, OpenCode, and compatible clients.

## Bundled

| Agent | Path | Role |
| --- | --- | --- |
| `nanlabs-code-reviewer` | `agents/nanlabs-code-reviewer/` | Code quality / security / maintainability review |

Each agent directory contains `AGENT.md` (YAML frontmatter + instructions) and optional `references/`.

## Install notes

- **Claude Code:** ship via a plugin that lists agents, or copy into the client agents path per your tooling.
- **Cursor / rules:** map to project rules or plugin agents as documented by the client.
- More agents arrive in Wave 1 ([#17](https://github.com/nanlabs/agent-toolkit/issues/17)).

## Provenance

Migrated from `nanlabs/internal-workstation` with public-safe path scrubbing. See each agent's `NOTICE.txt` when present.
