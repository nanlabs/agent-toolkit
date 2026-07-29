---
name: figma-code-connect-components
description: Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes (Plugin API), install the opt-in `figma-use` pack documented in `docs/SKILLS.md`.
---

# Code Connect Components

## Overview

This skill helps you connect Figma design components to their corresponding code implementations using Figma's Code Connect feature. It analyzes the Figma design structure, searches your codebase for matching components, and establishes mappings that maintain design-code consistency.

## Skill Boundaries

- Use this skill for `get_code_connect_suggestions` + `send_code_connect_mappings` workflows.
- If the task requires writing to the Figma canvas with Plugin API scripts,
  install the opt-in `figma-use` pack (see `docs/SKILLS.md`).
- If the task is building or updating a full-page screen in Figma from code or a description, use the opt-in `figma-generate-design` pack (see `docs/SKILLS.md`); it is not bundled in this repo.
- If the task is implementing product code from Figma, switch to [figma-implement-design](../figma-implement-design/SKILL.md).

## Prerequisites

- Figma MCP server must be connected and accessible
- User must provide a Figma URL with node ID: `https://figma.com/design/:fileKey/:fileName?node-id=1-2`
  - **IMPORTANT:** The Figma URL must include the `node-id` parameter. Code Connect mapping will fail without it.
- **OR** when using `figma-desktop` MCP: User can select a node directly in the Figma desktop app (no URL required)
- **IMPORTANT:** The Figma component must be published to a team library. Code Connect only works with published components or component sets.
- **IMPORTANT:** Code Connect is only available on Organization and Enterprise plans.
- Access to the project codebase for component scanning

## Required workflow (summary)

1. `get_code_connect_suggestions` for unmapped components.
2. Match components in the codebase.
3. `send_code_connect_mappings` to publish mappings.

References: `references/workflow.md` (steps), `references/detail.md` (examples)
