# Production pilots checklist

> **Status:** The original pilot issue is **CLOSED**. This checklist is retained as the historical operator evidence template; record refreshed evidence in [RELEASE.md](RELEASE.md) and the surface-specific [CURSOR_CLI.md](CURSOR_CLI.md) matrix.

Run after recommended plugin artifacts are installable (prefer `nanlabs-core`).

**Equal-priority surfaces:** Claude · Claude Code · Cursor IDE · Cursor Agent CLI · GitHub Copilot. Do not treat any of these as optional or secondary for production certification.

## A — Technical Claude Code

- [ ] Clean profile / disposable machine
- [ ] `/plugin marketplace add nanlabs/agent-toolkit`
- [ ] `/plugin install nanlabs-core@nanlabs-agent-toolkit`
- [ ] Namespaced setup works (or setup skill completes doctor)
- [ ] Complete one real task using a core skill (e.g. orientation / PR fallback)
- [ ] Record Claude Code version + notes in the current release evidence ([RELEASE.md](RELEASE.md))

## B — Technical Cursor IDE

- [ ] Local plugin load **or** Team Marketplace install of `nanlabs-core`
- [ ] Skills discoverable; setup/onboarding usable
- [ ] Complete one real task
- [ ] Record Cursor version + notes in the current release evidence ([RELEASE.md](RELEASE.md))

## C — Technical Cursor Agent CLI

- [ ] Pin CLI binary/version (`agent` / `cursor agent`)
- [ ] Load `nanlabs-core` via supported CLI plugin path
- [ ] Fill skills + commands cells in [`CURSOR_CLI.md`](CURSOR_CLI.md)
- [ ] Complete one real headless or interactive task
- [ ] Record CLI results in the certification matrix ([CURSOR_CLI.md](CURSOR_CLI.md)) and current release evidence ([RELEASE.md](RELEASE.md))

## D — Claude (non–Claude Code) / skills path

- [ ] Skills-only or Claude project path succeeds for at least one core skill **or**
- [ ] Explicit packaging limits documented in README/ADOPTION (priority stays; delivery mechanism may differ)

## E — Non-technical journey

- [ ] Succeeded with single-instruction path **or**
- [ ] Explicitly removed from product promise in README/ADOPTION

## Go / no-go

- [ ] Record the go/no-go for the first production distribution milestone in the current release evidence ([RELEASE.md](RELEASE.md))
