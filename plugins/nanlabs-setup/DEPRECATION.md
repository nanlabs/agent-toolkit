# nanlabs-setup — deprecated

**Status:** Deprecated as of `nanlabs-core` v0.2.0. Removed from marketplace listings.

Setup (contract doctor, `/setup` command, and `nanlabs-setup` skill) now ships inside **`nanlabs-core`**.

## Migrate

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Use the namespaced command **`/nanlabs-core:setup`** (Claude Code).

You may uninstall the standalone `nanlabs-setup` plugin if it was previously installed.

## Why

- Single recommended install path (#49)
- Self-contained doctor + contracts inside the plugin (#55) — no git checkout required

This directory remains for one release cycle as a redirect stub; it will be removed in a future version.
