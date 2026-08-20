# Data Model: Amélioration de l'UX

Cette feature n'introduit **aucune nouvelle entité de données**. Elle réutilise
le `OutputDirectory` (dossier de sortie) de la feature 002 et n'ajoute que des
éléments d'interface.

## Entités réutilisées

- **Dossier de sortie** (feature 002) : chemin de destination, persisté via
  `QSettings`, utilisé par le bouton « Ouvrir le dossier de sortie ».

## Relations

Aucune nouvelle relation. Le bouton « Ouvrir le dossier » lit le dossier de
sortie courant (ou le dossier par défaut à côté de la source).
