> Also see [RELEASE.md](RELEASE.md) for tags, changelog, and rollback policy.

> [!IMPORTANT]
> 📘 **ClickUp Companion**, last synced **2026-08-03**
>
> This document is mirrored in ClickUp for cross-team discovery and execution logging:
>
> - 📑 **[NaN Workbench (Practices)](https://app.clickup.com/459857/docs/e12h-314297/e12h-156797)**
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

<!-- Internal: ClickUp links require NaNLABS workspace access -->

---

# Lifecycle — install, update, pin, rollback

Short operator guide for distributing `nanlabs/agent-toolkit`. Full evidence and sources: [`P0_FINDINGS.md`](P0_FINDINGS.md).

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

Install **`nanlabs-core`** (recommended); optionally **`nanlabs-agents`**. Setup: `/nanlabs-core:setup` when the IDE surfaces plugin commands.

## Cursor Agent CLI

Equal priority with Cursor IDE. Record binary/version, load plugins per CLI support, and update [`CURSOR_CLI.md`](CURSOR_CLI.md).

```bash
agent --version || cursor agent --version || true
bash scripts/smoke/preflight.sh
```

Paste CLI matrix results on GitHub issue #58 / #8.

## MCP stubs

Templates under `mcp/templates/` use `${ENV_VAR}` placeholders only. Never commit tokens. See each template README.


## Local preflight

```bash
bash scripts/smoke/preflight.sh
```

Paste live Claude Code / Cursor IDE / Cursor Agent CLI results on GitHub issue #8 (CLI matrix: #58).
