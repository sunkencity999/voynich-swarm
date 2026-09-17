#!/usr/bin/env python3
"""Phase 7: image-side feature pairing.

Tests whether visual plant features (from local VL extraction,
phase7_features.json) correlate with per-folio word-family profiles.

Stages:
  reliability  - per-feature self-agreement between features and rerun passes
  assoc        - feature x family permutation-tested association matrix + BH-FDR
  mantel       - visual-similarity vs text-similarity Mantel test
  consensus    - extracted features vs 7 scholarly consensus plant IDs
All results -> phase7_results.json
"""
import json, os, random, re, sys
from collections import Counter, defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
def J(p): return os.path.join(HERE, p)

RNG_SEED = 20260914
N_PERM = 2000

FEATURES = ["leaf_shape","leaf_arrangement","root_type","root_prominence",
            "flower_present","flower_color","flower_shape","stem_count","plant_count"]

# ---------- text side ----------

def load_folio_words():
    vlines = json.load(open(J("phase5_vlines.json")))
    meta = json.load(open(J("phase5_line_meta.json")))
    fw = defaultdict(list)
    for words, m in zip(vlines, meta):
        if m["sec"] == "herbal":
            fw[m["folio"]].extend(words)
    return fw

def build_families(fw, top_n=30):
    """Families = top-N 2-glyph prefixes in herbal text + phase-5/6 named regex families."""
    all_words = [w for ws in fw.values() for w in ws]
    pref = Counter(w[:2] for w in all_words if len(w) >= 2)
    fams = {f"p2:{p}": (lambda w, p=p: w.startswith(p)) for p, _ in pref.most_common(top_n)}
    named = {
        "fam:cth": lambda w: w.startswith("cth"),
        "fam:kch": lambda w: w.startswith("kch"),
        "fam:dch": lambda w: w.startswith("dch"),
        "fam:qoke": lambda w: w.startswith("qoke"),
        "fam:oteo": lambda w: w.startswith("oteo"),
        "fam:lk": lambda w: w.startswith("lk"),
        "fam:ol_dy": lambda w: w.startswith("ol") and w.endswith("dy"),
    }
    fams.update(named)
    return fams

def folio_profiles(fw, fams, folios):
    names = sorted(fams)
    X = np.zeros((len(folios), len(names)))
    tot = np.zeros(len(folios))
    for i, f in enumerate(folios):
        ws = fw.get(f, [])
        tot[i] = len(ws)
        for j, nm in enumerate(names):
            fn = fams[nm]
            X[i, j] = sum(1 for w in ws if fn(w))
    freq = X / np.maximum(tot[:, None], 1)
    return names, X, freq, tot

# ---------- stats ----------

def kw_stat(groups):
    """Kruskal-Wallis H (no tie correction needed for permutation calibration)."""
    allv = np.concatenate(groups)
    n = len(allv)
    ranks = np.empty(n)
    order = np.argsort(allv, kind="mergesort")
    # average ranks for ties
    sv = allv[order]
    r = np.arange(1, n + 1, dtype=float)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and sv[j + 1] == sv[i]:
            j += 1
        r[i:j + 1] = r[i:j + 1].mean()
        i = j + 1
    ranks[order] = r
    h = 0.0
    pos = 0
    for g in groups:
        k = len(g)
        rs = ranks[pos:pos + k].sum()
        h += rs * rs / k
        pos += k
    return 12.0 / (n * (n + 1)) * h - 3 * (n + 1)

