"""Tests d'intégration de la conversion par lot."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services import batch_service, report
from models import BatchStatus, CollisionPolicy, ConversionOptions


@pytest.fixture
def image_dir(tmp_path: Path) -> Path:
    d = tmp_path / "images"
    d.mkdir()
    for i, color in enumerate([(255, 0, 0), (0, 255, 0), (0, 0, 255)]):
        Image.new("RGB", (50, 50), color=color).save(d / f"img{i}.png")
    return d


def test_batch_collect_and_convert(image_dir: Path) -> None:
    service = batch_service.BatchService()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    batch = service.create_batch([image_dir], options)
    assert batch.total == 3

    # Exécution synchrone (sans thread) pour le test.
    from app.services import conversion_service

    for task in batch.tasks:
        result = conversion_service.convert_single(task.source.path, options)
        task.status = result.status
        task.output_path = result.output_path
        task.error = result.error

    batch.status = BatchStatus.COMPLETED
    batch.report = report.build_report(batch)
    assert batch.report.succeeded == 3
    assert batch.report.failed == 0


def test_batch_with_invalid_file(image_dir: Path, tmp_path: Path) -> None:
    bad = image_dir / "bad.png"
    bad.write_bytes(b"not an image")
    service = batch_service.BatchService()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    batch = service.create_batch([image_dir], options)
    assert batch.total == 4

    from app.services import conversion_service

    for task in batch.tasks:
        result = conversion_service.convert_single(task.source.path, options)
        task.status = result.status
        task.output_path = result.output_path
        task.error = result.error

    batch.report = report.build_report(batch)
    assert batch.report.succeeded == 3
    assert batch.report.failed == 1
