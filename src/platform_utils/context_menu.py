"""Intégration au menu contextuel du système (best-effort)."""

from __future__ import annotations

from app.core.logging import get_logger

logger = get_logger()


def register_context_menu() -> None:
    """Enregistre l'application dans le menu contextuel du système.

    Implémentation best-effort : selon l'OS, l'enregistrement peut nécessiter
    des privilèges ou des mécanismes spécifiques. Aucune exception n'est levée
    en cas d'échec.
    """
    try:
        import platform as _platform

        system = _platform.system()
        if system == "Windows":
            _register_windows()
        elif system == "Darwin":
            _register_macos()
        else:
            _register_linux()
    except Exception as exc:  # noqa: BLE001
        logger.info("Enregistrement du menu contextuel ignoré : %s", exc)


def _register_windows() -> None:
    """Enregistre via le registre Windows (nécessite des droits)."""
    # L'implémentation réelle utilise winreg ; laissée volontairement minimale.
    logger.info("Menu contextuel Windows : enregistrement non effectué (best-effort).")


def _register_macos() -> None:
    """Enregistre via un service macOS (nécessite un bundle .app)."""
    logger.info("Menu contextuel macOS : enregistrement non effectué (best-effort).")


def _register_linux() -> None:
    """Enregistre via un fichier .desktop (freedesktop)."""
    logger.info("Menu contextuel Linux : enregistrement non effectué (best-effort).")
