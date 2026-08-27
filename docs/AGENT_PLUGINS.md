# Agent Plugins

This repository ships Agent Plugins v1.0.0 portable manifests alongside
client-native plugin surfaces. Agent Plugins is the open standard for portable
skills and MCP configuration:

- [Agent Plugins specification](https://agent-plugins.org/specification)
- [Agent Plugins manifest reference](https://agent-plugins.org/plugin-authors/manifest)
- [Agent Plugins v1.0.0 plugin schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [Agent Plugins v1.0.0 MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)

## Manifest and component model

The `nanlabs-core` and `nanlabs-agents` plugins each have a closed, root-level
`plugins/<name>/plugin.json` manifest. It contains the canonical `$schema`,
plugin identity and metadata.
The portable manifest intentionally does not declare `skills` or `agents` path
fields: Agent Plugins clients discover skills at `skills/<name>/SKILL.md`, and
native clients retain their own component rules.

| Surface | Manifest | Portable or native | Components |
| --- | --- | --- | --- |
| Agent Plugins | `plugin.json` | Portable | Skills; optional MCP via `mcp.json` |
| Claude Code | `.claude-plugin/plugin.json` | Native | Claude commands, skills, agents, hooks, and MCP |
| Cursor | `.cursor-plugin/plugin.json` | Native | Cursor rules, skills, agents, commands, hooks, variables, and MCP |
| GitHub Copilot CLI | Root `plugin.json` plus `agents/` | Portable manifest plus Copilot surface | Skills and Copilot agent files |

The root manifest is generated from `products/plugins.yaml` by
`scripts/gen-copilot-surfaces.py`. Do not hand-edit generated root manifests or
the generated Copilot surfaces.

## Client behavior

### Claude Code

Claude Code uses `plugins/<name>/.claude-plugin/plugin.json`. That native
manifest is unchanged by the portable Agent Plugins manifest, and
`claude plugin validate --strict` is a required CI gate. See Anthropic's
[plugin marketplace documentation](https://docs.anthropic.com/en/docs/claude-code/plugin-marketplaces).

### Cursor

Cursor supports both formats. Its marketplace resolution checks
`.cursor-plugin/plugin.json` first, so the native manifest remains authoritative
for Cursor. The root `plugin.json` can coexist for portable consumers. See the
[Cursor plugin reference](https://cursor.com/docs/reference/plugins).

### GitHub Copilot CLI

GitHub Copilot CLI recognizes a root `plugin.json`. Declaring the canonical
Agent Plugins `$schema` opts into Open Plugin Spec mode additively; when
component path fields are omitted, `agents/` and `skills/` are the defaults.
This preserves the existing Copilot agent files and generated repository
customization under `.github/`. See the official
[Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

### Agent Skills clients

The canonical skills remain available under `skills/<group>/<name>/` and follow
the [Agent Skills specification](https://agentskills.io/specification).
Portable consumers discover each skill through its immediate `SKILL.md` file;
the Agent Plugins validator does not treat nested directories as additional
skills.

## What is portable here

`nanlabs-core` exposes its skills as the portable component set. Its commands,
scripts, contracts, and setup automation are client-native and are not claimed
to be Agent Plugins v1 portable components.

`nanlabs-agents` is a native-agent distribution. Its agent files are useful to
Copilot and other supported native clients, but agents are not a portable
component in Agent Plugins v1.0.0.

No `mcp.json` ships in either plugin. The repository's MCP material under
`mcp/templates/` is documentation and configuration-template content, not a
runtime server distribution. If a plugin later adds `mcp.json`, it must use the
vendored Agent Plugins v1.0.0 MCP schema and keep executable paths and working
directories contained by the plugin path rules.

## Conformance policy

The canonical schemas are vendored under
`schemas/agent-plugins/1.0.0/` with pinned SHA-256 hashes. CI and local
validation use `scripts/validate-agent-plugins.py` to check:

- the closed plugin schema and exact canonical `$schema` URL;
- plugin naming and directory-name agreement;
- immediate skill discovery and regular `SKILL.md` files;
- realpath containment for plugin files and discovered skills; and
- future `mcp.json` schema, schema-version, and executable-path compatibility.

Validation never fetches schemas at runtime. Regenerate surfaces and run
`python3 scripts/validate-agent-plugins.py` after changing
`products/plugins.yaml` or plugin layout.
