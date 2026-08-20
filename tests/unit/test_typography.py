"""Tests de la hiérarchie typographique."""

from __future__ import annotations

from app.ui.theme import tokens


def test_typography_hierarchy_in_tokens() -> None:
    """Les tokens définissent une hiérarchie typographique claire."""
    assert tokens.FONT_WEIGHT_TITLE > tokens.FONT_WEIGHT_LABEL
    assert tokens.FONT_WEIGHT_BUTTON > tokens.FONT_WEIGHT_NORMAL
    assert tokens.FONT_SIZE_HEADING > tokens.FONT_SIZE_TITLE > tokens.FONT_SIZE_BODY
    assert tokens.FONT_SIZE_BODY > tokens.FONT_SIZE_SMALL


def test_title_weight_heavier_than_body() -> None:
    assert tokens.FONT_WEIGHT_TITLE >= tokens.FONT_WEIGHT_BUTTON
