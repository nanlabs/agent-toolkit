# ClickUp CLI: tasks

## Task management

### View and search

```bash
# View a task (auto-detects from git branch if no ID given)
# Also detects tasks via PR URL in descriptions when branch has no task ID
# Subtask lines show due/start dates inline for at-a-glance visibility
clickup task view
clickup task view CU-abc123

# View with JSON — useful for extracting subtask IDs for bulk operations
clickup task view 86abc123 --json

# Bulk view: fetch multiple tasks concurrently (up to 10 parallel)
clickup task view 86abc1 86abc2 86abc3 --json

# Extract tags from multiple tasks
clickup task view 86abc1 86abc2 86abc3 --jq '[.[] | {id: .id, tags: [.tags[].name]}]'

# Search tasks by name and description (supports fuzzy matching)
# Uses server-side search (Level 0) with parallel space traversal
clickup task search "login bug"
clickup task search "login bug" --exact    # Exact matches only
clickup task search "login bug" --assignee me       # Only your tasks
clickup task search "login bug" --assignee "alice"   # By name/username/ID

# Recent tasks (excludes archived folders)
clickup task recent
clickup task recent --sprint               # Only current sprint tasks

# List tasks in a specific list
clickup task list --list-id 12345

# List tasks using configured default list (via `list select`)
clickup task list

# Include closed tasks in the list
clickup task list --include-closed
clickup task list -c --list-id 12345

# Recursive view — fetch subtasks and their children in a single tree
clickup task view 86abc123 --recursive --json

# Bulk delete tasks (requires confirmation or -y to skip)
clickup task delete 86abc1 86abc2 86abc3 -y

# Task activity/comment history
clickup task activity CU-abc123
```

**Navigating task hierarchies:** Use `--json` to drill into subtask trees. The JSON output includes a `subtasks` array with each subtask's `id`, `name`, `status`, `due_date`, and `start_date`. To operate on subtasks in bulk, view the parent with `--json`, extract the subtask IDs, then pass them to `task edit`.

### Task Naming Conventions

**IMPORTANT: Always use descriptive, well-structured task names.** Task names should be scannable on a sprint board without needing to click into the task. Follow this convention:

**Format:** `[Work Type] Context — Action (Platform/Scope)`

| Component | Purpose | Examples |
|-----------|---------|----------|
| `[Work Type]` | Categorises the work at a glance | `[Packdown]`, `[Bug]`, `[Feature]`, `[Refactor]`, `[Spike]`, `[Hotfix]` |
| `Context` | Campaign, project, or feature name | `NT x THL`, `Auth v2`, `Booking Flow` |
| `Action` | What is being done — use imperative verbs | `Remove landing page`, `Add SSO support`, `Fix timeout error` |
| `(Platform/Scope)` | Which app, site, or system is affected | `(CamperMate)`, `(Britz + Apollo)`, `(API)`, `(CamperMate + CM.com)` |

**Examples:**
- `[Packdown] NT x THL — Remove CamperMate campaign landing page`
- `[Packdown] NT x THL — Remove app menu links (CamperMate + CM.com)`
- `[Bug] Booking Flow — Fix timeout on slow connections (API)`
- `[Feature] Auth v2 — Add SSO support (CamperMate)`
- `[Spike] Search — Evaluate Algolia vs Typesense`

**When to simplify:** For small, self-evident tasks (e.g. subtasks or checklists), a short descriptive name is fine. The full convention is most valuable for sprint-level tasks that need to be scannable across teams.

**Template tasks:** Use `{Campaign}` or `{Project}` as a placeholder in the context position so the name can be filled in when the template is instantiated (e.g. `[Packdown] {Campaign} — Remove campaign landing page`).

### Create & Edit

**IMPORTANT: When creating a task, fill in ALL applicable fields.** Do not create bare tasks with just a name. Ask the user for any information you don't already have. Use the naming conventions above for the `--name` flag. A well-created task should include as many of these as possible:

- `--current` — **preferred**: auto-resolves the active sprint list (no need to know the list ID)
- `--list-id` — explicit list ID (use when creating outside the current sprint)
- `--list-name` — resolve a list name to its ID (e.g., `--list-name "Sprint 89"`)
- `--name` — task name (required — follow naming conventions above)
- `--description` or `--markdown-description` — clear description of the work
- `--status` — initial status (e.g., "open", "in progress")
- `--priority` — 1=Urgent, 2=High, 3=Normal, 4=Low
- `--assignee` — user ID(s) for who should work on it
- `--tags` — relevant tags (repeatable)
- `--due-date` — deadline (YYYY-MM-DD)
- `--start-date` — when work should begin (YYYY-MM-DD)
- `--time-estimate` — estimated effort (e.g., "2h", "4h", "1d")
- `--points` — sprint/story points
- `--parent` — parent task ID if this is a subtask
- `--links-to` — related task ID
- `--type` — 0=task, 1=milestone
- `--field "Name=value"` — custom fields (repeatable)

**IMPORTANT: Always use `--current` instead of hardcoding sprint list IDs.** Sprint list IDs change every sprint. Never cache or remember a specific list ID — always let the CLI resolve it dynamically.

After creating a task, consider adding checklists for acceptance criteria or subtasks:

