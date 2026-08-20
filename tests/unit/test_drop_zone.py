"""Tests du widget de zone de dépôt."""

from __future__ import annotations

import pytest

from app.ui.widgets.drop_zone import DropZone

pytest.importorskip("PySide6")


def test_drop_zone_creation(qtbot) -> None:  # type: ignore[no-untyped-def]
    zone = DropZone()
    qtbot.addWidget(zone)
    assert zone.minimumHeight() == 120
