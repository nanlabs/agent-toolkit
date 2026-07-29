# Default Development Workflow — Example Delivery Flow

## Scope

Use only when the project has no explicit workflow override. This example shows a typical sprint flow for a backend API team.

## Status Lifecycle

- [ ] Backlog: item exists but is not yet estimated/scoped/planned.
- [ ] Ready TODO: scope, AC, dependencies, and estimate are ready.
- [ ] In Progress: development and local testing started.
- [ ] Blocked: blocker, impacted environment, and dependency owner documented.
- [ ] Ready for Review: PR/MR created, linked, checks passing or documented.
- [ ] Ready for Acceptance: testing notes, evidence, and AC validation ready.
- [ ] Ready for QA: QA validation can start.
- [ ] Ready for Release: final checks completed.
- [ ] Closed: released/done/not released status selected with final validation notes.

## Definition of Ready (Example: API Endpoint)

- [ ] API contract agreed with consuming team
- [ ] Database migration reviewed (if applicable)
- [ ] Error codes and edge cases defined
- [ ] Unit tests covering core logic written
- [ ] Endpoint documented in OpenAPI/Swagger

## Definition of Done (Example: API Endpoint)

- [ ] Code follows project standards (naming, error handling)
- [ ] Peer review completed with at least 1 approval
- [ ] CI/CD checks pass (lint, test, build)
- [ ] Integration tests passing against staging
- [ ] OpenAPI spec updated
- [ ] Deployment to production completed
- [ ] Monitoring/alerting verified for new endpoint

## Evidence and Traceability (Example)

- [ ] Work item linked to PR/MR
- [ ] API contract documented in TRD
- [ ] Test results attached (Postman collection or automated run)
- [ ] Deployment verified in production logs
- [ ] Traceability: PRD -> Task -> PR/MR -> Deployment
