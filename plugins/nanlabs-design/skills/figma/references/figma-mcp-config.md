# Figma MCP — setup and troubleshooting

The Figma MCP is the official **streamable HTTP** endpoint at
`https://mcp.figma.com/mcp`. Authentication is **OAuth in the client**, not a
personal access token in plugin config.

Installing **`nanlabs-design`** registers this URL (`mcp.json` / `.mcp.json`).
See [`docs/wiki/MCP-Setup.md`](../../../../../docs/wiki/MCP-Setup.md).

## 1) Enable the plugin MCP

1. Install `nanlabs-design`.
2. Reload the client.
3. Complete Figma’s OAuth prompt (Allow Access).

Figma allowlists MCP clients (Cursor, VS Code, Claude Code, and others in
their catalog). Manual equivalent:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Cursor / VS Code: URL `https://mcp.figma.com/mcp` with no Authorization header.

## 2) Verify

1. Restart the AI tool so it re-reads plugin MCP config.
2. Ask the AI to list Figma tools or call `whoami` — it should return your
   Figma user identity.

## Troubleshooting

- **Not connected**: confirm `nanlabs-design` is enabled and complete OAuth.
- **403 / Forbidden**: the client may not be on Figma’s MCP allowlist.
- **Generic / vague output**: re-state the project-specific rules from the
  parent `SKILL.md` and ensure you follow the required flow
  (`get_design_context` → optional `get_metadata` → `get_screenshot`).

## Link-based prompting

The remote Figma MCP server is link-based: copy the Figma frame/layer link and
provide that URL to the AI tool. The AI tool will extract the node ID from the
link (it cannot browse the page itself).
