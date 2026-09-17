#!/usr/bin/env python3
"""Voynich phase 4: slot-grammar decomposition + verbose-cipher attack.

Steps:
  1. fit slot grammar (phase4_lib), report coverage + per-slot inventories
  2. per-slot entropy; within-word slot-pair MI; sequential slot MI
  3. residue extraction + ciphertext statistics vs Latin/Italian letters
  4. verbose-padding test: info content vs word length (Voynich vs Latin)
  5. line-position and Currier A/B effects
All shuffle-corrected where MLE bias matters. Results -> phase4_results.json.
"""
import json, math, random, re, sys
from collections import Counter, defaultdict
import phase4_lib as L

rng = random.Random(1234)
R = {}  # results

# ---------------------------------------------------------------- extraction
lines = L.extract_structured('ZL3b-n.txt')
words_all = [w for ln in lines for w in ln['words']]
print(f"[extract] lines={len(lines)} words={len(words_all)}", flush=True)

# ---------------------------------------------------------------- 1. grammar
parses = {}   # word -> (slots, pass_no)
for w in set(words_all):
    parses[w] = L.parse_word(w)
n = len(words_all)
cov = Counter(parses[w][1] for w in words_all)
R['grammar'] = {
    'n_slots': len(L.SLOT_NAMES), 'slot_names': L.SLOT_NAMES,
    'coverage_pass1': cov[1]/n, 'coverage_pass2': cov[2]/n,
    'coverage_pass3': cov[3]/n, 'coverage_total': (cov[1]+cov[2]+cov[3])/n,
    'coverage_types': sum(1 for w in parses if parses[w][1]) / len(parses),
}
print(f"[grammar] token coverage={R['grammar']['coverage_total']:.4f} "
      f"type coverage={R['grammar']['coverage_types']:.4f}", flush=True)

# parsed token stream (with line structure preserved)
plines = []
for ln in lines:
    pl = []
    for w in ln['words']:
        s, p = parses[w]
        pl.append((w, s if p else None))
    plines.append({**ln, 'parsed': pl})

# slot fill matrix over parsed tokens (in reading order)
tok_slots = []   # list of dicts, parsed words only, but keep index into full stream
stream = []      # (word, slots-or-None, line_idx, pos_in_line, line_len)
for li, ln in enumerate(plines):
    for pi, (w, s) in enumerate(ln['parsed']):
        stream.append((w, s, li, pi, len(ln['parsed'])))
        if s: tok_slots.append(s)
NP = len(tok_slots)
print(f"[grammar] parsed tokens={NP}", flush=True)

# per-slot inventories
inv = {}
for sl in L.SLOT_NAMES:
    c = Counter(s[sl] for s in tok_slots)
    inv[sl] = {'n_values': len(c), 'fill_rate': 1 - c.get('', 0)/NP,
               'top': c.most_common(8), 'entropy': L.H(c)}
R['slots'] = inv

# ---------------------------------------------------------------- 2. MI maps
cols = {sl: [s[sl] for s in tok_slots] for sl in L.SLOT_NAMES}

# 2a. within-word slot-pair MI (shuffle-corrected)
within = {}
for i, a in enumerate(L.SLOT_NAMES):
    for b in L.SLOT_NAMES[i+1:]:
        corr, raw, bm, bs = L.mi_corrected(cols[a], cols[b], nshuf=5, rng=rng)
        within[f"{a}|{b}"] = {'mi': corr, 'raw': raw, 'noise': bs}
R['within_word_mi'] = within
top_w = sorted(within.items(), key=lambda kv: -kv[1]['mi'])[:12]
print("[MI-within] top:", [(k, round(v['mi'],3)) for k,v in top_w[:6]], flush=True)

# 2b. sequential: adjacent parsed pairs within the same line
pairs = []
for i in range(len(stream)-1):
    w1, s1, l1, p1, _ = stream[i]
    w2, s2, l2, p2, _ = stream[i+1]
    if l1 == l2 and s1 and s2:
        pairs.append((s1, s2, w1, w2))
print(f"[seq] within-line parsed adjacent pairs={len(pairs)}", flush=True)

