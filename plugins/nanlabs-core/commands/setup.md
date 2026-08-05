---
name: setup
description: Inspect the local environment against NaNLABS contracts and guide first-run setup
---

# /nanlabs-core:setup

1. Load the `nanlabs-setup` skill (bundled in this plugin).
2. Run the bundled doctor (plugin-relative — **no repo checkout required**):

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/doctor-contracts.py" --contract nanlabs-core
   ```

   If `${CLAUDE_PLUGIN_ROOT}` is unavailable, use the skill's fallback path or baseline spot-checks.

3. Summarize gaps. **Ask approval** before any install; never auto-install workstation-owned tools.
4. Confirm `nanlabs-core` is installed; optionally guide `nanlabs-agents` install.
5. Print the change report (what changed, commands, verification, next packs).
6. Do not print secrets. Do not write credentials into the repository.
