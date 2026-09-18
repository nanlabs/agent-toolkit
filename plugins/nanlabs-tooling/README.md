# nanlabs-tooling

Playwright CLI and Jupyter notebook scaffolding

Canonical skills live under `skills/<name>/` (layout group `tooling`). There is no second tree under `skills/<group>/`.

## Skills

`jupyter-notebook`, `playwright-cli`

## Install

Complete client matrix: [docs/ADOPTION.md](../../docs/ADOPTION.md). Generated catalog: [docs/generated/catalog.md](../../docs/generated/catalog.md).

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-tooling@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-tooling
```

### Cursor IDE

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /path/to/agent-toolkit/plugins/nanlabs-tooling ~/.cursor/plugins/local/nanlabs-tooling
```

Then reload the window. Team Marketplace import of this repository also works.

### Cursor Agent CLI

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-tooling
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-tooling` (`plugin.json` + `skills/<name>/SKILL.md`). Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
