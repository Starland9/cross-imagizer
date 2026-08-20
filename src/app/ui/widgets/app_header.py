"""En-tête de l'application avec icône et titre."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget

from app.ui.resources import icons
from app.ui.theme import tokens


class AppHeader(QWidget):
    """En-tête compact affichant l'identité visuelle de l'application."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFixedHeight(tokens.HEADER_HEIGHT)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(
            tokens.SPACING_MEDIUM,
            tokens.SPACING_SMALL,
            tokens.SPACING_MEDIUM,
            tokens.SPACING_SMALL,
        )
        layout.setSpacing(tokens.SPACING_MEDIUM)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self._icon_label = QLabel()
        self._icon_label.setPixmap(icons.app_icon().pixmap(32, 32))
        layout.addWidget(self._icon_label)

        self._title_label = QLabel("Cross-Imagizer")
        font = self._title_label.font()
        font.setPointSize(tokens.FONT_SIZE_HEADING)
        font.setWeight(QFont.Weight.Bold)
        self._title_label.setFont(font)
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self._title_label)

        self._subtitle_label = QLabel("Convertisseur d'images multi-formats")
        self._subtitle_label.setObjectName("appHeaderSubtitle")
        self._subtitle_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self._subtitle_label)

        layout.addStretch()

    def apply_theme(self, dark: bool) -> None:
        """Met à jour les couleurs de l'en-tête selon le thème."""
        bg = tokens.COLOR_DARK_SURFACE if dark else tokens.COLOR_LIGHT_SURFACE
        text = tokens.COLOR_DARK_TEXT if dark else tokens.COLOR_LIGHT_TEXT
        muted = tokens.COLOR_DARK_TEXT_MUTED if dark else tokens.COLOR_LIGHT_TEXT_MUTED
        border = tokens.COLOR_DARK_BORDER if dark else tokens.COLOR_LIGHT_BORDER
        self.setStyleSheet(
            f"""
            QWidget#appHeader {{
                background-color: {bg};
                border-bottom: 1px solid {border};
                color: {text};
            }}
            QLabel#appHeaderSubtitle {{
                color: {muted};
                font-size: {tokens.FONT_SIZE_BODY}px;
            }}
            """
        )
