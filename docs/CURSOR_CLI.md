# Cursor Agent CLI certification matrix

**Product priority:** equal with Claude, Claude Code, and Cursor IDE.  
**Certification status:** matrix below is **uncertified** until smoke evidence is recorded — that is an evidence gap, not a priority demotion.

Cursor IDE and Cursor Agent CLI are separate runtimes. Do not assume IDE plugin components load identically in the CLI.

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
agent --version || cursor agent --version || true
# Load local plugin dir if supported by your CLI build, then:
#   list skills / commands / agents and capture output
```

Community history includes plugin-skill parity gaps between IDE and CLI; re-verify on the org’s pinned CLI version.

## Product rule

1. **Priority:** Cursor Agent CLI ships at the same priority as Claude, Claude Code, and Cursor IDE.
2. **Honesty:** until skills + commands are evidenced `pass` on a pinned CLI version, label support **uncertified / in-progress** in release notes — never “out of scope”, “candidate”, or “nice-to-have”.
3. **Blocking:** production certification epic [#19](https://github.com/nanlabs/agent-toolkit/issues/19) requires CLI matrix progress alongside Claude and Cursor IDE evidence.
