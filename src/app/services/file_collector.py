"""Collecte de fichiers images (fichiers multiples ou dossier)."""

from __future__ import annotations

from pathlib import Path

# Extensions de fichiers images à considérer lors du scan de dossiers.
_IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tif", ".tiff",
    ".ico", ".ppm", ".pgm", ".pbm",
}


def collect_files(paths: list[Path], recursive: bool = False) -> list[Path]:
    """Collecte les fichiers images à partir d'une liste de chemins.

    Les dossiers sont parcourus (récursivement si demandé) et seuls les
    fichiers avec une extension image connue sont retenus.

    Args:
        paths: Chemins de fichiers ou de dossiers.
        recursive: Parcourir les sous-dossiers récursivement.

    Returns:
        La liste triée des fichiers images collectés.
    """
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            pattern = "**/*" if recursive else "*"
            for child in path.glob(pattern):
                if child.is_file() and child.suffix.lower() in _IMAGE_EXTENSIONS:
                    files.append(child)
        elif path.is_file() and path.suffix.lower() in _IMAGE_EXTENSIONS:
            files.append(path)
    return sorted(set(files))
