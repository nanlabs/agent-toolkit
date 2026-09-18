---
name: hol-guard
description: >-
  HOW - Set up, verify, and troubleshoot HOL Guard local protection for supported
  AI coding harnesses. Use when a user wants to inspect Guard status, detect a
  harness, install Guard, run guided or manual setup, perform a dry run, launch
  through Guard, or review approvals and receipts.
metadata:
  author: nanlabs
  version: "1.0"
---

# HOL Guard local runtime safety

Use HOL Guard as an additional local protection layer around supported AI coding
harnesses. Native client sandboxing, permission controls, and organization policy
remain authoritative. Do not weaken them to make Guard work.

## When to use

- Install HOL Guard when the executable is not present.
- Check whether HOL Guard is running and what it is protecting.
- Detect a supported local harness before harness installation.
- Run guided or manual Guard setup.
- Test a harness through Guard before a protected launch.
- Review queued approvals, diffs, receipts, or troubleshooting evidence.

## Safety rules

- Never print, copy, or persist credentials, tokens, or private configuration in
  chat, logs, issues, or commits.
- Never edit Guard's local database or trust material directly.
- Never auto-approve a queued request. Approval is a trust decision and must stay
  explicit.
- Prefer the narrowest harness and approval scope that solves the task.
- Do not use `hol-guard init --yes` unless unattended setup was explicitly
  requested and side effects are acceptable.
- Do not start mutation-bearing harness work until Guard has passed the health
  gate below. If Guard cannot prove a healthy protection state, stop instead of
  launching the harness unprotected.

## Procedure

1. Ensure the `hol-guard` executable is installed. Use one of the supported HOL
   Guard package surfaces rather than inventing an installer:

   ```bash
   pipx install hol-guard
   ```

   If the user is intentionally working inside a Python environment instead of
   an isolated `pipx` application environment, use that environment's Python:

   ```bash
   python -m pip install hol-guard
   ```

   Confirm the installed executable before continuing:

   ```bash
   hol-guard --version
   ```

2. Inspect the current state before changing harness configuration:

   ```bash
   hol-guard status --json
   hol-guard detect --json
   ```

3. For guided first-run setup, use the interactive flow:

   ```bash
   hol-guard init
   ```

   Use the manual discovery path when each setup step should be inspected:

   ```bash
   hol-guard bootstrap
   ```

4. Use the exact harness identifier requested by the user or returned by
   detection. Common identifiers include `codex`, `claude`, `cursor`, `gemini`,
   and `opencode`. Install Guard for that harness only when installation is in
   scope:

   ```bash
   hol-guard install <harness>
   ```

5. Run a dry pass before a live protected launch:

   ```bash
   hol-guard run <harness> --dry-run
   ```

6. Enforce the health gate before any live mutation-bearing work. Re-run status
   after setup and require both commands below to succeed:

   ```bash
   hol-guard status --json
   hol-guard run <harness> --dry-run
   ```

   Stop if either command exits nonzero, if status reports that protection is
   degraded, inactive, or needs repair, or if the dry run cannot verify the
   selected harness. Do not fall back to launching the harness directly.

   When the health gate fails, diagnose before changing more state:

   ```bash
   hol-guard doctor <harness> --json
   hol-guard diff <harness>
   ```

   Repair the reported condition, then repeat the health gate from the start.

7. Launch through Guard only after the health gate passes:

   ```bash
   hol-guard run <harness>
   ```

8. Review decisions and evidence without bypassing the approval flow:

   ```bash
   hol-guard approvals
   hol-guard receipts
   hol-guard status --json
   ```

   Only run `hol-guard approvals approve <request-id>` or a denial command after
   the user has made that decision.

## Output contract

Report only what is needed to continue safely:

- detected harness or harnesses
- current Guard status
- commands that actually ran and whether they succeeded
- whether the health gate passed or blocked the launch
- pending approvals or warnings
- the next safe command, if one is needed

Do not claim that Guard replaced native sandboxing or host security. Do not claim
protection that the local status or command output did not verify.

## Reference

Current HOL Guard local setup and troubleshooting flow:
`https://github.com/hashgraph-online/hol-guard/blob/main/docs/guard/get-started.md`
