> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.
> If a ClickUp mirror is created later, update this banner with the link.

---

# Skills index

Canonical skills live under `plugins/nanlabs-<group>/skills/<skill>/` and follow the
[Agent Skills](https://agentskills.io/specification) format (`SKILL.md`).

Install: [`npx skills`](https://github.com/vercel-labs/skills) — `npx skills add nanlabs/agent-toolkit -g`  
Group plugin or domain pack: [`PACKS.md`](PACKS.md) (plugin skills dir or `--skill` filter)  
Catalog: [`catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml)  
Authoring: [`AUTHORING.md`](AUTHORING.md)

Each group plugin **is** the portable [Agent Plugins](https://agent-plugins.org/specification) package
(`plugin.json` + immediate `skills/<name>/`). See [`AGENT_PLUGINS.md`](AGENT_PLUGINS.md).

## Bundled groups

| Group | Path |
| --- | --- |
| core | `plugins/nanlabs-core/skills/` |
| delivery | `plugins/nanlabs-delivery/skills/` |
| workflow | `plugins/nanlabs-workflow/skills/` |
| forge | `plugins/nanlabs-forge/skills/` |
| integrations | `plugins/nanlabs-integrations/skills/` |
| design | `plugins/nanlabs-design/skills/` |
| data | `plugins/nanlabs-data/skills/` |
| ops | `plugins/nanlabs-ops/skills/` (includes `nanlabs-propose-skill`) |
| tooling | `plugins/nanlabs-tooling/skills/` |

## Opt-in / not bundled here

These appear in skill docs as related capabilities but are **not** shipped in
this repository (yet). Install or provision them separately when needed.

| Name | Kind | Notes |
| --- | --- | --- |
| `figma-use` | opt-in pack | Figma Plugin API / canvas writes |
| `figma-generate-design` | opt-in pack | Full-screen generation in Figma; needs `figma-use` |
| `figma-generate-library` | opt-in pack | Library generate/import |
| `nanlabs-e2e-runner` | agent | Playwright **test** authoring (agents wave) |
| `jira-assistant` / `confluence-assistant` | external packs | Not part of this public tree |

When a skill mentions one of the above, treat the name as a pointer — do not
expect a sibling `../<name>/SKILL.md` in this repo.
