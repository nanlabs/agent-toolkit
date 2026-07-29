# Code review checklists

## Quality

- [ ] Code is clear and self-documenting
- [ ] Functions do one thing (SRP)
- [ ] No meaningful duplication (DRY)
- [ ] Names reflect domain and intent

## Correctness

- [ ] All failure paths handled
- [ ] Edge cases: null, empty, boundary values
- [ ] No off-by-one or race conditions in hot paths
- [ ] Idempotency where retries exist

## Security (first pass)

- [ ] No secrets in code or logs
- [ ] User input validated before use
- [ ] SQL/command/template injection prevented
- [ ] Auth and authz on protected operations

## Performance

- [ ] No N+1 queries or equivalent fan-out
- [ ] No unnecessary re-renders or recomputation
- [ ] Appropriate caching; no unbounded memory growth

## Testing

- [ ] New behavior has tests
- [ ] Tests assert behavior, not implementation trivia
- [ ] Failure paths tested where risk is non-trivial
