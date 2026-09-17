#!/usr/bin/env python3
"""Phase 5 charts (dark-parchment theme, consistent with phases 1-4).
1. voynich_semantic_space.png — t-SNE of Voynich word embeddings colored by
   dominant manuscript section, word-shuffled null inset.
2. voynich_alignment_scores.png — GW relational-alignment scores: ceiling vs
   Voynich pairs vs shuffled floors (the no-power calibration result).
Run under: uvx --with matplotlib --with numpy python3 make_chart_phase5.py"""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, GRID, MUT = '#e0b23c', '#3a3020', '#6e5f45'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'savefig.facecolor': BG, 'text.color': INK,
    'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK,
    'axes.edgecolor': GRID, 'grid.color': GRID, 'font.size': 11,
})

R = json.load(open('phase5_results.json'))
D = np.load('phase5_chart_data.npz', allow_pickle=True)

SEC_COL = {'herbal': '#7fbf5f', 'astro': '#63c7c9', 'balneo': '#5f8fd9',
           'pharma': '#d97fb8', 'recipes': '#e0b23c', 'none': '#555049'}

# ---------------- chart 1: semantic space ----------------
fig, ax = plt.subplots(figsize=(9.6, 7.6))
xy, dom, share, counts = D['v_xy'], D['v_dom'], D['v_share'], D['v_counts']
size = 8 + 3.5 * np.sqrt(counts)
for sec, col in SEC_COL.items():
    m = dom == sec
    if m.sum() == 0:
        continue
    lbl = f'{sec} ({m.sum()})' if sec != 'none' else None
    ax.scatter(xy[m, 0], xy[m, 1], s=size[m], c=col, alpha=0.75,
               linewidths=0, label=lbl)
ax.legend(loc='upper left', frameon=False, fontsize=10, markerscale=1.2)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title('Voynich word embeddings (PPMI+SVD, within-line windows only)\n'
             't-SNE projection - color = dominant manuscript section',
             fontsize=13)
mi = R['topic']
ax.text(0.02, 0.02,
        f"token cluster{chr(8596)}section MI = {mi['token_MI_bits']:.3f} bits   "
        f"(line-shuffled null {mi['null_mu']:.4f}{chr(177)}{mi['null_sd']:.4f}, z{chr(8776)}{mi['z']:.0f})",
        transform=ax.transAxes, fontsize=9.5, color=GOLD)
# inset: word-shuffled null
ins = fig.add_axes((0.66, 0.08, 0.30, 0.30))
ins.set_facecolor('#252017')
sxy, sdom = D['s_xy'], D['s_dom']
for sec, col in SEC_COL.items():
    m = sdom == sec
    if m.sum():
        ins.scatter(sxy[m, 0], sxy[m, 1], s=4, c=col, alpha=0.6, linewidths=0)
ins.set_xticks([]); ins.set_yticks([])
ins.set_title('word-shuffled null', fontsize=9, color=MUT)
for s in ins.spines.values():
    s.set_color(GRID)
fig.tight_layout()
fig.savefig('../charts/voynich_semantic_space.png', dpi=160)
print('wrote voynich_semantic_space.png')

# ---------------- chart 2: alignment scores ----------------
A = R['alignment']
order = ['ceiling: Latin→Italian', 'Voynich→Latin', 'Voynich→Italian',
         'floor: Voynich→shuffled-Latin', 'floor: Latin→shuffled-Latin',
         'floor: shuffled-Voynich→Latin']
labels = ['Latin→Italian\nCEILING', 'Voynich→\nLatin', 'Voynich→\nItalian',
          'Voynich→\nshuf Latin\nfloor', 'Latin→\nshuf Latin\nfloor',
          'shuf Voynich\n→Latin\nfloor']
vals = [A[k]['relational_rho'] for k in order]
cols = [MUT, GOLD, GOLD, '#555049', '#555049', '#555049']

fig, ax = plt.subplots(figsize=(10.2, 6.6))
fig.subplots_adjust(left=0.09, right=0.97, top=0.84, bottom=0.24)
floor_vals = vals[3:]
band_lo, band_hi = min(floor_vals) - 0.01, max(floor_vals) + 0.01
ax.axhspan(band_lo, band_hi, color='#453a26', alpha=0.55, zorder=0)
ax.text(5.45, band_hi + 0.004, 'shuffled-floor band', fontsize=9, color=MUT,
        ha='right')
bars = ax.bar(range(6), vals, color=cols, width=0.62, zorder=2)
for i, v in enumerate(vals):
    ax.text(i, v + 0.004, f'{v:.3f}', ha='center', fontsize=10,
            color=INK, zorder=3)
ax.set_xticks(range(6))
ax.set_xticklabels(labels, fontsize=9.5)
ax.set_ylabel('relational preservation (Spearman rho)', fontsize=10.5)
ax.set_ylim(0, max(vals) * 1.25)
ax.grid(axis='y', alpha=0.4)
ax.set_title('Unsupervised Gromov-Wasserstein alignment - calibrated result: NO POWER\n'
             'the real-language ceiling sits inside the shuffled-floor band '
             '(n=400 words, ~35K-token corpora)', fontsize=12.5)
ax.text(0.5, -0.31,
        'Every pairing aligns equally well: GW matches generic embedding-cloud geometry, not meaning.\n'
        'A nomenclator can be neither confirmed nor excluded by seed-free alignment at this corpus size - '
        'no Voynich "word translations" are claimable.',
        transform=ax.transAxes, fontsize=9.5, color=MUT, ha='center')
fig.savefig('../charts/voynich_alignment_scores.png', dpi=160)
print('wrote voynich_alignment_scores.png')
