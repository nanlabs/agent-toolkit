# Wiki source (`docs/wiki/`)

Markdown here is the **source of truth** for the [GitHub Wiki](https://github.com/nanlabs/agent-toolkit/wiki).

This `README.md` stays in the git tree for contributors; the sync workflow **does not** publish it as a Wiki page.

On push to `main` (paths under `docs/wiki/**`), [`.github/workflows/wiki-sync.yml`](https://github.com/nanlabs/agent-toolkit/blob/main/.github/workflows/wiki-sync.yml) copies `*.md` into the wiki git repo.

## First-time setup

1. Open the [GitHub Wiki](https://github.com/nanlabs/agent-toolkit/wiki) and create the first page (e.g. Home) so GitHub creates the wiki repository.
2. Merge a PR that adds/updates `docs/wiki/`, or run **Actions → Sync Wiki → Run workflow**.

Until the wiki exists, the workflow logs “Wiki not initialized yet” and exits 0.

## Editing

Edit files in this directory (not the wiki UI) so changes stay reviewable in PRs.

**Generated (do not hand-edit):** `Plugin-Marketplace.md`, `Skills-Reference.md`, `MCP-Setup.md` — assembled by `python3 scripts/gen-surfaces.py` from `products/plugins.yaml` and catalogs. Keep NaNLABS scope smaller than personal multi-tool forks — see [Scope.md](Scope.md).
