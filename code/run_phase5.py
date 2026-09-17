#!/usr/bin/env python3
"""Phase 5 orchestrator. Steps are checkpointed; rerun skips finished stages.
Usage: python3 run_phase5.py [step]   step in {emb, geom, topic, align, all}"""
import sys, json, os, random
import numpy as np
from collections import Counter, defaultdict
import phase5_lib as L

OUT = 'phase5_results.json'


def load_results():
    return json.load(open(OUT)) if os.path.exists(OUT) else {}


def save_results(r):
    json.dump(r, open(OUT, 'w'), indent=1, default=float)


# ---------------- stage: embeddings ----------------

def stage_emb():
    vlines = L.voynich_lines()
    n_tokens = sum(len(w) for w, *_ in vlines)
    print(f'voynich: {len(vlines)} lines, {n_tokens} tokens')
    word_lines = [w for w, *_ in vlines]

    # nulls
    rng = random.Random(L.SEED)
    flat = [w for line in word_lines for w in line]
    shuf = flat[:]
    rng.shuffle(shuf)
    # word-shuffled: same line lengths, words drawn from global shuffle
    wshuf_lines, pos = [], 0
    for line in word_lines:
        wshuf_lines.append(shuf[pos:pos + len(line)])
        pos += len(line)

    lat = L.natural_sentences('raw_latin.txt', n_tokens)
    ita = L.natural_sentences('raw_italian.txt', n_tokens)
    print(f'latin: {len(lat)} sents, {sum(len(s) for s in lat)} tokens')
    print(f'italian: {len(ita)} sents, {sum(len(s) for s in ita)} tokens')

    # shuffled-Latin (floor calibration for alignment)
    lflat = [w for s in lat for w in s]
    lshuf = lflat[:]
    rng.shuffle(lshuf)
    lshuf_lines, pos = [], 0
    for s in lat:
        lshuf_lines.append(lshuf[pos:pos + len(s)])
        pos += len(s)

    spaces = {}
    for name, lines in [('voynich', word_lines), ('latin', lat), ('italian', ita),
                        ('voynich_wshuf', wshuf_lines), ('latin_wshuf', lshuf_lines)]:
        vocab, emb, counts, S = L.build_embeddings(lines, window=3, min_count=5,
                                                   dim=100, top_vocab=2000)
        spaces[name] = (vocab, emb)
        np.savez_compressed(f'phase5_emb_{name}.npz', emb=emb,
                            vocab=np.array(vocab, dtype=object),
                            counts=np.array([counts[w] for w in vocab]))
        print(f'{name}: V={len(vocab)} emb={emb.shape}')
    # save line metadata for topic stage
    meta = [{'sec': s, 'folio': f, 'lang': la, 'n': len(w)}
            for w, s, f, la in vlines]
    json.dump(meta, open('phase5_line_meta.json', 'w'))
    with open('phase5_vlines.json', 'w') as fh:
        json.dump([[w for w in line] for line in word_lines], fh)
    return spaces


def load_space(name):
    z = np.load(f'phase5_emb_{name}.npz', allow_pickle=True)
    return list(z['vocab']), z['emb'], z['counts']


# ---------------- stage: geometry ----------------

def stage_geom(res):
    geo = {}
    for name in ['voynich', 'latin', 'italian', 'voynich_wshuf']:
        vocab, emb, _ = load_space(name)
        geo[name] = L.geometry_metrics(emb, k=10)
        print(name, {k: round(v, 3) for k, v in geo[name].items()
                     if isinstance(v, float)})
    # line-shuffled Voynich: windows never cross lines, so its embedding is
    # IDENTICAL to the real one by construction — noted analytically, used
    # only as the null for the topic-section test.
    geo['note_line_shuffle'] = ('line-shuffle preserves within-line windows; '
                                'embedding identical to real — geometry null is word-shuffle only')
    res['geometry'] = geo
    save_results(res)


# ---------------- stage: topic-section MI ----------------

