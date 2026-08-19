> [!IMPORTANT]
> 📘 **ClickUp Companion**, last synced **2026-08-03**
>
> This document is mirrored in ClickUp for cross-team discovery and execution logging:
>
> - 📑 **[Practices](https://app.clickup.com/459857/docs/e12h-314297/e12h-155117)**
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

<!-- Internal: ClickUp links require NaNLABS workspace access -->

---

# Telemetry contract — L1 policy vs L1.5 adapters

**Status:** Contract only (Wave 1). Org-wide enablement is Part III (#30), not a
cutover blocker.

## Ownership split

| Responsibility | Owner | Layer |
| --- | --- | --- |
| Telemetry **policy** (on/off, retention, allowed backends) | Workstation / org | L1 |
| Endpoint, credentials, opt-in/out | Workstation | L1 |
| Deterministic **install** of approved adapters | Workstation (`nan-doctor` / profile) | L1 |
| Versioned client hooks (Claude / OpenCode / …) | `agent-toolkit` packages/plugins | L1.5 |
| Project-specific tweaks | Project overlay | L3 |
| Collector / backend | Infra | — |
| Redaction + retention enforcement | Security + Infra | — |

**Rule of thumb:** Workstation installs the telemetry adapter; telemetry must
**not** configure the Workstation.

## L1.5 may ship

- Versioned adapter code / hooks under `packages/` or a future dedicated plugin
  (when implemented under #30).
- Documentation of supported clients and required **env-var names**.
- Capability declarations in `contracts/requirements/` (future).

## L1.5 must never ship

- Telemetry endpoints, API keys, or tenant IDs as literals.
- Auto-enable without L1 policy (`telemetry=on`).
- PII-bearing sample payloads in fixtures.

## Env-var names (placeholders only)

| Name | Purpose |
| --- | --- |
| `NAN_TELEMETRY` | Org toggle hint (`on` / `off`) — L1 writes |
| `NAN_TELEMETRY_ENDPOINT` | OTLP or vendor ingest URL — L1 writes |
| `NAN_TELEMETRY_TOKEN` | Auth to collector — L1 secret store only |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Optional standard OTLP alias |
| `OTEL_EXPORTER_OTLP_HEADERS` | Optional; never commit values |

Doctor / setup may check **presence** of names when `NAN_TELEMETRY=on`; never
print values.

## Redaction requirements

1. Strip Authorization headers and bearer tokens from exported spans/logs.
2. Do not record file contents, prompts, or secrets in default exporters.
3. Prefer hashed / bucketed identifiers over emails when possible.
4. Retention follows Security policy — adapters must honor disable/opt-out from L1.

## Recommended install sequence (future)

1. L1 profile sets `telemetry=on` and writes `~/.config/nanlabs/telemetry.env`
   (mode `600`).
2. L1 installs the org-approved adapter version from L1.5.
3. AI client restarts; doctor probes endpoint reachability without dumping tokens.

## Current repository state

Telemetry remains **documentation-only** in this repository.
No `nanlabs-telemetry` plugin directory is kept in-tree until a real adapter
ships under #30.

## Related

- ADR-008 · Wave 0 inventory · Part III epic #29 / #30
