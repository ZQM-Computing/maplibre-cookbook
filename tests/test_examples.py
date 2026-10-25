"""
Tests for MapLibre patterns repository structure and content.
"""
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_examples_directory_exists():
    """Verify the examples directory exists."""
    assert (REPO_ROOT / "examples").is_dir(), "examples/ directory must exist"


def test_mkdocs_yml_exists():
    """Verify mkdocs.yml exists."""
    assert (REPO_ROOT / "mkdocs.yml").is_file(), "mkdocs.yml must exist"



def test_examples_avoid_private_maplibre_internals():
    """Examples use supported MapLibre APIs and show structurally valid MVT SQL."""
    performance = (REPO_ROOT / "examples/04-performance/index.html").read_text(
        encoding="utf-8"
    )
    assert "map.areTilesLoaded()" in performance
    assert "sourceCaches" not in performance

    mvt = (REPO_ROOT / "examples/05-postgis-mvt/index.html").read_text(
        encoding="utf-8"
    )
    assert "ST_TileEnvelope($1, $2, $3)" in mvt
    assert "ST_AsMVTGeom(t.geom, bounds.geom" in mvt
    assert "SELECT ST_AsMVT(mvtgeom, 'default', 4096, 'geom')" in mvt
    assert "FROM mvtgeom;" in mvt


def test_readme_exists():
    """Verify README.md exists."""
    assert (REPO_ROOT / "README.md").is_file(), "README.md must exist"


def test_at_least_six_examples():
    """Verify at least 6 example directories exist."""
    examples_dir = REPO_ROOT / "examples"
    examples = [d for d in examples_dir.iterdir() if d.is_dir()]
    assert len(examples) >= 6, f"Must have at least 6 examples, found {len(examples)}"


def test_mkdocs_has_site_name():
    """Verify mkdocs.yml has site_name."""
    content = (REPO_ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    assert "site_name:" in content, "mkdocs.yml must have site_name"


def test_readme_has_content():
    """Verify README has meaningful content."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert len(readme) > 100, "README must have substantial content"
    assert "MapLibre" in readme or "maplibre" in readme.lower(), "README should mention MapLibre"