seq = {}
for a in L.SLOT_NAMES:
    xs = [p[0][a] for p in pairs]
    for b in L.SLOT_NAMES:
        ys = [p[1][b] for p in pairs]
        corr, raw, bm, bs = L.mi_corrected(xs, ys, nshuf=5, rng=rng)
        seq[f"{a}->{b}"] = {'mi': corr, 'noise': bs}
R['seq_slot_mi'] = seq
top_s = sorted(seq.items(), key=lambda kv: -kv[1]['mi'])[:15]
print("[MI-seq] top:", [(k, round(v['mi'],4)) for k,v in top_s[:8]], flush=True)

# 2c. each slot vs next WORD identity; and word->word reference
next_words = [p[3] for p in pairs]
slot_vs_next = {}
for a in L.SLOT_NAMES:
    xs = [p[0][a] for p in pairs]
    corr, raw, bm, bs = L.mi_corrected(xs, next_words, nshuf=5, rng=rng)
    slot_vs_next[a] = {'mi': corr, 'noise': bs}
R['slot_vs_next_word'] = slot_vs_next
cur_words = [p[2] for p in pairs]
corr, raw, bm, bs = L.mi_corrected(cur_words, next_words, nshuf=5, rng=rng)
R['word_vs_next_word'] = {'mi': corr, 'raw': raw, 'noise': bs}
# also: which slot of the NEXT word does the CURRENT WORD identity predict?
word_vs_next_slot = {}
for b in L.SLOT_NAMES:
    ys = [p[1][b] for p in pairs]
    corr, raw, bm, bs = L.mi_corrected(cur_words, ys, nshuf=5, rng=rng)
    word_vs_next_slot[b] = {'mi': corr, 'noise': bs}
R['word_vs_next_slot'] = word_vs_next_slot
# word length (in glyphs) sequential coupling + vs next word
lens = [len(L.glyphs(p[2])) for p in pairs]
lens2 = [len(L.glyphs(p[3])) for p in pairs]
corr, raw, bm, bs = L.mi_corrected(lens, lens2, nshuf=5, rng=rng)
R['len_vs_next_len'] = {'mi': corr, 'noise': bs}
corr, raw, bm, bs = L.mi_corrected(lens, next_words, nshuf=5, rng=rng)
R['len_vs_next_word'] = {'mi': corr, 'noise': bs}
print(f"[seq] word->word MI={R['word_vs_next_word']['mi']:.4f}", flush=True)

json.dump(R, open('phase4_results_partial.json', 'w'), indent=1, default=str)
print("[checkpoint] partial results saved", flush=True)

# ---------------------------------------------------------------- 3. residue
# rank slots by entropy; residue = concatenation of slots covering the bulk of
# per-word entropy. Threshold: keep slots with H >= 0.9 bits (majority carriers).
slot_H = {sl: inv[sl]['entropy'] for sl in L.SLOT_NAMES}
keep = [sl for sl in L.SLOT_NAMES if slot_H[sl] >= 0.9]
drop = [sl for sl in L.SLOT_NAMES if sl not in keep]
R['residue_def'] = {'kept_slots': keep, 'dropped_slots': drop,
                    'kept_H_sum': sum(slot_H[s] for s in keep),
                    'total_H_sum': sum(slot_H.values())}
print(f"[residue] keep={keep} ({R['residue_def']['kept_H_sum']:.2f} of "
      f"{R['residue_def']['total_H_sum']:.2f} independent-slot bits)", flush=True)

def residue_of(slots):
    return ''.join(slots[sl] for sl in keep)

res_words = [residue_of(s) for s in tok_slots]
res_stream = []
for rw in res_words:
    res_stream.extend(L.glyphs(rw))

def analyze_symbol_stream(sym):
    c0 = Counter(sym)
    h = L.cond_entropy_orders(sym, 2)
    return c0, h

