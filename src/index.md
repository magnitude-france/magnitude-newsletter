---
toc: false
sidebar: false
---

<style>
/* Magnitude — accueil mobile d'abord. Fond teal (apaisement, neutralité) ; liens cliquables en bleu.
   Jamais de couleurs de partis : les couleurs des icônes de candidats sont décoratives. */
:root {
  --accent:#D97706; --amber-soft:#FBBF24; --amber-pale:#FEF3C7;
  --teal-900:#0B4A52; --teal-800:#0F5F66; --teal-700:#137A7F; --teal-200:#BFE6E3; --teal-100:#DDF2F0; --teal-50:#EEF8F7;
  --link:#0A58CA; --ink:#0B1F22; --ink-secondary:#3E5558; --ink-muted:#5F7679; --page:#F1F8F8; --border:rgba(11,74,82,.12);
  --serif: Georgia,"Times New Roman",serif;
}
.observablehq main { max-width:none !important; padding:0 !important; margin:0 !important; }
.observablehq-header, .observablehq-footer { display:none !important; }
body { background:var(--page); color:var(--ink); font:16px/1.55 -apple-system,"Helvetica Neue",Arial,sans-serif; }
.mg-wrap { max-width:640px; margin:0 auto; padding:0 16px; }
.mg-hero { background:var(--teal-900); color:#E6F6F5; padding:22px 0 34px; }
.mg-brand { display:inline-flex; align-items:center; gap:10px; font:700 15px var(--serif); letter-spacing:.14em; text-transform:uppercase; color:#fff; margin-bottom:22px; }
.mg-brand img { width:34px; height:34px; border-radius:8px; }
.mg-pill { display:inline-block; border:1px solid var(--amber-soft); color:var(--amber-soft); font-size:12px; font-weight:700; letter-spacing:.1em; text-transform:uppercase; padding:5px 12px; border-radius:999px; margin-bottom:14px; }
.mg-h1 { font:700 32px/1.15 var(--serif); color:#fff; margin:0 0 12px; }
.mg-h1 em { font-style:normal; color:var(--amber-soft); }
.mg-lede { color:#CFE9E7; margin:0 0 20px; font-size:16.5px; }
.mg-cta { display:block; text-align:center; background:var(--accent); color:#fff !important; text-decoration:none; font-weight:700; font-size:17px; padding:15px 20px; border-radius:16px; }
.mg-h2 { font:700 22px var(--serif); margin:34px 0 14px; }
/* Carte « une » façon App Store */
.mg-feature { display:block; text-decoration:none; color:inherit; background:#fff; border-radius:26px; overflow:hidden; box-shadow:0 10px 30px rgba(11,74,82,.16),0 1px 3px rgba(11,74,82,.1); margin-top:-18px; position:relative; }
.mg-feature-faces { display:grid; grid-template-columns:repeat(6,1fr); gap:0; background:var(--teal-100); padding:16px 12px 8px; }
.mg-feature-faces img { width:100%; max-width:52px; aspect-ratio:1; border-radius:50%; margin:0 auto; display:block; box-shadow:0 0 0 3px #fff; }
.mg-feature-body { padding:16px 20px 22px; }
.mg-feature-label { font-size:12px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-muted); }
.mg-feature-title { font:700 23px/1.25 var(--serif); margin:6px 0 8px; }
.mg-feature-lede { color:var(--ink-secondary); margin:0 0 14px; font-size:15.5px; }
.mg-feature-cta { display:block; text-align:center; font-weight:700; color:var(--link); border:2px solid var(--link); border-radius:14px; padding:12px; }
.mg-mini { display:flex; gap:14px; align-items:center; background:#fff; border-radius:20px; padding:14px 16px; text-decoration:none; color:inherit; box-shadow:0 1px 4px rgba(11,74,82,.12); margin-top:14px; }
.mg-mini b { font:700 16px/1.3 var(--serif); display:block; }
.mg-mini span.s { font-size:13.5px; color:var(--ink-secondary); }
.mg-mini .go { margin-left:auto; color:var(--link); font-weight:700; font-size:22px; }
.mg-tagrow { font-size:11.5px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:#92400E; background:var(--amber-pale); border-radius:999px; display:inline-block; padding:2px 10px; margin-bottom:6px; }
.mg-list { display:grid; gap:10px; }
.mg-row { display:flex; gap:12px; align-items:center; background:#fff; border-radius:18px; padding:12px 14px; text-decoration:none; color:inherit; box-shadow:0 1px 4px rgba(11,74,82,.12); }
.mg-row img { width:48px; height:48px; border-radius:50%; flex:none; }
.mg-row-t { display:flex; flex-direction:column; }
.mg-row-t b { font:700 15px var(--serif); }
.mg-row-title { color:var(--link); font-size:14.5px; line-height:1.35; margin:2px 0; }
.mg-row-s { font-size:12px; color:var(--ink-muted); }
.mg-note { font-size:13px; color:var(--ink-muted); margin:12px 0 0; }
.mg-note a, .mg-about a { color:var(--link); }
.mg-about { background:#fff; border-radius:22px; padding:6px 18px 18px; box-shadow:0 1px 4px rgba(11,74,82,.12); }
.mg-about p, .mg-about li { color:var(--ink-secondary); }
.mg-quote { font:italic 19px/1.5 var(--serif); color:var(--ink); margin:14px 0; }
details.mg-d { border-top:1px solid var(--border); padding:12px 0; }
details.mg-d summary { font-weight:700; cursor:pointer; }
details.mg-d p { margin:8px 0 0; }
.mg-footer { background:var(--teal-900); color:#CFE9E7; margin-top:40px; padding:30px 0 40px; text-align:center; }
.mg-footer h2 { font:700 22px var(--serif); color:#fff; margin:0 0 6px; }
.mg-footer a:not(.mg-cta) { color:#9FD8FF; }
.mg-legal { font-size:12px; color:#9CC9C6; margin-top:24px; }
</style>

<div class="mg-hero"><div class="mg-wrap">
  <div class="mg-brand"><img src="/magnitude-icon.png" alt="">Magnitude</div><br>
  <span class="mg-pill">Apartisan · Présidentielle 2027</span>
  <h1 class="mg-h1">Un chiffre politique, <em>remis à l'échelle</em> — chaque semaine.</h1>
  <p class="mg-lede">Un graphique et une histoire sourcée pour chaque mesure qui fait l'actualité. Sans jargon, sans étiquette politique.</p>
  <a class="mg-cta" href="https://lists.magnitude.pub/subscription/form">S'abonner gratuitement →</a>
</div></div>

<div class="mg-wrap">
  <a class="mg-feature" href="/numeros/1/numero-1.html" aria-label="Lire le dernier numéro : Numéro #1, six nouveaux candidats, six mesures, un seul chiffre à chaque fois">
    <div class="mg-feature-faces" aria-hidden="true"><img src="/candidats/attal.png" alt=""><img src="/candidats/faure.png" alt=""><img src="/candidats/roussel.png" alt=""><img src="/candidats/ruffin.png" alt=""><img src="/candidats/villepin.png" alt=""><img src="/candidats/zemmour.png" alt=""></div>
    <div class="mg-feature-body">
      <span class="mg-feature-label">Dernier numéro · N° 1 · octobre 2026</span>
      <h2 class="mg-feature-title">Six nouveaux candidats, six mesures, un seul chiffre à chaque fois</h2>
      <p class="mg-feature-lede">Une carte par candidat : à faire glisser, à toucher pour l'ouvrir en grand.</p>
      <span class="mg-feature-cta">Lire le numéro #1 →</span>
    </div>
  </a>
  <a class="mg-mini" href="/numeros/0/numero-0.html"><div><b>Numéro #0</b><span class="s">Six mesures, six familles politiques</span></div><span class="go">›</span></a>
  <a class="mg-mini" href="/editions-speciales/repression-lyceenne/analyse.html"><div><span class="mg-tagrow">Édition spéciale · octobre 2026</span><b>La mobilisation lycéenne, replacée parmi d'autres mouvements</b><span class="s">1 747 interpellations annoncées en une journée, comparées à d'autres mobilisations.</span></div><span class="go">›</span></a>

  <h2 class="mg-h2" id="historique">Toutes les cartes</h2>
  <div class="mg-list">
    <a class="mg-row" href="/numeros/1/reports/carte_07_attal_dette.html"><img src="/candidats/attal.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Gabriel Attal</b><span class="mg-row-title">Attal veut le zéro déficit en 2037 — la France affiche 5,1 % de déficit public en 2025</span><span class="mg-row-s">Finances publiques</span></span></a>
    <a class="mg-row" href="/numeros/1/reports/carte_08_faure_smic.html"><img src="/candidats/faure.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Olivier Faure</b><span class="mg-row-title">Faure veut porter le Smic à 1 700 € net — il est aujourd'hui de 1 478 € net</span><span class="mg-row-s">Salaires</span></span></a>
    <a class="mg-row" href="/numeros/1/reports/carte_09_roussel_securite.html"><img src="/candidats/roussel.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Fabien Roussel</b><span class="mg-row-title">Roussel veut embaucher 60 000 agents contre le narcotrafic — l'équivalent de 22 % des effectifs actuels</span><span class="mg-row-s">Sécurité</span></span></a>
    <a class="mg-row" href="/numeros/1/reports/carte_10_ruffin_loisirs.html"><img src="/candidats/ruffin.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>François Ruffin</b><span class="mg-row-title">Ruffin veut 1 Md€ par an pour les salles des fêtes — 81 % des crédits de la mission Sport, jeunesse et vie associative</span><span class="mg-row-s">Vie associative</span></span></a>
    <a class="mg-row" href="/numeros/1/reports/carte_11_villepin_darpa.html"><img src="/candidats/villepin.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Dominique de Villepin</b><span class="mg-row-title">Villepin veut une DARPA européenne à 4 milliards de dollars par an — l'agence américaine en reçoit environ 4,3</span><span class="mg-row-s">Innovation &amp; souveraineté</span></span></a>
    <a class="mg-row" href="/numeros/1/reports/carte_12_zemmour_immigration.html"><img src="/candidats/zemmour.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Éric Zemmour</b><span class="mg-row-title">Zemmour veut expulser les étrangers au chômage depuis un an — le chômage touche 12,4 % des immigrés, 7,7 % de la population</span><span class="mg-row-s">Immigration</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_03_philippe_fiscalite.html"><img src="/candidats/philippe.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Édouard Philippe</b><span class="mg-row-title">Philippe propose un « deal fiscal » aux entreprises — où en sont les impôts de production ?</span><span class="mg-row-s">Fiscalité des entreprises</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_04_glucksmann_patrimoine.html"><img src="/candidats/glucksmann.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Raphaël Glucksmann</b><span class="mg-row-title">Glucksmann veut taxer les « méga-héritages » — la concentration du patrimoine en 3 chiffres</span><span class="mg-row-s">Fiscalité & patrimoine</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_02_retailleau_referendum.html"><img src="/candidats/retailleau.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Bruno Retailleau</b><span class="mg-row-title">Retailleau veut élargir le référendum — la France n'en a pas organisé depuis 21 ans</span><span class="mg-row-s">Institutions</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_05_tondelier_climat.html"><img src="/candidats/tondelier.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Marine Tondelier</b><span class="mg-row-title">Tondelier veut surtaxer les plus gros héritages pour la transition — l'ampleur du décrochage de rythme</span><span class="mg-row-s">Climat</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_01_le_pen_logement.html"><img src="/candidats/le-pen.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Marine Le Pen</b><span class="mg-row-title">Le Pen veut faciliter l'achat d'un premier logement — le vrai décrochage est ailleurs</span><span class="mg-row-s">Logement</span></span></a>
    <a class="mg-row" href="/numeros/0/reports/carte_06_melenchon_confiance.html"><img src="/candidats/melenchon.png" width="48" height="48" alt="" loading="lazy"><span class="mg-row-t"><b>Jean-Luc Mélenchon</b><span class="mg-row-title">Mélenchon veut une VIe République — la confiance dans les institutions au plus bas</span><span class="mg-row-s">Institutions</span></span></a>
  </div>
  <p class="mg-note">Dans chaque numéro, l'onglet <a href="/numeros/1/numero-1.html#recherche">Recherche</a> permet de trouver une carte par candidat ou par thème. L'ordre est tiré au sort à chaque numéro (<a href="/charte-selection-sujets.html">méthode publique</a>) : ce n'est pas un classement.</p>

  <h2 class="mg-h2" id="qui-sommes-nous">Qui sommes-nous</h2>
  <div class="mg-about">
    <p class="mg-quote">« Magnitude est une communauté apartisane qui a pour but de démocratiser la pédagogie autour de l'analyse de données, pour permettre à chacun de prendre des décisions éclairées en fonction de ses sensibilités. »</p>
    <p>Une petite équipe indépendante, sans attache partisane : ni journalistes encartés, ni militants — des praticiens de la donnée.</p>
    <details class="mg-d"><summary>Symétrie de traitement</summary><p>Chaque famille politique représentée par un candidat déclaré reçoit, sur la durée, un traitement comparable en fréquence et en longueur.</p></details>
    <details class="mg-d"><summary>Sourcing systématique</summary><p>Chaque chiffre est associé à sa source primaire nommée, sa date d'extraction, un lien vérifiable et un niveau de confiance affiché.</p></details>
    <details class="mg-d"><summary>Ordre tiré au sort</summary><p>La position des cartes dans un numéro est calculée par un tirage pseudo-aléatoire déterministe, jamais choisie à la main.</p></details>
    <details class="mg-d"><summary>Ce que Magnitude n'est pas</summary><p>Ni un fact-checker de plus, ni un agrégateur de sondages, ni un média d'opinion : on ne dit jamais pour qui voter, ni quoi penser d'une mesure.</p></details>
    <details class="mg-d"><summary>Financement</summary><p>Publicité non partisane uniquement — jamais de subvention publique. Magnitude est gratuite : aucun contenu payant.</p></details>
    <p><a href="/charte-ton-style.html">Charte de ton et de style</a> · <a href="/charte-selection-sujets.html">Charte de sélection des sujets</a></p>
  </div>
</div>

<div class="mg-footer"><div class="mg-wrap">
  <h2>Rejoindre Magnitude</h2>
  <p>Un email par semaine, pas plus. Désinscription en un clic.</p>
  <a class="mg-cta" href="https://lists.magnitude.pub/subscription/form">S'abonner gratuitement →</a>
  <p style="margin-top:22px;">Suivez Magnitude sur <a href="https://x.com/magnitudefrance" target="_blank" rel="noopener">X (@magnitudefrance)</a>.</p>
  <p class="mg-legal">Magnitude — publication indépendante, magnitude.pub. Gratuite, sans contenu payant. Financement privé uniquement (publicité non partisane) — aucune subvention publique ni partisane. © 2026.</p>
</div></div>
