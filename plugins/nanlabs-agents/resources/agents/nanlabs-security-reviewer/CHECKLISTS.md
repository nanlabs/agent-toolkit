# Security review checklists

## Injection

- [ ] SQL: parameterized queries only
- [ ] Command injection: no unsanitized input to shell
- [ ] XSS: output encoding in templates and SPA
- [ ] Template/LDAP/SSRF/path traversal vectors reviewed

## Authentication and authorization

- [ ] No hardcoded credentials or API keys
- [ ] JWT: signature, expiry, algorithm allowlist
- [ ] Session cookies: secure, httpOnly where applicable
- [ ] Authorization on every protected operation
- [ ] No IDOR via predictable object references

## Data exposure

- [ ] Passwords, tokens, PII not logged
- [ ] API errors do not leak stack traces or internal schema
- [ ] Secrets not committed; `.env.example` only in repo

## Input validation

- [ ] All external inputs validated at boundary
- [ ] File uploads: type, size, content checks
- [ ] Webhooks: signature verification

## Cryptography

- [ ] No MD5/SHA1 for security-sensitive hashing
- [ ] Cryptographically secure randomness for tokens
- [ ] TLS for remote credentials in transit

## Dependencies

- [ ] Audit tooling run or CVE note when unavailable
- [ ] Pin versions for security-critical packages
