# Database review checklist

## Schema

- [ ] FKs and cascades intentional
- [ ] Indexes support query patterns
- [ ] No silent truncation from type mismatch
- [ ] Soft-delete vs hard-delete consistent

## Queries

- [ ] No N+1
- [ ] SELECT * avoided on wide tables in hot paths
- [ ] Pagination strategy appropriate
- [ ] Parameterized queries only

## Migrations

- [ ] Backward compatible deploy order documented
- [ ] Long-running DDL has batch strategy
- [ ] Down migration or recovery documented

## Operations

- [ ] Connection limits understood
- [ ] Timeouts and retries configured
- [ ] Sensitive columns encrypted or access-controlled
