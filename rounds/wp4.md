# WP4 / WP4-A — Notation-Family Mechanisms (L3 slate, N1–N4)

*Builder round 2026-09-23; adversary round same day. Inputs inherited frozen from WP2
(38,440 ZL / 37,759 IT tokens); nperm=1000, seed 20260923, crash-resume verified
bit-identical. New certification machinery this round: folio-cluster nulls and knife-edge
disclosure.*

## Design intent

Lucen's L3 slate, built on WP3's process-side placement: N1 notational abbreviation
(specialist hands), N2 folio-reference / indexing, N3 visual buffer / separator,
N4 quantitative / inventory tagging. Battery T1–T6, both transliterations.

## Master verdict

**No mechanism achieved SUPPORTED.**

- **N1 notational abbreviation — prereg letter MIXED; robustness DISFAVORED.** T1
  between-scribe variance passes raw (p=.001 both), but the effect evaporates under
  section × Currier stratification (PH1: p=.148/.121) — the "scribe" effect is not
  separable from the long-known Currier A/B division.
- **N2 folio-reference — MIXED**, and the round's real discovery: or- is enriched in the
  boundary paragraphs of folios (T3a: +.0046/+.0039, p=.002/.002), and the NOT_PREREG split
  shows it is entirely the **FIRST paragraph** (p=.001/.001; last-paragraph ns) — an opening
  stamp, not a closing one. But T3b shows no quire-boundary signal at all: the signal lives
  at page level, not codex-structure level.
- **N3 visual buffer — MIXED by letter, substantively weak.** Local-entropy dip is a dead
  null; the sole pass (T5 cross-translit repertoire stability, JSD .0457) sits at exact
  p = .04995 — a knife-edge — and the per-family breakdown shows the `ai` family is equally
  stable: nothing distinctively separator-like survived.
- **N4 inventory tagging — DISFAVORED.** Carried kill from WP3 (or--stems are free
  vocabulary, contradicting a closed shorthand inventory); its one live prong (T6 register
  contrast) reproduces WP2's raw shares exactly (bare-or share 77.1% H vs 55.4% P, ZL) but
  is **non-certifiable at folio-cluster level** (see adversary amendment).

## Adversary outcome (WP4-A)

Full independent recompute from primary dumps: **every builder number matched exactly; no
discrepancy anywhere.** Adjudications beyond confirmation:

- **T5 knife-edge dissected:** 49/1000 nulls strictly below observed, nearest 1.5e-05 away —
  a seed-level coin flip. Passes by prereg letter; ruled *not load-bearing evidence*.
  Repertoire stability: unproven-but-not-refuted.
- **T6 retitled non-certifiable** (amendment adopted into the builder summary): a faithful
  re-implementation lands IT at p=.047 (a pass) vs the builder seed's .055; across
  defensible null choices T6 ranges .008–.088 at 15–16 P-folio clusters. It cannot certify
  fail OR pass. N4's DISFAVORED verdict stands on the carried kill + non-certifiability.
- **PH1 caveat the builder undersold:** Currier stratification also shrinks the domain
  ~60% (171→67 folios) — correct reading is "cannot be separated from Currier," not
  "shown artifactual."
- **PH3 direction note:** the surviving N2 prong points at *openings*, not closings —
  an incipit/header geometry, cutting against the end-stamp flavor of N2 as slated.
- Campaign design rules adopted: Currier A/B is a mandatory stratum in any future
  scribe/hand test; repertoire-stability tests need a larger control pool.

## Key numbers

| Result | ZL | IT |
|---|---|---|
| T3a boundary-paragraph enrichment | +.0046, p=.002 | +.0039, p=.002 |
| PH3 first-paragraph split | p=.001 | p=.001 |
| PH3 last-paragraph split | p=.144 | p=.201 |
| T3b quire-boundary signal | none (p=.775) | none (p=.853) |
| T1 scribe variance raw / Currier-stratified | p=.001 / .148 | p=.001 / .121 |
| T5 repertoire JSD | .0457, exact p=.04995 (knife-edge) | — |
| T6 bare-or share H vs P (raw, exact) | 77.1% vs 55.4% | 76.2% vs 49.3% |
| T6 clustered contrast (range over defensible nulls) | .088 | .055 (.008–.088) |

## Handoff

The live thread after WP4: the **opening-boundary geometry** — the only signal in the L3
slate that is both strong (p=.001 both transliterations) and unexplained. WP5 was
commissioned to test it preregistered, with proper strata.
