#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "== agent-toolkit smoke preflight =="
bash scripts/validate-repo-structure.sh
python3 scripts/validate-manifests.py
python3 scripts/validate-skills.py
python3 scripts/validate-skill-inventory.py
python3 scripts/validate-agents.py
python3 scripts/gen-surfaces.py --check
bash scripts/secret-scan.sh
if command -v claude >/dev/null 2>&1; then
  echo "== claude plugin validate (non-strict) =="
  for p in plugins/nanlabs-*; do
    if [[ -d "$p/.claude-plugin" ]]; then
      claude plugin validate "$p" || true
    fi
  done
  echo "== claude plugin validate --strict (must pass for production) =="
  for p in plugins/nanlabs-*; do
    if [[ "$(basename "$p")" == "nanlabs-setup" ]]; then
      continue
    fi
    if [[ -d "$p/.claude-plugin" ]]; then
      claude plugin validate --strict "$p" || echo "STRICT FAIL $p (see #52)"
    fi
  done
else
  echo "SKIP: claude CLI not installed"
fi
if command -v npx >/dev/null 2>&1; then
  echo "== skills-ref sample =="
  npx --yes skills-ref validate plugins/nanlabs-core/skills/nanlabs-assistant
else
  echo "SKIP: npx not installed"
fi
echo "OK: preflight finished — complete live marketplace checklist on issue #8"
