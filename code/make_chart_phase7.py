#!/usr/bin/env python3
"""Phase 7 chart: feature x family association heatmap (left) + the surviving
cell's direction and Mantel scatter (right). Dark-parchment theme.
Run: uvx --with matplotlib --with numpy python3 make_chart_phase7.py"""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, GRID, MUT = '#e0b23c', '#3a3020', '#6e5f45'
GREEN, RED, BLUE = '#7fbf5f', '#d96a5f', '#63c7c9'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'savefig.facecolor': BG, 'text.color': INK,
    'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK,
    'axes.edgecolor': GRID, 'grid.color': GRID, 'font.size': 10,
})

R = json.load(open('phase7_results.json'))
F = json.load(open('phase7_features.json'))['features']
assoc = R['association']
folios = R['folios']

FEATS = ["leaf_shape","leaf_arrangement","root_type","root_prominence",
         "flower_present","flower_color","flower_shape","stem_count","plant_count"]
# families: named + a selection of frequent prefixes actually tested
fams = sorted({k.split('|')[1] for k in assoc})
named = [f for f in fams if f.startswith('fam:')]
p2 = [f for f in fams if f.startswith('p2:')]
# order p2 by best (min) p to show the interesting ones, cap 20
p2s = sorted(p2, key=lambda f: min(assoc.get(f"{ft}|{f}", {'p': 1})['p'] for ft in FEATS))[:20]
cols = named + p2s

M = np.full((len(FEATS), len(cols)), np.nan)
S = np.zeros_like(M, dtype=bool)
for i, ft in enumerate(FEATS):
    for j, fm in enumerate(cols):
        c = assoc.get(f"{ft}|{fm}")
        if c:
            p = c.get('p_refined', c['p'])
            M[i, j] = -np.log10(max(p, 1e-6))
            S[i, j] = c.get('fdr_survives', False)

fig = plt.figure(figsize=(14.4, 7.2))
gs = fig.add_gridspec(2, 2, width_ratios=[1.9, 1], hspace=0.42, wspace=0.16,
                      left=0.09, right=0.97, top=0.86, bottom=0.13)
axh = fig.add_subplot(gs[:, 0])
axd = fig.add_subplot(gs[0, 1])
axm = fig.add_subplot(gs[1, 1])
fig.suptitle('Voynich phase 7 — does the vocabulary track the botany?',
             fontsize=15, color=GOLD, y=0.965)

cmap = LinearSegmentedColormap.from_list('parch', ['#2b2418', '#6e5f45', '#e0b23c', '#f4e6b8'])
im = axh.imshow(M, aspect='auto', cmap=cmap, vmin=0, vmax=4.2)
for i in range(len(FEATS)):
    for j in range(len(cols)):
        if S[i, j]:
            axh.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=False,
                                        edgecolor=RED, lw=2.2))
axh.set_xticks(range(len(cols)))
axh.set_xticklabels([c.replace('p2:', '').replace('fam:', '')+('-' if True else '')
                     for c in cols], rotation=60, ha='right', fontsize=8.5)
axh.set_yticks(range(len(FEATS)))
axh.set_yticklabels(FEATS, fontsize=9.5)
axh.set_title(f'association matrix, −log₁₀(p), {R["n_tests"]} permutation tests\n'
              f'red box = survives BH-FDR q=0.05 (1 of {R["n_tests"]}) — root_prominence × or-',
              fontsize=10.5, color=INK)
cb = fig.colorbar(im, ax=axh, fraction=0.032, pad=0.015)
cb.ax.tick_params(labelsize=8)
cb.set_label('−log₁₀(p)', fontsize=9)

# direction panel: or- freq by root prominence
from collections import defaultdict
import re as _re
fw_or = {}
# recompute quickly from results-side stored profiles is not saved; recompute here
import sys; sys.path.insert(0, '.')
from run_phase7 import load_folio_words, build_families, folio_profiles
fw = load_folio_words(); fams_fn = build_families(fw)
names, X, freq, tot = folio_profiles(fw, fams_fn, folios)
jo = names.index('p2:or')
groups = defaultdict(list)
for i, f in enumerate(folios):
    groups[F[f]['root_prominence']].append(freq[i, jo])
order = ['minor', 'moderate', 'dominant']
data = [groups[g] for g in order]
bp = axd.boxplot(data, tick_labels=[f'{g}\n(n={len(groups[g])})' for g in order],
                 patch_artist=True, widths=0.55,
                 medianprops=dict(color=GOLD, lw=2),
                 boxprops=dict(facecolor='#3a3020', edgecolor=MUT),
                 whiskerprops=dict(color=MUT), capprops=dict(color=MUT),
                 flierprops=dict(marker='.', markerfacecolor=MUT, markeredgecolor=MUT))
for k, g in enumerate(order):
    xs = np.random.default_rng(3).normal(k+1, 0.06, len(groups[g]))
    axd.plot(xs, groups[g], '.', color=BLUE, ms=4, alpha=0.7, zorder=3)
axd.set_title('the surviving cell: or- word share rises with\nroot dominance in the drawing '
              f'(p={assoc["root_prominence|p2:or"].get("p_refined"):.1e}; dialect-stratified p=1.0e-3)',
              fontsize=9.8)
axd.set_ylabel('or- token share of folio text', fontsize=9)
axd.grid(True, axis='y', alpha=0.35)

# Mantel scatter
d = np.load('phase7_mantel.npz', allow_pickle=True)
vis, txt = d['vis'], d['txt']
iu = np.triu_indices(vis.shape[0], 1)
rng = np.random.default_rng(11)
sel = rng.choice(len(iu[0]), 1600, replace=False)
axm.plot(vis[iu][sel] + rng.normal(0, 0.012, 1600), txt[iu][sel], '.', ms=2.5,
         color=BLUE, alpha=0.35)
mm = R['mantel']
axm.set_title(f'folio-pair similarity: visual vs textual (Mantel)\nr={mm["r"]:.3f}, p={mm["p"]:.3f} — null',
              fontsize=10)
axm.set_xlabel('visual feature distance (folio pair)', fontsize=9)
axm.set_ylabel('word-profile distance', fontsize=9)
axm.grid(True, alpha=0.35)

fig.text(0.09, 0.02,
         'local VL extraction of 9 plant features on 129 herbal folios (self-agreement 0.9–1.0) × 37 word families; '
         'Kruskal–Wallis + ≥50k permutations; BH-FDR q=0.05. Drawings also track dialect: dominant roots on 66% of Currier-B vs 23% of A folios (p=2.5e-4).',
         fontsize=8.4, color=MUT)
plt.savefig('../charts/voynich_image_pairing.png', dpi=130)
print('saved ../charts/voynich_image_pairing.png')
