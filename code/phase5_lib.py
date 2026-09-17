#!/usr/bin/env python3
"""Phase 5 shared library: line-structured corpora, PPMI+SVD embeddings,
intrinsic geometry metrics, k-means/silhouette, entropic Gromov-Wasserstein
relational alignment. numpy/scipy only; fully deterministic (seeded)."""
import re, math, json
import numpy as np
from collections import Counter, defaultdict
from phase4_lib import extract_structured

SEED = 5

# ---------------- section mapping ----------------
# IVTFF $I codes in ZL3b-n: H=herbal, A=astronomical, Z=zodiac, C=cosmological,
# B=biological/balneological, P=pharmaceutical, S=stars/recipes, T=text-only.
# Mapping (documented in report): astro := A+Z+C (all star/cosmos diagrams),
# recipes := S, text-only excluded from section tests but kept for embeddings.
SECTION_MAP = {'H': 'herbal', 'A': 'astro', 'Z': 'astro', 'C': 'astro',
               'B': 'balneo', 'P': 'pharma', 'S': 'recipes', 'T': 'text'}
SECTIONS = ['herbal', 'astro', 'balneo', 'pharma', 'recipes']


def voynich_lines(path='ZL3b-n.txt'):
    """[(words, section, folio, currier_lang)] — one record per locus line."""
    out = []
    for l in extract_structured(path):
        sec = SECTION_MAP.get(l['ill'], 'text')
        out.append((l['words'], sec, l['folio'], l['lang']))
    return out


def natural_sentences(path, max_tokens):
    """Sentence-segmented, lowercased, alpha-only word lists, truncated to
    ~max_tokens total tokens. Same treatment for Latin and Italian."""
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    sents = re.split(r'[.;:!?]+', text)
    out, n = [], 0
    for s in sents:
        words = re.findall(r"[a-zà-ÿ]+", s)
        words = [w for w in words if len(w) > 1 or w in ('a', 'e', 'o', 'i')]
        if len(words) < 2:
            continue
        out.append(words)
        n += len(words)
        if n >= max_tokens:
            break
    return out


# ---------------- PPMI + SVD embeddings ----------------

def build_embeddings(lines, window=3, min_count=5, dim=100, top_vocab=None):
    """lines: list of word-lists. Windows NEVER cross a line/sentence boundary.
    Returns (vocab list, embedding matrix [V,dim], counts Counter)."""
    counts = Counter(w for l in lines for w in l)
    vocab = [w for w, c in counts.most_common() if c >= min_count]
    if top_vocab:
        vocab = vocab[:top_vocab]
    idx = {w: i for i, w in enumerate(vocab)}
    V = len(vocab)
    co = defaultdict(float)
    for line in lines:
        ids = [idx.get(w, -1) for w in line]
        n = len(ids)
        for i in range(n):
            if ids[i] < 0:
                continue
            for j in range(max(0, i - window), min(n, i + window + 1)):
                if j == i or ids[j] < 0:
                    continue
                co[(ids[i], ids[j])] += 1.0
    # sparse PPMI
    row_sum = np.zeros(V)
    col_sum = np.zeros(V)
    total = 0.0
    for (i, j), c in co.items():
        row_sum[i] += c
        col_sum[j] += c
        total += c
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import svds
    rows, cols, vals = [], [], []
    for (i, j), c in co.items():
        pmi = math.log((c * total) / (row_sum[i] * col_sum[j]))
        if pmi > 0:
            rows.append(i); cols.append(j); vals.append(pmi)
    M = csr_matrix((vals, (rows, cols)), shape=(V, V))
    k = min(dim, V - 1)
    np.random.seed(SEED)
    v0 = np.random.rand(min(M.shape))
    U, S, Vt = svds(M, k=k, v0=v0)
    order = np.argsort(-S)
    U, S = U[:, order], S[order]
    emb = U * np.sqrt(S)          # symmetric weighting (Levy&Goldberg)
    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    norms[norms == 0] = 1
    emb = emb / norms
    return vocab, emb.astype(np.float64), counts, S


