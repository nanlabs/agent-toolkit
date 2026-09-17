# Linear MCP

Official hosted MCP (Streamable HTTP + OAuth 2.1).

- Endpoint: `https://mcp.linear.app/mcp`
- Docs: [official setup](https://linear.app/docs/mcp)
- Plugin: `nanlabs-integrations` (`mcp.json`)

No environment variables. The client opens OAuth on first use.

The legacy SSE URL `https://mcp.linear.app/sse` is deprecated. WSL-only
`mcp-remote` fallbacks belong in user config, not in the plugin.
