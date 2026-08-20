# Quickstart: Validation de la refonte UX v3

**Date**: 2026-08-20

## Prerequisites

- Python 3.11+
- Environnement virtuel activé (`source .venv/bin/activate`)
- Dépendances installées (`pip install -e .` ou `pip install -r requirements.txt`)
- Variables d'environnement pour exécution headless (tests) :
  ```bash
  export QT_QPA_PLATFORM=offscreen
  ```

## End-to-End Validation Scenarios

### Scenario 1 — Lancer l'application et vérifier la nouvelle structure

1. Lancer l'application :
   ```bash
   python -m app.main
   ```
2. Observer la fenêtre.
3. **Expected outcome** :
   - Un en-tête avec l'icône et le titre « Cross-Imagizer » est visible.
   - La zone de dépôt est un bandeau compact (pas une grande zone vide).
   - Le workbench montre trois zones : options à gauche, aperçu au centre,
     onglets « File / Historique » à droite.
   - La barre du bas a le bouton « Convertir » en couleur primaire.

### Scenario 2 — Ajouter des images et vérifier la mise à jour des états

1. Cliquer sur « Ajouter des images » ou glisser-déposer des images.
2. **Expected outcome** :
   - L'aperçu de la première image apparaît dans la zone centrale.
   - La file d'attente affiche les chemins complets dans l'onglet « File ».
   - L'état vide de l'onglet « File » disparaît.

### Scenario 3 — Lancer une conversion

1. Sélectionner un dossier de sortie (bouton « Dossier de sortie… »).
2. Cliquer sur « Convertir ».
3. **Expected outcome** :
   - Le bouton « Convertir » se désactive.
   - Le bouton « Annuler » s'active.
   - La barre de progression avance.
   - À la fin, l'onglet « Historique » affiche les enregistrements.

### Scenario 4 — Ouvrir le dossier de sortie

1. Après une conversion réussie, cliquer sur « Ouvrir le dossier ».
2. **Expected outcome** :
   - Le gestionnaire de fichiers du système s'ouvre sur le dossier de sortie.

### Scenario 5 — Basculer entre les thèmes

1. Cliquer sur « Thème sombre » / « Thème clair ».
2. **Expected outcome** :
   - L'en-tête, la zone de dépôt, les onglets et les états vides adoptent les
     couleurs du thème actif.
   - Aucun texte ou icône ne devient illisible.

## Test Commands

```bash
# Lint + type check
ruff check src tests
mypy src

# Test suite
pytest tests/unit tests/integration tests/contract -q

# Coverage (business code)
pytest --cov=src --cov-report=term-missing --cov-config=pyproject.toml
```

## Expected Test Results

- `ruff check src tests` → All checks passed.
- `mypy src` → Success: no issues found.
- `pytest` → 74+ tests passing, 0 failures.
- Couverture métier ≥ 80 %.

## Regression Checklist

- [ ] Conversion par lot fonctionne toujours.
- [ ] Sélection du dossier de sortie persiste via `QSettings`.
- [ ] Historique des conversions s'enregistre.
- [ ] Notification de fin de conversion s'affiche.
- [ ] Annulation pendant la conversion fonctionne.
- [ ] System tray (minimiser/restore) fonctionne.
- [ ] Le temps de création de `MainWindow` n'augmente pas de plus de 10 % par
  rapport à la baseline enregistrée dans `specs/005-ux-polish-v3/baseline-startup.md`.
- [ ] L'aire centrale vide sans image est inférieure à 25 % (mesurée par
  inspection visuelle ou script de capture).