# ---------------- intrinsic geometry ----------------

def knn_indices(emb, k=10):
    sim = emb @ emb.T
    np.fill_diagonal(sim, -np.inf)
    return np.argsort(-sim, axis=1)[:, :k], sim


def geometry_metrics(emb, k=10):
    """hubness (skew of k-occurrence), NN-sim distribution, Gram spectrum
    stats, clustering coefficient of symmetrized kNN graph."""
    from scipy import stats as st
    V = emb.shape[0]
    nn, sim = knn_indices(emb, k)
    # hubness: skewness of N_k (how often each word appears in others' kNN)
    occ = np.bincount(nn.ravel(), minlength=V)
    hub_skew = float(st.skew(occ))
    # NN similarity distribution (sim to 1st and mean over kNN)
    nn1 = np.array([sim[i, nn[i, 0]] for i in range(V)])
    nnk = np.array([sim[i, nn[i]].mean() for i in range(V)])
    # Gram spectrum: eigenvalues of E E^T via singular values of emb
    sv = np.linalg.svd(emb, compute_uv=False)
    ev = sv ** 2
    ev = ev / ev.sum()
    spec_entropy = float(-(ev * np.log(ev + 1e-300)).sum())
    eff_rank = float(math.exp(spec_entropy))
    # top-10 eigen share
    top10 = float(ev[:10].sum())
    # clustering coefficient on symmetrized kNN graph
    adj = [set() for _ in range(V)]
    for i in range(V):
        for j in nn[i]:
            adj[i].add(int(j)); adj[int(j)].add(i)
    cc = []
    for i in range(V):
        nb = list(adj[i])
        d = len(nb)
        if d < 2:
            cc.append(0.0); continue
        links = 0
        nbset = adj[i]
        for a in range(d):
            links += len(adj[nb[a]] & nbset)
        cc.append(links / (d * (d - 1)))
    return {
        'V': V, 'k': k,
        'hubness_skew': hub_skew,
        'hub_occ_max': int(occ.max()), 'hub_occ_p99': float(np.percentile(occ, 99)),
        'nn1_sim_mean': float(nn1.mean()), 'nn1_sim_std': float(nn1.std()),
        'nnk_sim_mean': float(nnk.mean()),
        'spec_entropy': spec_entropy, 'effective_rank': eff_rank,
        'top10_eigen_share': top10,
        'clustering_coef': float(np.mean(cc)),
        'nn1_hist': np.histogram(nn1, bins=np.linspace(-0.2, 1.0, 25))[0].tolist(),
        'eigen_top30': ev[:30].tolist(),
    }


# ---------------- k-means + silhouette ----------------

def kmeans(emb, k, seed=SEED, iters=60):
    rng = np.random.default_rng(seed)
    # k-means++ init
    C = [emb[rng.integers(len(emb))]]
    for _ in range(k - 1):
        d2 = np.min([((emb - c) ** 2).sum(1) for c in C], axis=0)
        p = d2 / d2.sum()
        C.append(emb[rng.choice(len(emb), p=p)])
    C = np.array(C)
    for _ in range(iters):
        lab = np.argmax(emb @ C.T, axis=1)  # cosine (all unit-norm)
        newC = np.zeros_like(C)
        for j in range(k):
            m = lab == j
            if m.sum() == 0:
                newC[j] = emb[rng.integers(len(emb))]
            else:
                v = emb[m].mean(0)
                n = np.linalg.norm(v)
                newC[j] = v / (n if n > 0 else 1)
        if np.allclose(newC, C):
            C = newC; break
        C = newC
    lab = np.argmax(emb @ C.T, axis=1)
    return lab, C


