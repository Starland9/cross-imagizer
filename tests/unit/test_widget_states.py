"""Tests des états visuels des widgets interactifs."""

from __future__ import annotations

import pytest

from app.ui.theme.theme import _dark_qss, _light_qss

pytest.importorskip("PySide6")


def test_light_qss_has_hover_pressed_disabled() -> None:
    qss = _light_qss()
    assert "QPushButton:hover" in qss
    assert "QPushButton:pressed" in qss
    assert "QPushButton:disabled" in qss
    assert "QPushButton#secondary:hover" in qss
    assert "QPushButton#secondary:pressed" in qss
    assert "QPushButton#secondary:disabled" in qss


def test_dark_qss_has_hover_pressed_disabled() -> None:
    qss = _dark_qss()
    assert "QPushButton:hover" in qss
    assert "QPushButton:pressed" in qss
    assert "QPushButton:disabled" in qss
    assert "QPushButton#secondary:hover" in qss
    assert "QPushButton#secondary:pressed" in qss
    assert "QPushButton#secondary:disabled" in qss


def test_both_themes_define_focus_state() -> None:
    """SC-004 : les champs de saisie affichent un état de focus."""
    assert "QLineEdit:focus" in _light_qss()
    assert "QLineEdit:focus" in _dark_qss()


def test_ui_uses_threadpool_non_blocking(qtbot) -> None:  # type: ignore[no-untyped-def]
    """SC-004 : l'UI reste réactive (le worker tourne en arrière-plan)."""
    from PySide6.QtCore import QThreadPool

    from app.ui.main_window import MainWindow

    window = MainWindow()
    qtbot.addWidget(window)
    assert window._batch_service._pool is QThreadPool.globalInstance()
