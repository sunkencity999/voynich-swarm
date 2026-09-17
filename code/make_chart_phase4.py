#!/usr/bin/env python3
"""Phase 4 chart: slot-grammar entropy profile + information-vs-length curves.
Left  : per-slot entropy bars (gold = kept residue slots, muted = stripped shell).
Right : word information content vs word length, Voynich vs Latin.
Dark-parchment theme, consistent with phases 1-3."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R = json.load(open('phase4_results.json'))

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, LAT, GRID = '#e0b23c', '#8f7a5a', '#3a3020'
SHELL, TEAL = '#6e5f45', '#63c7c9'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'savefig.facecolor': BG, 'text.color': INK,
    'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK,
    'axes.edgecolor': GRID, 'font.size': 11,
})

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 5.8))

# ------------- LEFT: per-slot entropy -------------
slots = R['grammar']['slot_names']
kept = set(R['residue_def']['kept_slots'])
Hs = [R['slots'][s]['entropy'] for s in slots]
fills = [R['slots'][s]['fill_rate'] for s in slots]
colors = [GOLD if s in kept else SHELL for s in slots]
x = range(len(slots))
bars = axL.bar(x, Hs, color=colors, edgecolor=GRID, linewidth=0.6)
for xi, (h, f) in enumerate(zip(Hs, fills)):
    axL.text(xi, h + 0.04, f'{int(round(f*100))}%', ha='center', va='bottom',
             fontsize=7.5, color=INK, alpha=0.75)
axL.axhline(0.9, color=TEAL, lw=1.0, ls='--', alpha=0.8)
axL.text(len(slots)-0.4, 0.94, 'residue cut (0.9 bit)', ha='right',
         fontsize=8.5, color=TEAL)
axL.set_xticks(list(x))
axL.set_xticklabels(slots, rotation=55, ha='right', fontsize=9)
axL.set_ylabel('slot entropy (bits, incl. empty)')
axL.set_title('Slot grammar: 15 ordered slots, 93% of tokens parsed\n'
              'gold = information-bearing residue · brown = low-info shell '
              '(labels: fill rate)', fontsize=10.5)
axL.grid(axis='y', color=GRID, lw=0.6, alpha=0.7)
axL.set_axisbelow(True)

# ------------- RIGHT: info vs length -------------
def curve(d, nmin=30, lmax=10):
    pts = [(int(k), v['mean_info']) for k, v in d.items()
           if v['n'] >= nmin and int(k) <= lmax]
    pts.sort()
    return [p[0] for p in pts], [p[1] for p in pts]

xv, yv = curve(R['pad_voy_unigram'])
xl, yl = curve(R['pad_lat_unigram'])
xs, ys = curve(R['pad_voy_slotinfo'])
xvb, yvb = curve(R['pad_voy_bigram'])
xlb, ylb = curve(R['pad_lat_bigram'])

axR.plot(xvb, yvb, color=GOLD, lw=1.2, ls=':', alpha=0.8,
         label='Voynich · char-bigram model')
axR.plot(xlb, ylb, color=LAT, lw=1.2, ls=':', alpha=0.8,
         label='Latin · char-bigram model')
axR.plot(xs, ys, color=TEAL, lw=1.6, ls='--', marker='s', ms=3.5,
         label='Voynich · independent-slot model')
axR.plot(xv, yv, color=GOLD, lw=2.4, marker='o', ms=5,
         label='Voynich · true word info  (0.97 b/glyph)')
axR.plot(xl, yl, color='#b09468', lw=2.4, marker='o', ms=5,
         label='Latin · true word info  (0.85 b/letter)')
axR.set_xlabel('word length (glyphs / letters)')
axR.set_ylabel('mean information content (bits)')
axR.set_title('Verbose-padding test: information vs word length\n'
              'true word info (−log₂ p(word)) grows Latin-like — words are not '
              'hollow', fontsize=10.5)
axR.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=INK, fontsize=8.5,
           loc='upper left')
axR.grid(color=GRID, lw=0.6, alpha=0.7)
axR.set_axisbelow(True)

fig.suptitle('Voynich phase 4 — slot-grammar decomposition & verbose-cipher attack',
             fontsize=13, y=0.99)
fig.tight_layout(rect=(0, 0, 1, 0.96))
out = '../charts/voynich_slotgrammar_chart.png'
fig.savefig(out, dpi=160)
print('wrote', out)
