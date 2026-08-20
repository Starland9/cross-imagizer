"""Tests d'intégration de la conversion d'une image unique."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services import conversion_service
from models import CollisionPolicy, ConversionOptions, TaskStatus


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "photo.png"
    Image.new("RGB", (200, 100), color=(0, 128, 255)).save(path)
    return path


def test_single_conversion_success(sample_png: Path) -> None:
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    task = conversion_service.convert_single(sample_png, options)
    assert task.status is TaskStatus.SUCCEEDED
    assert task.output_path is not None
    assert task.output_path.exists()


def test_single_conversion_failure(tmp_path: Path) -> None:
    bad = tmp_path / "bad.png"
    bad.write_bytes(b"garbage")
    options = ConversionOptions(target_format="PNG")
    task = conversion_service.convert_single(bad, options)
    assert task.status is TaskStatus.FAILED
    assert task.error is not None
