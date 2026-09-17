#!/usr/bin/env python3
"""Phase 8: is the drawing<->dialect link confound, scribal, sectional, or content?

Covariates: quire ($Q), page-in-quire ($P), Lisa Fagin Davis scribe ($H, "LFD
hands" per voynich.nu/transcr.html) — all parsed from ZL3b-n.txt IVTFF headers.

PREREGISTERED TEST LIST (written before running; BH-FDR q=0.05 within family):

Confirmatory family (7 tests):
  C1  dialect ~ root_prominence | quire        (chi2, perm within quire, n=127)
  C3  scribe{2,3,5} ~ root_prominence within B (chi2, free perm, n=32)
  C4  quire ~ root_prominence within scribe 1  (chi2, free perm, n=95)
  C5  or- share ~ root_prominence | scribe     (KW, perm within scribe, n=129)
  C6  or- share ~ root_prominence | quire      (KW, perm within quire, n=129)
  C7  or- share ~ root_prominence | scribe x quire (KW, n=129)  <- headline
  C8  or- share ~ root_prominence within scribe 1 only | quire (KW, n=95)
  (C2 dialect ~ root_prominence | scribe is STRUCTURALLY UNTESTABLE: scribe
   and dialect are perfectly confounded in the herbal section — recorded, not
   counted in FDR.)

Exploratory family:
  E1  within scribe 1: all 9 features x 37 families, quire-stratified perm
  E2  within scribe 2 (n=20): same matrix, free perm + honest power sim

Descriptive (no FDR): logistic dialect ~ root_dominant (+ quire dummies),
mixed quires only, LRT.
Perms: confirmatory 20,000; exploratory 2,000 with p<=0.02 refined at 20,000.
"""
import json, os, re, sys
from collections import Counter, defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
def J(p): return os.path.join(HERE, p)
sys.path.insert(0, HERE)
from run_phase7 import load_folio_words, build_families, folio_profiles, kw_stat, bh_fdr, FEATURES

SEED = 20260916
NP_CONF = 20000
NP_EXPL = 2000
NP_REFINE = 20000

# ---------- covariates ----------

def load_headers():
    hdr = {}
    for line in open(J("ZL3b-n.txt")):
        m = re.match(r'^<(f\d+[rv]\d?)>\s+<!([^>]*)>', line)
        if m:
            d = dict(re.findall(r'\$(\w)=(\S+?)(?=\s|$)', m.group(2)))
            hdr[m.group(1)] = d
    return hdr

# ---------- stats ----------

def chi2_stat(x, y):
    """Pearson chi2 on contingency of two label arrays."""
    xs, ys = sorted(set(x)), sorted(set(y))
    xi = {v: i for i, v in enumerate(xs)}; yi = {v: i for i, v in enumerate(ys)}
    T = np.zeros((len(xs), len(ys)))
    for a, b in zip(x, y):
        T[xi[a], yi[b]] += 1
    E = np.outer(T.sum(1), T.sum(0)) / max(T.sum(), 1)
    mask = E > 0
    return float((((T - E) ** 2)[mask] / E[mask]).sum())

def merge_rare(vals, min_n=4):
    cnt = Counter(vals)
    return [v if cnt[v] >= min_n else "_rare" for v in vals]

def strat_perm(x, strata, rng):
    """Permute label array x within strata; returns new list."""
    x = list(x)
    by = defaultdict(list)
    for i, s in enumerate(strata):
        by[s].append(i)
    out = list(x)
    for idxs in by.values():
        vals = [x[i] for i in idxs]
        rng.shuffle(vals)
        for i, v in zip(idxs, vals):
            out[i] = v
    return out

def perm_test_chi2(x, y, strata, rng, n_perm):
    """chi2 of x vs y, permuting x within strata."""
    obs = chi2_stat(x, y)
    ge = 0
    for _ in range(n_perm):
        if chi2_stat(strat_perm(x, strata, rng), y) >= obs - 1e-12:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)

def kw_from_labels(x, yv):
    cats = sorted(set(x))
    if len(cats) < 2:
        return None
    groups = [yv[[i for i, v in enumerate(x) if v == c]] for c in cats]
    return kw_stat(groups)

