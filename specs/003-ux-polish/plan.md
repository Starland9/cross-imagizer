# Implementation Plan: Amélioration de l'UX

**Branch**: `003-ux-polish` | **Date**: 2026-08-20 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-ux-polish/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Amélioration de l'interface de l'application Cross-Imagizer existante (features
001 et 002) : mise en page équilibrée (suppression des larges colonnes vides),
bouton « Ouvrir le dossier de sortie » après conversion, et retours visuels
clairs (progression, succès, erreur). S'appuie sur la stack PySide6 existante,
sans nouvelle fonctionnalité métier.

## Technical Context

**Language/Version**: Python 3.11+ (identique aux features précédentes)

**Primary Dependencies**: PySide6 (Qt 6) — layouts, `QDesktopServices` pour
l'ouverture du dossier, QSS pour le style

**Storage**: N/A (aucune nouvelle donnée ; réutilise `QSettings` de la feature 002)

**Testing**: pytest + pytest-qt (réutilisés)

**Target Platform**: Desktop Windows, macOS, Linux

**Project Type**: desktop-app (amélioration UI de l'application existante)

**Performance Goals**: interface réactive (60 fps cible), aucun gel pendant les
conversions

**Constraints**: offline, sobre et authentique, cohérent avec le thème
clair/sombre existant

**Scale/Scope**: refonte de la mise en page de la fenêtre principale + 1 bouton
+ retours visuels

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principe | Statut | Justification |
|----------|--------|---------------|
| I. Code ultra clean | ✅ PASS | Typage, ruff/mypy, docstrings |
| II. Tests (NON-NÉGOCIABLE) | ✅ PASS | TDD, couverture ≥ 80 % |
| III. Performance appareils modestes | ✅ PASS | Pas de dépendance lourde, layouts légers |
| IV. Compatibilité cross-platform | ✅ PASS | `QDesktopServices.openUrl` portable |
| V. Simplicité & YAGNI | ✅ PASS | Refonte ciblée, pas de sur-ingénierie |

Aucune violation à justifier.

## Project Structure

### Documentation (this feature)

```text
specs/003-ux-polish/
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
│   ├── ui/
│   │   ├── main_window.py   # Refonte de la mise en page + bouton ouvrir dossier
│   │   ├── theme/theme.py   # Ajustements QSS (espacements, proportions)
│   │   └── widgets/         # Ajustements des widgets (proportions)
│   └── services/
│       └── settings_service.py  # Réutilisé (dossier de sortie)
└── platform_utils/
    └── open_folder.py       # Ouverture du dossier (QDesktopServices)

tests/
├── unit/                    # open_folder, layout
└── integration/             # ouverture du dossier après conversion
```

**Structure Decision**: Extension de la structure existante. Nouveau module
`platform_utils/open_folder.py` pour l'ouverture du dossier (isolation OS,
principe IV). Refonte de `main_window.py` pour la mise en page équilibrée.

## Complexity Tracking

> Aucune violation de la constitution à justifier.
