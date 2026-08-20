# Quickstart: Amélioration de l'UX

Guide de validation de bout en bout. Les détails d'implémentation sont dans
`tasks.md`.

## Prérequis

- Application Cross-Imagizer (features 001 et 002) installée et fonctionnelle.

## Scénarios de validation

### 1. Mise en page équilibrée (US1)

1. Lancer l'application.
2. Observer la fenêtre.

**Résultat attendu**: les panneaux sont proportionnés, sans colonne vide
disgracieuse ; le redimensionnement de la fenêtre adapte proprement la mise en
page.

### 2. Ouvrir le dossier de sortie (US2)

1. Convertir une image.
2. Cliquer sur « Ouvrir le dossier de sortie ».

**Résultat attendu**: le dossier contenant le fichier converti s'ouvre dans le
gestionnaire de fichiers du système.

### 3. Retours visuels (US3)

1. Lancer une conversion.

**Résultat attendu**: la progression est visible, le bouton « Convertir » est
désactivé pendant le traitement, et un retour de succès/erreur est affiché à la
fin.

## Commandes de test

```bash
pytest tests/unit
pytest tests/integration
pytest --cov=src --cov-report=term-missing
```

## Critères de succès à vérifier

- Aucune colonne vide disproportionnée (SC-001).
- Ouverture du dossier en 1 clic (SC-002).
- 100 % de retours visuels succès/erreur (SC-003).
- Interface réactive pendant les conversions (SC-004).
