"""Extrait, pour chaque carte, une fiche « Comprendre la mesure » ANONYME.

Usage (depuis la racine de magnitude-newsletter) :
    python3 prototypes/deck/extract_fiches.py [chemin/vers/magnitude-analysis]

Entrées (magnitude-analysis, déjà sourcées et relues) :
- data/analyses/carte_*.json : résumés « récit » et « Europe », chiffres clés,
  classement européen ;
- scripts/cards/carte_*.py   : liens d'origine (institutions et statistiques).
Sortie : clé "fiches" de prototypes/deck/deck-data.json.

Règle (décision de Guilhem, 2026-10-15) : la fiche se lit AVANT le choix, donc
elle ne contient ni nom de candidat ni de parti, ni position de candidat.
Toute phrase qui en mentionne un est retirée ; le script échoue s'il en reste.
"""
import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ANALYSIS = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parents[2] / "magnitude-analysis"

INTERDITS = ["Attal", "Faure", "Glucksmann", "Le Pen", "Mélenchon", "Melenchon", "Philippe", "Retailleau",
             "Roussel", "Ruffin", "Tondelier", "Villepin", "Zemmour", "Bardella", "Knafo", "Macron",
             "Rassemblement national", "RN", "LFI", "insoumis", "PS", "socialiste", "Républicains", "LR",
             "Reconquête", "Horizons", "Renaissance", "PCF", "communiste", "Écologistes", "écologiste",
             "Place publique", "Debout", "NFP", "candidat", "candidate", "candidats", "campagne", "programme"]
RE_INTERDIT = re.compile(r"\b(" + "|".join(re.escape(n) for n in INTERDITS) + r")\b", re.I)

# Sources acceptées dans la fiche : institutions, statistiques publiques, textes de loi,
# recherche. Jamais un site de parti, de campagne ou un comparateur de programmes.
DOMAINES_OK = ["insee.fr", "ec.europa.eu", "eur-lex.europa.eu", "senat.fr", "assemblee-nationale.fr",
               "vie-publique.fr", "douane.gouv.fr", "interieur.gouv.fr", "legifrance.gouv.fr", "impots.gouv.fr",
               "service-public.gouv.fr", "info.gouv.fr", "fonction-publique.gouv.fr", "ccomptes.fr",
               "banque-france.fr", "citepa.org", "hautconseilclimat.fr", "sciencespo.fr",
               "conseil-constitutionnel.fr", "parliament.uk", "bfs.admin.ch", "darpa.mil", "bundestag.de",
               "developpement-durable.gouv.fr", "credoc.fr", "institutmontaigne.org", "rexecode.fr",
               "recherches-solidarites.org", "acre.org.uk", "dejure.org", "lxgesetze.de", "juridischloket.nl",
               "nyidanmark.dk", "oecd.org", "theregister.com", "inegalites.fr"]
NOMS_DOMAINES = {"insee.fr": "Insee", "ec.europa.eu": "Eurostat / Commission européenne", "eur-lex.europa.eu": "EUR-Lex (droit de l'UE)",
                 "senat.fr": "Sénat", "assemblee-nationale.fr": "Assemblée nationale", "vie-publique.fr": "Vie publique",
                 "douane.gouv.fr": "Douane française", "interieur.gouv.fr": "Ministère de l'Intérieur",
                 "legifrance.gouv.fr": "Légifrance", "impots.gouv.fr": "DGFiP", "credoc.fr": "Crédoc",
                 "recherches-solidarites.org": "Recherches & Solidarités", "acre.org.uk": "ACRE (Royaume-Uni)",
                 "dejure.org": "Droit allemand (AufenthG)", "lxgesetze.de": "Droit allemand (FreizügG/EU)",
                 "juridischloket.nl": "Juridisch Loket (Pays-Bas)", "nyidanmark.dk": "SIRI (Danemark)",
                 "inegalites.fr": "Observatoire des inégalités", "oecd.org": "OCDE", "bundestag.de": "Bundestag",
                 "fonction-publique.gouv.fr": "DGAFP (fonction publique)"}


def propre(html):
    """Retire les phrases qui nomment un candidat ou un parti (balises conservées)."""
    if not html:
        return ""
    phrases = re.split(r"(?<=[.!?])\s+(?=[A-ZÉÀ<«])", html)
    return " ".join(p for p in phrases if not RE_INTERDIT.search(re.sub(r"<[^>]+>", "", p))).strip()


