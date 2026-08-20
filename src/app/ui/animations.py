"""Animations légères de l'interface."""

from __future__ import annotations

from PySide6.QtCore import QEasingCurve, QObject, QPropertyAnimation


def fade_in(widget: QObject, duration_ms: int = 200) -> QPropertyAnimation:
    """Applique une animation de fondu à l'apparition d'un widget."""
    animation = QPropertyAnimation(widget, b"windowOpacity", widget)
    animation.setDuration(duration_ms)
    animation.setStartValue(0.0)
    animation.setEndValue(1.0)
    animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    animation.start()
    return animation
