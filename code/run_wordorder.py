#!/usr/bin/env python3
"""Phase 2: word-order information tests on size-matched corpora.

For each corpus: unigram entropy, bigram conditional entropy (with
word-shuffle baseline to cancel small-sample MLE bias), mutual information
at distances d=1,2,4,8,16, char-level conditional entropies order 0-4,
and adjacent near-repeat rates (edit distance <= 1), real vs shuffled.
Pure python + stdlib. Outputs wordorder_results.json.
"""
import json, math, random
from collections import Counter

random.seed(1234)
N_SHUFFLES = 10
DISTANCES = [1, 2, 4, 8, 16]
CORPORA = ['voynich', 'latin', 'english', 'italian']

log2 = lambda x: math.log(x, 2)

def H_unigram(words):
    n = len(words)
    c = Counter(words)
    return -sum((v/n) * log2(v/n) for v in c.values())

def H_joint_at_distance(words, d):
    """Joint entropy H(W_i, W_{i+d}) and marginals over the pair positions."""
    pairs = list(zip(words[:-d], words[d:]))
    n = len(pairs)
    cj = Counter(pairs)
    Hj = -sum((v/n) * log2(v/n) for v in cj.values())
    c1 = Counter(p[0] for p in pairs)
    c2 = Counter(p[1] for p in pairs)
    H1 = -sum((v/n) * log2(v/n) for v in c1.values())
    H2 = -sum((v/n) * log2(v/n) for v in c2.values())
    return H1 + H2 - Hj  # MI = H1 + H2 - Hjoint

def H_cond_bigram(words):
    """H(W2|W1) = Hjoint - H(W1), over adjacent pairs."""
    pairs = list(zip(words[:-1], words[1:]))
    n = len(pairs)
    cj = Counter(pairs)
    Hj = -sum((v/n) * log2(v/n) for v in cj.values())
    c1 = Counter(p[0] for p in pairs)
    H1 = -sum((v/n) * log2(v/n) for v in c1.values())
    return Hj - H1

def edit_le1(a, b):
    """True if edit distance(a,b) <= 1. Cheap checks only."""
    if a == b: return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1: return False
    if la == lb:  # one substitution
        return sum(x != y for x, y in zip(a, b)) <= 1
    if la > lb: a, b, la, lb = b, a, lb, la
    # a shorter by 1: one insertion
    i = 0
    while i < la and a[i] == b[i]: i += 1
    return a[i:] == b[i+1:]

def repeat_stats(words):
    n = len(words) - 1
    ident = sum(1 for i in range(n) if words[i] == words[i+1])
    near = sum(1 for i in range(n) if edit_le1(words[i], words[i+1]))
    return ident/n, near/n

def char_cond_entropies(text, max_order=4):
    """H(c | previous k chars) for k=0..max_order, MLE on the corpus string."""
    out = {}
    n = len(text)
    for k in range(max_order+1):
        ctx = Counter(text[i:i+k] for i in range(n-k))
        joint = Counter(text[i:i+k+1] for i in range(n-k))
        H = 0.0
        total = n - k
        for gram, v in joint.items():
            p = v/total
            pc = v/ctx[gram[:k]]
            H -= p * log2(pc)
        out[k] = H
    return out

def mean_std(xs):
    m = sum(xs)/len(xs)
    var = sum((x-m)**2 for x in xs)/len(xs)
    return m, math.sqrt(var)

results = {}
for name in CORPORA:
    words = open(f'corpus_{name}.txt').read().split()
    text = ' '.join(words)
    print(f'=== {name}: {len(words)} words, {len(set(words))} types ===', flush=True)

    r = {'n_words': len(words), 'n_types': len(set(words))}
    r['H_unigram'] = H_unigram(words)
    r['H_cond_real'] = H_cond_bigram(words)
    r['MI_real'] = {d: H_joint_at_distance(words, d) for d in DISTANCES}
    r['ident_real'], r['near_real'] = repeat_stats(words)
    r['char_H'] = char_cond_entropies(text)

    # shuffle baselines
    sh_cond, sh_mi, sh_ident, sh_near = [], {d: [] for d in DISTANCES}, [], []
    for s in range(N_SHUFFLES):
        w = list(words)
        random.shuffle(w)
        sh_cond.append(H_cond_bigram(w))
        for d in DISTANCES:
            sh_mi[d].append(H_joint_at_distance(w, d))
        i_, n_ = repeat_stats(w)
        sh_ident.append(i_); sh_near.append(n_)

    r['H_cond_shuf_mean'], r['H_cond_shuf_std'] = mean_std(sh_cond)
    r['info_gain'] = r['H_cond_shuf_mean'] - r['H_cond_real']
    r['info_gain_std'] = r['H_cond_shuf_std']
    r['MI_shuf'] = {d: mean_std(sh_mi[d]) for d in DISTANCES}
    r['MI_corrected'] = {d: r['MI_real'][d] - r['MI_shuf'][d][0] for d in DISTANCES}
    r['ident_shuf'] = mean_std(sh_ident)
    r['near_shuf'] = mean_std(sh_near)
    results[name] = r
    print(json.dumps({k: v for k, v in r.items() if k != 'char_H'},
                     indent=1, default=str)[:600], flush=True)

json.dump(results, open('wordorder_results.json', 'w'), indent=2)
print('saved wordorder_results.json')
