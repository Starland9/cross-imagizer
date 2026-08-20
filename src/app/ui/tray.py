"""Icône de barre de tâche (system tray) avec menu contextuel."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from app.ui.resources import icons


class TrayIcon:
    """Icône de barre de tâche avec menu contextuel (ouvrir, convertir, quitter)."""

    def __init__(
        self,
        on_open: Callable[[], None],
        on_convert: Callable[[], None],
        on_quit: Callable[[], None],
    ) -> None:
        self._on_open = on_open
        self._on_convert = on_convert
        self._on_quit = on_quit

        self._tray = QSystemTrayIcon(icons.app_icon())
        self._tray.setToolTip("Cross-Imagizer")

        menu = QMenu()
        open_action = QAction("Ouvrir", menu)
        open_action.triggered.connect(self._on_open)
        menu.addAction(open_action)

        convert_action = QAction("Convertir", menu)
        convert_action.triggered.connect(self._on_convert)
        menu.addAction(convert_action)

        menu.addSeparator()

        quit_action = QAction("Quitter", menu)
        quit_action.triggered.connect(self._on_quit)
        menu.addAction(quit_action)

        self._tray.setContextMenu(menu)
        self._tray.activated.connect(self._on_activated)

    def show(self) -> None:
        """Affiche l'icône de barre de tâche."""
        self._tray.show()

    def hide(self) -> None:
        """Masque l'icône de barre de tâche."""
        self._tray.hide()

    def is_available(self) -> bool:
        """Indique si le system tray est disponible sur cet OS."""
        return QSystemTrayIcon.isSystemTrayAvailable()

    def _on_activated(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        """Ouvre la fenêtre au double-clic sur l'icône."""
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self._on_open()
