# ❓ FAQ

## Is this only for Claude Code?

No. Production surfaces are **Claude**, **Claude Code**, **Cursor IDE**, **Cursor Agent CLI**, and **GitHub Copilot**. Skills-only (`npx skills`) covers additional Agent Skills–compatible clients without plugin support.

## How is this different from `ulises-jeremias/agent-toolkit`?

That project is a broader multi-tool toolkit (CLI, loops, many targets). **`nanlabs/agent-toolkit`** is the NaNLABS production L1.5 distribution: fewer surfaces, no consumer CLI/loops compiler, focused on Claude + Cursor + GitHub Copilot (+ skills-only).

## Do I need `internal-workstation`?

No for installing plugins/skills from this public repo. Yes for NaNLABS machine provisioning, secrets, and fleet doctor. Workstation remains L1; this repo is L1.5 content.

## Why isn’t MCP available after installing the plugin?

MCP templates under `mcp/templates/` are **docs-only**. Plugins do not install MCP servers. Configure MCP separately using the stubs as reference.

## Where did `nanlabs-setup` go?

Merged into **`nanlabs-core`** (v0.3.0+). Use `/nanlabs-core:setup`. The old plugin directory may remain with a deprecation notice but is not in the marketplace catalog.

## Skills-only vs plugins?

| | Skills-only | Plugins (`nanlabs-core`) |
| --- | --- | --- |
| Skills | Yes | Yes (bundled subset + full tree via skills CLI) |
| Agents | No | Core reviewer; full roster via `nanlabs-agents` |
| Setup doctor | No | Yes (`/nanlabs-core:setup`) |
| MCP | No | No (docs-only either way) |

## Can I use this on client projects?

Yes — prefer marketplace/skills install without copying private NaN paths. Follow [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md). Do not commit client secrets into overlays.

## Cursor Agent CLI vs Cursor IDE?

Separate runtimes. CLI is equal **priority**; certification is tracked in [Cursor Agent CLI](Cursor-Agent-CLI). Prefer `--plugin-dir` until interactive `/plugins` install is fully evidenced.
