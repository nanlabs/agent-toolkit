# nanlabs-agents

Claude Code / Cursor / GitHub Copilot CLI plugin bundling all public agent
personas from `agents/`.

Canonical bodies live under repository-root `agents/`. Core skills live under `skills/core/`. This plugin tree is
**generated** by:

```bash
python3 scripts/gen-surfaces.py
python3 scripts/gen-surfaces.py --check   # CI drift gate
```

Do not hand-edit files under `plugins/nanlabs-agents/agents/` or `plugins/nanlabs-agents/resources/` — change
`agents/<name>/` and regenerate. Agent files are flat `agents/<name>.md` (Claude/Cursor discovery-safe); references
ship under `resources/agents/<name>/`.

## Install

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

For Cursor IDE, copy or symlink this directory under
`~/.cursor/plugins/local/`, or install it from the Team Marketplace. For the
Cursor Agent CLI, load the checkout with:

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-agents
```

For GitHub Copilot CLI, install directly from GitHub:

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
```

## Contents

See [`agents/README.md`](../../agents/README.md) and
[`catalogs/agent-catalog.yaml`](../../catalogs/agent-catalog.yaml).
