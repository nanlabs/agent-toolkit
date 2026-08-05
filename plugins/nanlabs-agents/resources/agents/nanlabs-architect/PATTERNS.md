# Architecture patterns reference

## SOLID (apply with judgment)

| Principle | Practical check |
|---|---|
| **S**ingle Responsibility | One reason to change per module; split when tests or reviews fight over unrelated concerns |
| **O**pen/Closed | Extend via composition or strategy at real variation points, not speculative hooks |
| **L**iskov Substitution | Subtypes honor contracts; no surprising side effects in overrides |
| **I**nterface Segregation | Small interfaces consumed by callers; avoid "god" service interfaces |
| **D**ependency Inversion | Domain logic does not import infrastructure; depend on abstractions at boundaries |

## Clean Architecture (lite)

- **Entities / domain** — business rules with no framework imports.
- **Use cases / application** — orchestration; depends on domain and port interfaces.
- **Adapters** — HTTP, DB, CLI, queues; implement ports, map external models inward.
- **Dependency rule** — source dependencies point inward; frameworks at the edge.

Use full layering only when the repo already follows it or the team will maintain the ceremony.

## Design patterns (when they earn their keep)

| Pattern | Good fit | Skip when |
|---|---|---|
| Repository | Multiple persistence backends or test doubles at boundary | Thin CRUD with one ORM |
| Strategy | Pluggable algorithms with 2+ real implementations | One algorithm forever |
| Factory | Complex object graphs or environment-specific construction | `new` is clear enough |
| Observer / events | Cross-cutting reactions, audit, async side effects | Synchronous flow is simpler |
| CQRS | Read/write scale or shape diverge materially | Same model serves both well |

## API and service boundaries

- Resources map to domain concepts, not database tables exposed raw.
- Version at the boundary when external consumers exist.
- Idempotency keys for mutating operations that clients may retry.
- Errors: stable codes, no stack traces or internal IDs in public responses.
- Pagination: cursor/keyset for large collections; document limits.

## Data modeling

- Model invariants in the domain layer; enforce with DB constraints where possible.
- Prefer explicit types over stringly-typed status fields.
- Migration strategy in the recommendation when schema changes are involved.
