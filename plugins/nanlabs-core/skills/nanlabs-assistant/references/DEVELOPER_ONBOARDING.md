# Developer onboarding (NaNLABS agent-toolkit)

Use only when the user asks about **toolkit setup**, **getting started**, or **validating install**.
For general repo work, use `REPO_INSPECTION.md` instead.

## First-time setup (public distribution)

Cite `docs/ADOPTION.md` and `docs/wiki/Installation.md` for the canonical install paths:

1. **Claude Code / Cursor** — add marketplace `nanlabs/agent-toolkit`, install **`nanlabs-core`**, run **`/nanlabs-core:setup`**.
2. **GitHub Copilot** — install CLI plugin manifests from `plugins/nanlabs-core/` (see `docs/wiki/Installation.md`).
3. **Skills-only** — `npx skills@1.5.23 add nanlabs/agent-toolkit -g` (see `docs/LIFECYCLE.md` for update/remove).

Machine provisioning (OS packages, chezmoi, fleet doctor) stays in the separate L1 repo documented in `docs/FAQ.md`; this toolkit does not require it for skills/plugin use.

## Post-setup validation

**Plugin install (preferred):**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/doctor-contracts.py" --contract nanlabs-core
```

**Repo checkout (contributors / CI):**

```bash
python3 scripts/doctor-contracts.py --contract nanlabs-core
```

Expected: required contract checks pass; optional gaps are reported as warnings.

## AI tools check

```bash
claude --version    # or cursor agent, copilot, etc.
npx skills@1.5.23 check
```

## Helpful commands

| Task | Command |
| --- | --- |
| Validate baseline tools | `/nanlabs-core:setup` or doctor script above |
| List installed skills (skills-only) | `npx skills@1.5.23 check` |
| Workstation health (optional) | load **nanlabs-workstation-triage** |
| Adoption docs | read `docs/ADOPTION.md` |

## If issues persist

1. Re-run the doctor / setup skill and address reported gaps.
2. Confirm marketplace/plugin versions in `docs/LIFECYCLE.md`.
3. Open a GitHub issue on `nanlabs/agent-toolkit` with doctor output (**no secrets**).
