# Tasks: Refonte de la disposition principale

**Input**: Design documents from `specs/005-ux-polish-v3/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Tests are included per constitution (TDD required).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare the feature workspace and confirm baseline tooling.

- [ ] T001 Verify current branch is `005-ux-polish-v3` and working tree is clean
- [ ] T002 Run baseline validation: `ruff check src tests`, `mypy src`, `pytest tests/unit tests/integration tests/contract -q`

---

## Phase 1b: Performance Baseline (Startup Time)

**Purpose**: Capture the current startup-time baseline so the ≤ +10 % NFR-001 budget can be verified.

- [ ] T002b [P] Add benchmark script `scripts/benchmark_startup.py` that measures `MainWindow` creation time over 5 runs and prints the median
- [ ] T002c [P] Run `scripts/benchmark_startup.py` before implementation and record the median baseline in `specs/005-ux-polish-v3/baseline-startup.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Enrich design tokens and icon helpers used by all user stories.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T003 Add layout-specific tokens to `src/app/ui/theme/tokens.py` (header height, drop-zone compact height, options fixed width, action-bar height, group spacing)
- [ ] T004 Add empty-state icon helpers to `src/app/ui/resources/icons.py` (inbox, image, history)
- [ ] T005 Add reusable `EmptyStateWidget` in `src/app/ui/widgets/empty_state.py` with icon, title, subtitle, and theme-aware muted color

**Checkpoint**: Foundation ready — tokens, icons, and empty-state widget exist and are unit-tested.

---

## Phase 3: User Story 1 — Layout global aéré et structuré (Priority: P1) 🎯 MVP

**Goal**: Refactor `MainWindow` into a clear vertical structure (header / drop zone / workbench / action bar) and eliminate the large empty drop-zone area.

**Independent Test**: Open the application without images. The window shows a compact header, a compact drop zone, a three-zone workbench, and a footer action bar. Less than 25 % of the central area is unused empty space.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Add unit test in `tests/unit/test_main_window_layout.py` asserting `_build_header`, `_build_drop_zone`, `_build_workbench`, `_build_action_bar` methods exist
- [ ] T007 [P] [US1] Add integration test in `tests/integration/test_main_window_layout.py` asserting drop-zone height is ≤ 140 px when no image is loaded
- [ ] T008 [P] [US1] Add contract test in `tests/contract/test_ui_layout_contract.py` asserting vertical section order per `contracts/ui-layout.md`

### Implementation for User Story 1

- [ ] T009 [US1] Create `src/app/ui/widgets/app_header.py` with icon + title + optional subtitle
- [ ] T010 [US1] Refactor `src/app/ui/main_window.py` `_build_ui` to call `_build_header`, `_build_drop_zone`, `_build_workbench`, `_build_action_bar`
- [ ] T011 [US1] Compact `src/app/ui/widgets/drop_zone.py` to a fixed-height band with an explicit empty-state message and click-to-browse behavior
- [ ] T012 [US1] Connect drop-zone click to existing `_pick_files` in `src/app/ui/main_window.py`

**Checkpoint**: User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 — Panneaux logiquement regroupés (Priority: P1)

**Goal**: Give `OptionsPanel` a fixed width, keep `PreviewPane` in the center, and group `BatchPanel` + `HistoryPanel` in a right-side `QTabWidget` with readable file paths.

**Independent Test**: Add images and observe that options stay ~260 px wide, the preview stretches, and the queue/history tabs show full paths on a 1280 px window.

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T013 [P] [US2] Add unit test in `tests/unit/test_options_panel_width.py` asserting `OptionsPanel.maximumWidth()` ≤ 320 and default width is 240–280 px
- [ ] T014 [P] [US2] Add unit test in `tests/unit/test_side_tabs.py` asserting `SideTabs` has exactly two tabs labeled "File d'attente" and "Historique"
- [ ] T015 [P] [US2] Add integration test in `tests/integration/test_batch_history_paths.py` asserting paths are not truncated in the batch tab at 1280 px window width

