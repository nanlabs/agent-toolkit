> [!NOTE]
> 📘 **ClickUp Companion**, last synced **2026-08-27**
>
> This document is mirrored in the NaNLABS internal ClickUp workspace for cross-team discovery and execution logging.
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

> [!WARNING]
> **HISTORICAL SNAPSHOT — 2026-07-29:** Evidence in this file is frozen at that date. Issues #8, #9, and #58 are now **CLOSED**, and v0.3.0 is published. For current status, use [RELEASE.md](RELEASE.md), [CURSOR_CLI.md](CURSOR_CLI.md), and the current GitHub issues.

---

# P0 findings — agent-toolkit feasibility

> **Status:** Documented evidence pack (compressed P0)  
> **Date:** 2026-07-29  
> **Related:** epic [#19](https://github.com/nanlabs/agent-toolkit/issues/19), smoke [#8](https://github.com/nanlabs/agent-toolkit/issues/8), pilots [#9](https://github.com/nanlabs/agent-toolkit/issues/9)  
> **Plan SoT:** [AI_ASSETS_MIGRATION_PLAN.md](https://github.com/nanlabs/internal-workstation/blob/main/docs/AI_ASSETS_MIGRATION_PLAN.md) (private workstation repo)

## Verdict (HP0)

**Conditional go — packaging exists; live org smoke across Claude Code, Cursor IDE, and Cursor Agent CLI still required** (epic #19).

Official Claude Code, Cursor, and `npx skills` documentation already defines install / update / pin / uninstall behavior. Packaging in this repo (`marketplace.json`, skills tree, CI) is past the “toy scaffold” stage. Remaining P0 work is **org smoke + UX evidence**, not architectural discovery.

| Gate | Result |
| --- | --- |
| Plugin model exists and is documented | **Pass** (Claude + Cursor + skills CLI) |
| Public repo can host marketplace + skills | **Pass** (#32, #34, #36) |
| Lifecycle matrix fillable from vendor docs | **Pass** (see below) |
| Live smoke on NaNLABS machines | **Operator checklist** (Appendix A) |
| Non-tech setup journey | **Operator / pilot** — [#9](https://github.com/nanlabs/agent-toolkit/issues/9) |

## What shipped before this doc

| Deliverable | Evidence |
| --- | --- |
| Marketplace + setup (now inside `nanlabs-core`) | PR [#32](https://github.com/nanlabs/agent-toolkit/pull/32); lineup [#71](https://github.com/nanlabs/agent-toolkit/pull/71) |
| 47 public skills (grouped Agent Skills layout) | PR [#34](https://github.com/nanlabs/agent-toolkit/pull/34) |
| MegaLinter + Danger TS CI | PR [#36](https://github.com/nanlabs/agent-toolkit/pull/36) |
| Public content policy | `docs/PUBLIC_CONTENT_POLICY.md` |
| One agent + one MCP stub | `agents/nanlabs-code-reviewer/`, `mcp/templates/github/` |
| Full agents + MCP stubs | 16 agents under `agents/`; 6 MCP stubs under `mcp/templates/` ([#17](https://github.com/nanlabs/agent-toolkit/issues/17)) |

Removed (2026-08-20): `nanlabs-tech-assistant` is not in this repo and is not bundled on workstation.

## Lifecycle matrix (documented)

Operator-facing commands also live in [`LIFECYCLE.md`](LIFECYCLE.md). Primary sources:

- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Discover / install / auto-update](https://code.claude.com/docs/en/discover-plugins)
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [Cursor plugins](https://cursor.com/docs/plugins)
- [vercel-labs/skills](https://github.com/vercel-labs/skills) (`npx skills`)

### Claude Code

| Concern | Behavior | Notes for NaNLABS |
| --- | --- | --- |
| **Install marketplace** | `/plugin marketplace add nanlabs/agent-toolkit` | Public git repo; no private auth for this catalog |
| **Install plugin** | `/plugin install nanlabs-core@nanlabs-agent-toolkit` | Scopes: user / project / local; setup via `/nanlabs-core:setup` |
| **Update discovery** | `/plugin marketplace update` then `/plugin update` | Third-party auto-update **default off** |
| **Auto-update** | Per-marketplace toggle; org can set `autoUpdate` on `extraKnownMarketplaces` | Prefer **off** for team until pin policy exists |
| **Pin** | Set `version` in `plugin.json` **or** omit → every git SHA is a version | Recommend explicit semver for releases; SHA for fast iteration |
| **Rollback** | No first-class rollback command — pin marketplace/`plugin.json` to prior version or commit SHA, then refresh | Document release tags |
| **Uninstall / disable** | `/plugin uninstall`, `/plugin disable`; `--keep-data` preserves plugin data dir | Cache keeps prior versions ~14 days |
| **Admin policy** | Managed settings: `extraKnownMarketplaces`, `DISABLE_AUTOUPDATER`, `FORCE_AUTOUPDATE_PLUGINS` | Workstation L1 can set env policy later |

### Cursor

| Concern | Behavior | Notes for NaNLABS |
| --- | --- | --- |
| **Install** | Customize panel / Marketplace; local test via `~/.cursor/plugins/local` | Official marketplace = Cursor review |
| **Team marketplace** | Dashboard → Plugins → import GitHub repo (Teams/Enterprise) | Requires org admin + plan |
| **Distribution modes** | Default Off / Default On / **Required** | Required cannot be uninstalled by developers |
| **Update** | Manual Refresh or **Auto Refresh** (GitHub App webhooks, ≤1 index / 10 min) | New plugins may need re-import |
| **Pin / rollback** | Less explicit than Claude — track branch/commit via marketplace refresh | Prefer tagged releases in repo |
| **Admin policy** | Marketplace Access + Organization Groups / SCIM | Enterprise controls |

### `npx skills` (technical multi-agent)

| Concern | Behavior | Notes for NaNLABS |
| --- | --- | --- |
| **Install** | `npx skills add nanlabs/agent-toolkit -g` | Nested `skills/<group>/<skill>` supported |
| **Update** | `npx skills update` / `check` | Reinstalls tracked skills |
| **Remove** | `npx skills remove` | Project or `--global` |
| **Pin / lock** | Project `skills-lock.json`; restore via `experimental_install` / evolving `ci` | Maturing in 2026 — commit lockfiles when used |
| **Agents** | `-a claude-code`, `cursor`, `'*'`, etc. | Same SKILL.md → many clients |

## Decisions recorded

1. **Canonical content** = Agent Skills `SKILL.md` (no workstation `skill.json`).
2. **Grouped layout** `skills/<group>/<skill>/` for navigability + CLI discovery.
3. **Equal priority** for Claude · Claude Code · Cursor IDE · Cursor Agent CLI; skills-only where plugins unavailable.
4. **Versioning:** ship `version` on published plugins; bump on every user-facing change.
5. **Auto-update:** leave third-party marketplaces at vendor default (off) until ops agrees.
6. **Workstation** remains L1 provisioner; do not delete skill SoT until Wave 3–4.

## Residual risks

| Risk | Mitigation |
| --- | --- |
| Cursor team marketplace not yet configured for NaNLABS | Track under Wave 2 / admin task; skills CLI covers tech users |
| Non-tech setup journey | Pilot [#9](https://github.com/nanlabs/agent-toolkit/issues/9); setup ships in `nanlabs-core` |
| Soft public scrub (`~/.local/share/nanlabs`, ClickUp URLs) | Follow-up scrub PRs; policy in `PUBLIC_CONTENT_POLICY.md` |
| Skills lockfile CLI still evolving | Prefer git tags + marketplace pin for Claude |

## Appendix A — Live smoke checklist (operators)

Run once on a disposable profile / machine and paste results into a comment on [#8](https://github.com/nanlabs/agent-toolkit/issues/8):

- [ ] Claude: marketplace add `nanlabs/agent-toolkit`
- [ ] Claude: install `nanlabs-core@nanlabs-agent-toolkit`
- [ ] Claude: `/nanlabs-core:setup` or setup skill; sees Git/Python/package-manager notes
- [ ] Claude: marketplace update + plugin update (or confirm “already latest”)
- [ ] `npx skills add nanlabs/agent-toolkit -g -y` lists expected skills
- [ ] (Optional) Cursor local plugin load from clone / team marketplace import

## Appendix B — Issue mapping

| Issue | Disposition after this pack |
| --- | --- |
| #8 Lifecycle matrix | **Documented** — live smoke remains operator checkbox |
| #10 P0 findings doc | **This file** |
| #7 One agent + MCP | Shipped with this change set |
| #9 Pilots | Still open (human journeys) |
| #5 P0 epic | Ready for HP0 **go** once Appendix A has at least one completed smoke |