res_c0, res_h = analyze_symbol_stream(res_stream)
R['residue'] = {
    'n_symbols': len(res_stream), 'alphabet': len(res_c0),
    'empty_residue_rate': sum(1 for r in res_words if not r)/len(res_words),
    'mean_len': len(res_stream)/len(res_words),
    'H_orders': res_h, 'top_symbols': res_c0.most_common(30),
}
print(f"[residue] alphabet={len(res_c0)} H0={res_h[0]:.3f} H1={res_h[1]:.3f} "
      f"H2={res_h[2]:.3f} meanlen={R['residue']['mean_len']:.2f}", flush=True)

# --- comparison letter distributions
def letters(path, drop_vowels=False):
    txt = open(path, encoding='utf-8', errors='ignore').read().lower()
    txt = re.sub(r'[^a-z]', '', txt)
    if drop_vowels:
        txt = re.sub(r'[aeiou]', '', txt)
    return Counter(txt)

lat = letters('raw_latin.txt'); ita = letters('raw_italian.txt')
lat_nv = letters('raw_latin.txt', drop_vowels=True)
# roman-numeral-like: letter distribution of roman numerals 1..2000
def roman(num):
    vals = [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),(100,'c'),(90,'xc'),
            (50,'l'),(40,'xl'),(10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]
    out = ''
    for v, s in vals:
        while num >= v: out += s; num -= v
    return out
rom = Counter(''.join(roman(i) for i in range(1, 2001)))

res_p = L.rank_probs(res_c0)
comps = {'latin': lat, 'italian': ita, 'latin_novowel': lat_nv, 'roman': rom}
R['residue_vs'] = {}
for name, c in comps.items():
    q = L.rank_probs(c)
    R['residue_vs'][name] = {'chi2_rank': L.chi2_rank(res_p, q),
                             'js_rank': L.js_divergence(res_p, q),
                             'alphabet': len(c)}
# reference: latin vs italian (how close are two real languages on this metric?)
R['residue_vs']['REF_latin_vs_italian'] = {
    'chi2_rank': L.chi2_rank(L.rank_probs(lat), L.rank_probs(ita)),
    'js_rank': L.js_divergence(L.rank_probs(lat), L.rank_probs(ita))}
R['residue_vs']['REF_latin_vs_latin_novowel'] = {
    'chi2_rank': L.chi2_rank(L.rank_probs(lat), L.rank_probs(lat_nv)),
    'js_rank': L.js_divergence(L.rank_probs(lat), L.rank_probs(lat_nv))}
# and full-word voynich glyph stream (no residue) for contrast
full_stream = []
for w in words_all:
    full_stream.extend(L.glyphs(w))
full_c0 = Counter(full_stream)
R['residue_vs']['REF_fullvoynich_vs_latin'] = {
    'chi2_rank': L.chi2_rank(L.rank_probs(full_c0), L.rank_probs(lat)),
    'js_rank': L.js_divergence(L.rank_probs(full_c0), L.rank_probs(lat))}
# residue entropy comparisons for latin letter stream (size-matched)
lat_txt = re.sub(r'[^a-z]', '', open('raw_latin.txt', encoding='utf-8', errors='ignore').read().lower())[:len(res_stream)]
R['latin_letter_H_orders'] = L.cond_entropy_orders(list(lat_txt), 2)
lat_nv_txt = re.sub(r'[aeiou]', '', lat_txt)[:len(res_stream)]
R['latin_novowel_H_orders'] = L.cond_entropy_orders(list(lat_nv_txt), 2)
print("[residue] vs:", {k: round(v['js_rank'],4) for k,v in R['residue_vs'].items()}, flush=True)

# residue sequential MI (does the residue carry the phase-2 word-order signal?)
res_pairs_x, res_pairs_y = [], []
for s1, s2, _, _ in pairs:
    res_pairs_x.append(residue_of(s1)); res_pairs_y.append(residue_of(s2))
corr, raw, bm, bs = L.mi_corrected(res_pairs_x, res_pairs_y, nshuf=5, rng=rng)
R['residue_seq_mi'] = {'mi': corr, 'noise': bs}
# and the dropped-slot "shell": what the padding carries
def shell_of(slots): return ''.join(slots[sl] for sl in drop)
sh_x = [shell_of(s1) for s1, s2, _, _ in pairs]
sh_y = [shell_of(s2) for s1, s2, _, _ in pairs]
corr2, raw2, bm2, bs2 = L.mi_corrected(sh_x, sh_y, nshuf=5, rng=rng)
R['shell_seq_mi'] = {'mi': corr2, 'noise': bs2}
print(f"[residue] seq MI residue={R['residue_seq_mi']['mi']:.4f} "
      f"shell={R['shell_seq_mi']['mi']:.4f} (word-word {R['word_vs_next_word']['mi']:.4f})", flush=True)

