# W3b / W3b-A — Memory-bearing nulls, part 2: the residue showdown at the certified corridor

*Builder: Cherubesque (round SEED 20261001; nperm = B = K = 1000, m = 20; 5
certification draws per grid point). Adversary: Smaug (disjoint seed 777004; full
288-point-mean certification replay at builder seeds + own-seed grid, all 12 scored
units replayed at own seeds, d=2 cluster attack at three grains, off-grid memory-heavy
probe). DESIGN frozen 2026-09-29 before any test code; obligatory round under AM-W3-1.
W3's generator code imported genuinely unchanged (adversary-verified: no commits after
W3's pre-run commit, clean worktree).*

## Design intent

W3-A left one question standing, and made answering it obligatory: the
**recency-to-uniform copy+mutate family** (W3's committed SC generator — the Timm &
Schinner "self-citation" lineage; the honest name is used because at the certified
large-τ corridor the copy kernel is quasi-uniform, i.e. frequency-preferential copying,
not recency-weighted self-citation proper) CAN be tuned to the manuscript's
unigram/word-structure surface. Does it then reproduce the certified residue structure?
W3b froze a 144-point corridor grid (τ up to 24000, p_cont ≤ 0.3), certified it,
selected configurations by frozen rule, and scored three preregistered cells — S_b
(boundary digram-class MI), S_w (within-word positional residue), S_d2 (d=2
boundary-class MI, promoted from Smaug's W3-A lead) — against K = 1000 generated
corpora per configuration, in both transliterations, with hard-only (AM-W2-1) and
GLYPH recomputes. T1 separately ran the first preregistered, cluster-bootstrapped
certification of the d=1 and d=2 residues on the real corpus.

## Master verdict: **FAMILY-FAILS-AT-RESIDUE (adversary: CONFIRMED-WITH-AMENDMENTS, AM-W3b-1..3) — headline carried by S_b and S_w ONLY**

The certified family — tuned fairly to certification at the corridor its own adversary
found — **does not reproduce the certified residue structure**: at both selected
certified configurations, in both transliterations, all 12 scored units are MISMATCH
with **n_ge = 0 against K = 1000 generated corpora** (p_two = 2/1001 everywhere; the
observation sits above ALL 1000 generated values in every unit). The adversary
reproduced n_ge = 0 in every unit at his own seeds (K = 500), verified the obs
statistics two independent ways to 0.0, and regenerated draws across the crash-resume
boundary bit-exactly.

**Per AM-W3b-1, the citable failure rests on S_b and S_w only** (see amendments):

| cell | obs ZL / IT | generator band (both configs, 2.5–97.5%) | verdict |
|---|---|---|---|
| S_b | **0.19992 / 0.17836** | 0.0052–0.0132 | MISMATCH — obs CIs ≥ 14× above gen bands even at basic (bias-corrected) CIs; ~8–20× across probed configs |
| S_w | **1.39542 / 1.36418** | 0.874–1.184 | MISMATCH — survives bias correction by huge margins |
| S_d2 | 0.01675 / 0.01631 | 0.0046–0.0093 | MISMATCH as frozen-rule outcome, **not independently citable** (AM-W3b-1) |

AM-W2-1 travels: ZL S_b = 0.1999 pooled / **0.1712 hard-space-only** (IT comma-free at
source, 0.1784/0.1789); hard-only and GLYPH recomputes agree in every unit, no
downgrades.

Not "cannot be tuned" (W3's struck overclaim) — it CAN be tuned; tuned, **it fails to
reproduce the certified sequential structure**.

## The corridor is real — four independent seed sets

Certification stage: **15/144 grid points certify jointly** at builder seeds
(τ ∈ {8000: 2, 12000: 4, 16000: 4, 24000: 5}, p_exact 0.60–0.70; ZL 32 / IT 38
singles), confirming Smaug's W3-A adversary-seed corridor (8/144) — and Smaug's W3b-A
own-seed grid gives 13/144 joint on the same τ ≥ 6000 corridor. With W3-A's discovery
scan that is four independent seed sets; the adversary's replay of all 288 point-means
at builder seeds is float-exact (max deviation 0.0). Selected by frozen rule:
**SC-fit = SC-freq = (τ=24000, p_exact=0.675, p2=0.2, p_cont=0)**;
**SC-mem = (12000, 0.675, 0.2, 0.3)** — the adversary's independent recompute of the
selection rule returns exactly these.

## What the family DOES reproduce (descriptive, never scored)

ρ_near (near-repeat rate): obs 0.0486/0.0457 sits INSIDE the generator band
([0.012, 0.087] / [0.012, 0.079] at SC-fit) — copy+mutate produces Voynichese's
repetition texture. Generator S_far and S_d1 sit at the bias floor vs obs 0.0125/0.0101
and 0.170/0.152. **The failure is specific: the family makes the repeats but not the
digram-class residue — memory of the wrong shape.**

## T1 — d-profile certification on the real corpus

- **d=1: PASS — A10 re-certified at a third builder seed set** (fourth counting the
  adversary): obs 0.16998/0.15244, n_ge = 0 both translits, folio-cluster CI
  [+0.164, +0.194] ZL / [+0.148, +0.179] IT, P(≤0) = 0.
- **d=2: MIXED** — permutation-clear (n_ge = 0, obs 0.0038/0.0042 ABOVE the null max in
  both translits; now replicated at FOUR seed sets) but the folio-cluster bootstrap
  fails to certify (CIs ∋ 0: ZL P(≤0) = .064, IT .191). A lead, not a claim. AM-W3b-3
  knife-edge disclosure travels: at folio grain the ZL CI is seed-knife-edge (adversary
  seeds exclude 0 at P(≤0) = .024); non-certification is carried by IT and by coarser
  grains (section/quire P(≤0) ≥ .085 both translits).
- d ≥ 4 at the bias floor; the ZL-only weak far tails (d=8/d=16) remain a
  bootstrap-refuted watch item. AM-W3-2 wording stands exactly.

## The adversary's two kill vectors that drew blood (→ amendments)

**AM-W3b-1 — S_d2 de-weighted.** Three independent reasons the S_d2 cell is not
independently citable: (a) d=2 is cluster-uncertified on the real corpus (the DESIGN's
own interpretive gate anticipated this); (b) its CI-disjointness leg is a
bootstrap-bias artifact — the folio-resampled percentile bootstrap of MI is upward
biased, and under the basic (reflected) bootstrap the S_d2 CI overlaps the generator
band in all four units (S_b and S_w disjointness survives bias correction by huge
margins); (c) the adversary found a **certified off-grid memory-heavy corner of the
same family** — p_cont = 0.7, outside the frozen grid's 0.3 cap — that reproduces
obs-magnitude S_d2 (gen max 0.0173, n_ge = 4/60). Every published statement of the W3b
result carries the headline on **S_b and S_w only**; future MI cluster bootstraps must
report bias and a basic-bootstrap sensitivity line whenever a CI leg gates a verdict.

**AM-W3b-2 — tuning-scope disclosure.** "Under fair tuning as implemented here" means
the frozen 144-point grid (p_cont ≤ 0.3); the certified family extends to p_cont ≥ 0.5
(adversary-verified joint certification at 6 points up to 0.7). Crucially, at that
memory-heaviest certified corner **S_b and S_w still fail by adversary probe**
(n_ge = 0/60 per translit at (24000, .675, .2, .7); S_b gen mean 0.026 vs obs
0.20/0.18) — so this is a disclosure, not a reopening obligation; no W3c mandated.
Claims beyond the probed region are unsupported until run.

## What this means (exact certified scope — ledger entry A12)

With W3's frozen-grid result and W3-A's corridor proof, the full picture: **the family
certifies on the unigram/word-structure surface across a τ ≥ 6000 corridor (four
independent seed sets) and everywhere tested under certification it fails the certified
residue cells S_b (~8–20×) and S_w — including at the memory-heaviest certified corner
probed.** AM-W3-1's obligation is discharged; W3 + W3b together are citable against
this family at the residue layer, in this operator-set implementation. The strongest
surviving "sophisticated gibberish" account now joins the memoryless family (A11) on
the excluded list — at the residue layer, under amended wording.

NOT certified: cipher, language, meaning. NOT excluded: mutation operator sets that
preserve boundary-digram statistics by construction; T&S's exact (paywalled) line-based
algorithm; the region beyond p_cont = 0.7. A10/A11 unamended (A10 re-certified here).

## Evidence

Round artifacts (private tree): `voynich-swarm-w3b/DESIGN.md` (frozen pre-run, with
committed ceilings code per AM-W2-3), `BUILD_LOG.md` (crash-resume proof §4:
gen_SC-mem.IT killed at 100/1000, resumed, cmp bit-identical),
`tests/results/{summary.md, T1.json, T2.json}`, `infra/gen_cert.json`, dumps
`infra/token_derived.{ZL,IT}.jsonl`, `ADVERSARY_REPORT.md` +
`adversary/adv_w3b.py` + `adv_w3b_{AB,DE,FGH}.json`.
Ledger entries: A12, B13, AM-W3b-1..3 in [CONSTRAINTS.md](../CONSTRAINTS.md).
