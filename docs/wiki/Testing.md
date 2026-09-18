# Testing

Run the same gates CI runs on a **ready** (non-draft) pull request. Draft PRs skip Validate.

Canonical list: [`CONTRIBUTING.md`](https://github.com/nanlabs/agent-toolkit/blob/main/CONTRIBUTING.md).

## One-time setup

```bash
git clone https://github.com/nanlabs/agent-toolkit.git
cd agent-toolkit
python3 -m pip install pre-commit
pre-commit install
```

Python **3.10+**. No Node needed unless you touch `tools/danger/`.

## Before you open a PR

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-agent-plugins.py
python3 scripts/validate-skill-inventory.py
python3 scripts/validate-public-content.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/validate-pack-catalog.py
python3 scripts/validate-mcp.py
python3 scripts/gen-surfaces.py --check
python3 scripts/gen-copilot-surfaces.py --check
bash scripts/secret-scan.sh
pre-commit run --all-files
```

If you **changed catalogs** (`products/plugins.yaml`, `catalogs/*`, skills layout), regenerate first:

```bash
python3 scripts/gen-surfaces.py
python3 scripts/gen-copilot-surfaces.py
```

`--check` must stay green. Generated files include plugin manifests, README install blocks, `docs/generated/`, and wiki [Plugin marketplace](Plugin-Marketplace) / [Skills](Skills-Reference) / [Official MCP](MCP-Setup).

## What CI runs

| Workflow | What it proves |
| --- | --- |
| `validate.yml` | Structure, manifests, Agent Plugins, skills, MCP, catalog drift, secret-scan, pre-commit, Claude plugin validate |
| `mega-linter.yml` | Markdown / YAML / shell / Actions (cupcake allowlist) |
| `pr-review.yml` | Danger JS — PR template + `Fixes #N` / `Refs #N` |

On `main`, wiki pages under `docs/wiki/` sync to the GitHub Wiki.

## Try a plugin locally

**Cursor IDE** — symlink and reload (see [Installation](Installation)).

### Cursor Agent CLI

```bash
agent --plugin-dir ./plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

**Claude Code** — `/plugin marketplace add` against your fork, or install from a local path if your client supports it.

### Skills-only

```bash
npx skills add ./plugins/nanlabs-core/skills
npx skills check
```

## Skill / plugin sanity

- `SKILL.md` frontmatter `name` matches the folder
- No placeholder README-only skill dirs (`validate-no-placeholders.py`)
- Plugin `plugin.json` stays a closed Agent Plugins v1 manifest
- MCP URLs come from `catalogs/mcp-catalog.yaml` — do not invent endpoints
- Public scrub: [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md)

## Doctor (core)

```bash
python3 scripts/doctor-contracts.py --contract nanlabs-core
python3 plugins/nanlabs-core/scripts/doctor-contracts.py --contract nanlabs-core
```
