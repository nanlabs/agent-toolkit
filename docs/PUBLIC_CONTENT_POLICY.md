> [!IMPORTANT]
> 📘 **ClickUp Companion**, last synced **2026-08-03**
>
> This document is mirrored in ClickUp for cross-team discovery and execution logging:
> - 📑 **[Practices](https://app.clickup.com/459857/docs/e12h-314297/e12h-155117)**
>
> **ClickUp** is the cross-team discovery + execution-log surface.
> **This repo doc** is the co-located implementation reference (close to the code).
> When you update one, sync the other and bump the **last synced** date above.

<!-- Internal: ClickUp links require NaNLABS workspace access -->

---

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
4. If content must stay private, keep it on **workstation**, **L2 packs**, or a **private project marketplace** — not in this public repository.

## Companion marketplace (decision)

**Decision (2026-07-30):** do **not** create a private companion marketplace yet.

| Keep private content in | When |
| --- | --- |
| `internal-workstation` (L1 AI home) | Internal-only skills/procedures still dual-railed |
| L2 / project overlays | Client or initiative-specific packs |
| Future private marketplace repo | Only if private corpus volume or sharing needs exceed workstation + L2 |

Revisit when cutover (#23) or enterprise packs force multi-team distribution of non-public skills. Until then, scrub-or-exclude is enough for `agent-toolkit`.

## Reporting

If you find sensitive material in this repo, follow `SECURITY.md` — do not discuss exploit details in a public issue.