json.dump(R, open('phase4_results_partial.json', 'w'), indent=1, default=str)

# ---------------------------------------------------------------- 4. padding
# info content per word vs length in glyphs.
# Model A (voynich): sum of per-slot surprisal under independent slot model.
slot_p = {sl: {v: c/NP for v, c in Counter(cols[sl]).items()} for sl in L.SLOT_NAMES}
def word_info_slots(slots):
    return -sum(math.log2(slot_p[sl][slots[sl]]) for sl in L.SLOT_NAMES)

# Model B (any corpus): -log2 unigram word probability vs length.
def info_vs_len_unigram(words):
    c = Counter(words); n = len(words)
    by_len = defaultdict(list)
    for w, k in c.items():
        by_len[len(L.glyphs(w))].append((-math.log2(k/n), k))
    out = {}
    for ln_, vals in sorted(by_len.items()):
        tot = sum(k for _, k in vals)
        mean = sum(i*k for i, k in vals)/tot
        out[ln_] = {'mean_info': mean, 'n': tot}
    return out

# Model C: char-bigram model surprisal vs length (comparable across corpora)
def info_vs_len_bigram(words, tokenizer):
    # fit char bigram model with add-0.5 smoothing over the word-internal stream
    big = Counter(); uni = Counter()
    toks = [tokenizer(w) for w in words]
    for t in toks:
        seq = ['^'] + t + ['$']
        for a, b in zip(seq, seq[1:]):
            big[(a, b)] += 1; uni[a] += 1
    V = len(set(b for _, b in big)) + 1
    def winfo(t):
        seq = ['^'] + t + ['$']
        return -sum(math.log2((big[(a, b)] + 0.5)/(uni[a] + 0.5*V))
                    for a, b in zip(seq, seq[1:]))
    by_len = defaultdict(list)
    for t in toks:
        by_len[len(t)].append(winfo(t))
    return {ln_: {'mean_info': sum(v)/len(v), 'n': len(v)}
            for ln_, v in sorted(by_len.items())}

voy_parsed_words = [w for w, s, _, _, _ in stream if s]
voy_slots_by_word = [parses[w][0] for w in voy_parsed_words]
by_len_slots = defaultdict(list)
for w, s in zip(voy_parsed_words, voy_slots_by_word):
    by_len_slots[len(L.glyphs(w))].append(word_info_slots(s))
R['pad_voy_slotinfo'] = {ln_: {'mean_info': sum(v)/len(v), 'n': len(v)}
                         for ln_, v in sorted(by_len_slots.items())}

lat_words = re.findall(r'[a-z]+', open('corpus_latin.txt').read())
R['pad_voy_unigram'] = info_vs_len_unigram(words_all)
R['pad_lat_unigram'] = info_vs_len_unigram(lat_words)
R['pad_voy_bigram'] = info_vs_len_bigram(words_all, L.glyphs)
R['pad_lat_bigram'] = info_vs_len_bigram(lat_words, list)

def slope(d, lo=2, hi=9):
    xs = [k for k in d if lo <= k <= hi and d[k]['n'] >= 30]
    if len(xs) < 3: return None
    ys = [d[k]['mean_info'] for k in xs]
    mx, my = sum(xs)/len(xs), sum(ys)/len(ys)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs)

R['pad_slopes'] = {
    'voy_slotinfo_bits_per_glyph': slope(R['pad_voy_slotinfo']),
    'voy_unigram_bits_per_glyph': slope(R['pad_voy_unigram']),
    'lat_unigram_bits_per_letter': slope(R['pad_lat_unigram']),
    'voy_bigram_bits_per_glyph': slope(R['pad_voy_bigram']),
    'lat_bigram_bits_per_letter': slope(R['pad_lat_bigram']),
}
print("[padding] slopes:", {k: round(v,3) for k,v in R['pad_slopes'].items() if v}, flush=True)

