# Tasks: Amélioration de l'UX

**Input**: Design documents from `/specs/003-ux-polish/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Inclus (TDD obligatoire — principe II de la constitution, NON-NÉGOCIABLE).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (structure en couches existante)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `open_folder.py` skeleton in `src/platform_utils/open_folder.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 [P] Unit tests for `open_folder` in `tests/unit/test_open_folder.py` (TDD: write FIRST, ensure FAIL)
- [X] T003 Implement `open_folder` (QDesktopServices) in `src/platform_utils/open_folder.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Interface visuellement soignée et compacte (Priority: P1) 🎯 MVP

**Goal**: Présenter une mise en page équilibrée, sans colonnes vides disproportionnées, adaptative au redimensionnement.

**Independent Test**: Ouvrir l'application et vérifier que les panneaux sont proportionnés et redimensionnables.

### Tests for User Story 1 ⚠️

- [X] T004 [P] [US1] Widget test for balanced layout in `tests/unit/test_layout.py`

### Implementation for User Story 1

- [X] T005 [US1] Refactor main window layout with QSplitter and stretch factors in `src/app/ui/main_window.py`
- [X] T006 [US1] Adjust QSS spacing and proportions in `src/app/ui/theme/theme.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ouvrir le dossier de sortie (Priority: P1)

**Goal**: Fournir un bouton « Ouvrir le dossier de sortie » après conversion.

**Independent Test**: Convertir une image puis cliquer sur « Ouvrir le dossier » et vérifier l'ouverture.

### Tests for User Story 2 ⚠️

- [X] T007 [P] [US2] Integration test for open folder after conversion in `tests/integration/test_open_folder.py`

### Implementation for User Story 2

- [X] T008 [US2] Add « Ouvrir le dossier de sortie » button in `src/app/ui/main_window.py`
- [X] T009 [US2] Wire button to `open_folder` with current output directory in `src/app/ui/main_window.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Retours visuels et ergonomie (Priority: P2)

**Goal**: Afficher des retours visuels clairs (progression, succès, erreur).

**Independent Test**: Effectuer une conversion et vérifier les retours visuels.

### Tests for User Story 3 ⚠️

- [X] T010 [P] [US3] Widget test for visual feedback states in `tests/unit/test_feedback.py`

### Implementation for User Story 3

- [X] T011 [US3] Ensure convert button disabled during conversion in `src/app/ui/main_window.py`
- [X] T012 [US3] Ensure success/error feedback after conversion in `src/app/ui/main_window.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T013 [P] Add remaining unit tests to reach ≥ 80 % coverage in `tests/unit/`
- [X] T014 Run quickstart.md validation scenarios end-to-end
- [X] T015 Code cleanup and refactoring (ruff, mypy clean)
- [X] T016 [P] Add UI non-blocking test during conversion in `tests/unit/test_feedback.py` per SC-004

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Reuses open_folder from Foundational
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Independent

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
Task: "Widget test for balanced layout in tests/unit/test_layout.py"

# Launch independent UI changes together:
Task: "Refactor main window layout with QSplitter in src/app/ui/main_window.py"
Task: "Adjust QSS spacing in src/app/ui/theme/theme.py"
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
