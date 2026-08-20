# Feature Specification: Amélioration de l'UX

**Feature Branch**: `003-ux-polish`

**Created**: 2026-08-20

**Status**: Draft

**Input**: User description: "l'UX est moche, juste des larges colonnes affreuses, pas de bouton pour ouvrir le dossier de sortie — améliore l'UX avec des trucs"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Interface visuellement soignée et compacte (Priority: P1)

L'utilisateur voit une interface agréable, équilibrée et non encombrée, au lieu
de larges colonnes vides et disgracieuses.

**Why this priority**: C'est le cœur de la demande ; l'apparence actuelle nuit à
l'expérience globale.

**Independent Test**: Peut être testé en ouvrant l'application et en vérifiant
que la mise en page est équilibrée, sans colonnes vides disproportionnées.

**Acceptance Scenarios**:

1. **Given** l'application ouverte, **When** l'utilisateur regarde la fenêtre,
   **Then** les panneaux sont proportionnés et aucun espace vide disgracieux
   n'est visible.
2. **Given** une fenêtre redimensionnée, **When** l'utilisateur l'agrandit ou la
   rétrécit, **Then** la mise en page s'adapte proprement sans colonnes étirées.

---

### User Story 2 - Ouvrir le dossier de sortie (Priority: P1)

L'utilisateur peut ouvrir directement le dossier de sortie depuis l'application
après une conversion.

**Why this priority**: Demande explicite ; améliore fortement le flux de travail
post-conversion.

**Independent Test**: Peut être testé en convertissant une image puis en
cliquant sur « Ouvrir le dossier » et en vérifiant que le dossier s'ouvre.

**Acceptance Scenarios**:

1. **Given** une conversion terminée, **When** l'utilisateur clique sur
   « Ouvrir le dossier de sortie », **Then** le dossier contenant les fichiers
   convertis s'ouvre dans le gestionnaire de fichiers du système.
2. **Given** aucun dossier de sortie défini, **When** l'utilisateur tente
   d'ouvrir le dossier, **Then** le dossier par défaut (à côté de la source) est
   ouvert, ou un message clair est affiché.

---

### User Story 3 - Retours visuels et ergonomie (Priority: P2)

L'utilisateur reçoit des retours visuels clairs (états, progression, succès) et
l'interface est plus intuitive.

**Why this priority**: Améliore la perception de qualité et la confiance, mais
secondaire par rapport aux deux premiers points.

**Independent Test**: Peut être testé en effectuant une conversion et en
vérifiant les retours visuels (progression, succès, erreurs).

**Acceptance Scenarios**:

1. **Given** une conversion en cours, **When** l'utilisateur observe
   l'interface, **Then** la progression est clairement visible.
2. **Given** une conversion réussie, **When** elle se termine, **Then** un
   retour visuel de succès est affiché.
3. **Given** une erreur, **When** elle survient, **Then** un retour visuel
   d'erreur clair est affiché.

---

### Edge Cases

- Que se passe-t-il si le dossier de sortie a été supprimé entre-temps ?
- Comment l'interface se comporte-t-elle sur un petit écran ?
- Que se passe-t-il si le gestionnaire de fichiers ne peut pas être ouvert ?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Le système MUST présenter une mise en page équilibrée, sans
  colonnes vides disproportionnées.
- **FR-002**: Le système MUST adapter la mise en page au redimensionnement de la
  fenêtre.
- **FR-003**: Le système MUST fournir un bouton « Ouvrir le dossier de sortie »
  après une conversion.
- **FR-004**: Le système MUST ouvrir le dossier de sortie dans le gestionnaire
  de fichiers du système.
- **FR-005**: Le système MUST afficher des retours visuels clairs (progression,
  succès, erreur).
- **FR-006**: Le système MUST rester fluide et réactif sur du matériel modeste.

### Key Entities

- **Dossier de sortie** : chemin de destination (réutilisé de la feature 002).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: L'interface ne présente aucune colonne vide disproportionnée à
  l'ouverture.
- **SC-002**: L'utilisateur ouvre le dossier de sortie en un seul clic après
  conversion.
- **SC-003**: 100 % des conversions affichent un retour visuel de succès ou
  d'erreur.
- **SC-004**: L'interface reste réactive (aucun gel perceptible) pendant les
  conversions.

## Assumptions

- L'amélioration porte sur l'application de bureau existante (features 001 et
  002), sans ajout de nouvelle fonctionnalité métier.
- L'ouverture du dossier utilise le mécanisme natif de chaque OS (explorateur,
  Finder, gestionnaire de fichiers).
- Le style visuel reste sobre et authentique, cohérent avec le thème clair/sombre
  existant.
