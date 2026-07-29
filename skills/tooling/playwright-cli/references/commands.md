## Sessions

```bash
pwcli --session todo open https://demo.playwright.dev/todomvc
pwcli --session todo snapshot
```

Or set the env var once:

```bash
export PLAYWRIGHT_CLI_SESSION=todo
pwcli open https://demo.playwright.dev/todomvc
```

## Boundaries

- This skill is **read/interact** on real browsers. No test framework, no test
  files. For test suites, hand off to `nanlabs-e2e-runner`.
- When this skill captures artifacts inside a project, write them under
  `output/playwright/` (or whatever the repo defines) — never introduce new
  top-level artifact folders.
- For sandboxed AI tools that block `npx`/network, ask the user to authorize
  outbound network for this skill rather than disabling sandboxing globally.

## References

- [`references/cli.md`](references/cli.md) — CLI command reference.
- [`references/workflows.md`](references/workflows.md) — practical workflows
  and troubleshooting.

## See also

- `nanlabs-e2e-runner` (agent; not bundled here yet) — Playwright **test**
  authoring & execution (different mental model than this skill).
