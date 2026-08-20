# Startup baseline for 005-ux-polish-v3

- Date: 2026-08-20
- Method: `scripts/benchmark_startup.py`, 5 runs, median
- Pre-implementation MainWindow creation median: `0.0050508 s`
- Post-implementation MainWindow creation median: `0.076116 s`
- NFR-001 budget: ≤ +10 % after implementation (≈ 0.005556 s)

> ⚠️ Le budget de +10 % est dépassé. La mesure post-implémentation inclut l'instanciation complète de tous les nouveaux widgets structuraux (`AppHeader`, `ActionBar`, `SideTabs`, `OptionsPanel`, `DropZone`, `BatchPanel`, `HistoryPanel`, `PreviewPane`). À réévaluer si une initialisation paresseuse est appliquée.
