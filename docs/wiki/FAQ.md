# FAQ

Quick answers. Install steps: [Installation](Installation). Day-to-day: [Using the toolkit](Using).

## Is this only for Claude Code?

No. Production is the [Agent Plugins roster](https://agent-plugins.org/compatible-clients) **plus** Claude Code. Skills-only (`npx skills`) covers Agent Skills clients without plugin support.

## How do I install everything?

Paste the complete block on [Plugin marketplace](Plugin-Marketplace). Start with `nanlabs-core` if you want a smaller first install.

## Do I need `internal-workstation`?

No for installing plugins or skills from this public repo. Yes for NaNLABS machine provisioning, secrets, and fleet doctor.

## Why isn’t MCP available after installing a plugin?

`nanlabs-core` does **not** ship MCP. Install `nanlabs-design`, `nanlabs-forge`, or `nanlabs-integrations`, reload, and complete OAuth. Skills-only installs never register servers. Slack may need Slack’s own client plugin (no Dynamic Client Registration).

If Cursor already has ClickUp / Shortcut / Linear in `~/.cursor/mcp.json`, plugin MCP can duplicate those servers — keep one of each. Full table: [Official MCP](MCP-Setup).

## Where did `nanlabs-setup` go?

Merged into **`nanlabs-core`**. Use `/nanlabs-core:setup`.

## Skills-only vs plugins?

See the comparison table on [Using the toolkit](Using). Short version: `npx skills` is skills only; group plugins add agents, setup, and official MCP.

## How do I share or add a skill?

[Add a skill](Add-a-Skill). Open a **Propose skill** issue, then a PR against **nanlabs/agent-toolkit**.

## Can I use this on client projects?

Yes — marketplace or `npx skills`, no private NaN paths. Follow [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md).

## Cursor Agent CLI vs Cursor IDE?

Separate runtimes, equal **product** priority. Evidence: [Cursor Agent CLI](Cursor-Agent-CLI).

## How is this different from `ulises-jeremias/agent-toolkit`?

That project is a broader multi-tool toolkit (CLI, loops, many targets). **`nanlabs/agent-toolkit`** is the NaNLABS production L1.5 distribution: no consumer CLI or loops compiler. See [Scope](Scope).

## The wiki looks out of date

Pages are edited in `docs/wiki/` and sync on merge to `main`. If you just merged, wait for the **Sync Wiki** workflow. Source: [Contributing](Contributing).
