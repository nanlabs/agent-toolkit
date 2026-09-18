# nanlabs-agents

Optional full set of NaNLABS agent / subagent personas (reviewers, architect, planner, e2e, …)

This plugin ships agent personas generated from repo-root `agents/`. Skill bodies live in the group plugins. Do not hand-edit `plugins/nanlabs-agents/agents/` — change `agents/<name>/` and regenerate.

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-agents ~/.cursor/plugins/local/nanlabs-agents
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-agents
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-agents` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
