# 🛠️ Skills reference

49 public skills under `plugins/nanlabs-<group>/skills/<skill>/SKILL.md` ([Agent Skills](https://agentskills.io/specification)).

Machine catalog: [`catalogs/skill-catalog.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/catalogs/skill-catalog.yaml) · packs: [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md) · human index: [`docs/SKILLS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/SKILLS.md).

## Groups

| Group | Path | Approx. count |
| --- | --- | --- |
| core | `plugins/nanlabs-core/skills/` | 7 |
| delivery | `plugins/nanlabs-delivery/skills/` | 19 |
| design | `plugins/nanlabs-design/skills/` | 6 |
| forge | `plugins/nanlabs-forge/skills/` | 4 |
| integrations | `plugins/nanlabs-integrations/skills/` | 4 |
| data | `plugins/nanlabs-data/skills/` | 2 |
| workflow | `plugins/nanlabs-workflow/skills/` | 2 |
| ops | `plugins/nanlabs-ops/skills/` | 3 |
| tooling | `plugins/nanlabs-tooling/skills/` | 2 |

## Install

```bash
npx skills add nanlabs/agent-toolkit -g
npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills
```

Or install **`nanlabs-core`** (bundles core skills + setup) via Claude/Cursor plugins — see [Installation](Installation). Domain packs: [`docs/PACKS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PACKS.md).

## Not shipped here

| Name | Notes |
| --- | --- |
| Some Figma opt-in packs | Documented as related; not in this tree |
| Jira/Confluence assistants | External packs |

## Authoring

See [`docs/AUTHORING.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/AUTHORING.md). After adding skills, keep catalogs in sync (`scripts/gen-surfaces.py` for manifests only).
