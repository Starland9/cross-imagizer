"""Panneau de lot : liste des fichiers et progression."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QListWidget, QProgressBar, QVBoxLayout, QWidget


class BatchPanel(QWidget):
    """Affiche la file de conversion et la progression du lot."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self._list = QListWidget()
        layout.addWidget(self._list)

        self._progress = QProgressBar()
        self._progress.setValue(0)
        layout.addWidget(self._progress)

    def add_files(self, paths: list[Path]) -> None:
        """Ajoute des fichiers à la file."""
        for path in paths:
            self._list.addItem(str(path))

    def clear(self) -> None:
        """Vide la file et réinitialise la progression."""
        self._list.clear()
        self._progress.setValue(0)

    def set_progress(self, done: int, total: int) -> None:
        """Met à jour la progression."""
        self._progress.setMaximum(total)
        self._progress.setValue(done)

    def files(self) -> list[Path]:
        """Retourne la liste des chemins de la file."""
        return [Path(self._list.item(i).text()) for i in range(self._list.count())]
