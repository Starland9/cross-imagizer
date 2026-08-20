"""Panneau d'affichage de l'historique des conversions."""

from __future__ import annotations

from PySide6.QtWidgets import QListWidget, QVBoxLayout, QWidget

from app.services import history_service


class HistoryPanel(QWidget):
    """Affiche l'historique des conversions."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self._list = QListWidget()
        layout.addWidget(self._list)
        self.refresh()

    def refresh(self) -> None:
        """Recharge l'historique depuis le service."""
        self._list.clear()
        for entry in history_service.list_entries():
            status = entry.status
            if entry.error:
                text = f"[{status}] {entry.source} — {entry.error}"
            else:
                text = f"[{status}] {entry.source} → {entry.output}"
            self._list.addItem(text)
