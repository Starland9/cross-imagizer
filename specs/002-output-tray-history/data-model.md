# Data Model: Dossier de sortie, barre de tâche & historique

## Entités

### OutputDirectory

Dossier de destination choisi par l'utilisateur.

| Champ | Type | Description |
|-------|------|-------------|
| `path` | `Path \| None` | Chemin du dossier de sortie (None = à côté de la source) |

**Règles de validation**:
- Si défini, `path` MUST être un dossier existant et accessible en écriture.
- Persisté via `QSettings` (clé `output_directory`).

### HistoryEntry

Enregistrement d'une conversion passée.

| Champ | Type | Description |
|-------|------|-------------|
| `source` | `str` | Chemin du fichier source |
| `output` | `str \| None` | Chemin du fichier de sortie (None si échec) |
| `status` | `str` | `succeeded` \| `failed` \| `cancelled` |
| `timestamp` | `str` | Date/heure ISO 8601 |
| `error` | `str \| None` | Raison de l'échec éventuelle |

**Règles de validation**:
- `status` MUST être l'une des valeurs autorisées.
- `timestamp` MUST être au format ISO 8601.
- L'historique est borné à 500 entrées (purge des plus anciennes).

## Relations

```text
HistoryEntry 1 ──── 1 ConversionTask (feature 001, source de l'enregistrement)
OutputDirectory 1 ──── * ConversionTask (dossier de destination)
```

## Transitions d'état

L'historique est **append-only** : les entrées sont ajoutées à la fin et jamais
modifiées ; seules les plus anciennes sont purgées au-delà de 500.
