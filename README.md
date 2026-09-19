# Magnitude — site newsletter

Site statique généré avec [Observable Framework](https://observablehq.com/framework/),
déployé sur GitHub Pages, domaine personnalisé `magnitude.pub`.

## Développement local

```
npm install
npm run dev
```

## Build

```
npm run build
```

## Déploiement

Le push sur `main` déclenche automatiquement le déploiement via GitHub
Actions (`.github/workflows/deploy.yml`).

Pour la première mise en ligne :
1. Créer le repo GitHub `magnitude-newsletter` et pousser ce dossier.
2. Dans Settings → Pages, choisir "GitHub Actions" comme source.
3. Toujours dans Settings → Pages, renseigner `magnitude.pub` comme domaine personnalisé.
4. Chez OVHcloud, pointer les DNS de `magnitude.pub` vers GitHub Pages
   (voir le journal du projet dans le second brain pour le détail des
   enregistrements).
