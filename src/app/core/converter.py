"""Moteur de conversion d'images (Pillow)."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from PIL import Image

from app.core import animation, collision, formats, metadata, resize
from app.core.errors import (
    ConversionError,
    OutputWriteError,
    UnreadableImageError,
    UnsupportedFormatError,
)
from models import ConversionOptions, ImageSource


def convert(
    source: Path,
    options: ConversionOptions,
    confirm: Callable[[Path], bool] | None = None,
    output_dir: Path | None = None,
) -> Path:
    """Convertit une image source vers le format cible.

    Args:
        source: Chemin du fichier source.
        options: Options de conversion.
        confirm: Callback de confirmation pour la politique de collision ``ASK``.
        output_dir: Dossier de sortie (défaut : à côté de la source).

    Returns:
        Le chemin du fichier de sortie produit.

    Raises:
        ConversionError: Si la source est illisible, le format non pris en
            charge, ou l'écriture impossible.
    """
    target_format = options.target_format.upper()
    if target_format not in formats.SUPPORTED_FORMATS:
        raise UnsupportedFormatError(f"Format cible non pris en charge : {target_format}")

    if not source.exists():
        raise UnreadableImageError(f"Fichier source introuvable : {source}")

    output_path = collision.resolve_output_path(
        source, target_format, output_dir, options.collision_policy, confirm
    )

    # Gestion des images animées.
    if formats.is_animated(source) and animation.convert_animated(
        source, output_path, target_format, options.quality
    ):
        return output_path
    # Sinon, dégradation : on traite la première frame ci-dessous.

    try:
        with Image.open(source) as opened:
            img: Image.Image = metadata.apply_orientation(opened)
            img = resize.resize(img, options.resize_width, options.resize_height)

            exif = metadata.extract_exif(img) if options.preserve_metadata else None

            save_kwargs: dict[str, object] = {}
            if options.quality is not None and target_format in {"JPEG", "WEBP"}:
                save_kwargs["quality"] = options.quality

            # Conversion du mode pour les formats sans canal alpha.
            if target_format in formats._NO_ALPHA_FORMATS and img.mode in ("RGBA", "LA", "P"):
                img = img.convert("RGB")

            if exif is not None and metadata.supports_exif(target_format):
                save_kwargs["exif"] = exif

            img.save(output_path, format=target_format, **save_kwargs)
    except (OSError, ValueError) as exc:
        raise ConversionError(f"Échec de conversion de {source} : {exc}") from exc

    if not output_path.exists():
        raise OutputWriteError(f"Le fichier de sortie n'a pas pu être écrit : {output_path}")

    return output_path


def load_source(path: Path) -> ImageSource:
    """Charge les métadonnées d'une image source (dimensions, format, animation)."""
    fmt = formats.detect_format(path)
    width: int | None = None
    height: int | None = None
    animated = formats.is_animated(path)
    try:
        with Image.open(path) as img:
            width, height = img.size
    except (OSError, ValueError):
        pass
    return ImageSource(
        path=path,
        format=fmt,
        width=width,
        height=height,
        is_animated=animated,
    )
