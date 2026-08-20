# Tasks: Conversion d'images multi-formats

**Input**: Design documents from `/specs/001-image-conversion/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Inclus (TDD obligatoire — principe II de la constitution, NON-NÉGOCIABLE).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (structure en couches définie dans plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan (src/app, src/models, src/platform, tests/)
- [X] T002 Initialize Python project with `pyproject.toml` (dependencies: PySide6, Pillow; dev: pytest, pytest-qt, pytest-cov, ruff, mypy)
- [X] T003 [P] Configure linting and formatting (ruff) in `pyproject.toml`
- [X] T004 [P] Configure static typing (mypy) in `pyproject.toml`
- [X] T005 [P] Configure pytest and coverage (pytest-cov, ≥ 80 %) in `pyproject.toml`
- [X] T006 [P] Configure CI matrix (Windows/macOS/Linux) in `.github/workflows/ci.yml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Create base entities (ImageSource, ConversionOptions, ConversionTask, Batch, BatchReport) in `src/models/`
- [X] T008 [P] Unit tests for core engine in `tests/unit/test_converter.py` (TDD: write FIRST, ensure FAIL)
- [X] T009 [P] Unit tests for models in `tests/unit/test_models.py` (TDD: write FIRST, ensure FAIL)
- [X] T010 [P] Implement format detection (`detect_format`, `supported_formats`) in `src/app/core/formats.py`
- [X] T011 [P] Implement conversion engine (`convert`) in `src/app/core/converter.py`
- [X] T012 [P] Implement error types (`ConversionError`) in `src/app/core/errors.py`
- [X] T013 [P] Implement platform abstraction (notifications, paths) in `src/platform/`
- [X] T014 Configure structured logging in `src/app/core/logging.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Conversion d'une image unique (Priority: P1) 🎯 MVP

**Goal**: Convertir une image d'un format source vers un format cible, avec gestion des erreurs et des collisions.

**Independent Test**: Convertir une seule image et vérifier que le fichier de sortie est valide et lisible.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T015 [P] [US1] Integration test for single image conversion in `tests/integration/test_single_conversion.py`
- [X] T016 [P] [US1] Contract test for `convert()` in `tests/contract/test_converter_contract.py`

### Implementation for User Story 1

- [X] T017 [US1] Implement collision policy (overwrite/rename/ask) in `src/app/core/collision.py`
- [X] T018 [US1] Implement metadata preservation (EXIF, orientation) in `src/app/core/metadata.py`
- [X] T019 [US1] Implement single conversion service in `src/app/services/conversion_service.py`
- [X] T020 [US1] Implement main window with single conversion flow in `src/app/ui/main_window.py`
- [X] T021 [US1] Implement file selection and format picker in `src/app/ui/widgets/`
- [X] T022 [US1] Add validation and error handling for single conversion
- [X] T023 [US1] Add logging for single conversion operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Conversion par lot (batch) (Priority: P1)

**Goal**: Convertir plusieurs images (fichiers multiples ou dossier) en une opération, avec progression et rapport.

**Independent Test**: Sélectionner un dossier de N images et vérifier que toutes sont converties avec un rapport succès/échec.

### Tests for User Story 2 ⚠️

- [X] T024 [P] [US2] Integration test for batch conversion in `tests/integration/test_batch_conversion.py`
- [X] T025 [P] [US2] Contract test for `BatchService.run()` in `tests/contract/test_batch_service_contract.py`

### Implementation for User Story 2

- [X] T026 [US2] Implement batch orchestration service in `src/app/services/batch_service.py`
- [X] T027 [US2] Implement batch report generation in `src/app/services/report.py`
- [X] T028 [US2] Implement batch UI (file list, progress) in `src/app/ui/widgets/batch_panel.py`
- [X] T029 [US2] Implement folder scanning and recursive file collection in `src/app/services/file_collector.py`
- [X] T030 [US2] Integrate batch flow into main window in `src/app/ui/main_window.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Traitement en arrière-plan avec notifications (Priority: P2)

