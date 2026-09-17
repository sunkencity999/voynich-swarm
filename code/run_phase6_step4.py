#!/usr/bin/env python3
"""Phase 6 step 4: consensus plant-ID pairing.
Consensus folios (>=2 independent sources agree; sources in REPORT_phase6.md):
  f1v Atropa belladonna | f2r Centaurea | f2v Nymphoides (water lily type)
  f9v Viola tricolor    | f15v Paris quadrifolia | f16r Cannabis
  f17v Dioscorea/Tamus communis
Candidate 'plant name' = first word of the folio's first paragraph
(paragraph-initial position; medieval herbal convention) + any label words
on the folio. Tests:
  (A) do candidate names share slot/family signature beyond chance?
  (B) do candidates recur in the pharma section (Lf/Lc labels or text),
      exact or edit-distance<=1, vs null of random herbal page-initial words?
Checkpoint -> phase6_plantpairs.json
"""
import json, random
from collections import Counter, defaultdict
import numpy as np
from phase6_lib import extract_loci, split_loci, edit_distance
from phase4_lib import parse_word, glyphs

rng = random.Random(4)
loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

CONSENSUS = {
    'f1v': 'Atropa belladonna (deadly nightshade)',
    'f2r': 'Centaurea (knapweed/cornflower)',
    'f2v': 'Nymphoides/Nymphaea (water lily)',
    'f9v': 'Viola tricolor (heartsease)',
    'f15v': 'Paris quadrifolia (herb Paris)',
    'f16r': 'Cannabis (hemp)',
    'f17v': 'Dioscorea communis/Tamus (black bryony)',
}

# --- gather per-folio material ---
first_para_word = {}
para_initial_words = defaultdict(list)   # all paragraph-initial words per folio
folio_labels = defaultdict(list)
folio_section = {}
seen_first = set()
for p in paras:
    folio_section[p['folio']] = p['section']
    if p['locator'] in '@*' and p['words']:
        para_initial_words[p['folio']].append(p['words'][0])
        if p['folio'] not in seen_first:
            first_para_word[p['folio']] = p['words'][0]
            seen_first.add(p['folio'])
for l in labels:
    for w in l['words']:
        folio_labels[l['folio']].append(w)

# pharma vocab pools
pharma_label_words = set()
pharma_text_words = set()
for l in labels:
    if l['section'] == 'pharma':
        pharma_label_words.update(l['words'])
for p in paras:
    if p['section'] == 'pharma':
        pharma_text_words.update(p['words'])
print(f"pharma label vocab: {len(pharma_label_words)}, pharma text vocab: {len(pharma_text_words)}")

def near(w, pool):
    """exact or edit-distance-1 match in pool (only for len>=4 to avoid noise)."""
    if w in pool:
        return w, 0
    if len(w) >= 4:
        for v in pool:
            if abs(len(v) - len(w)) <= 1 and edit_distance(w, v) == 1:
                return v, 1
    return None, None

rows = []
for f, ident in CONSENSUS.items():
    cands = []
    if f in first_para_word:
        cands.append(('para-initial', first_para_word[f]))
    for w in folio_labels.get(f, []):
        cands.append(('label', w))
    for kind, w in cands:
        pl, dl = near(w, pharma_label_words)
        pt, dt = near(w, pharma_text_words)
        s, _ = parse_word(w)
        g = glyphs(w)
        rows.append({'folio': f, 'id': ident, 'kind': kind, 'word': w,
                     'prefix2': ''.join(g[:2]),
                     'gallows': s['GALL'] if s else None,
                     'pharma_label_match': pl, 'pharma_label_dist': dl,
                     'pharma_text_match': pt, 'pharma_text_dist': dt})

print("\ncandidate table:")
for r in rows:
    print(f"  {r['folio']:5s} {r['kind']:12s} {r['word']:12s} pref={r['prefix2']:4s} "
          f"g={r['gallows'] or '-':3s} pharmaLab={r['pharma_label_match'] or '-'} "
          f"pharmaTxt={r['pharma_text_match'] or '-'}")

# --- (A) family signature consistency among para-initial candidates ---
cand_words = [r['word'] for r in rows if r['kind'] == 'para-initial']
def sig_stat(words):
    prefs = Counter(''.join(glyphs(w)[:1]) for w in words)   # first glyph
    return max(prefs.values()) / len(words)                  # modal first-glyph share

obs_sig = sig_stat(cand_words)
herbal_first = [w for f, w in first_para_word.items()
                if folio_section.get(f) == 'herbal' and f not in CONSENSUS]
null_sig = []
for _ in range(20000):
    null_sig.append(sig_stat(rng.sample(herbal_first, len(cand_words))))
null_sig = np.array(null_sig)
pA = float((null_sig >= obs_sig).mean())
print(f"\n(A) modal first-glyph share among {len(cand_words)} candidates: {obs_sig:.3f} "
      f"null {null_sig.mean():.3f}±{null_sig.std():.3f} p={pA:.4f}")

# --- (B) pharma recurrence vs null ---
_recur_cache = {}
def recurs(w):
    if w not in _recur_cache:
        _recur_cache[w] = bool(near(w, pharma_label_words)[0] or near(w, pharma_text_words)[0])
    return _recur_cache[w]

def recur_count(words):
    return sum(1 for w in words if recurs(w))

obs_rec = recur_count(cand_words)
null_rec = []
for _ in range(20000):
    null_rec.append(recur_count(rng.sample(herbal_first, len(cand_words))))
null_rec = np.array(null_rec)
pB = float((null_rec >= obs_rec).mean())
print(f"(B) pharma recurrence (exact or ed<=1): {obs_rec}/{len(cand_words)} "
      f"null {null_rec.mean():.2f}±{null_rec.std():.2f} p={pB:.4f}")

# how common is pharma recurrence for ANY herbal page-initial word (base rate)?
base_rec = recur_count(herbal_first) / len(herbal_first)
print(f"    base rate over all {len(herbal_first)} herbal page-initial words: {base_rec:.3f}")

json.dump({'consensus': CONSENSUS, 'candidates': rows,
           'sig_test': {'obs_modal_first_glyph': obs_sig, 'null_mean': float(null_sig.mean()),
                        'null_std': float(null_sig.std()), 'p': pA},
           'recurrence_test': {'obs': obs_rec, 'n': len(cand_words),
                               'null_mean': float(null_rec.mean()),
                               'null_std': float(null_rec.std()), 'p': pB,
                               'herbal_base_rate': base_rec}},
          open('phase6_plantpairs.json', 'w'), indent=1)
print("\ncheckpoint -> phase6_plantpairs.json")
