#!/usr/bin/env python3
"""Prepare size-matched corpora: latin, english, italian cleaned like voynich;
plus char-shuffled and word-shuffled Voynich controls. All truncated to the
same char count (min of all cleaned corpora, expected = voynich size)."""
import re, random, unicodedata, json

random.seed(42)

def clean_gutenberg(path):
    txt = open(path, encoding='utf-8').read()
    # strip PG header/footer
    m = re.search(r'\*\*\* START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*\*\*\*', txt)
    if m: txt = txt[m.end():]
    m = re.search(r'\*\*\* END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK', txt)
    if m: txt = txt[:m.start()]
    # strip accents -> ascii
    txt = unicodedata.normalize('NFKD', txt)
    txt = ''.join(c for c in txt if not unicodedata.combining(c))
    txt = txt.lower()
    words = re.findall(r'[a-z]+', txt)
    return words

corpora = {}
corpora['voynich'] = open('voynich_clean.txt').read().split()
corpora['latin'] = clean_gutenberg('raw_latin.txt')
corpora['english'] = clean_gutenberg('raw_english.txt')
corpora['italian'] = clean_gutenberg('raw_italian.txt')

sizes = {k: len(' '.join(v)) for k, v in corpora.items()}
print("cleaned sizes (chars):", sizes)
target = min(sizes.values())
print("target size:", target)

def truncate(words, nchars):
    out, total = [], -1  # first word has no preceding space
    for w in words:
        add = len(w) + 1
        if total + add > nchars: break
        out.append(w); total += add
    return out

final = {k: truncate(v, target) for k, v in corpora.items()}

# control 1: char-shuffled voynich — shuffle all characters across corpus,
# refill the same word-length skeleton (preserves char freqs + word lengths)
vw = final['voynich']
chars = list(''.join(vw))
random.shuffle(chars)
shuf, i = [], 0
for w in vw:
    shuf.append(''.join(chars[i:i+len(w)])); i += len(w)
final['charshuf'] = shuf

# control 2: word-shuffled voynich (preserves morphology, destroys order)
ws = list(vw)
random.shuffle(ws)
final['wordshuf'] = ws

stats = {}
for k, v in final.items():
    s = ' '.join(v)
    open(f'corpus_{k}.txt', 'w').write(s)
    stats[k] = {'chars': len(s), 'words': len(v), 'uniq': len(set(v)),
                'mean_wordlen': round(sum(map(len, v))/len(v), 3)}
print(json.dumps(stats, indent=2))
json.dump(stats, open('corpus_stats.json', 'w'), indent=2)
