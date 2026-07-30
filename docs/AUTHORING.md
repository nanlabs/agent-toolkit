# Authoring guide

This repository follows the open **[Agent Skills](https://agentskills.io/specification)** standard. Do not invent parallel manifests.

## Skill layout (canonical)

```text
skills/<group>/<skill>/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: executable helpers
├── references/       # Optional: progressive-disclosure docs
├── assets/           # Optional: templates / data
├── LICENSE.txt       # Optional: required when redistributing third-party skills
└── NOTICE.txt        # Optional: NaNLABS modifications to third-party skills
```

Grouped under `skills/<group>/` so the tree stays navigable; `npx skills` discovers nested `SKILL.md` (depth ≤ 5).

### `SKILL.md` frontmatter

Required by the Agent Skills spec:

| Field | Required | Notes |
| --- | --- | --- |
| `name` | Yes | Kebab-case; must match the parent directory name |
| `description` | Yes | What it does **and** when to use it (trigger keywords) |

Optional spec fields: `license`, `compatibility`, `metadata`, `allowed-tools`.

### What we do **not** ship

| Artifact | Why it is gone here |
| --- | --- |
| `skill.json` | Workstation-only (`nan-skills sync` / ADR-004). Agent Skills + `npx skills` + Claude/Cursor plugins read **`SKILL.md` only**. |
| `SKILL.md.tmpl` | Chezmoi template; this repo ships the rendered skill. |
| Per-tool symlink matrices in-repo | Distribution is marketplace / `npx skills`, not home-dir symlinks. |

Repo-level routing metadata lives in `catalogs/skill-catalog.yaml` (orchestrator index), not inside each skill folder.

## Other paths

| Path | Role |
| --- | --- |
| `agents/` | Agent/subagent personas |
| `mcp/templates/` | MCP config stubs (placeholders only) |
| `plugins/<id>/` | Claude / Cursor plugin bundles |
| `catalogs/` | Routing catalogs (`skill-catalog.yaml`, layout map) |
| `contracts/requirements/` | Dependency/permission contracts (`RequirementContract` v1) |
| `packs/` | Solution pack stubs (provisional names) |

## Dependency contracts

See [`contracts/README.md`](../contracts/README.md). Add one YAML file per capability that `nanlabs-setup` should detect/verify. Validate with:

```bash
python3 scripts/validate-contracts.py
```

## Rules

1. Author skills under `skills/<group>/<skill>/` per the Agent Skills spec. For Claude plugin caching limits, also ship the skill **inside** the plugin directory for P0 (`plugins/.../skills/...`). Later waves may automate sync.
2. Every `SKILL.md` needs valid YAML frontmatter (`name` + `description`).
3. Never commit secrets. Use env-var names only in MCP stubs.
4. Public scrub: read `docs/PUBLIC_CONTENT_POLICY.md` before migrating internal content.
5. Project overlays: follow `docs/OVERLAY_GOVERNANCE.md` (credentials remain L1-only).
6. Keep upstream `LICENSE.txt` / `NOTICE.txt` when redistributing third-party skills.
7. Run local validation before opening a PR:

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

## Adding a plugin

1. Create `plugins/<plugin-id>/.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`.
2. Register it in `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`.
3. Keep plugin `name` fields identical across marketplace entries and plugin manifests.
4. Update catalogs when the plugin exposes new skills/agents.
