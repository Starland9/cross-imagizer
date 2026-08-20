<!--
Sync Impact Report
==================
Version change: (none) → 1.0.0
Rationale: Initial constitution adoption (MAJOR — first governance baseline).

Modified principles: none (initial creation)
Added sections:
  - Core Principles (5 principes)
  - Contraintes techniques & plateformes
  - Workflow de développement & qualité
  - Governance
Removed sections: none

Follow-up TODOs: none
-->

# Cross-Imagizer Constitution

## Core Principles

### I. Code ultra clean (NON-NÉGOCIABLE)

Le code est la première interface du projet. Chaque contribution MUST respecter :

- Lisibilité avant tout : noms explicites, fonctions courtes et à responsabilité
  unique, pas de magie implicite.
- Typage statique systématique (annotations de types + `mypy`/`pyright` en CI).
- Formatage et lint automatisés (`ruff`/`black`) appliqués sans exception.
- Documentation des modules, fonctions publiques et décisions non triviales.
- Aucun code mort, aucun commentaire redondant, aucune duplication non justifiée.

Rationale : un code propre est la condition de la maintenabilité, de la revue
efficace et de la vélocité à long terme.

### II. Tests (NON-NÉGOCIABLE)

La qualité est prouvée, pas supposée.

- TDD obligatoire pour toute nouvelle fonctionnalité : test écrit → échec constaté
  → implémentation → vert.
- Couverture minimale cible de 80 % sur le code métier ; les chemins critiques
  MUST être couverts à 100 %.
- Tests unitaires rapides et isolés ; tests d'intégration pour les contrats entre
  modules et les interactions avec le système de fichiers/OS.
- Aucune fusion (merge) sans suite de tests verte en CI.

Rationale : les tests sont le filet de sécurité qui autorise le refactoring et
garantit la stabilité cross-platform.

### III. Performance sur appareils modestes

Le logiciel MUST rester fluide sur du matériel peu performant.

- Budget de ressources explicite : démarrage rapide, empreinte mémoire maîtrisée,
  aucune dépendance lourde non justifiée.
- Les opérations coûteuses (I/O, traitement d'images) MUST être paresseuses,
  incrémentales ou asynchrones quand c'est pertinent.
- Benchmark de référence sur une machine « bas de gamme » de référence ; toute
  régression de performance significative bloque la fusion.
- Éviter le sur-ingénierie : ne pas optimiser prématurément, mais ne jamais
  accepter une complexité algorithmique évitable.

Rationale : la cible inclut des utilisateurs sur machines modestes ; la
performance est une exigence fonctionnelle, pas un luxe.

### IV. Compatibilité cross-platform (Windows, macOS, Linux)

Le projet MUST fonctionner de manière identique sur les trois OS cibles.

- Aucune dépendance spécifique à un OS dans le code métier ; les différences
  (chemins, encodages, permissions) MUST être isolées dans une couche
  d'abstraction dédiée.
- Utiliser `pathlib` et les API standard Python pour la portabilité.
- CI MUST exécuter la suite de tests sur les trois plateformes (matrice
  Windows/macOS/Linux).
- Toute fonctionnalité nouvelle MUST être validée sur les trois OS avant fusion.

Rationale : la portabilité est la raison d'être du projet ; une régression
spécifique à un OS est un défaut bloquant.

### V. Simplicité & YAGNI

Commencer simple, ajouter seulement ce qui est nécessaire.

- Pas de fonctionnalité spéculative ; chaque ajout MUST répondre à un besoin
  réel et documenté.
- Préférer la bibliothèque standard aux dépendances tierces quand elle suffit.
- Toute complexité introduite MUST être justifiée dans la revue de code.
- Une abstraction n'est introduite que lorsqu'au moins deux cas d'usage réels
  la rendent nécessaire.

Rationale : la simplicité réduit les bugs, facilite la revue et préserve la
performance sur matériel modeste.

## Contraintes techniques & plateformes

- **Langage** : Python 3.11+ (compatible avec les versions stables des trois OS).
- **Gestion des dépendances** : `pyproject.toml` unique, dépendances épinglées,
  environnement reproductible (lockfile).
- **Packaging** : distribution installable (`pip`/`pipx`) ; binaires autonomes
  envisagés uniquement si le besoin est avéré.
- **Encodage & chemins** : UTF-8 partout, `pathlib.Path` exclusivement, aucune
  hypothèse sur le séparateur de chemin ou la casse du système de fichiers.
- **Sécurité** : aucune exécution de code non fiable, validation des entrées,
  gestion explicite des permissions et des secrets (jamais commités).

## Workflow de développement & qualité

- **Revue de code** : toute fusion MUST passer par une revue vérifiant la
  conformité aux principes ci-dessus.
- **Qualité en CI** : lint, typage, tests et benchmark MUST être verts avant
  fusion.
- **Versionnement** : `MAJOR.MINOR.PATCH` (SemVer) ; les changements cassants
  MUST être documentés et versionnés en MAJOR.
- **Observabilité** : journalisation structurée et messages d'erreur clairs ;
  les erreurs MUST être explicites et actionnables.

## Governance

La présente constitution prime sur toute autre pratique ou convention du projet.

- Toute modification MUST être documentée, justifiée et suivie d'un plan de
  migration si elle impacte du code existant.
- Les amendements suivent le versionnement sémantique décrit ci-dessus.
- La conformité MUST être vérifiée lors de chaque revue de code et de chaque
  fusion.
- Toute dérogation à un principe NON-NÉGOCIABLE est interdite sans amendement
  préalable de la constitution.

**Version**: 1.0.0 | **Ratified**: 2026-08-20 | **Last Amended**: 2026-08-20
