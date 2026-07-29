# Authoring guide

## Layout

| Path | Role |
| --- | --- |
| `skills/` | Canonical Agent Skills tree (`SKILL.md` + `references/`) |
| `agents/` | Canonical agent/subagent personas |
| `mcp/templates/` | MCP config stubs (placeholders only) |
| `plugins/<id>/` | Distributable plugin bundles for Claude / Cursor |
| `catalogs/` | Routing catalogs |
| `contracts/requirements/` | Dependency/permission contracts (P1+) |

## Rules

1. Author skills once under `skills/`. For Claude plugin caching limits, also ship the skill **inside** the plugin directory for P0 (`plugins/.../skills/...`). Later waves may automate sync/symlinks.
2. Every `SKILL.md` needs YAML frontmatter with kebab-case `name` and a clear `description`.
3. Never commit secrets. Use env-var names only in MCP stubs.
4. Public scrub: read `docs/PUBLIC_CONTENT_POLICY.md` before migrating internal content.
5. Run local validation before opening a PR:

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Adding a plugin

1. Create `plugins/<plugin-id>/.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`.
2. Register it in `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`.
3. Keep plugin `name` fields identical across marketplace entries and plugin manifests.
4. Update catalogs when the plugin exposes new skills/agents.
