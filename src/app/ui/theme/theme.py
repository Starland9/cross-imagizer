"""Système de thème (clair/sombre) via QSS."""

from __future__ import annotations

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from app.ui.theme import tokens


def _light_qss() -> str:
    t = tokens
    return f"""
QWidget {{
    background-color: {t.COLOR_LIGHT_BG};
    color: {t.COLOR_LIGHT_TEXT};
    font-family: {t.FONT_FAMILY};
    font-size: {t.FONT_SIZE_BODY}px;
}}
QMainWindow, QDialog {{
    background-color: {t.COLOR_LIGHT_BG};
}}
QGroupBox {{
    border: 1px solid {t.COLOR_LIGHT_BORDER};
    border-radius: 8px;
    margin: {t.SPACING_MEDIUM}px;
    margin-top: {t.SPACING_LARGE}px;
    padding: {t.SPACING_MEDIUM}px;
    padding-top: {t.SPACING_LARGE}px;
    font-size: {t.FONT_SIZE_TITLE}px;
    font-weight: {t.FONT_WEIGHT_TITLE};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: {t.SPACING_MEDIUM}px;
    padding: 0 {t.SPACING_SMALL}px;
    color: {t.COLOR_LIGHT_TEXT_MUTED};
    font-weight: {t.FONT_WEIGHT_TITLE};
}}
QPushButton {{
    background-color: {t.COLOR_LIGHT_PRIMARY};
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: {t.SPACING_MEDIUM}px {t.SPACING_LARGE}px;
    font-weight: {t.FONT_WEIGHT_BUTTON};
    min-height: 24px;
}}
QPushButton:hover {{
    background-color: {t.COLOR_LIGHT_PRIMARY_HOVER};
}}
QPushButton:pressed {{
    background-color: {t.COLOR_LIGHT_PRIMARY_PRESSED};
}}
QPushButton:disabled {{
    background-color: {t.COLOR_LIGHT_DISABLED_BG};
    color: {t.COLOR_LIGHT_DISABLED_TEXT};
}}
QPushButton#secondary {{
    background-color: {t.COLOR_LIGHT_SECONDARY_BG};
    color: {t.COLOR_LIGHT_TEXT};
}}
QPushButton#secondary:hover {{
    background-color: {t.COLOR_LIGHT_SECONDARY_HOVER};
}}
QPushButton#secondary:pressed {{
    background-color: {t.COLOR_LIGHT_BORDER};
}}
QPushButton#secondary:disabled {{
    background-color: {t.COLOR_LIGHT_DISABLED_BG};
    color: {t.COLOR_LIGHT_DISABLED_TEXT};
}}
QLineEdit, QComboBox, QSpinBox {{
    background-color: {t.COLOR_LIGHT_SURFACE};
    border: 1px solid {t.COLOR_LIGHT_BORDER};
    border-radius: 6px;
    padding: {t.SPACING_SMALL}px {t.SPACING_MEDIUM}px;
    selection-background-color: {t.COLOR_LIGHT_PRIMARY};
}}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus {{
    border: 1px solid {t.COLOR_LIGHT_PRIMARY};
}}
QComboBox::drop-down {{
    border: none;
}}
QProgressBar {{
    background-color: {t.COLOR_LIGHT_SECONDARY_BG};
    border: none;
    border-radius: 6px;
    text-align: center;
    height: 18px;
}}
QProgressBar::chunk {{
    background-color: {t.COLOR_LIGHT_PRIMARY};
    border-radius: 6px;
}}
QListWidget {{
    background-color: {t.COLOR_LIGHT_SURFACE};
    border: 1px solid {t.COLOR_LIGHT_BORDER};
    border-radius: 6px;
    padding: {t.SPACING_SMALL}px;
}}
QLabel {{
    font-weight: {t.FONT_WEIGHT_LABEL};
}}
"""


