# Deck Magnitude (« Find your Candidate »)

Jeu de cartes à collectionner de Magnitude (comité de direction n°1,
2026-10-14). Nom retenu le 2026-10-15 : **Magnitude**, avec « Find your
Candidate » en accroche. **Déployé** : depuis le 2026-10-24 (décision de
Guilhem), `deck.html` est la page d'accueil de magnitude.pub (copié par
`.github/workflows/deploy.yml`) ; il reste servi à /deck (noindex) et
l'ancienne accueil Observable est servie à /newsletter.

## Ce que fait le prototype
- Introduction par un « maître du jeu » (2026-10-30) : accueil, écran
  « Vos priorités » (1 à 5 thèmes parmi ceux des cartes et des thèmes sans
  carte, `THEMES_ATTENDUS`), puis première partie guidée (retourner la carte,
  les 4 gestes montrés par la carte, commentaire du premier vote, première
  révélation commentée). À la fin du paquet, bascule automatique sur Mon deck.
- Carte mystère : le verso montre le thème sur un motif holographique tiré au
  hasard à chaque carte ; un toucher (ou Entrée, Espace, une flèche) la
  retourne avec un zoom. Le recto, allégé : thème, accroche directe
  (`ACCROCHES`, relues le 2026-10-30), chiffre-clé, graphique européen réduit à
  5 lignes au plus (la ligne France toujours gardée), bouton « Comprendre ·
  sources » vers la fiche complète.
- Swipe dans 4 directions : → Aligné (d'accord), ← Désaligné (pas d'accord),
  ↑ J'aimerais (le sujet compte, la mesure est à revoir), ↓ M'en fous (pas ma
  priorité, un autre sujet passerait avant) — souris, doigt, flèches du
  clavier ou boutons ; la carte se lit avant de se trancher.
- Tirage d'affilée, sans fenêtre « qui est le candidat » entre deux cartes
  (décision du 2026-10-24) : les candidats se révèlent par lots de 5 cartes
  (et à la dernière carte du paquet). Le lot retourne les cartes, montre la
  bascule éventuelle de galaxie et permet de changer un choix ; le détail de
  chaque carte reste accessible depuis Mon deck.
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
  Désaligné, sur les cartes dans le score uniquement), **pondéré par les
  priorités** (2026-10-30) : une carte d'un thème prioritaire pèse double, et
  un candidat sans position documentée sur une carte prioritaire dans le
  score compte un demi-désaccord (« silence »). Thèmes prioritaires = choisis
  à l'introduction + ceux des cartes votées J'aimerais − ceux des cartes
  votées M'en fous. Seuil de 4 cartes documentées, égalités affichées,
  classement de tous les candidats toujours visible.
- Mon deck : bloc « Vos priorités » (modifiable), filtres du recueil par
  choix (Aligné, Désaligné, J'aimerais, M'en fous, à trancher).
- « Redistribuer une pioche » (fin du paquet et Mon deck) : les mesures sont
  remélangées (ordre gardé dans `localStorage`, `order`) et se rejouent depuis
  le début ; les choix sont effacés, les priorités gardées. « Tout
  recommencer » rejoue dans l'ordre des numéros.
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
- Test de neutralité (`test_neutralite.py`, trois lectures dont une avec
  priorités) en **échec** au 2026-10-30, avant comme après la pondération :
  sur les 7 cartes dans le score, Philippe sort n°1 chez ~44 % des
  utilisateurs simulés qui obtiennent une galaxie (borne : 12,5 %).
- Polices : Literata (lecture), IM Fell English (grands titres), La Belle
  Aurore (quelques encarts manuscrits), SIL OFL, intégrées dans `deck.html`.

## Ajouter un numéro
```bash
python3 prototypes/deck/ajout_numero.py 2 ../magnitude-analysis --semaine 45
python3 prototypes/deck/extract_fiches.py ../magnitude-analysis
```
Puis ajouter le chiffre-clé (anonyme), l'accroche (anonyme, sans chiffre
nouveau) et le pictogramme de chaque nouvelle carte dans `build_deck.py`
(FIGURES, ACCROCHES, ICONS), copier les analyses complètes
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