```bash
clickup task checklist add <task-id> "Acceptance Criteria"
clickup task checklist item add <checklist-id> "Unit tests pass"
clickup task checklist item add <checklist-id> "Code reviewed"
clickup task checklist item add <checklist-id> "Assigned item" --assignee 12345678
```

Example — create a task by list name (resolves name to ID):

```bash
clickup task create --list-name "Sprint 89" --name "Fix bug" --status "open"
```

Example of a well-populated task creation:

```bash
clickup task create --current \
  --name "[Bug] Auth — Fix login timeout on slow connections (API)" \
  --markdown-description "Users on slow 3G connections get a timeout error..." \
  --status "open" \
  --priority 2 \
  --assignee 12345678 \
  --tags "bug" --tags "auth" \
  --due-date 2025-03-01 \
  --start-date 2025-02-20 \
  --time-estimate 4h \
  --points 3
```

**Tags:** Before creating a task, check what tags are available in the space with `clickup tag list`. Use existing tags rather than inventing new ones — tags should be consistent across the workspace. If no suitable tag exists, discuss with the user before creating a new one.

**Bulk create from JSON file** — use `--from-file` for batch task creation:

```bash
# Create many tasks at once from a JSON file
clickup task create --current --from-file tasks.json
clickup task create --current --from-file tasks.json --json
```

The JSON file should contain an array of task objects:

```json
[
  {
    "name": "Design homepage",
    "description": "Create wireframes and mockups",
    "status": "open",
    "priority": 2,
    "due_date": "2026-03-15",
    "time_estimate": "4h",
    "tags": ["design"],
    "parent": "86abc123",
    "fields": [{"name": "Environment", "value": "staging"}]
  },
  {
    "name": "Implement auth flow",
    "start_date": "2026-03-01",
    "due_date": "2026-03-10",
    "assignees": [12345678],
    "points": 5
  }
]
```

Errors on individual tasks are reported but don't stop the batch. A summary is printed at the end.

```bash
# Edit a task (auto-detects from git branch)
clickup task edit --status "in progress" --priority 2
clickup task edit CU-abc123 --field "Environment=production"
clickup task edit --due-date 2025-03-01 --time-estimate 4h

# Bulk edit multiple tasks at once — pass all IDs as positional args
clickup task edit 86abc1 86abc2 86abc3 --status "Closed"
clickup task edit 86abc1 86abc2 86abc3 --due-date 2026-03-01 --priority 2

# Tags — add without removing existing
clickup task edit CU-abc123 --add-tags new-feature-development
clickup task edit 86abc1 86abc2 --add-tags r&d,new-app-development

# Tags — remove specific tags
clickup task edit CU-abc123 --remove-tags fix

# Tags — replace all (use with caution)
clickup task edit CU-abc123 --tags "ios,android,new-app-development"

# Custom fields
clickup task edit CU-abc123 --field "Environment=production"
clickup task edit CU-abc123 --clear-field "Environment"
clickup field list --list-id 12345    # Discover available fields
```

**Bulk edit workflow — closing all subtasks of a parent:**

1. View the parent task with `--json` to get subtask IDs:
   ```bash
   clickup task view 86parent --json
   # → .subtasks[].id gives you the child IDs
   ```
2. If subtasks themselves have children, view each subtask with `--json` to get the next level of IDs.
3. Pass all collected IDs to a single `task edit`:
   ```bash
   clickup task edit 86child1 86child2 86child3 ... --status "Closed"
   ```
4. Errors on individual tasks are reported but don't stop the batch. A summary line shows `Updated X/N tasks`.

**Important:** Check `clickup status list` or the validation error output to find the correct status name for the space — statuses vary between spaces (e.g., "done" vs "Closed" vs "complete").

### Multi-List (Add/Remove Tasks from Lists)

```bash
# Add a task to a sprint list (task stays in its original list too)
clickup task list-add 86abc123 --list-id 901613544162

# Add multiple tasks to the same list at once
clickup task list-add 86abc1 86abc2 86abc3 --list-id 901613544162

# Remove a task from a list (must belong to at least one other list)
clickup task list-remove 86abc123 --list-id 901613544162

# Remove multiple tasks from the same list
clickup task list-remove 86abc1 86abc2 86abc3 --list-id 901613544162
```

Use `list-add` when a task needs to appear in multiple lists — e.g., a campaign task that also belongs in an engineering sprint. Use `list-remove` to undo this. Neither command moves the task; they manage secondary list memberships.

### Status Management

```bash
# Set status (supports fuzzy matching: "review" matches "code review")
clickup status set "in progress"
clickup status set "in progress" CU-abc123

# List available statuses
clickup status list
clickup status list --space 12345

# Add a new status to a space (inserted before Closed)
clickup status add "done"
clickup status add "QA Review" --color "#7C4DFF"
clickup status add "done" -y              # Skip confirmation
clickup status add "done" --space 12345   # Specific space
```

Status values are fuzzy-matched: exact match > contains match > fuzzy match. If ambiguous, the CLI picks the most specific match and prints a warning.

**Guardrails for `status add`:** Only suggest adding a status when there's a genuine gap in the workflow (e.g., a space has "Closed" but no "done" equivalent). Always confirm with the user before adding. Never remove statuses without explicit user instruction — statuses affect all tasks in the space.
