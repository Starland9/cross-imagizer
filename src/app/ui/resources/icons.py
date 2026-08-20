"""Icônes et assets de l'interface (générées programmatiquement)."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPen, QPixmap

DrawFn = Callable[[QPainter, int], None]


def _make_pixmap(draw: DrawFn, size: int = 64) -> QPixmap:
    """Crée un pixmap et applique la fonction de dessin ``draw``."""
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    draw(painter, size)
    painter.end()
    return pixmap


def _draw_convert(painter: QPainter, size: int) -> None:
    """Dessine une icône de conversion (deux flèches circulaires)."""
    pen = QPen(QColor("#2563eb"), size * 0.08)
    painter.setPen(pen)
    painter.setBrush(Qt.BrushStyle.NoBrush)
    rect = QRectF(size * 0.2, size * 0.2, size * 0.6, size * 0.6)
    painter.drawArc(rect, 30 * 16, 300 * 16)
    # Flèches
    painter.drawLine(QPointF(size * 0.5, size * 0.15), QPointF(size * 0.5, size * 0.3))
    painter.drawLine(QPointF(size * 0.5, size * 0.15), QPointF(size * 0.42, size * 0.22))
    painter.drawLine(QPointF(size * 0.5, size * 0.15), QPointF(size * 0.58, size * 0.22))


def _draw_add(painter: QPainter, size: int) -> None:
    """Dessine une icône « plus »."""
    pen = QPen(QColor("#2563eb"), size * 0.1)
    painter.setPen(pen)
    painter.drawLine(QPointF(size * 0.5, size * 0.2), QPointF(size * 0.5, size * 0.8))
    painter.drawLine(QPointF(size * 0.2, size * 0.5), QPointF(size * 0.8, size * 0.5))


def _draw_theme(painter: QPainter, size: int) -> None:
    """Dessine une icône de thème (cercle mi-clair mi-sombre)."""
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor("#2563eb"))
    painter.drawEllipse(QRectF(size * 0.2, size * 0.2, size * 0.6, size * 0.6))
    painter.setBrush(QColor("#ffffff"))
    painter.drawPie(QRectF(size * 0.2, size * 0.2, size * 0.6, size * 0.6), 90 * 16, 180 * 16)


def convert_icon() -> QIcon:
    """Icône de conversion."""
    return QIcon(_make_pixmap(_draw_convert))


def add_icon() -> QIcon:
    """Icône « ajouter »."""
    return QIcon(_make_pixmap(_draw_add))


def theme_icon() -> QIcon:
    """Icône de thème."""
    return QIcon(_make_pixmap(_draw_theme))


def app_icon() -> QIcon:
    """Icône de l'application."""
    return convert_icon()