def perm_assoc(feature_vals, fam_freq, rng, n_perm=N_PERM):
    """feature_vals: list of category labels per folio; fam_freq: vector per folio.
    Returns (H, p_perm). Categories with <4 folios merged into 'other'."""
    cnt = Counter(feature_vals)
    vals = [v if cnt[v] >= 4 else "_rare" for v in feature_vals]
    cats = sorted(set(vals))
    if len(cats) < 2:
        return None, None
    idx = {c: [i for i, v in enumerate(vals) if v == c] for c in cats}
    groups = [fam_freq[idx[c]] for c in cats]
    h_obs = kw_stat(groups)
    sizes = [len(idx[c]) for c in cats]
    ge = 0
    v = fam_freq.copy()
    for _ in range(n_perm):
        rng.shuffle(v)
        pos = 0
        gs = []
        for s in sizes:
            gs.append(v[pos:pos + s]); pos += s
        if kw_stat(gs) >= h_obs - 1e-12:
            ge += 1
    return h_obs, (ge + 1) / (n_perm + 1)

def bh_fdr(pvals, q=0.05):
    idx = np.argsort(pvals)
    m = len(pvals)
    thresh = np.zeros(m, dtype=bool)
    maxk = -1
    for rank, i in enumerate(idx, 1):
        if pvals[i] <= q * rank / m:
            maxk = rank
    if maxk > 0:
        for rank, i in enumerate(idx, 1):
            if rank <= maxk:
                thresh[i] = True
    return thresh

def mantel(d1, d2, rng, n_perm=N_PERM):
    """Spearman Mantel on condensed upper triangles."""
    n = d1.shape[0]
    iu = np.triu_indices(n, 1)
    a, b = d1[iu], d2[iu]
    def spear(x, y):
        rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
        rx = rx - rx.mean(); ry = ry - ry.mean()
        return float((rx * ry).sum() / np.sqrt((rx * rx).sum() * (ry * ry).sum()))
    r_obs = spear(a, b)
    ge = 0
    perm = np.arange(n)
    for _ in range(n_perm):
        rng.shuffle(perm)
        d2p = d2[np.ix_(perm, perm)]
        if abs(spear(a, d2p[iu])) >= abs(r_obs) - 1e-12:
            ge += 1
    return r_obs, (ge + 1) / (n_perm + 1)

# ---------- main ----------

