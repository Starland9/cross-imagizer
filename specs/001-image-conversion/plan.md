# Implementation Plan: Conversion d'images multi-formats

**Branch**: `001-image-conversion` | **Date**: 2026-08-20 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-image-conversion/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Application de bureau cross-platform (Windows, macOS, Linux) de conversion
d'images multi-formats, avec traitement par lot, exécution en arrière-plan avec
notifications natives, aperçu et options de conversion. L'interface est une
application PySide6 (Qt 6) avec un thème custom sobre et authentique (CSS/QSS),
mode clair et sombre, animations fluides, widgets et icônes personnalisés. Le
cœur de conversion s'appuie sur Pillow (PIL) pour un large éventail de formats,
avec une architecture en couches (UI / services / moteur de conversion) pour
garantir la testabilité et la portabilité.

## Technical Context

**Language/Version**: Python 3.11+ (latest stable compatible avec les trois OS)

**Primary Dependencies**: PySide6 (Qt 6, latest stable), Pillow (PIL) pour la
conversion d'images, pytest pour les tests

**Storage**: Système de fichiers local (aucune base de données) ; préférences
utilisateur persistées via QSettings

**Testing**: pytest (unitaires + intégration), pytest-qt pour les tests UI,
pytest-cov pour la couverture

**Target Platform**: Desktop Windows, macOS, Linux (matrice CI 3 OS)

**Project Type**: desktop-app (application de bureau)

**Performance Goals**: démarrage < 3 s, conversion d'une image < 5 s sur machine
modeste, UI réactive pendant les lots (60 fps cible pour les animations)

**Constraints**: empreinte mémoire maîtrisée, aucune dépendance lourde non
justifiée, opérations d'I/O et de conversion paresseuses/asynchrones, offline
(conversion 100 % locale)

**Scale/Scope**: application mono-utilisateur locale ; lots de l'ordre de la
centaine d'images ; ~15 formats d'images pris en charge

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

| Principe                            | Statut  | Justification                                                    |
| ----------------------------------- | ------- | ---------------------------------------------------------------- |
| I. Code ultra clean                 | ✅ PASS | Typage statique, ruff/black, docstrings, architecture en couches |
| II. Tests (NON-NÉGOCIABLE)          | ✅ PASS | TDD, couverture ≥ 80 %, CI verte obligatoire                     |
| III. Performance appareils modestes | ✅ PASS | Conversion asynchrone, I/O paresseuse, budget mémoire            |
| IV. Compatibilité cross-platform    | ✅ PASS | `pathlib`, isolation des différences OS, matrice CI 3 OS         |
| V. Simplicité & YAGNI               | ✅ PASS | Pillow + PySide6 uniquement, pas de sur-ingénierie               |

Aucune violation à justifier.

## Project Structure

### Documentation (this feature)

```text
specs/001-image-conversion/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
src/
├── app/
│   ├── main.py              # Point d'entrée de l'application
│   ├── ui/                  # Couche présentation (PySide6)
│   │   ├── main_window.py
│   │   ├── widgets/         # Widgets custom (drop zone, progress, preview)
│   │   ├── theme/           # QSS, thèmes clair/sombre, palette
│   │   └── resources/       # Icônes et assets
│   ├── services/            # Couche métier (orchestration, batch, notifications)
│   └── core/                # Moteur de conversion (Pillow), formats, options
├── models/                  # Entités du domaine (tâche, lot, options)
└── platform/                # Abstraction des différences OS (notifications, chemins)

tests/
├── unit/                    # Tests unitaires (moteur, modèles, services)
├── integration/             # Tests d'intégration (conversion réelle, batch)
└── contract/                # Tests de contrat (interfaces publiques)
```

**Structure Decision**: Structure « single project » en couches (UI / services /
core / models / platform). La couche `platform` isole les différences OS
(notifications natives, chemins) conformément au principe IV. Le moteur de
conversion (`core`) est indépendant de l'UI pour être testable unitairement.

## Complexity Tracking

> Aucune violation de la constitution à justifier.
