# Cross-Imagizer

Application de bureau cross-platform (Windows, macOS, Linux) de conversion
d'images multi-formats, avec traitement par lot, exécution en arrière-plan avec
notifications natives, aperçu et options de conversion.

## Fonctionnalités

- Conversion d'images entre de nombreux formats (JPEG, PNG, WebP, GIF, BMP,
  TIFF, ICO, PPM, PGM, PBM).
- Conversion par lot (fichiers multiples ou dossier entier) avec progression.
- Traitement en arrière-plan avec notifications natives.
- Aperçu et options (qualité, dimensions).
- Glisser-déposer et intégration au menu contextuel système.
- Thème clair/sombre, animations fluides, widgets personnalisés.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Lancement

```bash
cross-imagizer
# ou
python -m app.main
```

## Tests

```bash
pytest
pytest --cov=src --cov-report=term-missing
```

## Build d'un exécutable standalone

```bash
pip install -e ".[build]"
pyinstaller --clean --noconfirm cross_imagizer.spec
```

L'exécutable est généré dans `dist/`.

## Release automatisée (GitHub Actions)

Le workflow `.github/workflows/release.yml` construit des exécutables
standalone pour **Windows**, **macOS** et **Linux** à chaque tag `v*`
(ou manuellement via l'onglet *Actions*), puis publie une *GitHub Release*
avec les artefacts.

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Licence

MIT
