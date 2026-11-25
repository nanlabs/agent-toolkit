#!/usr/bin/env python3
"""Build a self-contained architecture diagram HTML page from a JSON model.

Usage:
    python3 build.py model.json -o diagram.html [--offline] [--strict]

Steps:
  1. Validate the model and print warnings (unknown ids, overlapping boxes,
     text that will overflow, edges that cross boxes, diagonal segments).
  2. Download the Simple Icons it references (pinned version, cached), unless
     --offline. Missing icons fall back to letter monograms in the page.
  3. Inline icons and model into assets/engine.html and write one HTML file.

Exit code 1 on errors; with --strict, also on warnings.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SIMPLE_ICONS_VERSION = "13.21.0"
ICON_URL = "https://cdn.jsdelivr.net/npm/simple-icons@{v}/icons/{slug}.svg"
HERE = Path(__file__).resolve().parent
ENGINE = HERE.parent / "assets" / "engine.html"
CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "architecture-diagram" / f"simple-icons-{SIMPLE_ICONS_VERSION}"
GLYPHS = {"user", "laptop", "db", "bucket", "key", "lock", "shield", "gear", "globe", "wave", "folder", "net", "lb", "clock", "box", "cpu", "bell", "code", "queue"}
SLUG_RE = re.compile(r"^[a-z0-9]+$")

# Rough text metrics (px per character) for the fonts the engine uses.
TITLE_PX = 7.3   # Inter 600 13px
MONO_PX = 6.4    # JetBrains Mono 10.5px
PILL_PX = 6.1    # label pill text, mirrors engine.html


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def icon_spec(spec: str, where: str, rep: Report) -> tuple[str, str] | None:
    if ":" not in spec:
        rep.error(f"{where}: icon '{spec}' must look like si:<slug>|<hex>, g:<glyph>|<hex> or m:<letters>|<hex>")
        return None
    kind, rest = spec.split(":", 1)
    name = rest.split("|", 1)[0]
    if kind == "si":
        if not SLUG_RE.match(name):
            rep.error(f"{where}: Simple Icons slug '{name}' must be lowercase letters and digits")
            return None
        return kind, name
    if kind == "g":
        if name not in GLYPHS:
            rep.error(f"{where}: unknown glyph '{name}' (known: {', '.join(sorted(GLYPHS))})")
        return None
    if kind == "m":
        if not 1 <= len(name) <= 3:
            rep.warn(f"{where}: monogram '{name}' reads best with 1 to 3 letters")
        return None
    rep.error(f"{where}: unknown icon kind '{kind}'")
    return None


def inside(a: float, lo: float, hi: float, pad: float = 2) -> bool:
    return lo + pad < a < hi - pad


def segment_crosses(seg: tuple[tuple[float, float], tuple[float, float]], n: dict) -> bool:
    (x1, y1), (x2, y2) = seg
    nx, ny, nw, nh = n["x"], n["y"], n["w"], n["h"]
    if y1 == y2:  # horizontal
        lo, hi = sorted((x1, x2))
        return inside(y1, ny, ny + nh) and min(hi, nx + nw - 2) - max(lo, nx + 2) > 0
    if x1 == x2:  # vertical
        lo, hi = sorted((y1, y2))
        return inside(x1, nx, nx + nw) and min(hi, ny + nh - 2) - max(lo, ny + 2) > 0
    return False


def rects_overlap(a: dict, b: dict) -> bool:
    return a["x"] < b["x"] + b["w"] and b["x"] < a["x"] + a["w"] and a["y"] < b["y"] + b["h"] and b["y"] < a["y"] + a["h"]


def validate(m: dict) -> tuple[Report, set[str]]:
    rep = Report()
    slugs: set[str] = set()
    for key in ("title", "nodes"):
        if key not in m:
            rep.error(f"model is missing '{key}'")
    flows = {f.get("id"): f for f in m.get("flows", [])}
    nodes = m.get("nodes", [])
    ids: set[str] = set()
    for n in nodes:
        nid = n.get("id", "?")
        if nid in ids:
            rep.error(f"duplicate node id '{nid}'")
        ids.add(nid)
        for k in ("x", "y", "w", "h", "title"):
            if k not in n:
                rep.error(f"node '{nid}' is missing '{k}'")
        if "icon" in n:
            got = icon_spec(n["icon"], f"node '{nid}'", rep)
            if got:
                slugs.add(got[1])
        if {"x", "y", "w", "h", "title"} <= n.keys():
            s = 36 if n["h"] >= 76 else 30
            text_x = 10 + s + 10
            if text_x + len(n["title"]) * TITLE_PX + 8 > n["w"]:
                rep.warn(f"node '{nid}': title '{n['title']}' will overflow a {n['w']}px box; shorten it or widen the box")
            for line in n.get("lines", []):
                start = 14 if n["h"] > 120 else text_x
                if start + len(line) * MONO_PX + 8 > n["w"]:
                    rep.warn(f"node '{nid}': line '{line}' will overflow")
            for k in ("desc", "access", "source"):
                if not n.get(k) and not n.get("planned"):
                    rep.warn(f"node '{nid}': no '{k}' (the hover card will be thin)")
    for c in m.get("containers", []):
        if "icon" in c:
            got = icon_spec(c["icon"], f"container '{c.get('id')}'", rep)
            if got:
                slugs.add(got[1])
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if {"x", "y", "w", "h"} <= a.keys() and {"x", "y", "w", "h"} <= b.keys() and rects_overlap(a, b):
                rep.warn(f"nodes '{a['id']}' and '{b['id']}' overlap")
    for fid, f in flows.items():
        for nid in f.get("nodes", []):
            if nid not in ids:
                rep.error(f"flow '{fid}' lists unknown node '{nid}'")
        if not f.get("steps"):
            rep.warn(f"flow '{fid}' has no steps")
    used_flows: set[str] = set()
    for i, e in enumerate(m.get("edges", [])):
        where = f"edge #{i + 1} ({e.get('label') or e.get('flow')})"
        if e.get("flow") not in flows:
            rep.error(f"{where}: unknown flow '{e.get('flow')}'")
        used_flows.add(e.get("flow"))
        pts = e.get("points", [])
        if len(pts) < 2:
            rep.error(f"{where}: needs at least two points")
            continue
        for a, b in zip(pts, pts[1:]):
            if a[0] != b[0] and a[1] != b[1]:
                rep.warn(f"{where}: segment {a}->{b} is diagonal; use orthogonal segments")
            for n in nodes:
                if {"x", "y", "w", "h"} <= n.keys() and segment_crosses((tuple(a), tuple(b)), n):
                    rep.warn(f"{where}: segment {a}->{b} crosses node '{n['id']}'; route it through a free lane")
        if e.get("label") and e.get("labelAt"):
            lx, ly = e["labelAt"]
            tw = len(e["label"]) * PILL_PX + (32 if e.get("step") else 18)
            pill = {"x": lx - tw / 2, "y": ly - 11, "w": tw, "h": 22}
            for n in nodes:
                if {"x", "y", "w", "h"} <= n.keys() and rects_overlap(pill, n):
                    rep.warn(f"{where}: label pill overlaps node '{n['id']}'; move labelAt")
    for fid in flows:
        if fid not in used_flows:
            rep.warn(f"flow '{fid}' has no edges")
    for g in m.get("inventory", []):
        for nid in g.get("nodes", []):
            if nid not in ids:
                rep.error(f"inventory group '{g.get('title')}' lists unknown node '{nid}'")
    return rep, slugs


def fetch_icons(slugs: set[str], offline: bool) -> tuple[list[str], list[str]]:
    symbols, missing = [], []
    CACHE.mkdir(parents=True, exist_ok=True)
    for slug in sorted(slugs):
        path = CACHE / f"{slug}.svg"
        if not path.exists() and not offline:
            try:
                with urllib.request.urlopen(ICON_URL.format(v=SIMPLE_ICONS_VERSION, slug=slug), timeout=15) as r:
                    path.write_bytes(r.read())
            except (urllib.error.URLError, TimeoutError):
                pass
        if not path.exists():
            missing.append(slug)
            continue
        match = re.search(r'<path d="([^"]+)"', path.read_text(encoding="utf-8"))
        if not match:
            missing.append(slug)
            continue
        symbols.append(f'<symbol id="si-{slug}" viewBox="0 0 24 24"><path d="{match.group(1)}"/></symbol>')
    return symbols, missing


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--offline", action="store_true", help="use only cached icons")
    ap.add_argument("--strict", action="store_true", help="fail on warnings too")
    args = ap.parse_args()

    model = json.loads(args.model.read_text(encoding="utf-8"))
    rep, slugs = validate(model)
    symbols, missing = fetch_icons(slugs, args.offline) if not rep.errors else ([], [])
    for s in missing:
        rep.warn(f"icon 'si:{s}' not available (offline or unknown slug); a monogram is used instead")

    for w in rep.warnings:
        print(f"WARN  {w}", file=sys.stderr)
    for e in rep.errors:
        print(f"ERROR {e}", file=sys.stderr)
    if rep.errors or (args.strict and rep.warnings):
        return 1

    # The model is embedded as a JS literal; escape "</" so no string can close the script tag.
    data = json.dumps(model, ensure_ascii=False).replace("</", "<\\/")
    html = ENGINE.read_text(encoding="utf-8").replace("/*ICONS*/", "\n".join(symbols)).replace("/*MODEL*/", data)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html, encoding="utf-8")
    print(f"wrote {args.out} ({len(html) // 1024} KB, {len(symbols)} brand icons, {len(rep.warnings)} warnings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
