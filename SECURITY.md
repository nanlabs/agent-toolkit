# Security Policy

## Supported baseline

Only the latest `main` branch is actively supported for security updates.

## Reporting a vulnerability

If you discover a security issue:

1. **Do not** open a public issue with exploit details or leaked secrets.
2. Contact the NaNLABS Technology team through internal channels, or email `technology@nanlabs.com` if you are an external reporter.
3. Include reproduction details, impact, and affected files when safe to share.

## Security principles in this repository

- No credentials are stored in source control.
- MCP templates (when present) use environment-variable placeholders only.
- CI runs `scripts/secret-scan.sh` plus GitHub secret scanning / push protection.
- Public content must pass `docs/PUBLIC_CONTENT_POLICY.md` before merge.
