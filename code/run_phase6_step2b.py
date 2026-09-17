#!/usr/bin/env python3
"""Phase 6 step 2b: anchoring rate v2 — page text = paragraphs + circular/
radial text (zodiac/astro/cosmo running text lives in C/R loci).
Checkpoint -> phase6_anchoring2.json"""
import json, random
from collections import Counter, defaultdict
import numpy as np
from phase6_lib import extract_loci, split_loci

rng = random.Random(66)
loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

page_text = defaultdict(list)
for p in paras + circ:
    page_text[p['folio']].extend(p['words'])

label_tokens = [(l['folio'], l['section'], w) for l in labels for w in l['words']]

def anchoring(min_len=1, nperm=20000):
    page_labels = defaultdict(list)
    for f, s, w in label_tokens:
        if len(w) >= min_len:
            page_labels[(s, f)].append(w)
    sec_groups = defaultdict(list)
    for (s, f), ws in page_labels.items():
        if page_text.get(f):
            sec_groups[s].append((f, ws))
    per_sec, obs_hits, obs_n = {}, 0, 0
    pooled_null = np.zeros(nperm)
    for s, grp in sorted(sec_groups.items()):
        folios = [f for f, ws in grp]
        tsets = {f: set(page_text[f]) for f in folios}
        wordsets = [ws for f, ws in grp]
        n = sum(len(ws) for ws in wordsets)
        hits = sum(1 for f, ws in grp for w in ws if w in tsets[f])
        obs_hits += hits; obs_n += n
        cross_hits = cross_n = 0
        for f, ws in grp:
            for g in folios:
                if g == f: continue
                cross_hits += sum(1 for w in ws if w in tsets[g])
                cross_n += len(ws)
        null = np.zeros(nperm)
        for i in range(nperm):
            perm = folios[:]
            rng.shuffle(perm)
            null[i] = sum(1 for ws, f in zip(wordsets, perm) for w in ws if w in tsets[f])
        pooled_null += null
        nullr = null / n
        obs = hits / n
        per_sec[s] = {'n_label_words': n, 'n_pages': len(folios),
                      'same_page_rate': obs,
                      'cross_page_rate': cross_hits / cross_n if cross_n else None,
                      'null_mean': float(nullr.mean()), 'null_std': float(nullr.std()),
                      'z': float((obs - nullr.mean()) / nullr.std()) if nullr.std() > 0 else None,
                      'p_perm': float((nullr >= obs).mean())}
    pooled_null /= obs_n
    obs_rate = obs_hits / obs_n
    return {'per_section': per_sec,
            'pooled': {'n_label_words': obs_n, 'same_page_rate': obs_rate,
                       'null_mean': float(pooled_null.mean()),
                       'null_std': float(pooled_null.std()),
                       'z': float((obs_rate - pooled_null.mean()) / pooled_null.std()),
                       'p_perm': float((pooled_null >= obs_rate).mean())}}

out = {}
for ml, key in [(1, 'anchoring_all'), (3, 'anchoring_len3')]:
    r = anchoring(min_len=ml)
    out[key] = r
    P = r['pooled']
    print(f"anchoring v2 (min len {ml}): same-page {P['same_page_rate']:.3f} "
          f"null {P['null_mean']:.3f}±{P['null_std']:.3f} z={P['z']:.1f} p={P['p_perm']:.5f}  (n={P['n_label_words']})")
    for s, d in sorted(r['per_section'].items()):
        print(f"  {s:8s} n={d['n_label_words']:4d} pages={d['n_pages']:3d} same={d['same_page_rate']:.3f} "
              f"cross={d['cross_page_rate'] if d['cross_page_rate'] is None else round(d['cross_page_rate'],3)} "
              f"null={d['null_mean']:.3f} z={d['z'] and round(d['z'],1)} p={d['p_perm']:.4f}")
    print()
json.dump(out, open('phase6_anchoring2.json', 'w'), indent=1)
print("checkpoint -> phase6_anchoring2.json")
