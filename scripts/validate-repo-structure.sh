#!/usr/bin/env bash
# Structural checks for the agent-toolkit repository layout.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

required_paths=(
  ".claude-plugin/marketplace.json"
  ".cursor-plugin/marketplace.json"
  "plugins/nanlabs-setup/.claude-plugin/plugin.json"
  "plugins/nanlabs-setup/.cursor-plugin/plugin.json"
  "plugins/nanlabs-setup/skills/nanlabs-setup/SKILL.md"
  "skills/nanlabs-setup/SKILL.md"
  "catalogs/skill-catalog.yaml"
  "docs/PUBLIC_CONTENT_POLICY.md"
  "docs/ADOPTION.md"
  "AGENTS.md"
  "CONTRIBUTING.md"
  "SECURITY.md"
  "LICENSE"
  "README.md"
  ".github/CODEOWNERS"
  ".github/workflows/validate.yml"
)

missing=0
for path in "${required_paths[@]}"; do
  if [[ ! -e $path ]]; then
    printf 'ERROR: missing required path: %s\n' "$path" >&2
    missing=1
  fi
done

if [[ $missing -ne 0 ]]; then
  exit 1
fi

printf 'OK: repository structure checks passed (%d paths)\n' "${#required_paths[@]}"
