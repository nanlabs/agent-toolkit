# ClickUp CLI: sprints and lists

```bash
# Show current sprint tasks
clickup sprint current

# List all sprints in a folder
clickup sprint list
```

## Folders

```bash
# List folders in a space
clickup folder list
clickup folder list --space 12345
clickup folder list --archived --json

# Select a default folder (interactive)
clickup folder select
clickup folder select --local  # per-directory
```

## Lists

```bash
# List lists in a folder
clickup list list --folder 12345
clickup list list --space 12345  # folderless lists
clickup list list --json

# Select a default list (interactive)
clickup list select
clickup list select --local  # per-directory
```
