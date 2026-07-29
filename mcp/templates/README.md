# MCP templates

Public MCP config **stubs** — env-var placeholders only. Never commit tokens, PATs, or private hosts.

## Bundled

| Template | Path | Required env |
| --- | --- | --- |
| GitHub | `mcp/templates/github/` | `GITHUB_TOKEN` |

Each stub includes:

- `config.template.json` — client-agnostic shape with `${ENV_VAR}` substitution
- `README.md` — how to wire it
- Optional `wrapper.sh` — local launcher example

## Rules

1. Secrets stay in the environment or a secret manager — not in git.
2. Prefer least-privilege tokens.
3. Document every required variable in the template README.

See [`docs/PUBLIC_CONTENT_POLICY.md`](../docs/PUBLIC_CONTENT_POLICY.md).
