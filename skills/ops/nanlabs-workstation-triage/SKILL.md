---
name: nanlabs-workstation-triage
description: Workstation health triage, validate tooling, directory layout, and run nan-doctor with remediation suggestions.
metadata:
  author: nanlabs
  version: "1.1"
---

# Workstation Triage (NaNLABS)

Use when the user reports workstation issues, install problems, tool failures, or needs a health check before starting work.

## Prerequisites

Run this skill on the **local workstation** where the user is experiencing issues. Do not run it on a remote server unless the user confirms the remote has the NaNLABS setup.

Verify `nan-doctor` is installed:

```bash
command -v nan-doctor
```

If missing, install via chezmoi (`chezmoi apply`) or direct installation.

> **Repo location:** The internal-workstation repository (which manages this skill) is cloned at `~/.ai-workspace/repos/github.com/nanlabs/internal-workstation`. When updating or debugging this skill, check that path first.

## Output modes

Use the mode that matches the user's need:

| Mode | Command | When to use |
|------|---------|-------------|
| **Colored** (default) | `nan-doctor` | Interactive terminal session, human-readable colored output |
| **Markdown** | `nan-doctor --issue` | GitHub issues, Slack threads, tickets, paste-ready block |
| **JSON** | `nan-doctor --json` | Automation scripts, CI parsing, enriched machine-readable report |
| **ClickUp inventory** | `nan-doctor --clickup` | Upsert this machine to M&I Workstation Inventory (opt-in; requires `clickup auth login`) |
| **ClickUp preview** | `nan-doctor --clickup-dry-run` | Show what would be uploaded without calling ClickUp |

### Markdown output (`--issue`)

Always use `nan-doctor --issue` (not the default) when the output will be shared in:
- GitHub issues or PR comments
- Slack messages
- Support tickets
- Any written async communication

### JSON output (`--json`)

Use `nan-doctor --json` only when:
- A script or automation pipeline needs to parse the result
- You need structured JSON (identity, checks[], integrations, tooling) for programmatic handling
- Requires `python3` in PATH

### ClickUp inventory (`--clickup`)

Use when Technology needs a live registry of NaNLABS workstations:

```bash
clickup auth status
nan-doctor --clickup-dry-run
nan-doctor --clickup
```

One task per machine in [Workstation Inventory](https://app.clickup.com/459857/v/l/li/901714155258). Never paste API tokens into tickets, auth is via `clickup auth login` only.

## Profile and check groups

The doctor's behavior is controlled by `~/.config/nanlabs/profile.env`. Checks can be selectively enabled/disabled via environment variables:

| Variable | Default | Effect |
|----------|---------|--------|
| `NAN_DOCTOR_GROUP_CORE` | `true` | Core tools: `git`, `curl`, `wget`, `jq`, `rg`, `fd`, `zsh`, `gh` |
| `NAN_DOCTOR_GROUP_NODE` | `true` | Node.js: `fnm`, `node` |
| `NAN_DOCTOR_GROUP_PYTHON` | `true` | Python: `uv`, `python3` |
| `NAN_DOCTOR_GROUP_GO` | profile-driven | Go: `go` (enabled with `install_group_go` or productivity CLIs) |
| `NAN_DOCTOR_GROUP_DOCKER` | `true` | Docker: `docker` |
| `NAN_DOCTOR_GROUP_AI` | `true` | LLM API key presence flags (ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY) |
| `NAN_DOCTOR_GROUP_SKILLS_PRODUCTIVITY` | `false` | Optional productivity tool group |
| `NAN_DOCTOR_SKILL_JIRA` | `false` | JIRA skill integration check |
| `NAN_DOCTOR_SKILL_CONFLUENCE` | `false` | Confluence skill integration check |

> **Note:** Profile variables are read from `~/.config/nanlabs/profile.env`. If the file is missing, defaults apply.

## Directory checks

The doctor validates the presence and structure of:
- `~/.local/share/nanlabs/prompts`
- `~/.local/share/nanlabs/skills`
- `~/.local/share/nanlabs/templates`
- `~/.local/share/nanlabs/mcp/github`
- `~/.local/share/nanlabs/mcp/clickup`
- `~/.local/share/nanlabs/mcp/notion`
- `~/.local/share/nanlabs/mcp/slack`

## Remediation guidance

Propose fixes in order of lowest risk first:

1. **Missing directories** → run `chezmoi apply` to bootstrap the full NaNLABS installation
2. **Missing commands** → use the respective skill's installation instructions (e.g., `uv` via `curl -LsSf https://astral.sh/uv/install.sh`, `go` via `chezmoi apply` with the go group or productivity profile)
3. **Auth failures** → run `gh auth login`, `clickup auth login`, or `glab auth login` as appropriate
4. **Profile/group mismatches** → edit `~/.config/nanlabs/profile.env` and run `chezmoi apply`
5. **Go / clickup CLI missing** → verify `~/.config/nanlabs/env.d/go.env` exists and `GOPATH/bin` is on PATH (`eval "$(nan-loadenv --emit)"`)
6. **API key missing** → guide user to set the appropriate env var in their shell profile

## Common issues

### nan-doctor exits 1 (NON-COMPLIANT)

Run with `--issue` to get the full markdown checklist. Address failures in this order:
1. Install any missing core commands
2. Run `chezmoi apply` to restore directory structure
3. Re-authenticate CLIs (`gh`, `clickup`, `glab`)
4. Verify `~/.config/nanlabs/profile.env` matches the intended profile

### nan-doctor --json requires python3

If `python3` is not available, fall back to `nan-doctor --issue` and parse the markdown manually.

### nan-doctor: Missing dependency: easyoptions.sh

The `easyoptions.sh` library is missing from `~/.local/lib/nanlabs`. Re-run `chezmoi apply` to restore it, or check if the NaNLABS installation is incomplete.

### Legacy workflow symlinks detected

If the doctor reports legacy `workflow-*` symlinks in `~/.claude/skills/` or `~/.agents/skills/`, these should point to `nanlabs-*` equivalents. Run `dots-skills sync` or re-link manually.

## Skill boundaries

- This skill **does not fix issues automatically**, it diagnoses and proposes remediation steps.
- This skill **does not modify** `profile.env` or authentication state, user must approve and execute fixes.
- For **chezmoi-managed configuration issues**, pair with the **`nanlabs-dev-companion`** or direct chezmoi guidance.
- For **CI/build failures** on a project repo, use **`nanlabs-build-error-resolver`** instead of this skill.


## Default guardrails

1. Apply **nanlabs-output-handshake** before final output.
2. Use **skill-catalog.yaml** for routing to HOW skills.

## References

- `nan-doctor --help`, full option list
- `~/.config/nanlabs/profile.env`, check group configuration
- `~/.local/lib/nanlabs/easy-options/easyoptions.sh`, dependency library
