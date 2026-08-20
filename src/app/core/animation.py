"""Gestion des images animées (GIF, WebP animé)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from app.core.errors import ConversionError

# Formats cibles supportant l'animation.
_ANIMATED_FORMATS = {"GIF", "WEBP"}


def convert_animated(
    source: Path,
    output_path: Path,
    target_format: str,
    quality: int | None,
) -> bool:
    """Convertit une image animée en préservant l'animation si possible.

    Returns:
        ``True`` si l'animation a été préservée, ``False`` sinon (dégradation
        vers la première frame, gérée par l'appelant).
    """
    if target_format.upper() not in _ANIMATED_FORMATS:
        return False

    try:
        with Image.open(source) as img:
            if not getattr(img, "is_animated", False):
                return False
            frames: list[Image.Image] = []
            durations: list[int] = []
            for frame in range(getattr(img, "n_frames", 1)):
                img.seek(frame)
                frames.append(img.convert("RGBA"))
                durations.append(int(img.info.get("duration", 100)))
            save_kwargs: dict[str, object] = {
                "save_all": True,
                "append_images": frames[1:],
                "duration": durations,
                "loop": 0,
            }
            if quality is not None and target_format.upper() == "WEBP":
                save_kwargs["quality"] = quality
            frames[0].save(output_path, format=target_format.upper(), **save_kwargs)
            return True
    except (OSError, ValueError) as exc:
        raise ConversionError(f"Échec de conversion de l'image animée : {source}") from exc
