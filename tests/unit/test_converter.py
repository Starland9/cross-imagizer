"""Tests unitaires du moteur de conversion."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import converter, formats
from app.core.errors import UnreadableImageError, UnsupportedFormatError
from models import CollisionPolicy, ConversionOptions


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    """Crée une image PNG de test."""
    path = tmp_path / "sample.png"
    Image.new("RGB", (100, 50), color=(255, 0, 0)).save(path)
    return path


def test_detect_format(sample_png: Path) -> None:
    assert formats.detect_format(sample_png) == "PNG"


def test_detect_format_unreadable(tmp_path: Path) -> None:
    bad = tmp_path / "bad.png"
    bad.write_bytes(b"not an image")
    with pytest.raises(UnreadableImageError):
        formats.detect_format(bad)


def test_supported_formats() -> None:
    assert "PNG" in formats.supported_formats()
    assert "JPEG" in formats.supported_formats()


def test_convert_png_to_jpeg(sample_png: Path, tmp_path: Path) -> None:
    options = ConversionOptions(target_format="JPEG", collision_policy=CollisionPolicy.OVERWRITE)
    out = converter.convert(sample_png, options)
    assert out.exists()
    assert out.suffix == ".jpeg" or out.suffix == ".jpg"


def test_convert_unsupported_format(sample_png: Path) -> None:
    options = ConversionOptions(target_format="XYZ")
    with pytest.raises(UnsupportedFormatError):
        converter.convert(sample_png, options)


def test_convert_missing_source(tmp_path: Path) -> None:
    options = ConversionOptions(target_format="PNG")
    with pytest.raises(UnreadableImageError):
        converter.convert(tmp_path / "missing.png", options)


def test_convert_rename_collision(sample_png: Path) -> None:
    options = ConversionOptions(target_format="PNG", collision_policy=CollisionPolicy.RENAME)
    out1 = converter.convert(sample_png, options)
    out2 = converter.convert(sample_png, options)
    assert out1 != out2
    assert out1.exists() and out2.exists()
