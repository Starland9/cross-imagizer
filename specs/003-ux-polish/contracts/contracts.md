# Contrats d'interface: Amélioration de l'UX

## 1. Ouverture du dossier (`platform_utils/open_folder`)

### `open_folder(path: Path) -> bool`

Ouvre le dossier `path` dans le gestionnaire de fichiers natif.

- **Entrée**: chemin d'un dossier existant.
- **Sortie**: `True` si l'ouverture a réussi, `False` sinon (dégradation
  silencieuse, sans exception).
- **Contrat**: portable sur Windows, macOS et Linux.

## 2. Mise en page (`main_window`)

### Contrat de layout

- Les panneaux (aperçu, options, batch, historique) MUST être proportionnés et
  redimensionnables (via `QSplitter`).
- Aucune colonne vide disproportionnée à l'ouverture.
- La mise en page MUST s'adapter au redimensionnement de la fenêtre.

## 3. Retours visuels

- Le bouton « Convertir » MUST être désactivé pendant une conversion.
- Une conversion terminée MUST afficher un retour de succès ou d'erreur.
- Le bouton « Ouvrir le dossier de sortie » MUST être disponible après une
  conversion réussie.
