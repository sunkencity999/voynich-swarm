#!/usr/bin/env python3
"""Phase 3: self-citation falsification test.

Implements a Timm & Schinner (2020)-style self-citation generator:
each new word is a copy of a recency-weighted earlier word, with small
mutations (context-conditional glyph substitution, deletion, insertion,
affix swap) or an occasional exact copy. Affix inventory and glyph
substitution statistics are extracted FROM the real Voynich corpus, not
hardcoded. 3 free parameters (recency scale tau, exact-copy prob,
second-mutation prob) are tuned by coarse grid search against the
statistics the model most directly controls (unigram entropy, TTR,
adjacent identical & near repeat rates). Everything else is HELD OUT:
BPE compression @500/1000/2000, BPE Zipf slope, char-level conditional
entropies order 0-4, shuffle-corrected bigram info gain, long-range MI
at d=1,2,4,8,16.

Battery code replicates run_bpe.py and run_wordorder.py exactly
(same estimators, same HF tokenizers BPE, same shuffle-correction with
N=10 shuffles, seed conventions preserved).

Outputs: phase3_results.json, synth_run0.txt (example corpus).
"""
import json, math, random, bisect, sys, time
from collections import Counter
from tokenizers import Tokenizer, models, trainers, pre_tokenizers

log2 = lambda x: math.log(x, 2)
t0 = time.time()

# ---------------------------------------------------------------- targets
REAL_WORDS = open('corpus_voynich.txt').read().split()
N_TARGET = len(REAL_WORDS)                      # 37,942
bpe_prior = json.load(open('bpe_results.json'))
wo_prior = json.load(open('wordorder_results.json'))
V = wo_prior['voynich']
TARGETS = dict(
    H_unigram=V['H_unigram'],                   # 10.32
    ttr=V['n_types'] / V['n_words'],            # 0.2028
    ident=V['ident_real'],                      # 0.0081
    near=V['near_real'],                        # 0.0461
)
print(f'real Voynich: {N_TARGET} words, targets {TARGETS}', flush=True)

# ------------------------------------------- corpus-derived model tables
def top_affixes(words, min_len=1, max_len=3, k=25):
    """Top-k prefixes and suffixes by token frequency."""
    pre, suf = Counter(), Counter()
    for w in words:
        for L in range(min_len, min(max_len, len(w) - 1) + 1):
            pre[w[:L]] += 1
            suf[w[-L:]] += 1
    return ([a for a, _ in pre.most_common(k)],
            [a for a, _ in suf.most_common(k)])

PREFIXES, SUFFIXES = top_affixes(REAL_WORDS)
print('top prefixes:', PREFIXES[:12])
print('top suffixes:', SUFFIXES[:12], flush=True)

# char-in-context table: P(c | left char, right char), word-boundary = '^'/'$'
# token-weighted context table
CTX = {}
for w in REAL_WORDS:
    ww = '^' + w + '$'
    for i in range(1, len(ww) - 1):
        key = (ww[i-1], ww[i+1])
        CTX.setdefault(key, Counter())[ww[i]] += 1
CTX_CHOICES = {k: (list(c.keys()), list(c.values())) for k, c in CTX.items()}

# ------------------------------------------------------------- generator
SEED_WORDS = REAL_WORDS[:12]                    # ~first line of the ms

def sample_ctx_char(left, right, exclude=None, rng=random):
    ch = CTX_CHOICES.get((left, right))
    if not ch:
        return None
    keys, wts = ch
    if exclude is not None and len(keys) > 1:
        pairs = [(k, v) for k, v in zip(keys, wts) if k != exclude]
        if not pairs:
            return None
        keys, wts = zip(*pairs)
    return rng.choices(keys, weights=wts)[0]

