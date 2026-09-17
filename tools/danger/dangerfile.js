const { danger, fail, markdown, message, warn } = require("danger");

/**
 * Danger JS rules for nanlabs/agent-toolkit.
 * Aligned with internal-workstation / internal-nan-tools patterns and this
 * repository's .github/PULL_REQUEST_TEMPLATE.md.
 *
 * Plain JS so Danger does not need to transpile TypeScript at runtime
 * (avoids intermittent `ts.transpileModule is not a function` on CI).
 */

const SMALL_PR_FILES = 25;
const SMALL_PR_LINES = 800;

const templateSections = [
  "## Description",
  "## Type of Change",
  "## Public-repo checklist",
  "## How Has This Been Tested?",
  "## Checklist",
];

const publicRepoChecklist = [
  "No secrets, tokens, private URLs, or client data",
  "New skills/plugins marked public-safe (see `docs/PUBLIC_CONTENT_POLICY.md`)",
  "Manifests still validate (`python3 scripts/validate-manifests.py`)",
];

const skillAgentChecklist = [
  "Not a duplicate of an existing catalog skill or agent",
  "Pack membership recorded in `catalogs/pack-catalog.yaml` (or N/A)",
  "Handoff / output contract documented (or N/A; see `docs/HANDOFFS.md`)",
  "Cloud-safe as skills-only (or documented Code/Cursor-only)",
  "`docs/PUBLIC_CONTENT_POLICY.md` satisfied",
];

const agentPluginsChecklist = [
  "Root `plugin.json` is closed-schema v1 (`$schema` + `name`; no `skills`/`agents` path fields)",
  "Plugin skills are immediate `plugins/<id>/skills/<name>/SKILL.md` (not nested groups)",
  "Packs were not given a `plugin.json` (`python3 scripts/validate-agent-plugins.py`)",
];

const prBody = danger.github.pr.body ?? "";
const prTitle = danger.github.pr.title ?? "";
const releasePrTitle =
  /^(version packages|chore: version packages|chore\(release\):|chore: release\b)/i;

