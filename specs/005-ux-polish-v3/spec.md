# Feature Specification: Refonte de la disposition principale

**Feature Branch**: `005-ux-polish-v3`

**Created**: 2026-08-20

**Status**: Draft

**Input**: User description: "c est toujours laid"

## Contexte

Après deux itérations de polish visuel (features 003 et 004), l'utilisateur juge
l'interface toujours « laide ». L'analyse de la capture d'écran actuelle montre
que les problèmes ne résident plus dans les détails de spacing ou les tokens de
design, mais dans la **structure globale de la fenêtre** :

- La zone de dépôt occupe la moitié supérieure de la fenêtre, laissant un grand
  espace vide lorsqu'aucune image n'est sélectionnée.
- Quatre panneaux sont alignés horizontalement côte à côte (aperçu, options,
  file, historique), ce qui crée des colonnes étirées, des largeurs non
  optimales et des panneaux mal dimensionnés (historique coupé).
- La barre de boutons en bas contient six actions alignées, sans groupement
  logique ni hiérarchie d'actions.
- L'application manque d'identité visuelle : pas de header, pas de pied de
  page, pas de typographie marquante sur l'action principale.

Cette feature vise à résoudre ces problèmes structurants par une **refonte de la
disposition principale** et une **hiérarchie visuelle claire**.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Layout global aéré et structuré (Priority: P1)

L'utilisateur ouvre l'application et voit une interface structurée avec un
en-tête, une zone de travail claire, et une barre d'actions organisée, sans
grands espaces vides inutiles.

**Why this priority**: C'est le principal reproche de l'utilisateur. La
structure actuelle avec drop zone géante et quatre colonnes côte à côte est
ressentie comme « laide » indépendamment des détails de spacing.

**Independent Test**: Peut être testé en ouvrant l'application et en vérifiant
que la fenêtre présente une structure verticale cohérente sans zone vide
excessive.

**Acceptance Scenarios**:

1. **Given** l'application ouverte sans image sélectionnée, **When**
   l'utilisateur regarde la fenêtre, **Then** la zone centrale n'est pas
   dominée par un grand espace vide.
2. **Given** la fenêtre redimensionnée verticalement ou horizontalement,
   **When** les dimensions changent, **Then** les zones principales se
   redimensionnent de manière cohérente et conservent leur hiérarchie.

---

### User Story 2 - Panneaux logiquement regroupés (Priority: P1)

L'utilisateur distingue clairement les trois espaces fonctionnels : la zone de
dépôt/aperçu, les options de conversion, et la file d'attente avec l'historique.
Les panneaux ne sont plus quatre colonnes étirées côte à côte.

**Why this priority**: L'alignement horizontal de quatre panneaux crée des
proportions disgracieuses et un historique coupé. Un regroupement logique
améliore la lisibilité et l'utilisabilité.

**Independent Test**: Peut être testé en vérifiant que la file d'attente et
l'historique occupent un emplacement commun ou adjacent, et que les options ne
sont pas étirées en largeur.

**Acceptance Scenarios**:

1. **Given** l'interface affichée, **When** l'utilisateur regarde la zone
   centrale, **Then** les options de conversion ont une largeur fixe ou
   contrainte adaptée à leur contenu.
2. **Given** la file d'attente et l'historique, **When** l'utilisateur les
   consulte, **Then** ils apparaissent dans une zone commune avec suffisamment
   de largeur pour lire les chemins complets.
3. **Given** un écran étroit, **When** l'utilisateur réduit la fenêtre,
   **Then** l'interface passe à une disposition adaptée sans tronquer le
   contenu essentiel.

---

### User Story 3 - Barre d'actions hiérarchisée (Priority: P1)

L'utilisateur identifie immédiatement l'action principale (convertir) et trouve
les actions secondaires (ajouter, annuler, thème, dossier, historique) regroupées
logiquement sans encombrer la barre du bas.

**Why this priority**: La barre actuelle avec six boutons alignés est visuellement
chargée et ne met pas en valeur l'action principale.

**Independent Test**: Peut être testé en vérifiant que le bouton de conversion
est visuellement dominant et que les actions secondaires sont regroupées.

**Acceptance Scenarios**:

1. **Given** l'interface affichée, **When** l'utilisateur regarde la barre
   d'actions, **Then** le bouton de conversion se distingue des autres
   boutons (taille, couleur ou position).
2. **Given** les actions secondaires, **When** l'utilisateur les regarde,
   **Then** elles sont regroupées par fonction (fichier, conversion,
   affichage) ou séparées visuellement.

---

### User Story 4 - Identité visuelle et états vides explicites (Priority: P2)

L'application affiche un en-tête ou un titre identifiable, et les zones vides
(drop zone sans image, historique vide, file vide) présentent un message
explicite avec une icône ou une illustration légère, plutôt qu'un rectangle vide.

**Why this priority**: Améliore la perception de qualité et l'orientation de
l'utilisateur, sans être bloquant pour l'expérience principale.

**Independent Test**: Peut être testé en vérifiant que la zone de dépôt vide et
les listes vides affichent un message d'invitation clair.

**Acceptance Scenarios**:

1. **Given** aucune image dans la file, **When** l'utilisateur regarde la zone
   de dépôt, **Then** un message et/ou une icône invitent à glisser-déposer ou
   à cliquer sur « Ajouter des images ».
2. **Given** l'historique vide, **When** l'utilisateur regarde le panneau
   d'historique, **Then** un message indique qu'aucune conversion n'a encore
   été effectuée.
3. **Given** l'application ouverte, **When** l'utilisateur regarde l'en-tête,
   **Then** le nom de l'application et/ou un logo/icône sont visibles.

