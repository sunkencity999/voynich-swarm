# W3c / W3c-A — Formal closure of the memory-heavy certified corner

*Builder: Cherubesque (round SEED 20261005; K = B = 1000, 5 certification draws per
grid point per AM-W2-2; DESIGN frozen 2026-09-29 23:35 PDT, test code committed
pre-run per AM-W4-5, certified-region map committed before the showdown ran;
crash-resume proven bit-identical across a SIGKILL at generator draw 100). Adversary:
Smaug (seed 777007; fabrication screen from git facts alone; all-76-unit checkpoint
recounts exact; builder-seed float replays 0.0 including the crash boundary; own-seed
full 300-point certification grid; own-seed showdown at K = 500; a 138-point
NOT_PREREG ceiling/edge probe that delivered on his pre-named target).*

## Design intent: paying off a debt

A12 — the exclusion of the recency-to-uniform copy+mutate family (the Timm & Schinner
"self-citation" lineage) at the residue layer — carried a known soft spot. W3b's frozen
grid capped the phrase-continuation parameter at p_cont ≤ 0.3; it was Smaug's W3b-A
spot probe that showed the certified family extends to p_cont = 0.7, and the ledger's
"fails at the residue layer everywhere it certifies" rested, for the memory-heavy
region, on that single adversary probe (6 points, n_ge = 0/60). W3c was the ordered
closure: a **preregistered 300-point sweep** of the memory-heavy region — τ ∈
{6000–24000} × p_exact ∈ {0.60–0.70} × p2 ∈ {0, 0.2} × **p_cont ∈ {0.4–0.9}** —
certify every point against the four frozen unigram/word-structure bars (5-draw means,
both transliterations), then score the certified residue cells S_b and S_w at every
jointly certified point against K = 1000 generated corpora per unit, with S_d2 carried
as a REQUIRED descriptive companion (never scored, per AM-W3b-1).

## Master verdict: **CORNER-CLOSED — adversary CONFIRMED-WITH-AMENDMENTS (AM-W3c-1..4); A12 gloss upgrade APPROVED-AS-AMENDED**

**38 of 300 grid points certify jointly** (ZL 71 / IT 82 single-translit passes),
spread over every τ and every p_cont level, p_exact 0.60–0.70 — and **every one of
them FAILS both certified residue cells, in both transliterations: n_ge = 0 against
K = 1000 generated corpora in all 76 point × translit units** (p_two = 2/1001
everywhere; no marginal flags; no hard-only or GLYPH downgrades; obs basic-bootstrap
CI disjoint from every generator band). Key numbers (verified against the committed
JSONs):

| | obs ZL / IT | worst generator band across all 38 pts (2.5–97.5%) | closest approach |
|---|---|---|---|
| S_b | 0.19992 / 0.17835 | up to [0.042, 0.110] (at p_cont = 0.9) | gap 0.0355 (IT, gi 149), n_ge = 0 |
| S_w | 1.39542 / 1.36418 | hi up to ≈ 1.19 | gap 0.0898 (IT, gi 205), n_ge = 0 |

AM-W2-1 companions carried: obs S_b hard-junction-only 0.1712 ZL / 0.1789 IT
(hard-only tails agree with pooled everywhere, n_ge = 0). Bootstrap gating used the
basic CI per AM-W3b-1, with percentile + BCa + bias lines filed (S_b bias
+0.0050/+0.0047, S_w +0.0137/+0.0140); Smaug verified that substituting the percentile
CI flips **zero** disjointness calls in all 76 scored cells.

The honest trend was flagged in the builder's own summary as "the obvious adversary
target": the generator's S_b **rises with memory** — band hi 0.016 at p_cont = 0.4 →
0.110 at 0.9, max single draw 0.148 — and the grid maximum p_cont = 0.9 was declared
**not bracketed above**.

## Smaug delivers on the pre-named target — and the closure holds anyway

The adversary's NOT_PREREG strip probe (90 points at τ {12k,16k,24k} × p_exact
{.60–.70} × p2 {0,.2} × p_cont {.92,.95,.98}, plus 48 p_exact edge points) found that
**certification does not stop at 0.9**: two points certify jointly above the grid —
(12000, .625, 0, .95) and (16000, .625, 0, .92) — with single-translit passes reaching
p_cont = 0.98. And at the 0.95 joint point, **individual S_b draws CROSS the
manuscript**: n_ge = 2/200 ZL (max draw 0.2089 ≥ obs 0.19992), 1/200 IT. The round's
"yet never reaches obs" sentence is therefore **STRUCK unless scoped to the grid**
(AM-W3c-1), and the ledger now says so.

