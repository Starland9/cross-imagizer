# Data Model: Polish UX avancé

Cette feature n'introduit **aucune entité de données**. Elle est purement
visuelle et réutilise les entités existantes (features 001 à 003).

## Éléments de design (non persistés)

- **Design tokens** : valeurs centralisées (espacements, tailles, polices,
  couleurs) exposées par `tokens.py` et consommées par le thème QSS.
- Ces tokens ne sont pas des données métier ; ce sont des constantes de
  configuration visuelle.