def main():
    rng = np.random.default_rng(RNG_SEED)
    py_rng = random.Random(RNG_SEED)
    ck = json.load(open(J("phase7_features.json")))
    feats = ck["features"]; rerun = ck.get("rerun", {})
    fw = load_folio_words()
    folios = sorted(set(feats) & set(fw), key=lambda f: (int(re.match(r'f(\d+)', f).group(1)), f))
    print(f"folios with both features and text: {len(folios)}")
    results = {"n_folios": len(folios), "folios": folios}

    # --- reliability ---
    rel = {}
    common = sorted(set(feats) & set(rerun))
    for k in FEATURES:
        agree = sum(1 for f in common if feats[f].get(k) == rerun[f].get(k))
        rel[k] = {"n": len(common), "agree": agree, "rate": round(agree / max(len(common), 1), 3)}
    results["reliability"] = rel
    reliable = [k for k in FEATURES if rel[k]["rate"] >= 0.70]
    results["reliable_features"] = reliable
    print("reliability:", {k: rel[k]["rate"] for k in FEATURES})
    print("reliable (>=0.70):", reliable)

    # --- profiles ---
    fams = build_families(fw)
    names, X, freq, tot = folio_profiles(fw, fams, folios)
    results["families"] = names
    results["tokens_per_folio"] = {f: int(t) for f, t in zip(folios, tot)}

    # --- association matrix ---
    assoc = {}
    pvals, cells = [], []
    for feat in FEATURES:
        fv = [feats[f].get(feat, "missing") for f in folios]
        for j, fam in enumerate(names):
            r = np.random.default_rng(RNG_SEED + hash((feat, fam)) % 100000)
            h, p = perm_assoc(fv, freq[:, j], r)
            if h is None:
                continue
            assoc[f"{feat}|{fam}"] = {"H": round(h, 3), "p": round(p, 5)}
            pvals.append(p); cells.append((feat, fam))
    surv = bh_fdr(np.array(pvals), q=0.05)
    n_surv = int(surv.sum())
    for (feat, fam), s in zip(cells, surv):
        assoc[f"{feat}|{fam}"]["fdr_survives"] = bool(s)
    results["association"] = assoc
    results["n_tests"] = len(pvals)
    results["n_fdr_survivors"] = n_surv
    results["min_p"] = float(min(pvals))
    print(f"association tests: {len(pvals)}, FDR(q=0.05) survivors: {n_surv}, min p = {min(pvals):.5f}")
    # survivors restricted to reliable features
    surv_rel = [c for c, s in zip(cells, surv) if s and c[0] in reliable]
    results["fdr_survivors_reliable"] = [f"{a}|{b}" for a, b in surv_rel]
    print("reliable-feature survivors:", surv_rel)

    # --- Mantel ---
    n = len(folios)
    vis = np.zeros((n, n))
    usef = reliable if reliable else FEATURES
    for i in range(n):
        for j in range(i + 1, n):
            mism = sum(1 for k in usef if feats[folios[i]].get(k) != feats[folios[j]].get(k))
            vis[i, j] = vis[j, i] = mism / len(usef)
    # text distance: cosine on sqrt-freq profiles
    P = np.sqrt(freq)
    Pn = P / np.maximum(np.linalg.norm(P, axis=1, keepdims=True), 1e-12)
    txt = 1.0 - Pn @ Pn.T
    r_obs, p_m = mantel(vis, txt, np.random.default_rng(RNG_SEED + 7))
    results["mantel"] = {"r": round(r_obs, 4), "p": round(p_m, 5), "features_used": usef}
    print(f"Mantel: r={r_obs:.4f} p={p_m:.5f}")
    # save distances for chart
    np.savez(J("phase7_mantel.npz"), vis=vis, txt=txt, folios=folios)

    # --- consensus sanity ---
    expected = {
        "f1v":  {"id": "Atropa belladonna", "expect": {"leaf_shape": ["broad"], "flower_present": ["yes"]}},
        "f2r":  {"id": "Centaurea", "expect": {"leaf_shape": ["narrow", "lobed"], "flower_present": ["yes"]}},
        "f2v":  {"id": "Nymphoides (water-lily)", "expect": {"leaf_shape": ["round", "broad"], "root_type": ["rhizome", "other", "branching"]}},
        "f9v":  {"id": "Viola tricolor", "expect": {"flower_present": ["yes"], "flower_color": ["purple", "blue", "yellow"]}},
        "f15v": {"id": "Paris quadrifolia", "expect": {"leaf_arrangement": ["whorled"], "stem_count": ["single"]}},
        "f16r": {"id": "Cannabis", "expect": {"leaf_shape": ["compound", "spiky", "narrow"]}},
        "f17v": {"id": "Dioscorea/Tamus", "expect": {"leaf_shape": ["broad", "round"], "stem_count": ["single", "multiple"]}},
    }
    cons = {}
    hits = checks = 0
    for f, spec in expected.items():
        got = feats.get(f)
        if not got:
            cons[f] = {"id": spec["id"], "status": "no extraction"}
            continue
        row = {"id": spec["id"], "matches": {}, "extracted": {k: got.get(k) for k in FEATURES}}
        for k, ok_vals in spec["expect"].items():
            m = got.get(k) in ok_vals
            row["matches"][k] = {"got": got.get(k), "expected_any_of": ok_vals, "match": m}
            hits += int(m); checks += 1
        cons[f] = row
    results["consensus"] = cons
    results["consensus_hitrate"] = {"hits": hits, "checks": checks, "rate": round(hits / max(checks, 1), 3)}
    print(f"consensus feature-match: {hits}/{checks}")

    with open(J("phase7_results.json"), "w") as f:
        json.dump(results, f, indent=1)
    print("saved phase7_results.json")

if __name__ == "__main__":
    main()
