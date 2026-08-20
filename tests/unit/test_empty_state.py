"""Tests for EmptyStateWidget."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel

from app.ui.resources import icons
from app.ui.widgets.empty_state import EmptyStateWidget


def test_empty_state_widgets_exist(qapp: object) -> None:
    widget = EmptyStateWidget(icons.inbox_icon(), "Title", "Subtitle")
    assert isinstance(widget, EmptyStateWidget)
    labels = widget.findChildren(QLabel)
    texts = {label.text() for label in labels}
    assert "Title" in texts
    assert "Subtitle" in texts
