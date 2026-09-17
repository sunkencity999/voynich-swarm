#!/usr/bin/env python3
"""Phase 6 step 1: label census. Checkpoint -> phase6_labels.json"""
import json
from collections import Counter, defaultdict
from phase6_lib import extract_loci, split_loci, LABEL_TYPES

loci = extract_loci()
labels, paras, circ, extra = split_loci(loci)

print(f"total loci: {len(loci)}")
print(f"paragraph loci: {len(paras)}  ({sum(len(l['words']) for l in paras)} words)")
print(f"label loci: {len(labels)}  ({sum(len(l['words']) for l in labels)} words)")
print(f"circular/radial loci: {len(circ)}  ({sum(len(l['words']) for l in circ)} words)")
print(f"extraneous Lx loci (excluded): {len(extra)}")

by_type = Counter(l['ltype'] for l in labels)
by_sec = Counter(l['section'] for l in labels)
print("\nlabel loci by type:", dict(by_type.most_common()))
print("label loci by section:", dict(by_sec.most_common()))

# word-level stats
label_words = [w for l in labels for w in l['words']]
wc = Counter(label_words)
print(f"\nlabel words: {len(label_words)} tokens, {len(wc)} types")
print(f"repeated label words (freq>=2): {sum(1 for w,c in wc.items() if c>=2)} types, "
      f"{sum(c for w,c in wc.items() if c>=2)} tokens")
print("top 20 label words:", wc.most_common(20))

# multiword labels
mw = Counter(len(l['words']) for l in labels)
print("\nwords per label locus:", dict(sorted(mw.items())))

# per section+type matrix
mat = defaultdict(Counter)
for l in labels:
    mat[l['section']][l['ltype']] += 1
print("\nsection x type:")
for s, c in sorted(mat.items()):
    print(f"  {s:8s} {dict(c.most_common())}")

# folios with labels
folios = sorted({l['folio'] for l in labels})
print(f"\nfolios bearing labels: {len(folios)}")

json.dump({
    'total_loci': len(loci), 'n_para': len(paras), 'n_label': len(labels),
    'n_circ': len(circ), 'n_lx': len(extra),
    'label_type_counts': dict(by_type), 'label_section_counts': dict(by_sec),
    'label_tokens': len(label_words), 'label_types_unique': len(wc),
    'label_word_freq': dict(wc.most_common()),
    'words_per_label': {str(k): v for k, v in sorted(mw.items())},
    'section_x_type': {s: dict(c) for s, c in mat.items()},
    'label_folios': folios,
    'labels': [{'folio': l['folio'], 'ltype': l['ltype'], 'section': l['section'],
                'lang': l['lang'], 'words': l['words']} for l in labels],
}, open('phase6_labels.json', 'w'), indent=1)
print("\ncheckpoint -> phase6_labels.json")
