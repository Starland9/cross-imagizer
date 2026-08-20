# Implementation Plan: Refonte de la disposition principale

**Branch**: `005-ux-polish-v3` | **Date**: 2026-08-20 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/005-ux-polish-v3/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Refondre la disposition de la fenêtre principale Cross-Imagizer pour résoudre
les problèmes visuels structurels : zone de dépôt trop grande, quatre panneaux
alignés horizontalement, barre d'actions plate, et absence d'identité visuelle.
La solution repose sur une organisation verticale (header / corps / footer),
un panneau d'options à largeur fixe, un regroupement file + historique,
une barre d'actions hiérarchisée, des états vides explicites, et le maintien
du support clair/sombre. Aucune nouvelle fonctionnalité métier n'est ajoutée.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: PySide6 (latest stable), Pillow

**Storage**: N/A (état géré via `QSettings` pour le dossier de sortie et
l'historique ; pas de base de données).

**Testing**: pytest, pytest-qt, pytest-cov, ruff, mypy

**Target Platform**: Windows 10+, macOS 12+, Linux (glibc-based)

**Project Type**: desktop-app

**Performance Goals**: Démarrage de la fenêtre principale en moins de 500 ms
sur machine de référence ; redimensionnement fluide ≥ 30 fps ; pas de freeze
sur du matériel modeste.

**Constraints**:
- Pas de dépendance tierce supplémentaire (reste sur PySide6).
- Largeur minimale de fenêtre 800 px, hauteur minimale 500 px.
- Le code UI est exclu de l'exigence de couverture 80 %, mais les interactions
  critiques (conversion, annulation, historique) doivent rester testables.

**Scale/Scope**: Refonte UI/UX limitée à la fenêtre principale et aux widgets
afférants ; aucun changement sur le moteur de conversion ni sur les services.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Design Gate

| Principle | Assessment | Notes |
|-----------|------------|-------|
| I. Code ultra clean | PASS | La refonte doit découper la construction UI en méthodes courtes, réutiliser les tokens existants, et éviter la duplication de styles inline. |
| II. Tests | PASS | Les tests existants sur `main_window.py` seront mis à jour ; les chemins critiques (conversion, annulation, historique) restent couverts. Aucune logique métier nouvelle. |
| III. Performance | PASS | Pas de traitement lourd ajouté ; le redimensionnement reste géré par Qt. Objectif : pas de régression de démarrage. |
| IV. Cross-platform | PASS | PySide6 + `pathlib` déjà utilisés ; pas d'appel système spécifique. |
| V. Simplicité / YAGNI | PASS | Pas de feature spéculative : le redesign répond directement au feedback utilisateur. Pas de dépendance externe. |

**Pre-design gate result**: PASS.

### Post-Design Gate

| Principle | Assessment | Notes |
|-----------|------------|-------|
| I. Code ultra clean | PASS | Plan prévoit un découpage en méthodes `_build_header`, `_build_drop_zone`, `_build_workbench`, `_build_action_bar`, avec réutilisation des tokens. |
| II. Tests | PASS | `quickstart.md` inclut la mise à jour des tests et la non-régression des conversions/historique. |
| III. Performance | PASS | Pas de traitement lourd ; les états vides sont de simples widgets cachés/affichés. |
| IV. Cross-platform | PASS | Aucun appel OS spécifique introduit. |
| V. Simplicité / YAGNI | PASS | Les décisions restent sur PySide6 natif ; pas de bibliothèque tierce. |

**Post-design gate result**: PASS — aucune violation à justifier.

## Project Structure

### Documentation (this feature)

```text
specs/005-ux-polish-v3/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
├── checklists/
│   └── requirements.md  # Specification quality checklist
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
src/
├── app/
│   ├── core/            # Conversion engine (inchangé)
│   ├── services/        # Batch, settings, history (inchangé)
│   └── ui/
│       ├── animations.py
│       ├── main_window.py          # REFONTE PRINCIPALE
│       ├── resources/
│       │   └── icons.py            # Icônes d'état vide à ajouter
│       ├── theme/
│       │   ├── theme.py              # QSS + tokens (ajustements)
│       │   └── tokens.py             # Tokens existants à enrichir
│       ├── tray.py
│       └── widgets/
│           ├── batch_panel.py      # Ajustements de largeur / état vide
│           ├── drop_zone.py        # Zone de dépôt compacte
│           ├── history_panel.py    # Regroupement file+historique ou onglets
│           ├── options_panel.py    # Largeur fixe
│           └── preview_pane.py     # Aperçu (inchangé logiquement)
├── models/
├── platform_utils/
tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Conserver la structure monolithique existante. La
feature touche principalement à `src/app/ui/main_window.py` et aux widgets
sous `src/app/ui/widgets/`. Aucun nouveau module métier n'est nécessaire.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

Aucune violation constatée.
