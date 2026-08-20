"""Point d'entrée de l'application Cross-Imagizer."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.core.logging import setup_logging
from app.ui.main_window import MainWindow
from app.ui.theme.theme import apply_theme


def main() -> int:
    """Lance l'application."""
    setup_logging()
    app = QApplication(sys.argv)
    app.setApplicationName("Cross-Imagizer")
    apply_theme(app, dark=False)

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
