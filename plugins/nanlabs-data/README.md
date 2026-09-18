# nanlabs-data

dbt and Snowflake validation skills

Canonical skills live under `skills/<name>/` (layout group `data`). There is no second tree under `skills/<group>/`.

## Skills

`dbt-validation`, `snowflake-validation`

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-data@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-data
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-data ~/.cursor/plugins/local/nanlabs-data
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-data
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-data` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
