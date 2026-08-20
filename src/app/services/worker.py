"""Worker d'arrière-plan pour l'exécution des lots de conversion."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from PySide6.QtCore import QObject, QRunnable, Signal, Slot

from app.core.logging import get_logger
from app.services import conversion_service, report
from models import Batch, BatchStatus, ConversionOptions, TaskStatus

logger = get_logger()


class WorkerSignals(QObject):
    """Signaux émis par le worker de conversion."""

    progress = Signal(int, int)
    task_finished = Signal(object)
    finished = Signal(object)
    cancelled = Signal()


class BatchWorker(QRunnable):
    """Exécute un lot de conversion en arrière-plan."""

    def __init__(
        self,
        batch: Batch,
        options: ConversionOptions,
        confirm: Callable[[Path], bool] | None = None,
        output_dir: Path | None = None,
    ) -> None:
        super().__init__()
        self.batch = batch
        self.options = options
        self.confirm = confirm
        self.output_dir = output_dir
        self.signals = WorkerSignals()
        self._cancelled = False

    def cancel(self) -> None:
        """Demande l'annulation du lot en cours."""
        self._cancelled = True

    @Slot()
    def run(self) -> None:
        """Exécute le lot (appelé par le QThreadPool)."""
        self.batch.status = BatchStatus.RUNNING
        total = self.batch.total
        for done, task in enumerate(self.batch.tasks, start=1):
            if self._cancelled:
                task.status = TaskStatus.CANCELLED
                self.signals.cancelled.emit()
                break
            task.status = TaskStatus.RUNNING
            result = conversion_service.convert_single(
                task.source.path, self.options, self.confirm, self.output_dir
            )
            task.status = result.status
            task.output_path = result.output_path
            task.error = result.error
            self.signals.progress.emit(done, total)
            self.signals.task_finished.emit(task)

        if not self._cancelled:
            self.batch.status = BatchStatus.COMPLETED
        self.batch.report = report.build_report(self.batch)
        self.signals.finished.emit(self.batch.report)
