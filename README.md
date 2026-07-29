# agent-toolkit

[![CI Validate](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml)
[![MegaLinter](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-0A7EA4)](https://agentskills.io/specification)

NaNLABS **skills**, **agents**, **plugins**, and **MCP stubs** for Claude Code, Cursor, GitHub Copilot, OpenCode, and other Agent Skills–compatible clients.

> Public distribution repo (L1.5). Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation).  
> Migration program: GitHub Project [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12) · findings: [`docs/P0_FINDINGS.md`](docs/P0_FINDINGS.md)

## Install (60 seconds)

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
```

Then ask Claude to run setup, or use the `/setup` command from the plugin.

### Any agent (skills.sh / CLI)

```bash
npx skills add nanlabs/agent-toolkit -g
```

Installs the grouped tree `skills/<group>/<skill>/` (47 public skills). See [`docs/SKILLS.md`](docs/SKILLS.md) and [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md).

### Cursor

- **Local:** load plugins from this repo under `~/.cursor/plugins/local` (see [Cursor plugins docs](https://cursor.com/docs/plugins)).
- **Team:** import this repository as a Team Marketplace (admin; Teams/Enterprise).

## What's included

| Area | Count / notes |
| --- | --- |
| Skills | 47 under `skills/<group>/` — [catalog](catalogs/skill-catalog.yaml) |
| Setup plugin | `nanlabs-setup` (Claude + Cursor manifests) |
| Agents | `nanlabs-code-reviewer` (more in Wave 1) |
| MCP | Public stubs under `mcp/templates/` (env placeholders only) |

## Repository layout

| Path | Purpose |
| --- | --- |
| `skills/<group>/<skill>/` | Canonical [Agent Skills](https://agentskills.io/specification) tree |
| `plugins/` | Claude / Cursor plugin bundles |
| `.claude-plugin/` · `.cursor-plugin/` | Marketplace catalogs |
| `agents/` | Agent / subagent personas |
| `mcp/templates/` | MCP config stubs (no secrets) |
| `catalogs/` | Skill / agent indexes |
| `scripts/` | Validation + secret scan |
| `docs/` | Adoption, lifecycle, authoring, P0 findings |
| `tools/danger/` | Danger JS (TypeScript) for PR review |

## Quality bar

- Validate: structure, marketplace manifests, skills, secret-scan
- Pre-commit (YAML / JSON / markdown / private-key)
- MegaLinter v9 (cupcake allowlist)
- Danger JS on non-draft PRs
- [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Docs

| Doc | Topic |
| --- | --- |
| [`docs/ADOPTION.md`](docs/ADOPTION.md) | Install paths by client |
| [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md) | Update / pin / rollback |
| [`docs/P0_FINDINGS.md`](docs/P0_FINDINGS.md) | Feasibility + lifecycle matrix |
| [`docs/AUTHORING.md`](docs/AUTHORING.md) | How to add skills/plugins |
| [`docs/SKILLS.md`](docs/SKILLS.md) | Skill groups + opt-in packs |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md). Use the PR template; link an issue (`Fixes #N`).

## Security

[`SECURITY.md`](SECURITY.md) · [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

## License

[MIT](LICENSE)