def _dark_qss() -> str:
    t = tokens
    return f"""
QWidget {{
    background-color: {t.COLOR_DARK_BG};
    color: {t.COLOR_DARK_TEXT};
    font-family: {t.FONT_FAMILY};
    font-size: {t.FONT_SIZE_BODY}px;
}}
QMainWindow, QDialog {{
    background-color: {t.COLOR_DARK_BG};
}}
QGroupBox {{
    border: 1px solid {t.COLOR_DARK_BORDER};
    border-radius: 8px;
    margin: {t.SPACING_MEDIUM}px;
    margin-top: {t.SPACING_LARGE}px;
    padding: {t.SPACING_MEDIUM}px;
    padding-top: {t.SPACING_LARGE}px;
    font-size: {t.FONT_SIZE_TITLE}px;
    font-weight: {t.FONT_WEIGHT_TITLE};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: {t.SPACING_MEDIUM}px;
    padding: 0 {t.SPACING_SMALL}px;
    color: {t.COLOR_DARK_TEXT_MUTED};
    font-weight: {t.FONT_WEIGHT_TITLE};
}}
QPushButton {{
    background-color: {t.COLOR_DARK_PRIMARY};
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: {t.SPACING_MEDIUM}px {t.SPACING_LARGE}px;
    font-weight: {t.FONT_WEIGHT_BUTTON};
    min-height: 24px;
}}
QPushButton:hover {{
    background-color: {t.COLOR_DARK_PRIMARY_HOVER};
}}
QPushButton:pressed {{
    background-color: {t.COLOR_DARK_PRIMARY_PRESSED};
}}
QPushButton:disabled {{
    background-color: {t.COLOR_DARK_DISABLED_BG};
    color: {t.COLOR_DARK_DISABLED_TEXT};
}}
QPushButton#secondary {{
    background-color: {t.COLOR_DARK_SECONDARY_BG};
    color: {t.COLOR_DARK_TEXT};
}}
QPushButton#secondary:hover {{
    background-color: {t.COLOR_DARK_SECONDARY_HOVER};
}}
QPushButton#secondary:pressed {{
    background-color: {t.COLOR_DARK_BORDER};
}}
QPushButton#secondary:disabled {{
    background-color: {t.COLOR_DARK_DISABLED_BG};
    color: {t.COLOR_DARK_DISABLED_TEXT};
}}
QLineEdit, QComboBox, QSpinBox {{
    background-color: {t.COLOR_DARK_SURFACE};
    border: 1px solid {t.COLOR_DARK_BORDER};
    border-radius: 6px;
    padding: {t.SPACING_SMALL}px {t.SPACING_MEDIUM}px;
    color: {t.COLOR_DARK_TEXT};
    selection-background-color: {t.COLOR_DARK_PRIMARY};
}}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus {{
    border: 1px solid {t.COLOR_DARK_PRIMARY};
}}
QComboBox::drop-down {{
    border: none;
}}
QProgressBar {{
    background-color: {t.COLOR_DARK_SURFACE};
    border: none;
    border-radius: 6px;
    text-align: center;
    height: 18px;
}}
QProgressBar::chunk {{
    background-color: {t.COLOR_DARK_PRIMARY};
    border-radius: 6px;
}}
QListWidget {{
    background-color: {t.COLOR_DARK_SURFACE};
    border: 1px solid {t.COLOR_DARK_BORDER};
    border-radius: 6px;
    padding: {t.SPACING_SMALL}px;
}}
QLabel {{
    font-weight: {t.FONT_WEIGHT_LABEL};
}}
"""


def apply_theme(app: QApplication, dark: bool) -> None:
    """Applique le thème clair ou sombre à l'application."""
    app.setStyleSheet(_dark_qss() if dark else _light_qss())
    palette = QPalette()
    if dark:
        palette.setColor(QPalette.ColorRole.Window, QColor("#111827"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#e5e7eb"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#1f2937"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#e5e7eb"))
    else:
        palette.setColor(QPalette.ColorRole.Window, QColor("#fafafa"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#1f2937"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#1f2937"))
    app.setPalette(palette)
