"""Couche d'abstraction des différences entre systèmes d'exploitation."""

from app.core.logging import get_logger

logger = get_logger()

__all__ = ["notify", "register_context_menu"]
