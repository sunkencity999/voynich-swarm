# CONSTRAINTS.md — Certified Constraint Ledger of the Voynich Swarm Campaign

*Compiled 2026-09-23 by the orchestrator (Cherubesque) from the round evidence files of
WP2–WP6. Every entry cites the file(s) that certified it; every number below was verified
against those files (and spot-checked against the underlying test JSONs) at compile time.
Nothing here is upgraded beyond the certification level filed in the round record.*

---

## Purpose

The campaign's product is not a translation. It is a **bounding box for translations**: a
ledger of structural facts about the *or-* token system (and the manuscript's positional
grammar) that survived preregistration, adversarial recomputation, and — where required —
folio-cluster bootstrap. Voynich theorizing has historically been unbounded guesswork; this
ledger ends that for any theory that engages with it honestly.

**How to use it:** any candidate translation, cipher, generation mechanism, or structural
theory of the Voynich manuscript must reproduce **every Tier-A fact** below. A theory that
cannot is dead on arrival, whatever else it explains. Tier-B observations are supported but
carry named caveats — a theory gains credit for explaining them but cannot be killed by
them alone. Tier-C framings are retired: a theory that *depends* on one of them inherits
its refutation.

## Method (what "certified" means here)

- **Preregistration:** every test's statistic, direction, strata, and pass/fail rule frozen
  in the round DESIGN.md before execution. Post-hoc analyses permanently labeled NOT_PREREG.
- **Frozen inputs & seeds:** all rounds inherit one frozen token parse (38,440 ZL / 37,759 IT
  tokens; ZL = EVA/ZL3b-n, IT = Takahashi/IT2a-n). Permutation nulls nperm=1000, per-round
  seeds, checkpointed every 100 draws with crash-resume verified bit-identical.
- **Both transliterations:** every claim tested in ZL and IT; transliteration-divergent
  results are flagged, never pooled away.
- **Adversarial recompute:** an independent adversary (Smaug; WP4-A by the orchestrator)
  re-derives headline cells from primary dumps with its own code, nulls, and seeds. The
  adversary was calibrated on planted ringers and caught a fabricated dossier cell (WP2
  slate, dossier C7) by integer-fingerprint and cross-cell consistency — the screen works.
- **Folio-cluster bootstrap:** from WP4 onward, headline claims additionally require a
  cluster-level bootstrap CI excluding zero (folios are the sampling unit; pooled-token
  permutation alone can be carried by a few dense pages).
- **Knife-edge disclosure:** results whose p ranges straddle .05 across defensible null
  choices are declared **NON-CERTIFIABLE** in either direction, with the full range filed.
- **Contrast-domain existence proofs (campaign law, WP8):** input existence proofs must
  cover the contrast domain, not just the measurand — **both arms non-empty at
  preregistered floors** before a battery may be declared runnable. Adopted after WP7
  (measurand missing from all frozen inputs) and WP8 (measurand exists, contrast arm
  empty corpus-wide) failed one level apart on the same omission.
- **Image-derived measurands (WP8):** any image-derived measurand must pass a blind
  reliability certification (spot-check vs independent measurement, prereg ICC/agreement
  bars) at a stage-0 commit boundary BEFORE any statistic consumes it; an uncertified
  measurand is terminal for all downstream statistics, prereg or not. Machinery validated
  end-to-end in WP8 (negative case: a broken CV pipeline was caught and stopped) and
  again in WP8b (second negative case, upgraded machinery: n=100 spot lines, git-fact
  stage boundaries, bootstrap-CI prong — the CI prong is load-bearing, closing the
  sampling-luck hole identified in WP8-A).
- **Git-fact stage boundaries (campaign law, WP8b-A amendment A):** stage boundaries are
  proven by commit ordering, never mtime; human measurement files committed BEFORE the
  scorer runs; measurement code committed BEFORE the corpus run. Freeze/boundary times
  quoted in prose MUST be generated from `git log --format=%cI` / `stat`, never typed
  from memory (third occurrence of wall-clock drift; next occurrence is a round defect
  proper).
- **Exhaustive triage partitions (campaign law, WP8b-A amendment B):** any post-verdict
  failure-triage census must be an exhaustive partition of the failure set — every line
  beyond the bar gets exactly one class, counts sum to n.