json.dump(R, open('phase4_results_partial.json', 'w'), indent=1, default=str)

# ---------------------------------------------------------------- 5. position
# line-initial vs mid vs final slot distributions
posbuck = {'initial': [], 'mid': [], 'final': []}
for w, s, li, pi, ll in stream:
    if not s: continue
    if pi == 0: posbuck['initial'].append(s)
    elif pi == ll-1: posbuck['final'].append(s)
    else: posbuck['mid'].append(s)
pos_stats = {}
for sl in L.SLOT_NAMES:
    entry = {}
    for pos, arr in posbuck.items():
        c = Counter(x[sl] for x in arr)
        n_ = len(arr)
        entry[pos] = {'fill': 1 - c.get('', 0)/n_, 'H': L.H(c)}
    pos_stats[sl] = entry
R['line_position'] = {sl: pos_stats[sl] for sl in L.SLOT_NAMES}
R['line_position_n'] = {k: len(v) for k, v in posbuck.items()}
gall_init = pos_stats['GALL']['initial']['fill']
gall_mid = pos_stats['GALL']['mid']['fill']
print(f"[line] GALL fill initial={gall_init:.3f} mid={gall_mid:.3f}", flush=True)

# sequential MI within-line vs across-line-boundary (word identity level)
cross = []
for i in range(len(stream)-1):
    w1, s1, l1, p1, _ = stream[i]
    w2, s2, l2, p2, _ = stream[i+1]
    if l1 != l2:
        cross.append((w1, w2))
if len(cross) > 500:
    xs, ys = [c[0] for c in cross], [c[1] for c in cross]
    corr, raw, bm, bs = L.mi_corrected(xs, ys, nshuf=5, rng=rng)
    R['crossline_word_mi'] = {'mi': corr, 'noise': bs, 'n_pairs': len(cross)}
    print(f"[line] cross-line word MI={corr:.4f} (n={len(cross)})", flush=True)

# ---------------------------------------------------------------- 6. A vs B
AB = {}
for lang in ('A', 'B'):
    lw = [w for ln in lines if ln['lang'] == lang for w in ln['words']]
    ps = [parses[w] for w in lw]
    covd = sum(1 for _, p in ps if p)/len(lw)
    slots_l = [s for s, p in ps if p]
    ent = {sl: L.H(Counter(x[sl] for x in slots_l)) for sl in L.SLOT_NAMES}
    fill = {sl: sum(1 for x in slots_l if x[sl])/len(slots_l) for sl in L.SLOT_NAMES}
    AB[lang] = {'n_words': len(lw), 'coverage': covd, 'slot_H': ent, 'slot_fill': fill}
# JS divergence per slot between A and B fills
slots_A = [parses[w][0] for ln in lines if ln['lang']=='A' for w in ln['words'] if parses[w][1]]
slots_B = [parses[w][0] for ln in lines if ln['lang']=='B' for w in ln['words'] if parses[w][1]]
js_ab = {}
for sl in L.SLOT_NAMES:
    ca, cb = Counter(x[sl] for x in slots_A), Counter(x[sl] for x in slots_B)
    na, nb = sum(ca.values()), sum(cb.values())
    keys = set(ca) | set(cb)
    p = [ca.get(k,0)/na for k in keys]; q = [cb.get(k,0)/nb for k in keys]
    # aligned JS (not rank-sorted: same symbols)
    d = 0.0
    for pi, qi in zip(p, q):
        m_ = (pi+qi)/2
        if pi: d += 0.5*pi*math.log2(pi/m_)
        if qi: d += 0.5*qi*math.log2(qi/m_)
    js_ab[sl] = d
AB['js_per_slot'] = js_ab
R['currier_AB'] = AB
print("[A/B] JS per slot:", {k: round(v,3) for k,v in sorted(js_ab.items(), key=lambda kv:-kv[1])[:6]}, flush=True)

json.dump(R, open('phase4_results.json', 'w'), indent=1, default=str)
print("[done] phase4_results.json written", flush=True)
