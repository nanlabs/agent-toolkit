# 📦 Installation

Production surfaces: **Claude · Claude Code · Cursor IDE · Cursor Agent CLI · GitHub Copilot**.

Canonical long-form: [`docs/ADOPTION.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/ADOPTION.md) · lifecycle: [`docs/LIFECYCLE.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/LIFECYCLE.md).

## Prerequisites

- **git** (clone / marketplace fetch)
- At least one target client (Claude Code, Cursor IDE, and/or Cursor Agent CLI)
- For skills-only: **Node.js** + `npx`
- For local validation (maintainers): **Python 3.10+**

## Claude Code (plugin marketplace)

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
```

Run setup:

```text
/nanlabs-core:setup
```

Optional full agent roster:

```text
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

> `nanlabs-setup` as a **separate** marketplace plugin is deprecated. Setup ships inside `nanlabs-core` (v0.3.0+).

## Cursor IDE

1. **Local:** symlink or copy `plugins/nanlabs-core` under `~/.cursor/plugins/local/` and reload.
2. **Team:** org admin imports `nanlabs/agent-toolkit` as a Team Marketplace, then install `nanlabs-core`.

See [Cursor plugins](https://cursor.com/docs/plugins).

## Cursor Agent CLI

Same product priority as Cursor IDE. Do not assume IDE behavior.

```bash
agent --version
agent plugin marketplace add https://github.com/nanlabs/agent-toolkit
```

`marketplace add` registers the catalog; it does not install a plugin. Use
`--plugin-dir` for the documented local load and smoke path:

```bash
agent --plugin-dir /path/to/agent-toolkit/plugins/nanlabs-core \
  -p --mode ask --output-format text \
  "List skills and slash commands from the loaded plugin"
```

The repository snapshot does not certify a non-interactive CLI marketplace
install. Use Cursor's interactive plugin dashboard or Team Marketplace for
marketplace installation.

Parity matrix: [Cursor Agent CLI](Cursor-Agent-CLI) · repo [`docs/CURSOR_CLI.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/CURSOR_CLI.md).

## GitHub Copilot

**Prerequisite:** [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) installed and authenticated.

Two supported surfaces:

1. **CLI plugin surface** — Agent Plugins v1.0.0 portable manifests generated in:
   - `plugins/nanlabs-core/plugin.json`
   - `plugins/nanlabs-agents/plugin.json`
   Copilot uses `agents/` and `skills/` as the default component paths in
   additive Open Plugin Spec mode.

   Install directly from GitHub, or use the equivalent path in a checkout:

   ```bash
   copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-core
   # optional full agent roster:
   copilot plugin install nanlabs/agent-toolkit:plugins/nanlabs-agents
   ```

   The `OWNER/REPO:PATH` form is documented in the
   [Copilot CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

2. **Repository customization** — committed in:
   - `.github/copilot-instructions.md`
   - `.github/agents/*.agent.md`
   - `.github/skills/*/SKILL.md`

The recommended baseline remains `nanlabs-core`, which also bundles the
report-only `nanlabs-pyrightination` skill for Python type-check reporting.

Honesty rules:

- Hooks are not bundled for Copilot yet.
- MCP is still configured separately.
- Repository customization is repo-scoped, not a machine-global install.

## Skills-only (Agent Skills CLI)

```bash
npx skills add nanlabs/agent-toolkit -g
```

Uses the [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI to
install `skills/<group>/<skill>/` only. Does **not** install plugins, agents,
MCP, or `/nanlabs-core:setup`.

## Verify

| Path | Check |
| --- | --- |
| Claude Code | Ask “what NaNLABS skills are available?” after installing `nanlabs-core` |
| Cursor IDE | Skills / commands discoverable after local or team install |
| Cursor Agent CLI | Inventory via `--plugin-dir` print mode (see matrix) |
| Skills-only | `npx skills check` lists nested skills |

## Update / uninstall

See [Lifecycle](Lifecycle).
