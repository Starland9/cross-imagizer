# Research: Dossier de sortie, barre de tâche & historique

## Décisions techniques

### D1. Persistance : QSettings

- **Decision**: Utiliser `QSettings` (préférences natives) pour persister le
  dossier de sortie et l'historique (sérialisé en JSON).
- **Rationale**: `QSettings` est portable (Windows registry, macOS plist, Linux
  INI), léger, et déjà disponible via PySide6. Aucune dépendance supplémentaire.
  Conforme au principe V (simplicité) et III (performance).
- **Alternatives considérées**:
  - *SQLite* : surdimensionné pour un historique borné à 500 entrées.
  - *Fichier JSON manuel* : réinvente ce que QSettings fait déjà.

### D2. Icône de barre de tâche : QSystemTrayIcon

- **Decision**: `QSystemTrayIcon` avec un `QMenu` contextuel (ouvrir, convertir,
  quitter).
- **Rationale**: API Qt standard, portable sur les trois OS, intégrée à PySide6.
  Dégradation silencieuse si `isSystemTrayAvailable()` est faux.
- **Alternatives considérées**:
  - *pystray* : dépendance tierce inutile alors que Qt le fournit nativement.

### D3. Historique : liste bornée

- **Decision**: Historique en mémoire + persistance JSON via QSettings, limité à
  500 entrées (purge des plus anciennes).
- **Rationale**: borne explicite pour maîtriser la mémoire (principe III) et
  éviter une croissance non bornée.
- **Alternatives considérées**: historique illimité (rejeté — risque mémoire).

### D4. Câblage du dossier de sortie

- **Decision**: Réutiliser le paramètre `output_dir` déjà présent dans
  `collision.resolve_output_path()` et `converter.convert()`, en le propageant
  depuis un `SettingsService` vers le `BatchService`/`conversion_service`.
- **Rationale**: le moteur de la feature 001 expose déjà ce paramètre (actuellement
  `None`) ; il suffit de le câbler, sans réécrire le moteur.
- **Alternatives considérées**: réécrire le moteur (rejeté — YAGNI).

## Points d'attention

- **Fermeture de la fenêtre** : intercepter l'événement de fermeture pour
  masquer la fenêtre (au lieu de quitter) tant que le tray est actif.
- **Quitter proprement** : le menu « Quitter » du tray doit arrêter les workers
  en cours avant de fermer l'application.
- **Dégradation** : si le tray n'est pas disponible, la fermeture de la fenêtre
  quitte l'application (comportement actuel).
