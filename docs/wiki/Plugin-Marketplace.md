# Plugin marketplace

Marketplace catalogs:

- Claude: [`.claude-plugin/marketplace.json`](https://github.com/nanlabs/agent-toolkit/blob/main/.claude-plugin/marketplace.json)
- Cursor: [`.cursor-plugin/marketplace.json`](https://github.com/nanlabs/agent-toolkit/blob/main/.cursor-plugin/marketplace.json) (official schema: `name` / `source` / `description` / optional `minClientVersions` only on entries)

Version SoT: [`products/plugins.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/products/plugins.yaml) · sync via `python3 scripts/gen-surfaces.py`.

## Plugins

| Plugin | Version (see SoT) | Contents |
| --- | --- | --- |
| `nanlabs-core` | 0.2.x | Setup/onboarding, orchestrator skills, `/nanlabs-core:setup`, `nanlabs-code-reviewer` |
| `nanlabs-agents` | 0.1.x | Full agent roster |

Deprecated: standalone `nanlabs-setup` (not listed in marketplace).

## Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

## Cursor

Team Marketplace import or local `~/.cursor/plugins/local`. Cursor Agent CLI: see [Cursor Agent CLI](Cursor-Agent-CLI).

## Building / validating

```bash
python3 scripts/gen-surfaces.py
python3 scripts/gen-surfaces.py --check
python3 scripts/validate-manifests.py
claude plugin validate --strict plugins/nanlabs-core
```
