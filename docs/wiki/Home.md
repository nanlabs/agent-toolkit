> **Note:** Canonical documentation lives under [`docs/`](https://github.com/nanlabs/agent-toolkit/tree/main/docs). This wiki is synced from `docs/wiki/` via GitHub Actions and may lag briefly after merges.

# NaNLABS agent-toolkit

Public **L1.5** distribution: one plugin per skill group, official hosted MCP, Agent Plugins roster + Claude Code.

**Install everything** (copy-paste): [Plugin marketplace](Plugin-Marketplace) · generated catalog: [`docs/generated/catalog.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/generated/catalog.md)

Machine provisioning stays in private [`internal-workstation`](https://github.com/nanlabs/internal-workstation). This repo does **not** ship a consumer CLI or loop runtime.

---

## Quick start

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then **`/nanlabs-core:setup`**. Repeat install for the other group plugins, or paste the complete block on [Plugin marketplace](Plugin-Marketplace).

### Cursor IDE

Symlink each `plugins/nanlabs-*` under `~/.cursor/plugins/local/` and reload, or import this repo as a Team Marketplace.

### GitHub Copilot

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
```

---

## Navigation

### Getting started

- [Installation](Installation) — all clients
- [Plugin marketplace](Plugin-Marketplace) — versions, complete install
- [Official MCP](MCP-Setup) — ClickUp, Linear, GitHub, Figma, …
- [Scope](Scope) · [FAQ](FAQ)

### Reference

- [Skills](Skills-Reference) · [Agents](Agents-Reference)
- [Lifecycle](Lifecycle) · [Cursor Agent CLI](Cursor-Agent-CLI)

### Contributing

- [Contributing](Contributing)

---

## Repo docs

| Doc | Topic |
| --- | --- |
| [`docs/ADOPTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/ADOPTION.md) | Adoption by client |
| [`docs/generated/catalog.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/generated/catalog.md) | Generated plugin / MCP / skill tables |
| [`docs/RELEASE.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/RELEASE.md) | Versions, tags, rollback |
| [`README.md`](https://github.com/nanlabs/agent-toolkit/blob/main/README.md) | Hero + architecture artwork |

## License

[MIT](https://github.com/nanlabs/agent-toolkit/blob/main/LICENSE)
