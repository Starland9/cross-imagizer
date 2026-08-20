"""Génération du rapport récapitulatif d'un lot."""

from __future__ import annotations

from models import Batch, BatchReport, TaskStatus


def build_report(batch: Batch) -> BatchReport:
    """Construit le rapport récapitulatif d'un lot à partir de ses tâches."""
    report = BatchReport()
    for task in batch.tasks:
        if task.status is TaskStatus.SUCCEEDED:
            report.succeeded += 1
        elif task.status is TaskStatus.FAILED:
            report.failed += 1
            report.failures.append(
                {"file": str(task.source.path), "reason": task.error or "Erreur inconnue"}
            )
        elif task.status is TaskStatus.CANCELLED:
            report.cancelled += 1
    return report
