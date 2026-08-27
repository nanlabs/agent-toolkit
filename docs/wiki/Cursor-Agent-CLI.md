# ⌨️ Cursor Agent CLI

**Priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Status:** certified for documented load/add paths; see repo [`docs/CURSOR_CLI.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CURSOR_CLI.md) for the live matrix.

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

- Skills from `nanlabs-core` (7)
- Commands `/nanlabs-core:setup`, `/nanlabs-core:core-help`
- Agents from core + full 18-agent roster with `nanlabs-agents`
- Marketplace **add** works

Known limitation: this CLI build does not expose non-interactive marketplace `plugin install`; use `--plugin-dir` or IDE/Team installation. Sandbox/`--force` behavior is documented in the repo matrix.

## Rule

Evidence gap ≠ lower product priority. Never label CLI as “out of scope” or “nice-to-have”.
