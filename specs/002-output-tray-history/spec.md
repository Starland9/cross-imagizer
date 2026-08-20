# Feature Specification: Dossier de sortie, barre de tâche & historique

**Feature Branch**: `002-output-tray-history`

**Created**: 2026-08-20

**Status**: Draft

**Input**: User description: "Sélection de dossier de sortie, icône avec menu contextuel en barre de tâche (system tray), historique des conversions"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Sélection du dossier de sortie (Priority: P1)

L'utilisateur choisit un dossier de destination pour ses conversions, au lieu
d'écrire systématiquement à côté des fichiers sources.

**Why this priority**: C'est le besoin le plus immédiat et le plus fréquent ;
sans lui, l'utilisateur ne contrôle pas où vont ses fichiers.

**Independent Test**: Peut être testé en choisissant un dossier de sortie, en
convertissant une image, et en vérifiant que le fichier est créé dans ce dossier.

**Acceptance Scenarios**:

1. **Given** un dossier de sortie sélectionné, **When** l'utilisateur convertit
   une image, **Then** le fichier converti est créé dans ce dossier.
2. **Given** aucun dossier de sortie sélectionné, **When** l'utilisateur
   convertit, **Then** le fichier est créé à côté de la source (comportement
   actuel).
3. **Given** un dossier de sortie choisi puis supprimé, **When** la conversion
   est lancée, **Then** un message d'erreur clair est affiché.

---

### User Story 2 - Icône de barre de tâche (system tray) (Priority: P2)

L'application reste accessible via une icône dans la barre de tâche, avec un
menu contextuel, même lorsque la fenêtre principale est fermée.

**Why this priority**: Améliore l'ergonomie pour les conversions en arrière-plan,
mais n'est pas indispensable au fonctionnement de base.

**Independent Test**: Peut être testé en fermant la fenêtre principale et en
vérifiant que l'icône de barre de tâche reste active avec son menu.

**Acceptance Scenarios**:

1. **Given** l'application lancée, **When** l'utilisateur ferme la fenêtre
   principale, **Then** l'application reste accessible via l'icône de barre de
   tâche.
2. **Given** l'icône de barre de tâche, **When** l'utilisateur ouvre son menu
   contextuel, **Then** il peut rouvrir la fenêtre, lancer une conversion ou
   quitter l'application.
3. **Given** une conversion en arrière-plan, **When** l'utilisateur quitte via
   le menu de la barre de tâche, **Then** l'application se ferme proprement.

---

### User Story 3 - Historique des conversions (Priority: P2)

L'utilisateur consulte la liste des conversions passées (fichier source, fichier
de sortie, statut, date).

**Why this priority**: Apporte de la valeur et de la traçabilité, mais n'est pas
requis pour convertir.

**Independent Test**: Peut être testé en effectuant des conversions puis en
vérifiant qu'elles apparaissent dans l'historique.

**Acceptance Scenarios**:

1. **Given** des conversions effectuées, **When** l'utilisateur ouvre
   l'historique, **Then** chaque conversion apparaît avec source, sortie, statut
   et date.
2. **Given** une conversion échouée, **When** l'utilisateur consulte
   l'historique, **Then** l'échec est signalé avec sa raison.
3. **Given** l'historique, **When** l'utilisateur relance l'application,
   **Then** l'historique est conservé entre les sessions.

---

### Edge Cases

- Que se passe-t-il si le dossier de sortie n'est pas accessible en écriture ?
- Comment l'historique est-il limité (nombre d'entrées, purge) ?
- Que se passe-t-il si l'icône de barre de tâche n'est pas supportée par l'OS ?
- Comment gérer les conversions lancées depuis le menu de la barre de tâche
  sans fenêtre ouverte ?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Le système MUST permettre à l'utilisateur de sélectionner un
  dossier de sortie pour les conversions.
- **FR-002**: Le système MUST utiliser le dossier de sortie sélectionné pour
  écrire les fichiers convertis.
- **FR-003**: Le système MUST afficher une erreur claire si le dossier de sortie
  est inaccessible en écriture.
- **FR-004**: Le système MUST fournir une icône de barre de tâche (system tray)
  avec un menu contextuel (ouvrir, convertir, quitter).
- **FR-005**: Le système MUST rester accessible via la barre de tâche lorsque la
  fenêtre principale est fermée.
- **FR-006**: Le système MUST enregistrer chaque conversion (source, sortie,
  statut, date) dans un historique.
- **FR-007**: Le système MUST conserver l'historique entre les sessions.
- **FR-008**: Le système MUST permettre de consulter l'historique des conversions.
- **FR-009**: Le système MUST limiter la taille de l'historique (purge des
  entrées les plus anciennes).
- **FR-010**: Le système MUST fonctionner de manière identique sur Windows,
  macOS et Linux.

### Key Entities

- **Dossier de sortie** : chemin de destination choisi par l'utilisateur,
  persisté entre les sessions.
- **Entrée d'historique** : enregistrement d'une conversion (source, sortie,
  statut, date, raison d'échec éventuelle).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Un utilisateur sélectionne un dossier de sortie et convertit une
  image en moins de 10 secondes (sélection + conversion).
- **SC-002**: L'icône de barre de tâche reste fonctionnelle après fermeture de
  la fenêtre sur les trois OS.
- **SC-003**: 100 % des conversions réussies apparaissent dans l'historique.
- **SC-004**: L'historique est conservé après redémarrage de l'application.

## Assumptions

- L'historique est stocké localement (fichier de préférences ou base légère),
  sans service distant.
- Le dossier de sortie et l'historique sont persistés via le mécanisme de
  préférences natif (QSettings).
- L'icône de barre de tâche utilise `QSystemTrayIcon` (Qt), avec dégradation
  silencieuse si non supportée.
- La taille maximale de l'historique est fixée à une valeur raisonnable
  (ex. 500 entrées) avec purge des plus anciennes.
