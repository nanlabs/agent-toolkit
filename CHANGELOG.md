# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for plugin packages.

## [Unreleased]

### Added

- User-facing GitHub Wiki: install plugins, using the toolkit, add a skill, testing, and contributing. README and docs index send people to [the live wiki](https://github.com/nanlabs/agent-toolkit/wiki).

### Removed

- Deprecated standalone `nanlabs-setup` plugin stub. Setup remains the `nanlabs-setup` skill inside `nanlabs-core` (`/nanlabs-core:setup`).
- Historical Wave 0 / P0 / telemetry / overlay / pilot snapshot docs that no longer describe the product.
- Operator smoke wrapper that only pointed at closed issue #8.

### Changed

- README hero SVG is GitHub-safe (no pattern fills, no invalid UTF-8) so GitHub renders the image instead of "Invalid image source".
- Cursor Agent CLI matrix: official MCP now ships in design/forge/integrations plugins; CLI MCP load remains uncertified.
- README hero SVG, architecture diagram, and generated catalog tables (`docs/generated/`, wiki Plugin-Marketplace / Skills-Reference / MCP-Setup) so plugin/MCP/skill counts cannot drift from YAML sources of truth.
- Complete copy-paste install for every group plugin on Claude Code, Copilot CLI, and Cursor local.

## [0.4.0] — 2026-09-17

Distribution tag matches `nanlabs-core` **0.4.0**. Marketplace metadata **0.7.0**.

### Added

- Official hosted MCP servers in group plugins (`mcp.json` + `.mcp.json`) from `catalogs/mcp-catalog.yaml`: ClickUp, Slack, Linear, Shortcut, Notion, Atlassian (Jira/Confluence), GitHub, GitLab.com, Figma. Auth is client OAuth; no tokens in the plugin.
- One **plugin per skill group**. Canonical skills live only under `plugins/nanlabs-<group>/skills/<name>/` (no `skills/<group>/` tree, no `.github/skills/` mirror). `gen-surfaces` writes manifests only.
- Group plugins: `nanlabs-data`, `nanlabs-delivery`, `nanlabs-design`, `nanlabs-forge`, `nanlabs-integrations`, `nanlabs-ops`, `nanlabs-tooling`, `nanlabs-workflow`. Optional `nanlabs-agents` unchanged at 0.2.1.
- ChatGPT/Codex catalog at `.agents/plugins/marketplace.json`. Copilot VS Code agents under `com.github.copilot/agents/`.
- Domain and group **packs** as catalog aliases (`catalogs/pack-catalog.yaml`).
- Skill `nanlabs-propose-skill` plus contribution docs and PR/issue checklists.

### Changed

- `nanlabs-design`, `nanlabs-forge`, and `nanlabs-integrations` **0.2.0** (official MCP).
- Inventory CI (`scripts/validate-skill-inventory.py`) fails on duplicated or leftover skill trees.

## [0.3.1] — 2026-08-27

- Public-content hardening removes direct internal ClickUp workspace/document URLs and adds a deterministic public-content validator.
- Agent Plugins v1.0.0 manifests use vendored schemas and deterministic validation.
- Distribution metadata: `nanlabs-core` **0.3.1**, `nanlabs-agents` **0.2.1**, marketplace metadata **0.5.1**.
- Documentation is current with v0.3.1 distribution metadata, 48 skills, 18 agents, and closed #8/#9/#58 status.

## [0.3.0] — 2026-08-20

Sole-source distribution: skills, agents, plugins, and MCP templates live **here**. `internal-workstation` provisions machines only.

### Added

- Agents: `nanlabs-devcompanion-lead`, `nanlabs-forge-pr`, `nanlabs-data-validator`.
- MCP templates under `mcp/templates/` (ClickUp, GitHub, Slack, Notion, Linear, Figma).

### Removed

- Agent `nanlabs-tech-assistant` (procedure pack was never public; persona removed to match zero-bundled workstation).

### Changed

- `nanlabs-core` **0.3.0**, `nanlabs-agents` **0.2.0**, marketplace metadata **0.5.0**.
- Adoption / README: workstation is L1 (chezmoi + `nan-ai-enable`); this repo is L1.5.

## [0.2.0] — 2026-08-05

First distribution tag aligned with **`nanlabs-core` 0.2.0** (marketplace metadata `0.4.0`).

### Added

- Production plugin lineup: marketplace ships **`nanlabs-core`** + **`nanlabs-agents`** only; setup/doctor bundled in core (`/nanlabs-core:setup`).
- Deterministic `scripts/gen-surfaces.py` assembler (agents + skill mirror + versions from `products/plugins.yaml`).
- Official Cursor marketplace/plugin schemas under `schemas/cursor/` + CI validation.
- CI: Agent Skills upstream validator, Claude plugin validate, contracts doctor.
- Docs: `RELEASE.md`, `CURSOR_CLI.md`, `SCOPE.md`, `FAQ.md`, pilot/smoke checklists, wiki source + sync workflow.
- README hero / architecture artwork (`static/`).
- MCP templates reclassified as docs-only; GitHub stub uses official server package.

### Changed

- Equal-priority product surfaces: Claude · Claude Code · Cursor IDE · Cursor Agent CLI.
- Flat plugin agent files (`plugins/*/agents/*.md`); references under `resources/`.
- Neutral canonical agent frontmatter (target map at build).

### Deprecated

- Standalone `nanlabs-setup` marketplace plugin (directory retained with `DEPRECATION.md`).

### Fixed

- Cursor marketplace entries pass official `additionalProperties: false` schema.
- Claude `plugin validate --strict` agent layout (no nested `references` as agents).

## [0.1.0] — 2026-07-29

### Added

- Initial public marketplace scaffold, skills tree, CI (MegaLinter + Danger), early plugins.
