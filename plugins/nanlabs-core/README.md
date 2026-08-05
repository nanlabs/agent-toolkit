# nanlabs-core

Baseline NaNLABS harness plugin for Claude Code / Cursor — **single recommended install**.

Includes bundled setup: contract doctor, `nanlabs-setup` skill, and `/nanlabs-core:setup` command.

## Install

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run setup via **`/nanlabs-core:setup`** or ask Claude to run the `nanlabs-setup` skill.

Optional: install `nanlabs-agents` for the full agent roster.

> **Deprecated:** the standalone `nanlabs-setup` plugin is no longer listed in the marketplace. Setup ships here.

## Contents

| Area | Notes |
| --- | --- |
| Skills | `nanlabs-assistant`, `nanlabs-dev-companion`, `nanlabs-output-handshake`, `nanlabs-pr-fallback`, `nanlabs-workspace-knowledge-sync`, `nanlabs-setup` |
| Agent | `nanlabs-code-reviewer` |
| Setup | `scripts/doctor-contracts.py`, `contracts/requirements/nanlabs-core.yaml`, `commands/setup.md` |

Source of truth remains the repo-root `skills/core/` and `agents/` trees — keep plugin copies in sync when those change.
