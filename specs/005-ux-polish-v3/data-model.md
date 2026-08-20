# Data Model: Refonte de la disposition principale

**Date**: 2026-08-20

## Overview

Cette feature est purement UI/UX : elle ne modifie pas les entités métier
existantes (`ConversionJob`, `Batch`, `ConversionOptions`, `BatchReport`,
`ConversionRecord`). Elle introduit uniquement des entités de présentation
pour structurer la nouvelle interface.

## Existing Entities (unchanged)

### ConversionOptions

| Field | Type | Notes |
|-------|------|-------|
| target_format | str | Format cible (JPEG, PNG, etc.) |
| quality | int | Qualité JPEG/WebP (1-100) |
| width | int \| None | Largeur cible, `None` = auto |
| height | int \| None | Hauteur cible, `None` = auto |
| on_conflict | str | Stratégie de conflit de nom |

### ConversionJob

| Field | Type | Notes |
|-------|------|-------|
| source | Path | Fichier source |
| destination | Path | Fichier de sortie |

### BatchReport

| Field | Type | Notes |
|-------|------|-------|
| succeeded | int | Nombre de conversions réussies |
| failed | int | Nombre d'échecs |
| cancelled | int | Nombre d'annulations |

### ConversionRecord (history)

| Field | Type | Notes |
|-------|------|-------|
| source | str | Chemin source |
| destination | str | Chemin de sortie |
| timestamp | datetime | Date/heure de la conversion |
| status | str | `succeeded`, `failed`, etc. |

## New Presentation Entities

### AppHeader (nouveau widget)

| Field | Type | Notes |
|-------|------|-------|
| title_label | QLabel | Affiche le nom de l'application |
| icon_label | QLabel | Affiche l'icône/logo léger |

**Responsibility**: Afficher l'identité visuelle en haut de la fenêtre.

### DropZone (modifié)

| Field | Type | Notes |
|-------|------|-------|
| empty_state | QWidget | Message + icône d'invitation |
| preview | PreviewPane | Aperçu de l'image courante quand disponible |
| is_compact | bool | Indique si la zone est en mode bandeau |

**State transitions**:
- `empty` → `preview` : lors du premier fichier déposé/ajouté.
- `preview` → `empty` : quand tous les fichiers sont retirés (si cette action
  est permise).

### BatchPanel (modifié)

| Field | Type | Notes |
|-------|------|-------|
| empty_state | QWidget | Message « Aucune image en attente » |
| list_view | QListView / QListWidget | Liste des fichiers |
| progress | QProgressBar | Progression de la conversion |

**State transitions**:
- `empty` → `populated` : ajout de fichiers.
- `populated` → `empty` : conversion terminée ou fichiers effacés.

### HistoryPanel (modifié)

| Field | Type | Notes |
|-------|------|-------|
| empty_state | QWidget | Message « Aucune conversion pour le moment » |
| list_view | QListView / QListWidget | Liste des enregistrements |

**State transitions**:
- `empty` → `populated` : après la première conversion réussie/échouée
  enregistrée.

### SideTabs (nouveau conteneur)

| Field | Type | Notes |
|-------|------|-------|
| tabs | QTabWidget | Contient `BatchPanel` et `HistoryPanel` |
| tab_batch | QWidget | Onglet « File d'attente » |
| tab_history | QWidget | Onglet « Historique » |

**Responsibility**: Regrouper la file d'attente et l'historique dans une
zone unique à droite de l'interface.

### ActionBar (nouveau conteneur)

| Field | Type | Notes |
|-------|------|-------|
| file_group | QHBoxLayout | Ajouter, Dossier de sortie, Ouvrir le dossier |
| primary_action | QPushButton | Convertir (mis en avant) |
| control_group | QHBoxLayout | Annuler |
| view_group | QHBoxLayout | Thème |

**Responsibility**: Organiser les actions de la barre du bas par groupe
fonctionnel et hiérarchie visuelle.

## Relationships

```text
MainWindow
├── AppHeader
├── CentralArea
│   ├── DropZone (compact / preview)
│   └── Workbench
│       ├── OptionsPanel (largeur fixe)
│       ├── PreviewPane (zone centrale)
│       └── SideTabs
│           ├── BatchPanel
│           └── HistoryPanel
└── ActionBar
    ├── file_group
    ├── primary_action (Convertir)
    ├── control_group
    └── view_group
```

## Validation Rules

- `AppHeader.title_label` doit afficher « Cross-Imagizer ».
- `OptionsPanel` doit respecter une largeur fixe de 240–280 px par défaut et
  ne pas dépasser 320 px.
- `SideTabs` doit permettre l'affichage des chemins complets sur une fenêtre
  de 1280 px.
- `ActionBar.primary_action` (Convertir) doit être visuellement dominant.
- Tous les états vides doivent s'afficher quand le modèle sous-jacent est vide.

## State Transitions Summary

| Entity | From | To | Trigger |
|--------|------|----|---------|
| DropZone | empty | preview | Fichier(s) ajouté(s) |
| DropZone | preview | empty | Dernier fichier retiré |
| BatchPanel | empty | populated | Fichier(s) ajouté(s) |
| BatchPanel | populated | empty | Liste vidée |
| HistoryPanel | empty | populated | Première conversion enregistrée |
