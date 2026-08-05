# Cursor Agent CLI certification matrix

**Product priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Certification status:** **partially certified** (skills + commands + agents via `--plugin-dir`; marketplace add works). Remaining gaps below stay `unknown`/`partial` until re-verified.

Cursor IDE and Cursor Agent CLI are separate runtimes. Do not assume IDE plugin components load identically in the CLI.

## Evidence snapshot

| Field | Value |
| --- | --- |
| Date | 2026-08-05 |
| CLI binary | `cursor-agent` (invoked as `agent`) |
| CLI version | `2026.07.23-e383d2b` |
| OS | linux x64 |
| Profile | disposable local; Pro+ account |
| Plugin load | `--plugin-dir plugins/nanlabs-core` (+ optional `nanlabs-agents`) |
| Marketplace | `agent plugin marketplace add https://github.com/nanlabs/agent-toolkit` → `nanlabs-agent-toolkit` (2 plugins) |

## Component matrix

| Component | IDE (expected) | CLI result | Evidence / notes |
| --- | --- | --- | --- |
| Skills from installed plugins | yes | **pass** | `--plugin-dir` + print ask listed all 6 `nanlabs-core` skills (`nanlabs-setup`, `nanlabs-assistant`, `nanlabs-dev-companion`, `nanlabs-output-handshake`, `nanlabs-pr-fallback`, `nanlabs-workspace-knowledge-sync`) |
| Slash commands from plugins | yes | **pass** | `/nanlabs-core:setup`, `/nanlabs-core:core-help` visible under `--plugin-dir` |
| Subagents / agents | yes | **pass** | `nanlabs-code-reviewer` from core; all 16 agents when also loading `nanlabs-agents` |
| Rules | if shipped | n/a | NaNLABS core does not ship Cursor rules |
| Hooks | if shipped | n/a | not shipped today |
| MCP from plugin | if shipped | n/a | MCP not packaged in plugins today |
| Local `--plugin-dir` | yes | **pass** | flag works; can be repeated |
| Marketplace add (git URL) | team/admin in IDE | **pass** | `plugin marketplace add` registered `nanlabs-agent-toolkit` with core + agents |
| Marketplace install + enable (non-interactive) | yes | **partial** | CLI tip says use `/plugins` in interactive mode; no non-interactive `plugin install` verified yet |
| Headless / print mode (`-p`) skill invoke | n/a | **pass** | `-p --mode ask --output-format text` returned deterministic `PONG`; inventory prompts succeeded |
| Permissions / sandbox | n/a | **partial** | flags exist (`--force`/`--yolo`, `--sandbox`); not exercise-tested for NaN skills |

## Smoke commands (operators)

```bash
# Install CLI (official installer) or pin a lab build
agent --version
# 2026.07.23-e383d2b

agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent plugin marketplace list

# Preferred local certification path
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"

# Optional full roster
agent --plugin-dir .../nanlabs-core --plugin-dir .../nanlabs-agents \
  -p --mode ask --output-format text \
  "List custom agents available"
```

## Product rule

1. **Priority:** Cursor Agent CLI ships at the same priority as Claude, Claude Code, and Cursor IDE.
2. **Honesty:** skills + commands + agents are evidenced `pass` on CLI `2026.07.23-e383d2b` via `--plugin-dir`. Marketplace **install** UX and sandbox policy remain partial — do not claim full parity with IDE Team Marketplace install yet.
3. **Blocking:** epic [#19](https://github.com/nanlabs/agent-toolkit/issues/19) still needs interactive `/plugins` install evidence + pilot journeys (#9) before calling CLI fully certified.
