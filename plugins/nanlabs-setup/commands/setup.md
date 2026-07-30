---
name: setup
description: Inspect the local environment against NaNLABS contracts and guide first-run setup
---

# /setup

1. Load the `nanlabs-setup` skill.
2. Run `python3 scripts/doctor-contracts.py --contract nanlabs-setup` from an `agent-toolkit` checkout when available; otherwise use the skill’s baseline spot-checks.
3. Summarize gaps. **Ask approval** before any install; never auto-install workstation-owned tools.
4. Guide marketplace/plugin install (`nanlabs-setup`, `nanlabs-core`, `nanlabs-agents`).
5. Print the change report (what changed, commands, verification, next packs).
6. Do not print secrets. Do not write credentials into the repository.
