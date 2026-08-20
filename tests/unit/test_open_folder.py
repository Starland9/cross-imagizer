"""Tests unitaires de l'ouverture de dossier."""

from __future__ import annotations

from pathlib import Path

import pytest

from platform_utils import open_folder

pytest.importorskip("PySide6")


def test_open_folder_missing_dir(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    assert open_folder.open_folder(missing) is False


def test_open_folder_existing_dir(tmp_path: Path) -> None:
    # L'ouverture réelle dépend de l'environnement ; on vérifie seulement
    # qu'elle ne lève pas d'exception et retourne un booléen.
    result = open_folder.open_folder(tmp_path)
    assert isinstance(result, bool)