def mutate(word, rng):
    """Apply one mutation; return new word (may equal input on failure)."""
    r = rng.random()
    ww = '^' + word + '$'
    if r < 0.50:                                # glyph substitution in context
        if len(word) == 0:
            return word
        i = rng.randrange(len(word))            # position within word
        c = sample_ctx_char(ww[i], ww[i+2], exclude=word[i], rng=rng)
        if c is None:
            return word
        return word[:i] + c + word[i+1:]
    elif r < 0.80:                              # affix swap
        if rng.random() < 0.5:
            cands = [p for p in PREFIXES if word.startswith(p) and len(word) - len(p) >= 1]
            if not cands:
                return word
            old = rng.choice(cands)
            new = rng.choice(PREFIXES)
            return new + word[len(old):]
        else:
            cands = [s for s in SUFFIXES if word.endswith(s) and len(word) - len(s) >= 1]
            if not cands:
                return word
            old = rng.choice(cands)
            new = rng.choice(SUFFIXES)
            return word[:len(word) - len(old)] + new
    elif r < 0.90:                              # deletion
        if len(word) <= 2:
            return word
        i = rng.randrange(len(word))
        return word[:i] + word[i+1:]
    else:                                       # insertion in context
        i = rng.randrange(len(word) + 1)
        c = sample_ctx_char(ww[i], ww[i+1], rng=rng)
        if c is None:
            return word
        return word[:i] + c + word[i:]

def make_delta_sampler(tau, rng):
    """Recency-weighted distance sampler: weight(d) ~ exp(-d/tau), d=1..8*tau."""
    cap = max(2, int(8 * tau))
    cum, s = [], 0.0
    for d in range(1, cap + 1):
        s += math.exp(-d / tau)
        cum.append(s)
    total = cum[-1]
    def sample():
        x = rng.random() * total
        return bisect.bisect_left(cum, x) + 1
    return sample

def generate(tau, p_exact, p2, n_words, seed):
    rng = random.Random(seed)
    sample_delta = make_delta_sampler(tau, rng)
    out = list(SEED_WORDS)
    while len(out) < n_words:
        i = len(out)
        d = sample_delta()
        if d > i:
            d = (d - 1) % i + 1
        src = out[i - d]
        if rng.random() < p_exact:
            out.append(src)
            continue
        w = mutate(src, rng)
        if rng.random() < p2:
            w = mutate(w, rng)
        if w:
            out.append(w)
    return out[:n_words]

# ------------------------------------------------------- battery (phase 2)
def H_unigram(words):
    n = len(words); c = Counter(words)
    return -sum((v/n) * log2(v/n) for v in c.values())

def H_joint_at_distance(words, d):
    pairs = list(zip(words[:-d], words[d:]))
    n = len(pairs)
    cj = Counter(pairs)
    Hj = -sum((v/n) * log2(v/n) for v in cj.values())
    c1 = Counter(p[0] for p in pairs); c2 = Counter(p[1] for p in pairs)
    H1 = -sum((v/n) * log2(v/n) for v in c1.values())
    H2 = -sum((v/n) * log2(v/n) for v in c2.values())
    return H1 + H2 - Hj

def H_cond_bigram(words):
    pairs = list(zip(words[:-1], words[1:]))
    n = len(pairs)
    cj = Counter(pairs)
    Hj = -sum((v/n) * log2(v/n) for v in cj.values())
    c1 = Counter(p[0] for p in pairs)
    H1 = -sum((v/n) * log2(v/n) for v in c1.values())
    return Hj - H1

def edit_le1(a, b):
    if a == b: return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1: return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) <= 1
    if la > lb: a, b, la, lb = b, a, lb, la
    i = 0
    while i < la and a[i] == b[i]: i += 1
    return a[i:] == b[i+1:]

def repeat_stats(words):
    n = len(words) - 1
    ident = sum(1 for i in range(n) if words[i] == words[i+1])
    near = sum(1 for i in range(n) if edit_le1(words[i], words[i+1]))
    return ident/n, near/n

def char_cond_entropies(text, max_order=4):
    out = {}
    n = len(text)
    for k in range(max_order + 1):
        ctx = Counter(text[i:i+k] for i in range(n-k))
        joint = Counter(text[i:i+k+1] for i in range(n-k))
        H = 0.0
        total = n - k
        for gram, v in joint.items():
            H -= (v/total) * log2(v/ctx[gram[:k]])
        out[k] = H
    return out

