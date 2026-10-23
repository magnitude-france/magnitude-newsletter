# Deck Magnitude (« Find your Candidate »)

Jeu de cartes à collectionner de Magnitude (comité de direction n°1,
2026-10-14). Nom retenu le 2026-10-15 : **Magnitude**, avec « Find your
Candidate » en accroche. **Déployé** : depuis le 2026-10-24 (décision de
Guilhem), `deck.html` est la page d'accueil de magnitude.pub (copié par
`.github/workflows/deploy.yml`) ; il reste servi à /deck (noindex) et
l'ancienne accueil Observable est servie à /newsletter.
## Ce que fait le prototype
- Swipe dans 4 directions : → Aligné, ← Désaligné, ↑ J'aimerais, ↓ M'en fous
  (souris, doigt, flèches du clavier ou boutons).
- Swipe « à l'aveugle » : le candidat est révélé après le geste, avec les
  positions documentées des autres candidats.
- Badge de décision sur chaque carte, décisions modifiables (« Mon deck »).
- Cartes « dans le score » et « hors score » (décision du 2026-10-15, seuils
  redéfinis le 2026-10-23) : une carte compte si au moins les deux tiers des
  candidats du deck ont une position documentée, dont la moitié en niveau A
  ou B (8/6 avec 12 candidats, 9/7 avec 13 ; calcul automatique). À la
  révélation, une carte dans le score prend la teinte Magnitude de son
  candidat avec un reflet holographique (portrait brillant, inclinaison au
  doigt ou à la souris) ; une carte hors score devient sobre, garde l'avis
  mais n'entre pas dans le calcul. Le recto reste anonyme dans les deux cas.
- Score par candidat = accords / positions documentées (cartes Aligné ou
  Désaligné, sur les cartes dans le score uniquement), seuil de 4 cartes, égalités affichées, classement
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

## Ajouter un numéro
```bash
python3 prototypes/deck/ajout_numero.py 2 ../magnitude-analysis --semaine 45
python3 prototypes/deck/extract_fiches.py ../magnitude-analysis
```
Puis ajouter le chiffre-clé (anonyme) et le pictogramme de chaque nouvelle
carte dans `build_deck.py` (FIGURES, ICONS), copier les analyses complètes
dans `src/numeros/<n>/reports/` et reconstruire. Un nouveau candidat reçoit
une teinte supplémentaire (TEINTES_SUPPL) sans changer celles des autres, et
un monogramme tant que son portrait n'est pas dans `src/candidats/`.

## Reconstruire
```bash
python3 prototypes/deck/build_deck.py
```
Entrées : `deck-data.json` (extrait de `magnitude-analysis/data/analyses/*.json`
et des pages de numéro publiées), `src/candidats/*.png`, `deck-template.html`.
Sortie : `deck.html` (fichier unique, autonome).
