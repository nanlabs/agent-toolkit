#!/usr/bin/env bash
# Lightweight secret scan for tracked text files (defense in depth vs GitHub push protection).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -t 1 && -z ${NO_COLOR:-} ]]; then
  c_red=$'\033[1;31m'
  c_green=$'\033[1;32m'
  c_blue=$'\033[1;34m'
  c_reset=$'\033[0m'
else
  c_red=''
  c_green=''
  c_blue=''
  c_reset=''
fi

info() { printf '%b[secret-scan]%b %s\n' "$c_blue" "$c_reset" "$*"; }
fail() { printf '%b[secret-scan]%b %s\n' "$c_red" "$c_reset" "$*"; }
ok() { printf '%b[secret-scan]%b %s\n' "$c_green" "$c_reset" "$*"; }

info "scanning tracked text files for high-risk secret patterns"

# Exclude binary-ish extensions; rely on git ls-files for tracked content only.
mapfile -t files < <(git ls-files | rg -v '\.(png|jpg|jpeg|gif|webp|ico|pdf|zip|gz|tgz|woff2?|ttf|eot)$' || true)

if [[ ${#files[@]} -eq 0 ]]; then
  fail "no tracked files to scan"
  exit 1
fi

patterns=(
  '-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----'
  '\bAKIA[0-9A-Z]{16}\b'
  '\bghp_[A-Za-z0-9]{36}\b'
  '\bgithub_pat_[A-Za-z0-9_]{20,}\b'
  '\bxox[baprs]-[A-Za-z0-9-]{10,}\b'
  '(?i)api[_-]?key\s*[:=]\s*['\''\"][^'\''\"]{12,}['\''\"]'
)

status=0
for pattern in "${patterns[@]}"; do
  if rg -n --hidden -S -e "$pattern" -- "${files[@]}" >/tmp/agent-toolkit-secret-hits.txt 2>/dev/null; then
    fail "pattern matched: ${pattern}"
    cat /tmp/agent-toolkit-secret-hits.txt >&2 || true
    status=1
  fi
done

rm -f /tmp/agent-toolkit-secret-hits.txt

if [[ $status -ne 0 ]]; then
  fail "secret scan failed"
  exit 1
fi

ok "no high-risk secret patterns found in tracked files"
