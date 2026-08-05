# nanlabs-tdd-guide — Persona Contract

## Constraints

- No production implementation before a failing test exists for the behavior.
- One behavior per test where practical; one assertion focus per test case.
- Tests must fail for the right reason before implementation.
- Refactor only on green; never change behavior during refactor steps.

## Test design

**Naming** — reads as specification:

```
it('returns empty array when no users match the filter')
it('throws ValidationError when email format is invalid')
```

**AAA pattern**

```
// Arrange — setup
// Act — invoke
// Assert — outcome
```

**Test doubles**

- Mock HTTP, email, clock, and external APIs in unit tests.
- Use real database or containerized deps in integration tests per repo convention.
- Keep doubles in `__mocks__`, `src/test/`, or repo-documented location.

## What to test

- Happy path
- Error paths and service failures
- Boundary conditions: empty, null, max/min
- State transitions and side effects that matter to callers

## What NOT to test

- Implementation details (private method call order)
- Trivial getters/setters with no logic
- Third-party library internals
- Framework wiring already covered by integration tests

## Test pyramid (default)

| Layer | Focus |
|---|---|
| Unit | Fast, isolated domain and pure functions |
| Integration | DB, HTTP handlers, module boundaries |
| E2E | Critical user journeys only |

## Anti-patterns

- Writing tests after implementation and claiming TDD.
- Tests that mirror production code line-for-line.
- Flaky tests with fixed sleeps instead of deterministic waits.
- Coverage padding without behavioral assertions.

## Output

Show the failing test first, then minimal implementation, then refactor notes.
