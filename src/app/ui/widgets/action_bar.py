"""Barre d'actions hiérarchisée avec groupe primaire et secondaires."""

from __future__ import annotations

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from app.ui.resources import icons
from app.ui.theme import tokens


class ActionBar(QWidget):
    """Barre du bas regroupant les actions par fonction."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFixedHeight(tokens.ACTION_BAR_HEIGHT)

        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(
            tokens.SPACING_MEDIUM,
            tokens.SPACING_SMALL,
            tokens.SPACING_MEDIUM,
            tokens.SPACING_SMALL,
        )
        self._layout.setSpacing(tokens.SPACING_LARGE)

        # Groupe Fichier
        self._file_group = QHBoxLayout()
        self._file_group.setSpacing(tokens.SPACING_MEDIUM)
        self._add_btn = QPushButton("Ajouter")
        self._add_btn.setIcon(icons.add_icon())
        self._add_btn.setToolTip("Ajouter des images")
        self._file_group.addWidget(self._add_btn)

        self._output_btn = QPushButton("Sortie…")
        self._output_btn.setToolTip("Choisir le dossier de sortie")
        self._file_group.addWidget(self._output_btn)

        self._open_folder_btn = QPushButton("Ouvrir")
        self._open_folder_btn.setToolTip("Ouvrir le dossier de sortie")
        self._open_folder_btn.setEnabled(False)
        self._file_group.addWidget(self._open_folder_btn)
        self._layout.addLayout(self._file_group)

        self._layout.addStretch()

        # Groupe Contrôle
        self._control_group = QHBoxLayout()
        self._control_group.setSpacing(tokens.SPACING_MEDIUM)
        self._convert_btn = QPushButton("Convertir")
        self._convert_btn.setObjectName("primary")
        self._convert_btn.setIcon(icons.convert_icon())
        font = self._convert_btn.font()
        font.setPointSize(tokens.FONT_SIZE_TITLE)
        font.setWeight(QFont.Weight.Bold)
        self._convert_btn.setFont(font)
        self._control_group.addWidget(self._convert_btn)

        self._cancel_btn = QPushButton("Annuler")
        self._cancel_btn.setEnabled(False)
        self._control_group.addWidget(self._cancel_btn)
        self._layout.addLayout(self._control_group)

        # Groupe Affichage
        self._view_group = QHBoxLayout()
        self._view_group.setSpacing(tokens.SPACING_MEDIUM)
        self._theme_btn = QPushButton("Thème sombre")
        self._theme_btn.setIcon(icons.theme_icon())
        self._view_group.addWidget(self._theme_btn)
        self._layout.addLayout(self._view_group)

    # Boutons exposés
    @property
    def add_button(self) -> QPushButton:
        return self._add_btn

    @property
    def convert_button(self) -> QPushButton:
        return self._convert_btn

    @property
    def cancel_button(self) -> QPushButton:
        return self._cancel_btn

    @property
    def theme_button(self) -> QPushButton:
        return self._theme_btn

    @property
    def output_button(self) -> QPushButton:
        return self._output_btn

    @property
    def open_folder_button(self) -> QPushButton:
        return self._open_folder_btn

    def apply_theme(self, dark: bool) -> None:
        """Met à jour le style de la barre selon le thème."""
        bg = tokens.COLOR_DARK_SURFACE if dark else tokens.COLOR_LIGHT_SURFACE
        border = tokens.COLOR_DARK_BORDER if dark else tokens.COLOR_LIGHT_BORDER
        self.setStyleSheet(
            f"""
            QWidget#actionBar {{
                background-color: {bg};
                border-top: 1px solid {border};
            }}
            """
        )
