# nanlabs-ops

Workstation triage, presentations ops, and skill contribution

Canonical skills live under `skills/<name>/` (layout group `ops`). There is no second tree under `skills/<group>/`.

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-ops@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-ops
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-ops
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-ops` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
