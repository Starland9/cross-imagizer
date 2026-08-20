"""Tests du worker d'arrière-plan (exécution synchrone du run)."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services.worker import BatchWorker
from models import (
    Batch,
    BatchStatus,
    CollisionPolicy,
    ConversionOptions,
    ConversionTask,
    ImageSource,
)


@pytest.fixture
def image_dir(tmp_path: Path) -> Path:
    d = tmp_path / "imgs"
    d.mkdir()
    Image.new("RGB", (20, 20), color=(1, 1, 1)).save(d / "x.png")
    Image.new("RGB", (20, 20), color=(2, 2, 2)).save(d / "y.png")
    return d


def test_worker_runs_batch(image_dir: Path) -> None:
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    tasks = [
        ConversionTask(id=str(p), source=ImageSource(path=p), options=options)
        for p in sorted(image_dir.glob("*.png"))
    ]
    batch = Batch(id="b", tasks=tasks)
    worker = BatchWorker(batch, options)
    worker.run()  # exécution synchrone pour le test
    assert batch.status is BatchStatus.COMPLETED
    assert batch.report.succeeded == 2
