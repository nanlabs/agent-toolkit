---
name: nanlabs-propose-skill
description: >-
  HOW — Propose a new public skill or agent to the GitHub repository
  nanlabs/agent-toolkit (https://github.com/nanlabs/agent-toolkit). Use when
  sharing a local skill, checking for duplicates, opening a contribution issue,
  or preparing a pull request against that repo for maintainers to review.
metadata:
  author: nanlabs
  version: "1.2"
---

# Propose a skill (NaNLABS)

Walk a contributor through proposing a skill or agent to **NaNLABS
agent-toolkit**, not to whatever repo they happen to have open.

## Target repository

| | |
| --- | --- |
| GitHub | **[nanlabs/agent-toolkit](https://github.com/nanlabs/agent-toolkit)** |
| Clone | `git clone https://github.com/nanlabs/agent-toolkit.git` |
| Default branch | `main` |
| After merge | installable with `npx skills add nanlabs/agent-toolkit@<skill-name>` |

Issues and pull requests **must** target `nanlabs/agent-toolkit`. If the
current workspace is a client project or `internal-workstation`, clone or
worktree **agent-toolkit** and open the PR there. Do not add NaNLABS public
skills to the user's application repo.

Paths below (`docs/`, `catalogs/`, `skills/`) are relative to
`nanlabs/agent-toolkit`.

This is the artisan equivalent of a share-then-approve loop. GitHub remains
the source of truth. There is no separate sharing platform.

## When to use

- Someone wants to share a skill they use locally into **nanlabs/agent-toolkit**
- A user asks how to contribute a skill or agent to agent-toolkit
- A maintainer is reviewing a proposed skill on that repo and needs the checklist

## Do not use

- To publish client-confidential or internal-only procedures (see
  `docs/PUBLIC_CONTENT_POLICY.md` in **nanlabs/agent-toolkit**)
- To add empty `packs/` directories or README-only placeholders
- To treat a pack as an Agent Plugins package (`plugin.json` under `plugins/`)
- To bypass CODEOWNERS review
- To open the contribution PR against any other repository

## Procedure

1. **Destination handshake** — Confirm the artifact is a public issue + PR
   against **https://github.com/nanlabs/agent-toolkit**. If the content cannot
   be public, stop. If the session is not in a checkout of that repo, clone it
   (or add a worktree) before editing.
2. **Duplicate check** — In **nanlabs/agent-toolkit**, search
   `catalogs/skill-catalog.yaml`, `catalogs/pack-catalog.yaml`,
   `catalogs/agent-catalog.yaml`, and `skills/<group>/` for the same job. If a
   skill already covers it, propose an improvement to the existing skill
   instead of a new name.
3. **Author** — Follow `docs/AUTHORING.md` and `docs/CONTRIBUTION.md` in
   **nanlabs/agent-toolkit**. Layout: `skills/<group>/<skill>/SKILL.md` with
   kebab-case `name` matching the directory. That nested group tree is for
   Agent Skills / `npx skills`. [Agent Plugins](https://agent-plugins.org/specification)
   v1 discovers only immediate `plugins/<id>/skills/<name>/SKILL.md`. Do **not**
   add `plugin.json` or `plugins/<pack-id>/` for a catalog pack. Core plugin
   skills are mirrored from `skills/core/` by `gen-surfaces`.
4. **Pack membership** — Add the skill to `catalogs/skill-catalog.yaml` and
   `catalogs/skills-layout.json`. If it belongs in a domain pack, update
   `catalogs/pack-catalog.yaml`. Run `python3 scripts/validate-pack-catalog.py`.
   If you changed `plugins/`, also run
   `python3 scripts/validate-agent-plugins.py`.
5. **Issue** — Open a GitHub issue **on nanlabs/agent-toolkit** with the
   **Propose skill** template
   (`https://github.com/nanlabs/agent-toolkit/issues/new?template=propose-skill.yml`).
6. **Pull request** — Branch from `main` **in nanlabs/agent-toolkit**, fill
   `.github/PULL_REQUEST_TEMPLATE.md` including the Skill/Agent checklist (and
   the Agent Plugins checklist if `plugins/` changed), and
   link the issue (`Fixes #N`). Create the PR against
   `https://github.com/nanlabs/agent-toolkit` (`base: main`).
7. **Handoff** — Tell the contributor that CODEOWNERS on that repo
   (`@nanlabs/internal-maintainers`, `@nanlabs/oss-core-team`) review for
   security, duplication, quality, and pack membership. After merge the skill
   is installable:

   ```bash
   npx skills add nanlabs/agent-toolkit@<skill-name>
   ```

## Review bar (maintainers)

Read `references/REVIEW-CHECKLIST.md` before approving a PR **on
nanlabs/agent-toolkit**. Reject secrets, duplicates, placeholder directories,
and Cloud-hostile instructions that assume native subagents without a skills
fallback.

## Related

- `https://github.com/nanlabs/agent-toolkit` — contribution target
- `docs/CONTRIBUTION.md` — human-readable flow (in that repo)
- `docs/PACKS.md` — installable domain packs
- `docs/AGENT_PLUGINS.md` — portable vs native plugins
- `docs/HANDOFFS.md` — output contracts
- `github-cli-workflow` — draft the PR against **nanlabs/agent-toolkit**
