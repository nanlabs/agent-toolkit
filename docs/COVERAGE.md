> [!NOTE]
> 📘 **Repo-Only Doc** — last reviewed **2026-09-17**
>
> This document lives only in the repo. It is public-ready and self-contained.

---

# Coverage

Honest map of NaNLABS domains and roles against skills, agents, and packs in
this repository. Use it to pick a first pack and to see gaps. Personas are a
**coverage lens**, not a product to install.

Packs: [`PACKS.md`](PACKS.md) · skills: [`SKILLS.md`](SKILLS.md).

| Domain / role | Pack | What exists today | Gap |
| --- | --- | --- | --- |
| Delivery / PM | `delivery` (group) | PRD, TRD, ADR, epics, stories, tasks, bugs, incidents, planning, assessments, meeting minutes | Strong. Handshake via `nanlabs-output-handshake`. |
| Engineering — code review | `code-review` | Forge skills + `nanlabs-pr-fallback`; agents `nanlabs-code-reviewer`, `nanlabs-security-reviewer`, `nanlabs-typescript-reviewer` | Medium-high. Reviewer must post on the PR ([`HANDOFFS.md`](HANDOFFS.md)). |
| QA | `qa` | `playwright-cli` (browser drive) + agent `nanlabs-e2e-runner` (test authoring) | **Low.** No QA process, test strategy, or case-design skill. |
| Architect | `architect` | Agent `nanlabs-architect` + `nanlabs-adr` / `nanlabs-trd` | Medium. No system-context or C4 skill. |
| Design | `design` (group) | Figma MCP skills + `ui-ux-pro-max` | Medium. Figma connection, not a designer workflow (critique, visual system, presentation layout). |
| Staff / comms | `staff` | `nanlabs-presentations-reconciliation` (ClickUp list vs calendar) | **Low.** No style, tone, or slide-layout consistency skill. |
| Commercial | `delivery` + `workflow` | Work-item and generic-project skills | Medium. No commercial-specific pack (proposals, SOW). Delivery skills are the closest fit. |
| Operations | `ops`, `integrations` | Workstation triage, ClickUp/Slack/Linear, propose-skill | Medium. Ops is tools, not an operations playbook. |
| DevOps / golden stack | — | None in this repo | **Explicit gap.** Next.js + Terraform + AWS (and similar golden deploys) are out of this catalog on purpose. Track as outcome-pack issues `#24` / `#25` / `#28`. |
| Contribution / maintainers | `contribute` | `nanlabs-propose-skill` | Process skill; not a coverage gap. |

## How to read coverage

| Rating | Meaning |
| --- | --- |
| high | A practitioner can do the job with current skills |
| medium | Useful subset; obvious missing procedures |
| low | One or two pointers; do not claim the role is supported |
| none / gap | No pack; do not invent placeholder directories |

Do not fill low/gap rows with empty skills. Add real `SKILL.md` files in a
follow-up PR, then point a pack at them.
