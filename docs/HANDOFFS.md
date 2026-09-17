> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Handoffs

Subagents in this repository are **user-driven** (invoked in Claude Code or
Cursor). They are not autonomous agents. Cloud has no native subagents: the
matching **skill** is the Cloud counterpart.

| Term | Meaning here |
| --- | --- |
| Subagent | User-invoked persona under `agents/` (Code / Cursor) |
| Skill | Portable procedure under `plugins/nanlabs-<group>/skills/` (every surface, including Cloud) |
| Autonomous agent | Out of scope for this repo |

`nanlabs-assistant` routes. Packs ([`PACKS.md`](PACKS.md)) group the skills to
install. This page is the output contract between those pieces.

## Defaults

| Role | Skill fallback (Cloud) | Subagent (Code / Cursor) | Output |
| --- | --- | --- | --- |
| Router | `nanlabs-assistant` | `nanlabs-assistant` | Next skill or agent named in one line |
| Planner | `nanlabs-planning` | `nanlabs-planner` | Markdown plan **and** a self-contained HTML file; ask destination via `nanlabs-output-handshake` |
| Implementer | repo workflow + forge skills | (harness implementer / builder) | Code + tests; no plan rewrite |
| Architect | `nanlabs-adr`, `nanlabs-trd` | `nanlabs-architect` | ADR/TRD-shaped design, then handshake |
| Reviewer | `github-cli-workflow`, `gh-address-comments` | `nanlabs-code-reviewer` | Review **on the pull request**, not only in chat |
| Designer | `figma`, `ui-ux-pro-max` | — | Design-to-code or Figma MCP; no separate designer agent |

If a harness has no handoff primitive, write the artifact in markdown (or HTML
for plans) and say what the next skill should do with it.

## Planner

1. Produce the markdown contract in `agents/nanlabs-planner/references/CONTRACT.md`.
2. Also write a **self-contained HTML** file of the same plan (inline CSS, no
   external assets) so the user can open it in a browser.
3. Before writing the file, run **`nanlabs-output-handshake`**: where does the
   HTML live (repo path, gist, paste-only)?
4. Stop for explicit approval. Do not implement.

## Reviewer

1. Produce the markdown contract in `agents/nanlabs-code-reviewer/references/CONTRACT.md`.
2. If a GitHub pull request exists for the current branch, **post the review
   on that PR** (`gh pr review` and/or `gh pr comment`; use
   `github-cli-workflow` / `gh-address-comments`).
3. If there is no PR, say so and keep the review in chat, then offer to open
   a draft PR.
4. Do not treat a chat-only summary as the deliverable when a PR is available.

## Cloud

Do not invent a Cloud runtime. Install the pack’s skills. Name the Code/Cursor
agent only as optional follow-up.

## Related

- [`catalogs/pack-catalog.yaml`](../catalogs/pack-catalog.yaml)
- [`plugins/nanlabs-core/skills/nanlabs-assistant/references/ORCHESTRATION.md`](../plugins/nanlabs-core/skills/nanlabs-assistant/references/ORCHESTRATION.md)
- [`plugins/nanlabs-core/skills/nanlabs-output-handshake/SKILL.md`](../plugins/nanlabs-core/skills/nanlabs-output-handshake/SKILL.md)
