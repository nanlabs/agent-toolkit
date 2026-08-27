---
name: nanlabs-presentations-reconciliation
description: Reconcile the NaNLABS ClickUp Presentations list against Google Calendar Thursday events. Creates missing tasks; updates Video Link, External Minutes, talk type, category, and description fields. Use after a batch of delivered talks.
---

# NaNLABS Presentations List Reconciliation

Use this skill to keep the **ClickUp Presentations list** (`Learning / R&D` space) synchronized with the Google Calendar Thursday talk events. Run after each batch of delivered talks or whenever the list feels out of date.

## When to Use

- User says "reconcile the presentations list" or "update the presentations list"
- A batch of Thursday talks has passed and ClickUp is missing entries or has stale fields
- You need to bulk-update Video Link, External Minutes, talk type, category, or description across multiple tasks
- Periodic maintenance (e.g., monthly)

## Resources

| Item | Value |
|------|-------|
| ClickUp list | Presentations (list ID `901702403034`) |
| ClickUp space | Learning / R&D (space ID `90170461556`) |
| Google Calendar | `ulises.cornejo@nan-labs.com`, Thursdays 12–13hs |
| Official procedure | NaNLABS Presentation Management (ask internally for the current ClickUp link) |

## Custom Fields Reference

| Field Name | Field ID | Type | Notes |
|------------|----------|------|-------|
| `Qué tipo de charla vas a dar?` | `b57c9c3e-b933-40bb-94be-bb0aa735f168` | dropdown | Options: `"Light talk  "` (**2 trailing spaces!**), `"Geek club"`, `"Open Mic"` |
| `Categoría del contenido` | `32eb4ce6-727a-4555-aa24-0c71f17c11a7` | dropdown | Options: `"Technical"`, `"Soft skills"`, `"Organizational"`, `"Conversational"` |
| `Contanos en un párrafo corto de qué va la charla ` | `0b12f91a-af5d-4cc1-bdb3-f8bc006439ad` | text | **1 trailing space in name**, use exact string |
| `Video Link` | `1d7c06e4-a23d-41a7-8700-39f0533e2273` | url | YouTube or Drive recording URL |
| `📝 External Minutes` | `a0de4f84-7193-4931-991b-b9d1996bcd6d` | url | Google Docs "Notes by Gemini" or meeting notes |
| `Quién da la charla?` | `eadce3de-5e2e-4499-a0c9-08d9a63cdc32` | users | Speaker(s) |
| `Presentation` | `3321b2b5-7d6a-4106-8c10-09f3b78d0830` | url | Slides link |

---

## Reference

See `references/process.md` for the full procedure.
