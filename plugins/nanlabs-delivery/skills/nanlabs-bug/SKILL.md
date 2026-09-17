---
name: nanlabs-bug
description: >-
  WHAT - Draft and review bugs using the NaNLABS Bug Template; classifies whether an issue should be escalated to incident based on production/user impact.
---

# Bug (WHAT)

Use for defects that can be handled through the normal development workflow.

## Bug vs incident rule

Route to **`nanlabs-incident`** instead if the problem impacts production or live users now, degrades service, blocks critical business operations, creates client-reported urgency, or needs immediate response outside planning cycles.

## Default guardrails

1. Apply **`nanlabs-output-handshake`** before final output.
2. Capture reproduction steps and environment details.
3. Use **`clickup-cli`** for ClickUp writes only after approval.

## References

- `references/default-template.md`
- `references/example-search-filter-bug.md` — example bug with environment details, diagnostics, and severity assessment
- `nanlabs-incident`, when to escalate to incident
