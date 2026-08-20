# Contrats d'interface: Conversion d'images multi-formats

Ce document définit les contrats des interfaces publiques du projet. Le moteur
de conversion (`core`) est la principale interface exposée ; l'UI et les services
en dépendent.

## 1. Moteur de conversion (`core`)

### `convert(source: Path, options: ConversionOptions) -> Path`

Convertit une image source vers le format cible.

- **Entrée**: chemin source valide + options de conversion.
- **Sortie**: chemin du fichier de sortie produit.
- **Erreurs**: lève `ConversionError` (avec message actionnable) si la source est
  illisible, le format non pris en charge, ou l'écriture impossible.
- **Contrat**: ne modifie jamais le fichier source ; respecte la politique de
  collision ; préserve les métadonnées si demandé et possible.

### `detect_format(path: Path) -> str`

Détecte le format d'une image.

- **Entrée**: chemin d'un fichier.
- **Sortie**: identifiant de format (ex. `"JPEG"`, `"PNG"`).
- **Erreurs**: lève `ConversionError` si le format est inconnu ou le fichier
  illisible.

### `supported_formats() -> list[str]`

Retourne la liste des formats de sortie pris en charge.

## 2. Service de lot (`services`)

### `BatchService.run(batch: Batch) -> None`

Exécute un lot en arrière-plan.

- **Signaux émis**: `progress(int done, int total)`, `task_finished(task)`,
  `finished(report: BatchReport)`, `cancelled()`.
- **Contrat**: n'exécute jamais de conversion sur le thread UI ; l'annulation
  (`cancel()`) interrompt proprement le lot.

## 3. Notifications (`platform`)

### `notify(title: str, message: str) -> None`

Affiche une notification native.

- **Contrat**: fonctionne sur Windows, macOS et Linux ; ne lève pas d'exception
  si les notifications ne sont pas disponibles (dégradation silencieuse).

## 4. Interface utilisateur (`ui`)

### Contrat de thème

- Deux palettes (`light`, `dark`) chargées via QSS.
- Toute couleur/typo MUST être définie dans le thème, jamais en dur dans les
  widgets.
- Les animations MUST rester fluides (60 fps cible) et désactivables.

### Contrat de widgets custom

- `DropZone` : accepte le glisser-déposer de fichiers, émet `files_dropped(paths)`.
- `ProgressBar` : affiche la progression d'un lot.
- `PreviewPane` : affiche un aperçu fidèle de l'image sélectionnée.
