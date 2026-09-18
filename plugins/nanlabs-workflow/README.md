# nanlabs-workflow

Client delivery workflows and bootstrap

Canonical skills live under `skills/<name>/` (layout group `workflow`). There is no second tree under `skills/<group>/`.

## Skills

`nanlabs-workflow-client-bootstrap`, `nanlabs-workflow-generic-project`

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-workflow@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-workflow
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-workflow ~/.cursor/plugins/local/nanlabs-workflow
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-workflow
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-workflow` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
