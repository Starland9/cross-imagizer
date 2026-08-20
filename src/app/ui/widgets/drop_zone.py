"""Zone de dépôt de fichiers (glisser-déposer)."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DropZone(QWidget):
    """Zone acceptant le glisser-déposer de fichiers images."""

    files_dropped = Signal(list)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setMinimumHeight(120)
        self.setObjectName("dropZone")

        layout = QVBoxLayout(self)
        self._label = QLabel("Glissez vos images ici\nou utilisez le bouton ci-dessous")
        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._label)

        self.setStyleSheet(
            """
            QWidget#dropZone {
                border: 2px dashed #94a3b8;
                border-radius: 10px;
                background-color: transparent;
            }
            """
        )

    def dragEnterEvent(self, event: object) -> None:  # noqa: N802
        if event.mimeData().hasUrls():  # type: ignore[attr-defined]
            event.acceptProposedAction()  # type: ignore[attr-defined]

    def dropEvent(self, event: object) -> None:  # noqa: N802
        paths = [
            Path(url.toLocalFile())
            for url in event.mimeData().urls()  # type: ignore[attr-defined]
            if url.isLocalFile()
        ]
        if paths:
            self.files_dropped.emit(paths)
            event.acceptProposedAction()  # type: ignore[attr-defined]
