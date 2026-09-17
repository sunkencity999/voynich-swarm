#!/usr/bin/env python3
"""Phase 6 step 2: label lexicon analysis.
(a) labels vs paragraph words: length, slot-grammar profile
(b) label-enriched morphological families; overlap with phase-5 section-locked words
(c) label->same-page paragraph anchoring rate vs permutation null
Checkpoint -> phase6_lexicon.json
"""
import json, math, random
from collections import Counter, defaultdict
import numpy as np
from phase6_lib import extract_loci, split_loci
from phase4_lib import parse_word, glyphs, SLOT_NAMES

rng = random.Random(6)
loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

label_tokens = [(l['folio'], l['section'], w) for l in labels for w in l['words']]
para_words_by_folio = defaultdict(list)
for p in paras:
    para_words_by_folio[p['folio']].extend(p['words'])
para_tokens = [(p['folio'], p['section'], w) for p in paras for w in p['words']]

out = {}

# ---------------- (a) structural comparison ----------------
def profile(words):
    n = len(words)
    lens = [len(w) for w in words]
    glens = [len(glyphs(w)) for w in words]
    parsed = 0
    fill = Counter()
    for w in words:
        s, p = parse_word(w)
        if s:
            parsed += 1
            for k in SLOT_NAMES:
                if s[k]:
                    fill[k] += 1
    return {'n': n, 'mean_len': float(np.mean(lens)), 'mean_glyphs': float(np.mean(glens)),
            'parse_rate': parsed / n,
            'fill_rates': {k: fill[k] / max(parsed, 1) for k in SLOT_NAMES}}

# compare within sections that have enough labels
secs = ['zodiac', 'pharma', 'astro', 'balneo', 'cosmo', 'herbal']
cmp_tbl = {}
for sec in secs + ['ALL']:
    lw = [w for f, s, w in label_tokens if (s == sec or sec == 'ALL')]
    pw = [w for f, s, w in para_tokens if (s == sec or sec == 'ALL')]
    if len(lw) >= 25 and len(pw) >= 100:
        cmp_tbl[sec] = {'labels': profile(lw), 'paras': profile(pw)}
out['structure'] = cmp_tbl
for sec, d in cmp_tbl.items():
    L, P = d['labels'], d['paras']
    print(f"{sec:7s} labels n={L['n']:4d} len={L['mean_len']:.2f} parse={L['parse_rate']:.2f} | "
          f"paras n={P['n']:5d} len={P['mean_len']:.2f} parse={P['parse_rate']:.2f}")

# slot fill deltas (ALL)
A = cmp_tbl['ALL']
print("\nslot fill (labels vs paras, ALL):")
deltas = {}
for k in SLOT_NAMES:
    a, b = A['labels']['fill_rates'][k], A['paras']['fill_rates'][k]
    deltas[k] = (a, b)
    if abs(a - b) > 0.04:
        print(f"  {k:7s} label {a:.3f}  para {b:.3f}  Δ{a-b:+.3f}")
out['slot_fill_all'] = {k: {'label': v[0], 'para': v[1]} for k, v in deltas.items()}

# ---------------- (b) families ----------------
# family = first two glyphs (glyph tokenizer handles benched chars as units)
def fam(w):
    g = glyphs(w)
    return ''.join(g[:2]) if len(g) >= 2 else g[0] if g else ''

all_tokens_corpus = [w for f, s, w in para_tokens] + [w for f, s, w in label_tokens]
fam_tot = Counter(fam(w) for w in all_tokens_corpus)
fam_lab = Counter(fam(w) for f, s, w in label_tokens)
n_lab = len(label_tokens); n_tot = len(all_tokens_corpus)
base = n_lab / n_tot
rows = []
for f, c in fam_tot.items():
    if c < 30 or not f:
        continue
    lc = fam_lab.get(f, 0)
    exp = c * base
    enr = (lc / c) / base if c else 0
    # binomial z
    var = c * base * (1 - base)
    z = (lc - exp) / math.sqrt(var) if var > 0 else 0.0
    rows.append({'family': f, 'corpus_n': c, 'label_n': lc, 'enrichment': enr, 'z': z})
rows.sort(key=lambda r: -r['z'])
out['label_families_top'] = rows[:25]
out['label_families_bottom'] = rows[-10:]
print("\ntop label-enriched families (first-2-glyph, corpus n>=30):")
for r in rows[:20]:
    print(f"  {r['family']:6s} corpus={r['corpus_n']:5d} label={r['label_n']:3d} "
          f"enr={r['enrichment']:.2f} z={r['z']:+.1f}")
print("most label-avoidant families:")
for r in rows[-8:]:
    print(f"  {r['family']:6s} corpus={r['corpus_n']:5d} label={r['label_n']:3d} "
          f"enr={r['enrichment']:.2f} z={r['z']:+.1f}")

# phase-5 section-locked words as labels?
p5 = json.load(open('phase5_results.json'))
locked = [w['word'] for w in p5.get('section_locked_top', [])] if 'section_locked_top' in p5 else []
if not locked:
    # fall back to the report's table
    locked = ['oteos','qokeody','olkedy','cthor','otchol','olshedy','cthy','kchy',
              'ckhey','qol','lkaiin','ykchy','kchor','lkain','olkain','dchor',
              'lkar','dchy','oteody','qokeol']
