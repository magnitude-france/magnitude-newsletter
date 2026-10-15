# Prototype — La Pioche (« Find your Candidate »)

Prototype interne du repositionnement de Magnitude en jeu de cartes à
collectionner (comité de direction n°1, 2026-10-14). Nom retenu le
2026-10-15 : **La Pioche**, avec « Find your Candidate » en accroche. **Non déployé** : ce
dossier est hors de `src/`, le workflow GitHub Pages ne le publie pas.

## Ce que fait le prototype
- Swipe dans 4 directions : → Aligné, ← Désaligné, ↑ J'aimerais, ↓ M'en fous
  (souris, doigt, flèches du clavier ou boutons).
- Swipe « à l'aveugle » : le candidat est révélé après le geste, avec les
  positions documentées des autres candidats.
- Badge de décision sur chaque carte, décisions modifiables (« Mon deck »).
- **Fiche « Comprendre la mesure »** (toucher la carte ou bouton « Comprendre ») :
  l'essentiel, le chiffre clé, la comparaison avec les voisins européens et les
  sources institutionnelles, **sans nom ni position de candidat** (lue avant le
  choix). Extraite des analyses de `magnitude-analysis` par `extract_fiches.py`,
  qui retire toute phrase nommant un candidat ou un parti et échoue s'il en reste.
- Score par candidat = accords / positions documentées (cartes Aligné ou
  Désaligné uniquement), seuil de 4 cartes, égalités affichées, classement
  des 12 toujours visible.
- Couleur de deck qui bascule en direct quand le candidat de tête change ;
  « Le Grand Tri » après les 6 cartes de la semaine.
- Onglets Deck · Recherche (bureau des enquêtes) · La Maison Magnitude
  (maison de parfum, Puits aux souhaits).
- Tout est stocké dans le navigateur (`localStorage`) ; aucune requête
  réseau ; export / import du deck par copier-coller.

## Limites connues (voir le vault, `07-Recherches/INV-03-faisabilite-scoring`)
- La matrice des positions n'est couverte qu'à 42 % : le score est biaisé
  mécaniquement et **ne doit pas être publié** en l'état.
- Teintes de maison provisoires (tirage déterministe contraint, graine
  `magnitude-2027`) — règle des couleurs à trancher en comité.
- Illustrations des cartes = pictogrammes génériques + constellation
  générée ; les illustrations dessinées viendront ensuite.

## Reconstruire
```bash
python3 prototypes/deck/extract_fiches.py ../magnitude-analysis   # fiches anonymes
python3 prototypes/deck/build_deck.py
```
Entrées : `deck-data.json` (extrait de `magnitude-analysis/data/analyses/*.json`
et des pages de numéro publiées), `src/candidats/*.png`, `deck-template.html`.
Sortie : `deck.html` (fichier unique, autonome).
