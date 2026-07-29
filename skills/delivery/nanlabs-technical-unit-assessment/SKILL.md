---
name: nanlabs-technical-unit-assessment
description: >-
  WHAT - Evidence-based technical unit assessment for repositories, platforms,
  frontend, backend, infrastructure, data, UI/UX, and AI-native structural readiness.
---

# Technical Unit Assessment (WHAT)

Use this skill to assess a technical unit: frontend app, backend API, data platform, infrastructure/IaC scope, mobile app, AI/ML pipeline, or another technical workload.

Run **`nanlabs-project-assessment-evidence`** first and use **`nanlabs-project-assessment`** as the router when the assessment spans multiple units.

## Default guardrails

1. Apply **`nanlabs-output-handshake`** before final scorecards or reports.
2. Ask where each evidence source lives before scoring.
3. Score only indicators that match the unit type and available evidence.
4. Mark every score with evidence links and confidence.
5. Use **Not assessed** when evidence is missing or the indicator is out of scope.

## Unit intake

Ask:

- What is the technical unit name?
- What type of unit is it?
- Which repositories, services, infrastructure scopes, data pipelines, design assets, or environments are included?
- Who owns technical decisions: NaNLABS team, client/team counterpart, shared ownership, or unknown?
- What period should the assessment cover?
- Which systems are authoritative for code, docs, CI/CD, releases, incidents, observability, architecture, security, and data quality?

## Reference

See `references/indicators.md` for the full procedure.
