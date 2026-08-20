"""Benchmarks de performance (conversion, démarrage, lot)."""

from __future__ import annotations

import time
from pathlib import Path

import pytest
from PIL import Image

from app.core import converter
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "bench.png"
    Image.new("RGB", (800, 600), color=(100, 150, 200)).save(path)
    return path


def test_single_conversion_under_5s(sample_png: Path) -> None:
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    start = time.perf_counter()
    converter.convert(sample_png, options)
    elapsed = time.perf_counter() - start
    assert elapsed < 5.0, f"Conversion trop lente : {elapsed:.2f}s"


def test_batch_100_images(tmp_path: Path) -> None:
    d = tmp_path / "batch"
    d.mkdir()
    for i in range(100):
        Image.new("RGB", (100, 100), color=(i % 255, 0, 0)).save(d / f"img{i}.png")

    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    start = time.perf_counter()
    for p in sorted(d.glob("*.png")):
        converter.convert(p, options)
    elapsed = time.perf_counter() - start
    # 100 images doivent être traitées en un temps raisonnable (< 60s).
    assert elapsed < 60.0, f"Lot de 100 images trop lent : {elapsed:.2f}s"
