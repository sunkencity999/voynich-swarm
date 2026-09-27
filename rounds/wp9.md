# WP9 / WP9-A — The semantics round: blind visual annotation × or-opening structure

*Builder: Cherubesque (seeds 991001–991007). Adversary: Smaug (design-review SLATE R-1..R-20
before freeze; full independent recompute after — own κ code, own permutation p, own
seeded-draw reimplementation). DESIGN frozen 2026-09-26 (v1.0) before execution; all
stage boundaries git facts.*

## Design intent

Every prior round tested *structure*. WP9 was the campaign's first *semantics* test —
the only identified discharge path for B1 (or-token folio-opening enrichment): if
or-openings function as content labels, pages whose first line contains an or-token
should share blind-annotated **visual** content within section×Currier cells, beyond
what negative pages share.

The design survived a full adversarial review before freeze (20 binding rulings). The
review killed the draft's primary unit at census — exact first-token grouping is
DOMAIN-DEAD (5 groups ≥2, 11/171 eligible pages) — and replaced it with the binary
or-contrast in four cells (H-A, H-B, B-B, S-B). It also named the attack the draft
missed: **memorization**. Vision models have seen the Voynich in training; masking the
text does not blind a model that recognizes the folio. Defenses: a residual-ink leakage
probe (P1), a legibility QA (P2), a disclosed folio-recognition audit (P3), objective
countable-only axes, two annotators from distinct model families, and a third-family
image-groundedness verification with a hard bar (≥27/30) — ANNOTATION-FAILED on breach.

## Master verdict: **ANNOTATION-FAILED at the verification gate — instrument failure, terminal (adversary-confirmed, no overturns)**

| Stage | Outcome |
|---|---|
| Power sketch (frozen effect, 1,000 sims) | 0.961 ≥ 0.80 |
| Scan hash re-verification | PASS — 213/213 SHA256 |
| Masking v1 → probes r0 | P1 pass (p=.687), **P2 FAIL** (10/25 tiles legible), P3 recognition 2.9% |
| One preregistered revision (v2.1) | median masked fraction .777; 22/171 pages >90% masked excluded; post-masking domain 14 pos pages / 27 usable pairs (floors ≥8 / ≥12 — met) |
| Probes r1 | P1 pass **thinly** (p=.0555 builder / .0570 adversary vs bar ≥.05), P2 pass (1/25), P3 recognition 0.6% |
| Annotator A (Anthropic family, 151 blind presentations) | intra-rater 9/10 (but 7/10 duplicates vacuous — zero shared definite axes) |
| Annotator B (local Qwen family, 151) | intra-rater 10/10 (5/10 vacuous) |
| κ agreement gate | PASS — survivors: herbal h1/h3/h4, stars s1; no κ-paradox escape used |
| **Verification sample (third family, 30 seeded cells)** | **FAIL — 17/30 verified (11 "unclear", 2 "no") vs bar ≥27/30** |
| Token join / statistic | **never ran** — no commit joins token and annotation data; permutation and bootstrap seeds never consumed |

## Finding 1 — agreement without groundedness is exactly the mirage the gate exists to catch

Two distinct-family annotators cleared the κ bar on four axes, and then a third family
checking their claims against the images could confirm only 17 of 30 sampled cells.
Without the verification gate, the round would have "passed" its reliability gates on
annotations that were substantially not image-verifiable. The dominant failure mode was
not contradiction but **"unclear" (11/30)** — the verifier could not find the claimed
feature in the annotatable substrate at all.

## Finding 2 — the masking dilemma (binding method constraint)

Dilation-based masking of a binarized ink mask cannot simultaneously pass the
text-leakage gates and leave annotatable drawing substrate. The v1 render leaked
legible text (P2: 10/25); the minimal fix that passed the probes masked a median .777
of each page and pushed 22 pages over the 90% exclusion line. Passing the leakage test
destroyed the thing being annotated. **Revival of U1 requires stroke-level
text/drawing separation** (human-drawn outlines or a trained segmenter) — preregistered
as a prerequisite for any successor round.

## Finding 3 — what the exit means for B1

The semantic reading of B1 (or-opening as content label) is **UNTESTED — not killed,
not supported**. B1's structural finding (positional or-enrichment) is untouched.
Exact per-type grouping remains DOMAIN-FAILED at census. The round is a
process-certified negative about the *instrument*, not about the manuscript.

## Adversary round (WP9-A)

Ruling: **CONFIRMED** — clean instrument-failure exit, no taint. All 13 commits in
preregistered order; the semantic git-fact boundary held (no token+annotation
co-occurrence anywhere in the chain); unconsumed seed streams verified. The adversary's
from-scratch reimplementation of the seeded verification draw reproduced the committed
30-cell sample exactly — cherry-picking impossible. Independent recount: 17/30. κ table
reproduced on all 10 axes; P1 recomputed at .0570; the disclosed v2.0 intermediate
render was ruled a legitimate unprobed discard (zero probe artifacts between renders;
discarded on its own render stats, disclosed in the revision commit), so the
one-revision budget was respected. Fabrication screen clean: annotator payloads
contained no folio identifiers; 0/302 raw responses mention any folio; annotator B
never read A's file. Erratum **E-1** (self-disfavoring direction): the post-masking
positive domain was 14 pages, not the published 13; 27 pairs correct.

Five deviations logged, all ruled benign. Campaign law adopted (AM-1..AM-5): the
erratum; vacuous duplicates are unscored henceforth (≥5 informative duplicates or the
intra-rater gate is inconclusive); a revision counts against its budget the moment any
gate consumes its tiles; thin-margin caveats travel with any reuse of the method;
probe deployments must be logged in a commit preceding the first probe artifact.

## Evidence

Round artifacts (private tree, hashes and commit chain quoted in the reports):
`voynich-swarm-wp9/SUMMARY.md`, `BUILD_LOG.md`, `infra/verify_sample_results.json`,
`infra/power_sketch.json`, `design-review/SLATE.md`, `design-review/domain_census.json`,
`ADVERSARY_REPORT.md`. Ledger entry: [CONSTRAINTS.md](../CONSTRAINTS.md).
