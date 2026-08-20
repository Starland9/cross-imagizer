"""Préservation des métadonnées (EXIF, orientation)."""

from __future__ import annotations

from PIL import Image, ImageOps


def extract_exif(img: Image.Image) -> Image.Exif | None:
    """Extrait les métadonnées EXIF d'une image si disponibles."""
    exif = img.getexif()
    return exif if exif else None


def apply_orientation(img: Image.Image) -> Image.Image:
    """Applique l'orientation EXIF à l'image (transposition si nécessaire)."""
    try:
        return ImageOps.exif_transpose(img)
    except Exception:  # noqa: BLE001 - dégradation silencieuse
        return img


def supports_exif(target_format: str) -> bool:
    """Indique si un format cible supporte l'EXIF."""
    return target_format.upper() in {"JPEG", "TIFF", "WEBP"}
