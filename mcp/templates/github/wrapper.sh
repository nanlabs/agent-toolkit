#!/usr/bin/env bash
set -euo pipefail

if [[ -z ${GITHUB_PERSONAL_ACCESS_TOKEN:-} ]]; then
  echo "GITHUB_PERSONAL_ACCESS_TOKEN is required" >&2
  exit 1
fi

exec npx -y @modelcontextprotocol/server-github
