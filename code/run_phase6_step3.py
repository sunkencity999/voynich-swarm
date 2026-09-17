#!/usr/bin/env python3
"""Phase 6 step 3: within-page label-structure tests.
Do labels on one zodiac folio (nymph/star names of one constellation) look
more like each other than like labels on other zodiac folios? Same for
pharma pages (Lf+Lc) and astro star labels (Ls).
Metrics: normalized edit distance + shared-prefix(2-glyph) rate.
Permutation: shuffle label->page assignment within the group, 10k perms.
Checkpoint -> phase6_withinpage.json"""
import json, random
from collections import defaultdict
from itertools import combinations
import numpy as np
from phase6_lib import extract_loci, split_loci, edit_distance
from phase4_lib import glyphs

rng = random.Random(3)
loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

def norm_ed(a, b):
    return edit_distance(a, b) / max(len(a), len(b))

def pref2(w):
    g = glyphs(w)
    return ''.join(g[:2])

def within_test(group_name, sel, nperm=10000, min_per_page=3):
    """sel: list of (folio, word). Tests within- vs across-page similarity."""
    pages = defaultdict(list)
    for f, w in sel:
        if len(w) >= 2:
            pages[f].append(w)
    pages = {f: ws for f, ws in pages.items() if len(ws) >= min_per_page}
    if len(pages) < 3:
        return None
    folios = sorted(pages)
    allw = [(f, w) for f in folios for w in pages[f]]
    words = [w for f, w in allw]
    labs = [f for f, w in allw]
    n = len(words)
    # precompute pairwise
    ED = np.zeros((n, n)); PF = np.zeros((n, n))
    for i, j in combinations(range(n), 2):
        d = norm_ed(words[i], words[j])
        ED[i, j] = ED[j, i] = d
        p = 1.0 if pref2(words[i]) == pref2(words[j]) else 0.0
        PF[i, j] = PF[j, i] = p

    sizes = [len(pages[f]) for f in folios]
    tot_ed = ED.sum(); tot_pf = PF.sum()
    npairs_tot = n * (n - 1)
    npairs_within = sum(s * (s - 1) for s in sizes)
    npairs_across = npairs_tot - npairs_within

    def stat(order):
        """order: permuted index array; consecutive blocks of `sizes` are pages."""
        w_ed = w_pf = 0.0
        pos = 0
        for s in sizes:
            idx = order[pos:pos + s]
            w_ed += ED[np.ix_(idx, idx)].sum()
            w_pf += PF[np.ix_(idx, idx)].sum()
            pos += s
        a_ed = (tot_ed - w_ed) / npairs_across
        a_pf = (tot_pf - w_pf) / npairs_across
        return w_ed / npairs_within - a_ed, w_pf / npairs_within - a_pf

    base = np.arange(n)
    obs_ed, obs_pf = stat(base)
    nprng = np.random.default_rng(3)
    null_ed, null_pf = [], []
    for _ in range(nperm):
        e, p = stat(nprng.permutation(n))
        null_ed.append(e); null_pf.append(p)
    null_ed, null_pf = np.array(null_ed), np.array(null_pf)
    res = {
        'n_words': n, 'n_pages': len(folios),
        'within_minus_across_editdist': obs_ed,
        'ed_null_mean': float(null_ed.mean()), 'ed_null_std': float(null_ed.std()),
        'ed_z': float((obs_ed - null_ed.mean()) / null_ed.std()),
        'ed_p_more_similar': float((null_ed <= obs_ed).mean()),  # similar = LOWER within dist
        'within_minus_across_prefixshare': obs_pf,
        'pf_null_mean': float(null_pf.mean()), 'pf_null_std': float(null_pf.std()),
        'pf_z': float((obs_pf - null_pf.mean()) / null_pf.std()),
        'pf_p_more_shared': float((null_pf >= obs_pf).mean()),
    }
    print(f"{group_name}: n={n} pages={len(folios)}")
    print(f"  edit-dist within-across Δ={obs_ed:+.4f} (null {null_ed.mean():+.4f}±{null_ed.std():.4f}) "
          f"z={res['ed_z']:+.1f} p(within more similar)={res['ed_p_more_similar']:.4f}")
    print(f"  prefix2 share Δ={obs_pf:+.4f} (null {null_pf.mean():+.4f}±{null_pf.std():.4f}) "
          f"z={res['pf_z']:+.1f} p(within more shared)={res['pf_p_more_shared']:.4f}")
    return res

out = {}
zod = [(l['folio'], w) for l in labels if l['ltype'] == 'Lz' for w in l['words']]
out['zodiac_Lz'] = within_test('zodiac Lz', zod)
ph = [(l['folio'], w) for l in labels if l['ltype'] in ('Lf', 'Lc') for w in l['words']]
out['pharma_LfLc'] = within_test('pharma Lf+Lc', ph)
st = [(l['folio'], w) for l in labels if l['ltype'] == 'Ls' for w in l['words']]
out['astro_Ls'] = within_test('astro Ls', st)
ny = [(l['folio'], w) for l in labels if l['ltype'] in ('Ln', 'Lt') for w in l['words']]
out['balneo_LnLt'] = within_test('balneo Ln+Lt', ny)

json.dump(out, open('phase6_withinpage.json', 'w'), indent=1)
print("\ncheckpoint -> phase6_withinpage.json")
