---
name: nanlabs-workspace-knowledge-sync
description: >-
  Syncs knowledge to the internal-ai-workspace knowledge base. Use when the assistant
  discovers new patterns, learns user preferences, or identifies information worth
  preserving for future sessions. Can be triggered manually or by orchestrators.
---

# NaNLABS Workspace Knowledge Sync

Automatically syncs valuable discoveries, patterns, and decisions to the internal-ai-workspace knowledge base.

---

## Purpose

The orchestrator session accumulates knowledge through work. This skill ensures that valuable discoveries don't get lost and are available for future sessions.

---

## Consent and data classification (required)

Before syncing **anything** to a knowledge base — especially on **client repositories**:

1. **Ask the user** whether the item is approved for persistence outside the current session.
2. **Classify** the content: public-safe, internal-only, client-confidential, or unknown.
3. **Default to no sync** when classification is unknown or the repo is client-scoped unless the user explicitly approves.
4. **Redact** secrets, private URLs, credentials, client identifiers, and unredacted ticket/customer details before writing.
5. Follow `docs/PUBLIC_CONTENT_POLICY.md` and repository `AGENTS.md` when present.

Never persist ClickUp space IDs, list IDs, custom fields, or process details from client engagements without explicit approval.

---

## Trigger Points (Automatic)

Orchestrators may invoke this skill automatically **only after** the consent and classification checks above pass:

| Situation | What to Sync | Target File |
|-----------|--------------|-------------|
| Discovery of new skill/tool | Skill name, purpose, usage pattern | `knowledge/skills/discovered.md` |
| New ClickUp pattern (approved, redacted) | Non-sensitive routing metadata only | `knowledge/processes/clickup/` |
| New process pattern | Process steps, roles, tools (no client secrets) | `knowledge/processes/general.md` |
| Key decision made | Decision, rationale, outcome | `knowledge/learnings/general.md` |
| Pending follow-up | Task description, context | `knowledge/todos/pending.md` |
| User teaches something | Information, preference | Relevant knowledge file |

---

## How It Works

The skill uses `assistant-memory` CLI tool to sync knowledge:

```bash
# Search before adding
assistant-memory search "<query>"

# Add a learning
assistant-memory add --type learning "Pattern: <description>"

# Add a skill
assistant-memory add --type skill "New skill: <name> - <description>"

# Add a pending todo
assistant-memory add --type todo "<description>"
```

---

## Knowledge Structure

```
knowledge/
├── skills/
│   └── discovered.md      # New skills found during work
├── processes/
│   ├── clickup/
│   │   ├── README.md     # ClickUp workspace index
│   │   └── spaces/       # Per-space documentation
│   ├── jira.md
│   ├── confluence.md
│   └── general.md        # Generic process patterns
├── learnings/
│   └── general.md        # Key decisions and insights
└── todos/
    └── pending.md        # Follow-up items
```

---

## Manual Usage

You can also trigger this skill manually:

```
User: "Save that pattern for later"

Assistant: → Use knowledge-sync to preserve the pattern
```

---

## Integration with orchestrators

Orchestrators (`nanlabs-assistant`, dev-companion lead) may check for these automatic sync opportunities:

1. **After task creation/update** → Sync initiative info
2. **After discovering space/list IDs** → Sync to ClickUp knowledge
3. **After learning user preferences** → Sync to learnings
4. **When user mentions follow-up** → Add to pending

---

## Best Practices

1. **Be selective** - Only sync valuable, reusable information
2. **Be specific** - Include context and usage examples
3. **Be concise** - One idea per entry, link to details
4. **Be current** - Update outdated information when found

---

## Examples

### Auto-sync ClickUp discovery:
```
Assistant discovers Initiative list IDs for all Technology spaces
→ Syncs to knowledge/processes/clickup/spaces/
```

### Auto-sync key decision:
```
Assistant and user decide on naming convention
→ Syncs to knowledge/learnings/general.md
```

### Manual sync request:
```
User: "Remember that we always use feature branches"
→ Assistant syncs to knowledge/processes/general.md
```

---

## Configuration

The skill uses these environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `KNOWLEDGE_BASE_PATH` | `~/ai-workspace/knowledge` | Knowledge base root |

---

Base directory: `skills/core/nanlabs-workspace-knowledge-sync` (in this repo) or the agent-local install path after `npx skills@1.5.23 add`
