# Feature Specification: Polish UX avancé

**Feature Branch**: `004-ux-polish-v2`

**Created**: 2026-08-20

**Status**: Draft

**Input**: User description: "le polish a toujours de gros trucs — fait mieux"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Tailles et proportions des widgets (Priority: P1)

L'utilisateur voit des widgets correctement dimensionnés : les panneaux ne
sont ni trop larges ni trop étroits, les boutons ont une taille cohérente, et
les zones de saisie sont confortables.

**Why this priority**: Les « gros trucs » visuels actuels (panneaux
disproportionnés, boutons surdimensionnés) nuisent à l'expérience et sont le
cœur de la demande.

**Independent Test**: Peut être testé en ouvrant l'application et en vérifiant
que les tailles des widgets sont cohérentes et proportionnées.

**Acceptance Scenarios**:

1. **Given** l'application ouverte, **When** l'utilisateur observe les panneaux,
   **Then** chaque panneau a une largeur minimale et maximale raisonnable, sans
   débordement disproportionné.
2. **Given** la fenêtre redimensionnée, **When** l'utilisateur l'agrandit ou la
   rétrécit, **Then** les widgets conservent des proportions cohérentes.

---

### User Story 2 - Espacements et marges cohérents (Priority: P1)

L'utilisateur perçoit une interface aérée et équilibrée, avec des espacements
cohérents entre les éléments (pas trop serré, pas trop espacé).

**Why this priority**: Les espacements incohérents contribuent aux « gros
trucs » disgracieux.

**Independent Test**: Peut être testé en vérifiant que les marges et
espacements sont uniformes dans toute l'interface.

**Acceptance Scenarios**:

1. **Given** l'interface affichée, **When** l'utilisateur observe les
   espacements, **Then** les marges entre les widgets sont uniformes et
   raisonnables.
2. **Given** les boutons alignés, **When** l'utilisateur les regarde, **Then**
   l'espacement entre les boutons est cohérent.

---

### User Story 3 - Typographie et hiérarchie visuelle (Priority: P2)

L'utilisateur distingue clairement les titres, les labels et les contenus grâce
à une typographie hiérarchisée et lisible.

**Why this priority**: Améliore la lisibilité et la perception de qualité, mais
secondaire par rapport aux tailles et espacements.

**Independent Test**: Peut être testé en vérifiant que les titres sont visuellement
distincts des labels.

**Acceptance Scenarios**:

1. **Given** l'interface affichée, **When** l'utilisateur lit les titres et
   labels, **Then** les titres sont visuellement plus marqués que les labels.
2. **Given** les panneaux, **When** l'utilisateur les parcourt, **Then** chaque
   panneau a un titre clairement identifiable.

---

### User Story 4 - États visuels des widgets (Priority: P2)

Les boutons et éléments interactifs affichent des états visuels clairs
(normal, survol, pressé, désactivé) cohérents entre eux.

**Why this priority**: Améliore la perception de réactivité et de qualité.

**Independent Test**: Peut être testé en survolant et en pressant les boutons
et en vérifiant les changements visuels.

**Acceptance Scenarios**:

1. **Given** un bouton, **When** l'utilisateur le survole, **Then** un état de
   survol est visible.
2. **Given** un bouton désactivé, **When** l'utilisateur le regarde, **Then**
   il est visuellement distinct d'un bouton actif.
3. **Given** un bouton pressé, **When** l'utilisateur clique dessus, **Then**
   un état pressé est visible.

---

### User Story 5 - Réalignement des widgets (Priority: P1)

L'utilisateur voit une interface où les widgets sont proprement alignés :
alignement vertical des champs et boutons, alignement des labels, et
cohérence de l'orientation (gauche/droite/centré) au sein de chaque groupe
d'éléments.

**Why this priority**: Le mauvais alignement des widgets est l'un des « gros
trucs » visuels les plus flagrants ; il nuit immédiatement à la perception de
qualité.

**Independent Test**: Peut être testé en ouvrant l'application et en vérifiant
que les champs, labels et boutons d'un même groupe sont alignés sur un même
axe.

**Acceptance Scenarios**:

1. **Given** un formulaire ou une rangée de boutons, **When** l'utilisateur
   les observe, **Then** les éléments sont alignés sur un même axe (haut,
   gauche ou centré selon le groupe).
2. **Given** des labels et champs associés, **When** l'utilisateur les parcourt,
   **Then** les labels sont alignés entre eux et les champs sont alignés entre
   eux.
3. **Given** la fenêtre redimensionnée, **When** l'utilisateur l'agrandit ou la
   rétrécit, **Then** l'alignement des widgets reste cohérent.

---

### Edge Cases

- Comment l'interface se comporte-t-elle sur un très petit écran ?
- Les états visuels restent-ils cohérents en thème sombre ?
- Les tailles minimales empêchent-elles les widgets de devenir inutilisables ?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Le système MUST définir des tailles minimales et maximales pour
  chaque panneau afin d'éviter les disproportions.
- **FR-002**: Le système MUST appliquer des espacements (marges) uniformes et
  cohérents entre tous les widgets.
- **FR-003**: Le système MUST hiérarchiser la typographie (titres, labels,
  contenus) de manière visuellement distincte.
- **FR-004**: Le système MUST afficher des états visuels cohérents pour les
  éléments interactifs (normal, survol, pressé, désactivé).
- **FR-005**: Le système MUST conserver la cohérence visuelle en thème clair
  et sombre.
- **FR-006**: Le système MUST rester fluide et réactif sur du matériel modeste.
- **FR-007**: Le système MUST aligner les widgets d'un même groupe sur un même
  axe (vertical ou horizontal) de manière cohérente.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Aucun panneau ne dépasse 40 % de la largeur de la fenêtre sans
  justification.
- **SC-002**: Les marges entre widgets sont uniformes (écart ≤ 2 px).
- **SC-003**: 100 % des éléments interactifs affichent au moins 3 états
  visuels (normal, survol, désactivé).
- **SC-004**: L'interface reste réactive (aucun gel perceptible) pendant les
  interactions.
- **SC-005**: 100 % des groupes de widgets présentent un alignement cohérent
  sur un même axe.

## Assumptions

- L'amélioration porte sur l'application de bureau existante (features 001 à
  003), sans ajout de nouvelle fonctionnalité métier.
- Le style reste sobre et authentique, cohérent avec le thème clair/sombre
  existant (QSS).
- Les tailles et espacements sont définis centralisée dans le thème QSS pour
  faciliter la maintenance.