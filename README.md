<div align="center">

<img alt="NaNLABS agent-toolkit" src="static/hero-banner.svg" width="1280">

# agent-toolkit

NaNLABS skills, agents, and plugins — install once, use in Claude Code, Cursor, Copilot, and the [Agent Plugins](https://agent-plugins.org/compatible-clients) roster.

[Wiki](https://github.com/nanlabs/agent-toolkit/wiki) · [Install plugins](https://github.com/nanlabs/agent-toolkit/wiki/Installation) · [Add a skill](https://github.com/nanlabs/agent-toolkit/wiki/Add-a-Skill) · [Contribute](https://github.com/nanlabs/agent-toolkit/wiki/Contributing)

<p>
  <a href="https://github.com/nanlabs/agent-toolkit/wiki"><img src="https://img.shields.io/badge/GitHub-Wiki-58a6ff?logo=github" alt="GitHub Wiki"/></a>
  <a href="https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/nanlabs/agent-toolkit/validate.yml?branch=main&label=validate&color=58a6ff" alt="Validate"/></a>
  <a href="https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml"><img src="https://img.shields.io/github/actions/workflow/status/nanlabs/agent-toolkit/mega-linter.yml?branch=main&label=megalinter&color=f7c948" alt="MegaLinter"/></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-7ee787" alt="Agent Skills compatible"/></a>
  <a href="https://agent-plugins.org/specification"><img src="https://img.shields.io/badge/Agent%20Plugins-v1.0.0-58a6ff" alt="Agent Plugins v1.0.0"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-ff6b35" alt="MIT license"/></a>
</p>

<p>
<!-- generated:badges -->
  <img src="https://img.shields.io/badge/skills-%2B50-ff6b35" alt="+50 skills"/>
  <img src="https://img.shields.io/badge/agents-%2B18-58a6ff" alt="+18 agents"/>
  <img src="https://img.shields.io/badge/plugins-%2B10-f7c948" alt="+10 plugins"/>
  <img src="https://img.shields.io/badge/MCP-%2B9%20official-7ee787" alt="+9 official"/>
<!-- /generated:badges -->
</p>

</div>

> [!IMPORTANT]
> **This repo is the public product** (L1.5): skills, agents, plugins, official MCP.
> **NaNLABS laptops** are provisioned by private **`nanlabs/internal-workstation`** (L1). Employees run `nan-ai-enable` after chezmoi. You do **not** need the workstation to install plugins from here.
> **How do I use this?** The [GitHub Wiki](https://github.com/nanlabs/agent-toolkit/wiki) is the shareable guide: [install plugins](https://github.com/nanlabs/agent-toolkit/wiki/Installation), [day-to-day use](https://github.com/nanlabs/agent-toolkit/wiki/Using), [add a skill](https://github.com/nanlabs/agent-toolkit/wiki/Add-a-Skill), [testing](https://github.com/nanlabs/agent-toolkit/wiki/Testing).

## Install everything

Copy the block for your client. Then reload and complete MCP OAuth when prompted.

<details open>
<summary><strong>Claude Code</strong> — marketplace add, then every group plugin</summary>

<!-- generated:claude-install -->
```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
/plugin install nanlabs-data@nanlabs-agent-toolkit
/plugin install nanlabs-delivery@nanlabs-agent-toolkit
/plugin install nanlabs-design@nanlabs-agent-toolkit
/plugin install nanlabs-forge@nanlabs-agent-toolkit
/plugin install nanlabs-integrations@nanlabs-agent-toolkit
/plugin install nanlabs-ops@nanlabs-agent-toolkit
/plugin install nanlabs-tooling@nanlabs-agent-toolkit
/plugin install nanlabs-workflow@nanlabs-agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
/nanlabs-core:setup
```
<!-- /generated:claude-install -->

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong></summary>

<!-- generated:copilot-install -->
```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-data
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-delivery
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-design
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-forge
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-integrations
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-ops
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-tooling
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-workflow
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
```
<!-- /generated:copilot-install -->

</details>

<details>
<summary><strong>Cursor IDE</strong> — local plugins (or Team Marketplace import)</summary>

<!-- generated:cursor-install -->
```bash
mkdir -p ~/.cursor/plugins/local
REPO=/path/to/agent-toolkit
ln -sfn "$REPO/plugins/nanlabs-core" ~/.cursor/plugins/local/nanlabs-core
ln -sfn "$REPO/plugins/nanlabs-data" ~/.cursor/plugins/local/nanlabs-data
ln -sfn "$REPO/plugins/nanlabs-delivery" ~/.cursor/plugins/local/nanlabs-delivery
ln -sfn "$REPO/plugins/nanlabs-design" ~/.cursor/plugins/local/nanlabs-design
ln -sfn "$REPO/plugins/nanlabs-forge" ~/.cursor/plugins/local/nanlabs-forge
ln -sfn "$REPO/plugins/nanlabs-integrations" ~/.cursor/plugins/local/nanlabs-integrations
ln -sfn "$REPO/plugins/nanlabs-ops" ~/.cursor/plugins/local/nanlabs-ops
ln -sfn "$REPO/plugins/nanlabs-tooling" ~/.cursor/plugins/local/nanlabs-tooling
ln -sfn "$REPO/plugins/nanlabs-workflow" ~/.cursor/plugins/local/nanlabs-workflow
ln -sfn "$REPO/plugins/nanlabs-agents" ~/.cursor/plugins/local/nanlabs-agents
```
<!-- /generated:cursor-install -->

Reload the window after linking.

</details>

<details>
<summary><strong>Skills-only</strong> — Agent Skills CLI, no plugins / MCP / agents</summary>

```bash
npx skills add nanlabs/agent-toolkit -g
```

Group or domain pack: [`docs/PACKS.md`](docs/PACKS.md).

</details>

<details>
<summary><strong>VS Code · Codex · Kiro · rest of the Agent Plugins roster</strong></summary>

| Client | How |
| --- | --- |
| VS Code | `"chat.plugins.marketplaces": ["nanlabs/agent-toolkit"]` then install each `nanlabs-*` |
| ChatGPT / Codex | `codex plugin marketplace add nanlabs/agent-toolkit` then install from the Plugins Directory |
| Kiro | Powers → Import from folder → `plugins/nanlabs-<group>` (not the repo root) |
| Grok / Hermes / OpenClaw / NanoClaw | Point the client at `plugins/nanlabs-<group>/` (`plugin.json` + `skills/`) |
| Cursor Agent CLI | `agent plugin marketplace add https://github.com/nanlabs/agent-toolkit` then `--plugin-dir` — [`docs/CURSOR_CLI.md`](docs/CURSOR_CLI.md) |

Full matrix: [`docs/ADOPTION.md`](docs/ADOPTION.md).

</details>

Start with **`nanlabs-core`** if you want a smaller first install. Run **`/nanlabs-core:setup`** after Claude Code install.

## Catalog

Tables below are generated from [`products/plugins.yaml`](products/plugins.yaml), [`catalogs/mcp-catalog.yaml`](catalogs/mcp-catalog.yaml), and [`catalogs/skills-layout.json`](catalogs/skills-layout.json). Do not hand-edit them — run `python3 scripts/gen-surfaces.py`. Full dump: [`docs/generated/catalog.md`](docs/generated/catalog.md).

### Plugins

<!-- generated:plugins -->
| Plugin | Version | Skills | MCP | Role |
| --- | --- | --- | --- | --- |
| `nanlabs-core` | 0.4.0 | 7 | — | Recommended first install. Setup doctor + `/nanlabs-core:setup`. |
| `nanlabs-data` | 0.1.0 | 2 | — | dbt and Snowflake validation skills |
| `nanlabs-delivery` | 0.1.0 | 19 | — | PRD, TRD, ADR, work items, assessments, and delivery process |
| `nanlabs-design` | 0.2.0 | 6 | `figma` | Figma MCP and UI/UX intelligence (not a full designer workflow) |
| `nanlabs-forge` | 0.2.0 | 4 | `github`, `gitlab` | GitHub and GitLab CLI automation plus official GitHub and GitLab MCP |
| `nanlabs-integrations` | 0.2.0 | 4 | `atlassian`, `clickup`, `linear`, `notion`, `shortcut`, `slack` | ClickUp, Slack, Linear, Shortcut, Notion, and Atlassian (Jira/Confluence) MCP plus CLI skills |
| `nanlabs-ops` | 0.1.0 | 4 | — | Workstation triage, presentations ops, and skill contribution |
| `nanlabs-tooling` | 0.1.0 | 2 | — | Playwright CLI and Jupyter notebook scaffolding |
| `nanlabs-workflow` | 0.1.0 | 2 | — | Client delivery workflows and bootstrap |
| `nanlabs-agents` | 0.2.1 | — | — | Optional. Full agent roster. |
<!-- /generated:plugins -->

### Official MCP

Authenticate in the client. No tokens in the plugin. Slack may need workspace admin approval.

<!-- generated:mcp -->
| Server | Plugin | Official URL | Notes |
| --- | --- | --- | --- |
| `atlassian` | `nanlabs-integrations` | `https://mcp.atlassian.com/v2/mcp` | Covers Jira, Confluence, Jira Service Management, Bitbucket, Loom. Official Atlassian Rovo MCP v2. One server covers Jira and Confluence. |
| `clickup` | `nanlabs-integrations` | `https://mcp.clickup.com/mcp` | Official ClickUp hosted MCP. OAuth only; API tokens are not supported. |
| `figma` | `nanlabs-design` | `https://mcp.figma.com/mcp` | Official Figma remote MCP. OAuth. Figma allowlists MCP clients. |
| `github` | `nanlabs-forge` | `https://api.githubcopilot.com/mcp/` | Official GitHub hosted MCP. OAuth in VS Code / Copilot; some Cursor setups still prompt for a PAT in user MCP config, not in this plugin. |
| `gitlab` | `nanlabs-forge` | `https://gitlab.com/api/v4/mcp` | Official GitLab.com MCP. Self-managed instances use `https://<host>/api/v4/mcp` in user config instead. |
| `linear` | `nanlabs-integrations` | `https://mcp.linear.app/mcp` | Official Linear hosted MCP. OAuth 2.1. SSE at /sse is deprecated. |
| `notion` | `nanlabs-integrations` | `https://mcp.notion.com/mcp` | Official Notion hosted MCP. OAuth. Open-source notion-mcp-server is unmaintained. |
| `shortcut` | `nanlabs-integrations` | `https://mcp.shortcut.com/mcp` | Official Shortcut hosted MCP. OAuth; no API token. |
| `slack` | `nanlabs-integrations` | `https://mcp.slack.com/mcp` | Official Slack hosted MCP. OAuth. Slack does not support Dynamic Client Registration; workspace admin approval is required. Slack's own client plugins may still be needed for client-id-bound OAuth. |
<!-- /generated:mcp -->

## How it fits

<div align="center">
  <img alt="L1 workstation and L1.5 agent-toolkit layers" src="static/architecture.svg" width="1080">
</div>

| Layer | Repo | Owns |
| --- | --- | --- |
| L1 | `nanlabs/internal-workstation` (private) | Machine, secrets, chezmoi |
| L1.5 | **this repository** (public) | Skills, agents, plugins, MCP |

## Docs

Start at the **[GitHub Wiki](https://github.com/nanlabs/agent-toolkit/wiki)** (synced from `docs/wiki/`). Long-form repo docs stay under `docs/`.

| Need | Go to |
| --- | --- |
| Install plugins | [Wiki: Installation](https://github.com/nanlabs/agent-toolkit/wiki/Installation) |
| Use skills and MCP | [Wiki: Using](https://github.com/nanlabs/agent-toolkit/wiki/Using) · [Official MCP](https://github.com/nanlabs/agent-toolkit/wiki/MCP-Setup) |
| Add a skill / open a PR | [Wiki: Add a skill](https://github.com/nanlabs/agent-toolkit/wiki/Add-a-Skill) · [Wiki: Contributing](https://github.com/nanlabs/agent-toolkit/wiki/Contributing) |
| Run the same checks as CI | [Wiki: Testing](https://github.com/nanlabs/agent-toolkit/wiki/Testing) |
| Plugin / MCP / skill tables | [Wiki: Plugin marketplace](https://github.com/nanlabs/agent-toolkit/wiki/Plugin-Marketplace) · [Generated catalog](docs/generated/catalog.md) |
| Install matrix by client | [Adoption](docs/ADOPTION.md) |
| In / out of scope | [Wiki: Scope](https://github.com/nanlabs/agent-toolkit/wiki/Scope) · [SCOPE.md](docs/SCOPE.md) |
| Common questions | [Wiki: FAQ](https://github.com/nanlabs/agent-toolkit/wiki/FAQ) |
| Packs | [PACKS](docs/PACKS.md) |
| Release / pin / rollback | [Wiki: Lifecycle](https://github.com/nanlabs/agent-toolkit/wiki/Lifecycle) · [RELEASE](docs/RELEASE.md) |

## Quality bar

```bash
python3 scripts/gen-surfaces.py --check
python3 scripts/validate-manifests.py
python3 scripts/validate-mcp.py
python3 scripts/validate-skill-inventory.py
pre-commit run --all-files
```

CI on `main`: Validate, MegaLinter, wiki sync. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE) · [`SECURITY.md`](SECURITY.md) · [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

<sub>Brand: [NaNLABS Octonan](https://github.com/nanlabs/.github/blob/main/profile/octonan.png) from public `nanlabs/.github`. README artwork: [`static/`](static/README.md).</sub>
