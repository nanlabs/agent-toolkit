# ClickUp CLI: workspace and misc

```bash
# Show @mentions from the last 7 days (scans comments and task descriptions)
clickup inbox
clickup inbox --days 30
clickup inbox --limit 500    # Scan more tasks in busy workspaces
```

## Workspace

```bash
# List workspace members
clickup member list

# List/select spaces
clickup space list
clickup space select    # Set default space
```

## Docs

Manage ClickUp Docs and their pages via the v3 API. All read commands support `--json`, `--jq`, and `--template`.

> **API limitation:** Delete, archive, and restore operations for Docs and Pages are not available via the public ClickUp v3 API at this time.

### List & View

```bash
# List all Docs in the workspace
clickup doc list
clickup doc list --json

# Filter by parent location
clickup doc list --parent-id 123456 --parent-type SPACE

# Include archived or deleted Docs
clickup doc list --archived
clickup doc list --deleted

# Paginate results
clickup doc list --limit 20 --cursor <cursor>

# View a specific Doc
clickup doc view <doc-id>
clickup doc view <doc-id> --json
```

### Create

```bash
# Create a Doc (creates an initial empty page by default)
clickup doc create --name "Project Runbook"

# Create in a specific space with public visibility
clickup doc create --name "Team Wiki" \
  --parent-id 123456 --parent-type SPACE \
  --visibility PUBLIC

# Create without an initial page
clickup doc create --name "Drafts" --create-page=false
```

### Pages

```bash
# List pages in a Doc (returns a tree structure)
clickup doc page list <doc-id>
clickup doc page list <doc-id> --max-depth 0   # Top-level only
clickup doc page list <doc-id> --json

# View a page (with optional content format)
clickup doc page view <doc-id> <page-id>
clickup doc page view <doc-id> <page-id> --content-format text/md
clickup doc page view <doc-id> <page-id> --json

# Create a page
clickup doc page create <doc-id> --name "Introduction"
clickup doc page create <doc-id> --name "Setup Guide" \
  --content "# Setup\n\nFollow these steps..." \
  --content-format text/md

# Create a nested page
clickup doc page create <doc-id> --name "Advanced Config" \
  --parent-page-id <parent-page-id>

# Edit a page (replace, append, or prepend content)
clickup doc page edit <doc-id> <page-id> --content "New content"
clickup doc page edit <doc-id> <page-id> \
  --content "## Release Notes\n\n- Fixed bug X" \
  --content-edit-mode append
clickup doc page edit <doc-id> <page-id> --name "Updated Title"
```

### JSON-first agent usage

```bash
# Get all doc IDs
clickup doc list --jq '.[].id'

# Get page IDs for a specific doc
clickup doc page list <doc-id> --jq '.pages[].id'

# Append release notes programmatically
clickup doc page edit <doc-id> <page-id> \
  --content "## v1.2.3\n\n- Fixed auth timeout" \
  --content-edit-mode append \
  --content-format text/md

# Create doc and capture its ID
clickup doc create --name "Sprint Retro" --json | jq -r '.id'
```

## Chat

```bash
# Send a message to a chat channel
clickup chat send <channel-id> "Hello team!"
clickup chat send <channel-id> "Deploy complete" --json
```

## Checklists

```bash
# Add a checklist to a task
clickup task checklist add <task-id> "Acceptance Criteria"

# Add items to a checklist
clickup task checklist item add <checklist-id> "Unit tests pass"
clickup task checklist item add <checklist-id> "Assigned item" --assignee 12345678

# Edit checklist items (supports bulk — multiple item IDs)
clickup task checklist item edit <checklist-id> <item-id> --assignee 12345678
clickup task checklist item edit <checklist-id> <item-id1> <item-id2> --assignee 12345678
```
