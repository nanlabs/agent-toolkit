# Skills reference

47 public skills under `skills/<group>/<skill>/SKILL.md` ([Agent Skills](https://agentskills.io/specification)).

Machine catalog: [`catalogs/skill-catalog.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/catalogs/skill-catalog.yaml) · human index: [`docs/SKILLS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/SKILLS.md).

## Groups

| Group | Path | Approx. count |
| --- | --- | --- |
| core | `skills/core/` | 6 |
| delivery | `skills/delivery/` | 19 |
| design | `skills/design/` | 6 |
| forge | `skills/forge/` | 4 |
| integrations | `skills/integrations/` | 4 |
| data | `skills/data/` | 2 |
| workflow | `skills/workflow/` | 2 |
| ops | `skills/ops/` | 2 |
| tooling | `skills/tooling/` | 2 |

## Install

```bash
npx skills add nanlabs/agent-toolkit -g
```

Or install **`nanlabs-core`** (bundles core skills + setup) via Claude/Cursor plugins — see [Installation](Installation).

## Not shipped here

| Name | Notes |
| --- | --- |
| `nanlabs-tech-assistant` | Remains on `internal-workstation` for now |
| Some Figma opt-in packs | Documented as related; not in this tree |
| Jira/Confluence assistants | External packs |

## Authoring

See [`docs/AUTHORING.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/AUTHORING.md). After adding skills, keep catalogs/plugins in sync (`scripts/gen-surfaces.py` for plugin mirrors).
