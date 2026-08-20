"""Gestion des collisions de noms de fichiers de sortie."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from models import CollisionPolicy


def resolve_output_path(
    source: Path,
    target_format: str,
    output_dir: Path | None,
    policy: CollisionPolicy,
    confirm: Callable[[Path], bool] | None = None,
) -> Path:
    """Résout le chemin de sortie en appliquant la politique de collision.

    Args:
        source: Chemin du fichier source.
        target_format: Format cible (extension).
        output_dir: Dossier de sortie (défaut : à côté de la source).
        policy: Politique de collision (overwrite, rename, ask).
        confirm: Callback de confirmation pour la politique ``ASK``. Reçoit le
            chemin candidat et retourne ``True`` pour écraser, ``False`` pour
            renommer. Si absent, l'ASK se comporte comme un renommage sûr.

    Returns:
        Le chemin de sortie résolu.
    """
    ext = target_format.lower()
    directory = output_dir if output_dir is not None else source.parent
    candidate = directory / f"{source.stem}.{ext}"

    if policy is CollisionPolicy.OVERWRITE:
        return candidate
    if policy is CollisionPolicy.ASK:
        if candidate.exists() and confirm is not None and confirm(candidate):
            return candidate
        return _unique_path(candidate)
    return _unique_path(candidate)


def _unique_path(candidate: Path) -> Path:
    """Génère un chemin unique en ajoutant un suffixe incrémental."""
    if not candidate.exists():
        return candidate
    stem = candidate.stem
    suffix = candidate.suffix
    parent = candidate.parent
    counter = 1
    while True:
        new_candidate = parent / f"{stem}_{counter}{suffix}"
        if not new_candidate.exists():
            return new_candidate
        counter += 1