---

### User Story 5 - Compatibilité thème clair/sombre maintenue (Priority: P2)

La nouvelle disposition reste lisible et esthétique aussi bien en thème clair
qu'en thème sombre, sans éléments invisibles ou contrastes insuffisants.

**Why this priority**: Le redesign ne doit pas régresser le support des deux
thèmes déjà en place.

**Independent Test**: Peut être testé en basculant entre le thème clair et le
thème sombre et en vérifiant que tous les éléments restent lisibles.

**Acceptance Scenarios**:

1. **Given** le thème sombre actif, **When** l'utilisateur active le thème
   clair, **Then** les nouveaux éléments visuels (en-tête, états vides,
   séparateurs) adoptent les couleurs claires.
2. **Given** le thème clair actif, **When** l'utilisateur active le thème
   sombre, **Then** aucun texte ou icône ne devient illisible.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: L'interface MUST présenter une structure verticale claire
  (en-tête / corps / barre d'actions) au lieu de l'agencement actuel en quatre
  colonnes horizontales.
- **FR-002**: La zone de dépôt MUST être compactée ou intégrée à la zone
  centrale afin d'éviter un grand espace vide lorsqu'aucune image n'est
  sélectionnée.
- **FR-003**: Le panneau d'options de conversion MUST avoir une largeur fixe
  ou bornée adaptée à son contenu textuel, sans s'étirer inutilement.
- **FR-004**: La file d'attente et l'historique MUST être regroupés dans une
  zone commune via des onglets (`QTabWidget`) avec une largeur minimale de
  280 px permettant la lecture des chemins complets.
- **FR-005**: Le bouton de conversion MUST être visuellement dominant dans la
  barre d'actions (par taille, couleur ou position).
- **FR-006**: Les actions secondaires (ajouter, annuler, thème, dossier de
  sortie, ouvrir le dossier) SHOULD être regroupées ou séparées visuellement
  selon leur fonction (fichier / conversion / affichage).
- **FR-007**: Les états vides (zone de dépôt, file, historique) MUST afficher
  un message explicite et/ou une icône invitant l'utilisateur.
- **FR-008**: L'application MUST afficher un en-tête avec le nom et/ou une
  icône identifiable.
- **FR-009**: La nouvelle disposition MUST rester entièrement fonctionnelle en
  thème clair et en thème sombre.
- **FR-010**: La fenêtre MUST rester redimensionnable et utilisable sur des
  résolutions modestes (largeur minimale de 800 px, hauteur minimale de 500 px).

### Non-Functional Requirements

- **NFR-001**: Le temps de démarrage de la fenêtre principale ne doit pas
  augmenter de plus de 10 % par rapport à la version précédente.
- **NFR-002**: L'interface doit rester fluide lors du redimensionnement (pas de
  freezes perceptibles sur du matériel modeste).

## Success Criteria

- **SC-001**: L'application ouverte sans image présente moins de 25 % de
  l'aire centrale comme espace vide non utilisé. La mesure se fait par
  inspection visuelle ou script de capture d'écran comparant la zone de
  dépôt compacte à l'aire centrale totale.
- **SC-002**: Le panneau d'options a une largeur comprise entre 220 et 320 px
  par défaut, et ne dépasse pas 360 px lors du redimensionnement horizontal.
- **SC-003**: La file d'attente et l'historique affichent les chemins complets
  des fichiers sans troncature systématique sur une fenêtre de 1280 px de
  large.
- **SC-004**: Le bouton de conversion est identifiable comme action principale
  grâce à un style visuel distinctif (couleur primaire, texte en gras, taille
  supérieure ou position isolée) vérifié automatiquement par un test de
  contrat d'interface.
- **SC-005**: Les thèmes clair et sombre passent tous deux un contrôle visuel
  de lisibilité (textes, icônes, états vides).
- **SC-006**: Aucune régression fonctionnelle : conversion par lot,
  sélection de dossier de sortie, historique, notification, et annulation
  restent opérationnels.

## Key Entities *(optional)*

- **MainWindow** : fenêtre principale dont la disposition est refondue.
- **DropZone** : zone de dépôt à intégrer plus compactement.
- **OptionsPanel** : panneau d'options à largeur contrainte.
- **BatchPanel / HistoryPanel** : panneaux de file et d'historique à regrouper.
- **Theme tokens** : couleurs, espacements et tailles déjà centralisés dans
  `tokens.py`, à enrichir si nécessaire pour le nouvel agencement.

## Assumptions

- Les widgets existants (`DropZone`, `OptionsPanel`, `BatchPanel`,
  `HistoryPanel`, `PreviewPane`) peuvent être réorganisés sans réécriture
  complète de leur logique interne.
- Le framework de widgets reste PySide6 ; aucune bibliothèque de composants
  externe n'est requise.
- L'identité visuelle peut rester textuelle (nom + icône existante) sans
  création d'un logo dédié.
- La barre d'actions reste dans la fenêtre principale ; l'intégration dans la
  barre de titre native du système (titlebar personnalisée) est hors scope.

## Dependencies

- Dépend de la disponibilité des tokens de design (`tokens.py`) et du système
  de thème (`theme.py`) mis en place dans la feature 004.
- Les tests existants sur `main_window.py` devront être mis à jour pour
  refléter la nouvelle structure de widgets.

## Notes

- Cette feature ne doit pas ajouter de nouvelles fonctionnalités métier
  (formats, options de conversion, etc.) : c'est uniquement un redesign UX.
- Les captures d'écran actuelles et futures doivent être utilisées pour
  valider visuellement les itérations.
