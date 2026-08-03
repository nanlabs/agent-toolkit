> [!IMPORTANT]
> 📘 **ClickUp Companion**, last synced **2026-08-03**
>
> This document is mirrored in ClickUp for cross-team discovery and execution logging:
>
> - 📑 **[Workspace Conventions](https://app.clickup.com/459857/docs/e12h-314297/e12h-156937)**
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

<!-- Internal: ClickUp links require NaNLABS workspace access -->

---

# Project overlay governance

Project-specific plugins and packs are first-class (plan §4.5). This doc is the
governance checklist so overlays do not fork incompatible ecosystems.

## Hard rules

1. **Credentials stay in L1 only** — `env.d`, MDM, or secret managers. Never in
   overlay git content (no tokens, private hosts, or client secrets).
2. **Do not duplicate central skills** — depend on `nanlabs-core` /
   `nanlabs-agents` / catalog skills; override via thin project rules if needed.
3. **Declare a core version** — which `agent-toolkit` / plugin versions the
   overlay was validated against.
4. **Name an owner + review date** — stale overlays get archived or promoted.

## Required metadata (`overlay.yaml`)

Place at the root of a project overlay repo or under `packs/<id>/`:

```yaml
apiVersion: nanlabs.dev/v1
kind: ProjectOverlay
metadata:
  name: example-project-harness
  owner: "team-or-person@nanlabs.com"
  reviewBy: "2026-12-31"
spec:
  requires:
    agentToolkit: ">=0.3.0"   # marketplace / repo tag guidance
    plugins:
      - nanlabs-core@0.1.0
      - nanlabs-agents@0.1.0
  composes:
    packs:
      - engineering-workflow
      - delivery-discipline
    capabilities:
      - mcp:github
  permissions:
    - filesystem.read
    - network.outbound
  dataClasses:
    - internal
  # Never list secret values — names only if needed
  envNames:
    - GITHUB_TOKEN
```

## Governance checklist (PR / review)

- [ ] `overlay.yaml` present with owner + `reviewBy`
- [ ] Declares required core / plugin versions
- [ ] No duplicated copies of central `skills/` or `agents/`
- [ ] No secrets, private URLs, or client NDA material (see `PUBLIC_CONTENT_POLICY.md`)
- [ ] Permissions / data classes declared
- [ ] Credentials documented as L1-only
- [ ] Promotion path noted (stay L3 vs graduate to central catalog)

## Example composition

See [`packs/project-harness/`](../packs/project-harness/) — a **stub** solution
pack that documents how a project composes platform capabilities without
shipping credentials.

Typical stack:

```text
Org marketplace (agent-toolkit)
├── nanlabs-setup / nanlabs-core / nanlabs-agents
└── Project overlay (private repo or L3)
    ├── overlay.yaml
    ├── rules / AGENTS.md deltas
    └── optional thin skills unique to the engagement
```

## Related

- [`TELEMETRY_CONTRACT.md`](TELEMETRY_CONTRACT.md) — L1 installs adapters; overlays do not embed endpoints
- [`PUBLIC_CONTENT_POLICY.md`](PUBLIC_CONTENT_POLICY.md)
- [`../packs/README.md`](../packs/README.md)
