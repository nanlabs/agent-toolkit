# Public content policy — nanlabs/agent-toolkit

This repository is **public**. Anything merged here is visible on the internet.

## Allowed

- Generic skills, agents, plugins, and MCP **stubs** that help NaNLABS (and the community) work with AI clients.
- Documentation that does not expose private process, client names under NDA, or internal URLs.
- Env-var **names** and placeholder contracts (for example `${CLICKUP_API_TOKEN}`).
- Open-source licenses and attributed third-party excerpts that are redistribution-safe.

## Forbidden

- Secrets: API keys, PATs, passwords, private keys, session cookies.
- Private hostnames, bastion addresses, internal IP ranges, or non-public VPN endpoints.
- Client-confidential workflows, credentials, or data samples.
- Unredacted screenshots or logs containing tokens or PII.
- Copying internal-only workstation content without a scrub review.

## Review gate

Before merging content migrated from `internal-workstation`:

1. Run `bash scripts/secret-scan.sh` and `python3 scripts/validate-skills.py`.
2. Confirm GitHub secret scanning / push protection remain enabled.
3. Mark the skill/plugin as `public: true` in `catalogs/skill-catalog.yaml` only after scrub.
4. If content must stay private, keep it in a private companion marketplace (future) or L2 packs — not here.

## Reporting

If you find sensitive material in this repo, follow `SECURITY.md` — do not discuss exploit details in a public issue.
