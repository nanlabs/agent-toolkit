# ⌨️ Cursor Agent CLI

**Priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Status:** partially certified — see repo [`docs/CURSOR_CLI.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CURSOR_CLI.md) for the live matrix.

## Quick smoke

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

## Known good (evidence snapshot)

On CLI `2026.07.23-e383d2b` with `--plugin-dir`:

- Skills from `nanlabs-core` (6)
- Commands `/nanlabs-core:setup`, `/nanlabs-core:core-help`
- Agents from core + full roster with `nanlabs-agents`
- Marketplace **add** works

Still partial: interactive `/plugins` install UX; sandbox/`--force` exercise.

## Rule

Evidence gap ≠ lower product priority. Never label CLI as “out of scope” or “nice-to-have”.
