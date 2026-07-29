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

CI runs the same checks on non-draft pull requests (see `.github/workflows/validate.yml`).

## Pull requests

1. Create a feature branch from `main`.
2. Keep PRs focused and linked to a GitHub issue (`Fixes #N`).
3. Fill the PR template checklist, including the public-repo section.
4. Prefer squash merges unless maintainers request otherwise.

## Code owners

See `.github/CODEOWNERS`.
