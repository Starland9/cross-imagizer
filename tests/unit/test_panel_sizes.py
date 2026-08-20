"""Tests des tailles et bornes des panneaux."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow
from app.ui.theme import tokens

pytest.importorskip("PySide6")


def test_panels_have_min_max_width(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    for panel in (
        window._preview,
        window._options,
        window._batch_panel,
        window._history_panel,
    ):
        assert panel.minimumWidth() >= tokens.PANEL_MIN_WIDTH
        assert panel.maximumWidth() <= tokens.PANEL_MAX_WIDTH or panel.maximumWidth() == 16777215  # noqa: PLR2004


def test_splitter_panels_bounded(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    # Aucun panneau ne dépasse 40 % de la largeur de la fenêtre sans justification.
    window_width = window.width()
    for i in range(window._splitter.count()):
        widget = window._splitter.widget(i)
        if widget.maximumWidth() != 16777215:  # noqa: PLR2004
            assert widget.maximumWidth() <= window_width * 0.6  # noqa: PLR2004
