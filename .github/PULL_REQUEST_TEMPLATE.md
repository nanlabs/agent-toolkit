## Description

Summary of the change and the related issue.

Fixes #

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update
- [ ] Refactor
- [ ] Chore (CI, tooling, governance, templates)

## Public-repo checklist

- [ ] No secrets, tokens, private URLs, or client data
- [ ] New skills/plugins marked public-safe (see `docs/PUBLIC_CONTENT_POLICY.md`)
- [ ] Manifests still validate (`python3 scripts/validate-manifests.py`)

## How Has This Been Tested?

- [ ] `python3 scripts/validate-manifests.py`
- [ ] `python3 scripts/validate-skills.py`
- [ ] `python3 scripts/validate-pack-catalog.py` (if catalogs or packs changed)
- [ ] `bash scripts/secret-scan.sh`
- [ ] Relevant workflow(s) reviewed

## Skill / Agent checklist

Fill when the PR adds or changes `skills/` or `agents/`. Mark N/A items with a note in Description.

- [ ] Not a duplicate of an existing catalog skill or agent
- [ ] Pack membership recorded in `catalogs/pack-catalog.yaml` (or N/A)
- [ ] Handoff / output contract documented (or N/A; see `docs/HANDOFFS.md`)
- [ ] Cloud-safe as skills-only (or documented Code/Cursor-only)
- [ ] `docs/PUBLIC_CONTENT_POLICY.md` satisfied

## Checklist

- [ ] Self-reviewed
- [ ] Docs updated when behavior changed
- [ ] No new warnings from local validation
