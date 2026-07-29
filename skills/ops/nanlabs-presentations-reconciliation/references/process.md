## Process (7 Steps)

### Step 1, Pull calendar events

Use the `gws-calendar` skill to fetch all Thursday 12–13hs events from `ulises.cornejo@nan-labs.com`.
Typical date range: last 18 months to next 3 months.

> Events have attachments in the format `"<title> -> <url>"`, parse with `.split(" -> ")`.
> There is no separate calendar for talks, they are in the primary calendar filtered by day/time.

Save output to `/tmp/all_calendar_events.ndjson`.

### Step 2, Pull ClickUp tasks

```bash
clickup task list --list-id 901702403034 --json > /tmp/clickup_presentations.json
```

For large lists (>100 tasks), paginate:

```bash
clickup task list --list-id 901702403034 --json --limit 100 --page 0
clickup task list --list-id 901702403034 --json --limit 100 --page 1
```

### Step 3, Cross-reference calendar ↔ ClickUp

Match calendar events to ClickUp tasks by:
1. **Exact title** (normalized: lowercase, strip emoji and punctuation)
2. **Date** (same Thursday)
3. **Fuzzy title** (Levenshtein ≤ 3, or token overlap ≥ 60%)

> ⚠️ Always verify matches by comparing task name vs event title side-by-side.
> If they differ significantly (different topics on the same date), treat as `NO_MATCH` and flag for manual review.

Save to `/tmp/cross_reference.json`.

### Step 4, Identify gaps

- Calendar event with `NO_MATCH` → create new ClickUp task (→ Step 5)
- Calendar event with `MATCH` but missing fields → update task (→ Step 6)
- ClickUp task `confirmed`/`delivered` with no calendar match → flag for manual review

### Step 5, Create missing tasks

```bash
clickup task create \
  --list-id 901702403034 \
  --name "<Event Title>" \
  --status "delivered" \
  --due-date "<YYYY-MM-DD>"
```

> **Important:** the CLI defaults to `proposal` status. Always set `--status "delivered"` explicitly,
> then verify the task was created with the correct status.

After creating, add the bot comment:

```bash
clickup comment add <task-id> \
  "🤖 Automatically updated by Ulises' AI Agent as part of the Presentations list reconciliation."
```

### Step 6, Update custom fields

```bash
# Video link (from calendar attachment titled "Recording")
clickup task edit <task-id> \
  --field "Video Link=<drive-or-youtube-url>"

# External minutes (from calendar attachment "Notes by Gemini")
clickup task edit <task-id> \
  --field "📝 External Minutes=<docs-url>"

# Talk type, use EXACT value including trailing spaces
clickup task edit <task-id> \
  --field "Qué tipo de charla vas a dar?=Light talk  "

# Category
clickup task edit <task-id> \
  --field "Categoría del contenido=Technical"

# Description, NOTE: field name has 1 trailing space
clickup task edit <task-id> \
  --field "Contanos en un párrafo corto de qué va la charla =<description>"
```

After updating any task, add the bot comment (if not already present):

```bash
clickup comment add <task-id> \
  "🤖 Automatically updated by Ulises' AI Agent as part of the Presentations list reconciliation."
```

### Step 7, Fix statuses

Delivered talks must have status `delivered`.

```bash
# Single task
clickup task edit <task-id> --status "delivered"

# Multiple tasks at once
clickup task edit 86abc1 86abc2 86abc3 --status "delivered"
```

---

## Inference Rules for Talk Type / Category

| Signal in title or content | Talk Type | Category |
|----------------------------|-----------|----------|
| "Open Mic" in title | `Open Mic` | `Conversational` |
| `[BPS]` prefix | `Geek club` | `Technical` |
| Deep technical (two speakers, production-ready) | `Geek club` | `Technical` |
| Light tips / intro / how-to format | `Light talk  ` | `Technical` |
| Personal finance, climate, wellbeing, soft topics | `Light talk  ` | `Soft skills` |
| NaNLABS internal process or org topic | `Light talk  ` | `Organizational` |
| "how to present", meta-learning | `Light talk  ` | `Organizational` |

When in doubt, default to `Light talk  ` / `Technical`.

---

## Known Gotchas

1. **Trailing spaces in field names and values**, `"Contanos en un párrafo corto de qué va la charla "` and `"Light talk  "` both have trailing spaces. Use exact strings or edits will silently fail.

2. **Default status on create**, `clickup task create` always defaults to `proposal`. Always pass `--status "delivered"` and verify after.

3. **False-positive cross-references**, Two different talks can fall on the same Thursday. Always compare the task name and event title before updating. Flag mismatches for manual review.

4. **Dropdown values in API responses**, A set dropdown returns an integer (`orderindex`). An unset field returns the full `type_config` dict. When reading field values in code, use `if val is None or isinstance(val, dict)` to detect "unset", never `if not val`.

5. **Calendar attachments format**, Attachments are plain strings: `"<title> -> <url>"`. Parse by splitting on `" -> "`.

6. **No dedicated calendar**, Talk events live in the primary calendar `ulises.cornejo@nan-labs.com`. Filter by weekday (Thursday) and time (12:00–13:00 GMT-3).

---

## Verification

After the reconciliation run, verify:

- [ ] All calendar events from the date range have a corresponding ClickUp task
- [ ] All tasks with a matching calendar event have `Video Link` set (if a recording exists)
- [ ] All tasks with a matching calendar event have `📝 External Minutes` set (if notes exist)
- [ ] All delivered tasks have status `delivered`
- [ ] Bot comment added to all updated/created tasks
- [ ] Flagged mismatches documented and handed off for manual review

---

## Temporary Files

| File | Contents |
|------|----------|
| `/tmp/all_calendar_events.ndjson` | Raw calendar events fetched from Google Calendar |
| `/tmp/clickup_presentations.json` | All ClickUp tasks from the Presentations list |
| `/tmp/cross_reference.json` | Cross-reference result: calendar event → ClickUp task match/status |
