# Dependency and permission contracts

Machine-readable declarations that `nanlabs-setup` (and future `/setup` automation) use to detect, request approval for, install, and verify dependencies.

Canonical path: `contracts/requirements/<id>.yaml`

## Schema (v1)

| Field | Required | Description |
| --- | --- | --- |
| `apiVersion` | yes | Must be `nanlabs.dev/v1` |
| `kind` | yes | Must be `RequirementContract` |
| `metadata.name` | yes | Kebab-case id; must match filename stem |
| `metadata.description` | yes | Human summary |
| `metadata.appliesTo` | no | List of skill/plugin/MCP ids this contract covers |
| `spec.requirements.binaries` | yes | List of binary requirements (may be empty) |
| `spec.capabilities` | yes | List of capability strings (may be empty) |
| `spec.setup` | no | Interactive / verification hints |
| `spec.env` | no | Required env-var **names** (never values) |

### Binary entry

| Field | Required | Description |
| --- | --- | --- |
| `name` | yes | Executable name (`git`, `python3`, `clickup`, …) |
| `required` | yes | `true` / `false` |
| `installed_by` | yes | `workstation` \| `plugin` \| `user` |
| `version` | no | Semver range hint (informational for v1) |
| `verify` | no | Shell command that exits 0 when present |
| `installers` | no | Map of `macos` / `linux` / `windows` install hints (strings) |

### Capability vocabulary (v1 allowlist)

- `filesystem.read`
- `filesystem.write`
- `subprocess.execute`
- `network.outbound`
- `mcp.client`
- `secrets.env` — reads env vars; never writes secrets into git

### Setup block

| Field | Description |
| --- | --- |
| `interactive` | Prefer approval prompts before system changes |
| `verification_command` | Optional post-install check |
| `never_auto_install` | When true, setup only reports gaps (default for workstation-owned binaries) |

## Doctor (read-only)

```bash
python3 scripts/doctor-contracts.py --contract nanlabs-setup
python3 scripts/doctor-contracts.py          # all contracts
```

Never installs software; prints a Markdown gap/change-report template for `/setup`.
2. Workstation-owned tools (`git`, `python3`, OS package manager) use `installed_by: workstation` and should set `never_auto_install: true` unless IT policy says otherwise.
3. Plugin-owned optional tools may propose OS installers; `nanlabs-setup` must ask approval before running them.
4. `spec.requirements.binaries[].verify` must be a **simple argv command** (no shell metacharacters). The doctor runs it without a shell.
5. Validate with `python3 scripts/validate-contracts.py`.

See migration plan §4.4 and [`docs/AUTHORING.md`](../docs/AUTHORING.md).
