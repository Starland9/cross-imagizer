"""Widget d'état vide réutilisable."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.ui.theme import tokens


class EmptyStateWidget(QWidget):
    """Affiche un message d'invitation avec une icône et un sous-titre."""

    def __init__(
        self,
        icon: QIcon,
        title: str,
        subtitle: str = "",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(tokens.SPACING_MEDIUM)

        self._icon_label = QLabel()
        self._icon_label.setPixmap(icon.pixmap(48, 48))
        self._icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._icon_label)

        self._title_label = QLabel(title)
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setStyleSheet(
            f"font-size: {tokens.FONT_SIZE_TITLE}px; font-weight: {tokens.FONT_WEIGHT_TITLE};"
        )
        layout.addWidget(self._title_label)

        self._subtitle_label = QLabel(subtitle)
        self._subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._subtitle_label.setWordWrap(True)
        self._subtitle_label.setObjectName("emptySubtitle")
        layout.addWidget(self._subtitle_label)

    def apply_theme(self, dark: bool) -> None:
        """Met à jour la couleur du sous-titre selon le thème."""
        color = tokens.COLOR_DARK_TEXT_MUTED if dark else tokens.COLOR_LIGHT_TEXT_MUTED
        self._subtitle_label.setStyleSheet(f"color: {color}; font-size: {tokens.FONT_SIZE_BODY}px;")
