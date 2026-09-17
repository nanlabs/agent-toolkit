---
name: nanlabs-workflow-generic-project
description: >-
  WHAT — Generic client delivery: Jira or ClickUp, full repo context, human gates, English traceability
  on tickets, draft PR via delegated forge skills. Use workspace packs for client/account overlays.
---

# Workflow — Generic Project (WHAT)

**All skill instructions, ticket comments, and PR text must be in English.**

This workflow supports client delivery phases and gates. Apply any client/account constraints by loading the appropriate workspace pack first.

## Mode selection (mandatory)

- Use **this skill** for client delivery phases and gates.
- If the task is in a specific client/account context, load the corresponding workspace pack overlay first.
- If unclear → **ask** which engagement context to use before proceeding.

## Delegation (HOW lives in tool skills)

Consult **`skill-catalog.yaml`** for the full map. Common pairs for this workflow:

- Discovery → **nanlabs-assistant**
- Artifact gate → **nanlabs-output-handshake** (before final deliverables and PR/MR text)
- Planning / validation → **nanlabs-planning**, **nanlabs-development-workflow**
- Work items / docs / assessments → matching **nanlabs-*** WHAT skill from the catalog
- Tickets → **clickup-cli** or external jira/confluence packs
- Forge → **github-cli-workflow** / **gitlab-cli-workflow** (body: **nanlabs-pr-fallback** when no repo template)

Do **not** paste forge or ticket CLI sequences here; open the tool skill and follow it.

## Principles

1. **Context:** Pull Jira, ClickUp, Confluence, and linked docs the task references; treat them as source of truth with the codebase (**nanlabs-assistant** inspection order).
2. **Repo standards:** Follow `AGENTS.md`, CONTRIBUTING, PR templates, and documented Docker or devcontainer flows.
3. **Human in the loop:** Confirm understanding and plan **before** substantial implementation; get explicit approval **before** finalizing PR text; escalate when context is missing.
4. **Validation first:** Align on acceptance criteria and approach before deep implementation.
5. **Traceability:** Add concise English comments on the **original** Jira issue or ClickUp task for plan approval, meaningful milestones, and PR link—no duplicate full PR bodies in tickets.

## Phases (gates)

1. **Intake:** Identify ticket IDs and engagement context; retrieve linked docs via appropriate skills.
2. **Discovery:** Analyze repo per **nanlabs-assistant**; note CI, templates, dev environments.
3. **Plan:** Written plan → **stop for user approval.** No implementation until approved.
4. **Plan traceability:** After plan approval, post a short ticket comment (delegate comment mechanism to **clickup-cli**, **jira-*** or **confluence-*** as applicable).
5. **Implement:** Work in logical commits per repo conventions; self-review.
6. **Push and draft PR/MR:** Push branch, then invoke **github-cli-workflow** or **gitlab-cli-workflow** for a **draft**; confirm title/body with the user.
7. **Close loop:** Post final short ticket comment with PR link (via same ticket skills as above).

## Branch naming (intent)

Prefer **`<short-username>/<WORK_ITEM_ID>-<short-slug>`** (lowercase). Resolve username per repo or user preference; base branch per repo default (**main**, **develop**, etc.).

## Session override

If the user requests **local-only** work: skip push/PR automation; note limitations in ticket updates if still posting.

## Safety

- Never commit secrets; no force-push to shared defaults unless the user explicitly requests recovery steps.

## Checklist

- [ ] Engagement context (if any) confirmed
- [ ] Work item + doc context retrieved
- [ ] Plan approved before code; ticket comment after plan approval
- [ ] Repo standards (template, devcontainer) respected
- [ ] Draft PR/MR via **github-cli-workflow** or **gitlab-cli-workflow** (or documented fallback)
- [ ] Final traceability comment with PR link when applicable
