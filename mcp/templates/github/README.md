# GitHub MCP template (stub)

Public-safe MCP stub. **No secrets** — use env-var substitution only.

## Required environment variables

| Variable | Purpose |
| --- | --- |
| `GITHUB_TOKEN` | GitHub PAT or `gh` auth token with least privilege needed |

## Usage

1. Copy `config.template.json` into your MCP client config (shape varies by client).
2. Export `GITHUB_TOKEN` (never commit it).
3. Optionally run `./wrapper.sh` as a local launcher example.

## Provenance

Adapted from `nanlabs/internal-workstation` MCP templates for public distribution in `agent-toolkit`.
