# Quickstart: Dossier de sortie, barre de tâche & historique

Guide de validation de bout en bout. Les détails d'implémentation sont dans
`tasks.md`.

## Prérequis

- Application Cross-Imagizer (feature 001) installée et fonctionnelle.
- Environnement virtuel activé.

## Scénarios de validation

### 1. Sélection du dossier de sortie (US1)

1. Lancer l'application.
2. Choisir un dossier de sortie via l'interface.
3. Convertir une image.

**Résultat attendu**: le fichier converti est créé dans le dossier choisi ; le
choix est conservé après redémarrage.

### 2. Icône de barre de tâche (US2)

1. Lancer l'application.
2. Fermer la fenêtre principale.

**Résultat attendu**: l'icône de barre de tâche reste active ; son menu permet
d'ouvrir, convertir et quitter.

### 3. Historique des conversions (US3)

1. Effectuer plusieurs conversions (dont une échouée).
2. Ouvrir l'historique.

**Résultat attendu**: chaque conversion apparaît (source, sortie, statut, date) ;
l'échec est signalé avec sa raison ; l'historique persiste après redémarrage.

## Commandes de test

```bash
pytest tests/unit
pytest tests/integration
pytest --cov=src --cov-report=term-missing
```

## Critères de succès à vérifier

- Sélection + conversion < 10 s (SC-001).
- Tray fonctionnel après fermeture sur les 3 OS (SC-002).
- 100 % des conversions réussies dans l'historique (SC-003).
- Historique conservé après redémarrage (SC-004).
