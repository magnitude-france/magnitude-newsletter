---
toc: false
sidebar: false
---

<style>
/* Magnitude — site vitrine, one-pager (Version A)
   Palette et typographie reprises du design system des cartes/emails
   (voir 06-Tech/Design-system-graphiques dans le second brain) pour
   une cohérence visuelle entre le site, le front clickable et l'email. */
:root {
  --accent: #D97706;
  --reference: #2A78D6;
  --ink: #0B0B0B;
  --ink-secondary: #52514E;
  --ink-muted: #898781;
  --gridline: #E1E0D9;
  --surface: #FCFCFB;
  --page: #F9F9F7;
  --border: rgba(11,11,11,0.10);
}

/* Reprend toute la largeur de la page — le thème par défaut d'Observable
   Framework contraint la largeur de lecture (~640px), adapté à de la
   documentation mais pas à un one-pager marketing scrollable. */
.observablehq main {
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
.observablehq-header, .observablehq-footer { display: none !important; }

body {
  background: var(--page);
  color: var(--ink);
}

.mg-section {
  max-width: 880px;
  margin: 0 auto;
  padding: 72px 24px;
}
.mg-section + .mg-section { border-top: 1px solid var(--border); }
.mg-section.mg-surface { background: var(--surface); }

.mg-brand {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 15px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 22px;
}
.mg-h1 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 42px;
  line-height: 1.2;
  margin: 0 0 20px;
  max-width: 18ch;
}
.mg-lede {
  font-size: 18px;
  line-height: 1.6;
  color: var(--ink-secondary);
  max-width: 58ch;
  margin: 0 0 28px;
}
.mg-h2 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 28px;
  margin: 0 0 24px;
}
.mg-cta {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  text-decoration: none;
  font-weight: 700;
  font-size: 15px;
  padding: 13px 26px;
  border-radius: 6px;
}
.mg-cta:hover { opacity: 0.9; }
.mg-cta-ghost {
  display: inline-block;
  border: 1px solid var(--accent);
  color: var(--accent);
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  padding: 11px 22px;
  border-radius: 6px;
  margin-left: 12px;
}

.mg-pillars { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 8px; }
.mg-pillar { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 22px 22px; }
.mg-pillar h3 { font-size: 15px; margin: 0 0 8px; }
.mg-pillar p { font-size: 14px; color: var(--ink-secondary); margin: 0; line-height: 1.55; }

.mg-not-list { list-style: none; padding: 0; margin: 24px 0 0; }
.mg-not-list li { padding: 10px 0 10px 28px; position: relative; font-size: 15px; color: var(--ink-secondary); border-top: 1px solid var(--border); }
.mg-not-list li:before { content: "✕"; position: absolute; left: 0; color: var(--ink-muted); font-size: 12px; top: 13px; }

.mg-example { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: center; margin-top: 28px; }
.mg-example img { width: 100%; border-radius: 6px; border: 1px solid var(--border); display: block; }
.mg-example .mg-tag { display:inline-block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:3px 9px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:12px; }
.mg-example h3 { font-family: Georgia, serif; font-size: 19px; margin: 0 0 10px; }
.mg-example p { font-size: 14.5px; color: var(--ink-secondary); line-height:1.6; margin: 0 0 14px; }

.mg-filters { display: flex; gap: 12px; flex-wrap: wrap; margin: 8px 0 28px; }
.mg-filters select {
  font-family: inherit; font-size: 13.5px; padding: 8px 12px; border-radius: 6px;
  border: 1px solid var(--border); background: #fff; color: var(--ink);
}
.mg-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
.mg-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }
.mg-card img { width: 100%; height: auto; display: block; border-bottom: 1px solid var(--border); }
.mg-card .mg-body { padding: 16px 18px 18px; }
.mg-card .mg-tag { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:9px; }
.mg-card .mg-theme { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:#e9f0fa; color:var(--reference); margin-bottom:9px; margin-left:6px; }
.mg-card h4 { font-family: Georgia, serif; font-size: 15.5px; line-height:1.35; margin: 0 0 12px; }
.mg-card a { font-size: 13px; font-weight: 700; color: var(--accent); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }
.mg-empty { color: var(--ink-muted); font-size: 14px; padding: 24px 0; }

.mg-numero-link { text-align: center; margin-top: 28px; }

.mg-offer-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 24px; }
.mg-offer { border: 1px solid var(--border); border-radius: 8px; padding: 24px 24px; background: var(--surface); }
.mg-offer.mg-offer-premium { border-color: var(--accent); }
.mg-offer h3 { font-family: Georgia, serif; font-size: 18px; margin: 0 0 6px; }
.mg-offer .mg-price { font-size: 13px; color: var(--ink-muted); margin: 0 0 14px; }
.mg-offer ul { padding-left: 18px; margin: 0; font-size: 14px; color: var(--ink-secondary); line-height: 1.7; }
.mg-offer .mg-soon { display:inline-block; margin-top:14px; font-size:12px; color: var(--ink-muted); font-style: italic; }

