#!/usr/bin/env python3
"""Phase 6 chart: label anchoring rate vs permutation null (left) +
label-enriched vs label-avoidant word families (right).
Dark-parchment theme. Run: uvx --with matplotlib --with numpy python3 make_chart_phase6.py"""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, GRID, MUT = '#e0b23c', '#3a3020', '#6e5f45'
GREEN, RED, BLUE = '#7fbf5f', '#d96a5f', '#63c7c9'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'savefig.facecolor': BG, 'text.color': INK,
    'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK,
    'axes.edgecolor': GRID, 'grid.color': GRID, 'font.size': 11,
})

A = json.load(open('phase6_anchoring2.json'))['anchoring_all']
L = json.load(open('phase6_lexicon.json'))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 6.4),
                               gridspec_kw={'width_ratios': [1, 1.15]})
fig.suptitle('Voynich phase 6 — do labels talk to their pages?', fontsize=15,
             color=GOLD, y=0.98)

# ---- left: anchoring rate vs null ----
rows = [('ALL (pooled)', A['pooled'])] + [
    (s, d) for s, d in sorted(A['per_section'].items())
    if s not in ('text',) and d['n_label_words'] >= 100]
names = [r[0] for r in rows]
obs = [r[1]['same_page_rate'] for r in rows]
nmean = [r[1]['null_mean'] for r in rows]
nstd = [r[1]['null_std'] for r in rows]
y = np.arange(len(rows))[::-1]
ax1.barh(y + 0.18, obs, height=0.34, color=GOLD, label='observed same-page rate')
ax1.barh(y - 0.18, nmean, height=0.34, color=MUT, label='permutation null (±2σ)')
ax1.errorbar(nmean, y - 0.18, xerr=2 * np.array(nstd), fmt='none',
             ecolor=INK, elinewidth=1.2, capsize=3, alpha=0.8)
for yi, r in zip(y, rows):
    d = r[1]
    ax1.text(max(d['same_page_rate'], d['null_mean']) + 0.008, yi,
             f"z={d['z']:.1f}" + (f", p={d['p_perm']:.3f}" if r[0].startswith('ALL') else ''),
             va='center', fontsize=9, color=INK)
ax1.set_yticks(y)
ax1.set_yticklabels([f"{n}\n(n={r['n_label_words']})" for (n, r) in rows], fontsize=9)
ax1.set_xlabel('label word appears in same-page running text (rate)')
ax1.set_title('Label→page anchoring vs shuffled-page null', fontsize=11)
ax1.legend(loc='lower right', fontsize=9, facecolor=PANEL, edgecolor=GRID)
ax1.grid(axis='x', alpha=0.4)
ax1.set_axisbelow(True)

# ---- right: label-enriched / label-avoidant families ----
fams = L['label_families_top'][:10] + L['label_families_bottom'][-6:]
fams = sorted(fams, key=lambda r: r['z'], reverse=True)
names2 = [f"{r['family']}-" for r in fams]
zs = [r['z'] for r in fams]
cols = [GREEN if z > 0 else RED for z in zs]
y2 = np.arange(len(fams))[::-1]
ax2.barh(y2, zs, color=cols, height=0.7)
for yi, r in zip(y2, fams):
    ax2.text(r['z'] + (0.4 if r['z'] > 0 else -0.4), yi,
             f"{r['label_n']}/{r['corpus_n']}", va='center',
             ha='left' if r['z'] > 0 else 'right', fontsize=8, color=INK)
ax2.axvline(0, color=INK, lw=0.8)
ax2.set_xlim(min(zs) - 4.5, max(zs) + 3.5)
ax2.set_yticks(y2)
ax2.set_yticklabels(names2, fontsize=10, family='monospace')
ax2.set_xlabel('label enrichment z (binomial, vs corpus share)')
ax2.set_title('Word-initial families: label-enriched (green) vs avoidant (red)\n'
              'labels shun q- and benches, favor o+gallows', fontsize=11)
ax2.grid(axis='x', alpha=0.4)
ax2.set_axisbelow(True)

fig.text(0.5, 0.01,
         'ZL3b-n IVTFF loci: 1,026 label loci / 1,169 words. Null: label sets permuted across '
         'pages within section (20k perms). Zodiac labels within one folio share structure (z≈14); '
         'consensus plant-name pairing: null.',
         ha='center', fontsize=8.5, color=MUT)
plt.tight_layout(rect=[0, 0.035, 1, 0.95])
out = '../charts/voynich_labels_chart.png'
plt.savefig(out, dpi=140)
print('wrote', out)
