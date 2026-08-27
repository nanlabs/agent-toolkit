> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-08-27**
>
> This document lives only in the repo. It is public-ready and self-contained.
> If a ClickUp mirror is created later, update this banner with the link.

---

# Skills index

Canonical skills live under `skills/<group>/<skill>/` and follow the
[Agent Skills](https://agentskills.io/specification) format (`SKILL.md`).

Install: [`npx skills`](https://github.com/vercel-labs/skills) — `npx skills add nanlabs/agent-toolkit -g`
Catalog: [`catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml)  
Authoring: [`AUTHORING.md`](AUTHORING.md)

## Bundled groups

| Group | Path |
| --- | --- |
| core | `skills/core/` |
| delivery | `skills/delivery/` |
| workflow | `skills/workflow/` |
| forge | `skills/forge/` |
| integrations | `skills/integrations/` |
| design | `skills/design/` |
| data | `skills/data/` |
| ops | `skills/ops/` |
| tooling | `skills/tooling/` |

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
