---
name: nanlabs-pyrightination
description: >-
  HOW — Run Pyright in report-only mode for Python projects, summarize the
  diagnostics by severity and file, and recommend the next fix order without
  auto-applying code changes.
metadata:
  author: nanlabs
  version: "0.1.0"
  status: public
---

# NaNLABS Pyrightination

Use this skill when the user wants a **type-checking pass** over a Python codebase
with **Pyright**, but does not want speculative refactors or automatic fixes.

## Goals

1. Detect whether Pyright can run from the current environment.
2. Prefer **Python ecosystem** execution via `uvx --from pyright pyright`.
3. Fall back to `npx --yes pyright` only when the Python-first path is unavailable.
4. Produce a **report**: error count, warning count, most affected files, and a
   short remediation order.
5. Do **not** auto-fix code unless the user explicitly asks for a follow-up change.

## When to use

- The user asks for “run Pyright”, “type-check this repo”, or “what type errors do we have?”
- A Python project needs a production-readiness pass focused on typing.
- A CI failure points at Pyright diagnostics and the user wants a structured summary first.

## Hard rules

1. Report-first only. No silent code edits.
2. Keep the original Pyright output available if the user asks for it, but summarize the key findings.
3. Prefer the toolchain already available in the repo/environment.
4. Never invent config flags; use `pyrightconfig.json` / `pyproject.toml` if the repo already defines them.
5. If Pyright is not available, explain the missing runtime (`uvx` or `npx`) and ask before proposing install steps.

## Preferred execution order

### 1. Python-first path

```bash
uvx --from pyright pyright --outputjson
```

Use this when `uvx` is available. It avoids a permanent install while staying in
the Python/uv toolchain.

### 2. Existing environment path

If the repo already ships a dedicated wrapper or task runner, prefer that instead
of ad-hoc commands.

Examples:

```bash
python3 -m pyright --outputjson
pyright --outputjson
```

### 3. Node fallback

```bash
npx --yes pyright --outputjson
```

Use only when the Python-first path is unavailable and Node tooling exists.

## Reporting format

Summarize:

1. Whether Pyright ran successfully.
2. Total diagnostics by severity.
3. Top files with the most errors.
4. The first fixes that should unblock the highest number of downstream errors.

Preferred structure:

- `Result:` pass/fail
- `Counts:` errors / warnings / information
- `Hotspots:` top files
- `Next fixes:` 2–5 concrete items

## Triage heuristics

- Fix import resolution and missing symbol issues first.
- Then fix incompatible return / argument types.
- Defer noisy low-severity hints unless the user asks for strict cleanup.
- Group repeated errors by root cause instead of echoing dozens of near-identical messages.

## Out of scope

- Auto-applying type fixes
- Inventing a new project-wide typing policy
- Replacing MyPy/Pyrefly/other checkers without a user request
