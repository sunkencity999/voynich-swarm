#!/usr/bin/env python3
"""Phase 7 refinement: re-test cells whose 2000-perm p hit/neared the floor
with 50,000 permutations, then recompute BH-FDR over the full 333-cell set
using refined p-values. Also refine the Mantel test to 20k perms."""
import json, re
import numpy as np
from collections import Counter
from run_phase7 import (J, FEATURES, load_folio_words, build_families,
                        folio_profiles, perm_assoc, bh_fdr, mantel)

REFINE_P = 0.02      # refine every cell with p <= this
N_PERM_HI = 50000

res = json.load(open(J("phase7_results.json")))
ck = json.load(open(J("phase7_features.json")))
feats = ck["features"]
folios = res["folios"]
fw = load_folio_words()
fams = build_families(fw)
names, X, freq, tot = folio_profiles(fw, fams, folios)
jix = {nm: j for j, nm in enumerate(names)}

assoc = res["association"]
to_refine = [k for k, v in assoc.items() if v["p"] <= REFINE_P]
print(f"refining {len(to_refine)} cells at {N_PERM_HI} perms")
for k in to_refine:
    feat, fam = k.split("|")
    fv = [feats[f].get(feat, "missing") for f in folios]
    rng = np.random.default_rng(424242 + hash(k) % 100000)
    h, p = perm_assoc(fv, freq[:, jix[fam]], rng, n_perm=N_PERM_HI)
    print(f"  {k}: p {assoc[k]['p']} -> {p:.6f} (H={h:.3f})")
    assoc[k]["p_refined"] = round(p, 6)

# recompute FDR over all cells using refined p where available
keys = list(assoc)
pv = np.array([assoc[k].get("p_refined", assoc[k]["p"]) for k in keys])
surv = bh_fdr(pv, q=0.05)
for k, s in zip(keys, surv):
    assoc[k]["fdr_survives"] = bool(s)
survivors = [k for k, s in zip(keys, surv) if s]
res["n_fdr_survivors"] = len(survivors)
res["fdr_survivors"] = survivors
res["min_p_refined"] = float(pv.min())
print("FDR survivors after refinement:", survivors)
print("min refined p:", pv.min())

# refined Mantel
d = np.load(J("phase7_mantel.npz"), allow_pickle=True)
r_obs, p_m = mantel(d["vis"], d["txt"], np.random.default_rng(99), n_perm=20000)
res["mantel"]["r"] = round(float(r_obs), 4)
res["mantel"]["p"] = round(float(p_m), 6)
res["mantel"]["n_perm"] = 20000
print(f"Mantel refined: r={r_obs:.4f} p={p_m:.6f}")

with open(J("phase7_results.json"), "w") as f:
    json.dump(res, f, indent=1)
print("updated phase7_results.json")
