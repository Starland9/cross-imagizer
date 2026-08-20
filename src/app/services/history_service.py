"""Enregistrement et lecture de l'historique des conversions."""

from __future__ import annotations

import json

from PySide6.QtCore import QSettings

from models.history import HistoryEntry

_KEY = "history"
_MAX_ENTRIES = 500


def record(
    source: str,
    output: str | None,
    status: str,
    error: str | None = None,
) -> None:
    """Ajoute une entrée à l'historique et persiste (purge au-delà de 500)."""
    entry = HistoryEntry.create(source, output, status, error)
    entries = list_entries()
    entries.insert(0, entry)
    entries = entries[:_MAX_ENTRIES]
    _save(entries)


def list_entries() -> list[HistoryEntry]:
    """Retourne l'historique, du plus récent au plus ancien."""
    settings = QSettings()
    raw = settings.value(_KEY)
    if raw is None:
        return []
    try:
        data = json.loads(str(raw))
    except (json.JSONDecodeError, TypeError):
        return []
    return [HistoryEntry.from_dict(item) for item in data]


def clear() -> None:
    """Vide l'historique."""
    settings = QSettings()
    settings.remove(_KEY)


def _save(entries: list[HistoryEntry]) -> None:
    settings = QSettings()
    settings.setValue(_KEY, json.dumps([e.to_dict() for e in entries]))
