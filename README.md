<div align="center">

# agent-toolkit

**NaNLABS skills, agents, and plugins — L1.5 distribution**

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/nanlabs/.github/blob/main/profile/octonan.png?raw=true"/>
  <img alt="NaNLABS Octonan mascot" align="left" width="150" src="https://github.com/nanlabs/.github/blob/main/profile/octonan.png?raw=true"/>
</picture>

**Production surfaces:** Agent Plugins roster + Claude Code

<sub>Brand asset: [NaNLABS Octonan](https://github.com/nanlabs/.github/blob/main/profile/octonan.png), from the public `nanlabs/.github` repository.</sub>

[Docs](docs/README.md) · [Wiki source](docs/wiki/Home.md) · [Adoption](docs/ADOPTION.md) · [Scope](docs/SCOPE.md) · [Contributing](CONTRIBUTING.md)

<br clear="left">

<div align="center">

<p>
  <a href="https://github.com/nanlabs/agent-toolkit/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/nanlabs/agent-toolkit/validate.yml?branch=main&label=validate&color=58a6ff" alt="Validate"/></a>
  <a href="https://github.com/nanlabs/agent-toolkit/actions/workflows/mega-linter.yml"><img src="https://img.shields.io/github/actions/workflow/status/nanlabs/agent-toolkit/mega-linter.yml?branch=main&label=megalinter&color=f7c948" alt="MegaLinter"/></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-7ee787" alt="Agent Skills compatible"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-ff6b35" alt="MIT license"/></a>
</p>

<p>
  <img src="https://img.shields.io/badge/skills-49-ff6b35" alt="49 skills"/>
  <img src="https://img.shields.io/badge/agents-18-58a6ff" alt="18 agents"/>
  <img src="https://img.shields.io/badge/plugins-10-f7c948" alt="10 plugins"/>
  <img src="https://img.shields.io/badge/MCP-official%20remote-7ee787" alt="Official remote MCP"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude-equal-ff6b35" alt="Claude"/>
  <img src="https://img.shields.io/badge/Claude%20Code-equal-f7c948" alt="Claude Code"/>
  <img src="https://img.shields.io/badge/Cursor%20IDE-equal-58a6ff" alt="Cursor IDE"/>
  <img src="https://img.shields.io/badge/Cursor%20Agent%20CLI-equal-7ee787" alt="Cursor Agent CLI"/>
  <img src="https://img.shields.io/badge/GitHub%20Copilot-equal-8b949e" alt="GitHub Copilot"/>
</p>

</div>

> [!IMPORTANT]
> **L1.5 distribution (public)** — This repository ships NaNLABS skills, agents, and plugins for the [Agent Plugins](https://agent-plugins.org/compatible-clients) roster and Claude Code.
>
> **Machine provisioning (L1)** lives in **`nanlabs/internal-workstation`** — a **private** NaNLABS repository (org access required). Employees install the workstation via chezmoi, then run **`nan-ai-enable`** to pin this repo. See [Workstation cutover](docs/ADOPTION.md#workstation-cutover-internal-workstation) in Adoption.

---

## What is agent-toolkit?

Public **L1.5** distribution of NaNLABS AI capabilities: Agent Skills, agent personas, one plugin per skill group, and GitHub Copilot surfaces. Machine provisioning stays in **`nanlabs/internal-workstation`** (L1, **private**).

Smaller than multi-tool personal forks: **no** consumer CLI, loop runtime, or OpenCode/Windsurf/Gemini/Pi plugin targets. Portable skills may still work via `npx skills`.

<div align="center">
  <img alt="L1 and L1.5 architecture" src="static/architecture.svg" width="820">
</div>

## Highlights

- **Equal-priority surfaces** — Agent Plugins roster (VS Code, Copilot, Cursor, ChatGPT/Codex, Kiro, Grok Bot, Hermes, OpenClaw, NanoClaw) plus Claude Code
- **Group plugins** — one package per skill group (`plugins/nanlabs-delivery`, …); no duplicated skill trees
- **Recommended plugin** — `nanlabs-core` with bundled setup (`/nanlabs-core:setup`)
- **Optional roster** — `nanlabs-agents` for all 18 personas
- **Python typing** — `nanlabs-pyrightination` ships in `nanlabs-core`
- **Official MCP** — group plugins ship hosted OAuth MCP (`mcp.json`); authenticate in the client
- **CI quality bar** — inventory, manifests, skills-ref, Claude validate, MegaLinter, Danger

## Quick install

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Then run **`/nanlabs-core:setup`**. Repeat `/plugin install <id>@nanlabs-agent-toolkit` for the other group plugins. Optional: `/plugin install nanlabs-agents@nanlabs-agent-toolkit`.

<details>
<summary><strong>Cursor IDE</strong></summary>

- **Local:** copy or symlink `plugins/nanlabs-core` under `~/.cursor/plugins/local/`, then reload the window ([Cursor plugins](https://cursor.com/docs/plugins))
- **Team:** an org admin imports this repository as a Team Marketplace

Install **each** `nanlabs-*` group plugin (recommended start: **`nanlabs-core`**), optionally **`nanlabs-agents`**.

</details>

<details>
<summary><strong>Cursor Agent CLI</strong> — equal priority; see certification matrix</summary>

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
```

`marketplace add` registers the catalog; it does not install a plugin. For the
documented local load path, use `--plugin-dir` (see [`docs/CURSOR_CLI.md`](docs/CURSOR_CLI.md)).

</details>

<details>
<summary><strong>Skills-only</strong> — Agent Skills CLI (skills alone)</summary>

```bash
npx skills add nanlabs/agent-toolkit -g
```

Uses the [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI to
install the canonical Agent Skills tree. It does **not** install plugins,
agents, MCP, or setup automation.

Install a **group pack** (subdirectory) or a **domain pack** (skill filter):

```bash
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills
npx skills add nanlabs/agent-toolkit --skill github-cli-workflow --skill gh-address-comments
```

Pack catalog: [`catalogs/pack-catalog.yaml`](catalogs/pack-catalog.yaml) ·
[`docs/PACKS.md`](docs/PACKS.md). Helper: `bash scripts/install-pack.sh delivery`.
Group packs are the same directories as [Agent Plugins](https://agent-plugins.org/specification)
packages (closed `plugin.json`, immediate `skills/<name>/`).

</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

- **CLI plugin surface:** install a plugin from this repository or a checkout:

  ```bash
  copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
  copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-delivery
  # …repeat per group plugin
  copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
  ```

- **Repository customization surface:** `.github/copilot-instructions.md`, `.github/agents/`
- **VS Code Copilot agents:** `plugins/<id>/com.github.copilot/agents/`
- **Bundled typecheck skill:** `nanlabs-pyrightination` in `nanlabs-core`

</details>

Full paths: [`docs/ADOPTION.md`](docs/ADOPTION.md) · lifecycle: [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md)

## What's included

| Area | Notes |
| --- | --- |
| Skills | 49 under `plugins/nanlabs-<group>/skills/` — [catalog](catalogs/skill-catalog.yaml) · [packs](docs/PACKS.md) · [index](docs/SKILLS.md) |
| Group plugins | nine `nanlabs-*` packages (`nanlabs-core` v0.4.0 includes setup doctor + `/nanlabs-core:setup`) |
| Agents plugin | `nanlabs-agents` v0.2.1 (optional) — 18 personas via `gen-surfaces` |
| Copilot | Agent Plugins manifests + `.github/` instructions/agents + `com.github.copilot/agents/` |
| MCP | Official remote servers in `nanlabs-design` / `nanlabs-forge` / `nanlabs-integrations` |

## Repository layout

| Path | Purpose |
| --- | --- |
| `plugins/nanlabs-<group>/skills/<skill>/` | Canonical [Agent Skills](https://agentskills.io/specification) + [Agent Plugins](https://agent-plugins.org/specification) tree |
| `plugins/` | One package per group + optional `nanlabs-agents` |
| `.claude-plugin/` · `.cursor-plugin/` · `.agents/plugins/` | Marketplace catalogs |
| `.github/copilot-instructions.md` · `.github/agents/` | GitHub Copilot repository customization |
| `agents/` | Canonical personas |
| `products/plugins.yaml` | Plugin version + assembly SoT |
| `mcp/templates/` | Official MCP URL docs (same URLs shipped in plugin `mcp.json`) |
| `docs/` · `docs/wiki/` | Repo docs + GitHub Wiki source |
| `static/` | README artwork |
| `scripts/` | Validation + `gen-surfaces` |

## Start here

| Need | Go to |
| --- | --- |
| Install by surface | [Adoption](docs/ADOPTION.md) |
| In / out of scope | [Scope](docs/SCOPE.md) |
| Common questions | [FAQ](docs/FAQ.md) |
| Cursor Agent CLI matrix | [CURSOR_CLI](docs/CURSOR_CLI.md) |
| Docs map | [docs/README.md](docs/README.md) |
| Add a skill / plugin | [Authoring](docs/AUTHORING.md) |
| Install a domain pack | [Packs](docs/PACKS.md) |
| Propose a skill | [Contribution](docs/CONTRIBUTION.md) |
| Public safety | [Public content policy](docs/PUBLIC_CONTENT_POLICY.md) |

## Quality bar

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-agent-plugins.py
python3 scripts/validate-skill-inventory.py
python3 scripts/validate-public-content.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/validate-pack-catalog.py
python3 scripts/validate-mcp.py
python3 scripts/validate-contracts.py
python3 scripts/gen-surfaces.py --check
python3 scripts/gen-copilot-surfaces.py --check
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md). Use the PR template; link an issue (`Fixes #N` / `Refs #N`).

Wiki pages are edited under [`docs/wiki/`](docs/wiki/) and synced to the GitHub Wiki on `main`.

## Security

[`SECURITY.md`](SECURITY.md) · [`docs/PUBLIC_CONTENT_POLICY.md`](docs/PUBLIC_CONTENT_POLICY.md)

## License

[MIT](LICENSE)
