"""Onglets latéraux regroupant file d'attente et historique."""

from __future__ import annotations

from PySide6.QtWidgets import QTabWidget, QWidget

from app.ui.theme import tokens
from app.ui.widgets.batch_panel import BatchPanel
from app.ui.widgets.history_panel import HistoryPanel


class SideTabs(QTabWidget):
    """Regroupe BatchPanel et HistoryPanel dans deux onglets."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setMinimumWidth(tokens.SIDE_TABS_MIN_WIDTH)

        self._batch = BatchPanel()
        self._history = HistoryPanel()

        self.addTab(self._batch, "File d'attente")
        self.addTab(self._history, "Historique")

    @property
    def batch_panel(self) -> BatchPanel:
        return self._batch

    @property
    def history_panel(self) -> HistoryPanel:
        return self._history
