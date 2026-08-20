# Feature Specification: Conversion d'images multi-formats

**Feature Branch**: `001-image-conversion`

**Created**: 2026-08-20

**Status**: Draft

**Input**: User description: "On va creer une appli super belle mais aussi super performante de conversion image avec des tas d extension pris en compte, du batch, de l arriere plan avec notifs, des trucs que j ai pas dis mais tu vas voir et rajouter"

## User Scenarios & Testing _(mandatory)_

### User Story 1 - Conversion d'une image unique (Priority: P1)

L'utilisateur sélectionne une image, choisit un format de sortie, et obtient le
fichier converti en quelques secondes, sans configuration complexe.

**Why this priority**: C'est le cœur de la valeur du produit. Sans conversion
simple et fiable, aucune autre fonctionnalité n'a de sens.

**Independent Test**: Peut être testé en convertissant une seule image d'un
format source vers un format cible et en vérifiant que le fichier de sortie est
valide et lisible.

**Acceptance Scenarios**:

1. **Given** une image source valide, **When** l'utilisateur choisit un format
   cible et lance la conversion, **Then** un fichier converti valide est produit
   dans le format demandé.
2. **Given** une image source corrompue ou illisible, **When** la conversion est
   lancée, **Then** un message d'erreur clair et actionnable est affiché, sans
   plantage de l'application.
3. **Given** une image source, **When** l'utilisateur ne précise pas de dossier
   de sortie, **Then** le fichier est enregistré à côté de la source avec un nom
   non ambigu.

---

### User Story 2 - Conversion par lot (batch) (Priority: P1)

L'utilisateur sélectionne plusieurs images (ou un dossier entier) et les convertit
toutes en une seule opération, avec un suivi de progression.

**Why this priority**: Le traitement par lot est une raison d'usage majeure et
différenciante ; il multiplie la valeur de la conversion unitaire.

**Independent Test**: Peut être testé en sélectionnant un dossier de N images et
en vérifiant que toutes sont converties, avec un rapport de succès/échec.

**Acceptance Scenarios**:

1. **Given** un dossier contenant plusieurs images de formats variés, **When**
   l'utilisateur lance une conversion par lot, **Then** toutes les images
   convertibles sont traitées et un rapport récapitule succès et échecs.
2. **Given** un lot contenant des images invalides, **When** la conversion est
   lancée, **Then** les images valides sont converties et les échecs sont
   signalés individuellement sans interrompre le lot.
3. **Given** un lot en cours, **When** l'utilisateur consulte l'interface,
   **Then** une progression (nombre traité / total) est visible.

---

### User Story 3 - Traitement en arrière-plan avec notifications (Priority: P2)

L'utilisateur lance une conversion longue et peut continuer à utiliser
l'application ; il est notifié à la fin du traitement.

**Why this priority**: Améliore fortement l'expérience sur les gros lots, mais
n'est pas indispensable pour un premier usage fonctionnel.

**Independent Test**: Peut être testé en lançant un lot volumineux, en naviguant
dans l'application pendant le traitement, puis en vérifiant la réception d'une
notification de fin.

**Acceptance Scenarios**:

1. **Given** une conversion longue en cours, **When** l'utilisateur interagit
   avec l'application, **Then** l'interface reste réactive.
2. **Given** une conversion en arrière-plan terminée, **When** le traitement se
   termine, **Then** l'utilisateur reçoit une notification indiquant le résultat
   (succès, échecs, emplacement des fichiers).
3. **Given** une conversion en arrière-plan, **When** l'utilisateur souhaite
   l'annuler, **Then** l'annulation est possible et les fichiers partiels sont
   gérés proprement.

---

### User Story 4 - Aperçu et options de conversion (Priority: P2)

L'utilisateur visualise un aperçu de l'image et ajuste des options simples
(qualité, dimensions) avant de convertir.

**Why this priority**: Apporte de la valeur et de la confiance, mais la
conversion de base reste fonctionnelle sans ces options.

**Independent Test**: Peut être testé en ajustant la qualité ou les dimensions
d'une image et en vérifiant que le résultat reflète ces réglages.

**Acceptance Scenarios**:

1. **Given** une image sélectionnée, **When** l'utilisateur ouvre l'aperçu,
   **Then** l'image est affichée fidèlement.
2. **Given** une option de qualité ajustée, **When** la conversion est lancée,
   **Then** le fichier de sortie reflète le niveau de qualité choisi.
3. **Given** des dimensions cibles définies, **When** la conversion est lancée,
   **Then** l'image de sortie respecte ces dimensions en conservant les
   proportions.

---

### User Story 5 - Glisser-déposer et intégration système (Priority: P3)

L'utilisateur dépose des fichiers directement dans l'application et peut lancer
des conversions depuis le menu contextuel du système.

**Why this priority**: Confort d'usage appréciable, mais secondaire par rapport
aux flux principaux.

**Independent Test**: Peut être testé en glissant des fichiers dans la fenêtre
et en vérifiant qu'ils sont pris en compte.

**Acceptance Scenarios**:

1. **Given** des fichiers glissés dans la fenêtre, **When** le dépôt est effectué,
   **Then** les fichiers sont ajoutés à la file de conversion.
