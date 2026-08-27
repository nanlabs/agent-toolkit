> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-27**
>
> This document lives only in the repo. It is public-ready and self-contained.
> If a ClickUp mirror is created later, update this banner with the link.

---

# Adoption

How to install and use `nanlabs/agent-toolkit`.

Also see [SCOPE.md](SCOPE.md), [FAQ.md](FAQ.md), and the [wiki source](wiki/) (companion PR: wiki sync).

**Production surfaces:** Claude · Claude Code · Cursor IDE · Cursor Agent CLI · GitHub Copilot.  
**Skills-only** installs skills alone (needed on some Claude surfaces and any Agent Skills client). Cursor Agent CLI certification evidence lives in [`CURSOR_CLI.md`](CURSOR_CLI.md) — evidence gap ≠ lower product priority.

## Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Invoke setup via the **namespaced** plugin command: **`/nanlabs-core:setup`**, or ask Claude to run the bundled `nanlabs-setup` skill.

Optional full agent roster:

```text
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

> **Deprecated:** `nanlabs-setup` as a separate plugin is no longer in the marketplace. Setup ships inside `nanlabs-core` (v0.3.0+).

Lifecycle (update / pin / rollback): [`LIFECYCLE.md`](LIFECYCLE.md).

## Cursor IDE

1. **Local development:** place or symlink a plugin under `~/.cursor/plugins/local/` and reload the window.
2. **Team:** import this repository as a Team Marketplace (org admin; Teams or Enterprise).

Install **`nanlabs-core`** (recommended). Optionally install **`nanlabs-agents`**.

Marketplace entries use only `name`, `source`, `description`, and optional `minClientVersions` per the official Cursor schema.

See [Cursor plugins](https://cursor.com/docs/plugins).

## Cursor Agent CLI

Same product priority as Cursor IDE. Do not assume IDE plugin components load identically in the CLI.

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
```

`marketplace add` registers the repository catalog; it does not install
`nanlabs-core`. The recorded CLI evidence uses the local load path:

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

The evidence snapshot did not expose a non-interactive plugin-install command.
Use `--plugin-dir` for CLI smoke tests, or install interactively through
Cursor's plugin dashboard / Cursor IDE Team Marketplace. Fill the
component matrix in [`CURSOR_CLI.md`](CURSOR_CLI.md) with pass/fail/partial
evidence; unknown cells are **uncertified**, not deprioritized.

## GitHub Copilot

Two supported surfaces:

1. **CLI plugin surface** — Agent Plugins v1.0.0 portable root-level `plugin.json` in:
   - `plugins/nanlabs-core/`
   - `plugins/nanlabs-agents/`
   Copilot consumes these manifests additively in Open Plugin Spec mode, with
   `agents/` and `skills/` as the default component paths.

   Install directly from GitHub, or use the equivalent path in a checkout:

   ```bash
   copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
   # optional full agent roster:
   copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
   ```

2. **Repository customization** — committed under:
   - `.github/copilot-instructions.md`
   - `.github/agents/*.agent.md`
   - `.github/skills/*/SKILL.md`

The recommended baseline remains **`nanlabs-core`**. It includes the
report-only `nanlabs-pyrightination` skill for Python type-checking guidance.

Current honesty rules:

- Hooks are **not** shipped for Copilot yet.
- MCP remains configured separately; the repo does not claim bundled Copilot MCP support.
- Repository customization is repo-scoped, not a global machine install.

## Skills-only

```bash
npx skills add nanlabs/agent-toolkit -g
```

This uses the [`vercel-labs/skills`](https://github.com/vercel-labs/skills)
CLI to install the grouped tree `skills/<group>/<skill>/` (48 skills,
including `nanlabs-setup` and `nanlabs-pyrightination`).

Skills-only installs do **not** bundle the contract doctor; use baseline spot-checks in the skill or clone the repo for full validation.

Skill index: [`SKILLS.md`](SKILLS.md) · machine catalog: [`../catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml).

## Agents and MCP

- Agents: [`../agents/README.md`](../agents/README.md) (18 personas; plugin `nanlabs-agents`)
- MCP stubs: [`../mcp/templates/README.md`](../mcp/templates/README.md) (docs-only; no MCP server is shipped)
- Dependency contracts: [`../contracts/README.md`](../contracts/README.md)
- Future outcome packs are tracked in GitHub issues `#24`, `#25`, and `#28` rather than placeholder directories in this repo
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
- `npx skills` discovers nested skills under `skills/<group>/`.
- No secrets were required to install the plugin or skills themselves.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Setup can’t find doctor scripts | Use marketplace `nanlabs-core` ≥ 0.3.0 (bundles doctor); avoid relying on a git checkout |
| Cursor marketplace import fails | Ensure `.cursor-plugin/marketplace.json` passes official schema |
| Expected MCP tools missing | MCP templates are docs-only; configure MCP separately |
| CLI skills/commands missing | Re-check [`CURSOR_CLI.md`](CURSOR_CLI.md) on the pinned CLI version — IDE ≠ CLI |

## Related docs

- [`P0_FINDINGS.md`](P0_FINDINGS.md) — feasibility + lifecycle matrix
- [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md) — what may be published
- [`AUTHORING.md`](AUTHORING.md) — how to add skills/plugins
- [`../AGENTS.md`](../AGENTS.md) — contributor contract for this repo
