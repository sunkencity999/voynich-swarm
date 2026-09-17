#!/usr/bin/env python3
"""Phase 6 shared library: full IVTFF locus parsing WITH locus types
(labels vs paragraphs), per the IVTFF 2.0 spec (voynich.nu, Feb 2023).

Locus id format: <folio.num,XTT>  where X = locator (@ + * = & ~ / !)
and TT = locus type: P0/P1/Pb/Pc/Pr/Pt (paragraph text), L0/La/Lc/Lf/Ln/
Lp/Ls/Lt/Lz/Lx (labels), Ca/Cc (circular), Ri/Ro (radial).

Label subtype meanings (IVTFF 2.0 Table):
  L0 not clearly near any drawing element
  La astronomical/cosmological element (not star, not zodiac)
  Lc container (pharma section jars)
  Lf fragment of a herb (pharma section plant parts)
  Ln nymph (biological/balneo section)
  Lp large herb/plant drawing (herbal section)
  Ls star
  Lt tube or tub (balneo, non-nymph)
  Lx extraneous writing (margins) -- EXCLUDED from label analyses
  Lz zodiac element

Cleaning matches phase4_lib.extract_structured / clean_ivtff.py:
[x:y] -> x, <...> and {...} stripped, lowercase, tokens must be [a-z]+.
"""
import re
from collections import Counter, defaultdict

PARA_TYPES = {'P0', 'P1', 'Pb', 'Pc', 'Pr', 'Pt'}
LABEL_TYPES = {'L0', 'La', 'Lc', 'Lf', 'Ln', 'Lp', 'Ls', 'Lt', 'Lz'}
CIRC_TYPES = {'Ca', 'Cc', 'Ri', 'Ro'}

# section map, zodiac kept separate this phase (phase 5 merged Z into astro)
SECTION_MAP = {'H': 'herbal', 'A': 'astro', 'Z': 'zodiac', 'C': 'cosmo',
               'B': 'balneo', 'P': 'pharma', 'S': 'recipes', 'T': 'text'}

LOCUS_RE = re.compile(r'^<(f[^.>]+)\.(\d+[a-z]?),([@+*=&~/!])([A-Z][a-z0-9])>\s*(.*)$')
PAGE_RE = re.compile(r'^<(f[^.>]+)>\s*(.*)$')


def clean_words(text):
    text = re.sub(r'\[([^\]:]*):[^\]]*\]', r'\1', text)
    text = re.sub(r'<[^>]*>', ' ', text)
    text = re.sub(r'\{[^}]*\}', ' ', text)
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = text.lower()
    return [t for t in re.split(r'[.,\s]+', text) if t and re.fullmatch(r'[a-z]+', t)]


def extract_loci(path='ZL3b-n.txt'):
    """Every locus in the file: dict(folio, num, locator, ltype, lang, ill,
    section, words). Empty-word loci retained (words=[])."""
    out = []
    cur_lang = cur_ill = cur_folio = None
    for raw in open(path, encoding='latin-1'):
        raw = raw.strip()
        if not raw or raw.startswith('#'):
            continue
        m = LOCUS_RE.match(raw)
        if m:
            folio, num, locator, ltype, text = m.groups()
            out.append({'folio': folio, 'num': num, 'locator': locator,
                        'ltype': ltype, 'lang': cur_lang, 'ill': cur_ill,
                        'section': SECTION_MAP.get(cur_ill, 'text'),
                        'words': clean_words(text)})
            continue
        m = PAGE_RE.match(raw)
        if m and '.' not in m.group(1):
            cur_folio = m.group(1)
            lm = re.search(r'\$L=(\w)', m.group(2))
            im = re.search(r'\$I=(\w)', m.group(2))
            cur_lang = lm.group(1) if lm else None
            cur_ill = im.group(1) if im else None
    return out


def split_loci(loci):
    labels = [l for l in loci if l['ltype'] in LABEL_TYPES]
    paras = [l for l in loci if l['ltype'] in PARA_TYPES]
    circ = [l for l in loci if l['ltype'] in CIRC_TYPES]
    other = [l for l in loci if l['ltype'] == 'Lx']
    return labels, paras, circ, other


def edit_distance(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1,
                           prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