def perm_test_kw(x, yv, strata, rng, n_perm):
    """KW of numeric yv across categories of x, permuting x within strata."""
    obs = kw_from_labels(x, yv)
    if obs is None:
        return None, None
    ge = 0
    for _ in range(n_perm):
        s = kw_from_labels(strat_perm(x, strata, rng), yv)
        if s is not None and s >= obs - 1e-12:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)

def logistic_lrt(Xd, y):
    """IRLS logistic with tiny ridge; returns (coefs, loglik)."""
    n, k = Xd.shape
    b = np.zeros(k)
    for _ in range(200):
        eta = Xd @ b
        p = 1 / (1 + np.exp(-np.clip(eta, -30, 30)))
        W = np.maximum(p * (1 - p), 1e-9)
        H = Xd.T @ (Xd * W[:, None]) + 1e-6 * np.eye(k)
        g = Xd.T @ (y - p) - 1e-6 * b
        step = np.linalg.solve(H, g)
        b = b + step
        if np.abs(step).max() < 1e-10:
            break
    eta = Xd @ b
    ll = float((y * eta - np.log1p(np.exp(np.clip(eta, -30, 30)))).sum())
    return b, ll

# ---------- main ----------

def main():
    hdr = load_headers()
    feats = json.load(open(J("phase7_features.json")))["features"]
    fw = load_folio_words()
    folios = sorted(set(feats) & set(fw) & set(hdr),
                    key=lambda f: (int(re.match(r'f(\d+)', f).group(1)), f))
    fams = build_families(fw)
    names, X, freq, tot = folio_profiles(fw, fams, folios)
    j_or = names.index("p2:or")
    or_share = freq[:, j_or]

    scribe = [hdr[f].get("H", "?") for f in folios]
    quire = [hdr[f].get("Q", "?") for f in folios]
    dialect = [hdr[f].get("L", "?") for f in folios]
    sq = [f"{s}|{q}" for s, q in zip(scribe, quire)]
    rp = merge_rare([feats[f].get("root_prominence", "missing") for f in folios])

    res = {"n_folios": len(folios),
           "covariate_source": "ZL3b-n.txt IVTFF headers: $Q quire, $H = Lisa Fagin Davis scribes ('LFD hands', voynich.nu/transcr.html), $L Currier",
           "crosstab_dialect_scribe": {f"{d}|{s}": c for (d, s), c in
                sorted(Counter(zip(dialect, scribe)).items())},
           "crosstab_quire_dialect_scribe": {f"{q}|{d}|{s}": c for (q, d, s), c in
                sorted(Counter(zip(quire, dialect, scribe)).items())}}
    print("folios:", len(folios))
    print("dialect x scribe:", res["crosstab_dialect_scribe"])

    conf = {}
    # C2 — structurally untestable, recorded
    within_scribe_dialect_var = any(len(set(d for d, s2 in zip(dialect, scribe) if s2 == s and d in "AB")) > 1
                                    for s in set(scribe))
    conf["C2_dialect_vs_rootprom_given_scribe"] = {
        "status": "untestable",
        "reason": "scribe and dialect perfectly confounded in herbal section (no within-scribe dialect variance)",
        "within_scribe_dialect_variance": within_scribe_dialect_var}

    # dialect-known subset
    dia_idx = [i for i, d in enumerate(dialect) if d in ("A", "B")]
    rng = np.random.default_rng(SEED)

    # C1: dialect ~ rp | quire
    x = [rp[i] for i in dia_idx]; y = [dialect[i] for i in dia_idx]; st = [quire[i] for i in dia_idx]
    s_, p_ = perm_test_chi2(x, y, st, rng, NP_CONF)
    conf["C1_dialect_vs_rootprom_given_quire"] = {"chi2": round(s_, 3), "p": p_, "n": len(x)}
    # mixed-quire accounting
    mixed = sorted({q for q in st if len(set(yy for yy, qq in zip(y, st) if qq == q)) > 1})
    conf["C1_dialect_vs_rootprom_given_quire"]["mixed_quires"] = mixed
    conf["C1_dialect_vs_rootprom_given_quire"]["n_in_mixed_quires"] = sum(1 for q in st if q in mixed)
    print("C1", conf["C1_dialect_vs_rootprom_given_quire"])

    # C3: scribe ~ rp within B
    b_idx = [i for i, d in enumerate(dialect) if d == "B"]
    x = [rp[i] for i in b_idx]; y = [scribe[i] for i in b_idx]
    s_, p_ = perm_test_chi2(x, y, ["all"] * len(x), rng, NP_CONF)
    conf["C3_scribe_vs_rootprom_within_B"] = {"chi2": round(s_, 3), "p": p_, "n": len(x),
        "table": {f"{a}|{b}": c for (a, b), c in sorted(Counter(zip(x, y)).items())}}
    print("C3", conf["C3_scribe_vs_rootprom_within_B"])

    # C4: quire ~ rp within scribe 1
    s1_idx = [i for i, s in enumerate(scribe) if s == "1"]
    x = [rp[i] for i in s1_idx]; y = [quire[i] for i in s1_idx]
    s_, p_ = perm_test_chi2(x, y, ["all"] * len(x), rng, NP_CONF)
    conf["C4_quire_vs_rootprom_within_scribe1"] = {"chi2": round(s_, 3), "p": p_, "n": len(x)}
    print("C4", conf["C4_quire_vs_rootprom_within_scribe1"])

    # C5-C7: or- ~ rp under successive strata (all 129 folios)
    for tag, strata in [("C5_or_vs_rootprom_given_scribe", scribe),
                        ("C6_or_vs_rootprom_given_quire", quire),
                        ("C7_or_vs_rootprom_given_scribe_x_quire", sq)]:
        h, p_ = perm_test_kw(rp, or_share, strata, rng, NP_CONF)
        conf[tag] = {"H": round(h, 3), "p": p_, "n": len(rp),
                     "n_strata": len(set(strata))}
        print(tag, conf[tag])

    # C8: within scribe 1 only, quire-stratified
    x = [rp[i] for i in s1_idx]; yv = or_share[s1_idx]; st = [quire[i] for i in s1_idx]
    h, p_ = perm_test_kw(x, yv, st, rng, NP_CONF)
    conf["C8_or_vs_rootprom_scribe1_given_quire"] = {"H": round(h, 3), "p": p_, "n": len(x)}
    print("C8", conf["C8_or_vs_rootprom_scribe1_given_quire"])

    # BH over the 7 runnable confirmatory tests
    ckeys = [k for k in conf if conf[k].get("p") is not None]
    cp = np.array([conf[k]["p"] for k in ckeys])
    surv = bh_fdr(cp, q=0.05)
    for k, s in zip(ckeys, surv):
        conf[k]["fdr_survives"] = bool(s)
    res["confirmatory"] = conf
    res["confirmatory_fdr"] = {k: bool(s) for k, s in zip(ckeys, surv)}

    # or- means by rp category, per stratum set (for chart/report)
    means = {}
    for cat in sorted(set(rp)):
        idx = [i for i, v in enumerate(rp) if v == cat]
        means[cat] = {"n": len(idx), "mean_or_share": round(float(or_share[idx].mean()), 5)}
    res["or_share_by_rootprom"] = means
    s1means = {}
    for cat in sorted(set(rp[i] for i in s1_idx)):
        idx = [i for i in s1_idx if rp[i] == cat]
        s1means[cat] = {"n": len(idx), "mean_or_share": round(float(or_share[idx].mean()), 5)}
    res["or_share_by_rootprom_scribe1"] = s1means

    # descriptive logistic: dialect ~ root_dominant (+ quire dummies), mixed quires only
    mq_idx = [i for i in dia_idx if quire[i] in mixed]
    yb = np.array([1.0 if dialect[i] == "B" else 0.0 for i in mq_idx])
    xd = np.array([1.0 if rp[i] == "dominant" else 0.0 for i in mq_idx])
    qs = sorted(set(quire[i] for i in mq_idx))
    Q = np.array([[1.0 if quire[i] == q else 0.0 for q in qs[1:]] for i in mq_idx])
    X0 = np.column_stack([np.ones(len(mq_idx)), Q])            # null: quire only
    X1 = np.column_stack([np.ones(len(mq_idx)), Q, xd])         # + root_dominant
    b0, ll0 = logistic_lrt(X0, yb)
    b1, ll1 = logistic_lrt(X1, yb)
    from scipy.stats import chi2 as chi2dist
    lrt = 2 * (ll1 - ll0)
    res["logistic_descriptive"] = {
        "n": len(mq_idx), "quires": qs,
        "coef_root_dominant": round(float(b1[-1]), 3),
        "LRT_chi2_1df": round(float(lrt), 3),
        "LRT_p": float(chi2dist.sf(max(lrt, 0), 1)),
        "note": "descriptive only; permutation tests are primary"}
    print("logistic:", res["logistic_descriptive"])

    # ---------- exploratory ----------
    def explore(idx, strata, label, n_perm=NP_EXPL):
        out = {}
        pv, cells = [], []
        sub_freq = freq[idx]
        for feat in FEATURES:
            fv = merge_rare([feats[folios[i]].get(feat, "missing") for i in idx])
            if len(set(fv)) < 2:
                continue
            for j, fam in enumerate(names):
                r = np.random.default_rng(SEED + abs(hash((label, feat, fam))) % 10**6)
                h, p_ = perm_test_kw(fv, sub_freq[:, j], strata, r, n_perm)
                if h is None:
                    continue
                if p_ <= 0.02:  # refine
                    h, p_ = perm_test_kw(fv, sub_freq[:, j], strata, r, NP_REFINE)
                out[f"{feat}|{fam}"] = {"H": round(h, 3), "p": round(p_, 6)}
                pv.append(p_); cells.append(f"{feat}|{fam}")
        surv = bh_fdr(np.array(pv), q=0.05) if pv else np.array([])
        for c, s in zip(cells, surv):
            out[c]["fdr_survives"] = bool(s)
        return {"n_folios": len(idx), "n_tests": len(pv),
                "min_p": float(min(pv)) if pv else None,
                "fdr_survivors": [c for c, s in zip(cells, surv) if s],
                "top10": sorted(((c, out[c]["p"]) for c in cells), key=lambda t: t[1])[:10],
                "tests": out}

    print("E1: within scribe 1, quire-stratified ...")
    e1 = explore(s1_idx, [quire[i] for i in s1_idx], "E1")
    res["E1_within_scribe1"] = e1
    print("E1 survivors:", e1["fdr_survivors"], "min p:", e1["min_p"])

    s2_idx = [i for i, s in enumerate(scribe) if s == "2"]
    print("E2: within scribe 2 (n=%d), free perm ..." % len(s2_idx))
    e2 = explore(s2_idx, ["all"] * len(s2_idx), "E2")
    res["E2_within_scribe2"] = e2
    print("E2 survivors:", e2["fdr_survivors"], "min p:", e2["min_p"])

    # E2 power simulation: plant the pooled or-xroot effect into n=20 with
    # scribe 2's category mix; how often does KW at alpha=.05 detect it?
    rng2 = np.random.default_rng(SEED + 99)
    cat_pools = {}
    for cat in set(rp):
        vals = or_share[[i for i, v in enumerate(rp) if v == cat]]
        if len(vals):
            cat_pools[cat] = vals
    s2_cats = [rp[i] for i in s2_idx]
    hits = 0; SIMS = 500; NPS = 400
    for _ in range(SIMS):
        yv = np.array([cat_pools[c][rng2.integers(len(cat_pools[c]))] for c in s2_cats])
        h, p_ = perm_test_kw(s2_cats, yv, ["all"] * len(s2_cats), rng2, NPS)
        if p_ is not None and p_ < 0.05:
            hits += 1
    res["E2_power_sim"] = {"sims": SIMS, "perm_per_sim": NPS,
        "power_at_alpha05": round(hits / SIMS, 3),
        "note": "pooled effect planted into scribe-2 category mix (n=20)"}
    print("E2 power:", res["E2_power_sim"])

    with open(J("phase8_results.json"), "w") as f:
        json.dump(res, f, indent=1)
    print("saved phase8_results.json")

if __name__ == "__main__":
    main()
