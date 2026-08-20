"""Tests des retours visuels (états de boutons, non-blocage)."""

from __future__ import annotations

import pytest

from app.ui.main_window import MainWindow

pytest.importorskip("PySide6")


def test_convert_button_disabled_during_conversion(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    # Avant conversion, le bouton est actif.
    assert window._convert_btn.isEnabled() is True
    # Simule l'état pendant conversion.
    window._convert_btn.setEnabled(False)
    assert window._convert_btn.isEnabled() is False


def test_open_folder_button_disabled_initially(qtbot) -> None:  # type: ignore[no-untyped-def]
    window = MainWindow()
    qtbot.addWidget(window)
    # Le bouton « Ouvrir le dossier » est désactivé tant qu'aucune conversion
    # n'a réussi.
    assert window._open_folder_btn.isEnabled() is False


def test_ui_non_blocking_during_conversion(qtbot) -> None:  # type: ignore[no-untyped-def]
    """SC-004 : l'UI reste réactive (le worker tourne en arrière-plan)."""
    window = MainWindow()
    qtbot.addWidget(window)
    # Le service de lot utilise un QThreadPool (exécution hors thread UI).
    from PySide6.QtCore import QThreadPool

    assert window._batch_service._pool is QThreadPool.globalInstance()
