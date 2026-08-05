# Cursor Agent CLI certification matrix

**Product priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Certification status:** **mostly certified** for load path `--plugin-dir` + marketplace **add**. Interactive marketplace **install** remains CLI-limited (no non-interactive `plugin install`).

Cursor IDE and Cursor Agent CLI are separate runtimes. Do not assume IDE plugin components load identically in the CLI.

## Evidence snapshot

| Field | Value |
| --- | --- |
| Date | 2026-08-05 |
| CLI binary | `cursor-agent` (invoked as `agent`) |
| CLI version | `2026.07.23-e383d2b` |
| OS | linux x64 |
| Profile | local; Pro+ account |
| Plugin load | `--plugin-dir plugins/nanlabs-core` (+ optional `nanlabs-agents`) |
| Marketplace | `agent plugin marketplace add https://github.com/nanlabs/agent-toolkit` → `nanlabs-agent-toolkit` (2 plugins) |

## Component matrix

| Component | IDE (expected) | CLI result | Evidence / notes |
| --- | --- | --- | --- |
| Skills from installed plugins | yes | **pass** | `--plugin-dir` + print ask listed all 6 `nanlabs-core` skills |
| Slash commands from plugins | yes | **pass** | `/nanlabs-core:setup`, `/nanlabs-core:core-help` |
| Subagents / agents | yes | **pass** | `nanlabs-code-reviewer` from core; all 16 with `nanlabs-agents` |
| Rules | if shipped | n/a | not shipped |
| Hooks | if shipped | n/a | not shipped |
| MCP from plugin | if shipped | n/a | MCP not packaged in plugins |
| Local `--plugin-dir` | yes | **pass** | flag works; repeatable |
| Marketplace add (git URL) | team/admin in IDE | **pass** | registers `nanlabs-agent-toolkit` |
| Marketplace install (non-interactive) | yes | **partial / N/A** | CLI `agent plugin` only exposes `marketplace` subcommands on this build — tip points to interactive `/plugins`; use `--plugin-dir` or IDE/Team install |
| Headless / print mode (`-p`) | n/a | **pass** | `-p --mode ask --output-format text` (`PONG`, inventories) |
| Permissions / sandbox | n/a | **pass** | `--sandbox enabled` → `SANDBOX_OK`; `--force` → `FORCE_OK` (2026-08-05) |

## Smoke commands (operators)

```bash
agent --version
# 2026.07.23-e383d2b

agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent plugin marketplace list

agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"

agent --plugin-dir .../nanlabs-core --sandbox enabled \
  -p --mode ask --output-format text "Reply with exactly: SANDBOX_OK"
```

## Product rule

1. **Priority:** equal with Claude, Claude Code, and Cursor IDE.
2. **Honesty:** skills + commands + agents + sandbox/force evidenced on CLI `2026.07.23-e383d2b` via `--plugin-dir`. Non-interactive marketplace **install** is not offered by this CLI build — document IDE/`/plugins` for that UX.
3. **Epic #19:** remaining gates are live Claude Code + Cursor IDE smoke (#8) and pilots (#9), not CLI demotion.
