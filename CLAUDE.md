# Guardrails pour les agents IA — magnitude-newsletter

Ce fichier est lu par l'agent (Claude Code ou équivalent) en début de session
sur ce repo. Il fixe les règles à respecter sans qu'une review humaine soit
nécessaire pour les faire appliquer à chaque fois.

## Périmètre technique
- Ce repo utilise Observable Framework (Node.js / Markdown / JS). C'est le
  seul repo de Magnitude où du JS est légitime — c'est le framework qui
  l'impose, pas un choix à étendre ailleurs.
- Ne pas ajouter de nouvelle dépendance npm sans la justifier explicitement :
  chaque dépendance est une surface de plus à auditer sur un repo qui publie
  du contenu public.
- Respecter la structure existante : `src/` pour le contenu (pages
  `.md`, `numeros/`), pas de logique métier dispersée hors de cette
  structure.

## Contenu publié
- Ce repo produit un site public déployé automatiquement sur push vers
  `main` (voir `.github/workflows/deploy.yml`). Tout changement de contenu
  qui touche `src/numeros/` ou `src/index.md` est visible publiquement dès
  le merge — à traiter avec la même rigueur qu'un changement de code.
- Toute modification de `.github/workflows/deploy.yml` (permissions, trigger
  de déploiement) doit être signalée explicitement comme "à relire avant
  merge".

## Avant de proposer une pull request
- Vérifier que `npm run build` passe localement avant de proposer le commit.
- Résumer en une phrase le "pourquoi" du changement.
- Signaler explicitement tout changement de contenu publié (nouveau numéro,
  modification d'un numéro existant) pour relecture éditoriale avant merge.
