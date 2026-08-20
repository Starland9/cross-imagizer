# UI Layout Contract: Refonte de la disposition principale

**Date**: 2026-08-20

## Purpose

Ce document définit les contrats visuels et structurels entre les widgets de la
fenêtre principale Cross-Imagizer après la refonte UX de la feature 005.

## Layout Contract

### Overall Window Structure

La fenêtre principale (`MainWindow`) DOIT être organisée verticalement comme
suit :

```text
+------------------------------------------+
| AppHeader                                |
+------------------------------------------+
| DropZone (compact / preview)             |
+------------------------------------------+
| Workbench                                |
| +-----------+----------------+---------+ |
| | Options   |   Preview      | SideTabs| |
| | (fixed)   |   (stretch)    | (stretch)| |
| +-----------+----------------+---------+ |
+------------------------------------------+
| ActionBar                                |
+------------------------------------------+
```

### Section 1 — AppHeader

- **Hauteur**: 48–56 px.
- **Contenu**:
  - Icône de l'application (32×32 px) à gauche.
  - Titre « Cross-Imagizer » en `FONT_SIZE_HEADING` / `FONT_WEIGHT_TITLE`.
  - Optionnellement un sous-titre léger en `FONT_SIZE_BODY` / muted.
- **Thème**: utilise `COLOR_*_BG` pour le fond et `COLOR_*_TEXT` pour le
texte, avec une bordure inférieure `COLOR_*_BORDER` de 1 px.

### Section 2 — DropZone

- **Mode compact** (aucune image) :
  - Hauteur fixe : 100–120 px.
  - Fond légèrement différent du fond global (`COLOR_*_SURFACE`).
  - Bordure en pointillés (`COLOR_*_BORDER`).
  - Message centré : icône + « Glissez-déposez des images ici » +
    « ou cliquez pour parcourir ».
- **Mode preview** (au moins une image) :
  - Hauteur flexible mais bornée entre 140 et 240 px.
  - Affiche l'aperçu de la première image sélectionnée.
  - Garde une zone de drop visible (overlay ou bordure).

### Section 3 — Workbench

- **OptionsPanel** :
  - Largeur fixe : 260 px (tolérance 240–280 px).
  - MaximumWidth : 320 px.
  - Aligne à gauche.
  - Titre « Options de conversion » en `FONT_SIZE_TITLE` /
    `FONT_WEIGHT_TITLE`.

- **PreviewPane** :
  - S'étire horizontalement et verticalement pour occuper l'espace central.
  - Affiche l'image courante avec `Qt.AspectRatioMode.KeepAspectRatio`.
  - Quand aucune image n'est sélectionnée, affiche un état vide discret
    (icône + texte muted).

- **SideTabs** :
  - Widget `QTabWidget` vertical à droite.
  - Deux onglets : « File d'attente » et « Historique ».
  - S'étire horizontalement avec une largeur minimale de 280 px.
  - Les chemins des fichiers doivent être lisibles sans troncature sur une
    fenêtre de 1280 px de large.

### Section 4 — ActionBar

- **Hauteur**: 48–56 px.
- **Gauche** — Groupe Fichier :
  - Boutons : Ajouter des images, Dossier de sortie, Ouvrir le dossier.
  - Icônes + texte compact.
- **Centre/Droite** — Groupe Conversion :
  - Bouton **Convertir** (action principale).
    - Couleur primaire (`COLOR_*_PRIMARY`).
    - Texte en gras (`FONT_WEIGHT_BUTTON`).
    - Padding vertical supérieur aux boutons secondaires.
  - Bouton Annuler (à côté, mais visuellement secondaire).
- **Extrême droite** — Groupe Affichage :
  - Bouton Thème (clair/sombre).
- **Espacement** :
  - 8 px entre boutons d'un même groupe.
  - 24 px minimum entre groupes.

## Color Contracts

Tous les nouveaux éléments visuels DOIVENT dériver des tokens existants :

| Element | Light Theme | Dark Theme |
|---------|-------------|------------|
| AppHeader bg | `COLOR_LIGHT_SURFACE` | `COLOR_DARK_SURFACE` |
| AppHeader border | `COLOR_LIGHT_BORDER` | `COLOR_DARK_BORDER` |
| AppHeader text | `COLOR_LIGHT_TEXT` | `COLOR_DARK_TEXT` |
| DropZone border | `COLOR_LIGHT_BORDER` | `COLOR_DARK_BORDER` |
| DropZone empty text | `COLOR_LIGHT_TEXT_MUTED` | `COLOR_DARK_TEXT_MUTED` |
| Primary button bg | `COLOR_LIGHT_PRIMARY` | `COLOR_DARK_PRIMARY` |
| Primary button hover | `COLOR_LIGHT_PRIMARY_HOVER` | `COLOR_DARK_PRIMARY_HOVER` |
| Secondary button bg | `COLOR_LIGHT_SECONDARY_BG` | `COLOR_DARK_SECONDARY_BG` |
| Muted text | `COLOR_LIGHT_TEXT_MUTED` | `COLOR_DARK_TEXT_MUTED` |

## Interaction Contracts

- Le bouton **Convertir** reste désactivé si aucun fichier n'est présent.
- Le bouton **Annuler** est activé uniquement pendant une conversion.
- **Ouvrir le dossier** est activé uniquement après au moins une conversion
  réussie (ou si un dossier de sortie est défini).
- Le changement de thème met à jour instantanément les couleurs de tous les
  nouveaux widgets (header, drop zone, états vides).

## Accessibility Contracts

- Tous les textes doivent respecter un contraste minimum de 4.5:1 par rapport
  à leur arrière-plan (WCAG AA).
- Les boutons doivent avoir des labels explicites.
- L'ordre de tabulation doit suivre la structure visuelle : header (sauté) →
  drop zone → options → preview → onglets → barre d'actions.
