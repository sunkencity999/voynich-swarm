#!/usr/bin/env python3
"""Phase 9 chart: (left) or- share by root prominence across three independent
transliterations (ZL baseline, IT/Takahashi, GC/v101); (mid) slot-aware medial-
only re-test; (right) cross-section decoupling cells (null). Hand-built SVG ->
cairosvg PNG, dark-parchment theme."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'phase9_results.json')))

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, GRID, MUT = '#e0b23c', '#3a3020', '#6e5f45'
GREEN, RED, BLUE = '#7fbf5f', '#d96a5f', '#63c7c9'
PURP = '#b78fd6'

W, H = 1560, 780
S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="{BG}"/>']

def txt(x, y, s, size=15, fill=INK, anchor='start', weight='normal'):
    S.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" '
             f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

txt(W/2, 40, 'Voynich phase 9 — the or-/root-prominence link replicates across transliterations and inside the line',
    22, GOLD, 'middle', 'bold')
txt(W/2, 66, 'ZL = Zandbergen–Landini (campaign baseline) · IT = Takahashi · GC = v101 (different glyph alphabet; EVA or- = v101 oy-, locus-verified 85%) · perms=20k, BH-FDR q=.05',
    12.5, MUT, 'middle')

T = R['WP2']['tests']
cats = ['minor', 'moderate', 'dominant']
schemes = [('B0_ZL', GOLD, 'ZL (baseline)'), ('R12_IT', BLUE, 'IT Takahashi'), ('R34_GC', PURP, 'GC v101 (oy-)')]

# ---------- left: replication panel ----------
LX, LY, LW, LH = 55, 105, 640, 560
S.append(f'<rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" fill="{PANEL}" rx="8"/>')
txt(LX + LW/2, LY - 10, 'or- share vs drawn root prominence — three transliterations', 16, INK, 'middle', 'bold')
ymax = 0.026
px0, py0, pw, ph = LX + 70, LY + 40, LW - 100, LH - 150
for v in [0, 0.005, 0.010, 0.015, 0.020, 0.025]:
    yy = py0 + ph - v / ymax * ph
    S.append(f'<line x1="{px0}" y1="{yy}" x2="{px0+pw}" y2="{yy}" stroke="{GRID}"/>')
    txt(px0 - 8, yy + 4, f'{v:.3f}', 11, MUT, 'end')
bw = 42
for i, c in enumerate(cats):
    xc = px0 + (i + 0.5) * pw / 3
    for k, (tag, col, lab) in enumerate(schemes):
        m = T[tag + '_means'].get(c, {})
        v, n = m.get('mean_or_share', 0), m.get('n', 0)
        x = xc - 1.5 * bw - 8 + k * (bw + 8)
        hh = v / ymax * ph
        S.append(f'<rect x="{x}" y="{py0+ph-hh}" width="{bw}" height="{hh}" fill="{col}" opacity="0.85" rx="3"/>')
        txt(x + bw/2, py0 + ph - hh - 6, f'{v:.4f}', 10, col, 'middle')
    txt(xc, py0 + ph + 20, f'{c} (n={T["B0_ZL_means"][c]["n"]})', 13.5, INK, 'middle')
for k, (tag, col, lab) in enumerate(schemes):
    S.append(f'<rect x="{px0+8}" y="{py0+6+k*24}" width="15" height="15" fill="{col}" rx="3"/>')
    txt(px0 + 30, py0 + 18 + k * 24, lab, 12.5, INK)
pIT_a, pIT_1 = T['R12_IT_all_sxq']['p'], T['R12_IT_scribe1_q']['p']
pGC_a, pGC_1 = T['R34_GC_all_sxq']['p'], T['R34_GC_scribe1_q']['p']
txt(LX + LW/2, LY + LH - 60, f'IT: p={pIT_a:.4f} (scribe×quire strata) · p={pIT_1:.4f} within Scribe 1 — FDR ✓✓', 13, GREEN, 'middle')
txt(LX + LW/2, LY + LH - 38, f'GC v101: p={pGC_a:.4f} · p={pGC_1:.4f} within Scribe 1 — FDR ✓✓', 13, GREEN, 'middle')
txt(LX + LW/2, LY + LH - 16, 'not a transliteration artifact: monotone in all three schemes', 13, GOLD, 'middle', 'bold')

# ---------- middle: slot-aware ----------
MX, MY, MW, MH = 730, 105, 380, 560
S.append(f'<rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" fill="{PANEL}" rx="8"/>')
txt(MX + MW/2, MY - 10, 'slot-aware: line-medial tokens only', 16, INK, 'middle', 'bold')
txt(MX + MW/2, MY + 22, 'Scribe 1, quire-stratified (first+last token of every line removed)', 11.5, MUT, 'middle')
sm = R['SLOT']['medial_means']
ymax2 = 0.018
qx0, qy0, qw, qh = MX + 62, MY + 50, MW - 92, MH - 160
for v in [0, 0.005, 0.010, 0.015]:
    yy = qy0 + qh - v / ymax2 * qh
    S.append(f'<line x1="{qx0}" y1="{yy}" x2="{qx0+qw}" y2="{yy}" stroke="{GRID}"/>')
    txt(qx0 - 8, yy + 4, f'{v:.3f}', 11, MUT, 'end')
for i, c in enumerate(cats):
    m = sm.get(c, {})
    v, n = m.get('mean', 0), m.get('n', 0)
    x = qx0 + (i + 0.5) * qw / 3 - 30
    hh = v / ymax2 * qh
    S.append(f'<rect x="{x}" y="{qy0+qh-hh}" width="60" height="{hh}" fill="{GREEN}" opacity="0.85" rx="3"/>')
    txt(x + 30, qy0 + qh - hh - 7, f'{v:.4f}', 11, GREEN, 'middle')
    txt(x + 30, qy0 + qh + 18, c, 12.5, INK, 'middle')
    txt(x + 30, qy0 + qh + 34, f'n={n}', 11, MUT, 'middle')
pS1 = R['SLOT']['S1_medial_or_scribe1_q']['p']
txt(MX + MW/2, MY + MH - 46, f'H=8.7, p={pS1:.4f} — FDR ✓', 14, GREEN, 'middle', 'bold')
txt(MX + MW/2, MY + MH - 22, 'the link is not a line-edge/ornament artifact', 12.5, GOLD, 'middle')

# ---------- right: decoupling ----------
RX, RY, RW, RH = 1145, 105, 370, 560
S.append(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" fill="{PANEL}" rx="8"/>')
txt(RX + RW/2, RY - 10, 'cross-section decoupling: null', 16, INK, 'middle', 'bold')
txt(RX + RW/2, RY + 22, 'mean or- share (ZL) where scribe / dialect separate', 11.5, MUT, 'middle')
D1 = R['WP3']['D1_scribe3_AvsB_sectstrat']; D2 = R['WP3']['D2_withinB_scribe_sectstrat']
rows = [
    ('Scribe 3 · Currier A (f58)', D1['mean_or_A'], D1['n_A'], RED),
    ('Scribe 3 · Currier B', D1['mean_or_B'], D1['n_B'], RED),
    ('Scribe 2 · within B', D2['per_scribe']['2']['mean_or'], D2['per_scribe']['2']['n'], BLUE),
    ('Scribe 3 · within B', D2['per_scribe']['3']['mean_or'], D2['per_scribe']['3']['n'], BLUE),
    ('Scribe 5 · within B', D2['per_scribe']['5']['mean_or'], D2['per_scribe']['5']['n'], BLUE),
]
bx0, by0, bwid = RX + 30, RY + 60, RW - 120
xmax = 0.028
for i, (lab, v, n, col) in enumerate(rows):
    y = by0 + i * 74
    txt(bx0, y - 6, f'{lab}  (n={n})', 12.5, INK)
    wpx = v / xmax * bwid
    S.append(f'<rect x="{bx0}" y="{y}" width="{wpx}" height="26" fill="{col}" opacity="0.8" rx="3"/>')
    txt(bx0 + wpx + 8, y + 18, f'{v:.4f}', 12, col)
txt(RX + RW/2, RY + RH - 88, f'D1 same scribe+section, dialect varies: p={D1["p"]:.2f}', 12.5, MUT, 'middle')
txt(RX + RW/2, RY + RH - 66, f'(A folios sit HIGH — against pure dialect-driving, but nA=2)', 12, MUT, 'middle')
txt(RX + RW/2, RY + RH - 44, f'D2 same dialect, scribe varies: p={D2["p"]:.2f}', 12.5, MUT, 'middle')
txt(RX + RW/2, RY + RH - 18, 'decisive test remains underpowered — 2 folios carry it', 12.5, RED, 'middle')

txt(W/2, H - 40, 'Confirmatory family (7 tests): R1–R4 + S1 survive BH-FDR; D1, D2 null. Second annotator: 20/164 folios banked pre-crash (partial ρ=0.21, n=12) — completion deferred, host RAM under test.',
    13, INK, 'middle')
txt(W/2, H - 16, 'phase9_results.json · run_phase9.py (preregistered docstring) · 2026-09-17 🜂', 11.5, MUT, 'middle')

S.append('</svg>')
svg = '\n'.join(S)
open(os.path.join(HERE, 'phase9_chart.svg'), 'w').write(svg)
from cairosvg import svg2png
svg2png(bytestring=svg.encode(), write_to=os.path.join(HERE, 'phase9_chart.png'),
        output_width=1560, background_color=BG)
print('chart written')
