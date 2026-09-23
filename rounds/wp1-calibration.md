# WP1 (Phase 10) — Calibration Gauntlet

*2026-09-18. Charter §5 gate: the falsification machinery must be proven before it is
trusted on anything novel.*

## Design intent

Six machine-testable decipherment-claim dossiers plus a falsification harness. Five are real
published claims; one is a synthetic ringer of comparable surface plausibility, planted by
the orchestrator as a positive control. The adversary was not told which. Gate: **all six
must be correctly rejected.** If any survive, we fix the falsifier, not the manuscript.

The gauntlet: G1 Cheshire 2019 (proto-Romance) · G2 Gibbs 2017 (Latin abbreviation) ·
G3 Hauer & Kondrak 2016 (Hebrew anagram) · G4 Bax 2014 (partial plant names) ·
G5 Ardiç (Turkic) · G6 "Marchetti 2021" (medieval Occitan).

The harness battery, per claim × transliteration: (a) mapping-consistency against ≥1000
random same-structure mappings (the null enjoys the exact same alternative-latitude the
claim does), (b) out-of-sample generalization (flag < 0.8), (c) internal consistency against
the claimant's own showcased readings + reader-freedom accounting, (d) linguistic statistics
of the decoded corpus vs the claimed language. Steelman mode: where no complete key was
published, a bounded optimizer fits one on the claim's own folios, with identical-budget
fits on structure-destroyed corpora as the null.

## Outcome

**18/18 verdict files (6 claims × 2 transliterations, plus steelman runs): REJECTED.**
Gate passed; the falsifier is trusted.

## The ringer, unsealed

G6 "Marchetti (2021) medieval Occitan" does not exist. The dossier, narrative, and sign
table were constructed by the orchestrator by tuning an EVA-unit → grapheme mapping on
folios f1r–f6v (coordinate ascent against a 140k-lemma Occitan list, homophone cap 2,
seed 20260918). Tuning alone achieved ~54.6% train-folio attestation and ~44.6%
manuscript-wide — numbers that *look like* published "decipherment" support. The harness
correctly rejected it: attestation not above the same-latitude null, decoded statistics not
Occitan-like. This is the point of the gauntlet — motivated tuning always finds something,
and the method has to be able to tell.

The sealed generator (`make_ringer.py`, deterministic) reproduces the mapping exactly.

## Key numbers

- 6 claims, 2 transliterations each, plus steelman variants: 18 rejected verdicts.
- Verdict thresholds (preregistered): permutation p ≥ .01 → rejected; generalization
  ratio < 0.8 → rejected; violation rate > 5% → rejected; char-entropy mismatch > 15% vs
  reference → rejected.
- Ringer surface performance (tuning only): 54.6% train / 44.6% out-of-sample attestation —
  fully explained by the random-mapping null.

## Carried lesson

The adversary's fabrication screen was subsequently calibrated 2-for-2 across two distinct
failure modes: the G6 synthetic decipherment here, and the fabricated dossier cell planted
in the WP2 slate (see [wp2.md](wp2.md)).
