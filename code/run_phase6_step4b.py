#!/usr/bin/env python3
"""Phase 6 step 4b: stricter recurrence variants.
V1: exact match only, raw words.
V2: exact match after stripping the paragraph-initial gallows dressing
    (phase 4: GALL filled 84% at paragraph starts = positional ornament).
    Strip = remove leading gallows glyph (k,t,p,f,ckh,cth,cph,cfh) if present.
Same transformation applied to null draws. -> phase6_plantpairs_strict.json"""
import json, random
from collections import defaultdict
import numpy as np
from phase6_lib import extract_loci, split_loci
from phase4_lib import glyphs

rng = random.Random(44)
loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

CONSENSUS = ['f1v', 'f2r', 'f2v', 'f9v', 'f15v', 'f16r', 'f17v']

first_para_word, seen = {}, set()
folio_section = {}
for p in paras:
    folio_section[p['folio']] = p['section']
    if p['locator'] in '@*' and p['words'] and p['folio'] not in seen:
        first_para_word[p['folio']] = p['words'][0]
        seen.add(p['folio'])

pharma_vocab = set()
for l in labels:
    if l['section'] == 'pharma':
        pharma_vocab.update(l['words'])
for p in paras:
    if p['section'] == 'pharma':
        pharma_vocab.update(p['words'])

GALLOWS = ('ckh', 'cth', 'cph', 'cfh', 'k', 't', 'p', 'f')
def strip_gallows(w):
    g = glyphs(w)
    if g and g[0] in GALLOWS:
        return ''.join(g[1:])
    return w

cand = [first_para_word[f] for f in CONSENSUS if f in first_para_word]
herbal_first = [w for f, w in first_para_word.items()
                if folio_section.get(f) == 'herbal' and f not in CONSENSUS]

def test(words, pool, transform, label):
    tw = [transform(w) for w in words]
    obs = sum(1 for w in tw if w in pool)
    null = []
    for _ in range(20000):
        s = [transform(w) for w in rng.sample(herbal_first, len(words))]
        null.append(sum(1 for w in s if w in pool))
    null = np.array(null)
    p = float((null >= obs).mean())
    print(f"{label}: {obs}/{len(words)} (words: "
          f"{[w + ('->' + t if t != w else '') for w, t in zip(words, tw)]})")
    print(f"   null {null.mean():.2f}±{null.std():.2f} p={p:.4f}")
    return {'obs': obs, 'n': len(words), 'null_mean': float(null.mean()),
            'null_std': float(null.std()), 'p': p,
            'matched': [t for t in tw if t in pool]}

out = {}
out['exact_raw'] = test(cand, pharma_vocab, lambda w: w, "V1 exact, raw")
out['exact_stripped'] = test(cand, pharma_vocab, strip_gallows, "V2 exact, gallows-stripped")
json.dump(out, open('phase6_plantpairs_strict.json', 'w'), indent=1)
print("checkpoint -> phase6_plantpairs_strict.json")
