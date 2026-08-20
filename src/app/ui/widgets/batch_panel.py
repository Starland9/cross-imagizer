"""Panneau de lot : liste des fichiers et progression."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QListWidget, QProgressBar, QStackedLayout, QVBoxLayout, QWidget

from app.ui.resources import icons
from app.ui.widgets.empty_state import EmptyStateWidget


class BatchPanel(QWidget):
    """Affiche la file de conversion et la progression du lot."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._stack = QStackedLayout(self)
        self._stack.setContentsMargins(0, 0, 0, 0)

        self._empty_state = EmptyStateWidget(
            icons.inbox_icon(),
            "Aucune image en attente",
            "Ajoutez des fichiers pour démarrer une conversion.",
        )
        self._stack.addWidget(self._empty_state)

        self._content = QWidget()
        content_layout = QVBoxLayout(self._content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        self._list = QListWidget()
        content_layout.addWidget(self._list)
        self._progress = QProgressBar()
        self._progress.setValue(0)
        content_layout.addWidget(self._progress)
        self._stack.addWidget(self._content)

        self._update_visibility()

    def _update_visibility(self) -> None:
        """Affiche l'état vide si la liste est vide."""
        self._stack.setCurrentIndex(0 if self._list.count() == 0 else 1)

    def add_files(self, paths: list[Path]) -> None:
        """Ajoute des fichiers à la file."""
        for path in paths:
            self._list.addItem(str(path))
        self._update_visibility()

    def clear(self) -> None:
        """Vide la file et réinitialise la progression."""
        self._list.clear()
        self._progress.setValue(0)
        self._update_visibility()

    def set_progress(self, done: int, total: int) -> None:
        """Met à jour la progression."""
        self._progress.setMaximum(total)
        self._progress.setValue(done)

    def files(self) -> list[Path]:
        """Retourne la liste des chemins de la file."""
        return [Path(self._list.item(i).text()) for i in range(self._list.count())]

    def apply_theme(self, dark: bool) -> None:
        """Met à jour l'état vide selon le thème."""
        self._empty_state.apply_theme(dark)
