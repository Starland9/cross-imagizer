"""Service de conversion unitaire."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from app.core import converter
from app.core.logging import get_logger
from models import ConversionOptions, ConversionTask, ImageSource, TaskStatus

logger = get_logger()


def convert_single(
    source: Path,
    options: ConversionOptions,
    confirm: Callable[[Path], bool] | None = None,
) -> ConversionTask:
    """Convertit une image unique et retourne la tâche résultante.

    Args:
        source: Chemin du fichier source.
        options: Options de conversion.
        confirm: Callback de confirmation pour la politique de collision ``ASK``.

    Returns:
        La tâche de conversion avec son statut final.
    """
    task = ConversionTask(
        id=str(source),
        source=ImageSource(path=source),
        options=options,
    )
    try:
        task.source = converter.load_source(source)
        task.output_path = converter.convert(source, options, confirm)
        task.status = TaskStatus.SUCCEEDED
        logger.info("Conversion réussie : %s -> %s", source, task.output_path)
    except Exception as exc:  # noqa: BLE001 - on capture toute erreur de conversion
        task.status = TaskStatus.FAILED
        task.error = str(exc)
        logger.warning("Conversion échouée : %s (%s)", source, exc)
    return task
