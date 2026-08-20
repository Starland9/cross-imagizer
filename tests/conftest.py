"""Configuration pytest : QApplication et isolation de QSettings."""

from __future__ import annotations

import pytest
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp() -> QApplication:
    """Crée une QApplication unique pour la session de test."""
    app = QApplication.instance() or QApplication([])
    app.setOrganizationName("CrossImagizerTest")
    app.setApplicationName("CrossImagizerTest")
    return app


@pytest.fixture(autouse=True)
def _isolate_settings(qapp: QApplication) -> None:
    """Réinitialise QSettings avant chaque test pour l'isolation."""
    QSettings().clear()
