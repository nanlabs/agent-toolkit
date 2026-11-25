# Model schema

One JSON file describes the whole page. `scripts/build.py` validates it and embeds it into `assets/engine.html`. Start from `assets/example-model.json`.

Coordinates are SVG user units in the `viewBox` space. The default `viewBox` is `[0, -34, 1960, 1324]`; the negative top leaves a lane above everything for long edges (for example sign-in to an external identity provider).

## Page

| Field | Type | Notes |
| --- | --- | --- |
| `title` | string | Browser tab title and SVG label. Two to four words. |
| `heading` | string | Page H1. Defaults to `title`. |
| `lede` | rich text | One paragraph: what the page shows and how to use it. |
| `meta` | rich text | Source of truth and date ("Built from ... on main. Desired state."). |
| `callout` | rich text | Optional "Read this first" box, for the one thing readers get wrong. Empty hides it. |
| `footer` | rich text | Provenance line. |
| `viewBox` | `[x, y, w, h]` | Canvas size. Grow `w`/`h` instead of shrinking boxes. |
| `minWidth` | number | Minimum rendered width in px before the canvas scrolls (default 1150). |
| `defaultFlow` | string | Flow selected on load. `all` shows every edge without labels. A `#<flow-id>` URL hash overrides it. |

Rich text accepts plain text plus `<code>…</code>` and `<strong>…</strong>`. Write `&lt;` / `&gt;` for literal angle brackets (`control.&lt;ip&gt;`). Everything is rendered with DOM text nodes, never as HTML.

## `flows[]`

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | `f1`, `f2`, … Used by edges and URL hashes. |
| `name` | string | Button and card title, numbered: `"2 · Operator via tailnet"`. |
| `color` | string | A token `--f1` … `--f8` (themed for light and dark) or a hex color. |
| `why` | rich text | One sentence: the question this flow answers. |
| `steps` | rich text[] | Numbered steps. Step N must match the `step: N` badges on the edges. |
| `nodes` | string[] | Node ids that stay highlighted when the flow is selected. |

## `containers[]`

Drawn first, in order, so list outer containers before inner ones.

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Unique. |
| `kind` | `cloud` \| `cluster` \| `ns` \| `group` \| `saas` \| `ext` | Fill and border style. `ns` is dashed. |
| `x`, `y`, `w`, `h` | number | Box. |
| `title` | string | Header text. |
| `subtitle` | string | Smaller text after the title (region, node count, purpose). |
| `icon` | icon spec | Optional, in the header. |
| `compact` | boolean | Smaller header icon (use for a cluster inside a cloud). |

## `nodes[]`

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Unique. |
| `x`, `y`, `w`, `h` | number | Use heights 62 (in a namespace) or 76/80 (managed services, SaaS, people). Taller nodes can hold `lines`. |
| `icon` | icon spec | See below. |
| `title` | string | Component name. Keep it short: the validator warns when it will overflow. |
| `subtitle` | string | What it is, in a few words. Wraps if needed. |
| `lines` | string[] | Monospace lines (ports, versions, dashboards). |
| `desc` | string | Hover card and inventory: what it does. |
| `access` | string | Hover card and inventory: how it is reached. |
| `source` | string | Hover card and inventory: the file or directory that defines it. |
| `planned` | boolean | Dashed box with a "PLANNED" badge. Use for anything not live. |

## `edges[]`

| Field | Type | Notes |
| --- | --- | --- |
| `flow` | string | Flow id. The edge takes its color and is highlighted with it. |
| `points` | `[x, y][]` | Orthogonal polyline. First point on the source box border, last point on the target border (the arrowhead sits there). |
| `label` | string | Optional pill text. Leave it out for short edges between adjacent boxes. |
| `step` | number | Badge number; matches the flow's steps. |
| `dashed` | boolean | Tunnels, indirect or planned links. |
| `labelAt` | `[x, y]` | Pill or badge center. Defaults to the middle of the longest segment. |

## `inventory[]`, `gaps[]`

```json
"inventoryIntro": "Everything Argo CD deploys…",
"inventory": [ { "title": "app namespace", "nodes": ["web", "api"] } ],
"gapsTitle": "What is not there yet",
"gapsIntro": "Known open items, with their tickets.",
"gaps": [ { "status": "open", "tag": "Pending IT", "title": "Operator SSO", "text": "Built and off; waiting on the app registration (TICKET-123)." } ]
```

`status` is `open`, `planned` or `done` (color of the tag); `tag` is the visible text.

## Icon specs

| Spec | Meaning |
| --- | --- |
| `si:<slug>\|<hex>` | [Simple Icons](https://simpleicons.org) slug, fetched by `build.py` at a pinned version. Brand marks are trademarks of their owners; use them only to identify the product. |
| `g:<glyph>\|<hex>` | Built-in glyph: `user`, `laptop`, `db`, `bucket`, `key`, `lock`, `shield`, `gear`, `globe`, `wave`, `folder`, `net`, `lb`, `clock`, `box`, `cpu`, `bell`, `code`, `queue`. |
| `m:<letters>\|<hex>` | Monogram, for brands Simple Icons does not carry. 1–3 letters. |

Useful slugs: `kubernetes`, `argo`, `helm`, `terraform`, `githubactions`, `github`, `gitlab`, `docker`, `nginx`, `traefikproxy`, `letsencrypt`, `postgresql`, `mysql`, `redis`, `mongodb`, `clickhouse`, `opensearch`, `elasticsearch`, `apachekafka`, `rabbitmq`, `prometheus`, `grafana`, `opentelemetry`, `datadog`, `sentry`, `tailscale`, `wireguard`, `cloudflare`, `vault`, `nodedotjs`, `python`, `go`, `nextdotjs`, `react`, `electron`, `anthropic`, `openai`, `googlecloud`, `digitalocean`. Check a slug at `https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/<slug>.svg`; some vendors are absent (for example several cloud providers), so use a glyph or monogram for those.
