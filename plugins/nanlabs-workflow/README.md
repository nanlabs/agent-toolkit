# nanlabs-workflow

Client delivery workflows and bootstrap

Canonical skills live under `skills/<name>/` (layout group `workflow`). There is no second tree under `skills/<group>/`.

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-workflow@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-workflow
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-workflow
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-workflow` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
