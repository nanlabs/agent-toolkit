# Developer onboarding (NaN Workstation)

Use only when the user asks about **workstation setup**, **getting started**, or **validating install**.
For general repo work, use `REPO_INSPECTION.md` instead.

## First-time setup

Cite `docs/wiki/TECHNICAL_QUICKSTART.md` for the canonical steps:

```bash
git clone git@github.com:nanlabs/internal-workstation.git
cd internal-workstation
chezmoi init --source=. -c ~/.config/chezmoi/nan.toml
chezmoi apply --source=. -c ~/.config/chezmoi/nan.toml --dry-run
chezmoi apply --source=. -c ~/.config/chezmoi/nan.toml
```

## Post-setup validation

```bash
nan-doctor
```

Expected: `result: COMPLIANT`

## AI tools check

```bash
opencode --version   # or claude --version, etc.
nan-skills list
```

## Helpful commands

| Task | Command |
| --- | --- |
| Validate setup | `nan-doctor` |
| Check updates | `nan-update-check` |
| Update workstation | `chezmoi update && chezmoi apply --source=. -c ~/.config/chezmoi/nan.toml` |
| List AI skills | `nan-skills list` |
| Sync skills | `nan-skills sync` |
| Health triage | load **nanlabs-workstation-triage** |

## If issues persist

1. Run `nan-doctor` and address reported failures.
2. Run `nan-update-check` for pending workstation updates.
3. Escalate in Slack **#nan-workstation**.
