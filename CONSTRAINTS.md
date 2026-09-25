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
- Evidence: `rounds/wp2.md (builder summary)`, `rounds/wp2.md (M2 key numbers)`,
  `rounds/wp2.md (adversary)`.

### A2. or- has a strong positional grammar: depleted at openings, enriched at ends
Any valid theory MUST reproduce: line-initial position is the most or--depleted content
position (.0109 ZL / .0114 IT), line-final is enriched (.020 / .022), standalone
single-token lines highest (.026). (These are the true statistics that exposed the C7
fabrication, recomputed by the adversary from primary data.)
- Certified: WP2-A adversary recompute (C7 kill chain, true-statistics paragraph).
- Evidence: `rounds/wp2.md (adversary)`.

### A3. Paragraph-terminal gradient: or- avoids paragraph openings and accumulates toward closings
Any valid theory MUST reproduce: or- is depleted in paragraph-first lines and enriched in
paragraph-final lines, corpus-wide (builder χ² p = .002 ZL / .001 IT; adversary
Mantel–Haenszel OR 1.655 ZL / 1.955 IT, perm p = .003 / .001 under strata of
section × position-in-line × line-length × paragraph-length — "survives my worst confound
attack"). Carried mostly by herbal + S sections; **flat in pharma/balneo**. Both bare `or`
and or--compounds roughly double from initial to terminal — a property of the morpheme
class, not one lexeme.
- Certified: WP2 M8(i) + WP2-A independent confound attack.
- Evidence: `rounds/wp2.md (builder summary)`, `rounds/wp2.md (adversary)`.

### A4. The line-final enrichment is a STEP at the final slot, not a ramp
Any valid theory MUST reproduce: final-minus-penultimate or- rate +.0078 ZL / +.0075 IT
(p = .004 / .006; adversary independent replicate p = .005 / .010), while penultimate ≈
medial (if anything below). The enrichment is specific to the physical last slot of the
line — a slot effect, not a velocity profile along the line.
- Certified: WP3 T5b; adversary replicate with own estimator/null.
- Evidence: `rounds/wp3.md (builder summary)` (T5b), `rounds/wp3.md (adversary)` (item 4).

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
- Evidence: `rounds/wp3.md (builder summary)`, `rounds/wp3.md (adversary)` (item 2).

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
- Evidence: `rounds/wp3.md (builder summary)`, `rounds/wp3.md (adversary)` (item 4).

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
- Evidence: `rounds/wp4.md (builder summary)`, `rounds/wp4.md (adversary)`,
  `rounds/wp5.md (builder summary)`, `rounds/wp5.md (adversary)`.

### A8. No quire-scale structure anywhere
Any valid theory MUST NOT require quire-level or- structure: quire-opening folios are not
enriched (WP2 M8(iii): p = .774/.860), quire-boundary folios are not enriched (WP4 T3b:
trend negative, p = .775/.853; adversary exact), and the quire-opening page carries no
extra opening-paragraph signal (WP5 T3b: p = .36/.26; adversary cells exact,
13/474 vs 89/4787 ZL). Three independent nulls across three rounds. The or- system is
anchored to the page, not the codex gathering.
- Evidence: `rounds/wp2.md (builder summary)`, `rounds/wp4.md (builder summary)`,
  `rounds/wp5.md (builder summary)`, `rounds/wp5.md (adversary)`.

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
  discharge path. `rounds/wp5.md (builder summary)`, `rounds/wp5.md (adversary)`.
- **B2. Currier-language axis: UNRESOLVED.** The B-arm (P-B negative control) is
  NON-CERTIFIABLE both ways: permutation-significant (builder .012/.007; adversary
  .016/.025 — IT in the knife-edge band) but bootstrap-uncertified (P(≤0) = .088/.113,
  CIs include 0). B neither passes nor is cleanly null. The A−B interaction (T1c) is
  NON-CERTIFIABLE (menu range ZL .033–.091 + boot .061; IT .017–.053 + boot .067; adversary
  paired null .024/.016, boot .051/.063). `rounds/wp5.md (builder summary)`,
  `rounds/wp5.md (adversary)`.
- **B3. Within-herbal Currier reversal (PH4): ZL-solid, IT-thin.** H-B folios show larger
  opening enrichment than H-A (+.0157/+.0096 vs +.0032/+.0038), NOT_PREREG; the H-B arm is
  8/10 folios, adversary IT perm p = .065, and the IT effect flips negative on a one-folio
  jackknife (drop f39r: +.0096 → −.0008). Quote with the caveat attached (adversary-required
  wording). `rounds/wp5.md (adversary)`.
- **B4. Pharma-section or- enrichment: real, attribution unknown.** P section .0252/.0265 vs
  corpus .0154/.0161 — replicated, but all 16 P folios are scribe-1/Currier-A (section and
  hand coextensive); huge per-folio spread; register vs scribe vs content not separable with
  held data. `rounds/wp2.md (adversary)` (item 4).
- **B5. Register contrast (bare-or share H vs P): pooled-real, folio-cluster
  NON-CERTIFIABLE.** Raw shares exact (77.1% H vs 55.4% P ZL; 76.2% vs 49.3% IT), but the
  clustered contrast ranges p = .008–.088 across defensible nulls at 15–16 P-folio clusters —
  cannot certify fail OR pass (WP4-A amendment retitling the builder's "fails both").
  `rounds/wp4.md (builder summary)` (T6 + amendment), `rounds/wp4.md (adversary)`.
- **B6. Cross-transliteration repertoire stability: high but not unique.** T5 JSD .0457 vs
  null .1596, exact p = .04995 (49/1000 low nulls, nearest 1.5e-05 below obs — a seed-level
  coin flip); the entire low tail is generated by the `ai` family, which is equally stable.
  Adversary ruling: passes by prereg letter, "not load-bearing evidence" — treat as
  unproven-but-not-refuted. `rounds/wp4.md (builder summary)`,
  `rounds/wp4.md (adversary)`.
- **B7. Active anti-selectivity of or- contexts: IT-only, moderate.** Above-background
  left-neighbor entropy significant in IT (p = .028 builder; .033–.037 adversary estimators),
  ZL trend only (p = .06–.096). The strong claim is A6's *absence of integration*; ship the
  anti-selective direction with the IT-only label. `rounds/wp3.md (adversary)`.
- **B8. Within-folio line-index drift: straddles .05.** T4b mean Spearman +.019/+.015,
  p = .056/.051 (adversary conventions .060/.065). At most a weak global drift; the geometry
  is local to line ends. `rounds/wp3.md (builder summary)`.
- **B9. Scribe-hand effects are inseparable from Currier language on this corpus.** WP4 T1
  scribe-variance passes raw (p = .001/.001) but evaporates under section × Currier
  stratification (PH1 p = .148/.121) — with the adversary's caveat that stratification also
  costs ~60% of the domain (171→67 folios), so the honest reading is "cannot be separated,"
  not "shown artifactual." **Binding design rule: Currier A/B is a mandatory stratum in any
  future scribe/hand test.** `rounds/wp4.md (builder summary)`,
  `rounds/wp4.md (adversary)`.
- **B10. Ink-density coupling: positive, non-significant.** T5c ρ = +.111/+.114,
  p = .071/.073, against a WP2-carried anti-coupling on regularity. No verdict weight.
  `rounds/wp3.md (builder summary)`.
- **B11. The opening-paragraph zone is HEAD-anchored, unlike the corpus line-final step.**
  Inside opening paragraphs the line-final step is NOT established (T4a: ZL fail p = .110;
  IT NON-CERTIFIABLE, menu .037–.082 + boot .042; T4b descriptively flat-to-negative), and
  the first line of the opening paragraph carries the highest rate (PH2, NOT_PREREG:
  opening lines-2+ .0188/.0203 vs interior lines-2+ .0144/.0159). Two distinct positional
  signatures — worth separating in any theory and in L5.
  `rounds/wp5.md (builder summary)`.
- **B12. Opening effect is descriptively carried more by bare `or` than compounds**
  (PH3 WP5, NOT_PREREG: +.0044 vs +.0019 ZL). `rounds/wp5.md (builder summary)`.

---

## Tier C — RETIRED / FALSIFIED FRAMINGS

*A theory that depends on any of these inherits its refutation.*

- **C1. Production-order / scribal-timing artifact (WP2 M2): DISFAVORED.** Root signal
  survives full production conditioning (see A1). `rounds/wp2.md (builder summary)`.
- **C2. Visual-textual prosody / metronome (WP2 M4): DISFAVORED.** No sub-Poisson
  regularity (CV .82–.90, wrong direction in IT); ink-density coupling anti-predicted
  (ρ = −0.23/−0.27). `rounds/wp2.md (builder summary)`.
- **C3. Alchemical/recipe state-marker (WP2 M6): DISFAVORED.** or- flat across
  recipe-initial/medial/terminal lines in pharma paragraphs (p ≈ .995/.861).
  `rounds/wp2.md (builder summary)`.
- **C4. Script-as-ornament (WP2 M8) as stated: MOSTLY DISFAVORED**, and the
  **quire-opening explanation specifically is retired** (openings not enriched,
  p = .774/.860; reinforced by WP4 T3b and WP5 T3b — see A8). The one surviving M8 signal
  (paragraph-terminal gradient) is the *opposite* shape to ornamental headers and was
  reclassified as positional grammar (A3). `rounds/wp2.md (builder summary)`.
- **C5. Graphemic parts/segmentation marker (WP2 M3): DISFAVORED** within-section
  (p = .33/.43; stratified arm wrong sign; zodiac 100%-segmented yet or--poor).
  `rounds/wp2.md (builder summary)`.
- **C6. Spatial/depth encoding (WP2 M7): DISFAVORED** — wrong sign in the two effective
  arms; adversary steelman (CMH adjustment for token-length/position composition) FAILED to
  rescue it (OR .854/.866, still ≤ 1), while validly criticizing the "four arms" language.
  `rounds/wp2.md (builder summary)`, `rounds/wp2.md (adversary)`.
- **C7. Semantic anchor / block-closure coda (WP3 H3): DISFAVORED.** Paragraph-terminal
  enrichment does NOT exceed line-final (T3a p = .71/.63); counts over-dispersed (opposite
  of one-seal-per-block); gradient weakens in bigger blocks. There is ONE end-position
  grammar, not a separate block-seal mechanism. `rounds/wp3.md (builder summary)`.
- **C8. Directional decay residue (WP3 H2's directional component): KILLED.** The T4a
  excess is symmetric (post-hoc mirror p = .001 both); the surviving ZL-only directional
  residue (p = .003) vanishes under residual-length matching (adversary re-run: p = .46) —
  all three signatures of a forking path. What stands is only the symmetric fact (or-
  residues are common substrings of the folio's own material = A5 in positional dress).
  `rounds/wp3.md (adversary)` (item 3).
- **C9. Grammatical-particle reading of H1: DOWNGRADED.** The certified content is A5
  (prefix-family composition); particle status is NOT established (or- is mid-pack among
  productive EVA prefix families on both ladders). `rounds/wp3.md (adversary)` (item 2).
- **C10. Notational-abbreviation specialist hands (WP4 N1): DISFAVORED** — the scribe
  effect is inseparable from the Currier division (B9). `rounds/wp4.md (builder summary)`.
- **C11. Visual-buffer / separator (WP4 N3): MIXED by prereg letter, substantively
  DISFAVORED-leaning.** Local-entropy dip dead null (T4); regular-spacing prediction fails
  clearly both translits; the sole "pass" is the knife-edge, non-unique T5 (B6).
  `rounds/wp4.md (builder summary)`, `rounds/wp4.md (adversary)`.
- **C12. Quantitative/inventory tagging (WP4 N4): DISFAVORED.** Carried kill from WP3 T1b
  (stems are free vocabulary, contradicting a closed shorthand inventory) plus T6
  non-certifiability (B5). `rounds/wp4.md (builder summary)`.
- **C13. Geometric heading-confound explanation of the folio-opening effect: DISFAVORED.**
  T2a certified under both frozen annotation variants and a 0.5–0.9 threshold sweep;
  heading-like paragraphs are or--depleted (T2b). (The *semantic* one-line-heading variant
  remains open — B1.) `rounds/wp5.md (builder summary)`, `rounds/wp5.md (adversary)`.
- **C14. "A-language retirement" (WP5 draft claim): OVERCLAIM, corrected.** The claim that
  the opening effect is A-language-exclusive was not supported — but its wholesale
  "retirement" was itself overclaimed. Adversary-corrected scoping (binding wording):
  **"language specificity UNRESOLVED: B-arm certifiability fails both ways; section
  modulation observed, balneo-negativity cell-exact reproduced."**
  `rounds/wp5.md (adversary)`.
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
  `rounds/wp6.md (builder summary)`, `rounds/wp6.md (adversary)`.
- **C15. Fabricated dossier C7 ("grammatical case", WP2 slate): FABRICATION, caught.** A
  planted ringer; line-initial cells inflated ~2.5× (claimed .02742/.02809 vs true
  .01094/.01139), killed by recompute divergence + integer-impossibility fingerprint +
  cross-dossier inconsistency. Retained in the ledger as the calibration proof that the
  adversary screen detects fabrication — and because the TRUE statistics it exposed became
  A2. `rounds/wp2.md (adversary)`.

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

---

## Live threads (post-L5 / handed to WP7)

1. **The one-line-heading question (B1):** opening enrichment beyond the first line is
   permutation-strong but cluster-uncertified at every resampling grain; blind semantic
   heading annotation (U1) is the only identified discharge path.
2. **The Currier axis (B2/B3): UNRESOLVED** — B-arm non-certifiable both directions; the
   within-H reversal is ZL-solid/IT-thin with a one-folio jackknife caveat.
3. **L5 disposition:** Lucen's M1 killed (C16). Remaining L5 lanes for WP7: **M3**
   (folio-boundary/collation proxy — first-token x-offset geometry, morphology-independent
   redesign) and **M2** (rubric/ink markers → U4 image round, exploratory).
4. **NOT_PREREG lead (WP6-A, descriptive only, no verdict rests on it):** page-initial
   position shows no or- repertoire narrowing; for high-frequency classes qo/ol, first
   lines are significantly MORE lexically diverse than the within-page null (adversary
   seeds: qo dH p_le = .0001 / dS p_le = .0078; ol p_le = .0102/.0062, ol dS boot CI
   [−0.256, −0.008] excludes 0 opposite-direction). "First lines favor lexical variety"
   is a candidate mechanism for a future prereg round.

*Compiled from: WP2 (2026-09-18), WP2-A (2026-09-18), WP3 (2026-09-19), WP3-A (2026-09-19),
WP4 (2026-09-23), WP4-A (2026-09-23), WP5 (2026-09-23), WP5-A (2026-09-23), WP6 (2026-09-25),
WP6-A (2026-09-25). Claims from
earlier phases not documented in these round files (e.g. the phase-3 self-citation generator
result) are deliberately NOT entered here — nothing enters the ledger that cannot be
verified against a round evidence file.*

🜂
