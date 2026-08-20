"""Tests unitaires des design tokens."""

from __future__ import annotations

from app.ui.theme import tokens


def test_spacing_tokens_positive() -> None:
    assert tokens.SPACING_SMALL > 0
    assert tokens.SPACING_MEDIUM > tokens.SPACING_SMALL
    assert tokens.SPACING_LARGE > tokens.SPACING_MEDIUM


def test_panel_bounds_reasonable() -> None:
    assert tokens.PANEL_MIN_WIDTH < tokens.PANEL_MAX_WIDTH
    assert tokens.PANEL_MIN_WIDTH >= 120
    assert tokens.PANEL_MAX_WIDTH <= 640


def test_font_sizes_hierarchy() -> None:
    assert tokens.FONT_SIZE_SMALL < tokens.FONT_SIZE_BODY
    assert tokens.FONT_SIZE_BODY < tokens.FONT_SIZE_TITLE
    assert tokens.FONT_SIZE_TITLE < tokens.FONT_SIZE_HEADING


def test_colors_light_and_dark_defined() -> None:
    assert tokens.COLOR_LIGHT_PRIMARY != tokens.COLOR_DARK_PRIMARY
    assert tokens.COLOR_LIGHT_BG != tokens.COLOR_DARK_BG
    assert all(
        isinstance(getattr(tokens, attr), str) for attr in dir(tokens) if attr.startswith("COLOR_")
    )
