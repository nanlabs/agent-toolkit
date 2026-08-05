# Production pilots checklist

Companion to [#9](https://github.com/nanlabs/agent-toolkit/issues/9). Run after recommended plugin artifacts are installable (prefer `nanlabs-core`).

**Equal-priority surfaces:** Claude · Claude Code · Cursor IDE · Cursor Agent CLI. Do not treat any of these as optional or secondary for production certification.

## A — Technical Claude Code

- [ ] Clean profile / disposable machine
- [ ] `/plugin marketplace add nanlabs/agent-toolkit`
- [ ] `/plugin install nanlabs-core@nanlabs-agent-toolkit`
- [ ] Namespaced setup works (or setup skill completes doctor)
- [ ] Complete one real task using a core skill (e.g. orientation / PR fallback)
- [ ] Record Claude Code version + notes on #9

## B — Technical Cursor IDE

- [ ] Local plugin load **or** Team Marketplace install of `nanlabs-core`
- [ ] Skills discoverable; setup/onboarding usable
- [ ] Complete one real task
- [ ] Record Cursor version + notes on #9

## C — Technical Cursor Agent CLI

- [ ] Pin CLI binary/version (`agent` / `cursor agent`)
- [ ] Load `nanlabs-core` via supported CLI plugin path
- [ ] Fill skills + commands cells in [`CURSOR_CLI.md`](CURSOR_CLI.md)
- [ ] Complete one real headless or interactive task
- [ ] Record results on #58 and #9

## D — Claude (non–Claude Code) / skills path

- [ ] Skills-only or Claude project path succeeds for at least one core skill **or**
- [ ] Explicit packaging limits documented in README/ADOPTION (priority stays; delivery mechanism may differ)

## E — Non-technical journey

- [ ] Succeeded with single-instruction path **or**
- [ ] Explicitly removed from product promise in README/ADOPTION

## Go / no-go

- [ ] Comment on #9 with go/no-go for first production distribution milestone across all equal-priority surfaces
