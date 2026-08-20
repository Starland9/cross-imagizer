"""Panneau d'affichage de l'historique des conversions."""

from __future__ import annotations

from PySide6.QtWidgets import QListWidget, QStackedLayout, QWidget

from app.services import history_service
from app.ui.resources import icons
from app.ui.widgets.empty_state import EmptyStateWidget


class HistoryPanel(QWidget):
    """Affiche l'historique des conversions."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._stack = QStackedLayout(self)
        self._stack.setContentsMargins(0, 0, 0, 0)

        self._empty_state = EmptyStateWidget(
            icons.history_icon(),
            "Aucune conversion pour le moment",
            "Les conversions terminées apparaîtront ici.",
        )
        self._stack.addWidget(self._empty_state)

        self._list = QListWidget()
        self._stack.addWidget(self._list)

        self.refresh()

    def _update_visibility(self) -> None:
        """Affiche l'état vide si l'historique est vide."""
        self._stack.setCurrentIndex(0 if self._list.count() == 0 else 1)

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
        self._update_visibility()

    def apply_theme(self, dark: bool) -> None:
        """Met à jour l'état vide selon le thème."""
        self._empty_state.apply_theme(dark)
