#!/usr/bin/env python3
"""
Pull the last 24 hours of VIIRS active-fire detections worldwide from NASA FIRMS,
group them into fire complexes, and write data/fires.json for the map.

Usage:
    FIRMS_MAP_KEY=xxxxxxxx python3 scripts/fetch_fires.py

Get a free key (takes about a minute):
    https://firms.modaps.eosdis.nasa.gov/api/map_key/
"""

import csv
import io
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from collections import defaultdict

API = "https://firms.modaps.eosdis.nasa.gov/api/area/csv"
SENSORS = ["VIIRS_NOAA20_NRT", "VIIRS_NOAA21_NRT", "VIIRS_SNPP_NRT"]

# ~5.5 km cells. Detections in touching cells become one complex, so fires
# separated by less than roughly one cell read as a single front.
CELL = 0.05
MAX_COMPLEXES = 12000
DROP_LOW_CONFIDENCE = True

# First match wins, so put the narrow boxes above the wide ones.
REGIONS = [
    ("Canada & Alaska",              -170,  49,  -52,  85),
    ("United States",                -125,  24,  -66,  50),
    ("Hawaii & Pacific islands",     -180, -30, -130,  30),
    ("Mexico, C. America & Caribbean",-118,   6,  -59,  33),
    ("South America",                 -82, -56,  -34,  14),
    ("Europe",                        -26,  34,   40,  72),
    ("Russia & North Asia",            40,  48,  190,  78),
    ("Middle East & North Africa",    -18,  12,   63,  42),
    ("Sub-Saharan Africa",            -20, -36,   54,  16),
    ("South Asia",                     60,   5,   93,  38),
    ("Southeast Asia",                 92, -11,  142,  29),
    ("East Asia",                      93,  20,  147,  55),
    ("Australia & New Zealand",       110, -50,  180,  -8),
]


def region_of(lon, lat):
    for i, (_, w, s, e, n) in enumerate(REGIONS):
        if w <= lon <= e and s <= lat <= n:
            return i
    return len(REGIONS)  # "Elsewhere"


def fetch(sensor, key, date):
    # Always ask for an explicit, complete UTC day. A dateless query means "the
    # current UTC day", which is only partially processed for most of the day —
    # e.g. a run at 02:30 UTC once got 11 detections from a sensor instead of
    # ~65,000 because only the first granules of the new day existed yet.
    url = f"{API}/{key}/{sensor}/world/1/{date}"
    req = urllib.request.Request(url, headers={"User-Agent": "global-fire-map/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        body = r.read().decode("utf-8", "replace")
    if body.lstrip().lower().startswith(("invalid", "<!doctype", "<html")):
        raise RuntimeError(f"{sensor}: FIRMS rejected the request. Check FIRMS_MAP_KEY.")
    rows = list(csv.DictReader(io.StringIO(body)))
    print(f"  {sensor}: {len(rows):,} detections ({date})", file=sys.stderr)
    return rows


def main():
    key = os.environ.get("FIRMS_MAP_KEY", "").strip()
    if not key:
        sys.exit("FIRMS_MAP_KEY is not set. Get one at "
                 "https://firms.modaps.eosdis.nasa.gov/api/map_key/")

    day = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Fetching FIRMS world data for {day} (last complete UTC day)...",
          file=sys.stderr)
    # slots: n, frp sum, lon*w sum, lat*w sum, max brightness, weight sum
    cells = defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0, 0.0])
    total = 0
    used = []

    for sensor in SENSORS:
        try:
            rows = fetch(sensor, key, day)
        except Exception as exc:                      # one dead sensor must not kill the run
            print(f"  {sensor}: skipped ({exc})", file=sys.stderr)
            continue
        used.append(sensor)
        for row in rows:
            conf = (row.get("confidence") or "").strip().lower()
            if DROP_LOW_CONFIDENCE and conf == "l":
                continue
            try:
                lon = float(row["longitude"]); lat = float(row["latitude"])
                frp = float(row.get("frp") or 0.0)
                bt = float(row.get("bright_ti4") or row.get("brightness") or 0.0)
            except (KeyError, ValueError):
                continue
            total += 1
            k = (int(lon // CELL), int(lat // CELL))
            c = cells[k]
            w = max(frp, 0.01)
            c[0] += 1; c[1] += frp
            c[2] += lon * w; c[3] += lat * w
            c[4] = max(c[4], bt); c[5] += w

    if not used:
        sys.exit("Every sensor failed. Nothing written; the old fires.json is left alone.")
    if total == 0:
        sys.exit("Sensors responded but returned zero detections — refusing to "
                 "overwrite fires.json with an empty dataset.")
    print(f"Kept {total:,} detections in {len(cells):,} cells", file=sys.stderr)

    # Union adjacent cells (8-neighbour) into complexes.
    parent = {k: k for k in cells}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for (cx, cy) in list(cells):
        for dx in (0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy <= 0:
                    continue
                nb = (cx + dx, cy + dy)
                if nb in cells:
                    union((cx, cy), nb)

    groups = defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0, 0.0])
    for k, c in cells.items():
        g = groups[find(k)]
        g[0] += c[0]; g[1] += c[1]
        g[2] += c[2]; g[3] += c[3]
        g[4] = max(g[4], c[4]); g[5] += c[5]

    complexes = []
    for g in groups.values():
        if g[0] < 2 or g[5] <= 0:
            continue
        lon = round(g[2] / g[5], 3)
        lat = round(g[3] / g[5], 3)
        complexes.append([lon, lat, g[0], round(g[1], 1),
                          round(g[4], 1), region_of(lon, lat)])

    complexes.sort(key=lambda c: -c[2])
    if len(complexes) > MAX_COMPLEXES:
        print(f"Trimming {len(complexes):,} complexes to the {MAX_COMPLEXES:,} largest",
              file=sys.stderr)
        complexes = complexes[:MAX_COMPLEXES]

    out = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "window": "24h",
        "sources": used,
        "cell_deg": CELL,
        "detections": total,
        "regions": [r[0] for r in REGIONS] + ["Elsewhere"],
        "complexes": complexes,
    }

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "fires.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f, separators=(",", ":"))

    big = sum(1 for c in complexes if c[2] >= 20)
    size = os.path.getsize(path) / 1024
    print(f"Wrote {path} — {len(complexes):,} complexes, "
          f"{big:,} of them large, {size:.0f} KB", file=sys.stderr)


if __name__ == "__main__":
    main()
