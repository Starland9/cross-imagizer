"""Fenêtre principale de l'application."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.services import batch_service
from app.ui.widgets.batch_panel import BatchPanel
from app.ui.widgets.drop_zone import DropZone
from app.ui.widgets.options_panel import OptionsPanel
from app.ui.widgets.preview_pane import PreviewPane
from models import BatchReport
from platform_utils import notifications


class MainWindow(QMainWindow):
    """Fenêtre principale de Cross-Imagizer."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Cross-Imagizer")
        self.resize(900, 640)

        self._batch_service = batch_service.BatchService()
        self._batch_service.progress.connect(self._on_progress)
        self._batch_service.finished.connect(self._on_finished)
        self._batch_service.cancelled.connect(self._on_cancelled)

        self._build_ui()

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)

        # Zone de dépôt
        self._drop_zone = DropZone()
        self._drop_zone.files_dropped.connect(self._on_files_dropped)
        root.addWidget(self._drop_zone)

        # Corps : aperçu + options + batch
        body = QHBoxLayout()
        self._preview = PreviewPane()
        body.addWidget(self._preview, 1)

        self._options = OptionsPanel()
        body.addWidget(self._options, 1)

        self._batch_panel = BatchPanel()
        body.addWidget(self._batch_panel, 1)
        root.addLayout(body)

        # Boutons
        buttons = QHBoxLayout()
        self._add_btn = QPushButton("Ajouter des images")
        self._add_btn.clicked.connect(self._pick_files)
        buttons.addWidget(self._add_btn)

        self._convert_btn = QPushButton("Convertir")
        self._convert_btn.setObjectName("secondary")
        self._convert_btn.clicked.connect(self._convert)
        buttons.addWidget(self._convert_btn)

        self._cancel_btn = QPushButton("Annuler")
        self._cancel_btn.setObjectName("secondary")
        self._cancel_btn.clicked.connect(self._cancel)
        self._cancel_btn.setEnabled(False)
        buttons.addWidget(self._cancel_btn)

        self._theme_btn = QPushButton("Thème sombre")
        self._theme_btn.setObjectName("secondary")
        self._theme_btn.clicked.connect(self._toggle_theme)
        buttons.addWidget(self._theme_btn)
        root.addLayout(buttons)

        self._dark = False

    def _pick_files(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(self, "Sélectionner des images")
        if paths:
            self._on_files_dropped([Path(p) for p in paths])

    def _on_files_dropped(self, paths: list[Path]) -> None:
        self._batch_panel.add_files(paths)
        if paths:
            self._preview.show_image(paths[0])

    def _convert(self) -> None:
        files = self._batch_panel.files()
        if not files:
            QMessageBox.information(self, "Aucune image", "Ajoutez d'abord des images.")
            return
        options = self._options.options()
        batch = self._batch_service.create_batch(files, options)
        self._batch_service.run(batch, options)
        self._convert_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)

    def _cancel(self) -> None:
        self._batch_service.cancel()

    def _on_progress(self, done: int, total: int) -> None:
        self._batch_panel.set_progress(done, total)

    def _on_finished(self, report: BatchReport) -> None:
        self._convert_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        notifications.notify(
            "Conversion terminée",
            f"{report.succeeded} réussie(s), {report.failed} échec(s)",
        )
        QMessageBox.information(
            self,
            "Conversion terminée",
            f"{report.succeeded} réussie(s), {report.failed} échec(s), "
            f"{report.cancelled} annulée(s)",
        )

    def _on_cancelled(self) -> None:
        self._convert_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)

    def _toggle_theme(self) -> None:
        self._dark = not self._dark
        from PySide6.QtWidgets import QApplication

        from app.ui.theme.theme import apply_theme

        app = QApplication.instance()
        if isinstance(app, QApplication):
            apply_theme(app, self._dark)
        self._theme_btn.setText("Thème clair" if self._dark else "Thème sombre")
