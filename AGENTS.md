# AGENTS.md — agent-toolkit

Portable agent contract for work in this repository.

## Purpose

`nanlabs/agent-toolkit` is the **public** distribution source for NaNLABS AI capabilities (skills, agents, plugins, MCP stubs). Workstation provisioning stays in `internal-workstation`.

## Hard rules

1. This repo is **public** — follow `docs/PUBLIC_CONTENT_POLICY.md` on every change.
2. Never commit secrets, private URLs, client data, or unredacted credentials.
3. Prefer official scripts under `scripts/` and CI workflows under `.github/workflows/`.
4. Do not invent install flags; document real Claude/Cursor/`npx skills` flows in `docs/ADOPTION.md`.
5. Destructive or force-push operations require explicit human confirmation.

## Default workflow

1. Read `README.md`, `docs/ADOPTION.md`, and the linked GitHub issue.
2. Implement the smallest public-safe change.
3. Run:

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
bash scripts/secret-scan.sh
```

4. Open a PR using `.github/PULL_REQUEST_TEMPLATE.md` and link the issue.

## Routing

| Task | Where |
| --- | --- |
| Machine provisioning / doctor / telemetry policy | `nanlabs/internal-workstation` |
| Plugin/skill content and marketplaces | this repo |
| Onyx / observability backends | `nanlabs/internal-terraform-infra` |
| Migration program tracking | GitHub Project [AI Native Workbench](https://github.com/orgs/nanlabs/projects/12) |
