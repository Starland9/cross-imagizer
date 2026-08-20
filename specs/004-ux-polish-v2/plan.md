# Implementation Plan: Polish UX avancé

**Branch**: `004-ux-polish-v2` | **Date**: 2026-08-20 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-ux-polish-v2/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Refonte visuelle avancée de l'application Cross-Imagizer existante (features
001 à 003) : tailles et proportions des widgets (largeurs min/max), espacements
et marges uniformes, hiérarchie typographique, états visuels cohérents
(normal, survol, pressé, désactivé), et réalignement des widgets (alignement
cohérent sur un même axe au sein de chaque groupe). S'appuie sur le thème QSS
existant, en centralisant les valeurs de design (espacements, tailles, polices)
pour faciliter la maintenance.

## Technical Context

**Language/Version**: Python 3.11+ (identique aux features précédentes)

**Primary Dependencies**: PySide6 (Qt 6) — QSS, `setMinimumWidth`,
`setMaximumWidth`, `QSizePolicy`, `QFormLayout`/`QGridLayout` (alignement),
pseudo-états QSS (`:hover`, `:pressed`, `:disabled`)

**Storage**: N/A (aucune donnée ; refonte purement visuelle)

**Testing**: pytest + pytest-qt (réutilisés)

**Target Platform**: Desktop Windows, macOS, Linux

**Project Type**: desktop-app (refonte UI de l'application existante)

**Performance Goals**: interface réactive (60 fps cible), aucun gel

**Constraints**: offline, sobre et authentique, cohérent avec le thème
clair/sombre existant

**Scale/Scope**: refonte du thème QSS + tailles et alignement des widgets existants

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principe | Statut | Justification |
|----------|--------|---------------|
| I. Code ultra clean | ✅ PASS | Centralisation des valeurs de design, typage, ruff/mypy |
| II. Tests (NON-NÉGOCIABLE) | ✅ PASS | TDD, couverture ≥ 80 % |
| III. Performance appareils modestes | ✅ PASS | QSS léger, pas de dépendance lourde |
| IV. Compatibilité cross-platform | ✅ PASS | QSS et QSizePolicy portables |
| V. Simplicité & YAGNI | ✅ PASS | Refonte ciblée du thème existant, pas de sur-ingénierie |

Aucune violation à justifier.

## Project Structure

### Documentation (this feature)

```text
specs/004-ux-polish-v2/
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
│   │   ├── theme/
│   │   │   ├── theme.py      # Refonte QSS (espacements, états, typographie)
│   │   │   └── tokens.py     # Valeurs de design centralisées (nouveau)
│   │   ├── main_window.py    # Tailles min/max + réalignement des widgets
│   │   └── widgets/          # Tailles, QSizePolicy et alignement des widgets
│   └── ...
└── ...

tests/
├── unit/                    # tokens, tailles, alignement
└── integration/             # cohérence thème clair/sombre
```

**Structure Decision**: Extension de la structure existante. Nouveau module
`tokens.py` pour centraliser les valeurs de design (espacements, tailles,
polices). Refonte de `theme.py` (QSS) et ajustement des tailles et de
l'alignement dans `main_window.py` et les widgets (via `QFormLayout`/
`QGridLayout` et propriétés d'alignement).

## Complexity Tracking

> Aucune violation de la constitution à justifier.
