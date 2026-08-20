"""Tests unitaires du service d'historique."""

from __future__ import annotations

from app.services import history_service


def test_list_empty_by_default() -> None:
    history_service.clear()
    assert history_service.list_entries() == []


def test_record_and_list() -> None:
    history_service.clear()
    history_service.record("a.png", "a.jpg", "succeeded")
    history_service.record("b.png", None, "failed", error="boom")
    entries = history_service.list_entries()
    assert len(entries) == 2
    # Le plus récent en premier.
    assert entries[0].source == "b.png"
    assert entries[1].source == "a.png"


def test_clear() -> None:
    history_service.record("a.png", "a.jpg", "succeeded")
    history_service.clear()
    assert history_service.list_entries() == []
