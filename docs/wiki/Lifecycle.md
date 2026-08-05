# 🔄 Lifecycle — update, pin, rollback

Canonical: [`docs/LIFECYCLE.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/LIFECYCLE.md) · release policy: [`docs/RELEASE.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/RELEASE.md).

## Claude Code

| Action | Command |
| --- | --- |
| Refresh catalog | `/plugin marketplace update nanlabs-agent-toolkit` |
| Update plugin | `/plugin update nanlabs-core` |
| Disable / uninstall | `/plugin disable` · `/plugin uninstall` |
| Pin / rollback | Pin `version` in plugin manifest or marketplace source SHA; then refresh |

## Cursor IDE

Refresh / Auto Refresh on Team Marketplace; for local installs re-copy or re-symlink and reload.

## Cursor Agent CLI

Re-run marketplace update / `--plugin-dir` against a tagged commit. Record CLI version in the certification matrix.

## Skills-only

```bash
npx skills update -g
npx skills remove <skill-name> -g
```

## Local preflight

```bash
bash scripts/smoke/preflight.sh
```
