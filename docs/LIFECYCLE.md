> Also see [RELEASE.md](RELEASE.md) for tags, changelog, and rollback policy.
>
> [!NOTE]
> 📘 **ClickUp Companion**, last synced **2026-08-27**
>
> This document is mirrored in the NaNLABS internal ClickUp workspace for cross-team discovery and execution logging.
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

---

# Lifecycle — install, update, pin, rollback

Short operator guide for distributing `nanlabs/agent-toolkit`. Release tags and rollback policy: [`RELEASE.md`](RELEASE.md).

## Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

| Action | Command / mechanism |
| --- | --- |
| Refresh catalog | `/plugin marketplace update nanlabs-agent-toolkit` |
| Update plugin | `/plugin update nanlabs-core` then `/reload-plugins` if prompted |
| Disable | `/plugin disable nanlabs-core` |
| Uninstall | `/plugin uninstall nanlabs-core` |
| Pin | Set `"version": "x.y.z"` in `plugins/.../plugin.json` and bump to release |
| Rollback | Revert version / pin marketplace source to prior git SHA, then marketplace update |

Org: add the marketplace via managed `extraKnownMarketplaces`. Prefer auto-update **off** for third-party until policy is set.

## Any agent (skills CLI)

```bash
npx skills add nanlabs/agent-toolkit -g
npx skills check
npx skills update -g
npx skills remove <skill-name> -g
```

Project-scope installs can write `skills-lock.json` for reproducibility (CLI restore commands are evolving — see upstream `vercel-labs/skills`).

## Cursor IDE

1. **Local test:** copy or symlink a plugin under `~/.cursor/plugins/local/<name>` and reload.
2. **Team:** Dashboard → Plugins → import this GitHub repo (Teams/Enterprise admin).
3. Modes: Default Off / Default On / Required.
4. Updates: Refresh or enable Auto Refresh (GitHub App).

Install **`nanlabs-core`** first, then the other `nanlabs-*` group plugins for a complete skill set; optionally **`nanlabs-agents`**. Setup: `/nanlabs-core:setup` when the IDE surfaces plugin commands.

## Cursor Agent CLI

Equal priority with Cursor IDE. Record binary/version and use the supported
local load path for reproducible CLI smoke tests:

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

`marketplace add` registers the catalog; it does not install a plugin. The
repository's evidence snapshot does not certify a non-interactive CLI install.
See the current matrix in [`CURSOR_CLI.md`](CURSOR_CLI.md).

## GitHub Copilot CLI

```bash
copilot plugin update nanlabs-core
copilot plugin uninstall nanlabs-core
```

Use the GitHub repository subdirectory specification to reinstall a plugin:
`copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core`.

## Official MCP

Group plugins `nanlabs-design`, `nanlabs-forge`, and `nanlabs-integrations`
ship official hosted MCP URLs from `catalogs/mcp-catalog.yaml`. Authenticate
in the client after install. Never commit tokens; see each template README
and [`wiki/MCP-Setup.md`](wiki/MCP-Setup.md).

## Local validation

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
python3 scripts/gen-surfaces.py --check
bash scripts/secret-scan.sh
```

Keep live Claude Code / Cursor IDE / Cursor Agent CLI evidence in [`RELEASE.md`](RELEASE.md) and [`CURSOR_CLI.md`](CURSOR_CLI.md).
