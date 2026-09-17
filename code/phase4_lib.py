#!/usr/bin/env python3
"""Phase 4 shared library: structured extraction + slot grammar + entropy/MI helpers."""
import re, math, random
from collections import Counter, defaultdict

# ---------------- structured extraction from IVTFF ----------------

def extract_structured(path):
    """Return list of lines: dict(folio, lang, illust, words=[...]).
    Same cleaning rules as clean_ivtff.py, but preserving line boundaries and
    page variables $L (Currier language) and $I (illustration/section)."""
    lines = []
    cur_lang, cur_ill, cur_folio = None, None, None
    for raw in open(path, encoding='latin-1'):
        raw = raw.strip()
        if not raw or raw.startswith('#'):
            continue
        m = re.match(r'^<(f[^>]*)>\s*(.*)$', raw)
        if m is None:
            continue
        tag, text = m.group(1), m.group(2)
        # page header? tag has no '.', text is only a <! $..> comment
        if '.' not in tag:
            cur_folio = tag
            lm = re.search(r'\$L=(\w)', text)
            im = re.search(r'\$I=(\w)', text)
            cur_lang = lm.group(1) if lm else None
            cur_ill = im.group(1) if im else None
            continue
        # locus line
        text = re.sub(r'\[([^\]:]*):[^\]]*\]', r'\1', text)
        text = re.sub(r'<[^>]*>', ' ', text)
        text = re.sub(r'\{[^}]*\}', ' ', text)
        text = re.sub(r'\[[^\]]*\]', ' ', text)
        text = text.lower()
        words = [t for t in re.split(r'[.,\s]+', text) if t and re.fullmatch(r'[a-z]+', t)]
        if words:
            lines.append({'folio': cur_folio, 'lang': cur_lang, 'ill': cur_ill,
                          'words': words})
    return lines

# ---------------- glyph tokenizer ----------------

MULTI = ['ckh', 'cth', 'cph', 'cfh', 'ch', 'sh']

def glyphs(word):
    out, i = [], 0
    while i < len(word):
        for m in MULTI:
            if word.startswith(m, i):
                out.append(m); i += len(m); break
        else:
            out.append(word[i]); i += 1
    return out

# ---------------- slot grammar ----------------
# 15 ordered slots. Cascade: pass 1 = canonical template (no PREL/E1/AO0);
# pass 2 = extended template adding a prefix consonant slot PREL ([dlrs], for
# ol-/l-initial Currier-B words) and a pre-gallows e/ao cycle (cheky, choky).
# Cascade keeps canonical words in canonical slot assignments.
SLOT_NAMES = ['Q', 'AOY', 'PREL', 'BENCH1', 'E1', 'AO0', 'GALL', 'BENCH2',
              'E2', 'AO1', 'CORE', 'AO2', 'I', 'FIN', 'Y']

_TAIL = (r'(?P<GALL>(?:ckh|cth|cph|cfh|k|t|p|f)?)(?P<BENCH2>(?:ch|sh)?)'
         r'(?P<E2>e{0,3})(?P<AO1>[ao]?)(?P<CORE>[dlrs]?)(?P<AO2>[ao]?)'
         r'(?P<I>i{0,3})(?P<FIN>[nmlrs]?)(?P<Y>y?)$')
RE_P1 = re.compile(r'^(?P<Q>q?)(?P<AOY>[aoy]?)(?P<PREL>)(?P<BENCH1>(?:ch|sh)?)'
                   r'(?P<E1>)(?P<AO0>)' + _TAIL)
RE_P2 = re.compile(r'^(?P<Q>q?)(?P<AOY>[aoy]?)(?P<PREL>[dlrs]?)'
                   r'(?P<BENCH1>(?:ch|sh)?)(?P<E1>e{0,3})(?P<AO0>[ao]?)' + _TAIL)
