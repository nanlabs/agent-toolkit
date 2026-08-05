# Performance checklist

## Frontend

- [ ] Profiler shows unnecessary re-renders addressed
- [ ] Bundle size impact measured for new deps
- [ ] Images/fonts optimized
- [ ] Critical path resources not blocked

## Backend

- [ ] Query count per request acceptable
- [ ] No sync I/O on hot async paths
- [ ] Memory stable under load test
- [ ] Pool exhaustion ruled out

## Database

- [ ] EXPLAIN reviewed for hot queries
- [ ] Missing indexes identified
- [ ] Lock contention understood

## Verification

- [ ] Before/after numbers recorded
- [ ] Regression test or benchmark script noted
