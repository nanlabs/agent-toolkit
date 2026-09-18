#!/usr/bin/env python3
"""Render human-facing catalog tables from YAML/JSON sources of truth.

Imported by gen-surfaces.py so CI --check fails when README/wiki/docs drift.
Do not hand-edit files under docs/generated/.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "docs" / "generated"
REPO_BLOB = "https://github.com/nanlabs/agent-toolkit/blob/main"

GROUP_PLUGIN_ORDER = [
    "nanlabs-core",
    "nanlabs-data",
    "nanlabs-delivery",
    "nanlabs-design",
    "nanlabs-forge",
    "nanlabs-integrations",
    "nanlabs-ops",
    "nanlabs-tooling",
    "nanlabs-workflow",
    "nanlabs-agents",
]


def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def plugin_ids(products: dict[str, Any]) -> list[str]:
    ids = list((products.get("plugins") or {}).keys())
    ordered = [pid for pid in GROUP_PLUGIN_ORDER if pid in ids]
    extra = [pid for pid in ids if pid not in ordered]
    return ordered + extra


def skill_count(layout_groups: dict[str, list[str]]) -> int:
    return sum(len(names) for names in layout_groups.values())


def mcp_for_plugin(plugin_id: str, mcp_catalog: dict[str, dict[str, Any]]) -> list[str]:
    names = [
        name
        for name, cfg in mcp_catalog.items()
        if str(cfg.get("plugin")) == plugin_id
    ]
    return sorted(names)


def counts(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
    agent_count: int,
) -> dict[str, int]:
    return {
        "skills": skill_count(layout_groups),
        "agents": agent_count,
        "plugins": len(products.get("plugins") or {}),
        "mcp": len(mcp_catalog),
    }


def plugins_table(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "| Plugin | Version | Skills | MCP | Role |",
        "| --- | --- | --- | --- | --- |",
    ]
    plugins = products.get("plugins") or {}
    for plugin_id in plugin_ids(products):
        cfg = plugins[plugin_id]
        version = str(cfg.get("version") or "")
        group = cfg.get("skills_group")
        n_skills = len(layout_groups.get(str(group), [])) if group else 0
        skills_cell = str(n_skills) if n_skills else "—"
        mcp_names = mcp_for_plugin(plugin_id, mcp_catalog)
        mcp_cell = ", ".join(f"`{n}`" for n in mcp_names) if mcp_names else "—"
        role = str(cfg.get("description") or "").strip()
        if plugin_id == "nanlabs-core":
            role = "Recommended first install. Setup doctor + `/nanlabs-core:setup`."
        elif plugin_id == "nanlabs-agents":
            role = "Optional. Full 18-persona roster."
        lines.append(
            f"| `{plugin_id}` | {version} | {skills_cell} | {mcp_cell} | {role} |"
        )
    return "\n".join(lines) + "\n"


def mcp_table(mcp_catalog: dict[str, dict[str, Any]]) -> str:
    lines = [
        "| Server | Plugin | Official URL | Notes |",
        "| --- | --- | --- | --- |",
    ]
    for name in sorted(mcp_catalog):
        cfg = mcp_catalog[name]
        plugin = cfg.get("plugin")
        url = cfg.get("url")
        notes = str(cfg.get("notes") or "").replace("\n", " ").strip()
        products = cfg.get("products")
        if isinstance(products, list) and products:
            notes = f"Covers {', '.join(str(p) for p in products)}. " + notes
        lines.append(
            f"| `{name}` | `{plugin}` | `{url}` | {notes} |"
        )
    return "\n".join(lines) + "\n"


def skills_table(layout_groups: dict[str, list[str]]) -> str:
    lines = [
        "| Group | Plugin | Count | Skills |",
        "| --- | --- | --- | --- |",
    ]
    for group, names in layout_groups.items():
        skill_list = ", ".join(f"`{n}`" for n in names)
        lines.append(
            f"| `{group}` | `nanlabs-{group}` | {len(names)} | {skill_list} |"
        )
    return "\n".join(lines) + "\n"


def claude_install(ids: list[str]) -> str:
    lines = ["/plugin marketplace add nanlabs/agent-toolkit"]
    lines.extend(f"/plugin install {pid}@nanlabs-agent-toolkit" for pid in ids)
    lines.append("/nanlabs-core:setup")
    return "\n".join(lines) + "\n"


def copilot_install(ids: list[str]) -> str:
    return (
        "\n".join(
            f"copilot plugin install nanlabs/agent-toolkit:plugins/{pid}"
            for pid in ids
        )
        + "\n"
    )


def cursor_install(ids: list[str]) -> str:
    lines = [
        "mkdir -p ~/.cursor/plugins/local",
        "REPO=/path/to/agent-toolkit",
    ]
    lines.extend(
        f'ln -sfn "$REPO/plugins/{pid}" ~/.cursor/plugins/local/{pid}' for pid in ids
    )
    return "\n".join(lines) + "\n"


def generated_catalog_page(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
    agent_count: int,
) -> str:
    ids = plugin_ids(products)
    n = counts(products, layout_groups, mcp_catalog, agent_count)
    meta_version, _ = _marketplace_meta(products)
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# Catalog (generated)\n"
        "\n"
        "Source of truth: [`products/plugins.yaml`](../../products/plugins.yaml), "
        "[`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml), "
        "[`catalogs/skills-layout.json`](../../catalogs/skills-layout.json).\n"
        "\n"
        f"Marketplace metadata **{meta_version}**. "
        f"**{n['plugins']}** plugins · **{n['skills']}** skills · "
        f"**{n['agents']}** agents · **{n['mcp']}** official MCP servers.\n"
        "\n"
        "## Plugins\n"
        "\n"
        + plugins_table(products, layout_groups, mcp_catalog)
        + "\n## Official MCP\n"
        "\n"
        "Authenticate in the client (OAuth). Plugins never contain tokens.\n"
        "\n"
        + mcp_table(mcp_catalog)
        + "\n## Skills by group\n"
        "\n"
        + skills_table(layout_groups)
        + "\n## Complete install\n"
        "\n"
        "### Claude Code\n"
        "\n"
        "```text\n"
        + claude_install(ids)
        + "```\n"
        "\n"
        "### GitHub Copilot CLI\n"
        "\n"
        "```bash\n"
        + copilot_install(ids)
        + "```\n"
        "\n"
        "### Cursor IDE (local)\n"
        "\n"
        "```bash\n"
        + cursor_install(ids)
        + "```\n"
        "\n"
        "Reload Cursor after the symlinks exist.\n"
    )


def _marketplace_meta(products: dict[str, Any]) -> tuple[str, str]:
    meta = (products.get("marketplace") or {}).get("metadata") or {}
    version = meta.get("version")
    description = meta.get("description")
    if not isinstance(version, str) or not version.strip():
        fail("products/plugins.yaml: marketplace.metadata.version required")
    if not isinstance(description, str) or not description.strip():
        fail("products/plugins.yaml: marketplace.metadata.description required")
    return version, description


def wiki_plugin_marketplace(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
) -> str:
    ids = plugin_ids(products)
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# Plugin marketplace\n"
        "\n"
        "Catalogs: [Claude](https://github.com/nanlabs/agent-toolkit/blob/main/.claude-plugin/marketplace.json) · "
        "[Cursor](https://github.com/nanlabs/agent-toolkit/blob/main/.cursor-plugin/marketplace.json) · "
        "[ChatGPT/Codex](https://github.com/nanlabs/agent-toolkit/blob/main/.agents/plugins/marketplace.json).\n"
        "\n"
        "Version source of truth: [`products/plugins.yaml`](https://github.com/nanlabs/agent-toolkit/blob/main/products/plugins.yaml). "
        "Regenerate with `python3 scripts/gen-surfaces.py`.\n"
        "\n"
        "## Plugins\n"
        "\n"
        + plugins_table(products, layout_groups, mcp_catalog)
        + "\n"
        "Deprecated: standalone `nanlabs-setup` (not listed in the marketplace). "
        "Setup ships inside `nanlabs-core`.\n"
        "\n"
        "## Complete install\n"
        "\n"
        "### Claude Code\n"
        "\n"
        "```text\n"
        + claude_install(ids)
        + "```\n"
        "\n"
        "### GitHub Copilot CLI\n"
        "\n"
        "```bash\n"
        + copilot_install(ids)
        + "```\n"
        "\n"
        "### Cursor IDE\n"
        "\n"
        "Team Marketplace import of `nanlabs/agent-toolkit`, or local symlinks:\n"
        "\n"
        "```bash\n"
        + cursor_install(ids)
        + "```\n"
        "\n"
        "Cursor Agent CLI: `agent plugin marketplace add` registers the catalog; "
        "use `--plugin-dir` for local load. See [Cursor Agent CLI](Cursor-Agent-CLI).\n"
        "\n"
        "## Building / validating\n"
        "\n"
        "```bash\n"
        "python3 scripts/gen-surfaces.py\n"
        "python3 scripts/gen-surfaces.py --check\n"
        "python3 scripts/validate-manifests.py\n"
        "```\n"
    )


def wiki_skills_reference(layout_groups: dict[str, list[str]]) -> str:
    n = skill_count(layout_groups)
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# Skills reference\n"
        "\n"
        f"{n} public skills under `plugins/nanlabs-<group>/skills/<skill>/SKILL.md` "
        "([Agent Skills](https://agentskills.io/specification)).\n"
        "\n"
        f"Machine catalog: [`catalogs/skill-catalog.yaml`]({REPO_BLOB}/catalogs/skill-catalog.yaml) · "
        f"packs: [`docs/PACKS.md`]({REPO_BLOB}/docs/PACKS.md) · "
        f"human index: [`docs/SKILLS.md`]({REPO_BLOB}/docs/SKILLS.md).\n"
        "\n"
        "## Groups\n"
        "\n"
        + skills_table(layout_groups)
        + "\n"
        "## Install\n"
        "\n"
        "```bash\n"
        "npx skills add nanlabs/agent-toolkit -g\n"
        "npx skills add nanlabs/agent-toolkit/plugins/nanlabs-delivery/skills\n"
        "```\n"
        "\n"
        "Or install the matching **group plugin** (see [Plugin Marketplace](Plugin-Marketplace)). "
        "Skills-only does **not** register MCP or agents.\n"
        "\n"
        "## Not shipped here\n"
        "\n"
        "| Name | Notes |\n"
        "| --- | --- |\n"
        "| Some Figma opt-in packs | Documented as related; not in this tree |\n"
        "| Jira/Confluence assistants | Use the Atlassian MCP on `nanlabs-integrations` |\n"
        "\n"
        f"Authoring: [`docs/AUTHORING.md`]({REPO_BLOB}/docs/AUTHORING.md).\n"
    )


def wiki_mcp_setup(mcp_catalog: dict[str, dict[str, Any]]) -> str:
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# Official MCP servers\n"
        "\n"
        f"Catalog: [`catalogs/mcp-catalog.yaml`]({REPO_BLOB}/catalogs/mcp-catalog.yaml). "
        f"Templates: [`mcp/templates/`]({REPO_BLOB}/mcp/templates).\n"
        "\n"
        "Installing **`nanlabs-design`**, **`nanlabs-forge`**, or **`nanlabs-integrations`** "
        "registers these hosted servers. Authenticate in the client (OAuth). "
        "Plugins never contain tokens.\n"
        "\n"
        "`nanlabs-core` / `nanlabs-agents` do **not** ship MCP. "
        "Skills-only (`npx skills`) does not either.\n"
        "\n"
        "## What ships where\n"
        "\n"
        + mcp_table(mcp_catalog)
        + "\n"
        "Jira and Confluence are **one** Atlassian Rovo MCP, not two URLs.\n"
        "\n"
        "## Client files\n"
        "\n"
        "| Client | File | Transport field |\n"
        "| --- | --- | --- |\n"
        "| Agent Plugins / Cursor / Copilot | `plugins/<id>/mcp.json` | `type: streamable-http` |\n"
        "| Claude Code | `plugins/<id>/.mcp.json` | `type: http` |\n"
        "\n"
        "After install: reload the client, then complete the browser OAuth prompt. "
        "Slack workspace admins must approve MCP; if URL-only OAuth fails, use Slack’s "
        "own MCP plugin for that client.\n"
        "\n"
        "If you already have ClickUp / Shortcut / Linear in `~/.cursor/mcp.json`, "
        "the plugin copies may duplicate those servers — keep one of each.\n"
        "\n"
        "Official vendor docs live in each [`mcp/templates/<name>/README.md`]("
        f"{REPO_BLOB}/mcp/templates).\n"
    )


def docs_skills_md(layout_groups: dict[str, list[str]]) -> str:
    n = skill_count(layout_groups)
    return (
        "> [!NOTE]\n"
        "> 📘 **Repo-Only Doc** — generated by `scripts/gen-surfaces.py`\n"
        ">\n"
        "> Skill bodies are canonical under `plugins/nanlabs-<group>/skills/`.\n"
        "\n"
        "---\n"
        "\n"
        "# Skills index\n"
        "\n"
        f"{n} public skills follow the [Agent Skills](https://agentskills.io/specification) "
        "format (`SKILL.md`).\n"
        "\n"
        "Install: [`npx skills`](https://github.com/vercel-labs/skills) — "
        "`npx skills add nanlabs/agent-toolkit -g`\n"
        "Group plugin or domain pack: [`PACKS.md`](PACKS.md)\n"
        "Catalog: [`catalogs/skill-catalog.yaml`](../catalogs/skill-catalog.yaml)\n"
        "Authoring: [`AUTHORING.md`](AUTHORING.md)\n"
        "\n"
        "Each group plugin **is** the portable [Agent Plugins](https://agent-plugins.org/specification) "
        "package (`plugin.json` + immediate `skills/<name>/`). See [`AGENT_PLUGINS.md`](AGENT_PLUGINS.md).\n"
        "\n"
        "## Bundled groups\n"
        "\n"
        + skills_table(layout_groups)
        + "\n"
        "## Opt-in / not bundled here\n"
        "\n"
        "These appear in skill docs as related capabilities but are **not** shipped in "
        "this repository (yet). Install or provision them separately when needed.\n"
        "\n"
        "| Name | Kind | Notes |\n"
        "| --- | --- | --- |\n"
        "| `figma-use` | opt-in pack | Figma Plugin API / canvas writes |\n"
        "| `figma-generate-design` | opt-in pack | Full-screen generation in Figma; needs `figma-use` |\n"
        "| `figma-generate-library` | opt-in pack | Library generate/import |\n"
        "| `nanlabs-e2e-runner` | agent | Playwright **test** authoring (agents wave) |\n"
        "| `jira-assistant` / `confluence-assistant` | MCP | Use Atlassian Rovo MCP on `nanlabs-integrations` |\n"
        "\n"
        "When a skill mentions one of the above, treat the name as a pointer — do not "
        "expect a sibling `../<name>/SKILL.md` in this repo.\n"
    )


def mcp_templates_readme(mcp_catalog: dict[str, dict[str, Any]]) -> str:
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# MCP templates\n"
        "\n"
        "Official hosted MCP endpoints, documented here and **shipped** in the matching "
        "group plugin (`mcp.json` + `.mcp.json`). Source of truth: "
        "[`catalogs/mcp-catalog.yaml`](../../catalogs/mcp-catalog.yaml).\n"
        "\n"
        "Installing `nanlabs-design`, `nanlabs-forge`, or `nanlabs-integrations` "
        "registers these servers. The user authenticates in the client (OAuth). Plugins "
        "never contain tokens.\n"
        "\n"
        + mcp_table(mcp_catalog)
        + "\n"
        "Agent Plugins portable config uses `type: streamable-http`. Claude Code native "
        "`.mcp.json` uses `type: http` with the same URL. Auth is client-managed — see "
        "[Agent Plugins MCP](https://agent-plugins.org/plugin-authors/mcp-servers).\n"
        "\n"
        "Skills-only (`npx skills`) does **not** install MCP. `clickup-cli` / `gh` remain "
        "available as CLI alternatives.\n"
    )


def generated_index(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
    agent_count: int,
) -> str:
    n = counts(products, layout_groups, mcp_catalog, agent_count)
    return (
        "<!-- Generated by scripts/gen-surfaces.py. Do not edit. -->\n"
        "\n"
        "# Generated catalog docs\n"
        "\n"
        "These files are assembled from YAML/JSON catalogs. Edit the catalogs, then run "
        "`python3 scripts/gen-surfaces.py`.\n"
        "\n"
        f"| Metric | Count |\n"
        f"| --- | --- |\n"
        f"| Plugins | {n['plugins']} |\n"
        f"| Skills | {n['skills']} |\n"
        f"| Agents | {n['agents']} |\n"
        f"| Official MCP servers | {n['mcp']} |\n"
        "\n"
        "| File | Contents |\n"
        "| --- | --- |\n"
        "| [catalog.md](catalog.md) | Plugins + MCP + skills + complete install |\n"
        "\n"
        "Wiki pages `Plugin-Marketplace.md`, `Skills-Reference.md`, and `MCP-Setup.md` "
        "are generated from the same sources.\n"
    )


def replace_region(text: str, name: str, body: str, path: Path) -> str:
    start = f"<!-- generated:{name} -->"
    end = f"<!-- /generated:{name} -->"
    if start not in text or end not in text:
        fail(f"{path.relative_to(ROOT)}: missing region markers {start} … {end}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    inner = body.strip("\n")
    return f"{before}{start}\n{inner}\n{end}{after}"


def readme_regions(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
    agent_count: int,
) -> dict[str, str]:
    ids = plugin_ids(products)
    n = counts(products, layout_groups, mcp_catalog, agent_count)
    badges = (
        f'  <img src="https://img.shields.io/badge/skills-{n["skills"]}-ff6b35" alt="{n["skills"]} skills"/>\n'
        f'  <img src="https://img.shields.io/badge/agents-{n["agents"]}-58a6ff" alt="{n["agents"]} agents"/>\n'
        f'  <img src="https://img.shields.io/badge/plugins-{n["plugins"]}-f7c948" alt="{n["plugins"]} plugins"/>\n'
        f'  <img src="https://img.shields.io/badge/MCP-{n["mcp"]}%20official-7ee787" alt="{n["mcp"]} official MCP"/>'
    )
    return {
        "badges": badges,
        "plugins": plugins_table(products, layout_groups, mcp_catalog),
        "mcp": mcp_table(mcp_catalog),
        "claude-install": "```text\n" + claude_install(ids) + "```\n",
        "copilot-install": "```bash\n" + copilot_install(ids) + "```\n",
        "cursor-install": "```bash\n" + cursor_install(ids) + "```\n",
    }


def write_text(path: Path, expected: str, *, check: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if check:
        if not path.is_file():
            fail(f"missing {path.relative_to(ROOT)} — run scripts/gen-surfaces.py")
        current = path.read_text(encoding="utf-8")
        if current != expected:
            fail(f"drift: {path.relative_to(ROOT)}")
        return
    path.write_text(expected, encoding="utf-8")
    print(f"synced {path.relative_to(ROOT)}")


def sync_catalog_docs(
    products: dict[str, Any],
    layout_groups: dict[str, list[str]],
    mcp_catalog: dict[str, dict[str, Any]],
    agent_count: int,
    *,
    check: bool,
) -> None:
    expected_files = {
        GENERATED / "README.md": generated_index(
            products, layout_groups, mcp_catalog, agent_count
        ),
        GENERATED / "catalog.md": generated_catalog_page(
            products, layout_groups, mcp_catalog, agent_count
        ),
        ROOT / "docs" / "wiki" / "Plugin-Marketplace.md": wiki_plugin_marketplace(
            products, layout_groups, mcp_catalog
        ),
        ROOT / "docs" / "wiki" / "Skills-Reference.md": wiki_skills_reference(
            layout_groups
        ),
        ROOT / "docs" / "wiki" / "MCP-Setup.md": wiki_mcp_setup(mcp_catalog),
        ROOT / "docs" / "SKILLS.md": docs_skills_md(layout_groups),
        ROOT / "mcp" / "templates" / "README.md": mcp_templates_readme(mcp_catalog),
    }
    for path, text in expected_files.items():
        write_text(path, text, check=check)

    readme_path = ROOT / "README.md"
    if not readme_path.is_file():
        fail("missing README.md")
    current = readme_path.read_text(encoding="utf-8")
    regions = readme_regions(products, layout_groups, mcp_catalog, agent_count)
    updated = current
    for name, body in regions.items():
        updated = replace_region(updated, name, body, readme_path)
    if check:
        if updated != current:
            fail("drift: README.md generated regions — run scripts/gen-surfaces.py")
        return
    if updated != current:
        readme_path.write_text(updated, encoding="utf-8")
        print("synced README.md generated regions")
