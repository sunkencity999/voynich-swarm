#!/usr/bin/env python3
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r = json.load(open('wordorder_results.json'))
DIST = [1, 2, 4, 8, 16]

BG = '#1e1a14'; FG = '#e8dcc0'; GRID = '#3a342a'
COLORS = {'voynich': '#e8b84b', 'latin': '#8fb573', 'english': '#6da8c9',
          'italian': '#b389c9'}
LABELS = {'voynich': 'Voynich (EVA, ZL3b)', 'latin': 'Latin (Caesar)',
          'english': 'English (Austen)', 'italian': 'Italian (Dante)'}

plt.rcParams.update({'figure.facecolor': BG, 'axes.facecolor': BG,
    'axes.edgecolor': GRID, 'axes.labelcolor': FG, 'text.color': FG,
    'xtick.color': FG, 'ytick.color': FG, 'grid.color': GRID,
    'font.size': 11})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# left: shuffle-corrected MI decay, linear scale
# right: same, log-y to show the Voynich long-range plateau vs naturals at ~0
for ax in (ax1, ax2):
    for name in ['italian', 'english', 'latin', 'voynich']:
        v = r[name]
        ys = [v['MI_corrected'][str(d)] for d in DIST]
        # shuffle noise band (±2 std of the shuffle-baseline MI estimate)
        errs = [2 * v['MI_shuf'][str(d)][1] for d in DIST]
        lw = 2.8 if name == 'voynich' else 1.8
        ax.plot(DIST, ys, '-', color=COLORS[name], lw=lw, marker='o', ms=6,
                label=LABELS[name])
        ax.fill_between(DIST, [y-e for y, e in zip(ys, errs)],
                        [y+e for y, e in zip(ys, errs)],
                        color=COLORS[name], alpha=0.18)
    ax.set_xscale('log', base=2)
    ax.set_xticks(DIST); ax.set_xticklabels([str(d) for d in DIST])
    ax.set_xlabel('word distance d')
    ax.grid(True, alpha=0.4)

ax1.axhline(0, color='#c95f5f', ls='--', lw=1.2, alpha=0.8)
ax1.text(1.05, 0.012, 'shuffle baseline (bias-corrected zero)',
         color='#c95f5f', fontsize=9)
ax1.set_ylabel('shuffle-corrected MI  I(W$_i$;W$_{i+d}$)  [bits]')
ax1.set_title('Word-order information vs distance', color=FG)
ax1.legend(facecolor=BG, edgecolor=GRID, labelcolor=FG)

ax2.set_yscale('log')
ax2.set_ylim(1e-3, 1.2)
ax2.set_ylabel('corrected MI [bits, log scale]')
ax2.set_title('Log view: Voynich plateau vs natural-language decay', color=FG)

fig.suptitle('Voynich phase 2 — how much information does word order carry?',
             color=FG, fontsize=14, y=1.00)
fig.tight_layout()
fig.savefig('voynich_wordorder_chart.png', dpi=150, facecolor=BG,
            bbox_inches='tight')
print('saved voynich_wordorder_chart.png')
