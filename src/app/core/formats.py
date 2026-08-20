"""Détection et liste des formats d'images pris en charge."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from app.core.errors import UnreadableImageError, UnsupportedFormatError

# Formats de sortie pris en charge en v1 (aligné sur FR-001).
SUPPORTED_FORMATS: tuple[str, ...] = (
    "JPEG",
    "PNG",
    "WEBP",
    "GIF",
    "BMP",
    "TIFF",
    "ICO",
    "PPM",
    "PGM",
    "PBM",
)

# Formats nécessitant un mode d'image compatible (pas de canal alpha).
_NO_ALPHA_FORMATS = {"JPEG", "PPM", "PGM", "PBM"}


def supported_formats() -> list[str]:
    """Retourne la liste des formats de sortie pris en charge."""
    return list(SUPPORTED_FORMATS)


def detect_format(path: Path) -> str:
    """Détecte le format d'une image à partir de son contenu.

    Args:
        path: Chemin du fichier image.

    Returns:
        L'identifiant de format (ex. ``"JPEG"``, ``"PNG"``).

    Raises:
        UnreadableImageError: Si le fichier est illisible ou corrompu.
        UnsupportedFormatError: Si le format est inconnu.
    """
    try:
        with Image.open(path) as img:
            fmt = img.format
    except (OSError, ValueError) as exc:
        raise UnreadableImageError(f"Image illisible ou corrompue : {path}") from exc

    if fmt is None:
        raise UnsupportedFormatError(f"Format inconnu pour : {path}")
    return fmt.upper()


def is_animated(path: Path) -> bool:
    """Détecte si une image est animée (GIF, WebP animé)."""
    try:
        with Image.open(path) as img:
            return bool(getattr(img, "is_animated", False))
    except (OSError, ValueError):
        return False
