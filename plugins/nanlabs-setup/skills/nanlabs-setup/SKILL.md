---
name: nanlabs-setup
description: >-
  HOW — First-run setup for the NaNLABS agent toolkit. Inspect the local
  environment, report missing baseline tools (Git, Python, package manager, AI
  clients), and guide configuration. Never print or store secrets.
metadata:
  author: nanlabs
  version: "0.1.0"
  status: p0-scaffold
---

# NaNLABS Setup

Public P0 scaffold skill for `nanlabs/agent-toolkit`.

## Goals

1. Confirm the machine has a **deterministic execution baseline**: Git, a supported Python runtime, and an OS package manager.
2. Confirm at least one AI client is available (Claude Code preferred for P0).
3. Explain how to install this marketplace/plugin without requiring chezmoi.
4. **Never** request, echo, or commit secrets (tokens, PATs, private URLs).

## When to use

- User just added the `nanlabs/agent-toolkit` marketplace.
- User asks to "set up NaN plugins", "/setup", or "what am I missing?".
- Fresh laptop / existing machine smoke test during the P0 spike.

## Hard rules

1. Prefer **read-only inspection** first; ask for explicit approval before installing software.
2. Use OS-native package managers when proposing installs (`brew`, `winget`, `apt`/`dnf`/`pacman`).
3. Do not invent private NaNLABS credentials or endpoints.
4. Point durable process details at public docs in this repo (`docs/ADOPTION.md`, `docs/PUBLIC_CONTENT_POLICY.md`).
5. Client-specific or internal-only content must not be added to this public repository.

## Checklist

Run (or ask the user to run) and summarize:

```bash
command -v git && git --version
command -v python3 && python3 --version
command -v brew || command -v winget || command -v apt-get || command -v pacman || true
command -v claude || command -v cursor || true
```

Then report:

| Check | Status | Next step |
| --- | --- | --- |
| Git | pass/fail | Install via OS package manager |
| Python 3.12+ (preferred) | pass/fail | Install via `uv` / OS package manager |
| Package manager | pass/fail | Document which one is available |
| Claude Code or Cursor | pass/fail | Install client; then re-run marketplace add |

## Install this toolkit

### Claude Code

```text
/plugin marketplace add nanlabs/agent-toolkit
/plugin install nanlabs-setup@nanlabs-agent-toolkit
```

### Any agent (technical)

```bash
npx skills add nanlabs/agent-toolkit -g
```

## Out of scope (later issues)

- Full auto-install orchestration against every contract — Wave 2 (#20); schema lives in `contracts/requirements/`.
- Auto-install of arbitrary packages without approval.
- Telemetry adapters / Onyx knowledge plugins (Part III; conditional).
- Private/internal NaNLABS-only skills (must stay out of this public repo or scrubbed).

## Contracts

Baseline dependency contract: `contracts/requirements/nanlabs-setup.yaml`.
Use it when reporting gaps; do not invent installers outside the contract allowlist.

## References

- `docs/ADOPTION.md`
- `docs/PUBLIC_CONTENT_POLICY.md`
- `docs/WAVE0_INVENTORY.md`
- `contracts/README.md`
- Migration plan (internal): `nanlabs/internal-workstation` → `docs/AI_ASSETS_MIGRATION_PLAN.md`
