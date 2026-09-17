#!/usr/bin/env python3
"""Train BPE per corpus at vocab 500/1000/2000; compute metrics."""
import json, math, collections
from tokenizers import Tokenizer, models, trainers, pre_tokenizers

CORPORA = ['voynich', 'latin', 'english', 'italian', 'charshuf', 'wordshuf']
VOCABS = [500, 1000, 2000]

def zipf_slope(freqs, lo=10, hi=500):
    """log-log linear fit of freq vs rank over ranks lo..hi."""
    freqs = sorted(freqs, reverse=True)
    pts = [(math.log(r), math.log(freqs[r-1]))
           for r in range(lo, min(hi, len(freqs)) + 1) if freqs[r-1] > 0]
    n = len(pts)
    sx = sum(x for x, _ in pts); sy = sum(y for _, y in pts)
    sxx = sum(x*x for x, _ in pts); sxy = sum(x*y for x, y in pts)
    slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
    # r^2
    mx, my = sx/n, sy/n
    ssxy = sxy - n*mx*my; ssxx = sxx - n*mx*mx
    syy = sum(y*y for _, y in pts) - n*my*my
    r2 = (ssxy*ssxy) / (ssxx*syy) if syy > 0 else 0.0
    return slope, r2, n

results = {}
zipf_curves = {}   # (corpus, vocab) -> sorted freq list (for plotting @2000)
comp_curves = {}   # corpus -> {vocab: compression}

for name in CORPORA:
    text = open(f'corpus_{name}.txt').read()
    nchars = len(text)
    words = text.split()
    comp_curves[name] = {}
    for vs in VOCABS:
        tok = Tokenizer(models.BPE(unk_token='[UNK]'))
        tok.pre_tokenizer = pre_tokenizers.Whitespace()
        trainer = trainers.BpeTrainer(vocab_size=vs, special_tokens=['[UNK]'],
                                      show_progress=False)
        tok.train_from_iterator([text], trainer)
        enc = tok.encode(text)
        ids = enc.ids
        ntok = len(ids)
        comp = nchars / ntok
        # token frequency distribution
        cnt = collections.Counter(ids)
        freqs = sorted(cnt.values(), reverse=True)
        slope, r2, npts = zipf_slope(freqs)
        # top-100 coverage (by token count)
        top100 = sum(freqs[:100]) / ntok
        # merged-token lengths (vocab entries, excluding [UNK])
        vocab = tok.get_vocab()
        lens = [len(t) for t in vocab if t != '[UNK]']
        mean_len = sum(lens)/len(lens)
        # length histogram of vocab
        lh = collections.Counter(lens)
        # mean length of tokens as USED (weighted by frequency)
        id2tok = {v: k for k, v in vocab.items()}
        used_len = sum(len(id2tok[i])*c for i, c in cnt.items()) / ntok
        actual_vs = tok.get_vocab_size()
        results[(name, vs)] = dict(
            corpus=name, vocab=vs, actual_vocab=actual_vs, tokens=ntok,
            compression=round(comp, 4), zipf_slope=round(slope, 4),
            zipf_r2=round(r2, 4), zipf_pts=npts,
            top100_cov=round(top100, 4),
            mean_vocab_len=round(mean_len, 3),
            mean_used_len=round(used_len, 3),
            len_hist={str(k): v for k, v in sorted(lh.items())})
        comp_curves[name][vs] = comp
        if vs == 2000:
            zipf_curves[name] = freqs[:2000]
        print(f"{name:9s} v={vs:5d} comp={comp:.3f} zipf={slope:.3f} "
              f"(r2={r2:.3f}) top100={top100:.3f} vlen={mean_len:.2f}")

json.dump({f"{k[0]}_{k[1]}": v for k, v in results.items()},
          open('bpe_results.json', 'w'), indent=2)
json.dump({'comp_curves': comp_curves, 'zipf_curves': zipf_curves},
          open('plot_data.json', 'w'))
print('saved bpe_results.json, plot_data.json')
