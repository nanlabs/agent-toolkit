# Slack MCP

Official hosted MCP (Streamable HTTP + OAuth).

- Endpoint: `https://mcp.slack.com/mcp`
- Docs: https://docs.slack.dev/ai/slack-mcp-server/
- Plugin: `nanlabs-integrations` (`mcp.json`)

Slack does **not** support Dynamic Client Registration. Workspace admins must
approve MCP. If the client cannot complete OAuth from URL-only config, install
Slack’s own MCP plugin for that client (it binds Slack’s registered OAuth app).

Bot/app tokens do not belong in plugin config.
