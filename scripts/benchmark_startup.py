"""Benchmark MainWindow creation time."""

from __future__ import annotations

import statistics
import sys
import time

from PySide6.QtWidgets import QApplication

sys.path.insert(0, "src")

from app.ui.main_window import MainWindow


def run(runs: int = 5) -> float:
    """Measure MainWindow creation time and return the median."""
    app = QApplication.instance() or QApplication([])
    times: list[float] = []
    for _ in range(runs):
        t0 = time.perf_counter()
        window = MainWindow()
        t1 = time.perf_counter()
        times.append(t1 - t0)
        window.close()
    app.processEvents()
    return statistics.median(times)


if __name__ == "__main__":
    median = run()
    print(f"MainWindow creation median: {median:.6f}s")
