# Cursor Agent CLI certification matrix

**Product priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Certification status:** **certified** for the documented local load path
`--plugin-dir` and marketplace **add**. Marketplace **add** only registers a
catalog; it does not install a plugin. Interactive marketplace installation is
not certified by this repository's evidence snapshot.

Cursor IDE and Cursor Agent CLI are separate runtimes. Do not assume IDE plugin components load identically in the CLI.

Official references: [Cursor plugins](https://cursor.com/docs/plugins) ·
[CLI parameters](https://cursor.com/docs/cli/reference/parameters) ·
[CLI changelog](https://cursor.com/docs/cli/changelog).

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
| Skills from installed plugins | yes | **pass** | `--plugin-dir` + print ask listed all 7 `nanlabs-core` skills |
| Slash commands from plugins | yes | **pass** | `/nanlabs-core:setup`, `/nanlabs-core:core-help` |
| Subagents / agents | yes | **pass** | `nanlabs-code-reviewer` from core; all 18 with `nanlabs-agents` |
| Rules | if shipped | n/a | not shipped |
| Hooks | if shipped | n/a | not shipped |
| MCP from plugin | if shipped | n/a | MCP not packaged in plugins |
| Local `--plugin-dir` | yes | **pass** | flag works; repeatable |
| Marketplace add (git URL) | team/admin in IDE | **pass** | registers `nanlabs-agent-toolkit` |
| Marketplace install | yes | **uncertified** | Current Cursor documentation exposes interactive `/plugin` installation; this repository's snapshot did not record a CLI install command or smoke result. Use `--plugin-dir` for CLI certification |
| Headless / print mode (`-p`) | n/a | **pass** | `-p --mode ask --output-format text` (`PONG`, inventories) |
| Permissions / sandbox | n/a | **pass** | `--sandbox enabled` → `SANDBOX_OK`; `--force` → `FORCE_OK` (2026-08-05) |

## Smoke commands (operators)

```bash
agent --version
# 2026.07.23-e383d2b

agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent plugin marketplace list

# `marketplace add` registers the catalog; it does not install a plugin.
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"

agent --plugin-dir .../nanlabs-core --sandbox enabled \
  -p --mode ask --output-format text "Reply with exactly: SANDBOX_OK"
```

## Product rule

1. **Priority:** equal with Claude, Claude Code, and Cursor IDE.
2. **Honesty:** skills + commands + agents + sandbox/force are evidenced on
   CLI `2026.07.23-e383d2b` via `--plugin-dir`. Marketplace registration is
   evidenced; plugin installation is not. Follow current Cursor documentation
   for interactive marketplace installation, but do not claim it is certified
   here.
3. **Epic #19:** issues #8, #9, and #58 are closed. The documented non-interactive marketplace-install limitation remains a CLI constraint, not a product-priority change.
