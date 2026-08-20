"""Panneau d'options de conversion (format, qualité, dimensions)."""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGroupBox,
    QSpinBox,
    QWidget,
)

from app.core import formats
from models import CollisionPolicy, ConversionOptions


class OptionsPanel(QGroupBox):
    """Regroupe les options de conversion."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("Options de conversion", parent)

        layout = QFormLayout(self)

        self._format = QComboBox()
        self._format.addItems(formats.supported_formats())
        layout.addRow("Format cible :", self._format)

        self._quality = QSpinBox()
        self._quality.setRange(1, 100)
        self._quality.setValue(90)
        layout.addRow("Qualité :", self._quality)

        self._width = QSpinBox()
        self._width.setRange(0, 100000)
        self._width.setValue(0)
        self._width.setSpecialValueText("Auto")
        layout.addRow("Largeur :", self._width)

        self._height = QSpinBox()
        self._height.setRange(0, 100000)
        self._height.setValue(0)
        self._height.setSpecialValueText("Auto")
        layout.addRow("Hauteur :", self._height)

        self._collision = QComboBox()
        self._collision.addItem("Renommer", CollisionPolicy.RENAME)
        self._collision.addItem("Écraser", CollisionPolicy.OVERWRITE)
        self._collision.addItem("Demander", CollisionPolicy.ASK)
        layout.addRow("Conflit de nom :", self._collision)

    def options(self) -> ConversionOptions:
        """Construit les options de conversion à partir des champs."""
        return ConversionOptions(
            target_format=self._format.currentText(),
            quality=self._quality.value(),
            resize_width=self._width.value() or None,
            resize_height=self._height.value() or None,
            collision_policy=self._collision.currentData(),
        )
