# ClickUp CLI: comments git time

```bash
# Add a comment (supports @mentions — resolves usernames to ClickUp user tags)
clickup comment add CU-abc123 "Looks good, @alice please review"

# List comments (newest first — .[0] is most recent, .[-1] is oldest)
clickup comment list CU-abc123

# Edit/delete comments (you can only edit comments you authored)
clickup comment edit <comment-id> "Updated text"
clickup comment delete <comment-id>
```

## Git & GitHub Integration

The CLI auto-detects task IDs from git branch names. Branch naming convention: `feature/CU-abc123-description` or `CU-abc123/description`.

```bash
# Link a GitHub PR to a ClickUp task
clickup link pr
clickup link pr --task CU-abc123

# Link a specific PR number to a task (useful after merging)
clickup link pr 42 --task CU-abc123

# Link current branch
clickup link branch

# Link a commit
clickup link commit

# Sync ClickUp task info to GitHub PR description
clickup link sync
clickup link sync --task CU-abc123
clickup link sync 42 --repo owner/repo --task CU-abc123
```

Links are stored in the task's markdown description as rich-text with clickable URLs.

**Note:** When `--task` is specified but no PR number, the CLI first tries the current branch's PR, then searches for PRs matching the task ID in their branch name. This works even after merging when the feature branch is deleted.

**Auto-detection:** `task view` can detect the associated ClickUp task even on branches without task IDs by finding the branch's GitHub PR URL in task descriptions.

## Time Tracking

```bash
# Log time to a task (auto-detects from git branch)
clickup task time log --duration 2h
clickup task time log 86abc123 --duration 1h30m --description "Implemented auth flow"

# Log time for a specific date
clickup task time log --duration 45m --date 2025-01-15

# Log billable time
clickup task time log --duration 3h --billable

# Log time for another team member
clickup task time log 86abc123 --duration 2h --assignee 54874661

# Bulk log from a JSON file
clickup task time log --from-file entries.json
```

**Bulk time log file format:**

```json
[
  {"task_id": "86abc123", "duration": "2h", "date": "2026-03-15", "description": "Feature work", "assignee": "54874661"},
  {"task_id": "86abc456", "duration": "1h30m", "date": "2026-03-15", "description": "Code review"}
]
```

Each entry supports: `task_id` (required), `duration` (required), `date`, `description`, `assignee`, `billable`. The `--assignee` flag applies as a default for entries without their own assignee.

```bash
# List time entries for a task
clickup task time list
clickup task time list 86abc123
clickup task time list 86abc123 --json

# Timesheet: list all your time entries for a date range
clickup task time list --start-date 2026-02-01 --end-date 2026-02-28
clickup task time list --start-date 2026-02-01 --end-date 2026-02-28 --json

# Timesheet for a specific user
clickup task time list --start-date 2026-02-01 --end-date 2026-02-28 --assignee 54695018

# Timesheet for multiple users (fetched concurrently)
clickup task time list --start-date 2026-03-01 --end-date 2026-03-31 --assignee 48884897,54874661,54874662

# Timesheet for all workspace members
clickup task time list --start-date 2026-02-01 --end-date 2026-02-28 --assignee all

# Include task tags in JSON output (fetches concurrently)
clickup task time list --start-date 2026-03-01 --end-date 2026-03-31 --include-tags --json
```

When `--start-date` and `--end-date` are provided, the command switches to **timesheet mode** — querying all time entries across tasks for the date range, grouped by task. Defaults to the current user; use `--assignee all` for everyone, `--assignee <user-id>` for a specific person, or `--assignee id1,id2,id3` for multiple users (fetched concurrently).

Use `--include-tags` with `--json` to embed task tags in the output — useful for CapEx auditing without a separate bulk-view step.
