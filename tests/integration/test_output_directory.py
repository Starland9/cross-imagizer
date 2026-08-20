"""Tests d'intégration de la conversion vers un dossier de sortie."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import converter
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "src.png"
    Image.new("RGB", (50, 50), color=(1, 2, 3)).save(path)
    return path


def test_convert_to_output_directory(sample_png: Path, tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    result = converter.convert(sample_png, options, output_dir=out_dir)
    assert result.parent == out_dir
    assert result.exists()


def test_convert_default_output_directory(sample_png: Path) -> None:
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    result = converter.convert(sample_png, options)
    assert result.parent == sample_png.parent