### Implementation for User Story 2

- [ ] T016 [US2] Create `src/app/ui/widgets/side_tabs.py` wrapping `QTabWidget` with "File d'attente" and "Historique" tabs
- [ ] T017 [US2] Set fixed width policy and size constraints in `src/app/ui/widgets/options_panel.py` so the panel stays 240–320 px
- [ ] T018 [US2] Refactor `src/app/ui/main_window.py` `_build_workbench` to place options (left), preview (center), side-tabs (right) with a `QSplitter`
- [ ] T019 [US2] Move `BatchPanel` and `HistoryPanel` into `SideTabs` and remove them from the horizontal four-column splitter

**Checkpoint**: User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 — Barre d'actions hiérarchisée (Priority: P1)

**Goal**: Make the Convert button visually dominant and group secondary actions logically (file / control / view).

**Independent Test**: A 5-second visual test identifies the Convert button as the primary action for ≥ 4 out of 5 users.

### Tests for User Story 3 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T020 [P] [US3] Add unit test in `tests/unit/test_action_bar.py` asserting the Convert button object name is "primary"
- [ ] T021 [P] [US3] Add unit test in `tests/unit/test_action_bar.py` asserting the file group contains Add, Output dir, and Open folder buttons
- [ ] T022 [P] [US3] Add contract test in `tests/contract/test_ui_layout_contract.py` asserting Convert button uses primary color style

### Implementation for User Story 3

- [ ] T023 [US3] Create `src/app/ui/widgets/action_bar.py` with grouped layouts: file group, primary Convert button, control group (Cancel), view group (Theme)
- [ ] T024 [US3] Apply object name "primary" to Convert button and update `src/app/ui/theme/theme.py` to style it with primary background and bold text
- [ ] T025 [US3] Replace the flat bottom button row in `src/app/ui/main_window.py` with the new `ActionBar`

**Checkpoint**: User Stories 1, 2, and 3 should work independently.

---

## Phase 6: User Story 4 — Identité visuelle et états vides explicites (Priority: P2)

**Goal**: Add an application header with name/icon and explicit empty states for drop zone, batch list, and history list.

**Independent Test**: Open the app with no images and see a header title, plus invitation messages in the drop zone, batch tab, and history tab.

### Tests for User Story 4 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T026 [P] [US4] Add unit test in `tests/unit/test_app_header.py` asserting header title is "Cross-Imagizer"
- [ ] T027 [P] [US4] Add unit test in `tests/unit/test_empty_states.py` asserting empty-state labels exist for drop zone, batch, and history
- [ ] T028 [P] [US4] Add integration test in `tests/integration/test_empty_states.py` asserting empty-state text is visible when models are empty

### Implementation for User Story 4

- [ ] T029 [US4] Integrate `AppHeader` into `src/app/ui/main_window.py` and set the window icon
- [ ] T030 [US4] Use `EmptyStateWidget` in `src/app/ui/widgets/drop_zone.py` when no file is loaded
- [ ] T031 [US4] Use `EmptyStateWidget` in `src/app/ui/widgets/batch_panel.py` when the file list is empty
- [ ] T032 [US4] Use `EmptyStateWidget` in `src/app/ui/widgets/history_panel.py` when history is empty

**Checkpoint**: User Stories 1–4 should all be independently functional.

---

## Phase 7: User Story 5 — Compatibilité thème clair/sombre maintenue (Priority: P2)

**Goal**: Ensure header, drop zone, empty states, action bar, and side tabs update correctly when switching between light and dark themes.

**Independent Test**: Toggle theme and verify all new UI elements remain readable with correct contrast.

### Tests for User Story 5 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T033 [P] [US5] Add unit test in `tests/unit/test_theme_update.py` asserting `apply_theme` sets the expected palette/style on `AppHeader`, `ActionBar`, and `EmptyStateWidget`
- [ ] T034 [P] [US5] Add integration test in `tests/integration/test_theme_toggle.py` asserting empty-state text color changes after toggling dark mode

