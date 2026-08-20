# Quickstart: Conversion d'images multi-formats

Guide de validation de bout en bout de la feature. Les détails d'implémentation
sont dans `tasks.md` et la phase d'implémentation.

## Prérequis

- Python 3.11+ installé.
- Environnement virtuel créé et dépendances installées (voir `pyproject.toml`).

## Scénarios de validation

### 1. Conversion d'une image unique (US1)

1. Lancer l'application.
2. Sélectionner une image (ex. `photo.jpg`).
3. Choisir le format cible `PNG`.
4. Lancer la conversion.

**Résultat attendu**: un fichier `photo.png` valide est produit à côté de la
source ; l'aperçu et le résultat sont corrects.

### 2. Conversion par lot (US2)

1. Sélectionner un dossier contenant plusieurs images de formats variés.
2. Lancer la conversion par lot vers `WebP`.

**Résultat attendu**: toutes les images convertibles sont traitées ; la
progression est visible ; un rapport récapitule succès et échecs.

### 3. Traitement en arrière-plan + notification (US3)

1. Lancer un lot volumineux.
2. Naviguer dans l'application pendant le traitement (l'UI reste réactive).
3. Attendre la fin.

**Résultat attendu**: une notification native indique le résultat ; l'interface
n'a jamais été bloquée.

### 4. Aperçu et options (US4)

1. Sélectionner une image.
2. Ajuster la qualité (ex. 50) et/ou les dimensions.
3. Convertir.

**Résultat attendu**: le fichier de sortie reflète les réglages (taille, qualité).

### 5. Glisser-déposer (US5)

1. Glisser plusieurs fichiers dans la fenêtre.

**Résultat attendu**: les fichiers sont ajoutés à la file de conversion.

## Commandes de test

```bash
# Tests unitaires
pytest tests/unit

# Tests d'intégration
pytest tests/integration

# Couverture
pytest --cov=src --cov-report=term-missing
```

## Critères de succès à vérifier

- Conversion d'une image < 5 s (SC-001).
- Lot de 100 images sans blocage UI (SC-002).
- Démarrage < 3 s (SC-004).
- Comportement identique sur Windows, macOS, Linux (SC-006).
