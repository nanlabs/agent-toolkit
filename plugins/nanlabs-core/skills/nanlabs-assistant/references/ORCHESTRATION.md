# Skill orchestration (NaNLABS)

Authoritative routing lives with the **nanlabs-assistant** skill. This file is a short operational guide; **`catalogs/skill-catalog.yaml`** is the default machine-readable index (domain, WHAT vs HOW, triggers, `depends_on`). After a workstation install, an optional copy may also exist at `~/.local/share/nanlabs/skills/skill-catalog.yaml`.

## Role of this skill

**nanlabs-assistant** is the **orchestrator and fallback**:

- **Orchestrator:** choose workflow vs tool skills using the catalog and the user’s request.
- **Fallback:** when the task is unclear, spans domains, or no specialized skill fits, keep using this skill’s repo-inspection order and citation rules.

Do **not** duplicate full procedures owned by Jira, ClickUp, forge, or data skills inside this file.

## Routing algorithm (reasoning-based)

1. **Read** `skill-catalog.yaml` (same directory as bundled skills) and note **responsibility**: **WHAT** = workflow phases and gates; **HOW** = CLI and automation steps.
2. **Classify** the user request:
   - **Setup/onboarding** (new dev, validate install) → **nanlabs-setup** / `/nanlabs-core:setup`, `docs/ADOPTION.md`
   - **Client/account overlay** (explicit engagement mention, ticket prefix, or repo path context) → load the **workspace pack overlay** (see below), then proceed with **nanlabs-dev-companion** + **nanlabs-workflow-generic-project** (WHAT). Do **not** mix multiple workflow drivers on the same task.
   - **Generic NaNLABS/client delivery** → **nanlabs-dev-companion** (companion framing) + **nanlabs-workflow-generic-project** (WHAT).
   - **Planning / estimation / capacity** → **nanlabs-planning** (after output handshake for final notes).
   - **Default development workflow / DoR / DoD / validation** → **nanlabs-development-workflow** unless repo docs override.
   - **Work item creation or refinement** → **nanlabs-work-item** and then **nanlabs-epic**, **nanlabs-user-story**, **nanlabs-task**, **nanlabs-bug**, or **nanlabs-incident**.
   - **Meeting minutes** → **nanlabs-meeting-minutes**.
   - **Decision or agreement** → **nanlabs-decision-log**, **nanlabs-agreement**, or **nanlabs-adr** depending on durability and scope.
   - **Spike or research findings** → **nanlabs-spike**.
   - **Project assessment / maturity assessment / technical or management unit scorecard** → **nanlabs-project-assessment**; collect sources with **nanlabs-project-assessment-evidence**, then score via **nanlabs-technical-unit-assessment** or **nanlabs-management-unit-assessment**.
   - **Background job/plan generation** → **dev-companion-llm**. Default mode picks OpenCode/big-pickle; **for client engagements with a single-AI-account policy** (e.g. "only their Anthropic key") set **`NAN_DEVCOMPANION_LLM_ALLOWLIST`** + **`NAN_DEVCOMPANION_LLM_STRICT=1`** and verify with **`nan-devcompanion llm-status`** before queuing jobs. See **`docs/DEV_COMPANION_LLM.md`** for Cursor/Copilot guidance (`--no-llm` skeleton + IDE-driven LLM).
   - **Ticket system only** → external **jira-*** skills, external **confluence-*** skills, or bundled **clickup-cli** as appropriate.
   - **Where to save a deliverable + review** → **nanlabs-output-handshake** (what path, which system, who reviews) before final PRD/TRD/ADR or PR text.
   - **PRD / TRD / ADR** to NaNLABS templates in ClickUp → **nanlabs-prd**, **nanlabs-trd**, **nanlabs-adr** (after the handshake when output is final).
   - **Default pull-request body** when the repo has no template → **nanlabs-pr-fallback** (after the handshake) before **github-cli-workflow** or for MR description with **gitlab-cli-workflow** when applicable.
   - **Draft PR/MR** after push → **github-cli-workflow** or **gitlab-cli-workflow** by remote host.
   - **GitHub PR review comments / threads** on the open PR → **gh-address-comments** (read/triage); pair with **github-cli-workflow** when pushing fixes.
   - **Failing GitHub Actions checks** → **gh-fix-ci** (logs + snippet); pair with **nanlabs-planning** for an explicit fix plan before coding.
   - **Linear** issues, cycles, projects → **linear** (Linear MCP; OAuth).
   - **Figma design → code** → start from **figma** / **figma-implement-design**; **figma-code-connect-components** for Code Connect; **figma-create-design-system-rules** for `AGENTS.md`/rules files; **figma-create-new-file** for new files. Heavy canvas/plugin flows (**figma-use**, **figma-generate-design**) are opt-in packs — see `docs/SKILLS.md`.
   - **Terminal browser automation** (snapshot/click, not test specs) → **playwright-cli**. **Playwright test suites** → **nanlabs-e2e-runner**.
   - **Scaffold or refactor `.ipynb`** → **jupyter-notebook** (**nan-newnotebook** wrapper).
   - **Workstation install / health / pasteable diagnostics** → **nanlabs-workstation-triage** (optional; L1 provisioning is out of scope for this repo)
   - **dbt checks** → **dbt-validation**; **Snowflake checks** → **snowflake-validation** (read-only; never claim success without creds).
