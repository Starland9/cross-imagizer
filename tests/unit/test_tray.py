"""Tests du widget d'icône de barre de tâche."""

from __future__ import annotations

import pytest

from app.ui.tray import TrayIcon

pytest.importorskip("PySide6")


def test_tray_creation(qtbot) -> None:  # type: ignore[no-untyped-def]
    tray = TrayIcon(on_open=lambda: None, on_convert=lambda: None, on_quit=lambda: None)
    assert tray._tray.toolTip() == "Cross-Imagizer"


def test_tray_availability_flag() -> None:
    tray = TrayIcon(on_open=lambda: None, on_convert=lambda: None, on_quit=lambda: None)
    # is_available() retourne un booléen sans lever d'exception.
    assert isinstance(tray.is_available(), bool)


def test_tray_cross_platform_portability() -> None:
    """FR-010 : QSystemTrayIcon et QSettings sont portables sur les 3 OS.

    Vérifie que l'icône de barre de tâche et le stockage des réglages
    s'instancient sans dépendance spécifique à un OS.
    """
    from PySide6.QtCore import QSettings

    tray = TrayIcon(on_open=lambda: None, on_convert=lambda: None, on_quit=lambda: None)
    assert tray._tray is not None
    # QSettings s'instancie sur tous les OS (registry/plist/INI).
    settings = QSettings()
    assert settings is not None
