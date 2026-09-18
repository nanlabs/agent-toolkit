# Using the toolkit

You already installed at least `nanlabs-core`. This page is day-to-day use.

> [!TIP]
> After Claude Code install, run **`/nanlabs-core:setup`**. Then ask: “What NaNLABS skills are available?”

## Verify it loaded

| Client | Check |
| --- | --- |
| Claude Code | Skills listed; `/nanlabs-core:setup` and `/nanlabs-core:core-help` exist |
| Cursor IDE | Plugin skills visible after reload; MCP servers appear for design/forge/integrations |
| Copilot CLI | `copilot plugin list` shows `nanlabs-*` |
| Cursor Agent CLI | `--plugin-dir` smoke on [Cursor Agent CLI](Cursor-Agent-CLI) |
| Skills-only | `npx skills check` lists nested skills |

## Which plugin do I need?

Speak to the agent in normal language. The orchestrator (`nanlabs-assistant` in core) routes to the right skill. Install the **group** that owns that skill.

| If you are doing… | Install |
| --- | --- |
| First-time setup, repo inspection, handoffs | `nanlabs-core` |
| PRD / TRD / ADR / stories / assessments | `nanlabs-delivery` |
| `gh` / `glab` PRs, CI comments | `nanlabs-forge` (+ GitHub/GitLab MCP) |
| ClickUp, Slack, Linear, Notion, Jira/Confluence | `nanlabs-integrations` (+ those MCP servers) |
| Figma file context / UI implementation | `nanlabs-design` (+ Figma MCP) |
| dbt or Snowflake checks | `nanlabs-data` |
| Playwright or Jupyter | `nanlabs-tooling` |
| Client delivery phases | `nanlabs-workflow` |
| Extra specialist personas | `nanlabs-agents` |

Exact skill names: [Skills reference](Skills-Reference). Exact versions and copy-paste: [Plugin marketplace](Plugin-Marketplace).

## Official MCP

Plugins never contain tokens. After you install design / forge / integrations:

1. Reload the client.
2. Complete the browser OAuth prompt.
3. Slack may need a workspace admin to approve MCP.

Details and the URL table: [Official MCP](MCP-Setup).

> [!WARNING]
> If Cursor already has ClickUp, Shortcut, or Linear in `~/.cursor/mcp.json`, plugin MCP can **duplicate** those servers. Keep one of each.

## Skills-only vs plugins

| | `npx skills` | Group plugins |
| --- | --- | --- |
| Skills | Yes | Yes |
| Agents | No | Core reviewer; full roster via `nanlabs-agents` |
| `/nanlabs-core:setup` | No | Yes |
| Official MCP | No | Yes, on design / forge / integrations |

## Update, pin, rollback

See [Updates and rollback](Lifecycle). NaNLABS laptops pin a git tag with `NAN_AGENT_TOOLKIT_VERSION` after `nan-ai-enable`.

## Something broken?

[FAQ](FAQ) covers the usual cases (no MCP after core-only install, `nanlabs-setup` moved into core, skills-only vs plugins).
