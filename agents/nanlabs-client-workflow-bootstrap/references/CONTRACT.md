# nanlabs-client-workflow-bootstrap — Persona Contract

## Constraints

- Interview completeness before generation; no partial skill pairs.
- User confirmation gate is mandatory.
- All generated artifacts in **English** (commits, PR body, skill content).
- Follow patterns from existing `nanlabs-workflow-*` skills in internal-workstation.

## Generated artifacts

- `skills/nanlabs-<slug>-workflow/SKILL.md` + `reference.md` + `skill.json`
- `skills/nanlabs-<slug>-dev-companion/SKILL.md` + `skill.json`
- `skill-catalog.yaml` entries (two)
- Agent stubs for delivery (via sync script pattern when applicable)

## Updating existing workflow

1. Load existing files first.
2. Ask which interview groups to revisit.
3. Show diff summary before applying.

## Commit message

`feat(skills): add nanlabs-<slug>-workflow and dev-companion skill pair`

## Anti-patterns

- Generating without workspace pack context when engagement is known.
- Skipping validation tools section in reference.md.
- Non-draft PR without user approval.
