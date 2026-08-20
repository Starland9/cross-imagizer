# Tasks: Dossier de sortie, barre de tâche & historique

**Input**: Design documents from `/specs/002-output-tray-history/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Inclus (TDD obligatoire — principe II de la constitution, NON-NÉGOCIABLE).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (structure en couches existante de la feature 001)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `HistoryEntry` model in `src/models/history.py`
- [X] T002 [P] Create `settings_service.py` skeleton in `src/app/services/settings_service.py`
- [X] T003 [P] Create `history_service.py` skeleton in `src/app/services/history_service.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Unit tests for `HistoryEntry` model in `tests/unit/test_history_model.py` (TDD: write FIRST, ensure FAIL)
- [X] T005 [P] Unit tests for `settings_service` in `tests/unit/test_settings_service.py` (TDD: write FIRST, ensure FAIL)
- [X] T006 [P] Unit tests for `history_service` in `tests/unit/test_history_service.py` (TDD: write FIRST, ensure FAIL)
- [X] T007 Implement `HistoryEntry` model in `src/models/history.py`
- [X] T008 [P] Implement `settings_service` (get/set output directory via QSettings) in `src/app/services/settings_service.py`
- [X] T009 [P] Implement `history_service` (record/list/clear, 500-entry cap) in `src/app/services/history_service.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Sélection du dossier de sortie (Priority: P1) 🎯 MVP

**Goal**: Permettre à l'utilisateur de choisir un dossier de sortie persistant pour les conversions.

**Independent Test**: Choisir un dossier de sortie, convertir une image, vérifier que le fichier est créé dans ce dossier.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Integration test for output directory conversion in `tests/integration/test_output_directory.py`

### Implementation for User Story 1

- [X] T011 [US1] Wire `output_dir` from settings into `conversion_service.convert_single` in `src/app/services/conversion_service.py`
- [X] T012 [US1] Wire `output_dir` from settings into `BatchService.run` in `src/app/services/batch_service.py`
- [X] T013 [US1] Add output directory picker UI in `src/app/ui/main_window.py`
- [X] T014 [US1] Add error handling for unwritable output directory

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Icône de barre de tâche (system tray) (Priority: P2)

**Goal**: Fournir une icône de barre de tâche avec menu contextuel (ouvrir, convertir, quitter), accessible après fermeture de la fenêtre.

**Independent Test**: Fermer la fenêtre principale et vérifier que l'icône de barre de tâche reste active avec son menu.

### Tests for User Story 2 ⚠️

- [X] T015 [P] [US2] Widget test for tray icon in `tests/unit/test_tray.py`

### Implementation for User Story 2

- [X] T016 [US2] Implement `TrayIcon` (QSystemTrayIcon + QMenu) in `src/app/ui/tray.py`
- [X] T017 [US2] Intercept window close to hide instead of quit in `src/app/ui/main_window.py`
- [X] T018 [US2] Wire tray actions (open/convert/quit) in `src/app/ui/tray.py`
- [X] T019 [US2] Handle graceful quit (stop workers) in `src/app/ui/tray.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Historique des conversions (Priority: P2)

**Goal**: Enregistrer et consulter l'historique des conversions (source, sortie, statut, date), persisté entre sessions.

**Independent Test**: Effectuer des conversions puis vérifier qu'elles apparaissent dans l'historique.

### Tests for User Story 3 ⚠️

- [X] T020 [P] [US3] Integration test for history persistence in `tests/integration/test_history.py`

### Implementation for User Story 3

- [X] T021 [US3] Record conversions in history from `conversion_service` in `src/app/services/conversion_service.py`
- [X] T022 [US3] Implement history panel UI in `src/app/ui/widgets/history_panel.py`
- [X] T023 [US3] Wire history panel into main window in `src/app/ui/main_window.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T024 [P] Add remaining unit tests to reach ≥ 80 % coverage in `tests/unit/`
- [X] T025 Run quickstart.md validation scenarios end-to-end
- [X] T026 Code cleanup and refactoring (ruff, mypy clean)
- [X] T027 [P] Add cross-platform validation note for FR-010 (QSystemTrayIcon/QSettings portability) in `tests/unit/test_tray.py`
- [X] T028 [P] Add lightweight benchmark for output-directory selection + conversion (<10s) in `tests/benchmark/test_output_directory.py` per SC-001

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Reuses US1 conversion service

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
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Integration test for output directory conversion in tests/integration/test_output_directory.py"

# Launch independent services together:
Task: "Wire output_dir from settings into conversion_service.convert_single"
Task: "Wire output_dir from settings into BatchService.run"
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
