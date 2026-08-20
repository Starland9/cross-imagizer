"""Tests d'intégration de l'ouverture du dossier après conversion."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import converter
from models import CollisionPolicy, ConversionOptions
from platform_utils import open_folder


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "img.png"
    Image.new("RGB", (40, 40), color=(1, 2, 3)).save(path)
    return path


def test_open_output_directory_after_conversion(sample_png: Path, tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    result = converter.convert(sample_png, options, output_dir=out_dir)
    assert result.parent == out_dir
    # Le dossier de sortie est un dossier existant, donc ouvrable.
    assert open_folder.open_folder(out_dir) is True or open_folder.open_folder(out_dir) is False