def mean_std(xs):
    m = sum(xs)/len(xs)
    return m, math.sqrt(sum((x-m)**2 for x in xs)/len(xs))

DISTANCES = [1, 2, 4, 8, 16]
N_SHUFFLES = 10

def wordorder_battery(words, shuffle_seed=1234):
    rng = random.Random(shuffle_seed)
    r = {'n_words': len(words), 'n_types': len(set(words))}
    r['H_unigram'] = H_unigram(words)
    r['ttr'] = r['n_types'] / r['n_words']
    r['H_cond_real'] = H_cond_bigram(words)
    r['MI_real'] = {d: H_joint_at_distance(words, d) for d in DISTANCES}
    r['ident_real'], r['near_real'] = repeat_stats(words)
    r['char_H'] = char_cond_entropies(' '.join(words))
    sh_cond, sh_mi = [], {d: [] for d in DISTANCES}
    sh_ident, sh_near = [], []
    for s in range(N_SHUFFLES):
        w = list(words)
        rng.shuffle(w)
        sh_cond.append(H_cond_bigram(w))
        for d in DISTANCES:
            sh_mi[d].append(H_joint_at_distance(w, d))
        i_, n_ = repeat_stats(w)
        sh_ident.append(i_); sh_near.append(n_)
    r['H_cond_shuf'] = mean_std(sh_cond)
    r['info_gain'] = r['H_cond_shuf'][0] - r['H_cond_real']
    r['MI_shuf'] = {d: mean_std(sh_mi[d]) for d in DISTANCES}
    r['MI_corrected'] = {d: r['MI_real'][d] - r['MI_shuf'][d][0] for d in DISTANCES}
    r['ident_shuf'] = mean_std(sh_ident)
    r['near_shuf'] = mean_std(sh_near)
    return r

# ------------------------------------------------------- battery (phase 1)
def zipf_slope(freqs, lo=10, hi=500):
    freqs = sorted(freqs, reverse=True)
    pts = [(math.log(r), math.log(freqs[r-1]))
           for r in range(lo, min(hi, len(freqs)) + 1) if freqs[r-1] > 0]
    n = len(pts)
    sx = sum(x for x, _ in pts); sy = sum(y for _, y in pts)
    sxx = sum(x*x for x, _ in pts); sxy = sum(x*y for x, y in pts)
    slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
    return slope

def bpe_battery(text, vocabs=(500, 1000, 2000)):
    out = {}
    for vs in vocabs:
        tok = Tokenizer(models.BPE(unk_token='[UNK]'))
        tok.pre_tokenizer = pre_tokenizers.Whitespace()
        trainer = trainers.BpeTrainer(vocab_size=vs, special_tokens=['[UNK]'],
                                      show_progress=False)
        tok.train_from_iterator([text], trainer)
        ids = tok.encode(text).ids
        comp = len(text) / len(ids)
        freqs = sorted(Counter(ids).values(), reverse=True)
        out[vs] = {'compression': comp, 'zipf_slope': zipf_slope(freqs)}
    return out

# --------------------------------------------------------- 1) grid search
# Grid re-centered (v2): the tuning targets (unigram entropy 10.32, TTR 0.20)
# require a HIGH exact-copy rate; a coarse probe showed pe<0.05 leaves TTR at
# ~0.85 (nowhere near 0.20). We give the generator a fair chance to hit its
# tuning targets, then read the held-out metrics + tensions. Still 3 knobs.
GRID_TAU = [30, 60, 120, 250]
GRID_PEXACT = [0.55, 0.68, 0.78, 0.88]
GRID_P2 = [0.2, 0.4, 0.6]

def tuning_loss(words):
    h = H_unigram(words)
    ttr = len(set(words)) / len(words)
    ident, near = repeat_stats(words)
    return (((h - TARGETS['H_unigram']) / TARGETS['H_unigram'])**2 +
            ((ttr - TARGETS['ttr']) / TARGETS['ttr'])**2 +
            ((ident - TARGETS['ident']) / TARGETS['ident'])**2 +
            ((near - TARGETS['near']) / TARGETS['near'])**2), h, ttr, ident, near

