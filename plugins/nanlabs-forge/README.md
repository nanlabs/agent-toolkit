# nanlabs-forge

GitHub and GitLab CLI automation for PRs, reviews, and CI

Canonical skills live under `skills/<name>/` (layout group `forge`). There is no second tree under `skills/<group>/`.

## Install

See [docs/ADOPTION.md](../../docs/ADOPTION.md) for the full client matrix.

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-forge@nanlabs-agent-toolkit
```

### GitHub Copilot CLI

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-forge
```

### Cursor

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-forge
```

### Agent Plugins folder import

Point the client at `plugins/nanlabs-forge` (`plugin.json` + `skills/<name>/SKILL.md`).
Kiro, Grok Bot, Hermes Agent, OpenClaw, and NanoClaw use this path.
