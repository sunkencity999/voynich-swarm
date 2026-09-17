#!/usr/bin/env python3
"""Clean IVTFF (ZL3b-n) -> plain EVA word-per-space text.

Rules:
- drop comment lines (#) and page-header lines (<fNN..> with no text)
- strip locus tags <fN.M,XX> at line start
- inline <...> tags removed (incl. <!...> comments, <%>, <$>, <->)
- [x:y] alternative readings -> take FIRST alternative x
- {...} annotations removed entirely
- '.' and ',' -> word separator (space)
- lowercase; drop tokens containing anything outside [a-z] (unreadable '?',
  high-ascii @nnn; codes, etc.)
"""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
words = []
dropped_tokens = 0
for line in open(src, encoding='latin-1'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    m = re.match(r'^<f[^>]*>\s*(.*)$', line)
    if m is None:
        continue  # not a locus line
    text = m.group(1)
    if not text:
        continue
    # first alternative in [x:y] (may have >1 colon)
    text = re.sub(r'\[([^\]:]*):[^\]]*\]', r'\1', text)
    # remove inline tags/comments <...> and annotations {...} and any residual [..]
    text = re.sub(r'<[^>]*>', ' ', text)
    text = re.sub(r'\{[^}]*\}', ' ', text)
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = text.lower()
    for tok in re.split(r'[.,\s]+', text):
        if not tok:
            continue
        if re.fullmatch(r'[a-z]+', tok):
            words.append(tok)
        else:
            dropped_tokens += 1

out = ' '.join(words)
open(dst, 'w').write(out)
print(f"words={len(words)} chars={len(out)} dropped_tokens={dropped_tokens} uniq_words={len(set(words))}")
