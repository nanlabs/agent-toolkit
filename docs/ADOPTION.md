> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-05**
>
> This document lives only in the repo. It is public-ready and self-contained.
> If a ClickUp mirror is created later, update this banner with the link.

---

# Adoption

How to install and use `nanlabs/agent-toolkit`.

## Claude Code (recommended)

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Invoke setup via the **namespaced** plugin command: **`/nanlabs-core:setup`**, or ask Claude to run the bundled `nanlabs-setup` skill.

Optional full agent roster:

```text
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

> **Deprecated:** `nanlabs-setup` as a separate plugin is no longer in the marketplace. Setup ships inside `nanlabs-core` (v0.2.0+).

Lifecycle (update / pin / rollback): [`LIFECYCLE.md`](LIFECYCLE.md).

## Cursor

1. **Local development:** place or symlink a plugin under `~/.cursor/plugins/local/` and reload the window.
2. **Team:** import this repository as a Team Marketplace (org admin; Teams or Enterprise).

Install **`nanlabs-core`** (recommended). Optionally install **`nanlabs-agents`**.

Marketplace entries use only `name`, `source`, `description`, and optional `minClientVersions` per the official Cursor schema.

See [Cursor plugins](https://cursor.com/docs/plugins).

## Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

Installs the grouped tree `skills/<group>/<skill>/` (47 skills, including `nanlabs-setup`).

Skills-only installs do **not** bundle the contract doctor; use baseline spot-checks in the skill or clone the repo for full validation.

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
- `nanlabs-core` is installed; `/nanlabs-core:setup` runs the bundled doctor without a git checkout.
- `npx skills` discovers nested skills under `skills/<group>/`.
- No secrets were required to install the plugin or skills themselves.

## Related docs

- [`P0_FINDINGS.md`](P0_FINDINGS.md) — feasibility + lifecycle matrix
- [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md) — what may be published
- [`AUTHORING.md`](AUTHORING.md) — how to add skills/plugins
- [`../AGENTS.md`](../AGENTS.md) — contributor contract for this repo
