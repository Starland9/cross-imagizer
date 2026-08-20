# Research: Refonte de la disposition principale

**Date**: 2026-08-20

## Questions résolues

### Q1 — Comment structurer la fenêtre pour éviter le grand espace vide de la drop zone ?

**Decision**: Transformer la zone de dépôt en bandeau compact au-dessus de la
zone de travail, et l'utiliser aussi comme aperçu quand des images sont
présentes. La drop zone ne doit plus occuper 50 % de la hauteur.

**Rationale**:
- Un bandeau d'action (header + drop zone compacte) est un pattern classique
  des outils de conversion/batch (HandBrake, ImageOptim, XnConvert) : il guide
  l'utilisateur sans gaspiller l'espace vertical.
- L'aperçu de la première image peut remplacer le message d'invitation dès
  qu'un fichier est ajouté, ce qui réduit l'espace vide perçu.
- Cela satisfait FR-001, FR-002, SC-001.

**Alternatives considered**:
- Garder la drop zone en haut à 100 % de largeur mais réduire sa hauteur à
  ~120 px. Rejeté : même compactée, une barre horizontale seule est moins
  utile qu'un bandeau + aperçu.
- Ouvrir directement le sélecteur de fichiers au démarrage. Rejeté : cela
  déplace le problème sans résoudre la structure globale.

---

### Q2 — Comment regrouper la file d'attente et l'historique sans perdre en clarté ?

**Decision**: Utiliser un `QTabWidget` à droite de la zone centrale, avec deux
onglets : « File » et « Historique ». Le panneau d'options reste à largeur fixe
à gauche, et la zone d'aperçu/dépôt occupe le centre.

**Rationale**:
- Les onglets sont le widget natif PySide6 le plus simple pour partager une
  zone sans complexité. Ils garantissent que la file ou l'historique dispose
  de toute la largeur disponible pour afficher les chemins.
- Cela respecte FR-004 et SC-003 (chemins complets lisibles).
- L'utilisateur peut basculer entre les deux vues sans scinder davantage
  l'interface.

**Alternatives considered**:
- Empilement vertical file au-dessus + historique en dessous. Rejeté : cela
  réduit la hauteur utile de chaque liste et crée du scroll excessif.
- Panneau latéral droit avec `QSplitter` dédié. Rejeté : cela ramène le
  problème de quatre colonnes ; un onglet est plus compact.

---

### Q3 — Comment hiérarchiser la barre d'actions ?

**Decision**:
- Bouton **Convertir** en couleur primaire, légèrement plus haut, placé à
droite (ou centrée) de la barre.
- À gauche : groupe « Fichier » (Ajouter des images, Dossier de sortie,
  Ouvrir le dossier).
- Au centre/droite : groupe « Contrôle » (Annuler) et groupe « Affichage »
  (Thème).
- Utiliser des espacements plus larges entre les groupes qu'entre les
  boutons d'un même groupe.

**Rationale**:
- Le pattern Figma/Sketch/Adobe est d'ancrer l'action principale à droite ou
  au centre visuel, avec des boutons d'import/export groupés à gauche.
- Cela répond à FR-005 et FR-006 et rend le bouton de conversion immédiatement
  identifiable (SC-004).

**Alternatives considered**:
- Barre d'outils `QToolBar` en haut. Rejeté : cela disperserait les actions
  dans l'en-tête et complexifierait la structure. La barre du bas reste plus
  proche de l'action principale.

---

### Q4 — Comment ajouter un en-tête / identité visuelle sans dépendances tierces ?

**Decision**: Créer un petit widget d'en-tête personnalisé dans
`main_window.py` (ou `src/app/ui/widgets/app_header.py`) affichant :
- une icône de l'application (`windowIcon` existant ou icône SVG embarquée) ;
- le nom « Cross-Imagizer » ;
- éventuellement un sous-titre ou tagline légère.

**Rationale**:
- Cela répond à FR-008 sans créer de logo dédié (conforme à l'hypothèse du
  spec).
- L'objet reste simple, testable (existence du widget + texte) et thémable.

**Alternatives considered**:
- Supprimer le titre de fenêtre natif et dessiner une titlebar personnalisée.
  Rejeté : hors scope et risque cross-platform (macOS vs Windows).

---

### Q5 — Quels styles/états vides ajouter ?

**Decision**:
- Drop zone vide : icône + texte « Glissez-déposez des images ici » + lien
  « ou cliquez pour parcourir ».
- File vide : message « Aucune image en attente » + icône.
- Historique vide : message « Aucune conversion pour le moment » + icône.
- Les couleurs des messages vides utilisent `COLOR_*_TEXT_MUTED` des tokens
  existants.

**Rationale**:
- Les états vides explicites améliorent la perception de qualité (FR-007) et
  restent lisibles dans les deux thèmes (SC-005).
- Utiliser les tokens existants garantit la cohérence et minimise les ajouts.

---

## Résumé des décisions

| Sujet | Décision |
|-------|----------|
| Layout global | Header + drop zone compacte + corps à 3 zones (options fixe, aperçu, onglets file/historique) + barre d'actions hiérarchisée |
| Drop zone | Bandeau compact en haut du corps, remplacé par l'aperçu dès qu'une image est ajoutée |
| Options | Largeur fixe (~260 px), alignée à gauche |
| File + Historique | `QTabWidget` à droite, largeur flexible |
| Actions | Convertir primaire/dominant ; groupes Fichier / Contrôle / Affichage |
| Header | Widget texte + icône, pas de titlebar personnalisée |
| États vides | Messages + icônes, couleurs muted existantes |
| Responsive | Largeur min 800 px, hauteur min 500 px ; pas de layout alternatif, juste des tailles minimales et des splitters |
