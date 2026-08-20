"""Benchmark de la sélection de dossier de sortie + conversion."""

from __future__ import annotations

import time
from pathlib import Path

from PIL import Image

from app.core import converter
from app.services import settings_service
from models import CollisionPolicy, ConversionOptions


def test_output_directory_selection_and_conversion_under_10s(tmp_path: Path) -> None:
    """Vérifie que sélection + conversion d'une image prend < 10s."""
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    src = tmp_path / "img.png"
    Image.new("RGB", (400, 300), color=(10, 20, 30)).save(src)

    start = time.perf_counter()
    settings_service.set_output_directory(out_dir)
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    converter.convert(src, options, output_dir=out_dir)
    elapsed = time.perf_counter() - start

    assert elapsed < 10.0, f"Sélection + conversion trop lente : {elapsed:.2f}s"
