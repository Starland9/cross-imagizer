# Quickstart: Polish UX avancé

Guide de validation de bout en bout. Les détails d'implémentation sont dans
`tasks.md`.

## Prérequis

- Application Cross-Imagizer (features 001 à 003) installée et fonctionnelle.

## Scénarios de validation

### 1. Tailles et proportions (US1)

1. Lancer l'application.
2. Redimensionner la fenêtre.

**Résultat attendu**: les panneaux conservent des proportions cohérentes, aucun
panneau disproportionné.

### 2. Espacements (US2)

1. Observer l'interface.

**Résultat attendu**: les marges entre widgets sont uniformes, l'interface est
aérée sans être trop espacée.

### 3. Typographie (US3)

1. Lire les titres et labels.

**Résultat attendu**: les titres sont visuellement distincts des labels et
contenus.

### 4. États visuels (US4)

1. Survoler, presser et désactiver des boutons.

**Résultat attendu**: chaque état est visuellement distinct et cohérent en
thème clair comme sombre.

### 5. Réalignement des widgets (US5)

1. Observer les formulaires et rangées de boutons.

**Résultat attendu**: les labels sont alignés entre eux, les champs entre eux,
et les boutons d'un même groupe sont alignés sur un même axe ; l'alignement
reste cohérent au redimensionnement.

## Commandes de test

```bash
pytest tests/unit
pytest tests/integration
pytest --cov=src --cov-report=term-missing
```

## Critères de succès à vérifier

- Aucun panneau > 40 % de la largeur (SC-001).
- Marges uniformes écart ≤ 2 px (SC-002).
- 100 % des éléments interactifs avec ≥ 3 états (SC-003).
- Interface réactive (SC-004).
- 100 % des groupes de widgets alignés sur un même axe (SC-005).