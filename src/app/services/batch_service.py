"""Service d'orchestration des lots de conversion."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from PySide6.QtCore import QObject, QThreadPool, Signal

from app.services import file_collector
from app.services.worker import BatchWorker
from models import Batch, ConversionOptions, ConversionTask, ImageSource


class BatchService(QObject):
    """Orchestre l'exécution des lots de conversion en arrière-plan."""

    progress = Signal(int, int)
    task_finished = Signal(object)
    finished = Signal(object)
    cancelled = Signal()

    def __init__(self) -> None:
        super().__init__()
        self._pool = QThreadPool.globalInstance()
        self._worker: BatchWorker | None = None

    def create_batch(
        self,
        paths: list[Path],
        options: ConversionOptions,
        recursive: bool = False,
    ) -> Batch:
        """Crée un lot à partir d'une liste de chemins (fichiers ou dossiers)."""
        files = file_collector.collect_files(paths, recursive=recursive)
        tasks = [
            ConversionTask(
                id=str(f),
                source=ImageSource(path=f),
                options=options,
            )
            for f in files
        ]
        return Batch(id="batch", tasks=tasks)

    def run(
        self,
        batch: Batch,
        options: ConversionOptions,
        confirm: Callable[[Path], bool] | None = None,
        output_dir: Path | None = None,
    ) -> None:
        """Lance l'exécution d'un lot en arrière-plan."""
        self._worker = BatchWorker(batch, options, confirm=confirm, output_dir=output_dir)
        self._worker.signals.progress.connect(self.progress)
        self._worker.signals.task_finished.connect(self.task_finished)
        self._worker.signals.finished.connect(self.finished)
        self._worker.signals.cancelled.connect(self.cancelled)
        self._pool.start(self._worker)

    def cancel(self) -> None:
        """Annule le lot en cours."""
        if self._worker is not None:
            self._worker.cancel()
