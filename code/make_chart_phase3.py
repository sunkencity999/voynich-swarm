#!/usr/bin/env python3
"""Phase 3 chart: real Voynich vs tuned self-citation generator.
Left panel  : shuffle-corrected mutual information vs word distance (log-x).
Right panel : BPE compression (chars/token) vs vocab size.
Dark-parchment theme; generator shown as mean line + ±1σ band from 5 runs.
"""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

R = json.load(open('phase3_results.json'))['metrics']

# ---- palette ----
BG      = '#211b12'   # dark parchment brown
PANEL   = '#2b2418'
INK     = '#e8dcc0'   # aged ink / parchment text
GOLD    = '#e0b23c'   # Voynich real
SYNTH   = '#63c7c9'   # generator (teal)
LAT     = '#8f7a5a'
ENG     = '#a06a6a'
ITA     = '#6a8a6a'
GRID    = '#3a3020'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'savefig.facecolor': BG, 'text.color': INK,
    'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK,
    'axes.edgecolor': GRID, 'font.size': 11,
})

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 5.6))

# ============================ LEFT: MI decay ============================
D = [1, 2, 4, 8, 16]
real_mi = [0.1815, 0.0694, 0.0556, 0.0498, 0.0329]
lat_mi  = [0.2580, 0.0429, 0.0121, 0.0003, -0.0006]
eng_mi  = [0.7356, 0.2798, 0.0329, 0.0144, 0.0075]
ita_mi  = [0.4678, 0.0956, 0.0174, 0.0159, -0.0031]
gen_mi  = [R[f'MI_d{d}'][0] for d in D]
gen_sd  = [R[f'MI_d{d}'][1] for d in D]

axL.plot(D, eng_mi, '-', color=ENG, lw=1.3, alpha=.75, label='English (Austen)')
axL.plot(D, ita_mi, '-', color=ITA, lw=1.3, alpha=.75, label='Italian (Dante)')
axL.plot(D, lat_mi, '-', color=LAT, lw=1.3, alpha=.75, label='Latin (Caesar)')
axL.plot(D, real_mi, 'o-', color=GOLD, lw=2.6, ms=7, label='Voynich (real)', zorder=6)
axL.plot(D, gen_mi, 's--', color=SYNTH, lw=2.4, ms=6,
         label='Self-citation generator', zorder=5)
axL.fill_between(D, [m-s for m, s in zip(gen_mi, gen_sd)],
                 [m+s for m, s in zip(gen_mi, gen_sd)], color=SYNTH, alpha=.18)
axL.axhline(0, color=GRID, lw=1)
axL.set_xscale('log', base=2); axL.set_xticks(D); axL.set_xticklabels(D)
axL.set_xlabel('word distance  d'); axL.set_ylabel('shuffle-corrected MI  (bits)')
axL.set_title('Long-range mutual information', color=INK, fontsize=13, pad=10)
axL.grid(True, color=GRID, lw=.6, alpha=.5)
axL.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=INK, fontsize=9, loc='upper right')
axL.annotate('real decays 0.18 → 0.03\n(peak then plateau)', xy=(2, 0.069),
             xytext=(3.2, 0.20), color=GOLD, fontsize=8.5,
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1))
axL.annotate('generator: flat ~0.12\n(no short-range peak,\novershoots long range)',
             xy=(8, gen_mi[3]), xytext=(4.5, 0.42), color=SYNTH, fontsize=8.5,
             arrowprops=dict(arrowstyle='->', color=SYNTH, lw=1))

# ======================= RIGHT: BPE compression =======================
Vx = [500, 1000, 2000]
real_c = [4.147, 4.594, 4.981]
lat_c  = [3.036, 3.717, 4.549]
eng_c  = [3.162, 3.805, 4.481]
ita_c  = [3.012, 3.436, 3.864]
gen_c  = [R[f'bpe_comp_{v}'][0] for v in Vx]
gen_cs = [R[f'bpe_comp_{v}'][1] for v in Vx]

# natural-language band
nat_lo = [min(a, b, c) for a, b, c in zip(lat_c, eng_c, ita_c)]
nat_hi = [max(a, b, c) for a, b, c in zip(lat_c, eng_c, ita_c)]
axR.fill_between(Vx, nat_lo, nat_hi, color=LAT, alpha=.18,
                 label='natural-language band')
axR.plot(Vx, real_c, 'o-', color=GOLD, lw=2.6, ms=7, label='Voynich (real)', zorder=6)
axR.plot(Vx, gen_c, 's--', color=SYNTH, lw=2.4, ms=6,
         label='Self-citation generator', zorder=5)
axR.fill_between(Vx, [m-s for m, s in zip(gen_c, gen_cs)],
                 [m+s for m, s in zip(gen_c, gen_cs)], color=SYNTH, alpha=.20)
axR.set_xscale('log', base=2); axR.set_xticks(Vx); axR.set_xticklabels(Vx)
axR.set_xlabel('BPE vocab size'); axR.set_ylabel('compression  (chars / token)')
axR.set_title('BPE morphology compression', color=INK, fontsize=13, pad=10)
axR.grid(True, color=GRID, lw=.6, alpha=.5)
axR.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=INK, fontsize=9, loc='upper left')
axR.annotate('generator overshoots\nat large vocab', xy=(2000, gen_c[2]),
             xytext=(720, 5.25), color=SYNTH, fontsize=8.5,
             arrowprops=dict(arrowstyle='->', color=SYNTH, lw=1))

fig.suptitle('Voynich Phase 3 — self-citation generator vs the real manuscript',
             color=INK, fontsize=15, y=0.99)
fig.text(0.5, 0.005,
         'Generator tuned only on unigram entropy, type-token ratio, and repeat rate '
         '(tau=250, p_exact=0.78, p2=0.2). MI shape & BPE curve are held out.',
         ha='center', color=INK, fontsize=8.5, alpha=.75)
fig.tight_layout(rect=[0, 0.02, 1, 0.96])
out = '../charts/voynich_selfcite_chart.png'
fig.savefig(out, dpi=130)
print('wrote', out)
