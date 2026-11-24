---
name: architecture-diagram
description: "Build an interactive, Lucidchart-style architecture diagram of a deployed system as one self-contained HTML page: nested containers (cloud, cluster, namespaces), service boxes with brand icons, numbered flows people can select (user access, operator access over a VPN or tailnet, CI/GitOps deploy, secrets, observability, data), hover details, an inventory table and a 'not there yet' list. Built from the real source of truth (Terraform, Helm, Argo CD, Kubernetes manifests, docker-compose, runbooks), never from guesses. Also exports Mermaid, D2, draw.io, SVG or PNG when the user asks for another format. Use when asked for an architecture diagram, deployment diagram, infrastructure map, 'what is deployed where', network or access flow diagram, or an explainer of an environment for a client, a new engineer or a DevOps handover."
---

# Architecture diagram

Turn a deployed system into a diagram that a client, a new engineer or an incoming DevOps can read in five minutes, and that an operator can still trust in detail.

The default output is one self-contained `.html` file: an SVG canvas drawn from a JSON model, flow buttons that highlight one path at a time, hover cards per component, and explanatory sections below. If the user asks for another format, build the same model and export it (see [references/other-formats.md](references/other-formats.md)).

## When to use

- "Make a diagram of what we have deployed in <environment>."
- "Explain how users / operators / CI reach the cluster."
- "Lucidchart-style diagram with logos", "architecture explainer", "infra map for the handover".
- Any request for a deployment, network, access or data-flow diagram of a real system.

Not for: UI mockups (use `ui-ux-pro-max`), Figma work (use the `figma*` skills), or a diagram of a system that does not exist yet (draw it, but label every box as planned).

## Output contract

| Item | Default |
| --- | --- |
| Format | One `.html` file, no build step for the reader, works offline except web fonts |
| Language | The language the audience reads (ask if the audience differs from the requester) |
| Location | Where the user asks; otherwise a non-tracked folder (never commit it to a client repo unasked) |
| Content | Diagram + flows step by step + inventory + "not there yet" + source line |
| Safety | No IP addresses, account/project IDs, hostnames that are not public, secrets or personal data |

## Workflow

### 1. Collect facts from the source of truth

Read, do not assume. In order of authority:

1. What runs: GitOps apps (Argo CD / Flux Applications), Helm values per environment, Kubernetes manifests, `docker-compose`, serverless configs.
2. What exists around it: Terraform / Pulumi / CloudFormation for the environment (network, cluster, registry, buckets, secret store, IAM, load balancer, DNS).
3. How people get in: ingress and TLS config, auth middleware, VPN / tailnet / bastion docs, operator runbooks.
4. How changes arrive: CI workflows, image registry, deploy keys, OIDC federation.
5. Live state, only with read-only commands and only if the user already gave access (`kubectl get applications`, `kubectl get ns`). Say in the page footer whether it reflects desired state (git) or live state, and the date.

Write down for every component: name, what it does in one sentence, how it is reached, and the file that defines it. Those become the hover card.

**Correct the request when the facts disagree.** If the user says "show the user going through the VPN" and the config shows users on public HTTPS while only operators use the VPN, draw what is true, show both paths, and put a "Read this first" callout at the top explaining the difference. Tell the user in your reply too.

### 2. Model it

Copy [assets/example-model.json](assets/example-model.json) and edit it. The schema is in [references/model-schema.md](references/model-schema.md). In short:

- **containers**: nested regions (cloud account → cluster → namespace; SaaS column; people column).
- **nodes**: one box per component, with an icon, title, subtitle, optional mono lines (ports, versions) and the hover fields.
- **flows**: 4 to 7 named paths, each with a color, a one-line "why" and numbered steps.
- **edges**: orthogonal polylines that belong to one flow, with a step number and an optional label.
- **inventory**, **gaps**, **callout**, **footer**: the sections under the diagram.

Pick flows that answer real questions: "how does a user get in", "how does an operator get in", "how does code get deployed", "where do secrets come from", "where do I look when it breaks", "where does data live".

### 3. Lay it out

Follow [references/layout-and-routing.md](references/layout-and-routing.md). The rules that matter most:

- People and CI on the left, the cloud in the middle, external SaaS on the right, managed services at the bottom of the cloud.
- Fixed grid: node heights 62 / 80, column gaps of at least 15 px, namespace header band of 40 px.
- Edges route through empty lanes between containers, never through boxes. Reserve the lanes when you place the containers.
- Short edges (adjacent boxes) get a step badge and no label; long edges get a label pill.

### 4. Build

```bash
python3 scripts/build.py model.json -o diagram.html
```

`build.py` validates the model (unknown ids, overlapping boxes, text that will overflow its box, edges with an unknown flow), downloads the brand icons it needs from Simple Icons at a pinned version, inlines them, and writes one HTML file. Without network it falls back to letter monograms and says so. Fix every warning before you continue.

Icons: `si:<slug>|<hex>` uses a Simple Icons slug (`kubernetes`, `argo`, `grafana`, `postgresql`, `tailscale`, `terraform`, `githubactions`...). `g:<name>|<hex>` uses a built-in glyph (`user`, `laptop`, `db`, `bucket`, `key`, `shield`, `gear`, `globe`, `wave`, `folder`, `net`, `lb`, `clock`, `box`, `cpu`, `bell`, `code`, `lock`, `queue`). `m:<letters>|<hex>` draws a monogram for brands Simple Icons does not carry.

### 5. Look at it

Render and read the screenshot before you hand it over:

```bash
bash scripts/render.sh diagram.html shots/        # all flows + one PNG per flow
```

Check: no text leaves its box, no label pill sits on a box, every flow's arrows end on the right component, faded nodes in a flow view are really not part of it, dark mode is readable. Iterate on the model, not on the generated HTML.

### 6. Hand over

In your reply: where the file is, what each flow shows, what the diagram is built from (git vs live, date), and any correction you made to the request. Offer a translation or another format. Do not publish the page anywhere without the user's go-ahead.

## Quality bar

- Every box answers "what is this, how do I reach it, where is it defined".
- Planned or pending pieces are dashed and say "PLANNED"; the gaps section names the ticket.
- Words are plain: "Argo CD deploys from git", not "GitOps reconciliation paradigm".
- No secrets, internal IPs, account IDs or personal data. Use `<ip>`, `<account>` placeholders.
- Accessible: real text (not images of text), keyboard-focusable nodes, contrast in both themes.

## Files

| File | Purpose |
| --- | --- |
| `assets/engine.html` | Page template and renderer (DOM-safe, no `innerHTML`) |
| `assets/example-model.json` | Complete example: web app on managed Kubernetes with SSO, tailnet operator access, GitOps and observability |
| `scripts/build.py` | Validate a model, fetch icons, write the HTML |
| `scripts/render.sh` | Headless Chromium screenshots of every flow |
| `references/model-schema.md` | Every field of the model |
| `references/layout-and-routing.md` | Grid, lanes, label placement, common mistakes |
| `references/other-formats.md` | Mermaid, D2, draw.io, SVG and PNG exports from the same model |
