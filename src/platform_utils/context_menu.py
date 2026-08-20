"""Intégration au menu contextuel du système (best-effort)."""

from __future__ import annotations

import platform as _platform
import sys
from pathlib import Path

from app.core.logging import get_logger

logger = get_logger()

_APP_NAME = "Cross-Imagizer"


def register_context_menu() -> None:
    """Enregistre l'application dans le menu contextuel du système.

    Implémentation best-effort : selon l'OS, l'enregistrement peut nécessiter
    des privilèges ou des mécanismes spécifiques. Aucune exception n'est levée
    en cas d'échec.
    """
    try:
        system = _platform.system()
        if system == "Windows":
            _register_windows()
        elif system == "Darwin":
            _register_macos()
        else:
            _register_linux()
    except Exception as exc:  # noqa: BLE001
        logger.info("Enregistrement du menu contextuel ignoré : %s", exc)


def _executable() -> str:
    """Retourne la commande d'invocation de l'application."""
    return f"{sys.executable} -m app.main"


def _register_windows() -> None:
    """Enregistre via le registre Windows (nécessite des droits)."""
    try:
        import importlib
        from typing import Any

        winreg: Any = importlib.import_module("winreg")

        command = f'"{_executable()}" "%1"'
        key_path = r"*\shell\Cross-Imagizer"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValue(key, "", winreg.REG_SZ, "Convertir avec Cross-Imagizer")
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path + r"\command") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, command)
        logger.info("Menu contextuel Windows enregistré.")
    except Exception as exc:  # noqa: BLE001
        logger.info("Menu contextuel Windows non enregistré : %s", exc)


def _register_macos() -> None:
    """Enregistre via un service macOS (nécessite un bundle .app)."""
    # L'intégration macOS nécessite un bundle .app signé ; best-effort.
    logger.info("Menu contextuel macOS : enregistrement non effectué (best-effort).")


def _register_linux() -> None:
    """Enregistre via un fichier .desktop (freedesktop)."""
    desktop_dir = Path.home() / ".local" / "share" / "applications"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    desktop_file = desktop_dir / "cross-imagizer.desktop"
    content = (
        "[Desktop Entry]\n"
        "Type=Application\n"
        f"Name={_APP_NAME}\n"
        f"Exec={_executable()} %F\n"
        "Terminal=false\n"
        "MimeType=image/png;image/jpeg;image/webp;image/gif;image/bmp;image/tiff;\n"
    )
    desktop_file.write_text(content, encoding="utf-8")
    logger.info("Menu contextuel Linux enregistré : %s", desktop_file)
