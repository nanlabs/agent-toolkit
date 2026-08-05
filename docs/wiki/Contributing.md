# Contributing

Canonical: [`CONTRIBUTING.md`](https://github.com/nanlabs/agent-toolkit/blob/main/CONTRIBUTING.md) · agent contract: [`AGENTS.md`](https://github.com/nanlabs/agent-toolkit/blob/main/AGENTS.md).

## Setup

```bash
git clone https://github.com/nanlabs/agent-toolkit.git
cd agent-toolkit
python3 -m pip install pre-commit
pre-commit install
```

## Validate

```bash
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/gen-surfaces.py --check
bash scripts/secret-scan.sh
pre-commit run --all-files
```

## Wiki source

Edit pages under `docs/wiki/` in git. After merge to `main`, the **Sync Wiki** workflow copies them to the GitHub Wiki (wiki must be initialized once on GitHub).

## Public safety

No secrets, private URLs, or client data. See [`docs/PUBLIC_CONTENT_POLICY.md`](https://github.com/nanlabs/agent-toolkit/blob/main/docs/PUBLIC_CONTENT_POLICY.md).
