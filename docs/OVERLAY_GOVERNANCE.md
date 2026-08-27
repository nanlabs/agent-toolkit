> [!NOTE]
> 📘 **ClickUp Companion**, last synced **2026-08-27**
>
> This document is mirrored in the NaNLABS internal ClickUp workspace for cross-team discovery and execution logging.
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

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

Place at the root of a project overlay repo:

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
      - nanlabs-core@0.3.1
      - nanlabs-agents@0.2.1
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

Future outcome-pack work is tracked in GitHub issue `#24`. This repository no
longer keeps stub pack directories as overlay examples.

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
- GitHub issue `#24`
