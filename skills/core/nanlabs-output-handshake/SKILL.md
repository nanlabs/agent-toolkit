---
name: nanlabs-output-handshake
description: >-
  WHAT — Default gate for any deliverable: confirm where the final artifact will live and that a human will review, before writing PRDs, TRDs, ADRs, or PR bodies. Storage (repo, wiki, ticket) differs by engagement; never assume a single location.
---

# Output handshake (WHAT)

**Use first** when producing a **final** version of any deliverable that will leave the chat session: PRD, TRD, ADR, work item, planning notes, workflow/validation summary, project assessment, assessment scorecard, evidence map, meeting minutes, decision log, agreement, incident report, spike, or PR/MR body.

## Default behavior (always)

1. **Destination:** Ask explicitly where the final content should live (repo path, wiki page, ticket/Doc, paste-only, or combination). Do **not** default without user or pack guidance.
2. **Review:** State that a **human** must review before the artifact is approved; the assistant does not substitute for that review.
3. Then proceed with the relevant skill (**`nanlabs-prd`**, **`nanlabs-trd`**, **`nanlabs-adr`**, **`nanlabs-work-item`**, **`nanlabs-planning`**, **`nanlabs-development-workflow`**, **`nanlabs-project-assessment`**, **`nanlabs-project-assessment-evidence`**, **`nanlabs-technical-unit-assessment`**, **`nanlabs-management-unit-assessment`**, **`nanlabs-meeting-minutes`**, **`nanlabs-decision-log`**, **`nanlabs-agreement`**, **`nanlabs-incident`**, **`nanlabs-spike`**, **`nanlabs-pr-fallback`** + forge workflow, etc.).

## Boundaries

- This skill does not contain org templates; those stay in the specific artifact skills and their `references/default-template.md` files.

## See also

- `nanlabs-workflow-generic-project`, delivery gates
- `nanlabs-assistant`, discover existing `docs/`, PR templates, `AGENTS.md`
