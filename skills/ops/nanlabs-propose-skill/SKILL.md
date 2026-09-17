---
name: nanlabs-propose-skill
description: >-
  HOW — Propose a new public skill or agent to nanlabs/agent-toolkit via GitHub.
  Use when sharing a local skill, checking for duplicates, opening a contribution
  issue, or preparing a pull request for maintainers to review.
metadata:
  author: nanlabs
  version: "1.0"
---

# Propose a skill (NaNLABS)

Walk a contributor through the GitHub contribution flow for this public
repository: check duplicates, scrub private content, open an issue, and submit
a pull request. Maintainers approve; merge makes the skill installable via
`npx skills`.

This is the artisan equivalent of a share-then-approve loop. GitHub remains
the source of truth. There is no separate sharing platform.

## When to use

- Someone wants to share a skill they use locally
- A user asks how to contribute a skill or agent to agent-toolkit
- A maintainer is reviewing a proposed skill and needs the checklist

## Do not use

- To publish client-confidential or internal-only procedures (see
  `docs/PUBLIC_CONTENT_POLICY.md`)
- To add empty `packs/` directories or README-only placeholders
- To bypass CODEOWNERS review

## Procedure

1. **Destination handshake** — Confirm the artifact is a public PR against
   `nanlabs/agent-toolkit`. If the content cannot be public, stop.
2. **Duplicate check** — Search `catalogs/skill-catalog.yaml`,
   `catalogs/pack-catalog.yaml`, `catalogs/agent-catalog.yaml`, and
   `skills/<group>/` for the same job. If a skill already covers it, propose
   an improvement to the existing skill instead of a new name.
3. **Author** — Follow `docs/AUTHORING.md` and `docs/CONTRIBUTION.md`.
   Layout: `skills/<group>/<skill>/SKILL.md` with kebab-case `name` matching
   the directory.
4. **Pack membership** — Add the skill to `catalogs/skill-catalog.yaml` and
   `catalogs/skills-layout.json`. If it belongs in a domain pack, update
   `catalogs/pack-catalog.yaml`. Run `python3 scripts/validate-pack-catalog.py`.
5. **Issue** — Open a GitHub issue with the **Propose skill** template
   (`.github/ISSUE_TEMPLATE/propose-skill.yml`).
6. **Pull request** — Branch from `main`, fill `.github/PULL_REQUEST_TEMPLATE.md`
   including the Skill/Agent checklist, and link the issue (`Fixes #N`).
7. **Handoff** — Tell the contributor that CODEOWNERS
   (`@nanlabs/internal-maintainers`, `@nanlabs/oss-core-team`) review for
   security, duplication, quality, and pack membership. After merge the skill
   is installable:

   ```bash
   npx skills add nanlabs/agent-toolkit@<skill-name>
   ```

## Review bar (maintainers)

Read `references/REVIEW-CHECKLIST.md` before approving. Reject secrets,
duplicates, placeholder directories, and Cloud-hostile instructions that
assume native subagents without a skills fallback.

## Related

- `docs/CONTRIBUTION.md` — human-readable flow
- `docs/PACKS.md` — installable domain packs
- `docs/HANDOFFS.md` — output contracts
- `github-cli-workflow` — draft the PR
