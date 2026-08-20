"""Tests unitaires du modèle HistoryEntry."""

from __future__ import annotations

from models.history import HistoryEntry


def test_create_sets_timestamp() -> None:
    entry = HistoryEntry.create("a.png", "a.jpg", "succeeded")
    assert entry.source == "a.png"
    assert entry.output == "a.jpg"
    assert entry.status == "succeeded"
    assert entry.timestamp != ""
    assert entry.error is None


def test_roundtrip_dict() -> None:
    entry = HistoryEntry.create("a.png", None, "failed", error="boom")
    data = entry.to_dict()
    restored = HistoryEntry.from_dict(data)
    assert restored.source == "a.png"
    assert restored.output is None
    assert restored.status == "failed"
    assert restored.error == "boom"
    assert restored.timestamp == entry.timestamp
