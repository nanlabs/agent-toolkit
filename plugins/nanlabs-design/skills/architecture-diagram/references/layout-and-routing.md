# Layout and routing

A readable diagram is mostly empty space in the right places. Plan the lanes before you place the boxes.

## Page regions (left to right)

```text
 x: 14 ─ 296        310 ─────────────────────────── ~1655       1665 ─ 1955
 ┌ People ───┐      ┌ Cloud account ─────────────────────┐      ┌ SaaS ─────┐
 │ user      │      │ LB · K8s API          (top row)    │      │ IdP       │
 │           │      │ ┌ Cluster ──────────────────────┐  │      │ LLM API   │
 │ operator  │      │ │ ns row 1 (user-facing)        │  │      │ ACME CA   │
 └───────────┘      │ │ ns row 2 (ops, data, obs)     │  │      │ VPN/DNS   │
 ┌ Code & CI ┐      │ └───────────────────────────────┘  │      │ planned…  │
 │ repo · CI │      │ Managed services (registry, S3,    │      └───────────┘
 └───────────┘      │ secrets, IAM, Terraform)           │
                    └────────────────────────────────────┘
```

- Who starts a flow sits on the left (users, operators, CI). What the system calls out to sits on the right. Arrows then mostly go left to right.
- Inside the cluster, put the user-facing namespaces in the top row, next to the ingress, and the operator, observability and platform namespaces below.
- Managed cloud services go in a band at the bottom of the cloud box, so "pull image", "S3", "read secret" edges are short verticals.

## Grid

| Thing | Value |
| --- | --- |
| Node height | 62 inside a namespace; 76–80 for top-level and SaaS nodes |
| Node width | 150–265; long titles need ≥ 210 |
| Gap between nodes in a namespace | ≥ 13 px vertical, ≥ 15 px horizontal |
| Namespace header band | 40 px (first node at `ns.y + 42`) |
| Gap between namespaces | 15–20 px (these gaps are your lanes) |
| Container padding | 15 px |

## Lanes

An edge must never pass through a box. Reserve lanes:

- **Horizontal lanes**: the 15–20 px gaps between namespace rows, the band between the cluster header and the first namespace row, the band between the cluster and the managed-services group, and a lane above the whole canvas (y ≈ -14) for long edges to SaaS.
- **Vertical lanes**: the gaps between namespace columns, the strip between the cluster border and the cloud border, and the strip between the cloud and the SaaS column.
- When two flows must share a lane, offset them by 8–10 px. They are rarely shown together; the "All flows" view hides labels.

`build.py` warns when a segment crosses a node or a label pill sits on a node. Treat both as bugs.

## Edges

- Orthogonal only. Start on the source border, end on the target border (the arrowhead goes there).
- Adjacent boxes: a short edge plus a step badge, no label.
- Long edges: a label pill of 1–4 words ("push images (OIDC)", ":8080 Argo CD"). Put the pill on the longest straight segment, in empty space. Use `labelAt` when the default spot is crowded.
- Dashed for tunnels (VPN, WireGuard), indirect links and planned links.
- One edge can fan out: route a shared trunk, then branch (for example one tailnet trunk splitting to three admin UIs).

## Flows

- 4 to 7 flows. More than that means some should be merged.
- Steps are short sentences that name the component and the mechanism ("Argo CD reads `main` with a read-only deploy key").
- Number each step's main edge with `step`. Several edges may share a number (one step, several ports).
- `nodes` lists every box the flow touches, including external ones, so the rest fades out.

## Common mistakes

| Symptom | Fix |
| --- | --- |
| Title runs into the next box | Shorten the title (put detail in `subtitle` or `desc`) or widen the node |
| Label pill over a box | Move `labelAt` into a lane, or drop the label and keep the badge |
| Arrow enters a box from the middle of another box | Re-route through a lane; add a waypoint |
| Everything highlighted in a flow view | The flow's `nodes` list is too generous |
| A planned piece looks live | Set `planned: true` and add it to `gaps` with its ticket |
| The diagram shows what the user asked, not what exists | Draw what the config says; explain the difference in `callout` |
