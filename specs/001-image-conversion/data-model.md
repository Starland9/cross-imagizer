# Data Model: Conversion d'images multi-formats

## Entités

### ImageSource

Représente un fichier image d'entrée.

| Champ         | Type   | Description                                     |
| ------------- | ------ | ----------------------------------------------- |
| `path`        | `Path` | Chemin absolu du fichier source                 |
| `format`      | `str`  | Format détecté (extension + contenu)            |
| `width`       | `int`  | Largeur en pixels (si lisible)                  |
| `height`      | `int`  | Hauteur en pixels (si lisible)                  |
| `is_animated` | `bool` | Indique si l'image est animée (GIF, WebP animé) |
| `metadata`    | `dict` | Métadonnées EXIF/autres pertinentes             |

**Règles de validation**:

- `path` MUST exister et être un fichier lisible.
- `format` MUST être détecté à l'ouverture ; une image illisible produit une
  erreur explicite (FR-002).

### ConversionOptions

Réglages appliqués à une tâche de conversion.

| Champ               | Type          | Description                                               |
| ------------------- | ------------- | --------------------------------------------------------- |
| `target_format`     | `str`         | Format de sortie (JPEG, PNG, WebP, …)                     |
| `quality`           | `int \| None` | Niveau de qualité (1–100) pour les formats avec perte     |
| `resize_width`      | `int \| None` | Largeur cible (proportion conservée si hauteur absente)   |
| `resize_height`     | `int \| None` | Hauteur cible                                             |
| `collision_policy`  | `enum`        | `overwrite` \| `rename` \| `ask` (FR-010)                 |
| `preserve_metadata` | `bool`        | Préserver les métadonnées si le format le permet (FR-011) |

**Règles de validation**:

- `target_format` MUST être un format pris en charge.
- `quality` MUST être dans [1, 100] si fourni.
- Au moins une dimension de redimensionnement si le redimensionnement est demandé.

### ConversionTask

Une opération unitaire de conversion.

| Champ         | Type                | Description                                |
| ------------- | ------------------- | ------------------------------------------ |
| `id`          | `str`               | Identifiant unique                         |
| `source`      | `ImageSource`       | Image d'entrée                             |
| `options`     | `ConversionOptions` | Réglages de conversion                     |
| `output_path` | `Path \| None`      | Chemin de sortie (résolu après conversion) |
| `status`      | `enum`              | État (voir transitions)                    |
| `error`       | `str \| None`       | Message d'erreur si échec                  |

**Transitions d'état**:

```text
PENDING → RUNNING → SUCCEEDED
                 → FAILED
PENDING → CANCELLED
RUNNING → CANCELLED
```

### Batch

Un ensemble de tâches traitées ensemble.

| Champ      | Type                   | Description                                          |
| ---------- | ---------------------- | ---------------------------------------------------- |
| `id`       | `str`                  | Identifiant unique                                   |
| `tasks`    | `list[ConversionTask]` | Tâches du lot                                        |
| `progress` | `tuple[int, int]`      | (traité, total)                                      |
| `status`   | `enum`                 | `PENDING` \| `RUNNING` \| `COMPLETED` \| `CANCELLED` |
| `report`   | `BatchReport`          | Rapport récapitulatif (FR-015)                       |

### BatchReport

Résultat d'un lot.

| Champ       | Type         | Description                         |
| ----------- | ------------ | ----------------------------------- |
| `succeeded` | `int`        | Nombre de conversions réussies      |
| `failed`    | `int`        | Nombre d'échecs                     |
| `cancelled` | `int`        | Nombre d'annulations                |
| `failures`  | `list[dict]` | Détail des échecs (fichier, raison) |

## Relations

```text
Batch 1 ──── * ConversionTask
ConversionTask 1 ──── 1 ImageSource
ConversionTask 1 ──── 1 ConversionOptions
Batch 1 ──── 1 BatchReport
```
