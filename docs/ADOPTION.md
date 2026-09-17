> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.
> If a ClickUp mirror is created later, update this banner with the link.

---

# Adoption

How to install and use `nanlabs/agent-toolkit`.

Also see [SCOPE.md](SCOPE.md), [FAQ.md](FAQ.md), and the [wiki source](wiki/) (companion PR: wiki sync).

**Production:** [Agent Plugins](https://agent-plugins.org/compatible-clients) roster (9 clients) **plus** Claude Code (native marketplace; not on that roster). Group plugins ship official hosted MCP in `mcp.json` (Agent Plugins / Cursor) and `.mcp.json` (Claude Code). Authenticate in the client — no tokens in the plugin. Cursor Agent CLI certification evidence lives in [`CURSOR_CLI.md`](CURSOR_CLI.md) — evidence gap ≠ lower product priority.

There is **no** root `plugin.json`. Each package is `plugins/nanlabs-<group>/` (plus optional `nanlabs-agents`). Canonical skills live there under `skills/<name>/`.

**Complete install** = the nine group plugins, then optionally `nanlabs-agents`:

`nanlabs-core` · `nanlabs-data` · `nanlabs-delivery` · `nanlabs-design` · `nanlabs-forge` · `nanlabs-integrations` · `nanlabs-ops` · `nanlabs-tooling` · `nanlabs-workflow`

Repeat the install command per plugin id. Domain packs (`code-review`, `qa`, …) are `npx skills` aliases, not extra plugin packages.

Roster snapshot (compatible-clients page is JS-only; last checked 2026-09-17 against the 2026-08-13 listing): VS Code, GitHub Copilot, Cursor, ChatGPT & Codex (one entry), Kiro, Grok Bot, Hermes Agent, OpenClaw, NanoClaw. **Not on the roster:** Claude Code (still supported here), Gemini / Antigravity / OpenCode.

## VS Code

Enable plugins, add this repo as a marketplace, then install each `nanlabs-*` from **@agentPlugins**:

```json
{
  "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": ["nanlabs/agent-toolkit"]
}
```

Alternative: **Chat: Install Plugin From Source** → git URL or folder `plugins/nanlabs-delivery` (repeat per group). Copilot agents for VS Code live under each plugin’s `com.github.copilot/agents/`.

## GitHub Copilot (VS Code, CLI, app)

```bash
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-delivery
# …repeat for data, design, forge, integrations, ops, tooling, workflow
copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents   # optional
```

CLI installs land in `~/.copilot/installed-plugins/` and then show up in VS Code. Agents are not a portable Agent Plugins component; Copilot reads `agents/*.agent.md` and `com.github.copilot/agents/`.

## Cursor IDE and Cursor Agent CLI

**IDE:** Team Marketplace import of `nanlabs/agent-toolkit`, or copy/symlink each `plugins/nanlabs-*` under `~/.cursor/plugins/local/` and reload. Marketplace entries use only `name`, `source`, `description` (official schema). Shipped MCP servers are remote HTTPS URLs (no `${PLUGIN_ROOT}`). Cursor does **not** expand `${PLUGIN_ROOT}` / `${PLUGIN_DATA}` if a future stdio server is added.

**CLI:**

```bash
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

`marketplace add` registers the catalog; it does not install a plugin. Repeat `--plugin-dir` per group (or install interactively). See [`CURSOR_CLI.md`](CURSOR_CLI.md).

## ChatGPT and Codex

Codex 0.147+ reads `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`. ChatGPT desktop also documents `$REPO_ROOT/.agents/plugins/marketplace.json` (`source.path` is `./plugins/nanlabs-…`).

```bash
codex plugin marketplace add nanlabs/agent-toolkit
```

Install each plugin from the Plugins Directory (install TUI, not headless).

## Kiro

Powers → Import from folder → `plugins/nanlabs-<group>`. `keywords` in `plugin.json` activate the power. Do **not** import the GitHub repository root.

## Grok Bot, Hermes Agent, OpenClaw, NanoClaw

Point the client at the plugin directory (`plugin.json` + `skills/<name>/SKILL.md`). There is no separate NaNLABS marketplace for these clients.

## Claude Code (native, not on the Agent Plugins roster)

The portable `plugin.json` alone does not load Claude Code. Use the dual-rail `.claude-plugin/` marketplace:

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Repeat `/plugin install <id>@nanlabs-agent-toolkit` for each group plugin. Invoke setup with **`/nanlabs-core:setup`**, or ask Claude to run the bundled `nanlabs-setup` skill.

Optional full agent roster:

```text
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

> **Deprecated:** `nanlabs-setup` as a separate plugin is no longer in the marketplace. Setup ships inside `nanlabs-core` (v0.3.0+).

Lifecycle (update / pin / rollback): [`LIFECYCLE.md`](LIFECYCLE.md).

## Skills-only (`npx skills`)

```bash
npx skills add nanlabs/agent-toolkit -g
```

This uses the [`vercel-labs/skills`](https://github.com/vercel-labs/skills)
CLI. It recurses to depth ≤ 5 and finds `SKILL.md` under
`plugins/nanlabs-<group>/skills/<name>/` (49 skills).

Install one group or a named domain pack instead of the whole tree:

```bash
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills
npx skills add nanlabs/agent-toolkit --skill github-cli-workflow --skill gh-address-comments
bash scripts/install-pack.sh code-review -y
```

Skills-only installs do **not** bundle the contract doctor; use baseline spot-checks in the skill or clone the repo for full validation.

Skill index: [`SKILLS.md`](SKILLS.md) · packs: [`PACKS.md`](PACKS.md) · machine catalogs: [`../catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml), [`../catalogs/pack-catalog.yaml`](../catalogs/pack-catalog.yaml). Domain packs stay `npx` aliases; group packs match the Agent Plugins directories.

## Agents and MCP

- Agents: [`../agents/README.md`](../agents/README.md) (18 personas; plugin `nanlabs-agents`)
- MCP: [`../mcp/templates/README.md`](../mcp/templates/README.md) and [`../catalogs/mcp-catalog.yaml`](../catalogs/mcp-catalog.yaml) — official URLs shipped by `nanlabs-design`, `nanlabs-forge`, `nanlabs-integrations`
- Dependency contracts: [`../contracts/README.md`](../contracts/README.md)
- Domain packs: [`PACKS.md`](PACKS.md). Remaining outcome-pack **content** is tracked in GitHub issues `#24`, `#25`, and `#28` (no placeholder directories)
- Overlay governance: [`OVERLAY_GOVERNANCE.md`](OVERLAY_GOVERNANCE.md)
- Telemetry ownership: [`TELEMETRY_CONTRACT.md`](TELEMETRY_CONTRACT.md)

## Workstation cutover (`internal-workstation`)

> [!IMPORTANT]
> **L1 ↔ L1.5** — **`nanlabs/internal-workstation`** is **private** (NaNLABS org access). It provisions chezmoi and `nan-*` CLI only — **no bundled skills, MCP, or agents**. All AI assets live **here** (public `nanlabs/agent-toolkit`).

As of Wave 3+ single-source cutover, **`nanlabs/internal-workstation` bundles zero AI assets**. NaNLABS machines use:

- **`nan-ai-enable`** — pins `NAN_AGENT_TOOLKIT_VERSION`, runs `npx skills add`, syncs MCP templates to `~/.local/share/nanlabs/mcp/`
- **Claude/Cursor plugins** — same flows documented above

Install guide (private repo — clone with org access): `docs/AGENT_TOOLKIT.md` in **internal-workstation**.

## What success looks like

- Marketplace add succeeds without private-repo auth for this public repository.
- `nanlabs-core` is installed; `/nanlabs-core:setup` runs the bundled doctor without a git checkout.
- Cursor IDE and Cursor Agent CLI each have recorded install + smoke evidence (CLI matrix in [`CURSOR_CLI.md`](CURSOR_CLI.md)).
- `npx skills` discovers nested skills under `plugins/nanlabs-<group>/skills/`.
- No secrets were required to install the plugin or skills themselves.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Setup can’t find doctor scripts | Use marketplace `nanlabs-core` ≥ 0.3.0 (bundles doctor); avoid relying on a git checkout |
| Cursor marketplace import fails | Ensure `.cursor-plugin/marketplace.json` passes official schema |
| Expected MCP tools missing | Install `nanlabs-design` / `nanlabs-forge` / `nanlabs-integrations` and complete OAuth in the client |
| CLI skills/commands missing | Re-check [`CURSOR_CLI.md`](CURSOR_CLI.md) on the pinned CLI version — IDE ≠ CLI |

## Related docs

- [`P0_FINDINGS.md`](P0_FINDINGS.md) — feasibility + lifecycle matrix
- [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md) — what may be published
- [`AUTHORING.md`](AUTHORING.md) — how to add skills/plugins
- [`PACKS.md`](PACKS.md) — group and domain pack install
- [`CONTRIBUTION.md`](CONTRIBUTION.md) — propose a skill via PR
- [`../AGENTS.md`](../AGENTS.md) — contributor contract for this repo