grid_results = []
best = None
for tau in GRID_TAU:
    for pe in GRID_PEXACT:
        for p2 in GRID_P2:
            words = generate(tau, pe, p2, N_TARGET, seed=42)
            loss, h, ttr, ident, near = tuning_loss(words)
            grid_results.append(dict(tau=tau, p_exact=pe, p2=p2, loss=loss,
                                     H=h, ttr=ttr, ident=ident, near=near))
            if best is None or loss < best['loss']:
                best = grid_results[-1]
            print(f'tau={tau:4d} pe={pe:.3f} p2={p2:.1f}  loss={loss:8.4f} '
                  f'H={h:6.3f} ttr={ttr:.4f} ident={ident:.5f} near={near:.5f}'
                  f'  [{time.time()-t0:.0f}s]', flush=True)
print('\nBEST:', json.dumps(best), flush=True)

# ----------------------------------------------- 2) final runs + battery
FINAL_SEEDS = [101, 202, 303, 404, 505]
runs = []
for k, sd in enumerate(FINAL_SEEDS):
    words = generate(best['tau'], best['p_exact'], best['p2'], N_TARGET, seed=sd)
    if k == 0:
        open('synth_run0.txt', 'w').write(' '.join(words))
    text = ' '.join(words)
    wo = wordorder_battery(words, shuffle_seed=1234 + k)
    bp = bpe_battery(text)
    runs.append({'wordorder': wo, 'bpe': bp})
    print(f'run {k}: H={wo["H_unigram"]:.3f} ttr={wo["ttr"]:.4f} '
          f'gain={wo["info_gain"]:.4f} '
          f'MI8={wo["MI_corrected"][8]:.4f} MI16={wo["MI_corrected"][16]:.4f} '
          f'comp2000={bp[2000]["compression"]:.3f} '
          f'charH1={wo["char_H"][1]:.3f}  [{time.time()-t0:.0f}s]', flush=True)

# ------------------------------------------------------------ aggregate
def agg(getter):
    vals = [getter(r) for r in runs]
    return mean_std(vals)

summary = {
    'best_params': best,
    'grid': grid_results,
    'n_words': N_TARGET,
    'metrics': {}
}
M = summary['metrics']
M['H_unigram'] = agg(lambda r: r['wordorder']['H_unigram'])
M['ttr'] = agg(lambda r: r['wordorder']['ttr'])
M['n_types'] = agg(lambda r: r['wordorder']['n_types'])
M['info_gain'] = agg(lambda r: r['wordorder']['info_gain'])
M['ident_real'] = agg(lambda r: r['wordorder']['ident_real'])
M['near_real'] = agg(lambda r: r['wordorder']['near_real'])
M['ident_ratio'] = agg(lambda r: r['wordorder']['ident_real'] / r['wordorder']['ident_shuf'][0])
M['near_ratio'] = agg(lambda r: r['wordorder']['near_real'] / r['wordorder']['near_shuf'][0])
for d in DISTANCES:
    M[f'MI_d{d}'] = agg(lambda r, d=d: r['wordorder']['MI_corrected'][d])
for k in range(5):
    M[f'char_H{k}'] = agg(lambda r, k=k: r['wordorder']['char_H'][k])
for vs in (500, 1000, 2000):
    M[f'bpe_comp_{vs}'] = agg(lambda r, vs=vs: r['bpe'][vs]['compression'])
    M[f'bpe_zipf_{vs}'] = agg(lambda r, vs=vs: r['bpe'][vs]['zipf_slope'])

json.dump(summary, open('phase3_results.json', 'w'), indent=2, default=str)
print(f'\nsaved phase3_results.json  [{time.time()-t0:.0f}s total]')
print(json.dumps({k: v for k, v in M.items()}, indent=1, default=str))
