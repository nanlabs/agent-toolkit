# agent-toolkit

[![CI Validate](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml)
[![MegaLinter](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml/badge.svg)](https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-0A7EA4)](https://agentskills.io/specification)

NaNLABS **skills**, **agents**, and **plugins** for **Claude Code** and **Cursor**. Portable skills also install via the Agent Skills CLI (skills-only).

> Public distribution repo (L1.5). Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation).  
> Migration program: GitHub Project [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12) · findings: [`docs/P0_FINDINGS.md`](docs/P0_FINDINGS.md)

## Install (60 seconds)

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run **`/nanlabs-core:setup`** or ask Claude to run the bundled setup skill.

Optional: `/plugin install nanlabs-agents@nanlabs-agent-toolkit` for the full agent roster.

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
| Core plugin | `nanlabs-core` v0.2 — recommended install: harness + bundled setup doctor + `/nanlabs-core:setup` |
| Agents plugin | `nanlabs-agents` (optional) — all 16 personas (generated via `gen-surfaces`) |
| Agents | 16 under `agents/` — [catalog](catalogs/agent-catalog.yaml) |
| MCP templates | Docs-only under `mcp/templates/` (not installed by plugins) |

## Repository layout

| Path | Purpose |
| --- | --- |
| `skills/<group>/<skill>/` | Canonical [Agent Skills](https://agentskills.io/specification) tree |
| `plugins/` | Claude / Cursor plugin bundles |
| `.claude-plugin/` · `.cursor-plugin/` | Marketplace catalogs |
| `agents/` | Agent / subagent personas (canonical) |
| `products/` | Plugin assembler inputs (`plugins.yaml`) |
| `mcp/templates/` | MCP config stubs (no secrets) |
| `packs/` | Outcome-oriented solution pack stubs |
| `contracts/` | Dependency/permission contracts |
| `catalogs/` | Skill / agent / MCP / pack indexes |
| `scripts/` | Validation + secret scan |
| `docs/` | Adoption, lifecycle, authoring, P0 findings |
| `tools/danger/` | Danger JS (TypeScript) for PR review |

## Quality bar

- Validate: structure, marketplace manifests, skills, agents, MCP stubs, secret-scan
- Pre-commit (YAML / JSON / markdown / private-key)
- MegaLinter v9 (cupcake allowlist)
- Danger JS on non-draft PRs
- [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

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
| [`docs/ADOPTION.md`](docs/ADOPTION.md) | Install paths by client |
| [`docs/CURSOR_CLI.md`](docs/CURSOR_CLI.md) | Cursor CLI parity matrix (beta) |
| [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md) | Update / pin / rollback |
| [`docs/RELEASE.md`](docs/RELEASE.md) | Version SoT, tags, changelog, rollback |
| [`docs/PILOT_CHECKLIST.md`](docs/PILOT_CHECKLIST.md) | Production pilot journeys (#9) |
| [`docs/P0_FINDINGS.md`](docs/P0_FINDINGS.md) | Feasibility + lifecycle matrix |
| [`docs/AUTHORING.md`](docs/AUTHORING.md) | How to add skills/plugins |
| [`docs/AGENT_AUDIT.md`](docs/AGENT_AUDIT.md) | Core vs optional agents inventory |
| [`docs/WAVE0_INVENTORY.md`](docs/WAVE0_INVENTORY.md) | H0 inventory + privacy classes |
| [`docs/OVERLAY_GOVERNANCE.md`](docs/OVERLAY_GOVERNANCE.md) | Project overlay checklist |
| [`docs/TELEMETRY_CONTRACT.md`](docs/TELEMETRY_CONTRACT.md) | L1 policy vs L1.5 adapters |
| [`docs/adrs/ADR-008-plugins-agent-skills-distribution.md`](docs/adrs/ADR-008-plugins-agent-skills-distribution.md) | Distribution ADR |
| [`contracts/README.md`](contracts/README.md) | Dependency/permission contracts |
| [`packs/README.md`](packs/README.md) | Solution packs (provisional stubs) |
| [`docs/SKILLS.md`](docs/SKILLS.md) | Skill groups + opt-in packs |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md). Use the PR template; link an issue (`Fixes #N`).

## Security

[`SECURITY.md`](SECURITY.md) · [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

## License

[MIT](LICENSE)
