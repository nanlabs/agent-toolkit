# Atlassian Rovo MCP (Jira + Confluence)

Official hosted MCP v2. One server covers Jira, Confluence, Jira Service
Management, Bitbucket Cloud, Loom, and related Atlassian products.

- Endpoint: `https://mcp.atlassian.com/v2/mcp`
- Docs: [official setup](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/)
- Plugin: `nanlabs-integrations` (`mcp.json`)

OAuth 2.1 is the recommended auth. There are not separate Jira vs Confluence
MCP URLs — both go through this endpoint.
