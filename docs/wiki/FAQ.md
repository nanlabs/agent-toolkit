# FAQ

## Is this only for Claude Code?

No. Production is the [Agent Plugins roster](https://agent-plugins.org/compatible-clients) **plus** Claude Code. Skills-only (`npx skills`) covers Agent Skills clients without plugin support.

## How do I install everything?

Paste the complete block on [Plugin marketplace](Plugin-Marketplace). Start with `nanlabs-core` if you want a smaller first install.

## How is this different from `ulises-jeremias/agent-toolkit`?

That project is a broader multi-tool toolkit (CLI, loops, many targets). **`nanlabs/agent-toolkit`** is the NaNLABS production L1.5 distribution: no consumer CLI/loops compiler.

## Do I need `internal-workstation`?

No for installing plugins/skills from this public repo. Yes for NaNLABS machine provisioning, secrets, and fleet doctor.

## Why isn’t MCP available after installing a plugin?

`nanlabs-core` does not ship MCP. Install `nanlabs-design`, `nanlabs-forge`, or `nanlabs-integrations`, reload, and complete OAuth. Skills-only installs never register servers. Slack may need Slack’s own client plugin (no Dynamic Client Registration).

If Cursor already has ClickUp / Shortcut / Linear in `~/.cursor/mcp.json`, plugin MCP can duplicate those servers — keep one of each.

## Where did `nanlabs-setup` go?

Merged into **`nanlabs-core`**. Use `/nanlabs-core:setup`.

## Skills-only vs plugins?

| | Skills-only | Group plugins |
| --- | --- | --- |
| Skills | Yes (`npx skills`) | Yes (per group) |
| Agents | No | Core reviewer; full roster via `nanlabs-agents` |
| Setup doctor | No | Yes (`/nanlabs-core:setup`) |
| MCP | No | Yes, on design / forge / integrations |

## How do I share a skill?

Open a **Propose skill** issue and a pull request. See [`docs/CONTRIBUTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CONTRIBUTION.md).

## Can I use this on client projects?

Yes — marketplace/skills install, no private NaN paths. Follow [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md).

## Cursor Agent CLI vs Cursor IDE?

Separate runtimes, equal **product** priority. Evidence: [Cursor Agent CLI](Cursor-Agent-CLI).
