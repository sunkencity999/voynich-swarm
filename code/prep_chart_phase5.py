#!/usr/bin/env python3
"""Precompute chart data for phase 5 (system python: sklearn available).
Saves phase5_chart_data.npz: t-SNE coords + section colors for real and
word-shuffled Voynich embeddings."""
import json
import numpy as np
from collections import Counter, defaultdict
from sklearn.manifold import TSNE
from run_phase5 import load_space

vlines = json.load(open('phase5_vlines.json'))
meta = json.load(open('phase5_line_meta.json'))

def word_sections(vocab):
    idx = {w: i for i, w in enumerate(vocab)}
    ws = defaultdict(Counter)
    for line, m in zip(vlines, meta):
        if m['sec'] == 'text':
            continue
        for w in line:
            if w in idx:
                ws[w][m['sec']] += 1
    dom, share = [], []
    for w in vocab:
        c = ws.get(w)
        if not c:
            dom.append('none'); share.append(0.0); continue
        s, n = c.most_common(1)[0]
        dom.append(s); share.append(n / sum(c.values()))
    return dom, share

out = {}
for name in ['voynich', 'voynich_wshuf']:
    vocab, emb, counts = load_space(name)
    xy = TSNE(n_components=2, random_state=5, perplexity=30,
              init='pca', metric='cosine').fit_transform(emb)
    dom, share = word_sections(vocab)
    out[name] = (xy, dom, share, counts, vocab)

np.savez_compressed('phase5_chart_data.npz',
    v_xy=out['voynich'][0], v_dom=np.array(out['voynich'][1], dtype=object),
    v_share=np.array(out['voynich'][2]), v_counts=out['voynich'][3],
    v_vocab=np.array(out['voynich'][4], dtype=object),
    s_xy=out['voynich_wshuf'][0], s_dom=np.array(out['voynich_wshuf'][1], dtype=object),
    s_share=np.array(out['voynich_wshuf'][2]))
print('wrote phase5_chart_data.npz')
