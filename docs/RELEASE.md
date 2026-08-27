# Release policy — agent-toolkit

Lightweight release model for a **content marketplace** repository (no CLI package, no binaries).

## Version source of truth

| Artifact | Authoritative version |
| --- | --- |
| Portable plugin manifest | `plugins/<id>/plugin.json` → Agent Plugins v1.0.0 metadata |
| Each native plugin | `plugins/<id>/.claude-plugin/plugin.json` → `version` (mirror in `.cursor-plugin/plugin.json`) |
| Marketplace metadata | `.claude-plugin/marketplace.json` / `.cursor-plugin/marketplace.json` → `metadata.version` (catalog revision; optional) |
| Git | Annotated tag `vX.Y.Z` matching the **default recommended plugin** (`nanlabs-core`) when cutting a distribution release |

Do not put `version` on Cursor **marketplace plugin entries** (official schema forbids it).

## SemVer rules (plugins)

- **MAJOR:** breaking removal/rename of skills, agents, or commands users rely on
- **MINOR:** new skills/agents/commands or backward-compatible enhancements
- **PATCH:** docs, fixes, schema compliance, no user-facing contract change

Bump the plugin `version` on every user-facing change to that plugin.

## Changelog

Maintain `CHANGELOG.md` at repo root (Keep a Changelog style). Each release section lists plugins touched and migration notes.

## Tags and GitHub Releases

1. Ensure CI green on `main`.
2. Update plugin versions + `CHANGELOG.md`.
3. Tag: `git tag -a vX.Y.Z -m "agent-toolkit vX.Y.Z"`.
4. Push tag; create GitHub Release with changelog excerpt.
5. Claude: users run marketplace update / plugin update.
6. Cursor Team Marketplace: refresh/re-import as required by admin settings.

## Pin and rollback

- **Claude:** pin marketplace/plugin to a git tag or commit SHA per Claude Code docs; reinstall prior version.
- **Cursor:** refresh marketplace to prior tag/commit; document Team Marketplace refresh lag.
- **Skills-only:** reinstall from a tagged commit (`npx skills add nanlabs/agent-toolkit@vX.Y.Z` when supported) or pin via lockfile when using project installs.

## Deprecation

- Announce in CHANGELOG and README for at least one minor release before removing a plugin ID or skill name.
- Prefer alias/redirect skills during transition.

## Certification evidence

Before calling a tag “production”:

- [x] Official Cursor marketplace schema validation (CI)
- [x] `claude plugin validate --strict` on shipped plugins (CI)
- [x] Live smoke checklist ([LIFECYCLE.md](LIFECYCLE.md)) — issue #8 is closed; operator evidence is retained in that issue
- [x] No secrets in tree

`v0.3.1` is the current distribution release (`nanlabs-core` 0.3.1, `nanlabs-agents` 0.2.1, marketplace metadata 0.5.1). Issues #8, #9, and #58 are closed.

## Schema pins

Cursor official schemas live under `schemas/cursor/` with an upstream commit note. Agent Plugins schemas are pinned under `schemas/agent-plugins/`. Refresh intentionally; do not hand-edit schema JSON.
