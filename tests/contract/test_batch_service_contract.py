"""Tests de contrat du service de lot."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services import batch_service
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def image_dir(tmp_path: Path) -> Path:
    d = tmp_path / "imgs"
    d.mkdir()
    Image.new("RGB", (30, 30), color=(9, 9, 9)).save(d / "a.png")
    Image.new("RGB", (30, 30), color=(8, 8, 8)).save(d / "b.png")
    return d


def test_create_batch_returns_batch(image_dir: Path) -> None:
    service = batch_service.BatchService()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    batch = service.create_batch([image_dir], options)
    assert batch.total == 2
    assert all(t.status.value == "pending" for t in batch.tasks)
