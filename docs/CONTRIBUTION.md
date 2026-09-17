> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Contribution (skills and agents)

Anyone may **propose** a skill or agent to
**[nanlabs/agent-toolkit](https://github.com/nanlabs/agent-toolkit)**.
Maintainers **approve**. After merge the change is installable (`npx skills` /
plugins). That GitHub repository is the source of truth.

Clone (do not open the PR against a client repo or `internal-workstation`):

```bash
git clone https://github.com/nanlabs/agent-toolkit.git
```

This is the same shape as a share-then-approve loop (propose, security and
duplication review, then publish as an installable). There is no separate
sharing product.

Contributor walkthrough: skill **`nanlabs-propose-skill`**.
Maintainer bar: [`plugins/nanlabs-ops/skills/nanlabs-propose-skill/references/REVIEW-CHECKLIST.md`](../plugins/nanlabs-ops/skills/nanlabs-propose-skill/references/REVIEW-CHECKLIST.md).
Authoring layout: [`AUTHORING.md`](AUTHORING.md).
Public scrub: [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md).

## Flow

1. Search `catalogs/skill-catalog.yaml`, `catalogs/pack-catalog.yaml`, and
   `catalogs/agent-catalog.yaml` so the proposal is not a duplicate.
2. Open a GitHub issue on **nanlabs/agent-toolkit** with the **Propose skill**
   template: <https://github.com/nanlabs/agent-toolkit/issues/new?template=propose-skill.yml>.
3. Author under `plugins/nanlabs-<group>/skills/<name>/` (or `agents/<name>/`) with a real
   `SKILL.md` / `AGENT.md` — never a README-only directory.
4. Update catalogs and, if needed, [`PACKS.md`](PACKS.md).
5. Open a pull request against **`nanlabs/agent-toolkit` `main`**, fill the
   Skill/Agent checklist, link the issue (`Fixes #N`).
6. CODEOWNERS (`@nanlabs/internal-maintainers`, `@nanlabs/oss-core-team`)
   review: security, sense, duplicates, quality, pack membership, Cloud-safe
   skills fallback, and [Agent Plugins](https://agent-plugins.org/specification)
   layout if `plugins/` changed.
7. Squash-merge. The skill is then available:

   ```bash
   npx skills add nanlabs/agent-toolkit@<skill-name>
   npx skills add nanlabs/agent-toolkit/plugins/nanlabs-<group>/skills
   ```

## Review checklist (short)

- No secrets, private URLs, or client data
- Not a duplicate; description includes when to use it
- Handoff documented or N/A ([`HANDOFFS.md`](HANDOFFS.md))
- Cloud users can run the skill without native subagents
- Pack membership recorded or N/A
- Validators pass (`validate-skills.py`, `validate-pack-catalog.py`,
  `validate-no-placeholders.py`, `secret-scan.sh`; `validate-agent-plugins.py`
  when `plugins/` changes)

## Agent Plugins v1 (when touching `plugins/`)

Portable packages MUST match [Agent Plugins](https://agent-plugins.org/specification):

- Root `plugin.json` is a **closed** manifest (`$schema` MUST be
  `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`). No
  `skills`/`agents` path fields.
- Skills in a plugin are **only** `plugins/<id>/skills/<name>/SKILL.md`
  (immediate children). That directory **is** the canonical skill. Do not
  keep a second copy under `skills/<group>/` or `.github/skills/`.
- Agents are not a v1 portable component. Keep them in `agents/` and native
  plugin surfaces (`plugins/<id>/agents/`, `com.github.copilot/agents/`).
- Optional MCP is `mcp.json` at the plugin root with the matching schema
  version. This repo ships none.
- A **pack** is not a plugin. Do not add `plugin.json` for a catalog pack.

## Related

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — clone, CI, PR mechanics
- Packs: [`PACKS.md`](PACKS.md)
- Agent Plugins: [`AGENT_PLUGINS.md`](AGENT_PLUGINS.md)
- Coverage gaps: [`COVERAGE.md`](COVERAGE.md)
