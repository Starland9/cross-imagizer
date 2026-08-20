"""Fenêtre principale de l'application."""

from __future__ import annotations

import threading
from pathlib import Path

from PySide6.QtCore import Q_ARG, QMetaObject, Qt, Slot
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from app.services import batch_service, settings_service
from app.ui import animations
from app.ui.resources import icons
from app.ui.tray import TrayIcon
from app.ui.widgets.batch_panel import BatchPanel
from app.ui.widgets.drop_zone import DropZone
from app.ui.widgets.history_panel import HistoryPanel
from app.ui.widgets.options_panel import OptionsPanel
from app.ui.widgets.preview_pane import PreviewPane
from models import BatchReport
from platform_utils import notifications, open_folder


class MainWindow(QMainWindow):
    """Fenêtre principale de Cross-Imagizer."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Cross-Imagizer")
        self.resize(900, 640)

        self._confirm_event = threading.Event()
        self._confirm_answer = False
        self._tray: TrayIcon | None = None
        self._quitting = False

        self._batch_service = batch_service.BatchService()
        self._batch_service.progress.connect(self._on_progress)
        self._batch_service.finished.connect(self._on_finished)
        self._batch_service.cancelled.connect(self._on_cancelled)

        self._build_ui()

    def enable_tray(self, tray: TrayIcon) -> None:
        """Active le comportement de barre de tâche."""
        self._tray = tray

    def show_and_convert(self) -> None:
        """Ouvre la fenêtre et déclenche la sélection de fichiers."""
        self.show()
        self.raise_()
        self._pick_files()

    def quit_app(self) -> None:
        """Quitte proprement l'application (arrête les workers)."""
        self._quitting = True
        self._batch_service.cancel()
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        if isinstance(app, QApplication):
            app.quit()

    def closeEvent(self, event: object) -> None:  # noqa: N802
        """Masque la fenêtre au lieu de quitter si le tray est actif."""
        if self._tray is not None and not self._quitting:
            event.ignore()  # type: ignore[attr-defined]
            self.hide()
        else:
            event.accept()  # type: ignore[attr-defined]

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)

        # Zone de dépôt
        self._drop_zone = DropZone()
        self._drop_zone.files_dropped.connect(self._on_files_dropped)
        root.addWidget(self._drop_zone)

        # Corps : aperçu + options + batch + historique, équilibrés via QSplitter.
        self._preview = PreviewPane()
        self._options = OptionsPanel()
        self._batch_panel = BatchPanel()
        self._history_panel = HistoryPanel()

        self._splitter = QSplitter(Qt.Orientation.Horizontal)
        self._splitter.addWidget(self._preview)
        self._splitter.addWidget(self._options)
        self._splitter.addWidget(self._batch_panel)
        self._splitter.addWidget(self._history_panel)
        # Proportions initiales équilibrées (aperçu plus large, les autres égaux).
        self._splitter.setStretchFactor(0, 3)
        self._splitter.setStretchFactor(1, 2)
        self._splitter.setStretchFactor(2, 2)
        self._splitter.setStretchFactor(3, 2)
        self._splitter.setSizes([300, 200, 200, 200])
        root.addWidget(self._splitter)

        # Boutons
        buttons = QHBoxLayout()
        self._add_btn = QPushButton("Ajouter des images")
        self._add_btn.setIcon(icons.add_icon())
        self._add_btn.clicked.connect(self._pick_files)
        buttons.addWidget(self._add_btn)

        self._convert_btn = QPushButton("Convertir")
        self._convert_btn.setObjectName("secondary")
        self._convert_btn.setIcon(icons.convert_icon())
        self._convert_btn.clicked.connect(self._convert)
        buttons.addWidget(self._convert_btn)

        self._cancel_btn = QPushButton("Annuler")
        self._cancel_btn.setObjectName("secondary")
        self._cancel_btn.clicked.connect(self._cancel)
        self._cancel_btn.setEnabled(False)
        buttons.addWidget(self._cancel_btn)

        self._theme_btn = QPushButton("Thème sombre")
        self._theme_btn.setObjectName("secondary")
        self._theme_btn.setIcon(icons.theme_icon())
        self._theme_btn.clicked.connect(self._toggle_theme)
        buttons.addWidget(self._theme_btn)

        self._output_btn = QPushButton("Dossier de sortie…")
        self._output_btn.setObjectName("secondary")
        self._output_btn.clicked.connect(self._pick_output_dir)
        buttons.addWidget(self._output_btn)

        self._open_folder_btn = QPushButton("Ouvrir le dossier")
        self._open_folder_btn.setObjectName("secondary")
        self._open_folder_btn.clicked.connect(self._open_output_folder)
        self._open_folder_btn.setEnabled(False)
        buttons.addWidget(self._open_folder_btn)
        root.addLayout(buttons)

        self._dark = False
        self._output_dir: Path | None = settings_service.get_output_directory()

        # Animation d'apparition de la fenêtre.
        animations.fade_in(self)

    def _pick_output_dir(self) -> None:
        """Ouvre un sélecteur de dossier de sortie et le persiste."""
        directory = QFileDialog.getExistingDirectory(self, "Choisir un dossier de sortie")
        if not directory:
            return
        try:
            settings_service.set_output_directory(Path(directory))
            self._output_dir = Path(directory)
        except ValueError as exc:
            QMessageBox.warning(self, "Dossier invalide", str(exc))

    def _open_output_folder(self) -> None:
        """Ouvre le dossier de sortie courant dans le gestionnaire de fichiers."""
        target = self._output_dir
        if target is None:
            # Dossier par défaut : à côté de la première source de la file.
            files = self._batch_panel.files()
            target = files[0].parent if files else None
        if target is None:
            QMessageBox.information(self, "Aucun dossier", "Aucun dossier de sortie défini.")
            return
        if not open_folder.open_folder(target):
            QMessageBox.warning(self, "Ouverture impossible", f"Impossible d'ouvrir : {target}")

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
        self._batch_service.run(
            batch, options, confirm=self._confirm_overwrite, output_dir=self._output_dir
        )
        self._convert_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)

    @Slot(Path, result=bool)
    def _confirm_overwrite(self, candidate: Path) -> bool:
        """Demande confirmation d'écrasement (appelé depuis le thread worker)."""
        self._confirm_event.clear()
        self._confirm_answer = False
        # Marshal vers le thread UI de manière bloquante.
        QMetaObject.invokeMethod(
            self,
            "_show_overwrite_dialog",
            Qt.ConnectionType.BlockingQueuedConnection,
            Q_ARG(str, str(candidate)),
        )
        self._confirm_event.wait()
        return self._confirm_answer

    @Slot(str)
    def _show_overwrite_dialog(self, candidate: str) -> None:
        """Affiche le dialogue de confirmation d'écrasement (thread UI)."""
        answer = QMessageBox.question(
            self,
            "Fichier existant",
            f"Le fichier {candidate} existe déjà.\nVoulez-vous l'écraser ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        self._confirm_answer = answer == QMessageBox.StandardButton.Yes
        self._confirm_event.set()

    def _cancel(self) -> None:
        self._batch_service.cancel()

    def _on_progress(self, done: int, total: int) -> None:
        self._batch_panel.set_progress(done, total)

    def _on_finished(self, report: BatchReport) -> None:
        self._convert_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        self._history_panel.refresh()
        if report.succeeded > 0:
            self._open_folder_btn.setEnabled(True)
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
