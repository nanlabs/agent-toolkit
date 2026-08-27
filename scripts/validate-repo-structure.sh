#!/usr/bin/env bash
# Structural checks for the agent-toolkit repository layout.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

required_paths=(
  ".claude-plugin/marketplace.json"
  ".cursor-plugin/marketplace.json"
  ".github/copilot-instructions.md"
  ".github/agents/nanlabs-code-reviewer.agent.md"
  ".github/skills/nanlabs-assistant/SKILL.md"
  "plugins/nanlabs-setup/.claude-plugin/plugin.json"
  "plugins/nanlabs-setup/.cursor-plugin/plugin.json"
  "plugins/nanlabs-setup/DEPRECATION.md"
  "plugins/nanlabs-setup/skills/nanlabs-setup/SKILL.md"
  "plugins/nanlabs-core/.claude-plugin/plugin.json"
  "plugins/nanlabs-core/.cursor-plugin/plugin.json"
  "plugins/nanlabs-core/plugin.json"
  "plugins/nanlabs-core/agents/nanlabs-code-reviewer.agent.md"
  "plugins/nanlabs-core/skills/nanlabs-assistant/SKILL.md"
  "plugins/nanlabs-core/skills/nanlabs-setup/SKILL.md"
  "plugins/nanlabs-core/commands/setup.md"
  "plugins/nanlabs-core/scripts/doctor-contracts.py"
  "plugins/nanlabs-core/contracts/requirements/nanlabs-core.yaml"
  "plugins/nanlabs-agents/.claude-plugin/plugin.json"
  "plugins/nanlabs-agents/plugin.json"
  "plugins/nanlabs-agents/agents/nanlabs-architect.md"
  "plugins/nanlabs-agents/agents/nanlabs-architect.agent.md"
  "products/plugins.yaml"
  "catalogs/agent-target-map.yaml"
  "skills/core/nanlabs-setup/SKILL.md"
  "catalogs/skill-catalog.yaml"
  "catalogs/skills-layout.json"
  "docs/PUBLIC_CONTENT_POLICY.md"
  "docs/ADOPTION.md"
  "AGENTS.md"
  "CONTRIBUTING.md"
  "SECURITY.md"
  "LICENSE"
  "README.md"
  ".github/CODEOWNERS"
  ".github/workflows/validate.yml"
  ".github/workflows/mega-linter.yml"
  ".github/workflows/pr-review.yml"
  ".mega-linter.yml"
  ".yamllint.yaml"
  "tools/danger/dangerfile.js"
  "tools/danger/package.json"
  "docs/P0_FINDINGS.md"
  "docs/LIFECYCLE.md"
  "agents/nanlabs-code-reviewer/AGENT.md"
  "agents/nanlabs-assistant/AGENT.md"
  "agents/nanlabs-architect/AGENT.md"
  "mcp/templates/github/config.template.json"
  "mcp/templates/figma/config.template.json"
  "mcp/templates/clickup/config.template.json"
  "catalogs/agent-catalog.yaml"
  "catalogs/mcp-catalog.yaml"
  "schemas/agent-plugins/README.md"
  "schemas/agent-plugins/1.0.0/plugin.schema.json"
  "schemas/agent-plugins/1.0.0/mcp.schema.json"
  "contracts/README.md"
  "contracts/requirements/nanlabs-setup.yaml"
  "contracts/requirements/nanlabs-core.yaml"
  "scripts/gen-copilot-surfaces.py"
  "scripts/validate-no-placeholders.py"
  "scripts/validate-copilot-manifests.py"
  "scripts/validate-agent-plugins.py"
  "scripts/validate-public-content.py"
  "scripts/doctor-contracts.py"
  "docs/WAVE0_INVENTORY.md"
  "docs/adrs/ADR-008-plugins-agent-skills-distribution.md"
  "docs/OVERLAY_GOVERNANCE.md"
  "docs/TELEMETRY_CONTRACT.md"
  "docs/AGENT_PLUGINS.md"
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
