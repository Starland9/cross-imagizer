# Research: Polish UX avancé

## Décisions techniques

### D1. Centralisation des valeurs de design : tokens.py

- **Decision**: Créer un module `tokens.py` centralisant les valeurs de design
  (espacements, tailles min/max, polices, couleurs) sous forme de constantes.
- **Rationale**: évite la dispersion des valeurs dans le QSS et le code ;
  facilite la maintenance et la cohérence. Conforme au principe I (code propre).
- **Alternatives considérées**:
  - *Valeurs en dur dans le QSS* : dispersion, difficile à maintenir.
  - *Fichier JSON externe* : surdimensionné pour ce besoin (YAGNI).

### D2. Tailles des panneaux : setMinimumWidth / setMaximumWidth

- **Decision**: Définir des largeurs minimales et maximales sur chaque panneau
  via `setMinimumWidth`/`setMaximumWidth` et `QSizePolicy`.
- **Rationale**: empêche les disproportions (panneau trop large ou trop étroit)
  tout en gardant le redimensionnement via `QSplitter` (feature 003).
- **Alternatives considérées**:
  - *Largeurs fixes* : non adaptatif, contraire à la feature 003.
  - *Stretch factors uniquement* : ne borne pas les extrêmes.

### D3. Espacements : marges QSS uniformes

- **Decision**: Définir des marges et espacements uniformes via le QSS
  (`padding`, `margin`) en utilisant les tokens centralisés.
- **Rationale**: assure la cohérence visuelle sans code dispersé.
- **Alternatives considérées**: marges par widget (rejeté — dispersion).

### D4. Hiérarchie typographique : QSS font-weight + font-size

- **Decision**: Hiérarchiser via QSS (`font-size`, `font-weight`) avec des
  classes d'objets (titres, labels, contenus).
- **Rationale**: QSS supporte la typographie de manière portable.
- **Alternatives considérées**: `QFont` par widget (rejeté — dispersion).

### D5. États visuels : pseudo-états QSS

- **Decision**: Utiliser les pseudo-états QSS (`:hover`, `:pressed`,
  `:disabled`) pour les états visuels des éléments interactifs.
- **Rationale**: support natif de Qt, portable, léger.
- **Alternatives considérées**: gestion manuelle des événements (rejeté —
  complexité inutile).

### D6. Réalignement des widgets : QFormLayout / QGridLayout + alignement

- **Decision**: Utiliser `QFormLayout` (alignement labels/champs) et
  `QGridLayout` (alignement en grille) avec des propriétés d'alignement
  explicites (`Qt.AlignmentFlag`) pour réaligner les widgets au sein de chaque
  groupe.
- **Rationale**: Qt fournit des layouts d'alignement matures et portables ;
  `QFormLayout` aligne naturellement les labels entre eux et les champs entre
  eux, et `QGridLayout` garantit un alignement en colonnes/lignes cohérent.
- **Alternatives considérées**:
  - *QHBoxLayout/QVBoxLayout manuel avec insertStretch* : plus fragile,
    alignement difficile à maintenir.
  - *Alignement via QSS uniquement* : QSS ne gère pas l'alignement structurel
    des layouts.

## Points d'attention

- **Cohérence thème clair/sombre** : les états visuels doivent être définis dans
  les deux thèmes.
- **Petits écrans** : les tailles minimales ne doivent pas rendre l'interface
  inutilisable (valeurs raisonnables).