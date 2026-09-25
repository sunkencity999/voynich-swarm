# WP7 / WP7-A — L5-M3 geometry + first-line variety cross-link

*Builder round 2026-09-25 (seeds 666001/666002, nperm=10000, B=5000, crash-resume verified
bit-identical); adversary round (Smaug) same day (independent seeds 777001/777002,
B=10000, own domain build straight from frozen WP2 tables). Inputs inherited frozen from
WP2/WP5; nothing regenerated.*

## Design intent

Test the two L5 lanes left standing after WP6 killed M1:

- **H-A (T7a/b/c):** L5-M3 — page-initial or- as a *placed* folio-boundary/collation mark.
  Preregistered measurand: first-token start-x offset of page-initial or- lines vs
  frequency-matched control-class lines, with position-specificity (lines 2–4 null) and a
  predicted balneo null. Kill: folio-cluster boot CI ∋ 0 on both arms.
- **H-B (T7B):** convert WP6-A's NOT_PREREG "first lines favor lexical variety" lead into
  certifiable evidence via a NEW independent prediction: per-section first-line diversity
  elevation must co-vary POSITIVELY with the certified A7 or- opening enrichment across
  sections (Spearman ρ, section-cluster bootstrap + label permutation). Explicit HARKing
  guard: the descriptive leg itself can never certify from this design.

## Master verdicts (adversary-adjudicated)

| Arm | Verdict |
|---|---|
| **H-A** (L5-M3 geometry) | **NO VERDICT — NON-RUNNABLE**, adversary-confirmed as the correct honest call |
| **H-B** (variety cross-link) | **KILLED, prereg-clean** — adversary-confirmed under independent code and seeds |

## H-A: the finding is about the inputs

The preregistered measurand exists in **no frozen input**: the WP2 token tables carry no
horizontal-geometry field (0/17 candidate names, both transliterations); WP5 annotations
are heading-likeness only (line counts/lengths); image annotations are motif flags; and
both IVTFF sources are single-column aligned — every text locus starts at column 18, and
none of the `<->` gap markers (758 ZL / 875 IT) occur line-initial. The adversary
re-parsed both sources independently and confirmed the blocker in BOTH transliterations,
and verified no horizontal proxy was smuggled into any computed statistic.

The builder correctly refused to improvise an unblinded proxy mid-round (the WP5
blind-annotation bar forbids it). The defect traces to a contract-level input assumption
inherited from WP6's disposition note — not builder execution. **M3 is neither supported
nor killed**; its kill rule stays armed for a future blind start-x annotation round over
the folio images (natural companion to the U4 image round).

## H-B: killed with the wrong sign

| | Builder (666001/666002) | Adversary (777001/777002) |
|---|---|---|
| ρ_obs (ZL, k=4 sections) | −0.600 | −3/5 exactly (independent domain build, multiset-identical 7,375 rows) |
| exact enumeration p_ge | 20/24 = .8333 | 20/24 = .8333 (independent impl) |
| sampled p_ge (10k) | .832 | .825 |
| section-cluster boot CI95 | [−1.0, +1.0] (B=5000) | [−1.0, +1.0] (B=10000) |
| P(ρ≤0) | .882 | .888 |
| verdict | KILL | **KILL** |

Both preregistered kill conditions fire independently (wrong sign AND CI ∋ 0). The
anti-pattern is stark: balneo — the A7-*negative* section — shows the 2nd-largest
first-line diversity elevation (+0.378), while Stars (A7-positive) shows the smallest
(+0.113). Whatever drives first-line lexical variety, it is orthogonal-to-opposed to the
or- opening enrichment.

HARKing guard honored: the descriptive elevation replicated in every included section
(per-section p: B .0455, H .0001, P .0211, S .272) but stays NOT_PREREG — no verdict
consumes it. Power disclosure: k=4 sections ⇒ exact-p floor 1/24 ≈ .0417 (certifiable
only at ρ = 1.0); moot here given the wrong sign. IT replication gated off per design
(ZL fail).

## Adversary outcome

Fabrication screen **clean**: checkpoint per-draw seed reproduction bit-level exact
(draws regenerated from `SeedSequence((seed, i))` match the ckpt files); every reported
count, CI, and spot-check recomputes to the digit; A7 per-section effect values verified
against the WP5 source files. Zero major defects; two minor (a rounded-intermediate
statistic, immaterial at ~10⁴× margin; one unlogged-but-moot deviation), four notes.
No overturns.

## Campaign consequence

L5 now has **no live lane testable in the frozen text corpus**: M1 killed (WP6), M3
non-runnable on text, M2 untestable on text (U4 memo). The image/vision round — blind
start-x annotation + U4 exploratory page-image analysis — is the campaign's primary path
forward. "First lines favor lexical variety" survives only as an independent NOT_PREREG
mechanism question, now decoupled from the or- opening effect (C17).
