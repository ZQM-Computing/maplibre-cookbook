# MapLibre Patterns

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a> •
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

[![CI](https://github.com/ZQM-Computing/maplibre-patterns/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Computing/maplibre-patterns/actions/workflows/ci.yml)

Production-tested MapLibre GL JS patterns for frontend vector tile rendering — custom layers, 3D terrain, performance tuning, and interactive maps. Every example is a single self-contained HTML file: no build step, no dependencies beyond the MapLibre CDN.

## Repository role and status

**Status:** Active, public.

**What this repository is:** MapLibre GL JS patterns for frontend vector-tile rendering — custom layers, 3D terrain, performance tuning, and interactive maps, each example a single self-contained HTML file.

**What it contributes:** Part of the ZQM Computing public geospatial portfolio — production-grade pattern and reference repositories that document geospatial engineering practice across the stack. This repository is the reusable pattern library for its layer: working code and runbooks that practitioners can lift into their own pipelines, and portfolio evidence of the engineering practice behind ZQM Computing. The umbrella index for the series is [geospatial-patterns](https://github.com/ZQM-Computing/geospatial-patterns).

**Standing:** The portfolio program was completed and Tier-1 hardened on 2026-10-15, with prose CI enforced as required status checks. This repository is standalone — no other repository or deployment depends on it.

## Who this is for

Web developers, GIS developers, and frontend engineers who need to put spatial data on a map in the browser without a framework toolchain.

## Prerequisites

- A modern browser (Chrome, Firefox, Safari, Edge)
- Internet access for the MapLibre GL JS 4.x CDN (each example loads `maplibre-gl@4.0.0` from unpkg)

No install, no build. Clone the repo and open a file.

## Quickstart

```bash
# Serve locally (avoids file:// restrictions on some browsers)
python3 -m http.server 8000

# Then open http://localhost:8000/examples/01-vector-tiles/
```

Or just double-click any `examples/*/index.html`.

## Usage

Each pattern is a self-contained, runnable example. Start from the
[Quickstart](#quickstart), then open any entry in the [Patterns](#patterns)
list and run it end to end. Copy the pattern into your own project and
swap in your data — the patterns are reference implementations, not a
package to install.

## Patterns

| # | Example | What it demonstrates |
|---|---------|----------------------|
| 01 | `01-vector-tiles` | Rendering MVT vector tiles from a public tile source |
| 02 | `02-custom-layers` | Fill, line, symbol, circle, and heatmap layers |
| 03 | `03-3d-terrain` | Terrain exaggeration and 3D buildings |
| 04 | `04-performance` | Glyphs, sprites, and tile-loading optimization |
| 05 | `05-postgis-mvt` | Client-side rendering of MVT tiles generated server-side with PostGIS `ST_AsMVT` (see the pattern notes in the file for the SQL side) |
| 06 | `06-interactive-map` | Full-featured interactive map combining the earlier patterns |

Example 05 is client-side only: it shows how to consume MVT tiles in MapLibre, and documents the `ST_AsMVT` query shape you'd serve them from. For the server side, see [postgis-patterns](https://github.com/ZQM-Computing/postgis-patterns).

## Repository layout

```text
maplibre-patterns/
├── examples/
│   ├── 01-vector-tiles/index.html
│   ├── 02-custom-layers/index.html
│   ├── 03-3d-terrain/index.html
│   ├── 04-performance/index.html
│   ├── 05-postgis-mvt/index.html
│   └── 06-interactive-map/index.html
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## Validation

Examples are validated by opening them in a browser (or served via `python3 -m http.server`) and confirming the map renders without console errors. CI lints the repository on every push and pull request.

## Roadmap

- PMTiles single-file tiles as a vector source
- Deck.gl overlay interop sketch
- Offline/service-worker tile caching

## Contributing

See [CONTRIBUTING.md](https://github.com/ZQM-Computing/maplibre-patterns/blob/main/CONTRIBUTING.md). Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## Related repositories

- [postgis-patterns](https://github.com/ZQM-Computing/postgis-patterns) — Production PostGIS patterns: spatial indexing, joins & KNN, SRID management, vector tiles, data quality, partitioning
- [duckdb-spatial-patterns](https://github.com/ZQM-Computing/duckdb-spatial-patterns) — DuckDB Spatial patterns for analytical geospatial SQL: GeoParquet, spatial joins, KNN, H3 aggregation — no server required
- [pgrouting-patterns](https://github.com/ZQM-Computing/pgrouting-patterns) — pgRouting network analysis on PostGIS: shortest path, driving distance, isochrones, turn restrictions, traffic-aware routing
- [geopandas-patterns](https://github.com/ZQM-Computing/geopandas-patterns) — GeoPandas/Shapely patterns for Python geospatial workflows: spatial joins, CRS handling, overlays, interpolation, performance
- [gdal-patterns](https://github.com/ZQM-Computing/gdal-patterns) — GDAL/OGR command-line patterns: conversion, reprojection, clipping, mosaicking — production-tested, runnable examples
- [stac-patterns](https://github.com/ZQM-Computing/stac-patterns) — STAC patterns for geospatial data discovery: catalogs, item validation, search API, bulk operations, cloud deployment
- [cog-patterns](https://github.com/ZQM-Computing/cog-patterns) — Cloud Optimized GeoTIFF patterns: creation, validation, TiTiler serving, xarray integration, performance benchmarking
- [geoparquet-patterns](https://github.com/ZQM-Computing/geoparquet-patterns) — GeoParquet patterns for columnar geospatial analytics: partitioning, predicate pushdown, DuckDB/Spark integration
- [h3-patterns](https://github.com/ZQM-Computing/h3-patterns) — H3 hexagonal grid patterns: indexing, aggregation, visualization, grid comparisons, performance benchmarks
- [qgis-resources](https://github.com/ZQM-Computing/qgis-resources) — QGIS expressions, PyQGIS snippets, Processing scripts, styles, and QField field-collection guides
- [geospatial-api-reference](https://github.com/ZQM-Computing/geospatial-api-reference) — OGC API – Features reference implementation with FastAPI and PostGIS backends
- [ollama-fleet-patterns](https://github.com/ZQM-Computing/ollama-fleet-patterns) — Ollama fleet operations: model management, health checks, load-spreading, VRAM budgeting, dependency-light RAG
- [proxmox-ceph-operations](https://github.com/ZQM-Computing/proxmox-ceph-operations) — Proxmox VE + Ceph operations runbooks: health checks, backup discipline, OSD replacement, upgrade checklists
- [geospatial-patterns](https://github.com/ZQM-Computing/geospatial-patterns) — Umbrella index for all ZQM geospatial pattern repos

## Documentation and validation

For setup instructions, reproducible examples, data provenance, CRS/SRID assumptions, security guidance, and dependency labels, follow the [ZQM geospatial repository documentation standard](https://github.com/ZQM-Computing/geospatial-patterns/blob/main/docs/repository-documentation-standard.md).

The configured CI workflow is the source of truth for automated checks. A passing workflow establishes only that its checks passed for that commit; it does not certify production deployment or prove that every dependency and operating environment was covered.

## Installation

No installation — clone the repository and open the examples; patterns are copy-paste MapLibre GL JS snippets.

*Part of [ZQM Computing](https://github.com/ZQM-Computing) — geospatial engineering, scientific computing, and infrastructure patterns; the geospatial arm of [ZQM Labs](https://zqmlabs.com), makers of Z's Quests & Mischief location games.*

## License

MIT — see [LICENSE](LICENSE).

<!-- ZQM-FOOTER-START -->
<!-- markdownlint-disable MD033 -->
---

<p align="center">
  <em>Play more. Plan less.</em><br>
  <a href="https://zqmlabs.com">zqmlabs.com</a> •
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a> •
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-FOOTER-END -->