def sans_citation(html):
    """Retire les citations de candidat introduites par « pour un » ou « : »
    (ex. « combat sans merci ») : une formule de campagne peut trahir l'auteur."""
    return re.sub(r"\s*(?:pour une?|:)\s*«[^»]{3,80}»", "", html or "")


def neutre(txt):
    txt = re.sub(r"\b(proposé|proposée|cité|citée|annoncé|annoncée|voulu|voulue)\s+par\s+[A-ZÉ][\w'’-]+(\s+[A-Z][\w-]+)?",
                 r"\1 par la mesure", txt or "")
    return "" if RE_INTERDIT.search(txt) else txt


def sources(carte):
    txt = (ANALYSIS / "scripts" / "cards" / f"{carte}.py").read_text(encoding="utf-8")
    paires = []
    for node in ast.walk(ast.parse(txt)):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value == "sources" and isinstance(v, ast.List):
                    try:
                        paires += [(s.get("nom", ""), s["url"]) for s in ast.literal_eval(v) if isinstance(s, dict) and s.get("url")]
                    except ValueError:
                        pass
    for m in re.finditer(r"(?:^|\n|- )\s*([^\n:<>]{6,160}?)\s*:\s*(https?://[^\s<\"')]+)", txt):
        paires.append((m.group(1).strip(" -•"), m.group(2)))
    for url in re.findall(r"https?://[^\s<\"')]+", txt):
        paires.append(("", url))
    out, vus = [], set()
    for nom, url in paires:
        url = url.split("\\")[0].rstrip(".,;)»/")
        dom = urlparse(url).netloc.lower()
        if any(url.startswith(v) or v.startswith(url) for v in vus) or "comparateur" in url:
            continue
        cle = next((d for d in DOMAINES_OK if dom == d or dom.endswith("." + d)), None)
        if not cle or RE_INTERDIT.search(nom + " " + url):
            continue
        vus.add(url)
        out.append({"nom": nom or NOMS_DOMAINES.get(cle, cle), "url": url})
    return out[:8]


def fiche(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    r, h, eu = d.get("resume", {}), d.get("hero", {}), d.get("europe") or {}
    # Chiffres clés : tout chiffre lié à un nom est retiré (pas seulement le nom).
    chiffres = [{"value": x["value"], "label": x["label"]} for x in h.get("recit", []) if not RE_INTERDIT.search(x["label"])]
    chiffres_eu = [{"value": x["value"], "label": x["label"]} for x in h.get("europe", []) if not RE_INTERDIT.search(x["label"])]
    lignes = [{"label": neutre(l["label"]), "value": l["value"], "value_max": l.get("value_max"),
               "focus": l.get("kind") == "focus" or l["label"].startswith("France"), "note": neutre(l.get("note", ""))}
              for l in eu.get("lignes", []) if neutre(l["label"])]
    ref = eu.get("ref")
    if ref and not neutre(ref["label"]):
        ref = None
    f = {"essentiel": sans_citation(propre(r.get("recit"))), "chiffres": chiffres,
         "europe_texte": propre(r.get("europe")), "europe_chiffres": chiffres_eu,
         "europe": {"titre": neutre(eu.get("titre", "")), "unite": eu.get("unite", ""), "max": eu.get("echelle_max"),
                    "ref": {"label": neutre(ref["label"]), "value": ref["value"]} if ref else None, "lignes": lignes} if lignes else None,
         "sources": sources(path.stem)}
    reste = RE_INTERDIT.search(json.dumps(f, ensure_ascii=False))
    if reste:
        raise SystemExit(f"{path.stem} : nom ou parti encore présent ({reste.group(0)!r}) — fiche non anonyme")
    return f


def main():
    data_path = HERE / "deck-data.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    fiches = {}
    for p in sorted((ANALYSIS / "data" / "analyses").glob("carte_*.json")):
        n = p.stem.split("_")[1]
        fiches[n] = fiche(p)
    data["fiches"] = fiches
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for n, f in fiches.items():
        print(n, "chiffres", len(f["chiffres"]), "| Europe", len((f["europe"] or {}).get("lignes", [])), "| sources", len(f["sources"]))


if __name__ == "__main__":
    main()
