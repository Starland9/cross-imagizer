"""Tests d'intégration de la persistance de l'historique."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.services import conversion_service, history_service
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "img.png"
    Image.new("RGB", (30, 30), color=(5, 5, 5)).save(path)
    return path


def test_conversion_records_history(sample_png: Path) -> None:
    history_service.clear()
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    task = conversion_service.convert_single(sample_png, options)
    assert task.status.value == "succeeded"
    entries = history_service.list_entries()
    assert len(entries) == 1
    assert entries[0].source == str(sample_png)
    assert entries[0].status == "succeeded"


def test_failed_conversion_records_history(tmp_path: Path) -> None:
    history_service.clear()
    bad = tmp_path / "bad.png"
    bad.write_bytes(b"garbage")
    options = ConversionOptions(target_format="PNG")
    task = conversion_service.convert_single(bad, options)
    assert task.status.value == "failed"
    entries = history_service.list_entries()
    assert len(entries) == 1
    assert entries[0].status == "failed"
    assert entries[0].error is not None
