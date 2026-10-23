"""Ajoute (ou met à jour) dans deck-data.json les cartes d'un numéro.

Usage (depuis la racine de magnitude-newsletter) :
    python3 prototypes/deck/ajout_numero.py 2 [chemin/vers/magnitude-analysis] [--semaine 45]

Entrées (magnitude-analysis, mêmes sources que les pages de numéro) :
- data/analyses/carte_*.json : mesure, pôles et positions documentées des candidats ;
- scripts/lib/numeros.py      : titre, message et famille de chaque carte ;
- data/declarations.csv       : citation du candidat qui porte la mesure (ordre 1).
Les fiches anonymes « Comprendre la mesure » viennent d'extract_fiches.py ; le
chiffre-clé et le pictogramme de chaque carte sont dans build_deck.py.
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
NUM = int(args[0])
ANALYSIS = Path(args[1]) if len(args) > 1 else HERE.parents[2] / "magnitude-analysis"
SEMAINE = int(sys.argv[sys.argv.index("--semaine") + 1]) if "--semaine" in sys.argv else None

# Thème court affiché sur la carte (recto anonyme : jamais de nom de candidat).
THEMES = {"13": "Retraites", "14": "École", "15": "Énergie", "16": "Défense",
          "17": "Temps de travail", "18": "Fonction publique"}
# Candidats entrés dans le suivi après le numéro #1 : libellé de famille politique.
NOUVEAUX = {"lisnard": {"name": "David Lisnard", "tag": "Droite — Nouvelle Énergie"}}

sys.path.insert(0, str(ANALYSIS / "scripts"))
from lib import numeros  # noqa: E402


def citation(stem, nom):
    with open(ANALYSIS / "data" / "declarations.csv", encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["carte_id"] == stem and r["candidat"] == nom]
    rows.sort(key=lambda r: int(r.get("ordre") or 99))
    return "« " + rows[0]["verbatim"].strip().strip("«» ") + " »" if rows else ""


def main():
    path = HERE / "deck-data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for slug, c in NOUVEAUX.items():
        data["cands"].setdefault(slug, c)
    cards = {c["id"]: c for c in data["cards"]}
    for meta in numeros.cartes(NUM):
        stem = meta["deep_dive_url"].split("/")[-1][:-5]
        n = stem.split("_")[1]
        a = json.loads((ANALYSIS / "data" / "analyses" / f"{stem}.json").read_text(encoding="utf-8"))
        spec = a["candidats"]
        cid = spec.get("critere_mesure") or spec["dimensions"][0]["id"]
        dim = next(d for d in spec["dimensions"] if d["id"] == cid)
        pos = {}
        for slug, par_dim in spec["positions"].items():
            p = par_dim.get(cid)
            if p and p.get("v") in (1, -1):
                pos[slug] = [p["v"], p["niveau"]] + (["c"] if p.get("pole") == "c" else [])
        centre = a["centre"]
        nom = data["cands"][centre]["name"]
        card = {"id": stem, "n": n, "num": str(NUM), "theme": THEMES[n], "centre": centre,
                "mesure": spec["mesure"], "pole_a": dim["pole_a"], "pole_b": dim["pole_b"],
                "fig": "", "fig_label": "", "title": meta["titre"], "message": meta["message"],
                "quote": citation(stem, nom),
                "url": f"https://magnitude.pub/numeros/{NUM}/reports/{stem}.html", "pos": pos}
        if dim.get("pole_c"):
            card["pole_c"] = dim["pole_c"]
        cards[stem] = card
        print(n, centre, len(pos), "positions", "| citation" if card["quote"] else "| SANS citation")
    data["cards"] = sorted(cards.values(), key=lambda c: c["n"])
    if SEMAINE:
        data["semaine"] = SEMAINE
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