### Implementation for User Story 5

- [ ] T035 [US5] Update `src/app/ui/theme/theme.py` to style `AppHeader`, `ActionBar`, `EmptyStateWidget`, and `SideTabs` for both light and dark themes
- [ ] T036 [US5] Ensure `src/app/ui/main_window.py` `_toggle_theme` calls `style().unpolish`/`polish` on new top-level widgets if needed

**Checkpoint**: All user stories should now be independently functional in both themes.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, regression checks, and cleanup.

- [ ] T037 [P] Run full validation from `quickstart.md`: lint, type check, unit/integration/contract tests
- [ ] T038 [P] Update coverage configuration in `pyproject.toml` if new UI files need omission
- [ ] T039 [P] Run visual smoke test: open app, add image, convert, toggle theme, open output folder
- [ ] T039b [P] Re-run `scripts/benchmark_startup.py` after implementation and verify the median does not exceed the baseline by more than 10 %
- [ ] T039c [P] Measure central empty-space ratio via screenshot inspection or script and verify it is below 25 % when no image is loaded
- [ ] T040 [P] Update `README.md` screenshots section if applicable (placeholder note)
- [ ] T041 Final code cleanup: remove dead layout code, ensure all new functions have type hints and docstrings in `src/app/ui/main_window.py` and new widgets

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup. Blocks all user stories.
- **User Stories (Phase 3–7)**: All depend on Foundational phase completion.
  - Execute in priority order (P1 → P2).
- **Polish (Phase 8)**: Depends on all desired user stories.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational. No dependencies on other stories.
- **User Story 2 (P1)**: Can start after Foundational. Integrates layout from US1 but is independently testable once layout widgets exist.
- **User Story 3 (P1)**: Can start after Foundational. Replaces the old bottom row; independent from US1/US2 widget logic.
- **User Story 4 (P2)**: Can start after Foundational and US1 (needs `AppHeader`).
- **User Story 5 (P2)**: Can start after all UI widgets are created; cross-cutting theme styling.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.
- Widgets before integration into `main_window.py`.
- Story complete before moving to the next priority.

### Parallel Opportunities

- T003/T004/T005 can run in parallel.
- T006/T007/T008 can run in parallel.
- T013/T014/T015 can run in parallel.
- T020/T021/T022 can run in parallel.
- T026/T027/T028 can run in parallel.
- T033/T034 can run in parallel.
- T037/T038/T039/T040/T041 can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
pytest tests/unit/test_main_window_layout.py
pytest tests/integration/test_main_window_layout.py
pytest tests/contract/test_ui_layout_contract.py

# Launch widgets in parallel once tests exist:
# - src/app/ui/widgets/app_header.py
# - src/app/ui/widgets/drop_zone.py
# Then integrate into src/app/ui/main_window.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational.
3. Complete Phase 3: User Story 1.
4. **STOP and VALIDATE**: open the app and confirm the new vertical layout.
5. Deploy/demo if ready.

### Incremental Delivery

1. Setup + Foundational → Foundation ready.
2. Add User Story 1 → Test independently → Demo.
3. Add User Story 2 → Test independently → Demo.
4. Add User Story 3 → Test independently → Demo.
5. Add User Story 4 → Test independently → Demo.
6. Add User Story 5 → Test themes independently → Demo.
7. Final polish and regression checks.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1 + 4 (header identity).
   - Developer B: User Story 2 (side tabs + options width).
   - Developer C: User Story 3 (action bar).
3. All merge into `main_window.py` in a coordinated final integration task.
4. Developer D: User Story 5 (theme compatibility) + Polish phase.

---

## Notes

- [P] tasks = different files, no dependencies.
- [Story] label maps task to specific user story for traceability.
- Each user story should be independently completable and testable.
- Verify tests fail before implementing.
- Commit after each task or logical group.
- Stop at any checkpoint to validate a story independently.
- Avoid vague tasks, same-file conflicts, and cross-story dependencies that break independence.