# pass 3: two-consonant cores (-ldy class: choldy, okaldy, sholdy)
_TAIL3 = _TAIL.replace('(?P<CORE>[dlrs]?)', '(?P<CORE>[dlrs]{0,2})')
RE_P3 = re.compile(r'^(?P<Q>q?)(?P<AOY>[aoy]?)(?P<PREL>[dlrs]?)'
                   r'(?P<BENCH1>(?:ch|sh)?)(?P<E1>e{0,3})(?P<AO0>[ao]?)' + _TAIL3)

def parse_word(w):
    """Return (slots_dict, pass_no) or (None, 0)."""
    m = RE_P1.match(w)
    if m and any(m.group(s) for s in SLOT_NAMES):
        return {s: m.group(s) for s in SLOT_NAMES}, 1
    m = RE_P2.match(w)
    if m and any(m.group(s) for s in SLOT_NAMES):
        return {s: m.group(s) for s in SLOT_NAMES}, 2
    m = RE_P3.match(w)
    if m and any(m.group(s) for s in SLOT_NAMES):
        return {s: m.group(s) for s in SLOT_NAMES}, 3
    return None, 0

# ---------------- info-theory helpers ----------------

def H(counter):
    n = sum(counter.values())
    if n == 0: return 0.0
    return -sum(c/n * math.log2(c/n) for c in counter.values() if c)

def entropy_of(seq):
    return H(Counter(seq))

def mi(xs, ys):
    """MLE mutual information between two aligned sequences (bits)."""
    n = len(xs)
    cx, cy, cxy = Counter(xs), Counter(ys), Counter(zip(xs, ys))
    s = 0.0
    for (x, y), c in cxy.items():
        s += c/n * math.log2((c/n) / ((cx[x]/n) * (cy[y]/n)))
    return s

def mi_corrected(xs, ys, nshuf=5, rng=None):
    """Shuffle-corrected MI: raw minus mean MI after permuting ys."""
    rng = rng or random.Random(42)
    raw = mi(xs, ys)
    ys = list(ys)
    base = []
    for _ in range(nshuf):
        rng.shuffle(ys)
        base.append(mi(xs, ys))
    bmean = sum(base)/len(base)
    bstd = (sum((b-bmean)**2 for b in base)/len(base)) ** 0.5
    return raw - bmean, raw, bmean, bstd

def cond_entropy_orders(sym_seq, max_order=2):
    """H(X | previous k symbols) for k=0..max_order, MLE."""
    out = []
    n = len(sym_seq)
    for k in range(max_order+1):
        ctx = Counter(); joint = Counter()
        for i in range(k, n):
            c = tuple(sym_seq[i-k:i])
            ctx[c] += 1; joint[(c, sym_seq[i])] += 1
        h = 0.0
        for (c, x), cnt in joint.items():
            p = cnt/(n-k)
            h -= p * math.log2(cnt/ctx[c])
        out.append(h)
    return out

def js_divergence(p, q):
    """Jensen-Shannon divergence between two prob dicts/lists (bits)."""
    keys = set(range(max(len(p), len(q))))
    def g(v, i): return v[i] if i < len(v) else 0.0
    d = 0.0
    for i in keys:
        pi, qi, mi_ = g(p, i), g(q, i), (g(p, i)+g(q, i))/2
        if pi: d += 0.5*pi*math.log2(pi/mi_)
        if qi: d += 0.5*qi*math.log2(qi/mi_)
    return d

def chi2_rank(p, q):
    """Chi-square-style distance between rank-sorted prob vectors."""
    L = max(len(p), len(q))
    def g(v, i): return v[i] if i < len(v) else 0.0
    s = 0.0
    for i in range(L):
        a, b = g(p, i), g(q, i)
        if a+b > 0: s += (a-b)**2 / (a+b)
    return s

def rank_probs(counter, drop_space=True):
    n = sum(counter.values())
    return sorted((c/n for c in counter.values()), reverse=True)
