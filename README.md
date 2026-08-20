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

## Licence

MIT
