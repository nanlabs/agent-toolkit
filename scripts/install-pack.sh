#!/usr/bin/env bash
# Install one pack from catalogs/pack-catalog.yaml via npx skills.
# Extra flags after the pack id are forwarded (for example: -g -y).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALIDATOR="$ROOT/scripts/validate-pack-catalog.py"

usage() {
  cat <<'EOF'
Usage: scripts/install-pack.sh <pack-id> [npx skills flags...]
       scripts/install-pack.sh --list

Examples:
  scripts/install-pack.sh delivery
  scripts/install-pack.sh code-review -g -y
  scripts/install-pack.sh --list
EOF
}

if [[ $# -lt 1 ]]; then
  usage >&2
  exit 2
fi

if [[ $1 == "-h" || $1 == "--help" ]]; then
  usage
  exit 0
fi

if [[ $1 == "--list" ]]; then
  python3 "$VALIDATOR" --list
  exit 0
fi

PACK_ID=$1
shift

if ! command -v npx >/dev/null 2>&1; then
  printf 'ERROR: npx is required (Node.js).\n' >&2
  exit 1
fi

mapfile -t NPX_ARGS < <(python3 "$VALIDATOR" --npx-args "$PACK_ID")
if [[ ${#NPX_ARGS[@]} -eq 0 ]]; then
  printf 'ERROR: pack %s produced an empty npx argument list\n' "$PACK_ID" >&2
  exit 1
fi

printf 'Installing pack %s:\n  npx' "$PACK_ID"
for arg in "${NPX_ARGS[@]}" "$@"; do
  printf ' %q' "$arg"
done
printf '\n'

exec npx --yes "${NPX_ARGS[@]}" "$@"
