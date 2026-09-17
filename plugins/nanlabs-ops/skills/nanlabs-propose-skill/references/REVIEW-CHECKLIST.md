# Maintainer review checklist (propose skill)

Use this list when reviewing a PR **on
[nanlabs/agent-toolkit](https://github.com/nanlabs/agent-toolkit)** that adds or
changes `plugins/*/skills/` or `agents/`. It is the artisan approval gate: share via PR
to that repo, admin review, then installable.

## Security and public safety

- [ ] No secrets, tokens, private URLs, client names, or internal hostnames
- [ ] `docs/PUBLIC_CONTENT_POLICY.md` satisfied; skill marked `public: true`
      only after scrub
- [ ] Scripts do not exfiltrate data; env-var names only, never values
- [ ] `bash scripts/secret-scan.sh` and `python3 scripts/validate-public-content.py`
      pass

## Duplication and sense

- [ ] Not a rename of an existing catalog skill or agent
- [ ] Description states **what** it does **and when** to use it
- [ ] Group under `plugins/nanlabs-<group>/skills/` is the smallest honest bucket
- [ ] If the job is already a handoff of another skill, extend that skill
      instead of adding a sibling

## Quality

- [ ] `SKILL.md` / `AGENT.md` frontmatter `name` matches the directory
- [ ] `python3 scripts/validate-skills.py` (and `validate-agents.py` if needed)
- [ ] `python3 scripts/validate-pack-catalog.py` if pack membership changed
- [ ] `python3 scripts/validate-skill-inventory.py`
- [ ] `python3 scripts/validate-agent-plugins.py` if `plugins/` changed
- [ ] Handoff and output contract documented (`docs/HANDOFFS.md`) or N/A
- [ ] Cloud users can follow the skill without native subagents
      (Code/Cursor-only steps are labeled)

## Pack membership

- [ ] Listed in `catalogs/skill-catalog.yaml` and `catalogs/skills-layout.json`
- [ ] Domain pack updated, or an explicit N/A in the PR
- [ ] No new empty or README-only directories
      (`python3 scripts/validate-no-placeholders.py`)

## Agent Plugins v1

Apply when the PR touches `plugins/` or a root `plugin.json`.
See [Agent Plugins](https://agent-plugins.org/specification).

- [ ] Root `plugin.json` is closed schema (`$schema` MUST be
      `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`; no
      `skills`/`agents` path fields)
- [ ] Plugin skills are immediate `plugins/<id>/skills/<name>/SKILL.md`
      (clients MUST NOT recurse, §7.1). That directory is the only copy.
- [ ] Agents stay in `agents/` / native plugin surfaces (not a v1 portable type)
- [ ] Optional MCP is root `mcp.json` with matching schema version. Official
      hosted servers are generated from `catalogs/mcp-catalog.yaml`.
- [ ] Catalog packs were not given a `plugin.json`

## Merge

- [ ] CODEOWNERS approval
- [ ] Issue linked (`Fixes #N` / `Refs #N`)
- [ ] After merge, the skill is reachable with `npx skills add nanlabs/agent-toolkit@<name>`
