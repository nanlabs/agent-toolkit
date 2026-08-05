#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "== agent-toolkit smoke preflight =="
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
python3 scripts/validate-agents.py
python3 scripts/gen-surfaces.py --check
bash scripts/secret-scan.sh
if command -v claude >/dev/null 2>&1; then
  echo "== claude plugin validate (non-strict) =="
  claude plugin validate plugins/nanlabs-core || true
  claude plugin validate plugins/nanlabs-agents || true
  echo "== claude plugin validate --strict (must pass for production) =="
  claude plugin validate --strict plugins/nanlabs-core || echo "STRICT FAIL nanlabs-core (see #52)"
  claude plugin validate --strict plugins/nanlabs-agents || echo "STRICT FAIL nanlabs-agents (see #52)"
else
  echo "SKIP: claude CLI not installed"
fi
if command -v npx >/dev/null 2>&1; then
  echo "== skills-ref sample =="
  npx --yes skills-ref validate skills/core/nanlabs-assistant
else
  echo "SKIP: npx not installed"
fi
echo "OK: preflight finished — complete live marketplace checklist on issue #8"
