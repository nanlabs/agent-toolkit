---
name: nanlabs-dev-companion
description: >-
  WHAT — NaNLABS Dev Companion (general): layered companion for client delivery; modes, gates,
  delegation to nanlabs-assistant and nanlabs-workflow-generic-project; no CLI matrices.
---

# NaNLABS Dev Companion (WHAT) — general layer (L2)

This skill is the **general** dev companion for NaNLABS work. It does **not** replace **`nanlabs-assistant`** (orchestrator); it **sits above** workflows and names **what to invoke next**.

**Language:** English for ticket comments, PR text, and user-facing outputs when this companion drives delivery work.

## Layering

| Layer | Skill | Role |
| --- | --- | --- |
| L1 | **nanlabs-assistant** | Repo inspection order, conflict resolution, fallback |
| **L2 (this skill)** | **nanlabs-dev-companion** | Companion framing: modes, gates, delegation for client work |
| L3 | **Workspace pack overlay** | Client/account-specific context loaded from `~/.nan-ai-workspace/packs/` |

If engagement triggers match, load the appropriate **workspace pack overlay** first, then proceed with **nanlabs-workflow-generic-project**. Do not mix multiple workflow drivers on the same task.

## Mode selection

- **Default** for NaNLABS/client delivery: use **nanlabs-workflow-generic-project** for phased delivery.
- If the user mentions an engagement, ticket prefix, or repo context → load the matching pack from the workspace (overlay) and apply its boundaries/gates.
- If unclear → **ask** before applying L3.

## Delegation (HOW is in other skills)

Use **`skill-catalog.yaml`** and **`nanlabs-assistant`** for routing. This skill names **what** to invoke next:

- Discovery and conflicts → **nanlabs-assistant**
- Delivery phases → **nanlabs-workflow-generic-project**
- Artifact gate → **nanlabs-output-handshake** (before final deliverables)
- Tickets, forge, data, Figma, Slack → matching **HOW** skill from the catalog

Do **not** paste forge or ticket CLI sequences here.

## Operating modes

- **Interactive (default):** IDE session; user steers each step.
- **Queued job (optional):** only when a local runner is configured; see `~/.local/share/nanlabs/dev-companion/README.md` (installed from chezmoi) and **references/LOOP_GUARDRAILS.md**.

The queue worker is **mandatory infrastructure** (installed by workstation). The **workspace** (`~/ai-workspace`) is optional — it provides project-aware wrappers, job templates, and knowledge base integration. When both are present, the runner automatically enriches LLM prompts with workspace context (`projects.yaml`, `projects/`, `knowledge/todos/`).

### LLM policy gate (client engagements)

Before queueing background jobs for a client repo, confirm the active LLM policy with **`nan-devcompanion llm-status`**. If the engagement requires a single AI account (e.g. only the customer's Anthropic key), the workstation/pack must set **`NAN_DEVCOMPANION_LLM_ALLOWLIST`** and **`NAN_DEVCOMPANION_LLM_STRICT=1`** so the runner fails closed instead of falling back to OpenCode. For Cursor/Copilot-only engagements, prefer **`run-once --no-llm`** (skeleton plan) plus IDE-driven execution. Full reference: **`docs/DEV_COMPANION_LLM.md`**.

## Checklist

- [ ] L3 not needed; if needed, user confirmed engagement context
- [ ] **nanlabs-assistant** discovery pass before large edits
- [ ] **nanlabs-workflow-generic-project** phases and gates when doing generic client delivery
- [ ] Tool skills used for all CLI operations
