# nanlabs-core

Recommended install: setup/onboarding, orchestrator, companion, handshake, Pyright report-only typing, PR fallback, knowledge sync, and code-reviewer agent

Canonical skills live under `skills/<name>/` (layout group `core`). There is no second tree under `skills/<group>/`.

## Skills

`nanlabs-assistant`, `nanlabs-dev-companion`, `nanlabs-output-handshake`, `nanlabs-pyrightination`, `nanlabs-pr-fallback`, `nanlabs-setup`, `nanlabs-workspace-knowledge-sync`

## Setup

After install, run **`/nanlabs-core:setup`** (or ask the agent to run the bundled `nanlabs-setup` skill).

| Area | Notes |
| --- | --- |
| Agent | `nanlabs-code-reviewer` |
| Doctor | `scripts/doctor-contracts.py` + `commands/setup.md` |

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-core ~/.cursor/plugins/local/nanlabs-core
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-core` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
