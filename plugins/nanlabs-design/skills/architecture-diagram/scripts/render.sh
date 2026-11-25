#!/usr/bin/env bash
# Screenshot an architecture diagram page: the "all flows" view plus one PNG per flow.
#
# Usage: render.sh <diagram.html> <out-dir> [model.json]
#   model.json is used to list the flow ids; without it only the default view is rendered.
#   Set CHROME=/path/to/chrome to pick the browser.
set -euo pipefail

html="${1:?usage: render.sh <diagram.html> <out-dir> [model.json]}"
out="${2:?usage: render.sh <diagram.html> <out-dir> [model.json]}"
model="${3:-}"

find_chrome() {
  if [[ -n "${CHROME:-}" ]]; then echo "$CHROME"; return; fi
  for c in chromium chromium-browser google-chrome google-chrome-stable brave microsoft-edge; do
    if command -v "$c" >/dev/null 2>&1; then command -v "$c"; return; fi
  done
  case "$(uname -s)" in
    Darwin)
      for app in "Google Chrome" "Chromium" "Brave Browser"; do
        p="/Applications/$app.app/Contents/MacOS/$app"
        [[ -x "$p" ]] && { echo "$p"; return; }
      done ;;
  esac
  # Playwright's bundled Chromium, newest first.
  local p
  p="$(find "$HOME/.cache/ms-playwright" -maxdepth 3 -path '*/chromium-*/chrome-*/chrome' -type f 2>/dev/null | sort -V | tail -1 || true)"
  [[ -n "$p" ]] && { echo "$p"; return; }
  echo ""
}

chrome="$(find_chrome)"
if [[ -z "$chrome" ]]; then
  echo "No Chromium-based browser found. Install one or set CHROME=/path/to/chrome." >&2
  exit 1
fi

mkdir -p "$out"
abs="$(cd "$(dirname "$html")" && pwd)/$(basename "$html")"

flows=(all)
if [[ -n "$model" ]]; then
  while IFS= read -r f; do flows+=("$f"); done < <(python3 -c 'import json,sys; [print(f["id"]) for f in json.load(open(sys.argv[1])).get("flows",[])]' "$model")
fi

for f in "${flows[@]}"; do
  "$chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1960,1500 \
    --virtual-time-budget=5000 --screenshot="$out/flow-$f.png" "file://$abs#$f" >/dev/null 2>&1
  echo "$out/flow-$f.png"
done
