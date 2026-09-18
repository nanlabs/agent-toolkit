# nanlabs-ops

Workstation triage, presentations ops, and skill contribution

Canonical skills live under `skills/<name>/` (layout group `ops`). There is no second tree under `skills/<group>/`.

## Skills

`nanlabs-presentations-reconciliation`, `nanlabs-propose-skill`, `nanlabs-workstation-triage`

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-ops@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-ops
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-ops ~/.cursor/plugins/local/nanlabs-ops
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-ops
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-ops` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
