"""Tests unitaires des entités du domaine."""

from __future__ import annotations

from pathlib import Path

from models import (
    Batch,
    BatchReport,
    CollisionPolicy,
    ConversionOptions,
    ConversionTask,
    ImageSource,
    TaskStatus,
)


def test_image_source_defaults() -> None:
    src = ImageSource(path=Path("/tmp/a.png"))
    assert src.format is None
    assert src.width is None
    assert src.is_animated is False


def test_conversion_options_defaults() -> None:
    opts = ConversionOptions(target_format="PNG")
    assert opts.quality is None
    assert opts.collision_policy is CollisionPolicy.RENAME
    assert opts.preserve_metadata is True


def test_batch_progress() -> None:
    task1 = ConversionTask(
        id="1", source=ImageSource(Path("a.png")), options=ConversionOptions("PNG")
    )
    task2 = ConversionTask(
        id="2", source=ImageSource(Path("b.png")), options=ConversionOptions("PNG")
    )
    batch = Batch(id="b1", tasks=[task1, task2])
    assert batch.total == 2
    assert batch.done == 0
    task1.status = TaskStatus.SUCCEEDED
    assert batch.done == 1


def test_batch_report_defaults() -> None:
    report = BatchReport()
    assert report.succeeded == 0
    assert report.failures == []
