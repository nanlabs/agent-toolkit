# nanlabs-delivery

PRD, TRD, ADR, work items, assessments, and delivery process

Canonical skills live under `skills/<name>/` (layout group `delivery`). There is no second tree under `skills/<group>/`.

## Skills

`nanlabs-adr`, `nanlabs-agreement`, `nanlabs-bug`, `nanlabs-decision-log`, `nanlabs-development-workflow`, `nanlabs-epic`, `nanlabs-incident`, `nanlabs-management-unit-assessment`, `nanlabs-meeting-minutes`, `nanlabs-planning`, `nanlabs-prd`, `nanlabs-project-assessment`, `nanlabs-project-assessment-evidence`, `nanlabs-spike`, `nanlabs-task`, `nanlabs-technical-unit-assessment`, `nanlabs-trd`, `nanlabs-user-story`, `nanlabs-work-item`

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-delivery@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-delivery
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-delivery ~/.cursor/plugins/local/nanlabs-delivery
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-delivery
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-delivery` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
