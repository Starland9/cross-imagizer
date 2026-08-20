# Implementation Plan: Dossier de sortie, barre de tâche & historique

**Branch**: `002-output-tray-history` | **Date**: 2026-08-20 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-output-tray-history/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Extension de l'application Cross-Imagizer existante (feature 001) avec trois
capacités : (1) sélection d'un dossier de sortie persistant pour les
conversions, (2) icône de barre de tâche (system tray) avec menu contextuel
(ouvrir, convertir, quitter), (3) historique des conversions persisté entre les
sessions. S'appuie sur la stack existante PySide6 + Pillow, en réutilisant le
moteur de conversion et les services de la feature 001.

## Technical Context

**Language/Version**: Python 3.11+ (identique à la feature 001)

**Primary Dependencies**: PySide6 (Qt 6) — `QSystemTrayIcon`, `QSettings` ;
Pillow (réutilisé)

**Storage**: `QSettings` (préférences natives) pour le dossier de sortie et
l'historique (JSON sérialisé) ; aucun service distant

**Testing**: pytest + pytest-qt (réutilisés)

**Target Platform**: Desktop Windows, macOS, Linux (matrice CI 3 OS)

**Project Type**: desktop-app (extension de l'application existante)

**Performance Goals**: sélection + conversion < 10 s ; historique consultable
sans latence perceptible (≤ 500 entrées)

**Constraints**: offline, empreinte mémoire maîtrisée, dégradation silencieuse
si le system tray n'est pas supporté

**Scale/Scope**: mono-utilisateur local ; historique limité à 500 entrées

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principe | Statut | Justification |
|----------|--------|---------------|
| I. Code ultra clean | ✅ PASS | Typage, ruff/mypy, docstrings, réutilisation des couches existantes |
| II. Tests (NON-NÉGOCIABLE) | ✅ PASS | TDD, couverture ≥ 80 % sur le code métier |
| III. Performance appareils modestes | ✅ PASS | Historique borné (500), QSettings léger |
| IV. Compatibilité cross-platform | ✅ PASS | QSystemTrayIcon + QSettings sont portables ; dégradation silencieuse |
| V. Simplicité & YAGNI | ✅ PASS | QSettings plutôt qu'une base de données ; pas de sur-ingénierie |

Aucune violation à justifier.

## Project Structure

### Documentation (this feature)

```text
specs/002-output-tray-history/
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
│   ├── main.py              # Point d'entrée (câblage tray + historique)
│   ├── ui/
│   │   ├── main_window.py   # Fenêtre principale (sélection dossier de sortie)
│   │   ├── tray.py          # Icône de barre de tâche + menu contextuel
│   │   └── widgets/
│   │       └── history_panel.py  # Panneau d'historique
│   ├── services/
│   │   ├── history_service.py    # Enregistrement/lecture de l'historique
│   │   └── settings_service.py   # Persistance du dossier de sortie
│   └── core/
│       └── converter.py     # Réutilisé (paramètre output_dir déjà présent)
├── models/
│   └── history.py           # Entrée d'historique
└── platform_utils/          # Réutilisé

tests/
├── unit/                    # history_service, settings_service
├── integration/             # conversion vers dossier de sortie, persistance
└── contract/                # contrats des services
```

**Structure Decision**: Extension de la structure en couches existante (feature
001). Nouveaux modules : `tray.py` (UI), `history_service.py` et
`settings_service.py` (services), `history.py` (modèle). Le moteur de conversion
expose déjà un paramètre `output_dir` (actuellement `None`) qu'il suffit de
câbler.

## Complexity Tracking

> Aucune violation de la constitution à justifier.
