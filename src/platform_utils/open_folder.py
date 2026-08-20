"""Ouverture d'un dossier dans le gestionnaire de fichiers natif."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


def open_folder(path: Path) -> bool:
    """Ouvre le dossier ``path`` dans le gestionnaire de fichiers natif.

    Args:
        path: Chemin d'un dossier existant.

    Returns:
        ``True`` si l'ouverture a réussi, ``False`` sinon (dégradation
        silencieuse, sans exception).
    """
    if not path.is_dir():
        return False
    return QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))
