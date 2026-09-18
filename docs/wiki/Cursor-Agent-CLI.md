# Cursor Agent CLI

**Priority:** equal with Claude, Claude Code, and Cursor IDE.

**Status:** certified for documented load/add paths. Live matrix: [`docs/CURSOR_CLI.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CURSOR_CLI.md).

> [!NOTE]
> Cursor IDE and Cursor Agent CLI are separate runtimes. Do not assume IDE plugin components load identically in the CLI.

## Quick smoke

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

`marketplace add` registers the catalog; it does **not** install a plugin. Repeat `--plugin-dir` per group, or install in the IDE.

## Known good (evidence snapshot)

On CLI `2026.07.23-e383d2b` with `--plugin-dir`:

- Skills from `nanlabs-core`
- Commands `/nanlabs-core:setup`, `/nanlabs-core:core-help`
- Agents from core + full `nanlabs-agents` roster
- Marketplace **add** works

Known limitation: that CLI build does not expose non-interactive marketplace `plugin install`; use `--plugin-dir` or IDE/Team installation.

Official MCP ships in design / forge / integrations as of v0.4.0. CLI MCP load remains **uncertified** on that snapshot.

## Rule

Evidence gap ≠ lower product priority. Never label CLI as “out of scope” or “nice-to-have”.

Install for other clients: [Installation](Installation).