3. **Delegate** with one explicit line in the reply, e.g. *Applying **nanlabs-workflow-generic-project** for phases; using **github-cli-workflow** for draft PR.*
4. **If uncertain**, ask which engagement context applies before heavy work, then fall back to this skill’s discovery pass.

## Delegation phrasing

- Workflow skills state **phases, gates, and artifacts** only; they **name** the HOW skill to use next (see each workflow `SKILL.md`).
- Tool skills contain **commands, flags, and fallbacks**.
- One-line **telemetry-lite** for traceability: attribute the active workflow and tool skills by name when making a non-trivial decision.

## Conflicts

- If **AGENTS.md** or repo docs contradict a workflow skill, **surface the conflict** and default to **AGENTS.md** for repo-specific guardrails unless the user directs otherwise.
- Client overlays (workspace packs) and **nanlabs-workflow-generic-project** are compatible; avoid mixing multiple workflow drivers on the same task.

## Client/account overlays (workspace packs)

Client-specific and account-specific overlays live in the user workspace under:

- `~/.nan-ai-workspace/packs/`
- `~/.nan-ai-workspace/knowledge/`

If the user signals an engagement (ticket prefix, repo path prefix, explicit name), prefer loading the corresponding pack first, then proceed with the generic workflow and tool skills.

## Agent dispatch (personas vs skills)

Agents carry **methodology and output contracts**; skills carry **procedures and templates**. Use `@mention` (Claude/OpenCode) or the matching Cursor/Windsurf rule.

| Situation | Agent | Complementary skill |
| --- | --- | --- |
| Structural design / trade-offs | `nanlabs-architect` | `nanlabs-adr` |
| Plan before implementation | `nanlabs-planner` | `nanlabs-planning` |
| Post-change / pre-PR review | `nanlabs-code-reviewer` | `github-cli-workflow` |
| Auth, secrets, injection | `nanlabs-security-reviewer` | — |
| New feature with tests-first | `nanlabs-tdd-guide` | — |
| Type-heavy review | `nanlabs-typescript-reviewer` | — |
| Schema / query / migration | `nanlabs-database-reviewer` | — |
| Internal NaNLABS procedures | `nanlabs-tech-assistant` (workstation-only for now) | not bundled in agent-toolkit yet |
| Client delivery bootstrap | `nanlabs-client-workflow-bootstrap` | `nanlabs-workflow-client-bootstrap` |
| Repo discovery / routing | `nanlabs-assistant` | this skill |

Machine-readable index: `catalogs/agent-catalog.yaml`. Canonical bodies and `references/CONTRACT.md` live under `agents/<name>/` in this repository.

## Installed paths (reference)

| Asset | Path |
| --- | --- |
| Skill catalog (repo default) | `catalogs/skill-catalog.yaml` |
| Agent catalog | `catalogs/agent-catalog.yaml` |
| Agent personas (canonical) | `agents/<name>/AGENT.md` |
| This orchestrator | `skills/core/nanlabs-assistant/SKILL.md` |
| Repo inspection detail | `skills/core/nanlabs-assistant/references/REPO_INSPECTION.md` |

Optional workstation mirror paths after L1 install: `~/.local/share/nanlabs/skills/` and `~/.local/share/nanlabs/agents/`.
