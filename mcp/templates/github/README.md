# GitHub MCP

Official hosted MCP (Streamable HTTP).

- Endpoint: `https://api.githubcopilot.com/mcp/`
- Docs: [official setup](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- Plugin: `nanlabs-forge` (`mcp.json`)

VS Code / Copilot use OAuth against this URL. Some Cursor versions still ask
for a Personal Access Token in **user** MCP config (`~/.cursor/mcp.json`); do
not put tokens in the plugin.

The local Docker image `ghcr.io/github/github-mcp-server` is an official
alternative, not shipped here.
