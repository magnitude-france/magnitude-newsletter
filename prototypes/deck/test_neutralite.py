"""Test de neutralité du score du deck (protocole INV-03, décision du 2026-10-15).

Usage (depuis la racine de magnitude-newsletter) :
    python3 prototypes/deck/test_neutralite.py [--n 20000] [--graine 42]

On simule des utilisateurs SANS opinion structurée : chacun a une propension
p ~ U(0, 1) à répondre « Aligné », puis tranche chaque carte au hasard avec
cette propension (sinon « Désaligné »). On compte qui sort n°1.

Trois lectures, sur les seules cartes « dans le score » (même règle que le deck) :
- « protocole INV-03 » : part d'accord = accords / positions documentées,
  égalités réparties, sans seuil minimal de cartes (comme le test du 16/10) ;
- « règles du deck » : ce que voit l'utilisateur — seuil de MIN_N cartes,
  candidats qui ne sont plus en lice exclus, galaxie seulement si un
  candidat est strictement en tête (sinon « le deck hésite ») ;
- « règles du deck avec priorités » (2026-10-30) : mêmes règles, mais chaque
  utilisateur simulé choisit au hasard 0 à MAX_PRIO thèmes prioritaires parmi
  ceux de l'écran « Vos priorités » ; une carte prioritaire pèse W_PRIO et un
  candidat sans position documentée sur elle prend PEN × W_PRIO au dénominateur.
Critère : aucun candidat n°1 chez plus de 1,5 fois ni moins de 0,5 fois la
part neutre (1 / nombre de candidats en lice).
Aucune dépendance hors bibliothèque standard Python.
"""
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

from build_deck import THEMES_ATTENDUS

HERE = Path(__file__).resolve().parent
N = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 20000
GRAINE = int(sys.argv[sys.argv.index("--graine") + 1]) if "--graine" in sys.argv else 42
MIN_N = 4  # même valeur que deck-template.html
W_PRIO, PEN, MAX_PRIO = 2, 0.5, 5  # idem (priorités, 2026-10-30)


def main():
    data = json.loads((HERE / "deck-data.json").read_text(encoding="utf-8"))
    cands = sorted(data["cands"])
    en_lice = [s for s in cands if (data["cands"][s].get("statut") or {}).get("kind") != "retire"]
    sd, sa = math.ceil(2 * len(cands) / 3), math.ceil(len(cands) / 2)

    def dans_score(c):
        ks = c["pos"]
        return len(ks) >= sd and sum(1 for v in ks.values() if v[1] in ("A", "B")) >= sa

    cartes = [c for c in data["cards"] if dans_score(c)]
    rng = random.Random(GRAINE)
    inv03, deck, hesite = Counter(), Counter(), 0
    for _ in range(N):
        p = rng.random()
        choix = [1 if rng.random() < p else -1 for _ in cartes]
        acc, n = Counter(), Counter()
        for c, ch in zip(cartes, choix):
            for s, v in c["pos"].items():
                n[s] += 1
                acc[s] += v[0] == ch
        pct = {s: acc[s] / n[s] for s in cands if n[s]}
        best = max(pct.values())
        top = [s for s in pct if math.isclose(pct[s], best)]
        for s in top:
            inv03[s] += 1 / len(top)
        elig = sorted((s for s in en_lice if n[s] >= MIN_N), key=lambda s: -pct[s])
        if elig and (len(elig) == 1 or pct[elig[0]] > pct[elig[1]]):
            deck[elig[0]] += 1
        else:
            hesite += 1

    # Avec priorités : tirage séparé (même graine), pour garder les deux lectures précédentes inchangées.
    themes = sorted({c["theme"] for c in data["cards"]} | set(THEMES_ATTENDUS))
    rng = random.Random(GRAINE)
    prio_deck, prio_hesite = Counter(), 0
    for _ in range(N):
        p = rng.random()
        choix = [1 if rng.random() < p else -1 for _ in cartes]
        prio = set(rng.sample(themes, rng.randint(0, MAX_PRIO)))
        wa, wn, n = Counter(), Counter(), Counter()
        for c, ch in zip(cartes, choix):
            w = W_PRIO if c["theme"] in prio else 1
            for s in cands:
                v = c["pos"].get(s)
                if v:
                    n[s] += 1
                    wn[s] += w
                    wa[s] += w * (v[0] == ch)
                elif c["theme"] in prio:
                    wn[s] += PEN * w  # silence sur une priorité : demi-désaccord
        pct = {s: wa[s] / wn[s] for s in cands if n[s]}
        elig = sorted((s for s in en_lice if n[s] >= MIN_N), key=lambda s: -pct[s])
        if elig and (len(elig) == 1 or pct[elig[0]] > pct[elig[1]]):
            prio_deck[elig[0]] += 1
        else:
            prio_hesite += 1

    def verdict(parts, k):
        lo, hi = 50 / k, 150 / k
        hors = {s: v for s, v in parts.items() if not lo <= v <= hi}
        return lo, hi, hors

    nom = lambda s: data["cands"][s]["name"]
    out = {"cartes_dans_le_score": [c["n"] for c in cartes], "seuils": f"{sd}/{sa} sur {len(cands)}", "n": N, "graine": GRAINE}
    p1 = {s: 100 * inv03[s] / N for s in cands}
    lo, hi, hors = verdict(p1, len(cands))
    out["protocole_inv03"] = {"bornes": [round(lo, 1), round(hi, 1)], "parts": {nom(s): round(v, 1) for s, v in sorted(p1.items(), key=lambda x: -x[1])},
                              "hors_bornes": {nom(s): round(v, 1) for s, v in hors.items()}, "resultat": "réussi" if not hors else "échec"}
    gal = N - hesite
    p2 = {s: 100 * deck[s] / gal for s in en_lice} if gal else {}
    lo, hi, hors = verdict(p2, len(en_lice))
    out["regles_du_deck"] = {"sans_galaxie_pct": round(100 * hesite / N, 1), "bornes_parmi_galaxies": [round(lo, 1), round(hi, 1)],
                             "parts_parmi_galaxies": {nom(s): round(v, 1) for s, v in sorted(p2.items(), key=lambda x: -x[1])},
                             "hors_bornes": {nom(s): round(v, 1) for s, v in hors.items()}, "resultat": "réussi" if not hors else "échec"}
    gal = N - prio_hesite
    p3 = {s: 100 * prio_deck[s] / gal for s in en_lice} if gal else {}
    lo, hi, hors = verdict(p3, len(en_lice))
    out["regles_du_deck_avec_priorites"] = {"sans_galaxie_pct": round(100 * prio_hesite / N, 1), "bornes_parmi_galaxies": [round(lo, 1), round(hi, 1)],
                                            "parts_parmi_galaxies": {nom(s): round(v, 1) for s, v in sorted(p3.items(), key=lambda x: -x[1])},
                                            "hors_bornes": {nom(s): round(v, 1) for s, v in hors.items()}, "resultat": "réussi" if not hors else "échec"}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if all(out[k]["resultat"] == "réussi" for k in ("protocole_inv03", "regles_du_deck", "regles_du_deck_avec_priorites")) else 1


if __name__ == "__main__":
    sys.exit(main())
