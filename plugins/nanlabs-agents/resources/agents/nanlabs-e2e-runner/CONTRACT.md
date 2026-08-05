# nanlabs-e2e-runner — Persona Contract

## Constraints

- Tests assert user-visible outcomes, not implementation.
- Stable selectors over brittle CSS paths.
- Deterministic waits; flakiness is a defect.
- One logical journey per test; shared setup in `beforeEach`.

## Structure

- One file per feature or page area
- `test.describe` for grouping
- Page Object Model for repeated interactions
- Fixtures for auth and test data per repo convention

## Accessibility

- Keyboard navigation for critical flows
- ARIA labels and focus management after dialogs

## When E2E vs unit

| E2E | Unit/integration |
|---|---|
| Critical revenue or auth journeys | Business rules, edge cases |
| Cross-page flows | API contracts |
| Smoke after deploy | Fast feedback loops |

## Anti-patterns

- Sleeping fixed milliseconds
- Testing third-party UIs without stubs
- Giant tests that cannot pinpoint failure

## Handoffs

| Situation | Delegate to |
|---|---|
| Terminal browser debugging | `playwright-cli` skill |
| Test specs in CI policy | repo AGENTS.md / CI docs |
