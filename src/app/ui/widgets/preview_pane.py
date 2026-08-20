"""Panneau d'aperçu d'une image."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PreviewPane(QWidget):
    """Affiche un aperçu fidèle de l'image sélectionnée."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self._label = QLabel("Aucune image sélectionnée")
        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label.setMinimumSize(320, 240)
        self._label.setStyleSheet("border: 1px solid #94a3b8; border-radius: 8px;")
        layout.addWidget(self._label)

    def show_image(self, path: Path) -> None:
        """Affiche l'image située à ``path``."""
        pixmap = QPixmap(str(path))
        if pixmap.isNull():
            self._label.setText("Impossible d'afficher l'aperçu")
            return
        scaled = pixmap.scaled(
            self._label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self._label.setPixmap(scaled)

    def clear(self) -> None:
        """Efface l'aperçu."""
        self._label.setPixmap(QPixmap())
        self._label.setText("Aucune image sélectionnée")