def silhouette(emb, lab):
    # cosine-distance silhouette, sampled if large
    from scipy.spatial.distance import cdist
    n = len(emb)
    idx = np.arange(n)
    if n > 1500:
        rng = np.random.default_rng(SEED)
        idx = rng.choice(n, 1500, replace=False)
    D = cdist(emb[idx], emb, metric='cosine')
    s = []
    for r, i in enumerate(idx):
        same = lab == lab[i]
        same_i = same.copy(); same_i[i] = False
        if same_i.sum() == 0:
            continue
        a = D[r][same_i].mean()
        b = min(D[r][lab == c].mean() for c in np.unique(lab) if c != lab[i])
        s.append((b - a) / max(a, b))
    return float(np.mean(s))


# ---------------- MI helpers ----------------

def mutual_info(xs, ys):
    """MI in bits between two discrete label sequences."""
    cx, cy, cxy = Counter(xs), Counter(ys), Counter(zip(xs, ys))
    n = len(xs)
    mi = 0.0
    for (a, b), c in cxy.items():
        mi += (c / n) * math.log2((c * n) / (cx[a] * cy[b]))
    return mi


# ---------------- entropic Gromov-Wasserstein ----------------

def center_norm(C):
    """Double-center a similarity matrix and scale to unit std (removes the
    frequency/hub component that gives all pairs a spurious baseline
    correlation; makes the entropic eps scale meaningful)."""
    C = C - C.mean(1, keepdims=True) - C.mean(0, keepdims=True) + C.mean()
    return C / C.std()


def _logsinkhorn(G, eps, p, q, iters=80):
    from scipy.special import logsumexp
    f = np.zeros(len(p)); g = np.zeros(len(q))
    lp, lq = np.log(p), np.log(q)
    M = -G / eps
    for _ in range(iters):
        f = eps * (lp - logsumexp(M + g[None, :] / eps, axis=1))
        g = eps * (lq - logsumexp(M + f[:, None] / eps, axis=0))
    return np.exp(M + f[:, None] / eps + g[None, :] / eps)


def gromov_wasserstein(C1, C2, eps_list=(1.0, 0.3, 0.1, 0.03, 0.01), outer=25,
                       seed=SEED):
    """Entropic GW (Peyre et al. 2016) with eps annealing and log-domain
    sinkhorn. Inputs should be center_norm'ed similarity matrices.
    Uniform marginals. Returns coupling T and gw loss."""
    n1, n2 = C1.shape[0], C2.shape[0]
    p = np.full(n1, 1 / n1)
    q = np.full(n2, 1 / n2)
    T = np.outer(p, q)
    constC = ((C1 ** 2) @ p)[:, None] + ((C2 ** 2) @ q)[None, :]
    for eps in eps_list:
        for _ in range(outer):
            grad = constC - 2.0 * C1 @ T @ C2.T
            T = _logsinkhorn(grad, eps, p, q)
    loss = float(((constC - 2.0 * C1 @ T @ C2.T) * T).sum())
    return T, loss


def relational_score(C1, C2, T):
    """Hard-match by argmax of coupling; Spearman corr between pairwise
    similarities of matched pairs = relational preservation score."""
    from scipy import stats as st
    match = np.argmax(T, axis=1)
    n = C1.shape[0]
    rng = np.random.default_rng(SEED)
    ii = rng.choice(n, min(n, 400), replace=False)
    a, b = [], []
    for x in range(len(ii)):
        for y in range(x + 1, len(ii)):
            i, j = ii[x], ii[y]
            a.append(C1[i, j]); b.append(C2[match[i], match[j]])
    rho = st.spearmanr(a, b).statistic
    return float(rho), match


def align_spaces(embA, embB, n_top=400):
    """GW-align top-n_top rows of each embedding (frequency-ordered).
    Returns relational score + coupling entropy diagnostics."""
    A = embA[:n_top]
    B = embB[:n_top]
    C1 = center_norm(A @ A.T)
    C2 = center_norm(B @ B.T)
    T, loss = gromov_wasserstein(C1, C2)
    rho, match = relational_score(C1, C2, T)
    # coupling concentration: mean max-row-mass * n (1 = perfect permutation-like)
    conc = float((T.max(axis=1) * n_top).mean())
    return {'gw_loss': loss, 'relational_rho': rho, 'coupling_conc': conc}, T, match
