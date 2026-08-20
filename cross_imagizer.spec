# -*- mode: python ; coding: utf-8 -*-
"""Spécification PyInstaller pour Cross-Imagizer.

Génère un exécutable standalone (onefile) avec les données Qt nécessaires.
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = []
binaries = []
hiddenimports = []

# Données et sous-modules de PySide6 (plugins de plateforme, styles, etc.).
datas += collect_data_files("PySide6")
hiddenimports += collect_submodules("PySide6")

a = Analysis(
    ["src/app/__main__.py"],
    pathex=["src"],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="cross-imagizer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
