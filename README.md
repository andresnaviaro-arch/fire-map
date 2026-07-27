# Where the world is burning

A shareable world map of active fire detections, redrawn every day from NASA satellite data.

Everything is in one HTML file with no build step, no tile server and no map library.
The coastlines and borders are baked into the page, so the only thing that changes
day to day is `data/fires.json`.

---

## Publish it in about ten minutes

**1. Get a NASA FIRMS key.** Free, instant, no approval queue:
<https://firms.modaps.eosdis.nasa.gov/api/map_key/>

**2. Put this folder in a new GitHub repository.**

**3. Add the key as a repository secret.**
Settings → Secrets and variables → Actions → New repository secret.
Name it exactly `FIRMS_MAP_KEY`.

**4. Turn on GitHub Pages.**
Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

**5. Run the workflow once by hand.**
Actions tab → *Refresh fire data* → *Run workflow*.

Your link is then `https://<you>.github.io/<repo>/` and it refreshes itself
every morning at 05:40 UTC. The key never leaves the Actions runner, so you can
share the URL with anyone.

### Or just run it locally

```bash
export FIRMS_MAP_KEY=your_key_here
python3 scripts/fetch_fires.py
python3 -m http.server 8080
```

Then open <http://localhost:8080>. Opening `index.html` straight off the disk
will not work — browsers block the JSON load on `file://` URLs.

---

## What the map is actually showing

Each dot is a cluster of **VIIRS hot pixels** — 375 m patches of ground that were
radiating enough heat to trip the fire threshold during a satellite overpass in the
last 24 hours. Three satellites are pooled: NOAA-20, NOAA-21 and Suomi-NPP.

Detections within roughly 5 km of each other are merged into one **fire complex**,
so a single long fire front counts once rather than four hundred times.

**"Large" is a threshold you choose, not a fact.** The slider in the panel sets how
many detections a complex needs before it counts, and the headline number moves with
it. Twenty detections is a reasonable default — very roughly a 3 km² actively burning
front. The histogram above the slider shows how many fires sit on each side of your
cut, which is the honest way to present a count like this.

### What it is not

- **Not only wildfires.** Gas flares in the Niger Delta and the Persian Gulf, steel
  works, sugar-cane and stubble burning, and prescribed burns all radiate heat and all
  show up. Persistent dots in the same industrial spot every single day are usually flares.
- **Not burn scars.** A detection means something was hot at the moment of the overpass.
  It says nothing about total area burnt.
- **Not complete.** Thick smoke and cloud hide fires. A fire that starts and dies between
  overpasses is never seen. Small or cool ground fires under canopy are missed.
- **Not instant.** Near-real-time means roughly three hours behind the satellite.

### The green rings are different

Those are **named incidents typed in by hand** from news and fire-agency reports, each
with its own source and date, and each is labelled as such when you click it. They exist
because "Gironde" means more to a reader than an anonymous cluster of pixels. They are
not satellite data and they do not go stale on their own — edit the `INCIDENTS` array
near the top of the script in `index.html` to keep them current, or delete the array
if you would rather ship pure satellite data.

---

## Where the numbers come from

| Source | What it gives you |
|---|---|
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/map/) | The detections this map is built on |
| [EFFIS](https://forest-fire.emergency.copernicus.eu/) | EU burnt area, fire counts, danger forecasts |
| [NIFC](https://www.nifc.gov/fire-information/nfn) | US large-fire count and crew numbers, daily |
| [CIFFC](https://ciffc.net/situation/) | Canadian active fires and national preparedness level |
| [GWIS](https://gwis.jrc.ec.europa.eu/) | Global country-by-country burnt area statistics |

FIRMS data is free to use. NASA asks that you credit it — the footer already does.

## Credits

Coastlines and borders from [world-atlas](https://github.com/topojson/world-atlas)
(Natural Earth, public domain). Type is IBM Plex, open licensed.
