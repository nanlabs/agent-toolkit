# Production pilots checklist

Companion to [#9](https://github.com/nanlabs/agent-toolkit/issues/9). Run after recommended plugin artifacts are installable (prefer `nanlabs-core`).

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

## C — Non-technical journey (optional)

- [ ] Succeeded with single-instruction path **or**
- [ ] Explicitly removed from product promise in README/ADOPTION

## Go / no-go

- [ ] Comment on #9 with go/no-go for first production distribution milestone
