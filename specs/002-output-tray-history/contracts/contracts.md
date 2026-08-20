# Contrats d'interface: Dossier de sortie, barre de tâche & historique

## 1. Service de réglages (`settings_service`)

### `get_output_directory() -> Path | None`

Retourne le dossier de sortie persisté, ou `None` si non défini.

### `set_output_directory(path: Path | None) -> None`

Persiste le dossier de sortie. Lève `ValueError` si le chemin n'est pas un
dossier accessible en écriture.

## 2. Service d'historique (`history_service`)

### `record(source: str, output: str | None, status: str, error: str | None) -> None`

Ajoute une entrée à l'historique et persiste. Purge au-delà de 500 entrées.

### `list_entries() -> list[HistoryEntry]`

Retourne l'historique, du plus récent au plus ancien.

### `clear() -> None`

Vide l'historique.

## 3. Icône de barre de tâche (`tray`)

### Contrat de comportement

- `TrayIcon` expose un menu contextuel : « Ouvrir », « Convertir », « Quitter ».
- La fermeture de la fenêtre principale masque la fenêtre (ne quitte pas) tant
  que le tray est actif.
- « Quitter » arrête les workers en cours puis ferme l'application.
- Si `QSystemTrayIcon.isSystemTrayAvailable()` est faux, le tray est désactivé
  et la fermeture de la fenêtre quitte l'application.

## 4. Câblage du dossier de sortie

- Le `BatchService` et `conversion_service` acceptent un `output_dir: Path | None`
  propagé au moteur de conversion (paramètre `output_dir` déjà présent).
