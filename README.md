# agent-toolkit

[![CI Validate](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml)
[![MegaLinter](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-0A7EA4)](https://agentskills.io/specification)

NaNLABS **skills**, **agents**, and **plugins** for **Claude**, **Claude Code**, **Cursor IDE**, and **Cursor Agent CLI** (equal product priority).

> Public **L1.5** distribution. Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation).  
> Docs index: [`docs/README.md`](docs/README.md) · Wiki source: [`docs/wiki/`](docs/wiki/) · Scope: [`docs/SCOPE.md`](docs/SCOPE.md)

| Skills | Agents | Plugins | MCP |
| --- | --- | --- | --- |
| 47 | 16 | `nanlabs-core` + `nanlabs-agents` | Docs-only templates |

**Out of scope as plugin targets:** OpenCode, Copilot, Windsurf, Gemini CLI, Pi, … (skills may still work via `npx skills`). No consumer CLI / loop runtime in this repo.

## Install

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then **`/nanlabs-core:setup`**. Optional: `/plugin install nanlabs-agents@nanlabs-agent-toolkit`.

### Cursor IDE

- **Local:** `~/.cursor/plugins/local` ([docs](https://cursor.com/docs/plugins))
- **Team:** import this repo as a Team Marketplace

Install **`nanlabs-core`** (recommended).

### Cursor Agent CLI

Equal priority with Cursor IDE. See [`docs/CURSOR_CLI.md`](docs/CURSOR_CLI.md).

```bash
agent --version || cursor agent --version || true
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
# Prefer --plugin-dir for local smoke; see docs/CURSOR_CLI.md
```

### Skills-only

```bash
npx skills add nanlabs/agent-toolkit -g
```

Skills **only** — not plugins, agents, MCP, or setup automation.

## What's included

| Area | Notes |
| --- | --- |
| Skills | 47 under `skills/<group>/` — [catalog](catalogs/skill-catalog.yaml) · [index](docs/SKILLS.md) |
| Core plugin | `nanlabs-core` v0.2 — harness + setup doctor + `/nanlabs-core:setup` |
| Agents plugin | `nanlabs-agents` (optional) — 16 personas via `gen-surfaces` |
| MCP | Docs-only under `mcp/templates/` |

## Repository layout

| Path | Purpose |
| --- | --- |
| `skills/<group>/<skill>/` | Canonical Agent Skills tree |
| `plugins/` | Claude / Cursor bundles |
| `.claude-plugin/` · `.cursor-plugin/` | Marketplace catalogs |
| `agents/` | Canonical personas |
| `products/plugins.yaml` | Plugin version + assembly SoT |
| `mcp/templates/` | MCP stubs (no secrets) |
| `docs/` · `docs/wiki/` | Repo docs + GitHub Wiki source |
| `scripts/` | Validation + `gen-surfaces` |

## Quality bar

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/validate-mcp.py
python3 scripts/validate-contracts.py
python3 scripts/gen-surfaces.py --check
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Docs

| Doc | Topic |
| --- | --- |
| [`docs/README.md`](docs/README.md) | Full index |
| [`docs/ADOPTION.md`](docs/ADOPTION.md) | Install paths |
| [`docs/SCOPE.md`](docs/SCOPE.md) | In / out of scope |
| [`docs/FAQ.md`](docs/FAQ.md) | FAQ |
| [`docs/CURSOR_CLI.md`](docs/CURSOR_CLI.md) | Cursor Agent CLI matrix |
| [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md) | Update / pin / rollback |
| [`docs/RELEASE.md`](docs/RELEASE.md) | Tags / changelog |
| [`docs/AUTHORING.md`](docs/AUTHORING.md) | Add skills/plugins |
| [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md) | Public safety |

## Contributing

[`CONTRIBUTING.md`](CONTRIBUTING.md) · [`AGENTS.md`](AGENTS.md) · PR template · link an issue (`Fixes #N` / `Refs #N`).

## Security

[`SECURITY.md`](SECURITY.md) · [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

## License

[MIT](LICENSE)
