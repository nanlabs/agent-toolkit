<div align="center">

<img alt="NaNLABS agent-toolkit" src="https://raw.githubusercontent.com/nanlabs/agent-toolkit/main/static/hero-banner.svg" width="900">

# NaNLABS agent-toolkit wiki

Public skills, agents, plugins, and official MCP for Claude Code, Cursor, Copilot, and the [Agent Plugins](https://agent-plugins.org/compatible-clients) roster.

[![Wiki](https://img.shields.io/badge/share_this-wiki-58a6ff?style=for-the-badge&logo=github)](https://github.com/nanlabs/agent-toolkit/wiki)
[![Install](https://img.shields.io/badge/start-install_plugins-ff6b35?style=for-the-badge)](Installation)
[![Contribute](https://img.shields.io/badge/next-add_a_skill-f7c948?style=for-the-badge)](Add-a-Skill)

</div>

> [!TIP]
> When someone asks how to install this, connect ClickUp, or propose a skill, send them **this wiki**: [github.com/nanlabs/agent-toolkit/wiki](https://github.com/nanlabs/agent-toolkit/wiki).

<img alt="Install, use, then contribute" src="https://raw.githubusercontent.com/nanlabs/agent-toolkit/main/static/wiki-journey.svg" width="900">

## Pick a path

| I want to… | Page |
| --- | --- |
| Install plugins in my AI client | [Installation](Installation) |
| Know which plugin to install | [Using the toolkit](Using) |
| Connect ClickUp, GitHub, Figma, Linear… | [Official MCP](MCP-Setup) |
| See every plugin and copy-paste install | [Plugin marketplace](Plugin-Marketplace) |
| Propose or author a new skill | [Add a skill](Add-a-Skill) |
| Run the same checks as CI | [Testing](Testing) |
| Open a pull request | [Contributing](Contributing) |

```mermaid
flowchart LR
  A[Pick your client] --> B[Install plugins]
  B --> C[Reload and OAuth]
  C --> D[Use skills and MCP]
  D --> E[Optional: propose a skill]
```

## Two audiences

### You use the toolkit

You want skills and MCP in Claude Code, Cursor, Copilot, or another Agent Plugins client. You do **not** need to clone this repo.

1. [Installation](Installation) — marketplace or local plugins
2. [Using the toolkit](Using) — setup doctor, verify, pick a group
3. [Official MCP](MCP-Setup) — authenticate in the client (no tokens in the plugin)
4. [FAQ](FAQ) — common snags

NaNLABS laptops are provisioned separately by private `internal-workstation`. You can still install this public repo without that machine baseline.

### You want to contribute

You want to add a skill, fix docs, or change a plugin.

1. [Add a skill](Add-a-Skill) — issue template, layout, review bar
2. [Testing](Testing) — validators that match CI
3. [Contributing](Contributing) — branch, PR template, public-safety rules

Canonical long-form stays in the [docs/ tree](https://github.com/nanlabs/agent-toolkit/tree/main/docs). This wiki is the shareable map.

## What you get

| Piece | What it is |
| --- | --- |
| **Group plugins** | One plugin per skill group (`nanlabs-core`, `nanlabs-delivery`, …) |
| **Skills** | Agent Skills (`SKILL.md`) inside each plugin |
| **Agents** | Personas; core ships a reviewer, `nanlabs-agents` ships the full roster |
| **Official MCP** | Hosted OAuth servers on design / forge / integrations plugins |

Catalog tables are generated from YAML so they cannot drift. See [Plugin marketplace](Plugin-Marketplace) and [Skills](Skills-Reference).

## License

[MIT](https://github.com/nanlabs/agent-toolkit/blob/main/LICENSE)
