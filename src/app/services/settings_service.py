"""Persistance du dossier de sortie via QSettings."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QSettings

_KEY = "output_directory"


def get_output_directory() -> Path | None:
    """Retourne le dossier de sortie persisté, ou ``None`` si non défini."""
    settings = QSettings()
    value = settings.value(_KEY)
    if value is None or str(value) == "":
        return None
    return Path(str(value))


def set_output_directory(path: Path | None) -> None:
    """Persiste le dossier de sortie.

    Args:
        path: Chemin du dossier, ou ``None`` pour réinitialiser.

    Raises:
        ValueError: Si le chemin n'est pas un dossier accessible en écriture.
    """
    settings = QSettings()
    if path is None:
        settings.remove(_KEY)
        return
    if not path.is_dir():
        raise ValueError(f"Le dossier de sortie n'existe pas : {path}")
    if not _is_writable(path):
        raise ValueError(f"Le dossier de sortie n'est pas accessible en écriture : {path}")
    settings.setValue(_KEY, str(path))


def _is_writable(path: Path) -> bool:
    """Vérifie qu'un dossier est accessible en écriture (best-effort)."""
    try:
        probe = path / ".write_probe"
        probe.touch()
        probe.unlink()
        return True
    except OSError:
        return False
