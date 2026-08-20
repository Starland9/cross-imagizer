"""Entités du domaine pour la conversion d'images."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any


class TaskStatus(StrEnum):
    """État d'une tâche de conversion."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class BatchStatus(StrEnum):
    """État d'un lot de conversion."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CollisionPolicy(StrEnum):
    """Politique de gestion des collisions de noms de fichiers."""

    OVERWRITE = "overwrite"
    RENAME = "rename"
    ASK = "ask"


@dataclass
class ImageSource:
    """Représente un fichier image d'entrée."""

    path: Path
    format: str | None = None
    width: int | None = None
    height: int | None = None
    is_animated: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ConversionOptions:
    """Réglages appliqués à une tâche de conversion."""

    target_format: str
    quality: int | None = None
    resize_width: int | None = None
    resize_height: int | None = None
    collision_policy: CollisionPolicy = CollisionPolicy.RENAME
    preserve_metadata: bool = True


@dataclass
class ConversionTask:
    """Une opération unitaire de conversion."""

    id: str
    source: ImageSource
    options: ConversionOptions
    output_path: Path | None = None
    status: TaskStatus = TaskStatus.PENDING
    error: str | None = None


@dataclass
class BatchReport:
    """Résultat d'un lot de conversion."""

    succeeded: int = 0
    failed: int = 0
    cancelled: int = 0
    failures: list[dict[str, str]] = field(default_factory=list)


@dataclass
class Batch:
    """Un ensemble de tâches traitées ensemble."""

    id: str
    tasks: list[ConversionTask] = field(default_factory=list)
    status: BatchStatus = BatchStatus.PENDING
    report: BatchReport = field(default_factory=BatchReport)

    @property
    def total(self) -> int:
        """Nombre total de tâches."""
        return len(self.tasks)

    @property
    def done(self) -> int:
        """Nombre de tâches terminées (succès, échec ou annulation)."""
        return sum(
            1
            for t in self.tasks
            if t.status in (TaskStatus.SUCCEEDED, TaskStatus.FAILED, TaskStatus.CANCELLED)
        )
