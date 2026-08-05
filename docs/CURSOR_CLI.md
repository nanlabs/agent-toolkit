# Cursor CLI certification matrix

**Status:** **beta / uncertified** for NaNLABS plugins until smoke evidence is recorded below.

Cursor IDE and Cursor CLI are separate surfaces. Do not assume IDE plugin components load identically in the CLI.

## Component matrix

Fill with evidence (CLI version, date, profile). Mark each: `pass` · `fail` · `partial` · `unknown`.

| Component | IDE (expected) | CLI result | Evidence / notes |
| --- | --- | --- | --- |
| Skills from installed plugins | yes | unknown | |
| Slash commands from plugins | yes | unknown | |
| Subagents / agents | yes | unknown | |
| Rules | if shipped | unknown | NaNLABS core does not currently ship Cursor rules |
| Hooks | if shipped | unknown | not shipped today |
| MCP from plugin | if shipped | unknown | MCP not packaged in plugins today |
| Local `--plugin-dir` / settings `enabled_plugins` | yes | unknown | |
| Headless / print mode (`-p`) skill invoke | n/a | unknown | |
| Permissions / sandbox | n/a | unknown | |

## Smoke commands (operators)

Record exact binary (`agent` / `cursor agent`) and version:

```bash
# Example — adjust to your installed CLI entrypoint
agent --version || true
# Load local plugin dir if supported by your CLI build, then:
#   list skills / commands / agents and capture output
```

Community history includes plugin-skill parity gaps between IDE and CLI; re-verify on the org’s pinned CLI version.

## Product rule

Until this matrix has at least skills + commands evidenced `pass` on a pinned CLI version, README must label Cursor CLI as **beta**, not Tier-1 production.
