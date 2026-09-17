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
Maintainer bar: [`skills/ops/nanlabs-propose-skill/references/REVIEW-CHECKLIST.md`](../skills/ops/nanlabs-propose-skill/references/REVIEW-CHECKLIST.md).
Authoring layout: [`AUTHORING.md`](AUTHORING.md).
Public scrub: [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md).

## Flow

1. Search `catalogs/skill-catalog.yaml`, `catalogs/pack-catalog.yaml`, and
   `catalogs/agent-catalog.yaml` so the proposal is not a duplicate.
2. Open a GitHub issue on **nanlabs/agent-toolkit** with the **Propose skill**
   template: <https://github.com/nanlabs/agent-toolkit/issues/new?template=propose-skill.yml>.
3. Author under `skills/<group>/<name>/` (or `agents/<name>/`) with a real
   `SKILL.md` / `AGENT.md` — never a README-only directory.
4. Update catalogs and, if needed, [`PACKS.md`](PACKS.md).
5. Open a pull request against **`nanlabs/agent-toolkit` `main`**, fill the
   Skill/Agent checklist, link the issue (`Fixes #N`).
6. CODEOWNERS (`@nanlabs/internal-maintainers`, `@nanlabs/oss-core-team`)
   review: security, sense, duplicates, quality, pack membership, Cloud-safe
   skills fallback.
7. Squash-merge. The skill is then available:

   ```bash
   npx skills add nanlabs/agent-toolkit@<skill-name>
   npx skills add nanlabs/agent-toolkit/skills/<group>
   ```

## Review checklist (short)

- No secrets, private URLs, or client data
- Not a duplicate; description includes when to use it
- Handoff documented or N/A ([`HANDOFFS.md`](HANDOFFS.md))
- Cloud users can run the skill without native subagents
- Pack membership recorded or N/A
- Validators pass (`validate-skills.py`, `validate-pack-catalog.py`,
  `validate-no-placeholders.py`, `secret-scan.sh`)

## Related

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — clone, CI, PR mechanics
- Packs: [`PACKS.md`](PACKS.md)
- Coverage gaps: [`COVERAGE.md`](COVERAGE.md)
