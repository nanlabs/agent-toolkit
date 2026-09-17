# Agent Plugins

This repository ships Agent Plugins v1.0.0 portable manifests alongside
client-native plugin surfaces. Agent Plugins is the open standard for portable
skills and MCP configuration:

- [Agent Plugins specification](https://agent-plugins.org/specification)
- [Agent Plugins manifest reference](https://agent-plugins.org/plugin-authors/manifest)
- [Agent Plugins v1.0.0 plugin schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [Agent Plugins v1.0.0 MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)
- [Compatible clients](https://agent-plugins.org/compatible-clients) (JS table; snapshot 2026-08-13)

Install flows: [`ADOPTION.md`](ADOPTION.md). Production = the nine roster
clients **plus** Claude Code (native dual-rail; not on that roster).

There is **no** `plugin.json` at the repository root. Each group is its own
package under `plugins/nanlabs-<group>/`. Skill bodies live only there
(`skills/<name>/SKILL.md`). `gen-surfaces` writes manifests, not skill copies.

## Manifest and component model

Each group plugin has a closed, root-level `plugins/<name>/plugin.json`.
The portable manifest does not declare `skills` or `agents` path fields:
Agent Plugins clients discover skills at `skills/<name>/SKILL.md`, and
native clients retain their own component rules.

| Surface | Manifest | Portable or native | Components |
| --- | --- | --- | --- |
| Agent Plugins | `plugin.json` | Portable | Skills; optional MCP via `mcp.json` |
| Claude Code | `.claude-plugin/plugin.json` | Native | Claude commands, skills, agents, hooks, and MCP |
| Cursor | `.cursor-plugin/plugin.json` | Native | Cursor rules, skills, agents, commands, hooks, variables, and MCP |
| GitHub Copilot / VS Code | Root `plugin.json` plus `agents/` and `com.github.copilot/agents/` | Portable manifest plus Copilot surface | Skills and Copilot agent files |
| ChatGPT / Codex | `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json`, `.agents/plugins/marketplace.json` | Marketplace catalogs | Skills |

The root manifest is generated from `products/plugins.yaml` by
`scripts/gen-surfaces.py` / `scripts/gen-copilot-surfaces.py`. Do not hand-edit
generated root manifests or generated Copilot agent files.

## Official roster (9) + Claude Code

Source: [compatible-clients](https://agent-plugins.org/compatible-clients)
(page is client-side JS; re-check when implementing). All listed clients load
**Agent Skills**. MCP support varies. Design, forge, and integrations ship official hosted MCP in `mcp.json` (remote HTTPS + client OAuth).

| Client | How to load a group plugin |
| --- | --- |
| VS Code | `chat.plugins.enabled` + `chat.plugins.marketplaces: ["nanlabs/agent-toolkit"]`, then @agentPlugins; or Install Plugin From Source |
| GitHub Copilot | `copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-<group>` |
| Cursor | Team Marketplace or `--plugin-dir plugins/nanlabs-<group>` |
| ChatGPT & Codex | `codex plugin marketplace add nanlabs/agent-toolkit` then Plugins Directory |
| Kiro | Import folder `plugins/nanlabs-<group>` (`keywords` activate the power) |
| Grok Bot | Folder / Cursor-style plugin directory |
| Hermes Agent, OpenClaw, NanoClaw | Point at `plugins/nanlabs-<group>` (`plugin.json` + `skills/<name>/`) |
| Claude Code (not on the roster) | `/plugin marketplace add nanlabs/agent-toolkit` + `/plugin install <id>@nanlabs-agent-toolkit` |

**Out of production scope:** Gemini, Antigravity, OpenCode.

Complete install = nine group plugins + optional `nanlabs-agents`.

## Client notes

### Claude Code

Uses `plugins/<name>/.claude-plugin/plugin.json`. `claude plugin validate`
(and `--strict` except the deprecated `nanlabs-setup` plugin) is a CI gate.
See Anthropic's
[plugin marketplace documentation](https://docs.anthropic.com/en/docs/claude-code/plugin-marketplaces).

### Cursor

Checks `.cursor-plugin/plugin.json` first. The root `plugin.json` coexists for
portable consumers. Shipped MCP servers are remote URLs (no `${PLUGIN_ROOT}`).
Cursor does not expand `${PLUGIN_ROOT}` / `${PLUGIN_DATA}` in `mcp.json` if a
stdio server is added later. See the [Cursor plugin reference](https://cursor.com/docs/reference/plugins).

### GitHub Copilot and VS Code

Copilot CLI recognizes a root `plugin.json`. Declaring the canonical Agent
Plugins `$schema` opts into Open Plugin Spec mode additively; when component
path fields are omitted, `agents/` and `skills/` are the defaults. VS Code
Copilot agents live under `com.github.copilot/agents/`. Repository
customization is `.github/copilot-instructions.md` and `.github/agents/`
(skills are **not** mirrored under `.github/skills/`).

### ChatGPT and Codex

Codex reads Claude and Cursor marketplace files. ChatGPT desktop documents
`.agents/plugins/marketplace.json` with `source.path` prefixed `./`.

## Packs

[`PACKS.md`](PACKS.md) names catalog aliases. **Group** packs are the same
directories as group plugins. **Domain** packs (`code-review`, `qa`, …) are
`npx --skill` lists and are not Agent Plugins packages.

To expose a new skill: add `plugins/nanlabs-<group>/skills/<name>/SKILL.md`
and a row in `catalogs/skills-layout.json` / `skill-catalog.yaml`. Do not add
`skills` or `agents` path fields to `plugin.json` (closed schema,
[§5.2](https://agent-plugins.org/specification#52-manifest-object)).
Agents remain native-only (v1 portable component types are skills and MCP only).

Native Claude Code and Cursor files (`.claude-plugin/`, `.cursor-plugin/`,
`commands/`, Copilot `agents/*.agent.md`) sit beside the portable package.
Agent Plugins clients ignore those extra directories: they are not v1
component types and they are not reverse-domain extension namespaces
(`com.github.copilot` is the Copilot extension namespace).

## What is portable here

Each `nanlabs-<group>` plugin exposes its skills as the portable component set.
`nanlabs-core` also ships client-native setup (commands, doctor scripts,
contracts) that are not claimed as Agent Plugins v1 portable components.

`nanlabs-agents` is a native-agent distribution. Its agent files are useful to
Copilot and other supported native clients, but agents are not a portable
component in Agent Plugins v1.0.0.

`nanlabs-design`, `nanlabs-forge`, and `nanlabs-integrations` ship `mcp.json`
(Agent Plugins schema, `type: streamable-http`) and `.mcp.json` (Claude Code,
`type: http`) from [`catalogs/mcp-catalog.yaml`](../catalogs/mcp-catalog.yaml).
Auth is client-managed OAuth; headers and tokens are not packaged. Templates
under `mcp/templates/` document the same official URLs.

## Conformance policy

The canonical schemas are vendored under
`schemas/agent-plugins/1.0.0/` with pinned SHA-256 hashes. CI uses
`scripts/validate-agent-plugins.py` and `scripts/validate-skill-inventory.py`:

- the closed plugin schema and exact canonical `$schema` URL;
- plugin naming and directory-name agreement;
- immediate skill discovery and regular `SKILL.md` files;
- one inventory copy per layout skill (no `skills/<group>/`, no `.github/skills/`);
- realpath containment for plugin files and discovered skills; and
- `mcp.json` schema, schema-version match, and no secrets in headers.

Validation never fetches schemas at runtime. Regenerate manifests and run
`python3 scripts/validate-agent-plugins.py` after changing
`products/plugins.yaml`.
