> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Packs

A **pack** is a named, installable slice of this repository: a `skills/<group>/`
subdirectory, or a cross-group list of skills (and optional agents). Packs are
**catalog aliases**, not a `packs/` directory tree.

Machine catalog: [`catalogs/pack-catalog.yaml`](../catalogs/pack-catalog.yaml).

GitHub issues `#24`, `#25`, and `#28` still track **outcome-pack content**
(deeper QA, DevOps golden stacks, and similar). This catalog is the
discovery, install, and governance slice.

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
# 1. Group pack (subdirectory of skills/)
npx skills add nanlabs/agent-toolkit/skills/delivery

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

Pin a tag with a full GitHub URL when you need a release:

```bash
npx skills add https://github.com/nanlabs/agent-toolkit/tree/v0.3.1/skills/delivery
```

## Group packs

One-to-one with `skills/<group>/`. Install the subdirectory.

| Pack | Path | Coverage |
| --- | --- | --- |
| `core` | `skills/core/` | high |
| `delivery` | `skills/delivery/` | high |
| `design` | `skills/design/` | medium |
| `forge` | `skills/forge/` | high |
| `data` | `skills/data/` | medium |
| `integrations` | `skills/integrations/` | medium |
| `ops` | `skills/ops/` | medium |
| `tooling` | `skills/tooling/` | low |
| `workflow` | `skills/workflow/` | high |

```bash
npx skills add nanlabs/agent-toolkit/skills/<group>
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

1. Edit `catalogs/pack-catalog.yaml` (no empty directories).
2. Point only at skills and agents that already exist.
3. Run `python3 scripts/validate-pack-catalog.py`.
4. Document the pack here if it is user-facing.

Contribution flow: [`CONTRIBUTION.md`](CONTRIBUTION.md).