**Goal**: Exécuter les conversions longues en arrière-plan sans bloquer l'UI, avec notifications natives et annulation.

**Independent Test**: Lancer un lot volumineux, naviguer dans l'app pendant le traitement, vérifier la notification de fin.

### Tests for User Story 3 ⚠️

- [X] T031 [P] [US3] Integration test for background processing in `tests/integration/test_background.py`
- [X] T032 [P] [US3] Unit test for notification abstraction in `tests/unit/test_notifications.py`

### Implementation for User Story 3

- [X] T033 [US3] Implement background worker (QThreadPool + signals) in `src/app/services/worker.py`
- [X] T034 [US3] Implement cancellation support in `src/app/services/worker.py`
- [X] T035 [US3] Implement native notifications in `src/platform/notifications.py`
- [X] T036 [US3] Wire background processing + notifications into batch service
- [X] T037 [US3] Add progress signal handling in UI in `src/app/ui/main_window.py`

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Aperçu et options de conversion (Priority: P2)

**Goal**: Visualiser un aperçu de l'image et ajuster qualité/dimensions avant conversion.

**Independent Test**: Ajuster la qualité ou les dimensions et vérifier que le résultat reflète ces réglages.

### Tests for User Story 4 ⚠️

- [X] T038 [P] [US4] Integration test for resize/quality options in `tests/integration/test_options.py`

### Implementation for User Story 4

- [X] T039 [US4] Implement resize logic in `src/app/core/resize.py`
- [X] T040 [US4] Implement quality handling in `src/app/core/converter.py`
- [X] T041 [US4] Implement preview pane widget in `src/app/ui/widgets/preview_pane.py`
- [X] T042 [US4] Implement options panel (quality, dimensions) in `src/app/ui/widgets/options_panel.py`
- [X] T043 [US4] Wire options into conversion service

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Glisser-déposer et intégration système (Priority: P3)

**Goal**: Déposer des fichiers dans l'app et lancer des conversions depuis le menu contextuel système.

**Independent Test**: Glisser des fichiers dans la fenêtre et vérifier qu'ils sont ajoutés à la file.

### Tests for User Story 5 ⚠️

- [X] T044 [P] [US5] Widget test for drop zone in `tests/unit/test_drop_zone.py`

### Implementation for User Story 5

- [X] T045 [US5] Implement drop zone widget in `src/app/ui/widgets/drop_zone.py`
- [X] T046 [US5] Implement system context menu integration in `src/platform/context_menu.py`
- [X] T047 [US5] Wire drop zone and context menu into main window

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T048 [P] Implement theme system (light/dark QSS) in `src/app/ui/theme/`
- [X] T049 [P] Implement custom widgets styling and icons in `src/app/ui/resources/`
- [X] T050 [P] Implement animations (QPropertyAnimation) in `src/app/ui/animations.py`
- [X] T051 [P] Add remaining unit tests to reach ≥ 80 % coverage in `tests/unit/`
- [X] T052 Performance optimization (lazy I/O, memory budget) across all stories
- [X] T053 Run quickstart.md validation scenarios end-to-end
- [X] T054 Code cleanup and refactoring (ruff, mypy clean)
- [X] T055 [P] Implement animated image handling (GIF/WebP: preserve or degrade with warning) in `src/app/core/animation.py`
- [X] T056 [P] Add automated performance benchmarks (conversion <5s, batch 100 responsive, startup <3s) in `tests/benchmark/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Reuses US1 conversion service
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Extends US2 batch service
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Extends US1 converter
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Independent UI entry points

### Within Each User Story

- Tests MUST be written and FAIL before implementation (TDD)
- Models before services
- Services before UI
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Integration test for single image conversion in tests/integration/test_single_conversion.py"
Task: "Contract test for convert() in tests/contract/test_converter_contract.py"

# Launch independent core modules together:
Task: "Implement collision policy in src/app/core/collision.py"
Task: "Implement metadata preservation in src/app/core/metadata.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (TDD — constitution principe II)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
