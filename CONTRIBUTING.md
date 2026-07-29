# Contributing

Thanks for contributing to `agent-toolkit`.

## Public repository

This project is public. By opening a PR you confirm the change does **not** include secrets, private infrastructure details, or client-confidential material. See `docs/PUBLIC_CONTENT_POLICY.md`.

## Development setup

```bash
git clone https://github.com/nanlabs/agent-toolkit.git
cd agent-toolkit
python3 -m pip install pre-commit
pre-commit install
```

## Validation before PR

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
bash scripts/secret-scan.sh
pre-commit run --all-files
```

CI on non-draft PRs:

| Workflow | Job |
| --- | --- |
| `validate.yml` | Structure, manifests, skills, secret-scan, pre-commit |
| `mega-linter.yml` | MegaLinter v9 (cupcake allowlist) |
| `pr-review.yml` | Danger JS (TypeScript) under `tools/danger/` |

Danger expects the PR template sections and an issue reference (`Fixes #N` / `Refs #N`).

## Pull requests

1. Create a feature branch from `main`.
2. Keep PRs focused and linked to a GitHub issue (`Fixes #N`).
3. Fill the PR template checklist, including the public-repo section.
4. Prefer squash merges unless maintainers request otherwise.

## Code owners

See `.github/CODEOWNERS`.
