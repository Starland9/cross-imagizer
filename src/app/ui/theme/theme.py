"""Système de thème (clair/sombre) via QSS."""

from __future__ import annotations

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

_LIGHT_QSS = """
QWidget {
    background-color: #fafafa;
    color: #1f2937;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 13px;
}
QMainWindow, QDialog {
    background-color: #fafafa;
}
QPushButton {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #1d4ed8;
}
QPushButton:pressed {
    background-color: #1e40af;
}
QPushButton:disabled {
    background-color: #cbd5e1;
    color: #64748b;
}
QPushButton#secondary {
    background-color: #e2e8f0;
    color: #1f2937;
}
QPushButton#secondary:hover {
    background-color: #cbd5e1;
}
QLineEdit, QComboBox, QSpinBox {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 6px 8px;
}
QComboBox::drop-down {
    border: none;
}
QProgressBar {
    background-color: #e2e8f0;
    border: none;
    border-radius: 6px;
    text-align: center;
    height: 18px;
}
QProgressBar::chunk {
    background-color: #2563eb;
    border-radius: 6px;
}
QListWidget {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
}
QGroupBox {
    border: 1px solid #d1d5db;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 8px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 4px;
    color: #4b5563;
}
"""

_DARK_QSS = """
QWidget {
    background-color: #111827;
    color: #e5e7eb;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 13px;
}
QMainWindow, QDialog {
    background-color: #111827;
}
QPushButton {
    background-color: #3b82f6;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #2563eb;
}
QPushButton:pressed {
    background-color: #1d4ed8;
}
QPushButton:disabled {
    background-color: #374151;
    color: #6b7280;
}
QPushButton#secondary {
    background-color: #1f2937;
    color: #e5e7eb;
}
QPushButton#secondary:hover {
    background-color: #374151;
}
QLineEdit, QComboBox, QSpinBox {
    background-color: #1f2937;
    border: 1px solid #374151;
    border-radius: 6px;
    padding: 6px 8px;
    color: #e5e7eb;
}
QComboBox::drop-down {
    border: none;
}
QProgressBar {
    background-color: #1f2937;
    border: none;
    border-radius: 6px;
    text-align: center;
    height: 18px;
}
QProgressBar::chunk {
    background-color: #3b82f6;
    border-radius: 6px;
}
QListWidget {
    background-color: #1f2937;
    border: 1px solid #374151;
    border-radius: 6px;
}
QGroupBox {
    border: 1px solid #374151;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 8px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 4px;
    color: #9ca3af;
}
"""


def apply_theme(app: QApplication, dark: bool) -> None:
    """Applique le thème clair ou sombre à l'application."""
    app.setStyleSheet(_DARK_QSS if dark else _LIGHT_QSS)
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
