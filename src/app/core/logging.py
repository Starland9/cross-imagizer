"""Journalisation structurée de l'application."""

from __future__ import annotations

import logging
import sys

_LOGGER_NAME = "cross_imagizer"


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure et retourne le logger racine de l'application."""
    logger = logging.getLogger(_LOGGER_NAME)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger


def get_logger() -> logging.Logger:
    """Retourne le logger de l'application (le configure si nécessaire)."""
    logger = logging.getLogger(_LOGGER_NAME)
    if not logger.handlers:
        return setup_logging()
    return logger
