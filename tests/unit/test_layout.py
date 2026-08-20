"""Tests de la mise en page équilibrée de la fenêtre principale."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow

pytest.importorskip("PySide6")


def test_main_window_uses_splitter(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    # La fenêtre doit exposer un QSplitter pour le corps (mise en page équilibrée).
    assert window._splitter is not None
    # Le splitter contient les panneaux principaux.
    assert window._splitter.count() >= 3
