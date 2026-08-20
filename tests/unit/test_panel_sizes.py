"""Tests des tailles et bornes des panneaux."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow
from app.ui.theme import tokens

pytest.importorskip("PySide6")


def test_options_panel_width(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    options = window._options
    assert tokens.OPTIONS_PANEL_MIN_WIDTH <= options.width() <= tokens.OPTIONS_PANEL_MAX_WIDTH


def test_splitter_panels_bounded(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    # Aucun panneau ne dépasse 60 % de la largeur de la fenêtre sans justification.
    window_width = window.width()
    for i in range(window._workbench.count()):
        widget = window._workbench.widget(i)
        if widget.maximumWidth() != 16777215:  # noqa: PLR2004
            assert widget.maximumWidth() <= window_width * 0.6  # noqa: PLR2004
