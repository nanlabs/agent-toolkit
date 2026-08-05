# GitHub MCP template (docs-only stub)

Public-safe MCP **template** for contributors. **Not** installed by `nanlabs-core` / `nanlabs-agents` marketplace plugins.

Prefer the official [`github/github-mcp-server`](https://github.com/github/github-mcp-server) distribution. The example below uses the published npm package when available; verify current install docs before production use.

## Required environment variables

| Variable | Purpose |
| --- | --- |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | Fine-grained or classic PAT with least privilege |

Never commit tokens. Prefer read-only scopes until write actions are required.

## Usage

1. Copy `config.template.json` into your MCP client config (shape varies by client).
2. Export `GITHUB_PERSONAL_ACCESS_TOKEN`.
3. Optionally adapt `wrapper.sh` as a local launcher.

## Provenance

Adapted from `nanlabs/internal-workstation` for public docs in `agent-toolkit`. Classification: **docs-only** until an optional integrations plugin ships.
