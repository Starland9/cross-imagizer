"""Tests des espacements uniformes."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow

pytest.importorskip("PySide6")


def test_main_window_margins_uniform(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    central = window.centralWidget()
    layout = central.layout()
    assert layout is not None
    margins = layout.contentsMargins()
    # Les marges sont uniformes (gauche = droite, haut = bas, écart ≤ 2 px).
    assert abs(margins.left() - margins.right()) <= 2  # noqa: PLR2004
    assert abs(margins.top() - margins.bottom()) <= 2  # noqa: PLR2004
