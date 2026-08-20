"""Service de conversion unitaire."""

from __future__ import annotations

from pathlib import Path

from app.core import converter
from app.core.logging import get_logger
from models import ConversionOptions, ConversionTask, ImageSource, TaskStatus

logger = get_logger()


def convert_single(source: Path, options: ConversionOptions) -> ConversionTask:
    """Convertit une image unique et retourne la tâche résultante.

    Args:
        source: Chemin du fichier source.
        options: Options de conversion.

    Returns:
        La tâche de conversion avec son statut final.
    """
    task = ConversionTask(
        id=str(source),
        source=ImageSource(path=source),
        options=options,
    )
    try:
        task.output_path = converter.convert(source, options)
        task.status = TaskStatus.SUCCEEDED
        logger.info("Conversion réussie : %s -> %s", source, task.output_path)
    except Exception as exc:  # noqa: BLE001 - on capture toute erreur de conversion
        task.status = TaskStatus.FAILED
        task.error = str(exc)
        logger.warning("Conversion échouée : %s (%s)", source, exc)
    return task
