"""Redimensionnement d'images en conservant les proportions."""

from __future__ import annotations

from PIL import Image


def resize(
    img: Image.Image,
    width: int | None,
    height: int | None,
) -> Image.Image:
    """Redimensionne une image en conservant les proportions.

    Si une seule dimension est fournie, l'autre est calculée pour conserver le
    ratio. Si les deux sont fournies, l'image est ajustée dans la boîte définie
    (contenu, sans déformation).

    Args:
        img: Image source.
        width: Largeur cible (optionnelle).
        height: Hauteur cible (optionnelle).

    Returns:
        L'image redimensionnée (ou l'originale si aucune dimension fournie).
    """
    if width is None and height is None:
        return img

    orig_w, orig_h = img.size
    if width is not None and height is not None:
        # Ajustement dans la boîte (contenu), sans déformation.
        ratio = min(width / orig_w, height / orig_h)
        new_size = (int(orig_w * ratio), int(orig_h * ratio))
    elif width is not None:
        ratio = width / orig_w
        new_size = (width, int(orig_h * ratio))
    else:
        assert height is not None
        ratio = height / orig_h
        new_size = (int(orig_w * ratio), height)

    return img.resize(new_size, Image.Resampling.LANCZOS)
