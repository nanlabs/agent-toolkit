---
name: clickup-cli
description: >-
  HOW — ClickUp CLI for tasks, sprints, comments, Docs, and git integration. Use when the user
  mentions ClickUp task IDs, sprint status, or Docs. Do NOT use for delivery workflow phases.
---

# ClickUp CLI (`clickup`)

Prefer the `clickup` CLI over raw API calls. Auth: `clickup auth login` / `clickup auth status` (config: `~/.config/clickup/config.yml`).

## When to use

- Create, edit, view, or search ClickUp tasks
- Sprint status, comments, PR/branch linking, Docs/pages
- Task IDs like `CU-abc123` or numeric IDs

## When NOT to use

- Client delivery phases and gates (use **nanlabs-workflow-generic-project**)
- Replacing human approval on status or scope changes

## Quick start

```bash
clickup task view              # auto-detect from git branch
clickup task search "login bug"
clickup comment add CU-abc123 "Update"
clickup link pr --task CU-abc123
```

## Reference files (read as needed)

| Topic | File |
| --- | --- |
| Tasks (view, search, create, edit, bulk) | `references/tasks.md` |
| Sprints, folders, lists | `references/sprints-and-lists.md` |
| Comments, git links, time tracking | `references/comments-git-time.md` |
| Docs and pages | `references/docs.md` |
| Inbox, workspace, chat, checklists, flags | `references/workspace-and-misc.md` |

## Key behaviors

- Auto-detects task ID from git branch (`feature/CU-abc123-description`)
- Fuzzy status matching; validate before create/edit
- `--json` / `--jq` for agent-friendly output
- `@mentions` in comments resolve usernames to ClickUp tags
