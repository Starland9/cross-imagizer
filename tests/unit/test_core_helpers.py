"""Tests unitaires des modules core complémentaires."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from app.core import animation, collision, metadata, resize
from models import CollisionPolicy


@pytest.fixture
def sample_png(tmp_path: Path) -> Path:
    path = tmp_path / "s.png"
    Image.new("RGB", (100, 50), color=(1, 2, 3)).save(path)
    return path


def test_collision_overwrite(sample_png: Path) -> None:
    out = collision.resolve_output_path(sample_png, "PNG", None, CollisionPolicy.OVERWRITE)
    assert out == sample_png.parent / "s.png"


def test_collision_rename_unique(sample_png: Path) -> None:
    out1 = collision.resolve_output_path(sample_png, "PNG", None, CollisionPolicy.RENAME)
    out1.write_bytes(b"x")
    out2 = collision.resolve_output_path(sample_png, "PNG", None, CollisionPolicy.RENAME)
    assert out1 != out2


def test_resize_no_dims(sample_png: Path) -> None:
    with Image.open(sample_png) as img:
        result = resize.resize(img, None, None)
        assert result.size == (100, 50)


def test_resize_height_only(sample_png: Path) -> None:
    with Image.open(sample_png) as img:
        result = resize.resize(img, None, 25)
        assert result.size == (50, 25)


def test_metadata_supports_exif() -> None:
    assert metadata.supports_exif("JPEG")
    assert metadata.supports_exif("WEBP")
    assert not metadata.supports_exif("PNG")


def test_metadata_apply_orientation(sample_png: Path) -> None:
    with Image.open(sample_png) as img:
        result = metadata.apply_orientation(img)
        assert result.size == (100, 50)


def test_animation_non_animated(sample_png: Path) -> None:
    out = sample_png.parent / "out.gif"
    result = animation.convert_animated(sample_png, out, "GIF", None)
    assert result is False


def test_animation_unsupported_target(sample_png: Path) -> None:
    out = sample_png.parent / "out.png"
    result = animation.convert_animated(sample_png, out, "PNG", None)
    assert result is False
