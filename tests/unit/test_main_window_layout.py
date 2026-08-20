"""Tests for the new main window vertical layout."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow

pytest.importorskip("PySide6")


def test_main_window_has_section_builders(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    assert hasattr(window, "_build_header")
    assert hasattr(window, "_build_drop_zone")
    assert hasattr(window, "_build_workbench")
    assert hasattr(window, "_build_action_bar")


def test_main_window_vertical_layout_order(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    layout = window.centralWidget().layout()
    assert layout.itemAt(0).widget() is window._header
    assert layout.itemAt(1).widget() is window._drop_zone
    assert layout.itemAt(2).widget() is window._workbench
    assert layout.itemAt(3).widget() is window._action_bar
