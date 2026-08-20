"""Entité d'historique des conversions."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class HistoryEntry:
    """Enregistrement d'une conversion passée."""

    source: str
    output: str | None
    status: str
    timestamp: str
    error: str | None = None

    @classmethod
    def create(
        cls,
        source: str,
        output: str | None,
        status: str,
        error: str | None = None,
    ) -> HistoryEntry:
        """Crée une entrée avec l'horodatage courant (ISO 8601 UTC)."""
        return cls(
            source=source,
            output=output,
            status=status,
            timestamp=datetime.now(UTC).isoformat(),
            error=error,
        )

    def to_dict(self) -> dict[str, str | None]:
        """Sérialise l'entrée en dictionnaire."""
        return {
            "source": self.source,
            "output": self.output,
            "status": self.status,
            "timestamp": self.timestamp,
            "error": self.error,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | None]) -> HistoryEntry:
        """Désérialise une entrée depuis un dictionnaire."""
        return cls(
            source=str(data["source"]),
            output=data.get("output"),
            status=str(data["status"]),
            timestamp=str(data["timestamp"]),
            error=data.get("error"),
        )
