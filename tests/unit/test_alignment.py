"""Tests de l'alignement des widgets."""

from __future__ import annotations

import pytest

from app.ui.widgets.options_panel import OptionsPanel

pytest.importorskip("PySide6")


def test_options_panel_uses_form_layout(qtbot) -> None:  # type: ignore[no-untyped-def]
    panel = OptionsPanel()
    qtbot.addWidget(panel)
    layout = panel.layout()
    # QFormLayout garantit l'alignement labels/champs.
    from PySide6.QtWidgets import QFormLayout

    assert isinstance(layout, QFormLayout)


def test_options_panel_label_field_alignment(qtbot) -> None:  # type: ignore[no-untyped-def]
    panel = OptionsPanel()
    qtbot.addWidget(panel)
    layout = panel.layout()
    assert layout is not None
    # Le QFormLayout aligne les labels (colonne 0) et les champs (colonne 1).
    assert layout.rowCount() >= 5  # noqa: PLR2004
