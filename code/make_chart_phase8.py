#!/usr/bin/env python3
"""Phase 8 chart: (left) or- share by drawn root prominence, pooled vs scribe-1;
(right) the control ladder — the survivor's p under successive covariate
controls. Hand-built SVG -> cairosvg PNG, dark-parchment theme."""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'phase8_results.json')))

BG, PANEL, INK = '#211b12', '#2b2418', '#e8dcc0'
GOLD, GRID, MUT = '#e0b23c', '#3a3020', '#6e5f45'
GREEN, RED, BLUE = '#7fbf5f', '#d96a5f', '#63c7c9'

W, H = 1500, 760
S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="{BG}"/>']

def txt(x, y, s, size=15, fill=INK, anchor='start', weight='normal', style=''):
    S.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" '
             f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" {style}>{s}</text>')

txt(W/2, 42, 'Voynich phase 8 — does the drawing–text link survive scribe and quire control?',
    22, GOLD, 'middle', 'bold')
txt(W/2, 68, 'covariates: quire + Lisa Fagin Davis scribes (ZL3b-n IVTFF $Q/$H); scribe = dialect in the herbal section, so quire is the sharpest independent control',
    13, MUT, 'middle')

# ---------- left panel: or- share by root prominence ----------
LX, LY, LW, LH = 70, 110, 620, 520
S.append(f'<rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" fill="{PANEL}" rx="8"/>')
txt(LX + LW/2, LY - 12, 'or- token share vs drawn root prominence', 16, INK, 'middle', 'bold')

pooled = R['or_share_by_rootprom']; s1 = R['or_share_by_rootprom_scribe1']
cats = ['minor', 'moderate', 'dominant']
ymax = 0.026
px0, py0, pw, ph = LX + 70, LY + 40, LW - 110, LH - 120
# gridlines
for v in [0, 0.005, 0.010, 0.015, 0.020, 0.025]:
    yy = py0 + ph - v / ymax * ph
    S.append(f'<line x1="{px0}" y1="{yy}" x2="{px0+pw}" y2="{yy}" stroke="{GRID}" stroke-width="1"/>')
    txt(px0 - 10, yy + 5, f'{v:.3f}', 12, MUT, 'end')
bw = 44
for i, c in enumerate(cats):
    xc = px0 + (i + 0.5) * pw / len(cats)
    for k, (src, col, lab) in enumerate([(pooled, GOLD, 'all'), (s1, BLUE, 's1')]):
        v = src.get(c, {}).get('mean_or_share', 0)
        n = src.get(c, {}).get('n', 0)
        x = xc - bw - 6 + k * (bw + 12)
        hh = v / ymax * ph
        S.append(f'<rect x="{x}" y="{py0+ph-hh}" width="{bw}" height="{hh}" fill="{col}" opacity="0.85" rx="3"/>')
        txt(x + bw/2, py0 + ph - hh - 8, f'{v:.4f}', 11.5, col, 'middle')
        txt(x + bw/2, py0 + ph + 38, f'n={n}', 11.5, MUT, 'middle')
    txt(xc, py0 + ph + 20, c, 14, INK, 'middle')
# legend
S.append(f'<rect x="{px0+8}" y="{py0+6}" width="16" height="16" fill="{GOLD}" rx="3"/>')
txt(px0 + 32, py0 + 19, 'all 129 folios', 13, INK)
S.append(f'<rect x="{px0+8}" y="{py0+32}" width="16" height="16" fill="{BLUE}" rx="3"/>')
txt(px0 + 32, py0 + 45, 'Scribe 1 / Currier A only (n=95)', 13, INK)
txt(LX + LW/2, LY + LH - 14,
    'monotone in both: the gradient is not a between-scribe artifact', 13, GREEN, 'middle')

# ---------- right panel: control ladder ----------
RX, RY, RW, RH = 750, 110, 690, 520
S.append(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" fill="{PANEL}" rx="8"/>')
txt(RX + RW/2, RY - 12, 'the survivor under successive controls  (−log₁₀ p, permutation)', 16, INK, 'middle', 'bold')

conf = R['confirmatory']
ladder = [
    ('pooled (phase 7, 50k perms)', 8.1e-5, GOLD),
    ('| Currier dialect (phase 7)', 1.0e-3, GOLD),
    ('| scribe  (C5)', conf['C5_or_vs_rootprom_given_scribe']['p'], GREEN),
    ('| quire  (C6)', conf['C6_or_vs_rootprom_given_quire']['p'], GREEN),
    ('| scribe × quire  (C7)', conf['C7_or_vs_rootprom_given_scribe_x_quire']['p'], GREEN),
    ('within Scribe 1 | quire  (C8)', conf['C8_or_vs_rootprom_scribe1_given_quire']['p'], GREEN),
    ('drawing→dialect | quire  (C1)', conf['C1_dialect_vs_rootprom_given_quire']['p'], BLUE),
]
bx0, by0, bwd, bht = RX + 300, RY + 50, RW - 340, 44
xmax = 4.5
for v, lab in [(1.30103, 'p=0.05'), (3, 'p=0.001')]:
    xx = bx0 + v / xmax * bwd
    S.append(f'<line x1="{xx}" y1="{by0-14}" x2="{xx}" y2="{by0+len(ladder)*(bht+14)}" '
             f'stroke="{MUT}" stroke-width="1.4" stroke-dasharray="5,4"/>')
    txt(xx, by0 - 20, lab, 12, MUT, 'middle')
for i, (lab, p, col) in enumerate(ladder):
    y = by0 + i * (bht + 14)
    v = -math.log10(p)
    wpx = min(v, xmax) / xmax * bwd
    txt(bx0 - 12, y + bht/2 + 5, lab, 13.5, INK, 'end')
    S.append(f'<rect x="{bx0}" y="{y}" width="{wpx}" height="{bht}" fill="{col}" opacity="0.85" rx="4"/>')
    txt(bx0 + wpx + 10, y + bht/2 + 5, f'p={p:.1e}', 13, col)
txt(RX + RW/2, RY + RH - 40,
    'scribe control of the dialect link itself is structurally impossible:', 13, RED, 'middle')
txt(RX + RW/2, RY + RH - 20,
    'in the herbal section, scribe ⇄ dialect are the same partition (A=Scribe 1; B=Scribes 2/3/5)', 13, RED, 'middle')

txt(70, H - 60, f"green = phase-8 confirmatory tests surviving BH-FDR q=0.05 (5 of 7). Not significant: scribes within B do not differ "
    f"in root prominence (p={conf['C3_scribe_vs_rootprom_within_B']['p']:.2f}); quires within Scribe 1 do not differ (p={conf['C4_quire_vs_rootprom_within_scribe1']['p']:.2f}).", 13, MUT)
txt(70, H - 38, 'exploratory: no FDR survivor within a single scribe (Scribe 1: 333 quire-stratified tests, min p=0.0041; Scribe 2: n=20, power at α=0.05 only 0.26).', 13, MUT)
txt(70, H - 16, 'run_phase8.py · 20k permutations per confirmatory test · preregistered test list · 2026-09-16', 12, GRID.replace('#3a3020', '#5a4c34'))

S.append('</svg>')
svg = '\n'.join(S)
open(os.path.join(HERE, 'phase8_chart.svg'), 'w').write(svg)
from cairosvg import svg2png
svg2png(bytestring=svg.encode(), write_to=os.path.join(HERE, 'phase8_chart.png'),
        output_width=W, background_color=BG)
print('saved phase8_chart.png')
