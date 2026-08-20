# Research: Amélioration de l'UX

## Décisions techniques

### D1. Mise en page équilibrée : QSplitter + stretch factors

- **Decision**: Utiliser `QSplitter` (redimensionnable par l'utilisateur) et des
  `stretch` factors explicites sur les layouts pour équilibrer les panneaux,
  au lieu de colonnes à largeur fixe égale.
- **Rationale**: `QSplitter` permet à l'utilisateur d'ajuster les proportions et
  évite les colonnes vides disproportionnées. Les stretch factors donnent des
  proportions initiales raisonnables.
- **Alternatives considérées**:
  - *QHBoxLayout avec stretch=1 partout* : cause les colonnes vides actuelles.
  - *Largeurs fixes* : non adaptatif au redimensionnement.

### D2. Ouverture du dossier : QDesktopServices

- **Decision**: `QDesktopServices.openUrl(QUrl.fromLocalFile(path))` pour ouvrir
  le dossier de sortie dans le gestionnaire de fichiers natif.
- **Rationale**: API Qt portable (Explorer/Finder/gestionnaire Linux), aucune
  dépendance tierce, conforme au principe IV.
- **Alternatives considérées**:
  - *subprocess + commande OS* : non portable, contraire au principe IV.
  - *os.startfile / open / xdg-open* : spécifique à chaque OS.

### D3. Retours visuels : états de boutons + barre de progression

- **Decision**: Réutiliser la `QProgressBar` existante et ajouter des états
  visuels clairs (bouton désactivé pendant conversion, message de succès/erreur
  via `QMessageBox` et notification).
- **Rationale**: déjà partiellement en place (features 001/002) ; il s'agit de
  le rendre cohérent et visible.
- **Alternatives considérées**: refonte complète des notifications (rejeté —
  YAGNI).

## Points d'attention

- **Petits écrans** : la mise en page doit rester utilisable en fenêtre réduite
  (le `QSplitter` gère le redimensionnement).
- **Cohérence du thème** : les ajustements QSS doivent respecter les palettes
  clair/sombre existantes.