2. **Given** une intégration au menu contextuel, **When** l'utilisateur choisit
   « Convertir » sur un fichier, **Then** l'application s'ouvre avec ce fichier
   préchargé.

---

### Edge Cases

- Que se passe-t-il lorsqu'un fichier de sortie existe déjà (écrasement,
  renommage, ou demande de confirmation) ?
- Comment l'application gère-t-elle des images aux dimensions extrêmes ou aux
  métadonnées exotiques ?
- Que se passe-t-il si le disque est plein ou si le dossier de sortie n'est pas
  accessible en écriture ?
- Comment sont gérées les images animées (GIF, WebP animé) lors de la conversion ?
- Que se passe-t-il si l'utilisateur annule un lot en cours de traitement ?
- Comment l'application réagit-elle à des noms de fichiers avec caractères
  spéciaux ou non-ASCII ?

## Requirements _(mandatory)_

### Functional Requirements

- **FR-001**: Le système MUST convertir une image d'un format source vers un
  format cible parmi les formats pris en charge en v1 : JPEG, PNG, WebP, GIF,
  BMP, TIFF, ICO, PPM, PGM, PBM. Les formats AVIF et HEIC sont des extensions
  optionnelles (codecs supplémentaires).
- **FR-002**: Le système MUST détecter et signaler clairement les images
  corrompues ou non prises en charge sans interrompre le reste du traitement.
- **FR-003**: Le système MUST permettre la conversion par lot de plusieurs
  images (fichiers multiples ou dossier entier).
- **FR-004**: Le système MUST afficher une progression du traitement par lot
  (nombre d'éléments traités sur le total).
- **FR-005**: Le système MUST exécuter les conversions longues en arrière-plan
  sans bloquer l'interface utilisateur.
- **FR-006**: Le système MUST notifier l'utilisateur à la fin d'un traitement
  en arrière-plan (succès, échecs, emplacement des fichiers).
- **FR-007**: Le système MUST permettre l'annulation d'un traitement en cours.
- **FR-008**: Le système MUST offrir un aperçu de l'image avant conversion.
- **FR-009**: Le système MUST permettre d'ajuster la qualité et les dimensions
  de sortie.
- **FR-010**: Le système MUST gérer les collisions de noms de fichiers de
  sortie de manière prévisible (écrasement, renommage ou confirmation).
- **FR-011**: Le système MUST préserver les métadonnées pertinentes (EXIF,
  orientation) lorsque le format cible le permet.
- **FR-012**: Le système MUST fonctionner de manière identique sur Windows,
  macOS et Linux.
- **FR-013**: Le système MUST rester fluide sur du matériel peu performant
  (démarrage rapide, empreinte mémoire maîtrisée).
- **FR-014**: Le système MUST permettre le glisser-déposer de fichiers dans
  l'interface.
- **FR-015**: Le système MUST fournir un rapport récapitulatif après un
  traitement par lot (succès, échecs, raisons des échecs).
- **FR-016**: Le système MUST offrir une interface sobre et authentique avec un
  thème clair et un thème sombre, des animations fluides, des widgets
  personnalisés et des icônes dédiées.

### Key Entities

- **Image source** : fichier d'entrée, avec son format, ses dimensions, ses
  métadonnées et son emplacement.
- **Tâche de conversion** : une opération unitaire associant une image source,
  un format cible et des options (qualité, dimensions), avec un état
  (en attente, en cours, réussie, échouée, annulée).
- **Lot (batch)** : ensemble de tâches de conversion traitées ensemble, avec une
  progression globale et un rapport de résultat.
- **Options de conversion** : réglages appliqués à une tâche (format, qualité,
  dimensions, gestion des collisions).

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Un utilisateur convertit une image unique en moins de 5 secondes
  sur une machine de référence modeste.
- **SC-002**: Un lot de 100 images est traité sans dégradation perceptible de
  la réactivité de l'interface.
- **SC-003**: 95 % des conversions d'images valides aboutissent sans erreur.
- **SC-004**: L'application démarre en moins de 3 secondes sur une machine
  modeste.
- **SC-005**: 90 % des utilisateurs réussissent leur première conversion sans
  consulter d'aide.
- **SC-006**: L'application fonctionne de manière identique sur Windows, macOS
  et Linux (aucune régression spécifique à un OS).

## Assumptions

- Les utilisateurs cibles sont des particuliers et des professionnels ayant des
  besoins courants de conversion d'images, sur des machines potentiellement
  modestes.
- Les formats pris en charge couvrent les formats d'images courants du web et du
  bureau ; les formats propriétaires rares sont hors périmètre initial.
- La conversion est locale (aucun envoi de fichiers vers un service distant) ;
  la confidentialité des images est préservée.
- L'interface est une application de bureau (pas une application web) ; le
  support mobile est hors périmètre pour la v1.
- Les images animées (GIF, WebP animé) sont converties en préservant l'animation
  lorsque le format cible le permet ; sinon, seule la première image est
  conservée avec un avertissement.
- Les notifications utilisent le mécanisme natif de chaque système d'exploitation.
