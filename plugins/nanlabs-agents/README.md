# nanlabs-agents

Claude Code / Cursor plugin bundling all public agent personas from `agents/`.

Canonical bodies live under repository-root `agents/`. This plugin tree is
**generated** by:

```bash
python3 scripts/gen-surfaces.py
python3 scripts/gen-surfaces.py --check   # CI drift gate
```

Do not hand-edit files under `plugins/nanlabs-agents/agents/` — change
`agents/<name>/` and regenerate.

## Install

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

## Contents

See [`agents/README.md`](../../agents/README.md) and
[`catalogs/agent-catalog.yaml`](../../catalogs/agent-catalog.yaml).
