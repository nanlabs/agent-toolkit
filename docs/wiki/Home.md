> **Note:** Canonical documentation lives under [`docs/`](https://github.com/nanlabs/agent-toolkit/tree/main/docs). This wiki is synced from `docs/wiki/` via GitHub Actions and may lag briefly after merges.

# 🏠 NaNLABS agent-toolkit

Public **L1.5** distribution of NaNLABS skills, agents, and plugins.

| Surface | Priority |
| --- | --- |
| Agent Plugins roster (9) | Equal |
| Claude Code (native) | Equal |

Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation). This repo does **not** ship a consumer CLI, loop runtime, multi-tool profile compiler, or OpenCode/Windsurf/Gemini CLI/Pi plugin targets.

---

## ✨ What is included

| Component | Count | Notes |
| --- | --- | --- |
| Skills | 49 | `plugins/nanlabs-<group>/skills/` |
| Agents | 18 | Canonical personas; flat plugin surfaces via `gen-surfaces` |
| Plugins | 10 marketplace | nine group plugins · `nanlabs-agents` (optional) |
| MCP | 9 official | Shipped by `nanlabs-design` / `nanlabs-forge` / `nanlabs-integrations` |
| Copilot | 2 surfaces | Agent Plugins manifests + repository customization |

---

## 🚀 Quick install

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run **`/nanlabs-core:setup`**.

### Cursor IDE

Local plugins under `~/.cursor/plugins/local`, or Team Marketplace import of this repo. Install **`nanlabs-core`**.

### Cursor Agent CLI

Equal priority — see [Cursor Agent CLI](Cursor-Agent-CLI). Prefer `--plugin-dir` for local certification.

### Skills-only

```bash
npx skills add nanlabs/agent-toolkit -g
```

Group pack (subdirectory) or domain pack: see [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md).

```bash
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills
```

Skills only — no plugins, agents, MCP, or setup automation.

### GitHub Copilot

Install a plugin directly from this repository:

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
```

Agent Plugins v1.0.0 manifests live in each `plugins/nanlabs-*` directory.
Repository customization lives under `.github/copilot-instructions.md` and `.github/agents/`.

---

## 📚 Navigation

### Getting started

- [📦 Installation](Installation) — all install paths
- [🎯 Scope](Scope) — in / out of product scope
- [❓ FAQ](FAQ) — common questions

### Reference

- [🛠️ Skills](Skills-Reference) · [🤖 Agents](Agents-Reference)
- [🔌 Plugin Marketplace](Plugin-Marketplace) · [🔗 MCP Templates](MCP-Setup)
- [🔄 Lifecycle](Lifecycle) · [⌨️ Cursor Agent CLI](Cursor-Agent-CLI)

### Contributing

- [🤝 Contributing](Contributing)

---

## 📖 Repo docs (deep dive)

| Doc | Topic |
| --- | --- |
| [`docs/ADOPTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/ADOPTION.md) | Adoption by surface |
| [`docs/RELEASE.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/RELEASE.md) | Versions, tags, rollback |
| [`docs/AUTHORING.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/AUTHORING.md) | Add skills / plugins |
| [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md) | Domain pack install |
| [`docs/CONTRIBUTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CONTRIBUTION.md) | Propose a skill via PR |
| [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md) | What may be published |
| [`README.md`](https://github.com/nanlabs/agent-toolkit/blob/main/README.md) | Hero + architecture artwork |

## License

[MIT](https://github.com/nanlabs/agent-toolkit/blob/main/LICENSE)