What holds the closure is **S_w — the binding discriminator at extreme memory**. It is
essentially flat in memory: n_ge = 0/200 at every probed strip point, generator p97.5
≈ 1.11–1.12 vs obs 1.395/1.364 — a ~0.25-bit gap the family never bridges. The S_b
tail itself stays MISMATCH-level (p_two ≈ .03; obs basic CI [0.1784, 0.2097] disjoint
from the generator band). **No probed point survives.** The family buys the repeats,
buys d=2, and at absurd memory can even buy single S_b draws; it cannot buy the
within-word residue at any certifiable setting probed. Binding consequence: **S_b
alone may not be cited against this family above the sweep grid** — above p_cont = 0.9
the exclusion rests on S_w.

The upgraded A12 closure claim (adversary's binding wording): **"closed up to
p_cont = 0.9 by preregistered sweep, with adversary probes extending the S_b/S_w
failure through the certified strip to 0.95"** — not an unqualified "everywhere it
certifies", since certification demonstrably continues above the grid.

## The other amendments

- **Ceiling is seed-wobbly (AM-W3c-2).** Smaug's own-seed replay of the full 300-point
  grid yields 33 joint points with ceiling p_cont = 0.8 (overlap with the builder's 38:
  14 points). The memory-heavy REGION is now confirmed at a **fifth** independent seed
  set; the specific statistic "38 points / ceiling 0.9" is a builder-seed quantity
  (±0.1 at 5 draws/point). Cite the region qualitatively, never the count.
- **p_exact edges are occupied (AM-W3c-3).** Joint certifications sit at both edges of
  the frozen .60–.70 window at two seed sets, so the window does not bracket the
  corridor. Adversary escape probes beyond the edges — p_exact {.55, .575} at high
  τ/high p_cont and {.725, .75} at low τ — found **no joint certification** (2 singles
  at .575); the joint footprint stands as probed.
- **A13's weld STRENGTHENED (AM-W3c-4).** The S_d2 companion swept clean monotone
  structure along the memory axis, adversary-recounted at all 76 units and reproduced
  at his own seed: n_ge = 0 at p_cont ≤ 0.6, 23–61/1000 at 0.7, 832–880 at 0.8,
  999–1000 at 0.9 — the family **crosses obs d=2 magnitude at p_cont ≈ 0.7 and
  overshoots ~3.5× by 0.9** (and 200/200 in the adversary strip). The AM-W3b-2
  one-corner weld on W5's d=2 certification upgrades accordingly: d=2 residue is
  quantitatively non-discriminating along this family's memory axis — it constrains
  memoryless/short-memory mechanisms only.

## Audit record

Fabrication screen CLEAN from git facts alone: freeze (DESIGN only, no outcome
numbers) → pre-run code commit → certified-region map → results; DESIGN byte-identical
across the chain; all 76 generator checkpoints carry the declared seed/stream/offset,
verified programmatically. Builder-seed float replays: certification draws at 3 points
× both translits and generator showdown draws spanning the SIGKILL@100 crash-resume
boundary all reproduce at **max_abs_dev = 0.0**. Independent obs recompute (own
tabulation, own MI code, from W3b's committed dumps): dev ≤ 1.4e-16, pair counts exact
(ZL 33,241 / 37,988; IT 32,566 / 37,309). Own-seed showdown at 5 units, K = 500 —
including both p_cont = 0.9 closest-approach units — S_b and S_w n_ge = 0/500 in all
five. One operational deviation (the first cert-gate launch died with its shell before
any output existed; relaunched, draw-identical by determinism) audited and **CLEARED**
(F10). Smaug's close: *"The hoard is intact; the inscription on the door gains one
honest line."*

## What this means (exact certified scope)

The recency-to-uniform copy+mutate family — the strongest memory-bearing competitor
tested — is excluded at the residue layer across its entire certified memory-heavy
region, by preregistered sweep rather than spot probe, with the failure
adversary-extended through the certifying strip above the grid. NOT certified: cipher,
language, meaning. NOT exhausted: mutation operators preserving boundary-digram
statistics by construction; T&S's exact (paywalled) line-based algorithm; the region
beyond the scanned strip (p_cont > 0.98; p_exact outside [.55, .75] × the probed
sub-region); p_cont = 1.0 is degenerate (deterministic replay) and excluded by design.

## Evidence

Round artifacts (private tree): `voynich-swarm-w3c/DESIGN.md` (frozen contract),
`BUILD_LOG.md` (crash-resume proof §4, deviations §5), `infra/gen_cert.json`
(certified-region map), `tests/results/{T1.json, summary.md, T1_run.log,
T1_crash{1,2}.log}`, checkpoints `tests/ckpt/` (76 units × per-draw 13-measurand
vectors), `ADVERSARY_REPORT.md` + `adversary/battery.py` +
`adversary/{A_builder_seed_replay,B_obs_recompute,C_own_seed_cert_grid,
D_own_seed_showdown,E_ceiling_edge_probe}.json`.
Ledger entries: A12 gloss upgrade (approved-as-amended), AM-W3c-1..4, A13 weld
strengthening, live-thread-6 update in [CONSTRAINTS.md](../CONSTRAINTS.md).
