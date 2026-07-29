# Adoption

How to install and use `nanlabs/agent-toolkit`.

## Claude Code (recommended for P0)

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
```

Then ask Claude to run setup, or use the `/setup` command shipped with the plugin.

## Cursor (after lifecycle validation)

1. Import this repository as a Team Marketplace (org admin), **or**
2. Install the `nanlabs-setup` plugin from `.cursor-plugin/marketplace.json` once team import is configured.

P0 prioritizes Claude Code; Cursor packaging is present so the same canonical content can be reused without duplication.

## Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

This installs the canonical `skills/` tree (including `nanlabs-setup`).

## What success looks like

- Marketplace add succeeds without private-repo auth for this public repository.
- `nanlabs-setup` skill is available and can report Git / Python / package-manager presence.
- No secrets were required to install the plugin itself.

## Related docs

- `docs/PUBLIC_CONTENT_POLICY.md` — what may be published
- `docs/AUTHORING.md` — how to add skills/plugins
- `AGENTS.md` — agent contract for contributors working in this repo