def stage_topic(res):
    vocab, emb, counts = load_space('voynich')
    idx = {w: i for i, w in enumerate(vocab)}
    vlines = json.load(open('phase5_vlines.json'))
    meta = json.load(open('phase5_line_meta.json'))

    # silhouette-select k
    sil = {}
    best = None
    for k in [10, 14, 18, 22, 26, 30]:
        lab, C = L.kmeans(emb, k)
        s = L.silhouette(emb, lab)
        sil[k] = s
        print(f'k={k} silhouette={s:.4f}')
        if best is None or s > sil[best]:
            best = k
    lab, C = L.kmeans(emb, best)

    # token-level section/cluster labels
    tok_sec, tok_clu, tok_word = [], [], []
    for line, m in zip(vlines, meta):
        if m['sec'] == 'text':
            continue
        for w in line:
            i = idx.get(w)
            if i is None:
                continue
            tok_sec.append(m['sec']); tok_clu.append(int(lab[i])); tok_word.append(w)
    mi = L.mutual_info(tok_clu, tok_sec)

    # null: permute section labels over LINES (line-shuffled null)
    rng = random.Random(L.SEED)
    null_mis = []
    secs = [m['sec'] for m in meta]
    for rep in range(50):
        perm = secs[:]
        rng.shuffle(perm)
        ts = []
        for line, m, ps in zip(vlines, meta, perm):
            if ps == 'text':
                continue
            for w in line:
                if w in idx:
                    ts.append(ps)
        # rebuild clusters aligned with same tokens
        tc = []
        for line, m, ps in zip(vlines, meta, perm):
            if ps == 'text':
                continue
            for w in line:
                i = idx.get(w)
                if i is not None:
                    tc.append(int(lab[i]))
        null_mis.append(L.mutual_info(tc, ts))
    null_mu, null_sd = float(np.mean(null_mis)), float(np.std(null_mis))
    z = (mi - null_mu) / null_sd if null_sd > 0 else float('inf')
    print(f'k*={best} token cluster-section MI={mi:.4f} bits; null {null_mu:.4f}±{null_sd:.4f} z={z:.1f}')

    # per-word section profiles → section-lockedness
    sec_tot = Counter(tok_sec)
    word_sec = defaultdict(Counter)
    for w, s in zip(tok_word, tok_sec):
        word_sec[w][s] += 1
    lockness = []
    for w, cnt in word_sec.items():
        n = sum(cnt.values())
        if n < 20:
            continue
        # KL(word-section-dist || corpus-section-dist) in bits
        kl = 0.0
        for s, c in cnt.items():
            p = c / n
            q = sec_tot[s] / len(tok_sec)
            kl += p * np.log2(p / q)
        top = cnt.most_common(1)[0]
        lockness.append({'word': w, 'n': n, 'kl_bits': float(kl),
                         'top_sec': top[0], 'top_share': top[1] / n,
                         'profile': {s: c / n for s, c in cnt.items()}})
    lockness.sort(key=lambda d: -d['kl_bits'])
    universal = sorted([d for d in lockness if d['n'] >= 100],
                       key=lambda d: d['kl_bits'])[:20]

    # cluster section profiles
    clu_sec = defaultdict(Counter)
    for c, s in zip(tok_clu, tok_sec):
        clu_sec[c][s] += 1
    clu_prof = {int(c): {s: n / sum(cnt.values()) for s, n in cnt.items()}
                for c, cnt in clu_sec.items()}

    res['topic'] = {
        'silhouette_by_k': sil, 'k_selected': best,
        'token_MI_bits': mi, 'null_mu': null_mu, 'null_sd': null_sd, 'z': z,
        'section_token_counts': dict(sec_tot),
        'top20_section_locked': lockness[:20],
        'top20_universal': universal,
        'cluster_section_profiles': clu_prof,
        'cluster_sizes': dict(Counter(int(x) for x in lab)),
    }
    np.savez_compressed('phase5_clusters.npz', labels=lab,
                        vocab=np.array(vocab, dtype=object))
    save_results(res)


# ---------------- stage: alignment ----------------

def stage_align(res):
    out = {}
    pairs = [('latin', 'italian', 'ceiling: Latin→Italian'),
             ('voynich', 'latin', 'Voynich→Latin'),
             ('voynich', 'italian', 'Voynich→Italian'),
             ('voynich', 'latin_wshuf', 'floor: Voynich→shuffled-Latin'),
             ('latin', 'latin_wshuf', 'floor: Latin→shuffled-Latin'),
             ('voynich_wshuf', 'latin', 'floor: shuffled-Voynich→Latin')]
    for a, b, label in pairs:
        va, ea, _ = load_space(a)
        vb, eb, _ = load_space(b)
        n = min(400, len(va), len(vb))
        info, T, match = L.align_spaces(ea, eb, n_top=n)
        info['n'] = n
        out[label] = info
        print(label, {k: round(v, 4) if isinstance(v, float) else v
                      for k, v in info.items()})
        if a == 'voynich' and b in ('latin', 'italian'):
            np.savez_compressed(f'phase5_align_{b}.npz', T=T, match=match,
                                va=np.array(va[:n], dtype=object),
                                vb=np.array(vb[:n], dtype=object))
    res['alignment'] = out
    save_results(res)


if __name__ == '__main__':
    step = sys.argv[1] if len(sys.argv) > 1 else 'all'
    res = load_results()
    if step in ('emb', 'all'):
        stage_emb()
    if step in ('geom', 'all'):
        stage_geom(res)
    if step in ('topic', 'all'):
        stage_topic(res)
    if step in ('align', 'all'):
        stage_align(res)
    print('done:', step)
