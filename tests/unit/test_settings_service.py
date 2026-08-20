"""Tests unitaires du service de réglages (dossier de sortie)."""

from __future__ import annotations

from pathlib import Path

import pytest

from app.services import settings_service


def test_get_output_directory_none_by_default() -> None:
    settings_service.set_output_directory(None)
    assert settings_service.get_output_directory() is None


def test_set_and_get_output_directory(tmp_path: Path) -> None:
    settings_service.set_output_directory(tmp_path)
    assert settings_service.get_output_directory() == tmp_path


def test_set_invalid_directory_raises(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(ValueError):
        settings_service.set_output_directory(missing)


def test_set_none_clears() -> None:
    settings_service.set_output_directory(None)
    assert settings_service.get_output_directory() is None
