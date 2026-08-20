"""Tests unitaires des services (collecte de fichiers, rapport)."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services import file_collector, report
from models import Batch, ConversionOptions, ConversionTask, ImageSource, TaskStatus


@pytest.fixture
def image_dir(tmp_path: Path) -> Path:
    d = tmp_path / "imgs"
    d.mkdir()
    Image.new("RGB", (10, 10)).save(d / "a.png")
    Image.new("RGB", (10, 10)).save(d / "b.jpg")
    (d / "note.txt").write_text("not an image")
    sub = d / "sub"
    sub.mkdir()
    Image.new("RGB", (10, 10)).save(sub / "c.png")
    return d


def test_collect_files_non_recursive(image_dir: Path) -> None:
    files = file_collector.collect_files([image_dir], recursive=False)
    names = {f.name for f in files}
    assert names == {"a.png", "b.jpg"}


def test_collect_files_recursive(image_dir: Path) -> None:
    files = file_collector.collect_files([image_dir], recursive=True)
    names = {f.name for f in files}
    assert names == {"a.png", "b.jpg", "c.png"}


def test_collect_single_file(image_dir: Path) -> None:
    files = file_collector.collect_files([image_dir / "a.png"])
    assert len(files) == 1


def test_build_report() -> None:
    opts = ConversionOptions("PNG")
    t1 = ConversionTask("1", ImageSource(Path("a.png")), opts, status=TaskStatus.SUCCEEDED)
    t2 = ConversionTask(
        "2", ImageSource(Path("b.png")), opts, status=TaskStatus.FAILED, error="boom"
    )
    t3 = ConversionTask("3", ImageSource(Path("c.png")), opts, status=TaskStatus.CANCELLED)
    batch = Batch("b", tasks=[t1, t2, t3])
    rep = report.build_report(batch)
    assert rep.succeeded == 1
    assert rep.failed == 1
    assert rep.cancelled == 1
    assert rep.failures == [{"file": "b.png", "reason": "boom"}]
