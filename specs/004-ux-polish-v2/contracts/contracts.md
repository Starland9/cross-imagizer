# Contrats d'interface: Polish UX avancé

## 1. Design tokens (`tokens.py`)

### Contrat

`tokens.py` expose des constantes de design utilisées par le thème QSS et les
widgets :

- `SPACING_*` : espacements uniformes (small, medium, large).
- `PANEL_MIN_WIDTH`, `PANEL_MAX_WIDTH` : bornes des panneaux.
- `FONT_SIZE_*`, `FONT_WEIGHT_*` : hiérarchie typographique.
- `COLOR_*` : couleurs des états (normal, survol, pressé, désactivé) pour les
  thèmes clair et sombre.

## 2. Thème (`theme.py`)

### Contrat

- Le QSS MUST utiliser les tokens de `tokens.py` (pas de valeurs en dur).
- Les pseudo-états (`:hover`, `:pressed`, `:disabled`) MUST être définis pour
  les boutons et éléments interactifs.
- Les deux thèmes (clair, sombre) MUST définir des états visuels cohérents.

## 3. Tailles des widgets (`main_window.py`, `widgets/`)

### Contrat

- Chaque panneau MUST avoir une largeur minimale et maximale (via tokens).
- Les widgets MUST utiliser `QSizePolicy` pour un redimensionnement cohérent.
- Aucun panneau ne dépasse 40 % de la largeur de la fenêtre sans justification.

## 4. Alignement des widgets (`main_window.py`, `widgets/`)

### Contrat

- Les widgets d'un même groupe MUST être alignés sur un même axe via
  `QFormLayout` (labels/champs) ou `QGridLayout` (grille cohérente).
- Les labels d'un même formulaire MUST être alignés entre eux, et les champs
  associés MUST être alignés entre eux.
- L'alignement MUST rester cohérent au redimensionnement de la fenêtre.