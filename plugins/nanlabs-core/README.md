# nanlabs-core

Baseline NaNLABS harness plugin for Claude Code, Cursor, and GitHub Copilot CLI
— **single recommended install**.

Includes bundled setup: contract doctor, `nanlabs-setup` skill, and `/nanlabs-core:setup` command.

## Install

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run setup via **`/nanlabs-core:setup`** or ask Claude to run the `nanlabs-setup` skill.

For Cursor IDE, copy or symlink this directory under
`~/.cursor/plugins/local/`, or install it from the Team Marketplace. For the
Cursor Agent CLI, load the checkout with:

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core
```

For GitHub Copilot CLI, install directly from GitHub:

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
```

Optional: install `nanlabs-agents` for the full agent roster.

> **Deprecated:** the standalone `nanlabs-setup` plugin is no longer listed in the marketplace. Setup ships here.

## Contents

| Area | Notes |
| --- | --- |
| Skills | `nanlabs-assistant`, `nanlabs-dev-companion`, `nanlabs-output-handshake`, `nanlabs-pr-fallback`, `nanlabs-workspace-knowledge-sync`, `nanlabs-setup`, `nanlabs-pyrightination` |
| Agent | `nanlabs-code-reviewer` |
| Setup | `scripts/doctor-contracts.py`, `contracts/requirements/nanlabs-core.yaml`, `commands/setup.md` |

Source of truth remains the repo-root `skills/core/` and `agents/` trees — keep plugin copies in sync when those change.
