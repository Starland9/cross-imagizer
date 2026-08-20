"""Tests unitaires de la couche d'abstraction des notifications."""

from __future__ import annotations

from platform_utils import notifications


def test_notify_does_not_raise() -> None:
    # La notification doit dégrader silencieusement sans lever d'exception.
    notifications.notify("Titre", "Message")
