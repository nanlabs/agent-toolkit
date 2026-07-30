---
name: nanlabs-setup
description: >-
  HOW — First-run setup for the NaNLABS agent toolkit. Inspect the local
  environment against contracts/requirements, report missing baseline tools,
  ask approval before installs, and print a change report. Never print or
  store secrets.
metadata:
  author: nanlabs
  version: "0.2.0"
  status: wave2-doctor
---

# NaNLABS Setup

Public setup skill for `nanlabs/agent-toolkit`.

## Goals

1. Run the **contract doctor** (read-only) against `contracts/requirements/`.
2. Confirm the machine has a **deterministic execution baseline**: Git, Python, package manager awareness.
3. Guide marketplace/plugin install without chezmoi.
4. Ask **explicit approval** before any system change; never auto-install workstation-owned tools.
5. **Never** request, echo, or commit secrets.

## When to use

- User just added the `nanlabs/agent-toolkit` marketplace.
- User asks to "set up NaN plugins", `/setup`, or "what am I missing?".
- Fresh laptop / existing machine smoke test.

## Hard rules

1. Prefer **read-only inspection** first (`scripts/doctor-contracts.py`).
2. Ask for explicit approval before installing software.
3. Only propose installers listed in contracts (`installers.*`); never invent private endpoints.
4. Do not invent private NaNLABS credentials.
5. Point durable details at `docs/ADOPTION.md`, `docs/PUBLIC_CONTENT_POLICY.md`, `contracts/README.md`.

## Procedure

### 1. Doctor (required)

From the repo root (or a clone/checkout of `nanlabs/agent-toolkit`):

```bash
python3 scripts/doctor-contracts.py --contract nanlabs-setup
```

Optional deeper checks:

```bash
python3 scripts/doctor-contracts.py
python3 scripts/doctor-contracts.py --json
```

Summarize the Markdown table for the user. If the script exits non-zero, treat required gaps as **blocking**.

### 2. Baseline spot-checks (if doctor unavailable)

```bash
command -v git && git --version
command -v python3 && python3 --version
command -v brew || command -v winget || command -v apt-get || command -v pacman || true
command -v claude || command -v cursor || true
```

### 3. Approval before installs

For each **fail** / actionable **warn**:

1. Show the contract `install_hint` / installer line.
2. Ask: “Approve running this install?” (yes/no).
3. If `never_auto_install: true` or `installed_by: workstation` — only advise; do not run package managers unless the user insists and understands IT policy.
4. After any approved change, re-run the doctor and fill the **change report** section.

### 4. Install this toolkit

#### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
/plugin install nanlabs-core@nanlabs-agent-toolkit
/plugin install nanlabs-agents@nanlabs-agent-toolkit
```

#### Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

### 5. Propose next (do not auto-install)

- Enable integrations when needed (MCP stubs under `mcp/templates/`, `clickup-cli` skill).
- Point at `docs/LIFECYCLE.md` for pin/update/rollback.

## Change report (print every time)

1. What changed (packages / plugins)
2. Commands run (**no secrets**)
3. Doctor verification results
4. Proposed next packs

## Contracts

- Schema: `contracts/README.md`
- Baseline: `contracts/requirements/nanlabs-setup.yaml`
- Validator: `python3 scripts/validate-contracts.py`

## Out of scope

- Silent auto-install of arbitrary packages
- Telemetry adapters / knowledge backends (Part III)
- Private/internal-only skills (workstation / L2)

## References

- `docs/ADOPTION.md`
- `docs/PUBLIC_CONTENT_POLICY.md`
- `docs/WAVE0_INVENTORY.md`
- `contracts/README.md`
