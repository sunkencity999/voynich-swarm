#!/usr/bin/env python3
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d = json.load(open('plot_data.json'))
comp, zipf = d['comp_curves'], d['zipf_curves']

BG = '#1e1a14'; FG = '#e8dcc0'; GRID = '#3a342a'
COLORS = {'voynich': '#e8b84b', 'latin': '#8fb573', 'english': '#6da8c9',
          'italian': '#b389c9', 'charshuf': '#c95f5f', 'wordshuf': '#7a7267'}
LABELS = {'voynich': 'Voynich (EVA, ZL3b)', 'latin': 'Latin (Caesar)',
          'english': 'English (Austen)', 'italian': 'Italian (Dante)',
          'charshuf': 'char-shuffled Voynich', 'wordshuf': 'word-shuffled Voynich'}

plt.rcParams.update({'figure.facecolor': BG, 'axes.facecolor': BG,
    'axes.edgecolor': GRID, 'axes.labelcolor': FG, 'text.color': FG,
    'xtick.color': FG, 'ytick.color': FG, 'grid.color': GRID,
    'font.size': 11})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

for name in ['charshuf', 'wordshuf', 'italian', 'english', 'latin', 'voynich']:
    c = comp[name]
    xs = sorted(int(k) for k in c)
    ys = [c[str(x)] if str(x) in c else c[x] for x in xs]
    lw = 2.8 if name == 'voynich' else 1.8
    ls = '--' if name in ('charshuf', 'wordshuf') else '-'
    ax1.plot(xs, ys, ls, color=COLORS[name], lw=lw, marker='o', ms=5,
             label=LABELS[name])
ax1.set_xlabel('BPE vocab size'); ax1.set_ylabel('compression (chars/token)')
ax1.set_title('BPE compression vs vocab size', color=FG)
ax1.set_xscale('log'); ax1.set_xticks([500, 1000, 2000])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.grid(True, alpha=0.5); ax1.legend(facecolor=BG, edgecolor=GRID, fontsize=9)

for name in ['charshuf', 'wordshuf', 'italian', 'english', 'latin', 'voynich']:
    freqs = zipf[name]
    ranks = range(1, len(freqs) + 1)
    lw = 2.4 if name == 'voynich' else 1.4
    ls = '--' if name in ('charshuf', 'wordshuf') else '-'
    ax2.loglog(ranks, freqs, ls, color=COLORS[name], lw=lw, label=LABELS[name])
ax2.set_xlabel('token rank'); ax2.set_ylabel('token frequency')
ax2.set_title('Zipf curves of BPE tokens (vocab 2000)', color=FG)
ax2.grid(True, which='both', alpha=0.35)

fig.suptitle('Voynich-BPE: does Voynichese tokenize like language or gibberish?',
             color='#f0e6cc', fontsize=14, y=1.0)
fig.tight_layout()
fig.savefig('voynich_bpe_chart.png', dpi=140, facecolor=BG,
            bbox_inches='tight')
print('wrote voynich_bpe_chart.png')
