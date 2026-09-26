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
  --reference: #3D5A6C;
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
  color: var(--ink);
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
  color: var(--ink);
}
.mg-cta {
  display: inline-block;
  background: var(--accent);
  color: #fff !important;
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
  color: var(--accent) !important;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  padding: 11px 22px;
  border-radius: 6px;
  margin-left: 12px;
}

.mg-pillars { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 8px; }
.mg-pillar { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 22px 22px; }
.mg-pillar h3 { font-size: 15px; margin: 0 0 8px; color: var(--ink); }
.mg-pillar p { font-size: 14px; color: var(--ink-secondary); margin: 0; line-height: 1.55; }

.mg-not-list { list-style: none; padding: 0; margin: 24px 0 0; }
.mg-not-list li { padding: 10px 0 10px 28px; position: relative; font-size: 15px; color: var(--ink-secondary); border-top: 1px solid var(--border); }
.mg-not-list li:before { content: "✕"; position: absolute; left: 0; color: var(--ink-muted); font-size: 12px; top: 13px; }

.mg-example { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: center; margin-top: 28px; }
.mg-example img { width: 100%; border-radius: 6px; border: 1px solid var(--border); display: block; }
.mg-example .mg-tag { display:inline-block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:3px 9px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:12px; }
.mg-example h3 { font-family: Georgia, serif; font-size: 19px; margin: 0 0 10px; color: var(--ink); }
.mg-example p { font-size: 14.5px; color: var(--ink-secondary); line-height:1.6; margin: 0 0 14px; }
.mg-example a { font-size: 14px; font-weight: 700; color: var(--accent); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }

.mg-filters { display: flex; gap: 12px; flex-wrap: wrap; margin: 8px 0 28px; }
.mg-filters select {
  font-family: inherit; font-size: 13.5px; padding: 8px 12px; border-radius: 6px;
  border: 1px solid var(--border); background: #fff; color: var(--ink);
}
.mg-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
.mg-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; transition: box-shadow .15s ease, transform .15s ease; }
.mg-card:hover { box-shadow: 0 6px 18px rgba(11,11,11,0.08); transform: translateY(-1px); }
.mg-card img { width: 100%; height: auto; display: block; border-bottom: 1px solid var(--border); }
.mg-card > a.mg-card-link { display: block; }
.mg-card > a.mg-card-link img { transition: opacity .15s ease; }
.mg-card > a.mg-card-link:hover img { opacity: 0.88; }
.mg-card h4 a.mg-card-link { color: inherit; text-decoration: none; border-bottom: none; transition: color .15s ease; }
.mg-card h4 a.mg-card-link:hover { color: var(--accent); }
.mg-card .mg-body { padding: 16px 18px 18px; }
.mg-card .mg-tag { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:9px; }
.mg-card .mg-theme { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:#E7EEF0; color:var(--reference); margin-bottom:9px; margin-left:6px; }
.mg-card h4 { font-family: Georgia, serif; font-size: 15.5px; line-height:1.35; margin: 0 0 12px; color: var(--ink); }
.mg-card a { font-size: 13px; font-weight: 700; color: var(--accent); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }
.mg-empty { color: var(--ink-muted); font-size: 14px; padding: 24px 0; }

.mg-numero-link { margin: 4px 0 24px; }
.mg-numero-link .mg-cta-ghost { margin-left: 0; }

.mg-offer-grid { display: grid; grid-template-columns: 1fr; max-width: 420px; margin: 24px auto 0; gap: 20px; }
.mg-offer { border: 1px solid var(--border); border-radius: 8px; padding: 24px 24px; background: var(--surface); }
.mg-offer h3 { font-family: Georgia, serif; font-size: 18px; margin: 0 0 6px; color: var(--ink); }
.mg-offer .mg-price { font-size: 13px; color: var(--ink-muted); margin: 0 0 14px; }
.mg-offer ul { padding-left: 18px; margin: 0; font-size: 14px; color: var(--ink-secondary); line-height: 1.7; }

.mg-footer { background: #0F172A; color: #E7E5E1; }
.mg-footer .mg-h2 { color: #fff; }
.mg-footer p { color: #B8B6B0; font-size: 13.5px; line-height: 1.7; }
.mg-footer .mg-legal { font-size: 12px; color: #8B8A85; margin-top: 24px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }

@media (max-width: 720px) {
  .mg-h1 { font-size: 32px; }
  .mg-example { grid-template-columns: 1fr; }
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
    une mesure annoncée — citée mot pour mot, avec la source et la date
    de la déclaration du candidat —, un graphique qui remet le chiffre en contexte,
    et un deep dive qui raconte la donnée derrière — sourcée, datée, avec
    son niveau de confiance affiché.
  </p>
  <div class="mg-example">
    <img src="/numeros/0/charts/carte_03_philippe_fiscalite.png" alt="Impôts sur la production en % du PIB, France, UE à 27 et Allemagne, 2010-2024" loading="lazy">
    <div>
      <div class="mg-tag">Centre-droit — Horizons</div>
      <h3>Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?</h3>
      <p>Édouard Philippe propose de baisser les impôts de production en
      échange d'une baisse des aides aux entreprises. Ces impôts pèsent
      4,4 % du PIB en France, près de deux fois la moyenne européenne.</p>
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
  <div class="mg-numero-link">
    <a class="mg-cta-ghost" href="/numeros/0/numero-0.html">Voir le dernier numéro complet →</a>
  </div>
  <div class="mg-filters">
    <select id="mg-filter-theme" aria-label="Filtrer par thème">
      <option value="">Tous les thèmes</option>
    </select>
    <select id="mg-filter-famille" aria-label="Filtrer par famille politique">
      <option value="">Toutes les familles politiques</option>
    </select>
  </div>
  <div class="mg-grid" id="mg-grid">
    <div class="mg-card" data-theme="Fiscalité des entreprises" data-famille="Centre-droit — Horizons">
      <a class="mg-card-link" href="/numeros/0/reports/carte_03_philippe_fiscalite.html" aria-label="Lire le deep dive : Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?"><img src="/numeros/0/charts/carte_03_philippe_fiscalite.png" alt="Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Centre-droit — Horizons</span><span class="mg-theme">Fiscalité des entreprises</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?</a></h4>
        <a href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Lire le deep dive →</a>
      </div>
    </div>
    <div class="mg-card" data-theme="Fiscalité &amp; patrimoine" data-famille="Centre-gauche — Place Publique">
      <a class="mg-card-link" href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html" aria-label="Lire le deep dive : Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres"><img src="/numeros/0/charts/carte_04_glucksmann_patrimoine.png" alt="Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Centre-gauche — Place Publique</span><span class="mg-theme">Fiscalité & patrimoine</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html">Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres</a></h4>
        <a href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html">Lire le deep dive →</a>
      </div>
    </div>
    <div class="mg-card" data-theme="Institutions" data-famille="Droite — LR">
      <a class="mg-card-link" href="/numeros/0/reports/carte_02_retailleau_referendum.html" aria-label="Lire le deep dive : Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans"><img src="/numeros/0/charts/carte_02_retailleau_referendum.png" alt="Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Droite — LR</span><span class="mg-theme">Institutions</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_02_retailleau_referendum.html">Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans</a></h4>
        <a href="/numeros/0/reports/carte_02_retailleau_referendum.html">Lire le deep dive →</a>
      </div>
    </div>
    <div class="mg-card" data-theme="Climat" data-famille="Gauche écologiste — Les Écologistes">
      <a class="mg-card-link" href="/numeros/0/reports/carte_05_tondelier_climat.html" aria-label="Lire le deep dive : Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme"><img src="/numeros/0/charts/carte_05_tondelier_climat.png" alt="Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Gauche écologiste — Les Écologistes</span><span class="mg-theme">Climat</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_05_tondelier_climat.html">Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme</a></h4>
        <a href="/numeros/0/reports/carte_05_tondelier_climat.html">Lire le deep dive →</a>
      </div>
    </div>
    <div class="mg-card" data-theme="Logement" data-famille="Extrême-droite — RN">
      <a class="mg-card-link" href="/numeros/0/reports/carte_01_le_pen_logement.html" aria-label="Lire le deep dive : Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs"><img src="/numeros/0/charts/carte_01_le_pen_logement.png" alt="Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Extrême-droite — RN</span><span class="mg-theme">Logement</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_01_le_pen_logement.html">Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs</a></h4>
        <a href="/numeros/0/reports/carte_01_le_pen_logement.html">Lire le deep dive →</a>
      </div>
    </div>
    <div class="mg-card" data-theme="Institutions" data-famille="Extrême-gauche — LFI">
      <a class="mg-card-link" href="/numeros/0/reports/carte_06_melenchon_confiance.html" aria-label="Lire le deep dive : Mélenchon veut une VIe République — la confiance dans les institutions au plus bas"><img src="/numeros/0/charts/carte_06_melenchon_confiance.png" alt="Mélenchon veut une VIe République — la confiance dans les institutions au plus bas" loading="lazy"></a>
      <div class="mg-body">
        <span class="mg-tag">Extrême-gauche — LFI</span><span class="mg-theme">Institutions</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_06_melenchon_confiance.html">Mélenchon veut une VIe République — la confiance dans les institutions au plus bas</a></h4>
        <a href="/numeros/0/reports/carte_06_melenchon_confiance.html">Lire le deep dive →</a>
      </div>
    </div>
  </div>
  <p class="mg-empty" id="mg-empty" style="display:none;">Aucune carte ne correspond à ce filtre.</p>
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
      <p>Publicité non partisane uniquement — jamais de subvention publique. Magnitude est gratuite : aucun contenu payant.</p>
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
      <p class="mg-price">Pour tout le monde, sans exception, dès le premier numéro</p>
      <ul>
        <li>Toutes les cartes (graphique + message)</li>
        <li>Le deep dive complet de chaque carte, synthèse et récit approfondi</li>
        <li>L'historique complet des numéros</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ 8. FOOTER ============ -->
<section class="mg-section mg-footer">
  <h2 class="mg-h2">Rejoindre Magnitude</h2>
  <p>Un email par semaine, pas plus. Désinscription en un clic, à tout moment.</p>
  <a class="mg-cta" href="https://buttondown.com/magnitude-publication">S'abonner gratuitement →</a>
  <p style="margin-top:28px;">Suivez Magnitude sur <a href="https://x.com/magnitudefrance" target="_blank" rel="noopener">X (@magnitudefrance)</a>.</p>
  <p class="mg-legal">
    Magnitude — publication indépendante, magnitude.pub. Gratuite,
    sans contenu payant. Financement privé uniquement (publicité non
    partisane) — aucune subvention publique ni partisane. © 2026.
  </p>
</section>

<script type="module">
// Les cartes du grid "historique des numéros" sont maintenant du HTML
// statique (voir ci-dessus), pas générées en JS : Observable Framework
// ne détecte au moment du build que les images/liens présents dans le
// HTML statique de la page pour les copier au bon endroit -- des <img>
// injectées dynamiquement via innerHTML passaient inaperçues et
// pointaient vers un chemin qui n'existait plus une fois le site
// construit (d'où les images cassées). Ce script ne fait plus que
// filtrer (afficher/masquer) les cartes déjà présentes dans le DOM.
// TODO (futur) : générer les cartes statiques automatiquement depuis le
// pipeline Python plutôt que de les recopier à la main à chaque numéro.
const grid = document.getElementById("mg-grid");
const empty = document.getElementById("mg-empty");
const themeSelect = document.getElementById("mg-filter-theme");
const familleSelect = document.getElementById("mg-filter-famille");
const cards = Array.from(grid.querySelectorAll(".mg-card"));

function uniq(arr) { return [...new Set(arr)]; }

uniq(cards.map(c => c.dataset.theme)).sort().forEach(theme => {
  const opt = document.createElement("option");
  opt.value = theme; opt.textContent = theme;
  themeSelect.appendChild(opt);
});
uniq(cards.map(c => c.dataset.famille)).sort().forEach(famille => {
  const opt = document.createElement("option");
  opt.value = famille; opt.textContent = famille;
  familleSelect.appendChild(opt);
});

function render() {
  const theme = themeSelect.value;
  const famille = familleSelect.value;
  let visible = 0;
  cards.forEach(card => {
    const match = (!theme || card.dataset.theme === theme) && (!famille || card.dataset.famille === famille);
    card.style.display = match ? "" : "none";
    if (match) visible++;
  });
  empty.style.display = visible ? "none" : "block";
}

themeSelect.addEventListener("change", render);
familleSelect.addEventListener("change", render);
render();
</script>