- **Second annotator for passes (campaign law, WP8b-A amendment C):** any round in which
  the certification bar could PASS requires a second annotator independent of the builder
  (or the adversary's pass folded in before certification). Builder-only annotation is
  admissible evidence for failure, never for certification.
- **Ceiling-quoted coverage bars (campaign law, WP8c-A amendment 3):** every coverage bar
  must, at freeze, quote its structurally computable ceiling from frozen inputs; a bar
  above its ceiling is invalid prereg. Counting scripts for hard gates commit before
  they run.
- **Informative duplicates only (campaign law, WP9-A amendment AM-2):** a duplicate tile
  on which original and duplicate share zero definite axes is UNSCORED, not an agreement;
  intra-rater bars apply over informative duplicates with a minimum of 5, else the gate
  is INCONCLUSIVE and a fresh seeded duplicate draw is required.
- **Revision-budget consumption rule (campaign law, WP9-A amendment AM-3):** a masking/
  instrument revision counts against its preregistered budget the moment any gate, probe,
  or annotator consumes its outputs; unprobed intermediate renders are permitted only
  with their render statistics disclosed in the revision commit.
- **Thin-margin caveats travel (campaign law, WP9-A amendment AM-4):** any reuse or
  citation of a method certified by a thin-margin gate must carry the margin figure
  alongside it (WP9 P1: p=.0555 builder / .0570 adversary vs bar ≥.05).
- **Probe deployment pre-logging (campaign law, WP9-A amendment AM-5):** the concrete
  probe/verifier deployment must be logged in a commit that PRECEDES the first
  probe-call artifact commit; same-commit logging was ruled benign once (WP9) and is
  disallowed going forward.

Rounds: WP2 (mechanism discrimination, L1 slate), WP3 (H1–H4, L2 slate), WP4 (N1–N4, L3
slate), WP5 (opening-boundary battery, L4 round). Each has a builder `tests/results/summary.md`
and an adversary `verdicts-adversary/SUMMARY.md` (+ `VERIFICATION.md` in WP4/WP5). The
root correlate itself was established in phases 1–9 (`voynich-bpe/`) and is carried into
this ledger only in the WP2-formalized, adversary-verified form (A1).

---

## Tier A — CERTIFIED FACTS

*Survived preregistration + adversary recompute (+ folio-cluster bootstrap where the round
required it). Any valid theory MUST reproduce every one of these.*

### A1. The root-emphasis ↔ or- correlate is content-linked, not a production artifact
Any valid theory MUST reproduce: folios whose plant drawings emphasize roots have elevated
*or-* rates, **and this survives conditioning on scribe, quire, page-in-quire, Currier hand,
and global production sequence**. Nested-model ΔR² = 0.047 ZL / 0.045 IT (null means .006/.005;
observed ≈ 8–9× null, > 2× the null 95th percentile), permutation p = .001 / .001.
- Certified: WP2 M2 (DISFAVORED verdict on the production-order mechanism); adversary
  recompute exact (C3 cells, deltas 0).
- Evidence: `wp2/tests/results/summary.md`, `wp2/tests/results/M2.json`,
  `wp2/verdicts-adversary/SUMMARY.md`.

### A2. or- has a strong positional grammar: depleted at openings, enriched at ends
Any valid theory MUST reproduce: line-initial position is the most or--depleted content
position (.0109 ZL / .0114 IT), line-final is enriched (.020 / .022), standalone
single-token lines highest (.026). (These are the true statistics that exposed the C7
fabrication, recomputed by the adversary from primary data.)
- Certified: WP2-A adversary recompute (C7 kill chain, true-statistics paragraph).
- Evidence: `wp2/verdicts-adversary/SUMMARY.md`.

### A3. Paragraph-terminal gradient: or- avoids paragraph openings and accumulates toward closings
Any valid theory MUST reproduce: or- is depleted in paragraph-first lines and enriched in
paragraph-final lines, corpus-wide (builder χ² p = .002 ZL / .001 IT; adversary
Mantel–Haenszel OR 1.655 ZL / 1.955 IT, perm p = .003 / .001 under strata of
section × position-in-line × line-length × paragraph-length — "survives my worst confound
attack"). Carried mostly by herbal + S sections; **flat in pharma/balneo**. Both bare `or`
and or--compounds roughly double from initial to terminal — a property of the morpheme
class, not one lexeme.
- Certified: WP2 M8(i) + WP2-A independent confound attack.
- Evidence: `wp2/tests/results/summary.md`, `wp2/verdicts-adversary/SUMMARY.md`.

### A4. The line-final enrichment is a STEP at the final slot, not a ramp
Any valid theory MUST reproduce: final-minus-penultimate or- rate +.0078 ZL / +.0075 IT
(p = .004 / .006; adversary independent replicate p = .005 / .010), while penultimate ≈
medial (if anything below). The enrichment is specific to the physical last slot of the
line — a slot effect, not a velocity profile along the line.
- Certified: WP3 T5b; adversary replicate with own estimator/null.
- Evidence: `wp3/tests/results/summary.md` (T5b), `wp3/verdicts-adversary/SUMMARY.md` (item 4).

### A5. or- words decompose as `or` + free stems from a small closed repertoire
Any valid theory MUST reproduce: the or- family has drastically lower type/token ratio than
size-matched controls (.145 vs .653 ZL, .147 vs .661 IT, p = .001 both) and its
prefix-stripped stems are attested as free vocabulary far above matched controls
(.788 / .739 vs null ≈ .49, p = .001 both; survives token-length matching).
**Adversary-narrowed interpretation (binding):** this profile is shared by ordinary
productive EVA prefix families (or- ranks #7/24 ZL, #4/22 IT on the TTR ladder; #11/60,
#13/63 on attestation) — it certifies *closed-prefix-family composition*, NOT grammatical
particle status.
- Certified: WP3 T1a/T1b (exact adversary recompute), with the WP3-A item-2 downgrade of
  the H1 claim attached as part of the record.
- Evidence: `wp3/tests/results/summary.md`, `wp3/verdicts-adversary/SUMMARY.md` (item 2).

### A6. or- shows NO linguistic context-selectivity (integration absent)
Any valid theory MUST reproduce: left-neighbor entropy of or- tokens is at or above the
stratum-matched background (lower-tail p = .905 ZL / .973 IT — "crushing" absence of the
selectivity a grammatical particle class requires), and there is no particle-stacking
avoidance and no gloss-run excess (T2b both tails ns, both translits). The preregistered
master axis therefore lands on the **process** side: the or- profile matches insertion
from a repertoire, not syntactic integration. (Active *anti*-selectivity is IT-only
moderate — see B7.)
- Certified: WP3 T2a/T2b; adversary replicated with own estimator (Miller–Madow), own null,
  own seed; "accepted as campaign fact with the IT-only-strength caveat."
- Evidence: `wp3/tests/results/summary.md`, `wp3/verdicts-adversary/SUMMARY.md` (item 4).

### A7. Folio-opening enrichment: or- is enriched in the FIRST paragraph of a page — the campaign's headline certified fact
Any valid theory MUST reproduce ALL of the following facets:
- **Boundary-paragraph enrichment** (WP4 T3a, prereg): +.0046 ZL / +.0039 IT, p = .002/.002;
  the NOT_PREREG split shows it is entirely the FIRST paragraph (p = .001/.001; last-para
  ns) — an opening stamp, not a closing one. Adversary recompute exact
  (177/10026 vs 187/14320 ZL).
- **Folio-cluster certified** (WP5 T1a, Currier-A arm): +.0137 ZL (p = .002, boot CI
  [+.0026, +.0238]) / +.0127 IT (p = .003, boot CI [+.0031, +.0212]); adversary confirms
  with own nulls (p .002/.001) and own bootstrap seed.
- **Robust to heading geometry** (WP5 T2a): certified after removing geometrically
  heading-like paragraphs under both frozen annotation variants (+.0055/+.0055,
  p = .002/.001, boot CIs exclude 0); adversary threshold sweep 0.5–0.9 × folio-median
  passes all 10 cells. Heading-like paragraphs are themselves or--DEPLETED (T2b, −.0040/−.0026,
  p_ge = .89 both) — the geometric-heading confound is disfavored.
- **Page-level, both faces** (WP5 T3a): present on recto (+.0053 ZL p=.007 / +.0065 IT p=.001)
  and verso (+.0077 p=.006 / +.0060 p=.017) alike; recto−verso contrast null. The unit is
  the written page, not the leaf.
- **Section-modulated, balneo-negative**: positive in S/P/H sections, negative in the
  balneological section (−.002 ZL / −.003 IT; adversary reproduced cell-exact,
  −.002246/−.002585). NOT a Currier-language split (the Currier axis is UNRESOLVED — B2).
- Certified: WP4 T3a + PH3 + WP4-A; WP5 T1a/T2a/T2b/T3a + WP5-A.
- Evidence: `wp4/tests/results/summary.md`, `wp4/verdicts-adversary/SUMMARY.md`,
  `wp5/tests/results/summary.md`, `wp5/verdicts-adversary/SUMMARY.md`.

### A8. No quire-scale structure anywhere
Any valid theory MUST NOT require quire-level or- structure: quire-opening folios are not
enriched (WP2 M8(iii): p = .774/.860), quire-boundary folios are not enriched (WP4 T3b:
trend negative, p = .775/.853; adversary exact), and the quire-opening page carries no
extra opening-paragraph signal (WP5 T3b: p = .36/.26; adversary cells exact,
13/474 vs 89/4787 ZL). Three independent nulls across three rounds. The or- system is
anchored to the page, not the codex gathering.
- Evidence: `wp2/tests/results/summary.md`, `wp4/tests/results/summary.md`,
  `wp5/tests/results/summary.md`, `wp5/verdicts-adversary/SUMMARY.md`.

### A9. The or--initial page-initial contrast domain is EMPTY: or- never supplies the first token of a page's first line
Any valid theory MUST accommodate that or- tokens NEVER appear as the FIRST token of a
page's rank-1 paragraph line: **0/206 pages in ZL and 0/206 in IT** (deterministic corpus
count, adversary-confirmed by independent raw re-parse with own line-ranking and class
rules; control-class 10/6, first slots gallows-dominated: pc 32, po 31, ko 14). Body
lines ranks 2–4: 11 or--initial lines corpus-wide in each transliteration. This sharpens
A2/A3 (opening depletion) to an absolute zero at the strongest opening position — and it
renders the WP7-preregistered L5-M3 contrast (or--initial vs control-initial page-initial
lines) permanently NON-RUNNABLE as written. The contains-based domain (rank-1 line
contains ≥1 or- token) IS live: 23 ZL / 25 IT pages (12 of ZL's 23 in Herbal), filed for
a future WP8b prereg.
- Evidence: `wp8/tests/results/T7_contains_domain_census.json`,
  `wp8/verdicts-adversary/SUMMARY.md`,
  `wp8/verdicts-adversary/adversary_results.json`.

### Composite Tier-A profile (adversary synthesis, WP3-A item 5, extended by WP4/WP5)
> or- is appended at terminal slots — line-final specifically (step, not ramp), amplified at
> paragraph-terminal lines, depleted at line and paragraph openings — **and separately enriched
> in the first paragraph of the page** (head-anchored there, not final-slot-anchored — see B12);
> it is drawn from a prefix-family repertoire of free stems (`or` + orX), with no context
> selectivity, no stacking, no verbatim-label excess, no established direction-of-derivation,
> no ink coupling, and no quire-scale structure; and its density tracks root-emphasis drawing
> content within the herbal section independent of production order.

---

## Tier B — SUPPORTED BUT UNCERTIFIED

*Real observations with named caveats. A theory should engage these; none can certify or
kill a theory alone. Certification levels copied exactly as filed.*

- **B1. Opening enrichment beyond the first line (T2c): permutation-strong,
  cluster-UNCERTIFIED.** First-line-excised opening enrichment +.0043/+.0045, perm
  p = .001/.002, but boot CI includes 0 in both translits (exactly 50/1000 and 82/1000
  resamples ≤ 0, zero ties); adversary confirmed at folio, bifolio, AND quire grains
  (P(≤0) .053–.079). A one-line-heading reading is *disfavored* (T2b depletion) but not
  formally discharged — the U1 unlock (blind semantic heading annotation from scans) is the
  discharge path. `wp5/tests/results/summary.md`, `wp5/verdicts-adversary/SUMMARY.md`.
- **B2. Currier-language axis: UNRESOLVED.** The B-arm (P-B negative control) is
  NON-CERTIFIABLE both ways: permutation-significant (builder .012/.007; adversary
  .016/.025 — IT in the knife-edge band) but bootstrap-uncertified (P(≤0) = .088/.113,
  CIs include 0). B neither passes nor is cleanly null. The A−B interaction (T1c) is
  NON-CERTIFIABLE (menu range ZL .033–.091 + boot .061; IT .017–.053 + boot .067; adversary
  paired null .024/.016, boot .051/.063). `wp5/tests/results/summary.md`,
  `wp5/verdicts-adversary/SUMMARY.md`.
- **B3. Within-herbal Currier reversal (PH4): ZL-solid, IT-thin.** H-B folios show larger
  opening enrichment than H-A (+.0157/+.0096 vs +.0032/+.0038), NOT_PREREG; the H-B arm is
  8/10 folios, adversary IT perm p = .065, and the IT effect flips negative on a one-folio
  jackknife (drop f39r: +.0096 → −.0008). Quote with the caveat attached (adversary-required
  wording). `wp5/verdicts-adversary/SUMMARY.md`.
- **B4. Pharma-section or- enrichment: real, attribution unknown.** P section .0252/.0265 vs
  corpus .0154/.0161 — replicated, but all 16 P folios are scribe-1/Currier-A (section and
  hand coextensive); huge per-folio spread; register vs scribe vs content not separable with
  held data. `wp2/verdicts-adversary/SUMMARY.md` (item 4).
- **B5. Register contrast (bare-or share H vs P): pooled-real, folio-cluster
  NON-CERTIFIABLE.** Raw shares exact (77.1% H vs 55.4% P ZL; 76.2% vs 49.3% IT), but the
  clustered contrast ranges p = .008–.088 across defensible nulls at 15–16 P-folio clusters —
  cannot certify fail OR pass (WP4-A amendment retitling the builder's "fails both").
  `wp4/tests/results/summary.md` (T6 + amendment), `wp4/verdicts-adversary/SUMMARY.md`.
- **B6. Cross-transliteration repertoire stability: high but not unique.** T5 JSD .0457 vs
  null .1596, exact p = .04995 (49/1000 low nulls, nearest 1.5e-05 below obs — a seed-level
  coin flip); the entire low tail is generated by the `ai` family, which is equally stable.
  Adversary ruling: passes by prereg letter, "not load-bearing evidence" — treat as
  unproven-but-not-refuted. `wp4/tests/results/summary.md`,
  `wp4/verdicts-adversary/SUMMARY.md`.
- **B7. Active anti-selectivity of or- contexts: IT-only, moderate.** Above-background
  left-neighbor entropy significant in IT (p = .028 builder; .033–.037 adversary estimators),
  ZL trend only (p = .06–.096). The strong claim is A6's *absence of integration*; ship the
  anti-selective direction with the IT-only label. `wp3/verdicts-adversary/SUMMARY.md`.
- **B8. Within-folio line-index drift: straddles .05.** T4b mean Spearman +.019/+.015,
  p = .056/.051 (adversary conventions .060/.065). At most a weak global drift; the geometry
  is local to line ends. `wp3/tests/results/summary.md`.
- **B9. Scribe-hand effects are inseparable from Currier language on this corpus.** WP4 T1
  scribe-variance passes raw (p = .001/.001) but evaporates under section × Currier
  stratification (PH1 p = .148/.121) — with the adversary's caveat that stratification also
  costs ~60% of the domain (171→67 folios), so the honest reading is "cannot be separated,"
  not "shown artifactual." **Binding design rule: Currier A/B is a mandatory stratum in any
  future scribe/hand test.** `wp4/tests/results/summary.md`,
  `wp4/verdicts-adversary/SUMMARY.md`.
- **B10. Ink-density coupling: positive, non-significant.** T5c ρ = +.111/+.114,
  p = .071/.073, against a WP2-carried anti-coupling on regularity. No verdict weight.
  `wp3/tests/results/summary.md`.
- **B11. The opening-paragraph zone is HEAD-anchored, unlike the corpus line-final step.**
  Inside opening paragraphs the line-final step is NOT established (T4a: ZL fail p = .110;
  IT NON-CERTIFIABLE, menu .037–.082 + boot .042; T4b descriptively flat-to-negative), and
  the first line of the opening paragraph carries the highest rate (PH2, NOT_PREREG:
  opening lines-2+ .0188/.0203 vs interior lines-2+ .0144/.0159). Two distinct positional
  signatures — worth separating in any theory and in L5.
  `wp5/tests/results/summary.md`.
- **B12. Opening effect is descriptively carried more by bare `or` than compounds**
  (PH3 WP5, NOT_PREREG: +.0044 vs +.0019 ZL). `wp5/tests/results/summary.md`.

---

## Tier C — RETIRED / FALSIFIED FRAMINGS

*A theory that depends on any of these inherits its refutation.*

- **C1. Production-order / scribal-timing artifact (WP2 M2): DISFAVORED.** Root signal
  survives full production conditioning (see A1). `wp2/tests/results/summary.md`.
- **C2. Visual-textual prosody / metronome (WP2 M4): DISFAVORED.** No sub-Poisson
  regularity (CV .82–.90, wrong direction in IT); ink-density coupling anti-predicted
  (ρ = −0.23/−0.27). `wp2/tests/results/summary.md`.
- **C3. Alchemical/recipe state-marker (WP2 M6): DISFAVORED.** or- flat across
  recipe-initial/medial/terminal lines in pharma paragraphs (p ≈ .995/.861).
  `wp2/tests/results/summary.md`.
- **C4. Script-as-ornament (WP2 M8) as stated: MOSTLY DISFAVORED**, and the
  **quire-opening explanation specifically is retired** (openings not enriched,
  p = .774/.860; reinforced by WP4 T3b and WP5 T3b — see A8). The one surviving M8 signal
  (paragraph-terminal gradient) is the *opposite* shape to ornamental headers and was
  reclassified as positional grammar (A3). `wp2/tests/results/summary.md`.
- **C5. Graphemic parts/segmentation marker (WP2 M3): DISFAVORED** within-section
  (p = .33/.43; stratified arm wrong sign; zodiac 100%-segmented yet or--poor).
  `wp2/tests/results/summary.md`.
- **C6. Spatial/depth encoding (WP2 M7): DISFAVORED** — wrong sign in the two effective
  arms; adversary steelman (CMH adjustment for token-length/position composition) FAILED to
  rescue it (OR .854/.866, still ≤ 1), while validly criticizing the "four arms" language.
  `wp2/tests/results/summary.md`, `wp2/verdicts-adversary/SUMMARY.md`.
- **C7. Semantic anchor / block-closure coda (WP3 H3): DISFAVORED.** Paragraph-terminal
  enrichment does NOT exceed line-final (T3a p = .71/.63); counts over-dispersed (opposite
  of one-seal-per-block); gradient weakens in bigger blocks. There is ONE end-position
  grammar, not a separate block-seal mechanism. `wp3/tests/results/summary.md`.
- **C8. Directional decay residue (WP3 H2's directional component): KILLED.** The T4a
  excess is symmetric (post-hoc mirror p = .001 both); the surviving ZL-only directional
  residue (p = .003) vanishes under residual-length matching (adversary re-run: p = .46) —
  all three signatures of a forking path. What stands is only the symmetric fact (or-
  residues are common substrings of the folio's own material = A5 in positional dress).
  `wp3/verdicts-adversary/SUMMARY.md` (item 3).
- **C9. Grammatical-particle reading of H1: DOWNGRADED.** The certified content is A5
  (prefix-family composition); particle status is NOT established (or- is mid-pack among
  productive EVA prefix families on both ladders). `wp3/verdicts-adversary/SUMMARY.md` (item 2).
- **C10. Notational-abbreviation specialist hands (WP4 N1): DISFAVORED** — the scribe
  effect is inseparable from the Currier division (B9). `wp4/tests/results/summary.md`.
- **C11. Visual-buffer / separator (WP4 N3): MIXED by prereg letter, substantively
  DISFAVORED-leaning.** Local-entropy dip dead null (T4); regular-spacing prediction fails
  clearly both translits; the sole "pass" is the knife-edge, non-unique T5 (B6).
  `wp4/tests/results/summary.md`, `wp4/verdicts-adversary/SUMMARY.md`.
- **C12. Quantitative/inventory tagging (WP4 N4): DISFAVORED.** Carried kill from WP3 T1b
  (stems are free vocabulary, contradicting a closed shorthand inventory) plus T6
  non-certifiability (B5). `wp4/tests/results/summary.md`.
- **C13. Geometric heading-confound explanation of the folio-opening effect: DISFAVORED.**
  T2a certified under both frozen annotation variants and a 0.5–0.9 threshold sweep;
  heading-like paragraphs are or--depleted (T2b). (The *semantic* one-line-heading variant
  remains open — B1.) `wp5/tests/results/summary.md`, `wp5/verdicts-adversary/SUMMARY.md`.
- **C14. "A-language retirement" (WP5 draft claim): OVERCLAIM, corrected.** The claim that
  the opening effect is A-language-exclusive was not supported — but its wholesale
  "retirement" was itself overclaimed. Adversary-corrected scoping (binding wording):
  **"language specificity UNRESOLVED: B-arm certifiability fails both ways; section
  modulation observed, balneo-negativity cell-exact reproduced."**
  `wp5/verdicts-adversary/SUMMARY.md`.
- **C16. Incipit-index stamp (L5-M1, WP6): KILLED.** Lucen's top-ranked L5 mechanism —
  that page-initial or- tokens are a restricted, repeated formula (folio label / incipit /
  filing stamp) — gets no support. Prereg kill rule met exactly: page-initial vs body
  repertoire differences null on both headline statistics (dH obs −0.3697, perm p_ge = .857,
  folio-cluster boot CI [−1.000, 0.656] ∋ 0; dS obs −0.1140, p_ge = .862, CI [−0.334,
  0.074] ∋ 0; 10k draws, seeds 555001/555002). Direction is *opposite* to the hypothesis:
  page-initial or- lines are the most lexically diverse (H by line rank 2.326/1.785/1.748/
  1.482 bits), not formulaic. T6d artifact controls 0/4 triggered. Adversary CONFIRMED at
  independent seeds 777601/777602, 20k draws (p_ge .856/.860, CIs [−1.009, 0.638] /
  [−0.325, 0.072]), fabrication screen clean, zero substantive defects (one doc-only row-count
  typo: adversary dump is 2,142 rows, not 2,040). Whatever the certified page-opening or-
  concentration (A7) is, it is NOT a narrow repeated formula. Provenance: L5 mechanisms
  were generated by Lucen's AiBox local lane (gemma-4-26B), noted per WP6 DESIGN caveat.
  `wp6/SUMMARY.md`, `wp6/verdicts-adversary/SUMMARY.md`.
- **C17. First-line-variety mechanism for A7 (WP7 H-B): KILLED.** The cross-link
  hypothesis — that elevated first-line lexical diversity (WP6-A's NOT_PREREG lead) is the
  mechanism behind the certified or- opening enrichment (A7), predicting positive
  co-variation across sections — fails with the WRONG SIGN: Spearman ρ = −0.600 (ZL, k=4
  sections B/H/P/S; exact enumeration p_ge = 20/24 = .8333, sampled .832 at 10k draws,
  seeds 666001/666002), section-cluster boot CI95 [−1.0, +1.0] ∋ 0 (P(ρ≤0) = .882). Both
  prereg kill conditions fire independently. Anti-pattern: balneo (A7-negative) carries
  the 2nd-largest first-line diversity elevation (c_B = +0.378); S (A7-positive) the
  smallest (+0.113). Adversary CONFIRMED from an independently rebuilt domain
  (multiset-identical, 7,375 rows) at independent seeds 777001/777002, B=10000 boot
  (ρ = −3/5 exactly, p .8333, CI [−1.0, +1.0], P(ρ≤0) .888); per-draw seed reproduction
  bit-level clean; zero major defects (two minor: rounded-intermediate c_s — immaterial at
  ~10⁴× margin — and an unlogged moot arm-split omission). The descriptive first-line
  variety elevation itself replicated in every section (per-section dh_p: B .0455, H .0001,
  P .0211, S .272) but stays NOT_PREREG — decoupled from A7; if it returns, it returns as
  its own mechanism question. Power disclosure: k=4 ⇒ exact-p floor 1/24 ≈ .0417.
  `wp7/SUMMARY.md`, `wp7/verdicts-adversary/SUMMARY.md`.
- **C15. Fabricated dossier C7 ("grammatical case", WP2 slate): FABRICATION, caught.** A
  planted ringer; line-initial cells inflated ~2.5× (claimed .02742/.02809 vs true
  .01094/.01139), killed by recompute divergence + integer-impossibility fingerprint +
  cross-dossier inconsistency. Retained in the ledger as the calibration proof that the
  adversary screen detects fabrication — and because the TRUE statistics it exposed became
  A2. `wp2/verdicts-adversary/SUMMARY.md`.

### Untestable / no verdict possible (recorded, not retired)
- **M1 thematic lexicon (WP2): CONFOUNDED + UNDERPOWERED** — water imagery is coextensive
  with the balneological section (19/19 vs 0), so no discriminating contrast exists;
  descriptive anti-hint only. Unresolved, not refuted.
- **M5 (WP2): UNTESTABLE** with held data (memo filed; circular proxies).
- **WP5 U-memos:** U1 semantic heading annotation (the unlock for B1), U2 original page
  order, U3 cross-manuscript base rates. No verdict weight taken from any of them.
- **WP6 U-memo — U4 page-image analysis:** L5-M2 (rubric/invocation marked by ink density,
  stroke width, or pigment in first lines) is untestable in the text corpus; requires a
  facsimile-image round (explicitly exploratory — page images are outside the certified
  corpus). Recorded, no verdict weight.
- **WP7 H-A — L5-M3 folio-boundary geometry: NON-RUNNABLE, no verdict.** The
  preregistered measurand (first-token start-x offset of page-initial lines) exists in NO
  frozen input: WP2 token tables carry no horizontal-geometry field (0/17 candidate names,
  both translits), WP5 annotations are heading-likeness only, image annotations are motif
  flags, and both IVTFF sources (ZL3b-n, IT2a-n) are single-column aligned (every text
  locus at column 18; 758/875 `<->` gap markers, 0 line-initial). Adversary independently
  verified the blocker in BOTH transliterations and confirmed no proxy was smuggled into
  any computed statistic. Defect traces to WP6's DESIGN disposition note assuming
  x-offsets lived in WP5's para_table — a contract-level input error, not builder
  execution. M3 is neither supported nor killed; the prereg kill rule stays armed for a
  future BLIND start-x annotation round over the folio images (natural companion to U4).
  `wp7/tests/results/T7A.json`, `wp7/verdicts-adversary/SUMMARY.md`.
- **WP8 — L5-M3 image round: NO VERDICT, two independent terminal gates; M3 kill rule
  still armed.** The image round acquired an admissible corpus (213 scans, ~2700–3900 px,
  folio mapping proven against the Wayback-frozen Yale IIIF manifest; SHA256 + dims
  verified 213/213 by the adversary) and unlocked the start-x measurand — but (1) the
  preregistered contrast domain is EMPTY corpus-wide (see A9), and (2) the blind CV
  start-x measurand **FAILED stage-0 certification**: ICC(2,1) = 0.081 vs bar ≥ 0.8,
  median |diff| = 4.46 glyph widths vs bar ≤ 0.5 (adversary recompute 0.0814/4.464 gw,
  independent ICC implementation; sensitivity variant same verdict). Failure is
  pipeline-attributable (gutter-shading onsets, red paint admitted as ink, faint strokes
  missed), so no statistic — prereg or NOT_PREREG — was computed; the planned
  contains-variant was correctly NOT run. Balneo confound rule: not confounded (balneo
  joins second-best, .421) but the rule as written is VACUOUS (pooled median coverage
  0.0) — disclosed degenerate, not scored a pass. Herbal join coverage 0/128 is the main
  pipeline defect to fix for WP8b. M3 remains neither supported nor killed.
  `wp8/SUMMARY.md`, `wp8/infra/stage0_certification.json`,
  `wp8/verdicts-adversary/SUMMARY.md`.
- **WP8b — start-x recertification + contains-domain M3: MEASURAND-FAILED (second
  consecutive negative case); M3 kill rule still armed.** The repair round fixed what it
  aimed at — herbal joinability **0/128 → 27/128** (plant-mask + red-paint mask +
  gutter-shading guard; adversary-verified by independent join), overall joined coverage
  24 → 49/206, the balneo rule non-vacuous this round (balneo .368 ≥ .232, not
  confounded) — but the repaired measurand still failed all three certification prongs:
  **ICC(2,1) = 0.084** vs bar ≥ 0.8, **median |diff| = 5.86 glyph widths** vs ≤ 0.5,
  bootstrap CI lower bound **−0.158** vs ≥ 0.6 (adversary reproduced every number
  exactly with an independent ICC implementation and own-seed B=4000 bootstraps, and
  reproduced the failure magnitude ~8 gw on his own disjoint 8-line annotated sample).
  Adjudicated failure architecture (WP8b-A ledger ruling 1): whole-width y-profile band
  segmentation cannot certify a blind start-x measurand on these scans — the two
  residual failure classes (high-contrast page-edge/adjacent-page slivers admitted as
  onsets; genuine first words absorbed by plant-halo/contrast repairs) trade off
  directly. Second independent blocker (NOT_PREREG census, adversary-recounted): even a
  certified measurand would not unlock M3 — joined or-arm 7 pages (H 6, B 1) < prereg
  floor 15 (control 42 ≥ 30); unlock requires or-arm coverage ≈65% of census pages.
  Stage boundaries were literal git facts (WP8-A defects honored; adversary-audited);
  no statistic ran; seed 664001's permutation stream never consumed; fabrication screen
  clean. WP8c prerequisites (binding, WP8b-A amendment D): geometric edge-band kill +
  block-aware segmentation; or-arm coverage ≥65% demonstrated BEFORE the human
  spot-check is spent; preregistered ICC bootstrap unit and a defined "pooled median"
  for the balneo rule; second annotator per amendment C.
  `wp8b/SUMMARY.md`, `wp8b/infra/stage0_certification.json`,
  `wp8b/verdicts-adversary/SUMMARY.md`.
- **WP8c (COVERAGE-FAILED, terminal; adversary-CONFIRMED WP8c-A):** block-aware rebuild
  raised ZL joins 49→74 (herbal 27→47) and halved hard-edge junk onsets (21→11) but
  joined only **9/23** or-census pages (bar 15/23; control 65≥30 passed) — verdict
  COVERAGE-FAILED at the Stage C hard gate; no sample drawn, 0/100 human budget, no
  statistic, seeds unconsumed. Structural ceiling 18/23 (**5** or-pages lack a
  single-folio canvas). Absorbed-first-word class worsened 23→62/86 (census median
  4.79 gw): coverage and onset fidelity are **coupled** — Stage 0 would likely have
  failed regardless. M3 remains non-runnable; WP7 H-A kill rule stays armed. Adversary
  reproduced every gate number exactly with independent code (own hash pass, own token
  parse, own join implementation from the frozen spec text, seed 775001) and verified
  the r4→r5 freeze decision as self-disfavoring from the QA logs themselves.
  **WP8d prerequisites (binding, WP8c-A amendment 2):** no further round in this design
  family without (a) foldout/canvas handling or a gate on canvassed-joinable pages,
  (b) a join rule robust to ±small band-count noise that doesn't corrupt onsets, and
  (c) a demonstrated absorbed-first-word fix — coverage and fidelity gated **jointly**.
  `wp8c/SUMMARY.md`, `wp8c/infra/coverage_report.json`,
  `wp8c/verdicts-adversary/SUMMARY.md`.
- **WP9 (U1, or-opening content-label semantics): ANNOTATION-FAILED —
  instrument failure; claim UNTESTED (adversary-CONFIRMED WP9-A).** Blind two-family
  visual annotation of text-masked pages passed reliability gates (κ core set: H
  h1/h3/h4, S s1) but failed the preregistered third-family image-groundedness
  verification (17/30 verified vs bar ≥27/30). The round terminated at the R-16
  boundary: no token join was ever performed (no commit joins token and annotation
  data; SEED_PERM/SEED_BOOT unconsumed). The semantic reading of B1 (or-opening as
  content label) is **UNTESTED — not killed, not supported**. B1's structural finding
  (positional or-enrichment) is untouched. Exact per-type grouping remains
  DOMAIN-FAILED at census (5 groups ≥2, 11/171 pages, ZL). **Method constraint
  (binding for revival):** dilation-based masking of a binarized ink mask cannot
  simultaneously pass the text-leakage gates and leave annotatable drawing substrate
  (v2.1: median masked fraction .777, 22/171 pages >90% masked; verification failures
  were 11/30 "unclear"). Revival of U1 requires stroke-level text/drawing separation
  (human-drawn outlines or a trained segmenter). Caveats of record: P1 residual-ink
  non-leakage was certified only thinly (p=.0555 builder / .0570 adversary vs bar
  ≥.05; probe accuracy .698 vs null .651); the post-masking domain was 14 pos pages /
  27 usable pairs (published "13" is an erratum, self-disfavoring); intra-rater gates
  were largely vacuous on the over-masked corpus (A: 7/10 duplicates with zero shared
  definite axes). Adversary-audited WP9-A: chain, gates, and verdict CONFIRMED.
  `wp9/SUMMARY.md`, `wp9/infra/verify_sample_results.json`,
  `wp9/ADVERSARY_REPORT.md`.

---

## Live threads (post-WP9)

1. **The one-line-heading question (B1):** opening enrichment beyond the first line is
   permutation-strong but cluster-uncertified at every resampling grain; blind semantic
   heading annotation (U1) — the only identified discharge path — was attempted in WP9
   and exited ANNOTATION-FAILED (instrument failure, claim UNTESTED). Revival is gated
   on stroke-level text/drawing separation (WP9 method constraint); the WP9-A caveats
   (P1-thin, 14/27 domain) travel with any reuse of the masking method.
2. **The Currier axis (B2/B3): UNRESOLVED** — B-arm non-certifiable both directions; the
   within-H reversal is ZL-solid/IT-thin with a one-folio jackknife caveat.
3. **L5 disposition after WP8c:** M1 killed (C16); M3 blocked four times — no geometry
   in the text corpus (WP7), empty prereg domain on images (A9, WP8), the CV measurand
   failed certification twice (WP8: 4.46 gw; WP8b: 5.86 gw), and the block-aware
   rebuild failed the coverage gate (WP8c: or-arm 9/23 vs bar 15, structural ceiling
   18/23). Any **WP8d** is gated on the WP8c-A amendment-2 prerequisites (foldout/
   canvas handling, noise-robust join rule, demonstrated absorbed-first-word fix,
   joint coverage+fidelity gating) on top of the still-standing WP8b-A amendment-D
   items (prereg bootstrap unit, pooled-median definition, second annotator). The
   kill rule stays armed; nothing about M3 has been supported or falsified.
4. **U4 exploratory leads (NOT_PREREG, candidate generation only):** (a) balneo has the
   tightest line spacing (pitch CV .418) vs herbal loosest (.812) — needs a
   drawing-band-excluded measure; (b) first-line emphasis INVERTED — first bands ~32%
   LIGHTER than body text, disfavoring rubric-like darkening (L5-M2's expected sign).
5. **First-line lexical variety (WP6-A lead, WP7-scoped):** MORE diverse first lines
   replicated descriptively in every section, but the mechanism link to A7 is KILLED with
   the wrong sign (C17) — anti-A7 section profile. Survives only as an independent
   NOT_PREREG mechanism question, decoupled from or- enrichment.

*Compiled from: WP2 (2026-09-18), WP2-A (2026-09-18), WP3 (2026-09-19), WP3-A (2026-09-19),
WP4 (2026-09-23), WP4-A (2026-09-23), WP5 (2026-09-23), WP5-A (2026-09-23), WP6 (2026-09-25),
WP6-A (2026-09-25), WP7 (2026-09-25), WP7-A (2026-09-25), WP8 (2026-09-26), WP8-A
(2026-09-26), WP8b (2026-09-26), WP8b-A (2026-09-26), WP8c (2026-09-26), WP8c-A
(2026-09-26), WP9 (2026-09-26), WP9-A (2026-09-26). Claims from
earlier phases not documented in these round files (e.g. the phase-3 self-citation generator
result) are deliberately NOT entered here — nothing enters the ledger that cannot be
verified against a round evidence file.*

🜂
