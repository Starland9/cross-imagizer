# Research: Conversion d'images multi-formats

## Décisions techniques

### D1. Framework UI : PySide6 (Qt 6)

- **Decision**: PySide6 (dernière version stable) comme framework d'interface.
- **Rationale**: Qt 6 est le standard de facto pour les applications de bureau
  cross-platform en Python. PySide6 est la liaison officielle (licence LGPL),
  maintenue par The Qt Company, avec un support complet de QSS (feuilles de style
  type CSS), des animations (QPropertyAnimation), des widgets personnalisables
  et des icônes (QIcon + Qt Resource System). Il couvre nativement Windows,
  macOS et Linux.
- **Alternatives considérées**:
  - _Tkinter_ : trop limité pour un thème custom riche, animations et widgets
    avancés.
  - _Kivy_ : orienté tactile/mobile, moins adapté au desktop natif.
  - _Electron/Tauri_ : lourd en mémoire, contraire au principe III (performance
    sur appareils modestes).

### D2. Moteur de conversion : Pillow (PIL)

- **Decision**: Pillow comme bibliothèque de traitement d'images.
- **Rationale**: Pillow est la bibliothèque de référence en Python pour la
  lecture/écriture d'images, avec un large support de formats (JPEG, PNG, WebP,
  GIF, BMP, TIFF, ICO, etc.), la manipulation des métadonnées EXIF, et une API
  stable. Elle est légère et purement locale (offline).
- **Alternatives considérées**:
  - _ImageMagick (via subprocess)_ : dépendance système externe, non portable
    sans installation, contraire au principe IV.
  - _OpenCV_ : surdimensionné pour de la conversion simple, plus lourd.
  - _imageio_ : utile pour certains formats (AVIF, HEIC) mais nécessite des
    plugins ; peut être ajouté en complément si besoin.

### D3. Formats pris en charge

- **Decision**: Couverture des formats courants via Pillow : JPEG, PNG, WebP,
  GIF, BMP, TIFF, ICO, PPM, PGM, PBM. Les formats AVIF et HEIC nécessitent des
  codecs supplémentaires (pillow-avif-plugin, pillow-heif) et seront traités
  comme des extensions optionnelles.
- **Rationale**: Pillow couvre nativement la majorité des besoins ; les formats
  exotiques sont ajoutés de manière incrémentale (YAGNI).
- **Alternatives considérées**: intégrer tous les formats dès le départ (contraire
  au principe V).

### D4. Traitement en arrière-plan

- **Decision**: `QThreadPool` + `QRunnable` (ou `QThread` + signaux) pour exécuter
  les conversions hors du thread UI, avec communication par signaux Qt
  (progression, fin, erreur).
- **Rationale**: Qt fournit un modèle de threading mature et thread-safe pour
  garder l'UI réactive (FR-005). Les signaux/slots garantissent la mise à jour
  sûre de l'UI depuis les threads de travail.
- **Alternatives considérées**:
  - _asyncio_ : inadapté au CPU-bound (conversion d'images) et à l'intégration
    Qt.
  - _multiprocessing_ : plus lourd, sérialisation coûteuse des données.

### D5. Notifications natives

- **Decision**: Couche d'abstraction `platform` utilisant les mécanismes natifs :
  `plyer` (ou appels directs) pour les notifications desktop sur les trois OS.
- **Rationale**: Les notifications natives sont requises (FR-006) et diffèrent
  par OS ; une couche d'abstraction isole ces différences (principe IV).
- **Alternatives considérées**: notifications in-app uniquement (ne satisfait
  pas FR-006 pour les traitements en arrière-plan).

### D6. Thème et style

- **Decision**: QSS (Qt Style Sheets) pour un thème custom sobre et authentique,
  avec deux palettes (clair/sombre) chargées dynamiquement, animations via
  `QPropertyAnimation`/`QGraphicsOpacityEffect`, widgets custom (zone de dépôt,
  barre de progression, aperçu) et icônes via Qt Resource System.
- **Rationale**: QSS permet un style type CSS sans dépendance supplémentaire,
  conforme au principe V. Les animations restent légères (principe III).
- **Alternatives considérées**: bibliothèques de thème tierces (qt-material,
  QDarkStyle) — rejetées pour garder le contrôle total et éviter les dépendances.

### D7. Tests

- **Decision**: `pytest` + `pytest-qt` (tests UI) + `pytest-cov` (couverture).
- **Rationale**: pytest est le standard Python ; pytest-qt permet de tester les
  widgets Qt ; pytest-cov mesure la couverture exigée (≥ 80 %).
- **Alternatives considérées**: unittest (moins expressif), tox (complémentaire,
  pas remplaçant).

## Points d'attention

- **Images animées** (GIF, WebP animé) : Pillow préserve l'animation pour GIF ;
  pour WebP animé, vérifier le support de la version cible. Sinon, conserver la
  première frame avec avertissement (conforme aux hypothèses de la spec).
- **Métadonnées EXIF** : préserver l'orientation et les métadonnées pertinentes
  via `Image.Exif` lorsque le format cible le permet (FR-011).
- **Collisions de noms** : stratégie configurable (écrasement / renommage
  incrémental / confirmation) (FR-010).
