> **Note:** Canonical documentation lives under [`docs/`](https://github.com/nanlabs/agent-toolkit/tree/main/docs). This wiki is synced from `docs/wiki/` via GitHub Actions and may lag briefly after merges.

# 🏠 NaNLABS agent-toolkit

Public **L1.5** distribution of NaNLABS skills, agents, and plugins.

| Surface | Priority |
| --- | --- |
| Claude | Equal |
| Claude Code | Equal |
| Cursor IDE | Equal |
| Cursor Agent CLI | Equal |
| GitHub Copilot | Supported |

Machine provisioning stays in [`internal-workstation`](https://github.com/nanlabs/internal-workstation). This repo does **not** ship a consumer CLI, loop runtime, multi-tool profile compiler, or OpenCode/Windsurf/Gemini CLI/Pi plugin targets.

---

## ✨ What is included

| Component | Count | Notes |
| --- | --- | --- |
| Skills | 48 | Agent Skills tree under `skills/<group>/` |
| Agents | 16 | Canonical personas; flat plugin surfaces via `gen-surfaces` |
| Plugins | 2 marketplace | `nanlabs-core` (recommended) · `nanlabs-agents` (optional) |
| MCP templates | 6 | **Docs-only** stubs — not installed by plugins |
| Copilot | 2 surfaces | CLI plugin manifests + repository customization |

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

Skills only — no plugins, agents, MCP, or setup automation.

### GitHub Copilot

CLI plugin manifests are generated in `plugins/nanlabs-core/` and `plugins/nanlabs-agents/`.
Repository customization lives under `.github/copilot-instructions.md`, `.github/agents/`, and `.github/skills/`.

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
| [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md) | What may be published |
| [`README.md`](https://github.com/nanlabs/agent-toolkit/blob/main/README.md) | Hero + architecture artwork |

## License

[MIT](https://github.com/nanlabs/agent-toolkit/blob/main/LICENSE)
