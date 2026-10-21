"""Construit le prototype autonome du Deck « Find your Candidate ».

Usage (depuis la racine du repo magnitude-newsletter) :
    python3 prototypes/deck/build_deck.py

Entrées :
- prototypes/deck/deck-data.json  (extrait de magnitude-analysis/data/analyses/*.json
  et des pages de numéro publiées ; voir README.md)
- src/candidats/*.png               (portraits stylisés existants, inchangés)
- prototypes/deck/deck-template.html
Sortie :
- prototypes/deck/deck.html         (fichier unique, autonome, aucune requête réseau)

Aucune dépendance hors bibliothèque standard Python.
"""
import base64
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# Chiffre-clé (« point de force ») de chaque carte : repris mot pour mot des
# résumés publiés des cartes (magnitude-analysis/data/analyses/*.json, champ
# resume), donc déjà sourcés dans l'analyse complète correspondante.
FIGURES = {
    "01": ("56–58 %", "de propriétaires occupants, quasi stable depuis 2001"),
    "02": ("10", "référendums en 68 ans de Ve République, aucun depuis 2005"),
    "03": ("2ᵉ", "rang de la France dans l'UE pour le poids des impôts de production"),
    "04": ("45 %", "taux marginal des droits de succession en France (30 % en Allemagne)"),
    "05": ("−4,5 %/an", "baisse d'émissions nécessaire pour 2030 ; la France fait −1,5 à −1,8 %/an"),
    "06": ("20 %", "des Français font confiance à l'Assemblée nationale (janvier 2026)"),
    "07": ("5,1 %", "de déficit public en 2025, contre 3,1 % en moyenne dans l'UE"),
    "08": ("+15 %", "de Smic net : de 1 478 € à 1 700 € par mois"),
    "09": ("22 %", "des effectifs actuels de police, gendarmerie et douane"),
    "10": ("1 Md€/an", "pendant cinq ans pour les salles des fêtes et maisons du peuple"),
    "11": ("4 Md$/an", "pour une DARPA européenne (la DARPA américaine : ~4,3 Md$)"),
    "12": ("12,4 %", "de chômage chez les immigrés (2025), contre 7,7 % pour tous"),
}

ICONS = {  # pictogrammes génériques, tracés à la main (24×24, trait)
    "01": "M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6",
    "02": "M4 11h16v9H4zM8 11V4h8v7M10 7h4M9 15h6",
    "03": "M3 20V10l5 3v-3l5 3V7l8 4v9zM3 20h18M7 17h2M12 17h2M17 17h2",
    "04": "M4 10h16v10H4zM4 10l2-5h12l2 5M12 13v3M10 13h4",
    "05": "M5 19C5 10 11 5 20 4c-1 9-6 15-15 15zM5 19l7-7",
    "06": "M3 9l9-5 9 5M5 9v9M9.5 9v9M14.5 9v9M19 9v9M3 20h18",
    "07": "M3 4v16h18M6 8l4 4 3-3 6 6M19 11v4h-4",
    "08": "M6 7c0-1.1 2.7-2 6-2s6 .9 6 2-2.7 2-6 2-6-.9-6-2zM6 7v4c0 1.1 2.7 2 6 2s6-.9 6-2V7M6 11v4c0 1.1 2.7 2 6 2s6-.9 6-2v-4",
    "09": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4",
    "10": "M3 20V9l9-5 9 5v11M3 20h18M8 20v-5h8v5M6 9.5c2 2 4 2 6 0 2 2 4 2 6 0",
    "11": "M9 3h6M10 3v6L5 19a1 1 0 0 0 1 1.5h12A1 1 0 0 0 19 19l-5-10V3M7.5 14h9",
    "12": "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9S9.5 5.5 12 3z",
}

# Teintes de maison : palette propre à Magnitude (tons « parfum », aucune
# couleur de parti), attribuée par TIRAGE AU SORT DÉTERMINISTE CONTRAINT :
# graine publique « magnitude-2027 », on garde la première permutation où
# aucun candidat ne reçoit une teinte proche des couleurs associées à son
# parti. Provisoire — la règle des couleurs est à trancher en comité.
TONES = [("Ardoise", 240), ("Encre", 265), ("Iris", 290), ("Bruyère", 315),
         ("Prune", 340), ("Rose thé", 5), ("Corail", 30), ("Cèdre", 55),
         ("Ocre", 80), ("Olive", 105), ("Lichen", 130), ("Sauge", 155)]
FORBID = {
    "le-pen": {"Ardoise", "Encre"}, "retailleau": {"Ardoise", "Encre"},
    "zemmour": {"Ardoise", "Encre"}, "philippe": {"Ardoise"},
    "tondelier": {"Olive", "Lichen", "Sauge"},
    "melenchon": {"Prune", "Rose thé", "Corail"}, "roussel": {"Prune", "Rose thé", "Corail"},
    "faure": {"Prune", "Rose thé", "Corail"}, "glucksmann": {"Prune", "Rose thé", "Corail"},
    "ruffin": {"Rose thé", "Corail"}, "attal": {"Ocre"},
}


def draw_tones(cands):
    rng = random.Random("magnitude-2027")
    while True:
        perm = TONES[:]
        rng.shuffle(perm)
        m = dict(zip(cands, perm))
        if all(m[c][0] not in FORBID.get(c, set()) for c in cands):
            return m


def main():
    data = json.loads((HERE / "deck-data.json").read_text(encoding="utf-8"))
    cands = sorted(data["cands"])
    tones = draw_tones(cands)
    for slug in cands:
        png = (ROOT / "src" / "candidats" / f"{slug}.png").read_bytes()
        data["cands"][slug]["img"] = "data:image/png;base64," + base64.b64encode(png).decode()
        data["cands"][slug]["tone"] = tones[slug][0]
        data["cands"][slug]["hue"] = tones[slug][1]
    for card in data["cards"]:
        n = card["n"]
        card["fig"], card["fig_label"] = FIGURES[n]
        card["icon"] = ICONS[n]
    tpl = (HERE / "deck-template.html").read_text(encoding="utf-8")
    # Polices du registre (SIL OFL, voir fonts/) intégrées : aucune requête réseau.
    faces = []
    for fam, fichier, style in [("IM Fell English", "im-fell-english-latin-400-normal.woff2", "normal"),
                                ("IM Fell English", "im-fell-english-latin-400-italic.woff2", "italic"),
                                ("La Belle Aurore", "la-belle-aurore-latin-400-normal.woff2", "normal")]:
        b64 = base64.b64encode((HERE / "fonts" / fichier).read_bytes()).decode()
        faces.append(f'@font-face {{ font-family: "{fam}"; font-style: {style}; font-weight: 400; font-display: swap; src: url(data:font/woff2;base64,{b64}) format("woff2"); }}')
    tpl = tpl.replace("/*__FONTS__*/", "\n".join(faces))
    out = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    (HERE / "deck.html").write_text(out, encoding="utf-8")
    print(f"deck.html : {len(out) // 1024} Ko, {len(data['cards'])} cartes, {len(cands)} candidats")


if __name__ == "__main__":
    main()
