# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for plugin packages.

## [Unreleased]

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