.mg-footer { background: #0F172A; color: #E7E5E1; }
.mg-footer .mg-h2 { color: #fff; }
.mg-footer p { color: #B8B6B0; font-size: 13.5px; line-height: 1.7; }
.mg-footer .mg-legal { font-size: 12px; color: #8B8A85; margin-top: 24px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }

@media (max-width: 720px) {
  .mg-h1 { font-size: 32px; }
  .mg-example { grid-template-columns: 1fr; }
  .mg-offer-grid { grid-template-columns: 1fr; }
}
</style>

<!-- ============ 1. HERO ============ -->
<section class="mg-section" style="padding-top:96px;">
  <div class="mg-brand">Magnitude</div>
  <h1 class="mg-h1">Un chiffre politique, remis à l'échelle — chaque semaine.</h1>
  <p class="mg-lede">
    Magnitude est une publication data qui apprend à lire les chiffres
    de la vie politique et citoyenne : un graphique, une histoire
    sourcée, pour chaque mesure qui fait l'actualité. Sans jargon, sans
    étiquette politique affichée. Angle d'actualité actuel : la
    présidentielle 2027.
  </p>
  <a class="mg-cta" href="https://buttondown.com/magnitude-publication">S'abonner gratuitement →</a>
  <a class="mg-cta-ghost" href="#historique">Voir les numéros</a>
</section>

<!-- ============ 2. VISION / MANIFESTE ============ -->
<section class="mg-section mg-surface">
  <h2 class="mg-h2">Notre mission</h2>
  <p class="mg-lede" style="font-size:19px; font-style:italic; color:var(--ink);">
    « Magnitude est une communauté apartisane qui a pour but de
    démocratiser la pédagogie autour de l'analyse de données et de la
    compréhension des données par les citoyens, pour permettre à chacun
    de prendre des décisions éclairées en fonction de ses sensibilités. »
  </p>
  <h3 style="font-family:Georgia,serif; font-size:16px; margin:36px 0 4px;">Ce que Magnitude n'est pas</h3>
  <ul class="mg-not-list">
    <li>Un fact-checker de plus — on ne vérifie pas une déclaration isolée, on donne les clés pour la lire.</li>
    <li>Un agrégateur de sondages — on ne fait pas la course aux intentions de vote.</li>
    <li>Un média d'opinion — on ne dit jamais pour qui voter, ni ce qu'il faut penser d'une mesure.</li>
  </ul>
</section>

<!-- ============ 3. COMMENT ÇA MARCHE ============ -->
<section class="mg-section">
  <h2 class="mg-h2">Comment ça marche</h2>
  <p class="mg-lede">
    Chaque numéro assemble jusqu'à 6 cartes, une par mesure de campagne
    qui fait l'actualité. Une carte, c'est toujours la même anatomie :
    une mesure annoncée, un graphique qui remet le chiffre en contexte,
    et un deep dive qui raconte la donnée derrière — sourcée, datée, avec
    son niveau de confiance affiché.
  </p>
  <div class="mg-example">
    <img src="/numeros/0/charts/carte_03_philippe_fiscalite.png" alt="Comparaison du coin fiscal France vs moyenne UE-OCDE vs moyenne OCDE, 2024" loading="lazy">
    <div>
      <div class="mg-tag">Centre-droit — Horizons</div>
      <h3>Philippe veut baisser la fiscalité des classes moyennes — où la France se situe-t-elle vraiment ?</h3>
      <p>Édouard Philippe veut baisser la fiscalité des classes moyennes.
      La fiscalité du travail française est très élevée dans l'absolu,
      mais proche de la moyenne européenne.</p>
      <a href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Lire le deep dive complet →</a>
    </div>
  </div>
</section>

<!-- ============ 4. HISTORIQUE DES NUMÉROS ============ -->
<section class="mg-section mg-surface" id="historique">
  <h2 class="mg-h2">L'historique des numéros</h2>
  <p class="mg-lede" style="font-size:15px;">
    Toutes les cartes publiées, filtrables par thème et par famille
    politique. L'ordre d'affichage de chaque numéro est tiré
    aléatoirement (méthode publique — voir « Confiance & méthode »
    ci-dessous) : il ne reflète donc pas un classement ou une
    priorité, seulement l'ordre de tirage du numéro.
  </p>
  <div class="mg-filters">
    <select id="mg-filter-theme" aria-label="Filtrer par thème">
      <option value="">Tous les thèmes</option>
    </select>
    <select id="mg-filter-famille" aria-label="Filtrer par famille politique">
      <option value="">Toutes les familles politiques</option>
    </select>
  </div>
  <div class="mg-grid" id="mg-grid"></div>
  <p class="mg-empty" id="mg-empty" style="display:none;">Aucune carte ne correspond à ce filtre.</p>
  <div class="mg-numero-link">
    <a class="mg-cta-ghost" href="/numeros/0/numero-0.html">Voir le numéro #0 complet →</a>
  </div>
</section>

<!-- ============ 5. QUI SOMMES-NOUS ============ -->
<section class="mg-section">
  <h2 class="mg-h2">Qui sommes-nous</h2>
  <p class="mg-lede">
    Magnitude est portée par une petite équipe indépendante, sans
    attache partisane, convaincue qu'un citoyen bien informé se décide
    mieux qu'un citoyen convaincu par une infographie trompeuse. Notre
    seul engagement éditorial est envers le lecteur : sourcer chaque
    chiffre, traiter chaque famille politique avec la même rigueur, et
    ne jamais transformer un désaccord de fond en un jugement de valeur.
  </p>
  <p class="mg-lede">
    Nous ne sommes ni journalistes encartés, ni militants — nous sommes
    des praticiens de la donnée qui pensent que la lutte contre la
    désinformation passe autant par l'outillage du lecteur que par la
    correction de l'erreur après coup.
  </p>
</section>

<!-- ============ 6. CONFIANCE & MÉTHODE ============ -->
<section class="mg-section mg-surface">
  <h2 class="mg-h2">Confiance & méthode</h2>
  <div class="mg-pillars">
    <div class="mg-pillar">
      <h3>Symétrie de traitement</h3>
      <p>Chaque famille politique représentée par un candidat déclaré reçoit, sur la durée, un traitement comparable en fréquence et en longueur.</p>
    </div>
    <div class="mg-pillar">
      <h3>Sourcing systématique</h3>
      <p>Chaque chiffre est associé à sa source primaire nommée, sa date d'extraction, un lien vérifiable et un niveau de confiance affiché.</p>
    </div>
    <div class="mg-pillar">
      <h3>Ordre tiré au sort</h3>
      <p>La position des cartes dans un numéro est calculée par un tirage pseudo-aléatoire déterministe, jamais choisie à la main — méthode publique, auditée numéro après numéro.</p>
    </div>
    <div class="mg-pillar">
      <h3>Financement privé et transparent</h3>
      <p>Publicité non partisane et abonnements lecteurs uniquement — jamais de subvention publique, jamais d'annonceur lié à un parti ou un candidat.</p>
    </div>
  </div>
</section>

<!-- ============ 7. OFFRE ============ -->
<section class="mg-section">
  <h2 class="mg-h2">L'offre</h2>
  <p class="mg-lede">Un récap hebdomadaire, complété par des éditions au fil de l'actualité électorale.</p>
  <div class="mg-offer-grid">
    <div class="mg-offer">
      <h3>Gratuit</h3>
      <p class="mg-price">Pour tout le monde, dès le premier numéro</p>
      <ul>
        <li>Toutes les cartes (graphique + message)</li>
        <li>Le deep dive synthétique de chaque carte</li>
        <li>L'historique complet des numéros</li>
      </ul>
    </div>
    <div class="mg-offer mg-offer-premium">
      <h3>Premium</h3>
      <p class="mg-price">Le deep dive approfondi — le récit complet derrière l'insight</p>
      <ul>
        <li>Packs de crédits (dès 5 €) ou abonnement illimité</li>
        <li>Accès à l'intégralité du récit et de ses sources</li>
      </ul>
      <span class="mg-soon">Pas encore actif — Magnitude démarre 100 % gratuite, le palier premium arrive une fois l'audience installée.</span>
    </div>
  </div>
</section>

<!-- ============ 8. FOOTER ============ -->
<section class="mg-section mg-footer">
  <h2 class="mg-h2">Rejoindre Magnitude</h2>
  <p>Un email par semaine, pas plus. Désinscription en un clic, à tout moment.</p>
  <a class="mg-cta" href="https://buttondown.com/magnitude-publication">S'abonner gratuitement →</a>
  <p style="margin-top:28px;">Réseaux sociaux : bientôt disponibles.</p>
  <p class="mg-legal">
    Magnitude — publication indépendante, magnitude.pub.
    Financement privé uniquement (publicité non partisane et
    abonnements lecteurs) — aucune subvention publique ni partisane.
    © 2026.
  </p>
</section>

<script type="module">
// Données du grid "historique des numéros" — recopiées à la main depuis
// magnitude-analysis/scripts/build_front.py (CARTES_ORDONNEES, numéro #0).
// TODO (futur) : générer ce bloc automatiquement depuis le pipeline
// Python plutôt que de le recopier à la main à chaque nouveau numéro.
const numeros = [
  {
    numero: 0,
    cartes: [
      { slug: "philippe-fiscalite", candidat: "Édouard Philippe", famille: "Centre-droit — Horizons", theme: "Fiscalité",
        titre: "Philippe veut baisser la fiscalité des classes moyennes — où la France se situe-t-elle vraiment ?",
        chart: "/numeros/0/charts/carte_03_philippe_fiscalite.png",
        deepDive: "/numeros/0/reports/carte_03_philippe_fiscalite.html" },
      { slug: "glucksmann-patrimoine", candidat: "Raphaël Glucksmann", famille: "Centre-gauche — Place Publique", theme: "Fiscalité & patrimoine",
        titre: "Glucksmann veut taxer davantage les grandes fortunes — la concentration du patrimoine en 3 chiffres",
        chart: "/numeros/0/charts/carte_04_glucksmann_patrimoine.png",
        deepDive: "/numeros/0/reports/carte_04_glucksmann_patrimoine.html" },
      { slug: "retailleau-referendum", candidat: "Bruno Retailleau", famille: "Droite — LR", theme: "Institutions",
        titre: "Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans",
        chart: "/numeros/0/charts/carte_02_retailleau_referendum.png",
        deepDive: "/numeros/0/reports/carte_02_retailleau_referendum.html" },
      { slug: "tondelier-climat", candidat: "Marine Tondelier", famille: "Gauche écologiste — Les Écologistes", theme: "Climat",
        titre: "Tondelier veut une fiscalité verte pour la transition — l'ampleur du décrochage de rythme",
        chart: "/numeros/0/charts/carte_05_tondelier_climat.png",
        deepDive: "/numeros/0/reports/carte_05_tondelier_climat.html" },
      { slug: "le-pen-logement", candidat: "Marine Le Pen", famille: "Extrême-droite — RN", theme: "Logement",
        titre: "Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs",
        chart: "/numeros/0/charts/carte_01_le_pen_logement.png",
        deepDive: "/numeros/0/reports/carte_01_le_pen_logement.html" },
      { slug: "melenchon-confiance", candidat: "Jean-Luc Mélenchon", famille: "Extrême-gauche — LFI", theme: "Institutions",
        titre: "Mélenchon veut une VIe République — la confiance dans les institutions au plus bas",
        chart: "/numeros/0/charts/carte_06_melenchon_confiance.png",
        deepDive: "/numeros/0/reports/carte_06_melenchon_confiance.html" }
    ]
  }
];

const allCartes = numeros.flatMap(n => n.cartes.map(c => ({...c, numero: n.numero})));

const grid = document.getElementById("mg-grid");
const empty = document.getElementById("mg-empty");
const themeSelect = document.getElementById("mg-filter-theme");
const familleSelect = document.getElementById("mg-filter-famille");

function uniq(arr) { return [...new Set(arr)]; }

uniq(allCartes.map(c => c.theme)).sort().forEach(theme => {
  const opt = document.createElement("option");
  opt.value = theme; opt.textContent = theme;
  themeSelect.appendChild(opt);
});
uniq(allCartes.map(c => c.famille)).sort().forEach(famille => {
  const opt = document.createElement("option");
  opt.value = famille; opt.textContent = famille;
  familleSelect.appendChild(opt);
});

function render() {
  const theme = themeSelect.value;
  const famille = familleSelect.value;
  const filtered = allCartes.filter(c =>
    (!theme || c.theme === theme) && (!famille || c.famille === famille)
  );
  grid.innerHTML = "";
  empty.style.display = filtered.length ? "none" : "block";
  filtered.forEach(c => {
    const card = document.createElement("div");
    card.className = "mg-card";
    card.innerHTML = `
      <img src="${c.chart}" alt="${c.titre}" loading="lazy">
      <div class="mg-body">
        <span class="mg-tag">${c.famille}</span><span class="mg-theme">${c.theme}</span>
        <h4>${c.titre}</h4>
        <a href="${c.deepDive}">Lire le deep dive →</a>
      </div>`;
    grid.appendChild(card);
  });
}

themeSelect.addEventListener("change", render);
familleSelect.addEventListener("change", render);
render();
</script>
