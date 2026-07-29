---
name: figma-create-design-system-rules
description: Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.
---

# Create Design System Rules

## Overview

This skill helps you generate custom design system rules tailored to your project's specific needs. These rules guide AI coding agents to produce consistent, high-quality code when implementing Figma designs, ensuring that your team's conventions, component patterns, and architectural decisions are followed automatically.

### Supported Rule Files

| Agent | Rule File |
|-------|-----------|
| Claude Code | `AGENTS.md` (or `CLAUDE.md` symlink) |
| opencode | `AGENTS.md` (or `CLAUDE.md` symlink) |
| Cursor | `.cursor/rules/figma-design-system.mdc` |
| Gemini CLI | `GEMINI.md` (or symlink to `AGENTS.md`) |
| GitHub Copilot | `.github/copilot-instructions.md` (or symlink to `AGENTS.md`) |
| Windsurf | `.windsurfrules` |

> NaNLABS convention: prefer a single `AGENTS.md` and symlink the tool-specific
> files to it. See the workstation `AGENTS.md` portability table for details.

## What Are Design System Rules?

Design system rules are project-level instructions that encode the "unwritten knowledge" of your codebase - the kind of expertise that experienced developers know and would pass on to new team members:

- Which layout primitives and components to use
- Where component files should be located
- How components should be named and structured
- What should never be hardcoded
- How to handle design tokens and styling
- Project-specific architectural patterns

Once defined, these rules dramatically reduce repetitive prompting and ensure consistent output across all Figma implementation tasks.

## Prerequisites

- Figma MCP server must be connected and accessible
- Access to the project codebase for analysis
- Understanding of your team's component conventions (or willingness to establish them)

## When to Use This Skill

Use this skill when:

- Starting a new project that will use Figma designs
- Onboarding an AI coding agent to an existing project with established patterns
- Standardizing Figma-to-code workflows across your team
- Updating or refining existing design system conventions
- Users explicitly request: "create design system rules", "set up Figma guidelines", "customize rules for my project"

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Run the Create Design System Rules Tool

Call the Figma MCP server's `create_design_system_rules` tool to get the foundational prompt and template.

**Parameters:**

- `clientLanguages`: Comma-separated list of languages used in the project (e.g., "typescript,javascript", "python", "javascript")
- `clientFrameworks`: Framework being used (e.g., "react", "vue", "svelte", "angular", "unknown")

This tool returns guidance and a template for creating design system rules.

Structure your design system rules following the template format provided in the tool's response.

## Reference files

| Topic | File |
| --- | --- |
| Codebase analysis and rule templates | `references/workflow-detail.md` |
| Examples and troubleshooting | `references/examples.md` |
