# ❓ FAQ

## Is this only for Claude Code?

No. Production surfaces are the [Agent Plugins roster](https://agent-plugins.org/compatible-clients) plus Claude Code. Skills-only (`npx skills`) covers additional Agent Skills–compatible clients without plugin support.

## How is this different from `ulises-jeremias/agent-toolkit`?

That project is a broader multi-tool toolkit (CLI, loops, many targets). **`nanlabs/agent-toolkit`** is the NaNLABS production L1.5 distribution: fewer surfaces, no consumer CLI/loops compiler, focused on Claude + Cursor + GitHub Copilot (+ skills-only).

## Do I need `internal-workstation`?

No for installing plugins/skills from this public repo. Yes for NaNLABS machine provisioning, secrets, and fleet doctor. Workstation remains L1; this repo is L1.5 content.

## Why isn’t MCP available after installing the plugin?

Install `nanlabs-design`, `nanlabs-forge`, or `nanlabs-integrations` and complete OAuth. `nanlabs-core` does not ship MCP. Skills-only installs do not register servers. Slack may need Slack’s own client plugin (no Dynamic Client Registration).

## Where did `nanlabs-setup` go?

Merged into **`nanlabs-core`** (v0.3.0+). Use `/nanlabs-core:setup`. The old plugin directory may remain with a deprecation notice but is not in the marketplace catalog.

## Skills-only vs plugins?

| | Skills-only | Plugins (`nanlabs-core`) |
| --- | --- | --- |
| Skills | Yes (49 via `npx skills`; packs in [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md)) | Yes (group plugin skills; `nanlabs-core` has 7) |
| Agents | No | Core reviewer; full roster via `nanlabs-agents` |
| Setup doctor | No | Yes (`/nanlabs-core:setup`) |
| MCP | No | Yes, on design / forge / integrations plugins |

## How do I share a skill?

Open a **Propose skill** issue and a pull request. Maintainers review for security, duplication, and quality. See [`docs/CONTRIBUTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CONTRIBUTION.md).

## Can I use this on client projects?

Yes — prefer marketplace/skills install without copying private NaN paths. Follow [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md). Do not commit client secrets into overlays.

## Cursor Agent CLI vs Cursor IDE?

Separate runtimes. CLI is equal **priority**; certification is tracked in [Cursor Agent CLI](Cursor-Agent-CLI). Prefer `--plugin-dir` until interactive marketplace installation is evidenced for the pinned CLI build.
