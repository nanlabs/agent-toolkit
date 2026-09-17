# nanlabs-core

Baseline NaNLABS harness plugin — **recommended first install**.

Includes bundled setup: contract doctor, `nanlabs-setup` skill, and `/nanlabs-core:setup` command.

Canonical skills for this group live **in this directory** under `skills/<name>/`. There is no second tree at repo-root `skills/core/`.

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix (Agent Plugins roster + Claude Code).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run setup via **`/nanlabs-core:setup`** or ask Claude to run the `nanlabs-setup` skill.

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core
```

Or Team Marketplace / `~/.cursor/plugins/local/`.

### Agent Plugins folder import

Point the client at this directory (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.

Optional: install `nanlabs-agents` for the full agent roster, and the other
`nanlabs-*` group plugins for a complete skill install.

> **Deprecated:** the standalone `nanlabs-setup` plugin is no longer listed in the marketplace. Setup ships here.

## Contents

| Area | Notes |
| --- | --- |
| Skills | `nanlabs-assistant`, `nanlabs-dev-companion`, `nanlabs-output-handshake`, `nanlabs-pr-fallback`, `nanlabs-workspace-knowledge-sync`, `nanlabs-setup`, `nanlabs-pyrightination` |
| Agent | `nanlabs-code-reviewer` (also under `com.github.copilot/agents/`) |
| Setup | `scripts/doctor-contracts.py`, `contracts/requirements/nanlabs-core.yaml`, `commands/setup.md` |

Agent files are generated from repo-root `agents/`. Skill bodies in `skills/` are the source of truth — `gen-surfaces` does not copy them.
