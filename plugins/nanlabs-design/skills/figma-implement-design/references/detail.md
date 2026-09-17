## Implementation Rules

### Component Organization

- Place UI components in the project's designated design system directory
- Follow the project's component naming conventions
- Avoid inline styles unless truly necessary for dynamic values

### Design System Integration

- ALWAYS use components from the project's design system when possible
- Map Figma design tokens to project design tokens
- When a matching component exists, extend it rather than creating a new one
- Document any new components added to the design system

### Code Quality

- Avoid hardcoded values - extract to constants or design tokens
- Keep components composable and reusable
- Add TypeScript types for component props
- Include JSDoc comments for exported components

## Examples

### Example 1: Implementing a Button Component

User says: "Implement this Figma button component: https://figma.com/design/kL9xQn2VwM8pYrTb4ZcHjF/DesignSystem?node-id=42-15"

**Actions:**

1. Parse URL to extract fileKey=`kL9xQn2VwM8pYrTb4ZcHjF` and nodeId=`42-15`
2. Run `get_design_context(fileKey="kL9xQn2VwM8pYrTb4ZcHjF", nodeId="42-15")`
3. Run `get_screenshot(fileKey="kL9xQn2VwM8pYrTb4ZcHjF", nodeId="42-15")` for visual reference
4. Download any button icons from the assets endpoint
5. Check if project has existing button component
6. If yes, extend it with new variant; if no, create new component using project conventions
7. Map Figma colors to project design tokens (e.g., `primary-500`, `primary-hover`)
8. Validate against screenshot for padding, border radius, typography

**Result:** Button component matching Figma design, integrated with project design system.

### Example 2: Building a Dashboard Layout

User says: "Build this dashboard: https://figma.com/design/pR8mNv5KqXzGwY2JtCfL4D/Dashboard?node-id=10-5"

**Actions:**

1. Parse URL to extract fileKey=`pR8mNv5KqXzGwY2JtCfL4D` and nodeId=`10-5`
2. Run `get_metadata(fileKey="pR8mNv5KqXzGwY2JtCfL4D", nodeId="10-5")` to understand the page structure
3. Identify main sections from metadata (header, sidebar, content area, cards) and their child node IDs
4. Run `get_design_context(fileKey="pR8mNv5KqXzGwY2JtCfL4D", nodeId=":childNodeId")` for each major section
5. Run `get_screenshot(fileKey="pR8mNv5KqXzGwY2JtCfL4D", nodeId="10-5")` for the full page
6. Download all assets (logos, icons, charts)
7. Build layout using project's layout primitives
8. Implement each section using existing components where possible
9. Validate responsive behavior against Figma constraints

**Result:** Complete dashboard matching Figma design with responsive layout.

## Best Practices

### Always Start with Context

Never implement based on assumptions. Always fetch `get_design_context` and `get_screenshot` first.

### Incremental Validation

Validate frequently during implementation, not just at the end. This catches issues early.

### Document Deviations

If you must deviate from the Figma design (e.g., for accessibility or technical constraints), document why in code comments.

### Reuse Over Recreation

Always check for existing components before creating new ones. Consistency across the codebase is more important than exact Figma replication.

### Design System First

When in doubt, prefer the project's design system patterns over literal Figma translation.

## Common Issues and Solutions

### Issue: Figma output is truncated

**Cause:** The design is too complex or has too many nested layers to return in a single response.
**Solution:** Use `get_metadata` to get the node structure, then fetch specific nodes individually with `get_design_context`.

### Issue: Design doesn't match after implementation

**Cause:** Visual discrepancies between the implemented code and the original Figma design.
**Solution:** Compare side-by-side with the screenshot from Step 3. Check spacing, colors, and typography values in the design context data.

### Issue: Assets not loading

**Cause:** The Figma MCP server's assets endpoint is not accessible or the URLs are being modified.
**Solution:** Verify the Figma MCP server's assets endpoint is accessible. The server serves assets at `localhost` URLs. Use these directly without modification.

### Issue: Design token values differ from Figma

**Cause:** The project's design system tokens have different values than those specified in the Figma design.
**Solution:** When project tokens differ from Figma values, prefer project tokens for consistency but adjust spacing/sizing to maintain visual fidelity.

## Understanding Design Implementation

The Figma implementation workflow establishes a reliable process for translating designs to code:

**For designers:** Confidence that implementations will match their designs with pixel-perfect accuracy.
**For developers:** A structured approach that eliminates guesswork and reduces back-and-forth revisions.
**For teams:** Consistent, high-quality implementations that maintain design system integrity.

By following this workflow, you ensure that every Figma design is implemented with the same level of care and attention to detail.

## Additional Resources

- [Figma MCP Server Documentation](https://developers.figma.com/docs/figma-mcp-server/)
- [Figma MCP Server Tools and Prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
- [Figma Variables and Design Tokens](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma)
