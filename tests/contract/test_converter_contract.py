"""Tests de contrat du moteur de conversion."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import converter
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "src.png"
    Image.new("RGB", (60, 60), color=(1, 2, 3)).save(path)
    return path


def test_convert_never_modifies_source(sample_png: Path) -> None:
    before = sample_png.read_bytes()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    converter.convert(sample_png, options)
    assert sample_png.read_bytes() == before


def test_convert_returns_existing_output(sample_png: Path) -> None:
    options = ConversionOptions(target_format="PNG", collision_policy=CollisionPolicy.OVERWRITE)
    out = converter.convert(sample_png, options)
    assert out.exists()
    assert out.suffix == ".png"
