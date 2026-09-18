> [!NOTE]
> 📘 **ClickUp Companion**, last synced **2026-09-17**
>
> This document is mirrored in the NaNLABS internal ClickUp workspace for cross-team discovery and execution logging. Packs and contribution: [`PACKS.md`](PACKS.md), [`CONTRIBUTION.md`](CONTRIBUTION.md).
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

---

# Authoring guide

This repository follows the open **[Agent Skills](https://agentskills.io/specification)** standard. Do not invent parallel manifests.

Portable **plugins** additionally follow **[Agent Plugins](https://agent-plugins.org/specification)** v1.0.0. Those two layouts are different (see below).

## Skill layout (canonical)

One tree. Author the skill where Agent Plugins discovers it:

```text
plugins/nanlabs-<group>/
├── plugin.json
└── skills/
    └── <skill>/
        ├── SKILL.md          # Required: YAML frontmatter + instructions
        ├── scripts/          # Optional: executable helpers
        ├── references/       # Optional: progressive-disclosure docs
        ├── assets/           # Optional: templates / data
        ├── LICENSE.txt       # Optional: required when redistributing third-party skills
        └── NOTICE.txt        # Optional: NaNLABS modifications to third-party skills
```

`name` in frontmatter must match the directory. Grouping is inventory only (`catalogs/skills-layout.json` + `products/plugins.yaml` `skills_group`). Do **not** add `skills/<group>/` at repo root. `npx skills` still finds nested `SKILL.md` (depth ≤ 5).

[Agent Plugins §7.1](https://agent-plugins.org/specification#71-skills) discovers **only immediate** `skills/<name>/SKILL.md` children. `gen-surfaces` writes manifests, LICENSE, plugin README, native plugin.json, official `mcp.json` / `.mcp.json`, and catalog docs (`docs/generated/`, wiki Plugin-Marketplace / Skills-Reference / MCP-Setup, README generated regions) from [`products/plugins.yaml`](../products/plugins.yaml) + catalogs. Do not nest groups inside a plugin `skills/` directory. Do not add unknown top-level fields to `plugin.json`. Do not put agents or skill paths in that manifest. MCP is root `mcp.json` only.

Domain packs (`catalogs/pack-catalog.yaml`) are `npx skills` aliases. Group packs map 1:1 onto these plugin directories. See [`PACKS.md`](PACKS.md) and [`AGENT_PLUGINS.md`](AGENT_PLUGINS.md).

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

Repo-level routing metadata lives in `catalogs/skill-catalog.yaml` (orchestrator index) and `catalogs/pack-catalog.yaml` (installable packs), not inside each skill folder.

## Other paths

| Path | Role |
| --- | --- |
| `agents/` | Agent/subagent personas (canonical `agents/<name>/AGENT.md`) |
| `products/plugins.yaml` | Plugin + marketplace version source of truth (synced by gen-surfaces) |
| `catalogs/agent-target-map.yaml` | Target-specific agent frontmatter overlays |
| `mcp/templates/` | Official MCP URL docs (same URLs as plugin `mcp.json`) |
| `plugins/<id>/` | Claude / Cursor plugin bundles |
| `catalogs/` | Routing catalogs (`skill-catalog.yaml`, `pack-catalog.yaml`, layout map) |
| `contracts/requirements/` | Dependency/permission contracts (`RequirementContract` v1) |
| `docs/PACKS.md` | Installable group and domain packs |
| `docs/CONTRIBUTION.md` | Propose-via-PR flow |
| GitHub issues `#24`, `#25`, `#28` | Remaining outcome-pack **content** (not this catalog) |

## Dependency contracts

See [`contracts/README.md`](../contracts/README.md). Add one YAML file per capability that setup (`/nanlabs-core:setup`) should detect/verify. Validate with:

```bash
python3 scripts/validate-contracts.py
```

## Rules

1. Author skills under `plugins/nanlabs-<group>/skills/<skill>/` per the Agent Skills spec. Add the name to `catalogs/skills-layout.json` and `catalogs/skill-catalog.yaml`. `gen-surfaces` only refreshes manifests.
2. Every `SKILL.md` needs valid YAML frontmatter (`name` + `description`).
3. Never commit secrets. Official MCP URLs live in `catalogs/mcp-catalog.yaml`. Plugin `mcp.json` is generated and MUST use the Agent Plugins MCP schema with no tokens in headers.
4. Public scrub: read `docs/PUBLIC_CONTENT_POLICY.md` before migrating internal content.
5. Project overlays belong in private repos; credentials remain L1-only (`docs/PUBLIC_CONTENT_POLICY.md`).
6. Keep upstream `LICENSE.txt` / `NOTICE.txt` when redistributing third-party skills.
7. Do not treat a pack as a plugin: no `plugin.json` for catalog packs.
8. Run local validation before opening a PR:

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-agent-plugins.py
python3 scripts/validate-public-content.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/validate-pack-catalog.py
python3 scripts/validate-skill-inventory.py
python3 scripts/validate-mcp.py
python3 scripts/validate-contracts.py
python3 scripts/gen-surfaces.py --check
python3 scripts/gen-copilot-surfaces.py --check
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Adding a plugin

1. Register the plugin in `products/plugins.yaml` (`skills_group` and/or `agents`).
2. For a group plugin, put skills at `plugins/<id>/skills/<name>/SKILL.md` and
   list them in `catalogs/skills-layout.json`.
3. Run `python3 scripts/gen-surfaces.py` then `python3 scripts/gen-copilot-surfaces.py`
   to generate native + portable manifests, LICENSE, marketplaces
   (Claude, Cursor, `.agents/plugins/`), and Copilot agent files.
   Do not copy skill trees.
4. Keep plugin `name` fields identical across marketplace entries and plugin manifests.
5. Run `python3 scripts/validate-skill-inventory.py`,
   `python3 scripts/validate-agent-plugins.py`, plus the other local
   validation commands above.
