"""Couche d'abstraction des différences entre systèmes d'exploitation."""

from __future__ import annotations

from app.core.logging import get_logger

logger = get_logger()


def notify(title: str, message: str) -> None:
    """Affiche une notification native.

    Dégradation silencieuse si les notifications ne sont pas disponibles.
    """
    try:
        from plyer import notification  # type: ignore[import-not-found]

        notification.notify(title=title, message=message, app_name="Cross-Imagizer")
    except Exception:  # noqa: BLE001 - dégradation silencieuse
        logger.info("Notification non disponible : %s — %s", title, message)