flat = ['okar','r','saiin','y','or','chey','okal','chckhy','sheey','dar',
        'okaiin','otal','chdy','dal','shey','dain','aiin','oty','cheey','qokar']
lab_freq = Counter(w for f, s, w in label_tokens)
para_freq = Counter(w for f, s, w in para_tokens)
def label_rate(ws):
    rows = []
    for w in ws:
        lt, pt = lab_freq.get(w, 0), para_freq.get(w, 0)
        rows.append({'word': w, 'label_n': lt, 'para_n': pt,
                     'label_share': lt / (lt + pt) if lt + pt else 0})
    return rows
out['locked_as_labels'] = label_rate(locked)
out['flat_as_labels'] = label_rate(flat)
ls = sum(r['label_n'] for r in out['locked_as_labels']); ps = sum(r['para_n'] for r in out['locked_as_labels'])
fs = sum(r['label_n'] for r in out['flat_as_labels']); fp = sum(r['para_n'] for r in out['flat_as_labels'])
print(f"\nphase-5 section-locked top20: label share {ls}/{ls+ps} = {ls/(ls+ps):.4f}")
print(f"phase-5 section-flat top20:   label share {fs}/{fs+fp} = {fs/(fs+fp):.4f}")
print(f"corpus base rate: {base:.4f}")

# ---------------- (c) anchoring rate ----------------
def anchoring(min_len=1, nperm=10000):
    # group label words by (section, folio)
    page_labels = defaultdict(list)
    for f, s, w in label_tokens:
        if len(w) >= min_len:
            page_labels[(s, f)].append(w)
    results = {}
    per_sec = {}
    obs_hits = obs_n = 0
    sec_groups = defaultdict(list)   # section -> list of (folio, words)
    for (s, f), ws in page_labels.items():
        if f in para_words_by_folio and para_words_by_folio[f]:
            sec_groups[s].append((f, ws))
    for s, grp in sec_groups.items():
        folios = [f for f, ws in grp]
        para_sets = {f: set(para_words_by_folio[f]) for f in folios}
        hits = sum(1 for f, ws in grp for w in ws if w in para_sets[f])
        n = sum(len(ws) for f, ws in grp)
        obs_hits += hits; obs_n += n
        # cross-page baseline: word vs a different page in same section
        cross_hits = cross_n = 0
        for f, ws in grp:
            for g in folios:
                if g == f:
                    continue
                cross_hits += sum(1 for w in ws if w in para_sets[g])
                cross_n += len(ws)
        # permutation null within section
        null = []
        wordsets = [ws for f, ws in grp]
        for _ in range(nperm):
            perm = folios[:]
            rng.shuffle(perm)
            h = sum(1 for ws, f in zip(wordsets, perm) for w in ws if w in para_sets[f])
            null.append(h / n)
        null = np.array(null)
        obs = hits / n
        p = float((null >= obs).mean())
        per_sec[s] = {'n_label_words': n, 'same_page_rate': obs,
                      'cross_page_rate': cross_hits / cross_n if cross_n else None,
                      'null_mean': float(null.mean()), 'null_std': float(null.std()),
                      'z': float((obs - null.mean()) / null.std()) if null.std() > 0 else None,
                      'p_perm': p, 'n_pages': len(folios)}
    # pooled: permute within section, sum
    pooled_null = np.zeros(nperm)
    for s, grp in sec_groups.items():
        folios = [f for f, ws in grp]
        para_sets = {f: set(para_words_by_folio[f]) for f in folios}
        wordsets = [ws for f, ws in grp]
        n_s = sum(len(ws) for ws in wordsets)
        for i in range(nperm):
            perm = folios[:]
            rng.shuffle(perm)
            pooled_null[i] += sum(1 for ws, f in zip(wordsets, perm) for w in ws if w in para_sets[f])
    pooled_null /= obs_n
    obs_rate = obs_hits / obs_n
    results['per_section'] = per_sec
    results['pooled'] = {'n_label_words': obs_n, 'same_page_rate': obs_rate,
                         'null_mean': float(pooled_null.mean()),
                         'null_std': float(pooled_null.std()),
                         'z': float((obs_rate - pooled_null.mean()) / pooled_null.std()),
                         'p_perm': float((pooled_null >= obs_rate).mean())}
    return results

for ml, key in [(1, 'anchoring_all'), (3, 'anchoring_len3')]:
    r = anchoring(min_len=ml)
    out[key] = r
    P = r['pooled']
    print(f"\nanchoring (min word len {ml}): same-page {P['same_page_rate']:.3f} "
          f"null {P['null_mean']:.3f}±{P['null_std']:.3f} z={P['z']:.1f} p={P['p_perm']:.5f}")
    for s, d in sorted(r['per_section'].items()):
        print(f"  {s:8s} n={d['n_label_words']:4d} pages={d['n_pages']:3d} same={d['same_page_rate']:.3f} "
              f"cross={d['cross_page_rate'] if d['cross_page_rate'] is None else round(d['cross_page_rate'],3)} "
              f"null={d['null_mean']:.3f} z={d['z'] and round(d['z'],1)} p={d['p_perm']:.4f}")

json.dump(out, open('phase6_lexicon.json', 'w'), indent=1)
print("\ncheckpoint -> phase6_lexicon.json")
