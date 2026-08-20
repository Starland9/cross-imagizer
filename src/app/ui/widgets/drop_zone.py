"""Zone de dépôt de fichiers (glisser-déposer)."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QStackedLayout, QWidget

from app.ui.resources import icons
from app.ui.theme import tokens
from app.ui.widgets.empty_state import EmptyStateWidget
from app.ui.widgets.preview_pane import PreviewPane


class DropZone(QWidget):
    """Bandeau compact acceptant le glisser-déposer et affichant un aperçu."""

    files_dropped = Signal(list)
    clicked = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFixedHeight(tokens.DROP_ZONE_COMPACT_HEIGHT)
        self.setMinimumHeight(tokens.DROP_ZONE_COMPACT_HEIGHT)
        self.setMaximumHeight(tokens.DROP_ZONE_PREVIEW_MAX_HEIGHT)
        self.setObjectName("dropZone")

        self._stack = QStackedLayout(self)
        self._stack.setContentsMargins(0, 0, 0, 0)
        self._stack.setSpacing(0)

        self._empty_state = EmptyStateWidget(
            icons.image_icon(),
            "Glissez-déposez des images ici",
            "ou cliquez pour parcourir",
        )
        self._empty_state.setObjectName("dropEmpty")
        self._stack.addWidget(self._empty_state)

        self._preview = PreviewPane()
        self._preview.setObjectName("dropPreview")
        self._stack.addWidget(self._preview)

        self._stack.setCurrentIndex(0)

    def mousePressEvent(self, event: object) -> None:  # noqa: N802
        self.clicked.emit()

    def show_empty(self) -> None:
        """Affiche le message d'invitation."""
        self.setFixedHeight(tokens.DROP_ZONE_COMPACT_HEIGHT)
        self._stack.setCurrentIndex(0)

    def show_preview(self, path: Path) -> None:
        """Affiche l'aperçu de l'image dans le bandeau."""
        self.setMaximumHeight(tokens.DROP_ZONE_PREVIEW_MAX_HEIGHT)
        self.setMinimumHeight(tokens.DROP_ZONE_COMPACT_HEIGHT)
        self.setFixedHeight(tokens.DROP_ZONE_PREVIEW_MAX_HEIGHT)
        self._preview.show_image(path)
        self._stack.setCurrentIndex(1)

    def apply_theme(self, dark: bool) -> None:
        """Met à jour le style du bandeau selon le thème."""
        border = tokens.COLOR_DARK_BORDER if dark else tokens.COLOR_LIGHT_BORDER
        bg = tokens.COLOR_DARK_SURFACE if dark else tokens.COLOR_LIGHT_SURFACE
        self.setStyleSheet(
            f"""
            QWidget#dropZone {{
                border: 2px dashed {border};
                border-radius: 10px;
                background-color: {bg};
            }}
            """
        )
        self._empty_state.apply_theme(dark)

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
