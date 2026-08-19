# NaNLABS Copilot Instructions

Portable repository customization surface for `nanlabs/agent-toolkit`.

## Scope

- Baseline product: `nanlabs-core`
- Repository: `https://github.com/nanlabs/agent-toolkit`
- Product description: Recommended install: setup/onboarding, orchestrator, companion, handshake, PR fallback, knowledge sync, and code-reviewer agent

## Public repository rules

- Follow `AGENTS.md` and `docs/PUBLIC_CONTENT_POLICY.md` on every change.
- Never commit secrets, private URLs, client data, or credentials.
- Prefer official scripts under `scripts/` and CI workflows under `.github/workflows/`.
- Do not invent install flags; document only real platform flows already present in this repo.

## Available baseline skills

- `nanlabs-setup`
- `nanlabs-assistant`
- `nanlabs-dev-companion`
- `nanlabs-output-handshake`
- `nanlabs-pyrightination`
- `nanlabs-pr-fallback`
- `nanlabs-workspace-knowledge-sync`

## Available agents

- `nanlabs-code-reviewer`

## Source files

- `README.md`
- `AGENTS.md`
- `docs/ADOPTION.md`
- `docs/LIFECYCLE.md`
- `products/plugins.yaml`

