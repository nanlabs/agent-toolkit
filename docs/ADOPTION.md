# Adoption

How to install and use `nanlabs/agent-toolkit`.

## Claude Code (recommended)

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

Then ask Claude to run setup, or use the `/setup` command shipped with the plugin.

Lifecycle (update / pin / rollback): [`LIFECYCLE.md`](LIFECYCLE.md).

## Cursor

1. **Local development:** place or symlink a plugin under `~/.cursor/plugins/local/` and reload the window.
2. **Team:** import this repository as a Team Marketplace (org admin; Teams or Enterprise).

See [Cursor plugins](https://cursor.com/docs/plugins).

## Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

Installs the grouped tree `skills/<group>/<skill>/` (47 skills, including `nanlabs-setup`).

Skill index: [`SKILLS.md`](SKILLS.md) · machine catalog: [`../catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml).

## Agents and MCP

- Agents: [`../agents/README.md`](../agents/README.md) (16 personas; plugin `nanlabs-agents`)
- MCP stubs: [`../mcp/templates/README.md`](../mcp/templates/README.md) (6 stubs; env placeholders only)
- Dependency contracts: [`../contracts/README.md`](../contracts/README.md)
- Solution packs (stubs): [`../packs/README.md`](../packs/README.md)
- Overlay governance: [`OVERLAY_GOVERNANCE.md`](OVERLAY_GOVERNANCE.md)
- Telemetry ownership: [`TELEMETRY_CONTRACT.md`](TELEMETRY_CONTRACT.md)

## What success looks like

- Marketplace add succeeds without private-repo auth for this public repository.
- `nanlabs-setup` is available and can report Git / Python / package-manager presence.
- `npx skills` discovers nested skills under `skills/<group>/`.
- No secrets were required to install the plugin or skills themselves.

## Related docs

- [`P0_FINDINGS.md`](P0_FINDINGS.md) — feasibility + lifecycle matrix
- [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md) — what may be published
- [`AUTHORING.md`](AUTHORING.md) — how to add skills/plugins
- [`../AGENTS.md`](../AGENTS.md) — contributor contract for this repo