const hasIssueReference = (text) => {
  const cleaned = text.replace(/```[\s\S]*?```/g, "").replace(/#ISSUE\b/gi, "");
  const issueReference =
    /\b(?:closes|fixes|resolves|refs|see|related to|part of)\s+(?:#\d+|https:\/\/github\.com\/[\w.-]+\/[\w.-]+\/issues\/\d+)|(?<![#\w])#\d+\b/gim;
  return issueReference.test(cleaned);
};

/** Match "## Section" and emoji variants like "## 📑 Description". */
const hasSection = (section) => {
  const heading = section.replace(/^##\s+/, "");
  const escaped = heading.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return new RegExp(`^##\\s+(?:\\S+\\s+)?${escaped}\\s*$`, "m").test(prBody);
};

const isChecklistItemChecked = (item) => prBody.includes(`- [x] ${item}`);

const isIssueReferenceExempt =
  danger.github.pr.user.login.endsWith("[bot]") ||
  danger.github.pr.user.login.startsWith("app/") ||
  releasePrTitle.test(prTitle);

if (!prBody.trim()) {
  fail(
    ":clipboard: Missing Summary — add a `## Description` section explaining why this change exists.",
  );
}

if (!prTitle.trim()) {
  fail(":id: Missing PR Title — please add a clear title.");
}

if (
  !isIssueReferenceExempt &&
  !hasIssueReference(prBody) &&
  !hasIssueReference(prTitle)
) {
  fail(
    "This PR does not reference an issue. Link it with `Closes #N` or `Refs #N` in the description.",
  );
}

templateSections.forEach((section) => {
  if (!hasSection(section)) {
    fail(
      `:clipboard: Missing section — include <i>${section}</i> (see \`.github/PULL_REQUEST_TEMPLATE.md\`).`,
    );
  }
});

publicRepoChecklist.forEach((item) => {
  if (!isChecklistItemChecked(item)) {
    warn(`:lock: Public-repo checklist — please confirm: <i>${item}</i>`);
  }
});

const touchedFiles = danger.git.created_files.concat(danger.git.modified_files);
const additions = danger.github.pr.additions ?? 0;
const deletions = danger.github.pr.deletions ?? 0;
const totalChanges = additions + deletions;
const fileCount = touchedFiles.length;

if (totalChanges > SMALL_PR_LINES) {
  warn(`This PR changes more than ${SMALL_PR_LINES} lines (${totalChanges}).`);
}
if (fileCount > SMALL_PR_FILES) {
  warn(`This PR touches more than ${SMALL_PR_FILES} files (${fileCount}).`);
}
if (totalChanges <= SMALL_PR_LINES && fileCount <= SMALL_PR_FILES) {
  message("Thanks! We :heart: focused PRs.");
}

const hasDocs = touchedFiles.some(
  (f) =>
    f.startsWith("docs/") ||
    f === "README.md" ||
    f === "CONTRIBUTING.md" ||
    f === "AGENTS.md",
);
if (hasDocs) {
  message("Thanks for updating documentation! :books:");
}

const hasSkills = touchedFiles.some((f) => f.startsWith("skills/"));
const hasAgents = touchedFiles.some((f) => f.startsWith("agents/"));
if (hasSkills || hasAgents) {
  message(
    "Skills/agents changed — remember `docs/PUBLIC_CONTENT_POLICY.md`, `docs/CONTRIBUTION.md`, and `python3 scripts/validate-skills.py` / `validate-pack-catalog.py`.",
  );
  if (!hasSection("## Skill / Agent checklist")) {
    warn(
      ":clipboard: Skill/Agent checklist — include <i>## Skill / Agent checklist</i> when changing skills or agents.",
    );
  }
  skillAgentChecklist.forEach((item) => {
    if (!isChecklistItemChecked(item)) {
      warn(`:mag: Skill/Agent checklist — please confirm: <i>${item}</i>`);
    }
  });
}

const hasManifests = touchedFiles.some(
  (f) =>
    f.includes("marketplace.json") ||
    f.includes("plugin.json") ||
    f.startsWith("catalogs/"),
);
if (hasManifests) {
  message("Manifest/catalog changes — run `python3 scripts/validate-manifests.py`.");
}

const allTouched = [...touchedFiles, ...danger.git.deleted_files];
const hasAgentPlugins = allTouched.some(
  (f) =>
    f.startsWith("plugins/") ||
    f.startsWith("schemas/agent-plugins/") ||
    f === "scripts/validate-agent-plugins.py" ||
    f === "scripts/gen-copilot-surfaces.py",
);
if (hasAgentPlugins) {
  warn(
    "Agent Plugins files changed — keep root `plugin.json` closed-schema and skills as immediate `plugins/<id>/skills/<name>/SKILL.md` ([spec §7.1](https://agent-plugins.org/specification#71-skills)). Packs are not plugins. Run `python3 scripts/validate-agent-plugins.py`.",
  );
  if (!hasSection("## Agent Plugins checklist")) {
    warn(
      ":clipboard: Agent Plugins checklist — include <i>## Agent Plugins checklist</i> when changing `plugins/`.",
    );
  }
  agentPluginsChecklist.forEach((item) => {
    if (!isChecklistItemChecked(item)) {
      warn(`:package: Agent Plugins checklist — please confirm: <i>${item}</i>`);
    }
  });
}

const modifiedAnyPackageJson = allTouched.some((f) => f.endsWith("package.json"));
const modifiedLockfile = allTouched.some((f) => f.endsWith("pnpm-lock.yaml"));
if (modifiedLockfile && !modifiedAnyPackageJson) {
  fail(
    "A `pnpm-lock.yaml` changed without a matching `package.json` update. Revert the lockfile or add the dependency change.",
  );
}
if (modifiedAnyPackageJson && !modifiedLockfile) {
  warn(
    "`package.json` changed — ensure the corresponding `pnpm-lock.yaml` is updated.",
  );
}

markdown(`## PR stats

| Metric | Value |
| --- | --- |
| Lines added | ${additions} |
| Lines removed | ${deletions} |
| Files changed | ${fileCount} |`);
