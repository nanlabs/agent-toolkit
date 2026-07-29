---
name: nanlabs-pr-fallback
description: >-
  WHAT, Structure the pull-request body with the NaNLABS default in references/pr-body-default.md when the repo has no GitHub PR template. Pair with nanlabs-output-handshake and github-cli-workflow. Does not open the PR; HOW stays in the forge skill.
---

# PR body, default when no repo template (WHAT)

## When to use

- Remote is **GitHub** and **`nanlabs-assistant`** (or a file search) shows **no** `PULL_REQUEST_TEMPLATE` / `pull_request_template` under `.github/`.
- You need a **reasonable default** for `gh pr create --body-file` until the repo adds its own template.

## Instructions

1. Run **`nanlabs-output-handshake`**: user confirms where the final description will live (e.g. `body.md` for `gh`, paste-only) and that a **human** will review.
2. If the repository adds a template later, **prefer the repo** over this file.
3. Copy sections from **`references/pr-body-default.md`**, fill placeholders (issue id, test notes), and pass the path to **`github-cli-workflow`**.

## GitLab

If there is no `.gitlab/merge_request_templates/`, you may use the same Markdown structure in the **merge request description** for consistency, subject to the user’s **destination** choice (MR description field, file, etc.) and **`nanlabs-output-handshake`**.

## What not to do

- Do not **assume** a PR is always in ClickUp; the canonical **guidelines** live in ClickUp, the **file** the user points to is wherever they said in the handshake.


## Default guardrails

1. Apply **nanlabs-output-handshake** before final output.
2. Use **skill-catalog.yaml** for routing to HOW skills.

## References

- `references/pr-body-default.md`, local copy of the default body
- [ClickUp: Guidelines for Creating PRs](https://app.clickup.com/459857/v/dc/e12h-247177?page=e12h-103657)
- `nanlabs-development-workflow`, default PR validation and DoD expectations
- `github-cli-workflow`, draft PR creation
- `gitlab-cli-workflow`, GitLab MRs
