---
name: nanlabs-meeting-minutes
description: >-
  WHAT - Create structured meeting minutes from notes or transcripts using NaNLABS meeting templates, with redaction, action items, decisions, and traceability.
---

# Meeting Minutes (WHAT)

Use for meeting notes, validation meetings, or AI-assisted transcript summarization.

## Default guardrails

1. Apply **`nanlabs-output-handshake`** before final output.
2. Redact PII and sensitive details before finalizing.
3. Keep minutes concise and actionable.
4. Extract action items, owners, due dates, and linked task IDs when available.
5. Use **`clickup-cli`** to create follow-up tasks only after user approval.

## References

- `references/default-template.md`
- `references/example-weekly-sync.md` — example meeting minutes with action items and decisions
- `nanlabs-decision-log`
- `nanlabs-agreement`
