"""Point d'entrée de l'application Cross-Imagizer."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.core.logging import setup_logging
from app.ui.main_window import MainWindow
from app.ui.resources import icons
from app.ui.theme.theme import apply_theme
from platform_utils import context_menu


def main() -> int:
    """Lance l'application."""
    setup_logging()
    context_menu.register_context_menu()
    app = QApplication(sys.argv)
    app.setApplicationName("Cross-Imagizer")
    app.setWindowIcon(icons.app_icon())
    apply_theme(app, dark=False)

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
