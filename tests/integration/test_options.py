"""Tests d'intégration des options (redimensionnement, qualité)."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import converter
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "big.png"
    Image.new("RGB", (400, 200), color=(10, 20, 30)).save(path)
    return path


def test_resize_width(sample_png: Path) -> None:
    options = ConversionOptions(
        target_format="PNG",
        resize_width=200,
        collision_policy=CollisionPolicy.OVERWRITE,
    )
    out = converter.convert(sample_png, options)
    with Image.open(out) as img:
        assert img.size == (200, 100)


def test_resize_box(sample_png: Path) -> None:
    options = ConversionOptions(
        target_format="PNG",
        resize_width=100,
        resize_height=100,
        collision_policy=CollisionPolicy.OVERWRITE,
    )
    out = converter.convert(sample_png, options)
    with Image.open(out) as img:
        assert img.size == (100, 50)


def test_quality_jpeg(sample_png: Path) -> None:
    options = ConversionOptions(
        target_format="JPEG",
        quality=10,
        collision_policy=CollisionPolicy.OVERWRITE,
    )
    out = converter.convert(sample_png, options)
    assert out.exists()
