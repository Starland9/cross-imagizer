# Tasks: Polish UX avancé

**Input**: Design documents from `/specs/004-ux-polish-v2/`

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

- [ ] T001 Create design tokens module (spacings, sizes, fonts, colors) in `src/app/ui/theme/tokens.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T002 Unit tests for design tokens in `tests/unit/test_tokens.py` (TDD: write FIRST, ensure FAIL)
- [ ] T003 Implement design tokens (SPACING_*, PANEL_MIN/MAX_WIDTH, FONT_*, COLOR_*) in `src/app/ui/theme/tokens.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Tailles et proportions des widgets (Priority: P1) 🎯 MVP

**Goal**: Définir des tailles minimales et maximales pour chaque panneau afin d'éviter les disproportions.

**Independent Test**: Ouvrir l'application et vérifier qu'aucun panneau ne dépasse 40 % de la largeur de la fenêtre.

### Tests for User Story 1 ⚠️

- [ ] T004 [P] [US1] Widget test for panel size bounds in `tests/unit/test_panel_sizes.py`

### Implementation for User Story 1

- [ ] T005 [US1] Apply setMinimumWidth/setMaximumWidth and QSizePolicy to panels in `src/app/ui/main_window.py`
- [ ] T006 [US1] Apply size policies to widgets in `src/app/ui/widgets/`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Espacements et marges cohérents (Priority: P1)

**Goal**: Appliquer des espacements (marges) uniformes et cohérents entre tous les widgets.

**Independent Test**: Vérifier que les marges entre widgets sont uniformes (écart ≤ 2 px).

### Tests for User Story 2 ⚠️

- [ ] T007 [P] [US2] Widget test for uniform spacing in `tests/unit/test_spacing.py`

### Implementation for User Story 2

- [ ] T008 [US2] Apply uniform margins/padding via QSS tokens in `src/app/ui/theme/theme.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 5 - Réalignement des widgets (Priority: P1)

**Goal**: Aligner les widgets d'un même groupe sur un même axe de manière cohérente.

**Independent Test**: Ouvrir l'application et vérifier que les labels, champs et boutons d'un même groupe sont alignés.

### Tests for User Story 5 ⚠️

- [ ] T009 [P] [US5] Widget test for widget alignment in `tests/unit/test_alignment.py`

### Implementation for User Story 5

- [ ] T010 [US5] Refactor forms to QFormLayout for label/field alignment in `src/app/ui/widgets/options_panel.py`
- [ ] T011 [US5] Align button rows and groups in `src/app/ui/main_window.py`

**Checkpoint**: At this point, User Stories 1, 2 AND 5 should all work independently

---

## Phase 6: User Story 3 - Typographie et hiérarchie visuelle (Priority: P2)

**Goal**: Hiérarchiser la typographie (titres, labels, contenus) de manière visuellement distincte.

**Independent Test**: Vérifier que les titres sont visuellement plus marqués que les labels.

### Tests for User Story 3 ⚠️

- [ ] T012 [P] [US3] Widget test for typography hierarchy in `tests/unit/test_typography.py`

### Implementation for User Story 3

- [ ] T013 [US3] Apply font-size/font-weight hierarchy via QSS tokens in `src/app/ui/theme/theme.py`
- [ ] T014 [US3] Add titles to panels in `src/app/ui/widgets/`

**Checkpoint**: At this point, User Stories 1, 2, 5 AND 3 should all work independently

---

## Phase 7: User Story 4 - États visuels des widgets (Priority: P2)

**Goal**: Afficher des états visuels cohérents pour les éléments interactifs (normal, survol, pressé, désactivé).

**Independent Test**: Survoler, presser et désactiver des boutons et vérifier les changements visuels.

### Tests for User Story 4 ⚠️

- [ ] T015 [P] [US4] Widget test for interactive states in `tests/unit/test_widget_states.py`

### Implementation for User Story 4

- [ ] T016 [US4] Add :hover/:pressed/:disabled pseudo-states to QSS in `src/app/ui/theme/theme.py`
- [ ] T017 [US4] Ensure states are consistent in both light and dark themes in `src/app/ui/theme/theme.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T018 [P] Add remaining unit tests to reach ≥ 80 % coverage in `tests/unit/`
- [ ] T019 Run quickstart.md validation scenarios end-to-end
- [ ] T020 Code cleanup and refactoring (ruff, mypy clean)
- [ ] T021 [P] Add UI non-blocking test during interactions in `tests/unit/test_widget_states.py` per SC-004

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Reuses tokens from Foundational
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - Independent
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Reuses tokens
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Reuses tokens

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
Task: "Widget test for panel size bounds in tests/unit/test_panel_sizes.py"

# Launch independent UI changes together:
Task: "Apply setMinimumWidth/setMaximumWidth to panels in src/app/ui/main_window.py"
Task: "Apply size policies to widgets in src/app/ui/widgets/"
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
4. Add User Story 5 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 5
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