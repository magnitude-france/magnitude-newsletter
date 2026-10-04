---
toc: false
sidebar: false
---

<style>
/* Magnitude — site vitrine, one-pager (Version « Constellation »)
   Palette et typographie reprises du design system des cartes/emails
   (voir 05-Design/Guide-memorisation-visuelle dans le second brain).
   Jamais de couleurs de partis : les couleurs des icônes de candidats
   sont purement décoratives et ne codent aucune famille politique. */
:root {
  --accent: #D97706;
  --accent-dark: #B45309;
  --amber-soft: #FBBF24;
  --amber-pale: #FEF3C7;
  --reference: #0E659B;
  --sky: #38BDF8;
  --blue-pale: #DCEBF5;
  --navy: #0F172A;
  --navy-2: #1E293B;
  --ink: #0B0B0B;
  --ink-secondary: #52514E;
  --ink-muted: #898781;
  --gridline: #E1E0D9;
  --surface: #FCFCFB;
  --page: #F9F9F7;
  --border: rgba(11,11,11,0.10);
}

.observablehq main { max-width: none !important; padding: 0 !important; margin: 0 !important; }
.observablehq-header, .observablehq-footer { display: none !important; }
body { background: var(--page); color: var(--ink); }

/* Bandes pleine largeur */
.mg-band { width: 100%; }
.mg-band.mg-surface { background: var(--surface); }
.mg-band.mg-dark { background: var(--navy); color: #E2E8F0; }
.mg-band.mg-dark-deep { background: #0B1120; color: #E2E8F0; }
.mg-band + .mg-band { border-top: 1px solid var(--border); }
.mg-band.mg-dark + .mg-band.mg-dark, .mg-band.mg-dark + .mg-band { border-top: 0; }

.mg-section { max-width: 1040px; margin: 0 auto; padding: 72px 24px; }

.mg-brand {
  display: inline-flex; align-items: center; gap: 12px;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 18px; letter-spacing: 0.14em; text-transform: uppercase;
  color: #fff; font-weight: 700; margin-bottom: 26px;
}
.mg-brand img { width: 40px; height: 40px; border-radius: 9px; display: block; }
.mg-pill {
  display: inline-block; border: 1px solid var(--amber-soft); color: var(--amber-soft);
  font-size: 12.5px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
  padding: 6px 14px; border-radius: 999px; margin-bottom: 20px;
}
.mg-h1 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 54px; line-height: 1.07; margin: 0 0 20px; max-width: 14ch; color: #fff;
}
.mg-h1 em { font-style: normal; color: var(--amber-soft); }
.mg-lede { font-size: 18px; line-height: 1.6; color: var(--ink-secondary); max-width: 58ch; margin: 0 0 28px; }
.mg-dark .mg-lede { color: #CBD5E1; }
.mg-h2 { font-family: Georgia, "Times New Roman", serif; font-size: 32px; margin: 0 0 24px; color: var(--ink); }
.mg-dark .mg-h2, .mg-dark-deep .mg-h2 { color: #fff; }

.mg-cta {
  display: inline-block; background: var(--accent); color: #fff !important; text-decoration: none;
  font-weight: 700; font-size: 16px; padding: 15px 28px; border-radius: 10px;
}
.mg-cta:hover { opacity: 0.9; }
.mg-cta-ghost {
  display: inline-block; border: 1px solid var(--accent); color: var(--accent) !important;
  text-decoration: none; font-weight: 700; font-size: 14px; padding: 11px 22px; border-radius: 10px; margin-left: 12px;
}
.mg-dark .mg-cta-ghost { border-color: var(--amber-soft); color: var(--amber-soft) !important; }

/* ===== Hero + constellation ===== */
.mg-hero { display: flex; flex-wrap: wrap; align-items: center; gap: 40px; padding-top: 40px; padding-bottom: 80px; }
.mg-hero-text { flex: 1 1 440px; max-width: 560px; }
.mg-hero-art { flex: 1 1 420px; display: flex; justify-content: center; }
.mg-orbit { position: relative; width: 100%; max-width: 500px; aspect-ratio: 1 / 1; margin-bottom: 52px; }
.mg-orbit svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.mg-node, .mg-core {
  position: absolute; transform: translate(-50%, -50%); border-radius: 50%; display: block;
  box-shadow: 0 0 0 4px var(--navy), 0 6px 18px rgba(0,0,0,.35);
}
.mg-node { width: 11.5%; height: auto; aspect-ratio: 1/1; transition: transform .2s ease; }
.mg-node:hover { transform: translate(-50%, -50%) scale(1.08); }
.mg-core { left: 50%; top: 50%; width: 22%; border-radius: 22%; background: var(--navy-2); }
.mg-orbit-caption { text-align: center; font-size: 12.5px; color: #94A3B8; margin: 14px 0 0; }

/* ===== Mission ===== */
.mg-quote { font-family: Georgia, serif; font-size: 22px; line-height: 1.5; font-style: italic; color: var(--ink); max-width: 60ch; margin: 0; position: relative; padding-top: 64px; }
.mg-quote:before { content: "«"; position: absolute; top: -14px; left: -4px; font-size: 90px; color: var(--accent); line-height: 1; font-style: normal; }
.mg-not-list { list-style: none; padding: 0; margin: 24px 0 0; }
.mg-not-list li { padding: 10px 0 10px 28px; position: relative; font-size: 15px; color: var(--ink-secondary); border-top: 1px solid var(--border); }
.mg-not-list li:before { content: "✕"; position: absolute; left: 0; color: var(--accent); font-size: 12px; top: 13px; }

/* ===== Comment ça marche ===== */
.mg-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 8px 0 40px; }
.mg-step { background: var(--navy-2); border-top: 6px solid var(--accent); border-radius: 16px; padding: 26px; }
.mg-step:nth-child(2) { border-top-color: var(--sky); }
.mg-step:nth-child(3) { border-top-color: #FDE68A; }
.mg-step h3 { font-family: Georgia, serif; font-size: 22px; margin: 0 0 8px; color: var(--amber-soft); }
.mg-step:nth-child(2) h3 { color: var(--sky); }
.mg-step:nth-child(3) h3 { color: #FDE68A; }
.mg-step p { margin: 0; font-size: 15px; line-height: 1.55; color: #CBD5E1; }

.mg-example { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: center; background: #fff; border-radius: 18px; padding: 24px; color: var(--ink); }
.mg-example img { width: 100%; border-radius: 8px; border: 1px solid var(--border); display: block; }
.mg-example .mg-tag { display:inline-block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:3px 9px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:12px; }
.mg-example h3 { font-family: Georgia, serif; font-size: 19px; margin: 0 0 10px; color: var(--ink); }
.mg-example p { font-size: 14.5px; color: var(--ink-secondary); line-height:1.6; margin: 0 0 14px; }
.mg-example a.mg-more { font-size: 14px; font-weight: 700; color: var(--accent-dark); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }

/* ===== Historique ===== */
.mg-filters { display: flex; gap: 12px; flex-wrap: wrap; margin: 8px 0 28px; }
.mg-filters select { font-family: inherit; font-size: 13.5px; padding: 9px 12px; border-radius: 8px; border: 1px solid var(--border); background: #fff; color: var(--ink); }
.mg-gauge { display: flex; flex-direction: column; gap: 6px; min-width: 260px; font-size: 13.5px; color: var(--ink-secondary); }
.mg-gauge input[type=range] { width: 100%; accent-color: var(--accent); }
.mg-filters { align-items: end; }
.mg-card .mg-count { display:inline-block; font-size:10.5px; font-weight:700; letter-spacing:.04em; text-transform:uppercase; padding:2px 8px; border-radius:3px; background:var(--amber-pale); color:var(--accent-dark); margin-left:6px; margin-bottom:9px; }
.mg-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 22px; }
.mg-card { background: #fff; border: 1px solid var(--border); border-top: 6px solid var(--accent); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; transition: box-shadow .15s ease, transform .15s ease; }
.mg-card:nth-child(3n+2) { border-top-color: var(--reference); }
.mg-card:nth-child(3n) { border-top-color: var(--navy); }
.mg-card:hover { box-shadow: 0 8px 22px rgba(11,11,11,0.10); transform: translateY(-2px); }
.mg-card img { width: 100%; height: auto; display: block; border-bottom: 1px solid var(--border); }
.mg-card > a.mg-card-link { display: block; }
.mg-card > a.mg-card-link img { transition: opacity .15s ease; }
.mg-card > a.mg-card-link:hover img { opacity: 0.88; }
.mg-card h4 a.mg-card-link { color: inherit; text-decoration: none; border-bottom: none; transition: color .15s ease; }
.mg-card h4 a.mg-card-link:hover { color: var(--accent); }
.mg-card .mg-body { padding: 16px 18px 18px; }
.mg-card .mg-tag { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:#f3ede2; color:#92610a; margin-bottom:9px; }
.mg-card .mg-theme { display:inline-block; font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:2px 8px; border-radius:3px; background:var(--blue-pale); color:var(--reference); margin-bottom:9px; margin-left:6px; }
.mg-card h4 { font-family: Georgia, serif; font-size: 15.5px; line-height:1.35; margin: 0 0 12px; color: var(--ink); }
.mg-card a { font-size: 13px; font-weight: 700; color: var(--accent-dark); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }
.mg-empty { color: var(--ink-muted); font-size: 14px; padding: 24px 0; }
.mg-numero-link { margin: 4px 0 24px; }
.mg-numero-link .mg-cta-ghost { margin-left: 0; }

/* ===== Piliers ===== */
.mg-pillars { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 8px; }
.mg-pillar { border-radius: 16px; padding: 24px; background: var(--amber-pale); }
.mg-pillar:nth-child(2) { background: var(--blue-pale); }
.mg-pillar:nth-child(3) { background: #EFEEE9; }
.mg-pillar:nth-child(4) { background: #FDE68A; }
.mg-pillar h3 { font-family: Georgia, serif; font-size: 18px; margin: 0 0 8px; color: var(--ink); }
.mg-pillar p { font-size: 14.5px; color: #3a3935; margin: 0; line-height: 1.55; }

/* ===== Offre ===== */
.mg-offer-grid { display: grid; grid-template-columns: 1fr; max-width: 460px; margin: 24px 0 0; gap: 20px; }
.mg-offer { border-radius: 18px; padding: 28px; background: linear-gradient(135deg, var(--accent-dark), var(--accent)); color: #fff; }
.mg-offer h3 { font-family: Georgia, serif; font-size: 22px; margin: 0 0 6px; }
.mg-offer .mg-price { font-size: 13.5px; color: #FFF1D6; margin: 0 0 14px; }
.mg-offer ul { padding-left: 18px; margin: 0; font-size: 14.5px; line-height: 1.7; }

/* ===== Footer ===== */
.mg-footer-icons { display: flex; flex-wrap: wrap; gap: 12px; margin: 0 0 28px; }
.mg-footer-icons img { width: 52px; height: 52px; border-radius: 50%; display: block; }
.mg-footer p { color: #B8B6B0; font-size: 13.5px; line-height: 1.7; }
.mg-footer a:not(.mg-cta) { color: var(--amber-soft); }
.mg-footer .mg-legal { font-size: 12px; color: #8B8A85; margin-top: 24px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }

@media (max-width: 720px) {
  .mg-h1 { font-size: 36px; }
  .mg-example { grid-template-columns: 1fr; }
  .mg-section { padding: 56px 20px; }
  .mg-cta-ghost { margin: 14px 0 0; }
}

/* ===== Dernier numéro : porte d'entrée ===== */
.mg-band.mg-featured { background: var(--amber-pale); }
.mg-featured .mg-section { padding-top: 56px; padding-bottom: 56px; }
.mg-feature { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 28px; background: var(--navy); border-radius: 24px; padding: 40px 44px; text-decoration: none; color: #fff !important; box-shadow: 0 14px 40px rgba(15,23,42,.28); border-bottom: 8px solid var(--accent); transition: transform .15s ease, box-shadow .15s ease; }
.mg-feature:hover { transform: translateY(-3px); box-shadow: 0 20px 48px rgba(15,23,42,.34); }
.mg-feature-text { flex: 1 1 380px; }
.mg-feature-label { display: inline-block; background: var(--amber-soft); color: var(--navy); font-size: 12.5px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; padding: 6px 14px; border-radius: 999px; margin-bottom: 18px; }
.mg-feature-title { font-family: Georgia, "Times New Roman", serif; font-size: 34px; line-height: 1.15; margin: 0 0 14px; color: #fff; }
.mg-feature-lede { color: #CBD5E1; font-size: 17px; line-height: 1.55; margin: 0 0 24px; max-width: 52ch; }
.mg-feature-cta { display: inline-block; background: var(--accent); color: #fff; font-weight: 700; font-size: 18px; padding: 16px 30px; border-radius: 12px; }
.mg-feature:hover .mg-feature-cta { background: var(--amber-soft); color: var(--navy); }
.mg-feature-faces { flex: 0 1 280px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.mg-feature-faces img { width: 100%; height: auto; aspect-ratio: 1/1; border-radius: 50%; display: block; box-shadow: 0 0 0 3px var(--navy-2); }
.mg-who { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; font-family: Georgia, serif; font-weight: 700; font-size: 15px; color: var(--ink); }
.mg-who img { width: 44px; height: 44px; border-radius: 50%; display: block; flex: 0 0 auto; }
@media (max-width: 720px) { .mg-feature { padding: 28px 22px; } .mg-feature-title { font-size: 26px; } .mg-feature-faces { flex-basis: 100%; max-width: 280px; } }
.mg-dark .mg-cta-ghost.mg-cta-latest { background: var(--amber-soft); border-color: var(--amber-soft); color: var(--navy) !important; font-size: 16px; padding: 14px 26px; }
</style>

<!-- ============ 1. HERO (constellation) ============ -->
<div class="mg-band mg-dark">
<section class="mg-section mg-hero">
  <div class="mg-hero-text">
    <div class="mg-brand"><img src="/magnitude-icon.png" alt="">Magnitude</div><br>
    <span class="mg-pill">Apartisan · Présidentielle 2027</span>
    <h1 class="mg-h1">Un chiffre politique, <em>remis à l'échelle</em> — chaque semaine.</h1>
    <p class="mg-lede">
      Magnitude est une publication data qui apprend à lire les chiffres
      de la vie politique et citoyenne : un graphique, une histoire
      sourcée, pour chaque mesure qui fait l'actualité. Sans jargon, sans
      étiquette politique affichée. Angle d'actualité actuel : la
      présidentielle 2027.
    </p>
    <a class="mg-cta" href="https://buttondown.com/magnitude-publication">S'abonner gratuitement →</a>
    <a class="mg-cta-ghost mg-cta-latest" href="/numeros/1/numero-1.html">Lire le dernier numéro →</a>
  </div>
  <div class="mg-hero-art">
    <div>
      <div class="mg-orbit" role="img" aria-label="Constellation des douze candidats déclarés autour du logo Magnitude">
        <svg viewBox="0 0 520 520" aria-hidden="true">
          <circle cx="260" cy="260" r="240" fill="none" stroke="#1E293B" stroke-width="2"/>
          <circle cx="260" cy="260" r="170" fill="none" stroke="#1E293B" stroke-width="2"/>
          <circle cx="260" cy="260" r="100" fill="none" stroke="#334155" stroke-width="2"/>
          <g stroke="#475569" stroke-width="1.5">
            <line x1="260" y1="260" x2="260" y2="20"/><line x1="260" y1="260" x2="380" y2="52"/><line x1="260" y1="260" x2="468" y2="140"/><line x1="260" y1="260" x2="500" y2="260"/><line x1="260" y1="260" x2="468" y2="380"/><line x1="260" y1="260" x2="380" y2="468"/><line x1="260" y1="260" x2="260" y2="500"/><line x1="260" y1="260" x2="140" y2="468"/><line x1="260" y1="260" x2="52" y2="380"/><line x1="260" y1="260" x2="20" y2="260"/><line x1="260" y1="260" x2="52" y2="140"/><line x1="260" y1="260" x2="140" y2="52"/>
          </g>
        </svg>
        <!-- Ordre alphabétique, purement décoratif : aucun classement. -->
        <img class="mg-core" src="/magnitude-icon.png" alt="Logo Magnitude">
        <img class="mg-node" style="left:50.0%;top:3.8%" src="/candidats/attal.png" alt="Gabriel Attal">
        <img class="mg-node" style="left:73.1%;top:10.0%" src="/candidats/faure.png" alt="Olivier Faure">
        <img class="mg-node" style="left:90.0%;top:26.9%" src="/candidats/glucksmann.png" alt="Raphaël Glucksmann">
        <img class="mg-node" style="left:96.2%;top:50.0%" src="/candidats/le-pen.png" alt="Marine Le Pen">
        <img class="mg-node" style="left:90.0%;top:73.1%" src="/candidats/melenchon.png" alt="Jean-Luc Mélenchon">
        <img class="mg-node" style="left:73.1%;top:90.0%" src="/candidats/philippe.png" alt="Édouard Philippe">
        <img class="mg-node" style="left:50.0%;top:96.2%" src="/candidats/retailleau.png" alt="Bruno Retailleau">
        <img class="mg-node" style="left:26.9%;top:90.0%" src="/candidats/roussel.png" alt="Fabien Roussel">
        <img class="mg-node" style="left:10.0%;top:73.1%" src="/candidats/ruffin.png" alt="François Ruffin">
        <img class="mg-node" style="left:3.8%;top:50.0%" src="/candidats/tondelier.png" alt="Marine Tondelier">
        <img class="mg-node" style="left:10.0%;top:26.9%" src="/candidats/villepin.png" alt="Dominique de Villepin">
        <img class="mg-node" style="left:26.9%;top:10.0%" src="/candidats/zemmour.png" alt="Éric Zemmour">
      </div>
      <p class="mg-orbit-caption">Les douze candidats déclarés des deux premiers numéros, par ordre alphabétique — dessins stylisés, sans lien avec les couleurs des partis.</p>
    </div>
  </div>
</section>
</div>

<!-- ============ 1bis. DERNIER NUMÉRO (porte d'entrée) ============ -->
<div class="mg-band mg-featured">
<section class="mg-section">
  <a class="mg-feature" href="/numeros/1/numero-1.html" aria-label="Lire le dernier numéro : Numéro #1, six nouveaux candidats, six mesures, un seul chiffre à chaque fois">
    <div class="mg-feature-text">
      <span class="mg-feature-label">Dernier numéro · N° 1 · octobre 2026</span>
      <h2 class="mg-feature-title">Six nouveaux candidats, six mesures, un seul chiffre à chaque fois</h2>
      <p class="mg-feature-lede">Le numéro complet, prêt à lire : une carte par candidat déclaré, un graphique, une histoire sourcée. Le numéro #0 reste disponible dans l'historique.</p>
      <span class="mg-feature-cta">Lire le numéro #1 →</span>
    </div>
    <div class="mg-feature-faces" aria-hidden="true">
      <img src="/candidats/attal.png" alt=""><img src="/candidats/faure.png" alt=""><img src="/candidats/roussel.png" alt=""><img src="/candidats/ruffin.png" alt=""><img src="/candidats/villepin.png" alt=""><img src="/candidats/zemmour.png" alt="">
    </div>
  </a>
</section>
</div>

<!-- ============ 2. VISION / MANIFESTE ============ -->
<div class="mg-band mg-surface">
<section class="mg-section">
  <h2 class="mg-h2">Notre mission</h2>
  <p class="mg-quote">
    Magnitude est une communauté apartisane qui a pour but de
    démocratiser la pédagogie autour de l'analyse de données et de la
    compréhension des données par les citoyens, pour permettre à chacun
    de prendre des décisions éclairées en fonction de ses sensibilités. »
  </p>
  <h3 style="font-family:Georgia,serif; font-size:17px; margin:40px 0 4px;">Ce que Magnitude n'est pas</h3>
  <ul class="mg-not-list">
    <li>Un fact-checker de plus — on ne vérifie pas une déclaration isolée, on donne les clés pour la lire.</li>
    <li>Un agrégateur de sondages — on ne fait pas la course aux intentions de vote.</li>
    <li>Un média d'opinion — on ne dit jamais pour qui voter, ni ce qu'il faut penser d'une mesure.</li>
  </ul>
</section>
</div>

<!-- ============ 3. COMMENT ÇA MARCHE ============ -->
<div class="mg-band mg-dark">
<section class="mg-section">
  <h2 class="mg-h2">Comment ça marche</h2>
  <p class="mg-lede">
    Chaque numéro assemble jusqu'à 6 cartes, une par mesure de campagne
    qui fait l'actualité. Une carte, c'est toujours la même anatomie.
  </p>
  <div class="mg-steps">
    <div class="mg-step"><h3>La mesure</h3><p>Une mesure annoncée, citée mot pour mot, avec la source et la date de la déclaration du candidat.</p></div>
    <div class="mg-step"><h3>Le contexte</h3><p>Un graphique qui remet le chiffre en contexte, à la bonne échelle.</p></div>
    <div class="mg-step"><h3>L'analyse complète</h3><p>Le récit de la donnée derrière : sourcé, daté, avec son niveau de confiance affiché.</p></div>
  </div>
  <div class="mg-example">
    <a href="/numeros/0/reports/carte_03_philippe_fiscalite.html" style="display:block;" aria-label="Lire l'analyse complète : Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?"><img src="/numeros/0/charts/carte_03_philippe_fiscalite.png" alt="Impôts sur la production en % du PIB, France, UE à 27 et Allemagne, 2010-2024" loading="lazy"></a>
    <div>
      <div class="mg-tag">Centre-droit — Horizons</div>
      <h3><a href="/numeros/0/reports/carte_03_philippe_fiscalite.html" style="color:inherit; text-decoration:none;">Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?</a></h3>
      <p>Édouard Philippe propose de baisser les impôts de production en
      échange d'une baisse des aides aux entreprises. Ces impôts pèsent
      4,4 % du PIB en France, près de deux fois la moyenne européenne.</p>
      <a class="mg-more" href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Lire l'analyse complète →</a>
    </div>
  </div>
</section>
</div>

<!-- ============ 4. HISTORIQUE DES NUMÉROS ============ -->
<div class="mg-band">
<section class="mg-section" id="historique">
  <h2 class="mg-h2">Chercher une mesure précise</h2>
  <p class="mg-lede" style="font-size:15px;">
    Pour lire un numéro entier, commencez par <a href="/numeros/1/numero-1.html">le dernier numéro</a> (le <a href="/numeros/0/numero-0.html">numéro #0</a> reste disponible). Ici, toutes les cartes publiées, filtrables par thème et par famille
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
    <label class="mg-gauge" for="mg-filter-n">
      <span class="mg-gauge-label">Candidats ayant une position documentée : au moins <strong id="mg-n-value">0</strong></span>
      <input type="range" id="mg-filter-n" min="0" max="7" step="1" value="0" aria-label="Nombre minimum de candidats ayant une déclaration sur le sujet">
    </label>
    <select id="mg-filter-niveau" aria-label="Niveau de confiance pris en compte">
      <option value="ab">Niveaux A et B (publiables)</option>
      <option value="a">Niveau A seulement</option>
      <option value="abc">Niveaux A, B et C</option>
    </select>
    <select id="mg-sort" aria-label="Ordre d'affichage">
      <option value="desc">Plus de candidats d'abord</option>
      <option value="asc">Moins de candidats d'abord</option>
      <option value="tirage">Ordre de publication</option>
    </select>
  </div>
  <div class="mg-grid" id="mg-grid">
    <div class="mg-card" data-n-a="1" data-n-ab="5" data-n-abc="7" data-theme="Finances publiques" data-famille="Centre — Renaissance">
      <a class="mg-card-link" href="/numeros/1/reports/carte_07_attal_dette.html" aria-label="Lire l'analyse complète : Attal veut le zéro déficit en 2037 — la France affiche 5,1 % de déficit public en 2025"><img src="/numeros/1/charts/carte_07_attal_dette.png" alt="Attal veut le zéro déficit en 2037 — la France affiche 5,1 % de déficit public en 2025" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/attal.png" width="44" height="44" alt="Portrait stylisé de Gabriel Attal" loading="lazy"><span>Gabriel Attal</span></div>
        <span class="mg-tag">Centre — Renaissance</span><span class="mg-theme">Finances publiques</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_07_attal_dette.html">Attal veut le zéro déficit en 2037 — la France affiche 5,1 % de déficit public en 2025</a></h4>
        <a href="/numeros/1/reports/carte_07_attal_dette.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="0" data-n-ab="3" data-n-abc="6" data-theme="Salaires" data-famille="Gauche — PS">
      <a class="mg-card-link" href="/numeros/1/reports/carte_08_faure_smic.html" aria-label="Lire l'analyse complète : Faure veut porter le Smic à 1 700 € net — il est aujourd'hui de 1 478 € net"><img src="/numeros/1/charts/carte_08_faure_smic.png" alt="Faure veut porter le Smic à 1 700 € net — il est aujourd'hui de 1 478 € net" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/faure.png" width="44" height="44" alt="Portrait stylisé de Olivier Faure" loading="lazy"><span>Olivier Faure</span></div>
        <span class="mg-tag">Gauche — PS</span><span class="mg-theme">Salaires</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_08_faure_smic.html">Faure veut porter le Smic à 1 700 € net — il est aujourd'hui de 1 478 € net</a></h4>
        <a href="/numeros/1/reports/carte_08_faure_smic.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="1" data-n-ab="3" data-n-abc="5" data-theme="Sécurité" data-famille="Gauche — PCF">
      <a class="mg-card-link" href="/numeros/1/reports/carte_09_roussel_securite.html" aria-label="Lire l'analyse complète : Roussel veut embaucher 60 000 agents contre le narcotrafic — l'équivalent de 22 % des effectifs actuels"><img src="/numeros/1/charts/carte_09_roussel_securite.png" alt="Roussel veut embaucher 60 000 agents contre le narcotrafic — l'équivalent de 22 % des effectifs actuels" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/roussel.png" width="44" height="44" alt="Portrait stylisé de Fabien Roussel" loading="lazy"><span>Fabien Roussel</span></div>
        <span class="mg-tag">Gauche — PCF</span><span class="mg-theme">Sécurité</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_09_roussel_securite.html">Roussel veut embaucher 60 000 agents contre le narcotrafic — l'équivalent de 22 % des effectifs actuels</a></h4>
        <a href="/numeros/1/reports/carte_09_roussel_securite.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="1" data-n-ab="3" data-n-abc="3" data-theme="Vie associative" data-famille="Gauche — Debout !">
      <a class="mg-card-link" href="/numeros/1/reports/carte_10_ruffin_loisirs.html" aria-label="Lire l'analyse complète : Ruffin veut 1 Md€ par an pour les salles des fêtes — 81 % des crédits de la mission Sport, jeunesse et vie associative"><img src="/numeros/1/charts/carte_10_ruffin_loisirs.png" alt="Ruffin veut 1 Md€ par an pour les salles des fêtes — 81 % des crédits de la mission Sport, jeunesse et vie associative" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/ruffin.png" width="44" height="44" alt="Portrait stylisé de François Ruffin" loading="lazy"><span>François Ruffin</span></div>
        <span class="mg-tag">Gauche — Debout !</span><span class="mg-theme">Vie associative</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_10_ruffin_loisirs.html">Ruffin veut 1 Md€ par an pour les salles des fêtes — 81 % des crédits de la mission Sport, jeunesse et vie associative</a></h4>
        <a href="/numeros/1/reports/carte_10_ruffin_loisirs.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="1" data-n-ab="3" data-n-abc="3" data-theme="Innovation &amp; souveraineté" data-famille="Centre — La France humaniste">
      <a class="mg-card-link" href="/numeros/1/reports/carte_11_villepin_darpa.html" aria-label="Lire l'analyse complète : Villepin veut une DARPA européenne à 4 milliards de dollars par an — l'agence américaine en reçoit environ 4,3"><img src="/numeros/1/charts/carte_11_villepin_darpa.png" alt="Villepin veut une DARPA européenne à 4 milliards de dollars par an — l'agence américaine en reçoit environ 4,3" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/villepin.png" width="44" height="44" alt="Portrait stylisé de Dominique de Villepin" loading="lazy"><span>Dominique de Villepin</span></div>
        <span class="mg-tag">Centre — La France humaniste</span><span class="mg-theme">Innovation &amp; souveraineté</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_11_villepin_darpa.html">Villepin veut une DARPA européenne à 4 milliards de dollars par an — l'agence américaine en reçoit environ 4,3</a></h4>
        <a href="/numeros/1/reports/carte_11_villepin_darpa.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="0" data-n-ab="2" data-n-abc="2" data-theme="Immigration" data-famille="Extrême-droite — Reconquête">
      <a class="mg-card-link" href="/numeros/1/reports/carte_12_zemmour_immigration.html" aria-label="Lire l'analyse complète : Zemmour veut expulser les étrangers au chômage depuis un an — le chômage touche 12,4 % des immigrés, 7,7 % de la population"><img src="/numeros/1/charts/carte_12_zemmour_immigration.png" alt="Zemmour veut expulser les étrangers au chômage depuis un an — le chômage touche 12,4 % des immigrés, 7,7 % de la population" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/zemmour.png" width="44" height="44" alt="Portrait stylisé de Éric Zemmour" loading="lazy"><span>Éric Zemmour</span></div>
        <span class="mg-tag">Extrême-droite — Reconquête</span><span class="mg-theme">Immigration</span>
        <h4><a class="mg-card-link" href="/numeros/1/reports/carte_12_zemmour_immigration.html">Zemmour veut expulser les étrangers au chômage depuis un an — le chômage touche 12,4 % des immigrés, 7,7 % de la population</a></h4>
        <a href="/numeros/1/reports/carte_12_zemmour_immigration.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="1" data-n-ab="4" data-n-abc="5" data-theme="Fiscalité des entreprises" data-famille="Centre-droit — Horizons">
      <a class="mg-card-link" href="/numeros/0/reports/carte_03_philippe_fiscalite.html" aria-label="Lire l'analyse complète : Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?"><img src="/numeros/0/charts/carte_03_philippe_fiscalite.png" alt="Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/philippe.png" width="44" height="44" alt="Portrait stylisé de Édouard Philippe" loading="lazy"><span>Édouard Philippe</span></div>
        <span class="mg-tag">Centre-droit — Horizons</span><span class="mg-theme">Fiscalité des entreprises</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?</a></h4>
        <a href="/numeros/0/reports/carte_03_philippe_fiscalite.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="2" data-n-ab="5" data-n-abc="6" data-theme="Fiscalité &amp; patrimoine" data-famille="Centre-gauche — Place Publique">
      <a class="mg-card-link" href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html" aria-label="Lire l'analyse complète : Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres"><img src="/numeros/0/charts/carte_04_glucksmann_patrimoine.png" alt="Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/glucksmann.png" width="44" height="44" alt="Portrait stylisé de Raphaël Glucksmann" loading="lazy"><span>Raphaël Glucksmann</span></div>
        <span class="mg-tag">Centre-gauche — Place Publique</span><span class="mg-theme">Fiscalité & patrimoine</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html">Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres</a></h4>
        <a href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="4" data-n-ab="6" data-n-abc="6" data-theme="Institutions" data-famille="Droite — LR">
      <a class="mg-card-link" href="/numeros/0/reports/carte_02_retailleau_referendum.html" aria-label="Lire l'analyse complète : Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans"><img src="/numeros/0/charts/carte_02_retailleau_referendum.png" alt="Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/retailleau.png" width="44" height="44" alt="Portrait stylisé de Bruno Retailleau" loading="lazy"><span>Bruno Retailleau</span></div>
        <span class="mg-tag">Droite — LR</span><span class="mg-theme">Institutions</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_02_retailleau_referendum.html">Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans</a></h4>
        <a href="/numeros/0/reports/carte_02_retailleau_referendum.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="0" data-n-ab="5" data-n-abc="5" data-theme="Climat" data-famille="Gauche écologiste — Les Écologistes">
      <a class="mg-card-link" href="/numeros/0/reports/carte_05_tondelier_climat.html" aria-label="Lire l'analyse complète : Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme"><img src="/numeros/0/charts/carte_05_tondelier_climat.png" alt="Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/tondelier.png" width="44" height="44" alt="Portrait stylisé de Marine Tondelier" loading="lazy"><span>Marine Tondelier</span></div>
        <span class="mg-tag">Gauche écologiste — Les Écologistes</span><span class="mg-theme">Climat</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_05_tondelier_climat.html">Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme</a></h4>
        <a href="/numeros/0/reports/carte_05_tondelier_climat.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="3" data-n-ab="5" data-n-abc="5" data-theme="Logement" data-famille="Extrême-droite — RN">
      <a class="mg-card-link" href="/numeros/0/reports/carte_01_le_pen_logement.html" aria-label="Lire l'analyse complète : Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs"><img src="/numeros/0/charts/carte_01_le_pen_logement.png" alt="Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/le-pen.png" width="44" height="44" alt="Portrait stylisé de Marine Le Pen" loading="lazy"><span>Marine Le Pen</span></div>
        <span class="mg-tag">Extrême-droite — RN</span><span class="mg-theme">Logement</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_01_le_pen_logement.html">Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs</a></h4>
        <a href="/numeros/0/reports/carte_01_le_pen_logement.html">Lire l'analyse complète →</a>
      </div>
    </div>
    <div class="mg-card" data-n-a="4" data-n-ab="6" data-n-abc="6" data-theme="Institutions" data-famille="Extrême-gauche — LFI">
      <a class="mg-card-link" href="/numeros/0/reports/carte_06_melenchon_confiance.html" aria-label="Lire l'analyse complète : Mélenchon veut une VIe République — la confiance dans les institutions au plus bas"><img src="/numeros/0/charts/carte_06_melenchon_confiance.png" alt="Mélenchon veut une VIe République — la confiance dans les institutions au plus bas" loading="lazy"></a>
      <div class="mg-body">
        <div class="mg-who"><img src="/candidats/melenchon.png" width="44" height="44" alt="Portrait stylisé de Jean-Luc Mélenchon" loading="lazy"><span>Jean-Luc Mélenchon</span></div>
        <span class="mg-tag">Extrême-gauche — LFI</span><span class="mg-theme">Institutions</span>
        <h4><a class="mg-card-link" href="/numeros/0/reports/carte_06_melenchon_confiance.html">Mélenchon veut une VIe République — la confiance dans les institutions au plus bas</a></h4>
        <a href="/numeros/0/reports/carte_06_melenchon_confiance.html">Lire l'analyse complète →</a>
      </div>
    </div>
  </div>
  <p class="mg-empty" id="mg-empty" style="display:none;">Aucune carte ne correspond à ce filtre.</p>
</section>
</div>

<!-- ============ 5. QUI SOMMES-NOUS ============ -->
<div class="mg-band mg-surface">
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
</div>

<!-- ============ 6. CONFIANCE & MÉTHODE ============ -->
<div class="mg-band">
<section class="mg-section">
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
</div>

<!-- ============ 7. OFFRE ============ -->
<div class="mg-band mg-surface">
<section class="mg-section">
  <h2 class="mg-h2">L'offre</h2>
  <p class="mg-lede">Un récap hebdomadaire, complété par des éditions au fil de l'actualité électorale.</p>
  <div class="mg-offer-grid">
    <div class="mg-offer">
      <h3>Gratuit</h3>
      <p class="mg-price">Pour tout le monde, sans exception, dès le premier numéro</p>
      <ul>
        <li>Toutes les cartes (graphique + message)</li>
        <li>L'analyse complète de chaque carte, synthèse et récit approfondi</li>
        <li>L'historique complet des numéros</li>
      </ul>
    </div>
  </div>
</section>
</div>

<!-- ============ 8. FOOTER ============ -->
<div class="mg-band mg-dark-deep mg-footer">
<section class="mg-section">
  <div class="mg-footer-icons" aria-hidden="true">
    <img src="/candidats/attal.png" alt=""><img src="/candidats/faure.png" alt=""><img src="/candidats/glucksmann.png" alt=""><img src="/candidats/le-pen.png" alt=""><img src="/candidats/melenchon.png" alt=""><img src="/candidats/philippe.png" alt=""><img src="/candidats/retailleau.png" alt=""><img src="/candidats/roussel.png" alt=""><img src="/candidats/ruffin.png" alt=""><img src="/candidats/tondelier.png" alt=""><img src="/candidats/villepin.png" alt=""><img src="/candidats/zemmour.png" alt="">
  </div>
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
</div>

<script type="module">
// Les cartes du grid "historique des numéros" sont du HTML statique
// (voir ci-dessus), pas générées en JS : Observable Framework ne détecte
// au build que les images/liens présents dans le HTML statique. Ce script
// ne fait que filtrer (afficher/masquer) les cartes déjà dans le DOM.
// TODO (futur) : générer les cartes statiques depuis le pipeline Python.
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

const nRange = document.getElementById("mg-filter-n");
const nValue = document.getElementById("mg-n-value");
const niveauSelect = document.getElementById("mg-filter-niveau");
const sortSelect = document.getElementById("mg-sort");
cards.forEach((c, i) => { c.dataset.ordre = i; });
const niveauLabel = { a: "A", ab: "A ou B", abc: "A, B ou C" };
function render() {
  const theme = themeSelect.value;
  const famille = familleSelect.value;
  const key = "data-n-" + niveauSelect.value;
  nRange.max = Math.max(...cards.map(c => Number(c.getAttribute(key))));
  const nMin = Math.min(Number(nRange.value), Number(nRange.max));
  nRange.value = nMin;
  nValue.textContent = nMin;
  let visible = 0;
  cards.forEach(card => {
    const n = Number(card.getAttribute(key));
    card.querySelector(".mg-count")?.remove();
    const badge = document.createElement("span");
    badge.className = "mg-count";
    badge.textContent = n + " candidat" + (n > 1 ? "s" : "") + " · niveau " + niveauLabel[niveauSelect.value];
    card.querySelector(".mg-theme").after(badge);
    const match = (!theme || card.dataset.theme === theme) && (!famille || card.dataset.famille === famille) && n >= nMin;
    card.style.display = match ? "" : "none";
    if (match) visible++;
  });
  const mode = sortSelect.value;
  const sorted = [...cards].sort((a, b) => {
    if (mode === "tirage") return a.dataset.ordre - b.dataset.ordre;
    const d = Number(a.getAttribute(key)) - Number(b.getAttribute(key));
    return (mode === "desc" ? -d : d) || a.dataset.ordre - b.dataset.ordre;
  });
  sorted.forEach(c => grid.appendChild(c));
  empty.style.display = visible ? "none" : "block";
}
nRange.addEventListener("input", render);
niveauSelect.addEventListener("change", render);
sortSelect.addEventListener("change", render);
themeSelect.addEventListener("change", render);
familleSelect.addEventListener("change", render);
render();
</script>
