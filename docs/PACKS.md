> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Packs

A **pack** is a named, installable slice of this repository: a group plugin
directory (`plugins/nanlabs-<group>/skills/`), or a cross-group list of skills
(and optional agents). Domain packs are **catalog aliases**, not a `packs/`
directory tree. Group packs map 1:1 onto Agent Plugins packages.

Machine catalog: [`catalogs/pack-catalog.yaml`](../catalogs/pack-catalog.yaml).

GitHub issues `#24`, `#25`, and `#28` still track **outcome-pack content**
(deeper QA, DevOps golden stacks, and similar). This catalog is the
discovery, install, and governance slice.

## Packs vs Agent Plugins

This repository ships **two** install shapes. Group packs and group plugins are the same directories.

| | Domain packs | Group plugins / group packs |
| --- | --- | --- |
| Spec | [Agent Skills](https://agentskills.io/specification) + `npx skills --skill` | [Agent Plugins](https://agent-plugins.org/specification) + `npx skills` path |
| Unit | Named skill list | Directory with root `plugin.json` |
| Skill discovery | `--skill` names (CLI recurses) | **Immediate** `plugins/<id>/skills/<name>/SKILL.md` only (§7.1) |
| Manifest | `catalogs/pack-catalog.yaml` | Closed `plugin.json` (`$schema`, `name`, metadata; no `skills`/`agents` path fields) |
| Agents | Optional Code/Cursor personas | **Not** a v1 portable component (`nanlabs-agents` is native) |
| MCP | Not part of a pack | Optional root `mcp.json` only (none shipped) |

A domain pack MUST NOT add `plugin.json` and MUST NOT live as `plugins/<pack-id>/`.
Group plugins already are the skill tree — `gen-surfaces` does not copy skills.
Install a plugin with Copilot/Claude/Cursor/VS Code marketplace flows; install a
domain pack with `npx skills --skill`. See [`AGENT_PLUGINS.md`](AGENT_PLUGINS.md).

## Why packs (not personas)

Install “the pack of X” for a job (code review, delivery, QA). Personas remain
agent files under `agents/` for Claude Code and Cursor. Cloud has no native
subagents, so Cloud users install **skills only**.

| Surface | What a pack installs |
| --- | --- |
| Cloud / skills-only | Skills via `npx skills` |
| Claude Code / Cursor | Skills, plus agents when the pack lists them (`nanlabs-agents` plugin or a checkout) |

## Two-command trial

From a project directory:

```bash
# 1. Group pack (plugin skills directory)
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills

# 2. Domain pack (explicit skill filter)
npx skills add nanlabs/agent-toolkit --skill github-cli-workflow --skill gh-address-comments --skill gh-fix-ci --skill nanlabs-pr-fallback
```

Equivalent helper (requires a clone and `pyyaml`):

```bash
bash scripts/install-pack.sh delivery
bash scripts/install-pack.sh code-review -y
bash scripts/install-pack.sh --list
```

`scripts/install-pack.sh` expands the catalog and runs `npx skills`. Extra
flags after the pack id are forwarded (`-g`, `-y`, `--agent`).

Pin a tag with a full GitHub URL when you need a release. Tags after this
layout use the plugin skills directory; `v0.3.1` still used `skills/delivery`.

```bash
npx skills add https://github.com/nanlabs/agent-toolkit/tree/<tag>/plugins/nanlabs-delivery/skills
```

## Group packs

One-to-one with `plugins/nanlabs-<group>/skills/`. Install the plugin directory.

| Pack | Path | Coverage |
| --- | --- | --- |
| `core` | `plugins/nanlabs-core/skills/` | high |
| `delivery` | `plugins/nanlabs-delivery/skills/` | high |
| `design` | `plugins/nanlabs-design/skills/` | medium |
| `forge` | `plugins/nanlabs-forge/skills/` | high |
| `data` | `plugins/nanlabs-data/skills/` | medium |
| `integrations` | `plugins/nanlabs-integrations/skills/` | medium |
| `ops` | `plugins/nanlabs-ops/skills/` | medium |
| `tooling` | `plugins/nanlabs-tooling/skills/` | low |
| `workflow` | `plugins/nanlabs-workflow/skills/` | high |

```bash
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-<group>/skills
```

## Domain packs

Named jobs that may span groups. Cloud still gets skills only.

| Pack | Skills (installable) | Agents (Code / Cursor) | Coverage |
| --- | --- | --- | --- |
| `code-review` | `github-cli-workflow`, `gh-address-comments`, `gh-fix-ci`, `nanlabs-pr-fallback` | `nanlabs-code-reviewer`, `nanlabs-security-reviewer`, `nanlabs-typescript-reviewer` | medium |
| `qa` | `playwright-cli` | `nanlabs-e2e-runner` | low |
| `architect` | `nanlabs-adr`, `nanlabs-trd` | `nanlabs-architect` | medium |
| `staff` | `nanlabs-presentations-reconciliation` | — | low |
| `contribute` | `nanlabs-propose-skill` | — | n/a |

Low coverage is intentional: the catalog names the gap; it does not invent
skills. See [`COVERAGE.md`](COVERAGE.md).

## Assistant routing

`nanlabs-assistant` remains the router. Prefer a pack name when the user asks
to “install / use the pack of X”. Handoffs: [`HANDOFFS.md`](HANDOFFS.md).

## Adding or changing a pack

1. Edit `catalogs/pack-catalog.yaml` (no empty directories, no `plugin.json`).
2. Point only at skills and agents that already exist.
3. Do not create `plugins/<pack-id>/` for a **domain** pack. Group plugins
   already exist as `plugins/nanlabs-<group>/`.
4. Run `python3 scripts/validate-pack-catalog.py` and, if you touched
   `plugins/`, `python3 scripts/validate-agent-plugins.py`.
5. Document the pack here if it is user-facing.

Contribution flow: [`CONTRIBUTION.md`](CONTRIBUTION.md).
