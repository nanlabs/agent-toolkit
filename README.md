# agent-toolkit

NaNLABS skills, agents, plugins, MCP integrations, and reusable workflows for AI agents across Claude Code, Cursor, Copilot, OpenCode, and other compatible clients.

> **Status:** P0 scaffold in progress. Content migration from [`internal-workstation`](https://github.com/nanlabs/internal-workstation) is tracked in GitHub Project [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12).
>
> **Canonical migration plan:** [`docs/AI_ASSETS_MIGRATION_PLAN.md`](https://github.com/nanlabs/internal-workstation/blob/main/docs/AI_ASSETS_MIGRATION_PLAN.md) (internal workstation repo).

## Install (60 seconds)

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
```

### Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

## Repository layout

| Path | Purpose |
| --- | --- |
| `skills/<group>/<skill>/` | Canonical [Agent Skills](https://agentskills.io/specification) tree (`SKILL.md` only; grouped for `npx skills`) |
| `catalogs/skill-catalog.yaml` | Public skill index + group map |
| `plugins/` | Claude / Cursor plugin bundles |
| `.claude-plugin/` / `.cursor-plugin/` | Marketplace catalogs |
| `agents/` | Agent personas (populated during migration) |
| `mcp/templates/` | MCP stubs (placeholders only) |
| `scripts/` | Validation and secret scan |
| `docs/` | Adoption, authoring, public content policy |

## Quality bar

This public repository follows NaNLABS quality standards:

- Manifest + skill validation in CI
- Pre-commit hooks (YAML/JSON/markdown/private-key)
- Secret scan on tracked files
- `CODEOWNERS`, Dependabot for GitHub Actions
- Public content policy enforced in docs + PR template

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
bash scripts/secret-scan.sh
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`AGENTS.md`](AGENTS.md), and [`docs/AUTHORING.md`](docs/AUTHORING.md).

## Security

See [`SECURITY.md`](SECURITY.md) and [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md).

## License

[MIT](LICENSE)
