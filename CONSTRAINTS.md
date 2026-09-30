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
- **Junction-type disclosure (campaign law, W2-A amendment AM-W2-1):** any claim built
  on token adjacency must classify junction types at freeze (hard / uncertain-space /
  dropped-token), and any published boundary statistic must carry the hard-junction-only
  figure alongside the pooled one. For W2: ZL S_b = 0.1999 pooled / 0.1712 hard-only;
  IT = 0.1784 (comma-free at source).
- **Certification draw floor (campaign law, W2-A amendment AM-W2-2):** generator-
  certification grids use ≥5 draws per grid point (mean metrics vs bars), or a
  preregistered noise rule; single-draw selection is a seed lottery at bar boundaries.
- **Computed ceilings (campaign law, W2-A amendment AM-W2-3):** ceiling notes quoted at
  freeze must be computed from frozen inputs by committed code, never asserted from
  theory (extends WP8c-A amendment 3 from coverage bars to all frozen feasibility
  claims).
- **λ-asymmetry caveat travels (campaign law, W2-A amendment AM-W2-4):** any citation of
  W2's P3 must state that the S_w_raw separation depends on the TTR certification bar
  bounding λ < 1, and that the bag-of-attested-words alternative is excluded by S_b/P1,
  not by S_w_raw.
- **Grid-scoped generator verdicts (campaign law, W3-A amendment AM-W3-1):** a
  generator-certification verdict binds only to the frozen tuning range. W3's verdict is
  "GENERATOR-UNCERTIFIED **on the frozen grid**" (0/54 points, both translits); the
  builder's "cannot be tuned" sentence and its structural-tension explanation are
  STRUCK — the adversary certified the committed generator jointly off-grid at τ ≥ 6000
  with the builder's own unchanged code. The AM-W3-1 obligation (a W3b scoring the
  residue measurands at the certified corridor before W3 may be cited against
  self-citation in any strength) is **DISCHARGED** by W3b.
- **Memory-profile wording (campaign law, W3-A amendment AM-W3-2):** [SUPERSEDED by
  W5 per AM-W5-3 and the W5 DESIGN's pre-committed upgrade text — the gloss now reads:
  **certified multi-distance residue structure (d=1 AND d=2)**, see A13.] Historical
  wording: certified residue at d=1 (A10); d=2 permutation-clear in
  both transliterations but cluster-uncertified (lead, not claim); d ≥ 4 at the plug-in
  bias floor; no cluster-certified long-range residue. "Adjacent-scale only" and
  "cliff" are struck. A10 itself is unamended.
- **Probe-scope discipline (campaign law, W3-A amendment AM-W3-3):** conclusions drawn
  from NOT_PREREG diagnostic scans must state the scanned parameter region explicitly
  and may not assert structural impossibility beyond it; a "structural limitation"
  claim requires either a proof over the parameter space or an adversary-grade dense
  scan.
- **Narrative timestamps (campaign law, W3-A amendment AM-W3-4):** BUILD_LOG event
  timestamps must be captured by `date` at event time, never reconstructed; commit
  hashes + file mtimes remain the authoritative ordering record.
- **S_d2 de-weighting (campaign law, W3b-A amendment AM-W3b-1):** W3b's four S_d2
  MISMATCH units stand as frozen-rule outcomes but are NOT independently citable as
  family failures: (a) d=2 is cluster-uncertified on the real corpus; (b) their
  CI-disjointness leg does not survive basic-bootstrap bias correction; (c)
  obs-magnitude S_d2 is reachable at a certified off-grid memory-heavy corner of the
  same family. Every published statement of the W3b result carries the headline on
  **S_b and S_w only**. Future rounds scoring MI cells with cluster bootstraps must
  report bias (boot mean − obs) and a basic-bootstrap sensitivity line whenever a CI
  leg gates a verdict.
- **Tuning-scope disclosure (campaign law, W3b-A amendment AM-W3b-2):** W3b's "under
  fair tuning as implemented here" must be glossed, wherever cited, as "over the frozen
  144-point grid (p_cont ≤ 0.3); the certified family extends to p_cont ≥ 0.5
  (adversary-verified joint certification at 6 points up to p_cont = 0.7), where S_b
  and S_w still fail by adversary probe (n_ge = 0/60 per translit at
  (24000, .675, .2, .7)) but S_d2 does not." Disclosure, not a reopening obligation;
  claims about the family beyond the probed region are unsupported until run.
  [DISCHARGED for the memory-heavy region by W3c: the spot probe is superseded by the
  preregistered 300-point sweep + the W3c-A strip probes — AM-W3c-1..3 now govern; the
  A12 gloss below carries the binding upgraded text.]
- **ZL d=2 knife-edge disclosure (campaign law, W3b-A amendment AM-W3b-3):**
  [CONTRACTED by AM-W5-3 — no longer travels with the d=2 residue claim; historical
  statement about W3b's delta-method leg only, which W5-A retroactively explains as the
  expected regime at z ≈ 1.5 on a mismatched estimand (AM-W5-1).] Historical wording:
  at folio grain the ZL d=2 delta CI is
  seed-knife-edge (builder seeds CI ∋ 0 at P(≤0) = .064; adversary seeds CI excludes 0
  at P(≤0) = .024); non-certification is carried by IT and by coarser grains
  (section/quire P(≤0) ≥ .085 both translits).
- **Comma-cohesion lead amended & discharged (campaign law, W4-A amendment AM-W4-1):**
  the W2-A comma lead's measurement stands (ZL comma-only boundary table-MI
  S_b = 0.532, adversary re-verified 0.53198) but its cohesion gloss is struck: comma
  junctions sit at LOWER cross-trained pointwise cohesion than hard junctions
  (Δ = −0.167, comma mean 0.724 vs hard 0.891; opposite-tail 1/1001 builder seed and
  1/501 adversary seed, basic CI excludes 0). "MI-hot" is a table-MI
  (distribution-distinctiveness) fact that dissociates from realized cohesion. Any
  future citation of the comma finding must state both quantities. The lead is
  DISCHARGED (tested by W4, resolved negative for the soft-segmentation reading).
- **T2 letter verdict de-weighted; wordless-surrogate control required (campaign law,
  W4-A amendment AM-W4-2):** W4 T2's STRENGTHENED is a correct application of the
  frozen rule and stays in the record AS LETTER ONLY — non-evidential: a wordless
  first-order-Markov surrogate through the identical pipeline reproduces the full S_w
  gain (surrogate G_w ≥ real at builder seeds, adversary seeds, and an independent
  adversary implementation), via within-unit PMI enrichment + (L,i)-strata inflation.
  T2 STRENGTHENED may never be cited without this disclosure; any citation of W4's
  master outcome must carry the robustness-adjusted NEGATIVE reading. Corollary: a
  min-PMI/stratified-S_w exceedance over matched-random is inadmissible as
  segmentation evidence in future rounds without a wordless-surrogate control run in
  the same pipeline.
- **Boundary-independence lead wording (W4-A amendment AM-W4-3):** binding certified
  wording for W4's emergent lead — entered below as B14; cite only in that wording
  and scope (7.7×/8.6× vs matched-random, 5.1×/5.9× vs min-PMI's own boundaries;
  never a blanket "~8×").
- **Ledger prose correction (W4-A amendment AM-W4-4):** IT S_b quotes as **0.17835**
  (exact 0.17835460467460207), not "0.17836" — corrected in A10 and A12 below.
  Committed JSONs remain authoritative over prose everywhere.
- **Pre-run test-code commits (campaign law, W4-A amendment AM-W4-5):** every future
  round commits test code in a pre-run commit (W3b pattern) before any outcome-bearing
  execution; committing tests together with results (as W4 did) is a
  fabrication-screen defect even when — as in W4 — replays fully reproduce.
- **T1b arm-overlap disclosure (W4-A amendment AM-W4-6):** any citation of W4 T1b's
  ZL arm travels with: 88.2% (470/533) of ZL_only contested gaps are comma junctions —
  the ZL arm largely re-tests T1a on the aligned subdomain; the IT arm (274 hard-only
  gaps) is the independent arm and also fails.
- **Estimand history correction (campaign law, W5-A amendment AM-W5-1):** the sentence
  "W3b's per-folio delta was an inefficient estimator of the same pooled quantity" is
  STRUCK wherever it appears or is paraphrased. Binding replacement: "W3b's bootstrap
  leg targeted a DIFFERENT functional (weighted mean of per-folio MI deltas: .00443 ZL
  / .00384 IT on identical tables) than the pooled B13 statistic (.00633 / .00649) — a
  ~1.4–1.7× smaller estimand measured with far higher noise. B13's 'CI ∋ 0' was a
  mismatched, underpowered leg, not evidence about the pooled statistic. W5's bootstrap
  targets the pooled statistic B13 actually quotes (obs bit-identical to W3b T1)."
  Citations of the W5 certification may summarize this as "estimand re-alignment";
  "power artifact" alone is not a permitted summary. Verified functional comparison on
  the SAME committed null tables (adversary, zero seed noise): pooled .006334 ZL /
  .006492 IT vs per-folio-weighted .004430 / .003843 — ratios 1.43× / 1.69×.
- **Coarse-grain disclosure wording (campaign law, W5-A amendment AM-W5-2):** the
  welded quire disclosure becomes: "Certified at folio grain (campaign-law sampling
  unit). At quire grain (18 clusters) the basic CI lower bound is seed-wobbly and can
  dip below 0 (builder −.00004 ZL / −.00064 IT; adversary −.00104 / −.00141); BCa
  remains positive (≥ +.0033) and P(≤0) ≤ .0005 in every coarse-grain stream (≤ 1 of
  12,000 replicates incl. adversary section-grain NOT_PREREG probe at 8 clusters). The
  dip is a right-skewness artifact of the basic interval at small cluster counts, not
  sign uncertainty — and conversely, the basic-CI non-robustness at quire grain must be
  quoted wherever the quire figure travels." Bifolio-proxy and Currier-stratified
  grains pass all intervals (no disclosure).
- **Ceiling scope weld (campaign law, W3c-A amendment AM-W3c-1):** wherever
  CORNER-CLOSED / H-W3c is cited: "closed over the preregistered grid (p_cont ≤ 0.9)".
  The trend sentence "never reaches obs" is STRUCK unless scoped to the grid; binding
  replacement: "within the grid the generator's S_b band never reaches obs; adversary
  NOT_PREREG strip probe (seed 777007, τ {12k,16k,24k} × p_exact {.60–.70} × p2
  {0,.2} × p_cont {.92,.95,.98}) found joint certification persists above the grid
  (2 joint points, singles to p_cont = 0.98) and individual S_b draws cross obs at
  p_cont = 0.95 (n_ge 2/200 ZL, max 0.2089 vs obs 0.19992) while the tail stays
  MISMATCH-level and **S_w remains untouched (n_ge = 0/200 everywhere probed, gen
  p97.5 ≈ 1.12 vs obs 1.395/1.364)** — no probed point survives; claims beyond the
  scanned strip are unsupported." S_w, not S_b, is the binding discriminator at
  extreme memory; closure wording may say so. Ledger corollary: because individual
  S_b draws cross obs at p_cont = 0.95, **S_b alone may not be cited against this
  family above the sweep grid** — above p_cont = 0.9 the exclusion rests on S_w.
- **Ceiling seed wobble (campaign law, W3c-A amendment AM-W3c-2):** "Certified
  ceiling p_cont = 0.9" is a builder-seed statistic: at adversary seed 777007 the
  300-pt grid yields 33 joint points with ceiling 0.8 (overlap 14/38). Citations of
  the ceiling carry "(seed-wobbly ±0.1 at 5 draws/point; region robust at a fifth
  seed set; adversary strip probe certifies to 0.95 jointly)" — cite the certified
  REGION qualitatively, not the point count.
- **p_exact edge disclosure (campaign law, W3c-A amendment AM-W3c-3):** the frozen
  p_exact window .60–.70 does not bracket the corridor: both edges carry joint
  certifications at two seed sets. Adversary probes at .55/.575 (high τ, high p_cont)
  and .725/.75 (low τ) found no joint certification (2 singles at .575), so the joint
  footprint stands as probed; any claim about p_exact outside [.55, .75] × the probed
  sub-region is unsupported.
- **A13/W5 weld strengthening (campaign law, W3c-A amendment AM-W3c-4):** the
  AM-W3b-2-derived weld on W5's d=2 certification upgrades to: "W5's d=2
  certification does not discriminate the memory axis of the recency-to-uniform
  copy+mutate family: the W3c K = 1000 sweep (adversary-verified at seed 777007)
  shows S_d2 crossing obs magnitude at p_cont ≈ 0.7 and overshooting ~3.5× by 0.9;
  d=2 residue constrains memoryless/short-memory mechanisms only."
- **AM-W3b-3 contraction (W5-A amendment AM-W5-3):** the AM-W3b-3 knife-edge disclosure
  no longer travels with the d=2 residue claim: it is contracted to a historical
  statement about W3b's delta-method leg ("the W3b estimator's folio-grain CI was
  seed-knife-edged, as expected at z ≈ 1.5 on a mismatched estimand; superseded by W5,
  where 4 seed sets × basic+BCa concur with margins ≥ +.002 and P(≤0) = 0 at
  B = 16,000 total"). AM-W3-2's memory-profile wording is superseded per the W5
  DESIGN's pre-committed upgrade text: **certified multi-distance residue structure
  (d=1 AND d=2)** — see A13.
- **G1 label rider (campaign law, W6-A amendment AM-W6-1):** W6's G1 line carries the
  frozen label GATE-INFRA-FAILED, but it may never be cited as "the probe was
  inadequate, the segmenter was untested." The probe was adequate (it answered 7/7
  textless patches correctly; ceiling analysis confirmed pre-run). The precondition
  failed because the v1.9 segmenter misclassified drawing/edge ink as removable text,
  placing positive controls on textless spots. Any citation of W6's G1 line must
  state: *positive-control construction was violated by segmenter false-positive
  removals — this is segmenter-defect evidence, not probe-defect evidence.*
- **Round-0 G1 downgrade (campaign law, W6-A amendment AM-W6-2):** Round-0's G1 PASS
  (54/60, bar exactly met) is downgraded to *passed-by-luck*: adversary reconstruction
  proved ≥4 of its 6 positive-control misses were textless placements (the round-1
  defect already active), giving an honest round-0 ceiling of ≤56/60. Consequently
  round-0's leakage numbers (1/60 patch, 0/30 page) are **observations under a
  compromised power precondition** and may not be cited as certified leakage evidence
  for the approach class. (Extends the builder's welded disclosures 1 and 6, which
  are otherwise accurate.)
- **Record correction (W6-A amendment AM-W6-3):** the duplicate-cache disclosure
  undercounts: 25 duplicate-keyed records (not 23), all identical-answer, zero
  conflicts, zero effect on scored counts.
- **Contiguity-preserving null for contiguous-block contrasts (campaign law,
  forward-binding, W7-A amendment AM-W7-5):** for any future preregistered
  contrast whose arms are contiguous codicological blocks (sections, quires,
  gathering runs), folio-exchange permutation is inadmissible as the SOLE
  certifying null: a contiguity-preserving null (exact cyclic rotation or a
  block-resampling equivalent) must be preregistered as a load-bearing prong,
  not merely a knife-edge menu item. (W7's omnibus survives this standard;
  its contrast does not — the gap between the two is exactly what this law
  prevents from recurring silently.)
- **G3 failure decomposition (campaign law, W6-A amendment AM-W6-4, welded to any
  citation of W6's 21/30):** The 9 round-1 unverified cells decompose (adversary
  re-read): 2 genuine segmenter drawing-damage failures (f112r/f112v stars), 3
  annotator errors on intact features, 2 defensible judgment calls, 2 arguable
  verifier misfires (f37v, f51v root-form rejections). The FAIL is robust (max
  charitable flip reaches 25 < 27), but W6's G3 counts measure the annotate→verify
  CHAIN, not segmenter fidelity alone; successor rounds must budget for
  annotator/verifier noise explicitly (see the W6 successor prerequisites).

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

### A10. The character stream carries sequential digram-class structure — within words beyond the slot grammar, AND across word boundaries
Any valid theory MUST reproduce both facets (the campaign's first positive certified
constraint; round W2, adversary-confirmed):
- **Boundary digram residue (W2 P1, PASS):** mutual information between word-final and
  word-initial character classes across adjacent-word junctions S_b = 0.19992 bits ZL /
  0.17835 IT (AM-W4-4), permutation p = 1/1001 both translits (n_ge = 0 at nperm = 1000; null max
  .01333/.01280 — gap to nearest null ≈ 14× the null max), folio-cluster bootstrap CI
  [.145, .184] / [.125, .162], P(≤0) = 0. **AM-W2-1 disclosure (binding, travels with
  this number):** the inherited tokenizer splits on IVTFF uncertain-space commas — 8.02%
  of ZL boundary junctions are commas and they are table-MI-hot (comma-only
  S_b = 0.532 bits — per AM-W4-1 a distribution-distinctiveness fact, NOT high
  cohesion: comma junctions sit at LOWER cross-trained pointwise cohesion than hard
  junctions, Δ = −0.167, reversed at 1/1001; W4), inflating the pooled ZL figure ~14%; the hard-space-only ZL figure is **S_b = 0.1712**
  (still ~12× its own null max .01422, p = 1/1001, n_ge = 0), and IT contains zero comma
  junctions at source yet independently agrees.
- **Within-word positional residue (W2 P2, PASS):** digram MI conditioned on
  (word-length, position) cells — i.e. beyond the positional slot grammar —
  S_w = 1.39542 ZL / 1.36418 IT bits, p = 1/1001 both (null max .04968/.04762),
  folio-cluster bootstrap CI [.742, .816] / [.738, .811], P(≤0) = 0. Adversary
  folio-stratified (folio × length × position) null — which preserves every folio's
  positional unigram profile and kills hand/section/folio mixing as an explanation —
  still gives n_ge = 0/1000 (null max .0855/.0819; folio mixing contributes only
  ~0.035 bits of the pooled statistic).
- GLYPH-domain robustness (prereg'd variant): same direction, same 1/1001 tails
  everywhere; no downgrades.
**Frozen scope (verbatim, binding):** a pass supports "sequential digram-class structure
inconsistent with memoryless independent-draw generation as implemented here" — it does
NOT certify "cipher" or "language"; memory-bearing (self-citation-class) generators are
outside this round's null family. P1's pass means the residue extends ACROSS word
boundaries — the Naibbe-compatible channel is live, not just word-internal structure
(frozen interpretive wording).
- Certified: W2 T1/T2 (P1 PASS, P2 PASS); adversary W2-A recomputed every statistic with
  independent code to ~1e-13, replayed checkpoints bit-identical from the declared
  SeedSequence mapping, and re-ran nulls at disjoint seeds (2000 draws on P1) with
  n_ge = 0 everywhere; comma, line-position (induced-MI bound 0.027; stratified S_b
  *rises* to 0.280/0.250), and Currier/folio kill vectors all fail.
- Evidence: `w2/tests/results/summary.md`,
  `w2/tests/results/T1.json`, `w2/tests/results/T2.json`,
  `w2/ADVERSARY_REPORT.md`.

### A11. The manuscript is NOT the output of the certified memoryless generator family (Rugg grille / Stolfi core-mantle)
Any valid theory MUST NOT model the text as memoryless independent-draw generation of
the certified family: generators certified pre-run on four unigram/word-statistic bars
(H1 ± 0.10 bits, mean length ± 0.50, TTR ± 20% rel, top-100 mass ± 20% rel) — A1
Rugg-style grille at λ = 0.75 ZL / 0.70 IT and A2 Stolfi-style core-mantle at λ = 0.90
both translits, i.e. 70–90% bag-of-attested-words, the STRONGEST memoryless competitors
on unigram statistics — fail to reproduce the observed statistics in all 4 preregistered
cells (generator × statistic), each in both transliterations (8/8 cell × translit
units): every generator-null tail p = 1/1001 with n_ge = 0 for both S_b and the raw
within-word MI S_w_raw (obs 1.66059 ZL / 1.62396 IT), and the observed bootstrap CI lows
(1.63447/1.59840) clear every generator 97.5th percentile (A1: 1.46496/1.40473; A2:
1.36334/1.33550). Verdict **SUPPORTED** per the frozen rule (exact certification level —
not upgraded); master axis **SUPPORTED**; adversary **CONFIRMED** at own seeds (K = 500
fresh corpora per cell, n_ge = 0 in all 8 units), robust up to a λ = 0.95 probe (the
strongest admissible bag-of-attested-words). **AM-W2-4 caveat (binding, travels with any
citation):** the S_w_raw separation depends on the TTR bar bounding λ < 1 (a pure
attested-word bag reproduces the real digram table by construction); the exchangeable
bag-of-attested-words alternative is excluded by S_b/P1, which is the λ-robust
separator. Scope: this certifies exclusion of the certified memoryless generator family
only — not "cipher", not "language"; memory-bearing (self-citation-class) generators
remain untested by this round.
- Evidence: `w2/tests/results/summary.md`,
  `w2/tests/results/T3.json`, `w2/ADVERSARY_REPORT.md`.

### A12. The manuscript is NOT the output of the certified recency-to-uniform copy+mutate family: closed up to p_cont = 0.9 by preregistered sweep, failure extended through the certified strip to 0.95 by adversary probe
Any valid theory MUST NOT model the text as recency-weighted-to-uniform copy+mutate
generation of the certified family (W3's committed SC generator — the Timm & Schinner
"self-citation" lineage: recency-weighted source copying + context-conditional mutation
+ optional phrase continuation; at the certified large-τ corridor the copy kernel is
quasi-uniform, i.e. frequency-preferential copying, so the honest family name is the
**recency-to-uniform copy+mutate family**, not T&S self-citation proper). The family
CAN be tuned to the manuscript's unigram/word-structure surface — a joint certification
corridor at τ ≥ 6000 (same four bars as A11) is certified at **four independent seed
sets** (W3-A adversary 8/144 joint; W3b builder 15/144, τ ∈ {8000: 2, 12000: 4,
16000: 4, 24000: 5}; W3b-A adversary 13/144; replay float-exact) — and tuned, it
**fails to reproduce the certified residue structure** at both selected certified
configurations (SC-fit = SC-freq = (τ=24000, p_exact=.675, p2=.2, p_cont=0); SC-mem =
(12000, .675, .2, .3)), in both transliterations: **12/12 scored units MISMATCH with
n_ge = 0 against K = 1000 generated corpora each** (p_two = 2/1001 everywhere).
Per **AM-W3b-1 the headline rests on S_b and S_w ONLY**: boundary residue S_b obs
0.19992 ZL / 0.17835 IT (AM-W4-4) vs generator bands 0.0052–0.0132 (2.5–97.5%, both configs) —
observed folio-cluster CIs sit ≥ 14× above the generator bands even under
basic-bootstrap bias correction (adversary-verified; ~8–20× across probed configs) —
and within-word residue S_w obs 1.39542 / 1.36418 vs generator bands 0.874–1.184.
The S_d2 cell's MISMATCH stands as a frozen-rule outcome but is not independently
citable (AM-W3b-1: cluster-uncertified on the real corpus, CI leg bias-fragile, and a
certified memory-heavy corner p_cont = 0.7 reproduces its magnitude). **AM-W2-1
travels:** ZL S_b = 0.1999 pooled / **0.1712 hard-space-only** (IT comma-free at
source, 0.1784/0.1789).
**Memory-heavy closure (W3c + W3c-A; A12 gloss upgrade APPROVED-AS-AMENDED —
binding text):** "preregistered W3c sweep: 38 certified points across p_cont 0.4–0.9
(builder seed; 33 points / ceiling 0.8 at adversary seed — region robust, point set
seed-wobbly), S_b and S_w fail at every one (n_ge = 0/1000 per unit; adversary replay
n_ge = 0/500 incl. both p_cont = 0.9 units); certified ceiling p_cont = 0.9 = grid
max, not bracketed above — adversary NOT_PREREG strip probe certifies jointly to
p_cont = 0.95, where S_b single draws reach obs but the tail stays MISMATCH and S_w
remains unbridged (n_ge = 0/200, ~0.25 bits below obs); S_d2 crosses obs magnitude at
p_cont ≈ 0.7 and overshoots beyond — non-discriminating for this family's memory axis
(AM-W3c-4)." The closure claim stands as **"closed up to p_cont = 0.9 by
preregistered sweep, with adversary probes extending the S_b/S_w failure through the
certified strip to 0.95"** — not as an unqualified "everywhere it certifies", since
certification demonstrably continues above the grid (W3c-A F7). Per AM-W3c-1, **S_w
is the binding discriminator at extreme memory** — flat in memory (~0.25 bits below
obs, n_ge = 0 everywhere including the adversary's strip probes) — while individual
S_b draws CROSS obs at p_cont = 0.95 (n_ge 2/200 ZL, max draw 0.2089 ≥ obs 0.19992;
p_two ≈ .03, still MISMATCH): **S_b alone may not be cited against this family above
the sweep grid**. AM-W3c-2 travels (ceiling seed-wobbly ±0.1 at 5 draws/point; cite
the region, not the count). AM-W3c-3 travels (p_exact window .60–.70 does not bracket
the corridor — edges occupied at two seed sets; adversary escape probes at .55–.575
and .725–.75 found no joint escape). Trend, scoped per AM-W3c-1: within the grid the
generator's S_b band rises with p_cont (band hi 0.016 at 0.4 → 0.110 at 0.9; max
single draw 0.148) and never reaches obs; the climb continues above the grid and
begins to touch obs at p_cont ≈ 0.95 without ever bridging S_w.
What the family DOES reproduce (descriptive, never scored): the
repetition texture — ρ_near obs 0.0486/0.0457 sits inside the generator band — i.e.
copy+mutate makes the repeats but not the digram-class residue; memory of the wrong
shape.
**The W3 certification-layer record (honest history, binding wording):** W3's frozen
54-point grid (τ ≤ 1000, the published T&S recency scales) returned GENERATOR-
UNCERTIFIED 0/54 in both translits — mechanically exact, adversary-replayed to float
equality — but the builder's causal headline ("cannot be tuned"; non-overlapping
TTR/top-100 windows; "structural limitation, NOT grid coarseness") was **OVERTURNED by
the adversary (W3-A)**, who found the certification corridor with the builder's own
unchanged code (AM-W3-1). The T&S-recency end of the family (τ ≤ 1000) remains
excluded at the certification layer by the frozen-grid result; the AM-W3-1 showdown
obligation was discharged by W3b. The corpus memory profile (AM-W3-2 wording as
superseded by W5 per AM-W5-3): **certified multi-distance residue structure (d=1 AND
d=2)** — d=1 (A10 re-certified in W3b at a fourth seed set — T1 d=1 PASS, n_ge = 0,
folio-cluster CI [+.164, +.194] ZL / [+.148, +.179] IT, P(≤0) = 0); d=2
folio-cluster-certified by W5 (A13); d ≥ 4 at the plug-in bias floor; no
cluster-certified long-range residue (W3 T1: S_far ZL perm-marginal AND
bootstrap-refuted, IT null).
Scope: this certifies exclusion of the certified recency-to-uniform copy+mutate family
at the residue layer, in this operator-set implementation — NOT "cipher", NOT
"language", NOT "meaning". Mutation operators that preserve boundary-digram statistics
by construction, T&S's exact (paywalled) line-based algorithm, the region beyond the
adversary's scanned strip (p_cont > 0.98; p_exact outside [.55, .75] × the probed
sub-region — AM-W3c-1/-3), and p_cont = 1.0 (degenerate deterministic replay,
excluded by design) are NOT exhausted; the memoryless family exclusion is A11.
- Certified: W3 (frozen grid) + W3-A (corridor discovery, AM-W3-1..4) + W3b (residue
  showdown, 12/12 n_ge = 0) + W3b-A (CONFIRMED-WITH-AMENDMENTS, AM-W3b-1..3; own-seed
  replay n_ge = 0 in every unit at K = 500) + W3c (preregistered 300-pt closure sweep,
  CORNER-CLOSED: 38 certified points × both translits = 76 units, all FAIL S_b and
  S_w with n_ge = 0/1000) + W3c-A (CONFIRMED-WITH-AMENDMENTS, AM-W3c-1..4; fabrication
  clean, float replays 0.0 incl. crash boundary, all-76-unit ckpt recounts exact,
  own-seed showdown n_ge = 0/500, 138-pt NOT_PREREG strip/edge probe). W3c's one
  operational deviation (first cert-gate launch died with its shell before any output;
  relaunched, draw-identical by determinism) was audited and CLEARED (W3c-A F10).
- Evidence: `w3/tests/results/summary.md`, `w3/infra/gen_cert.json`,
  `w3/ADVERSARY_REPORT.md`, `w3b/tests/results/summary.md`,
  `w3b/tests/results/T2.json`, `w3b/tests/results/T1.json`,
  `w3b/infra/gen_cert.json`, `w3b/ADVERSARY_REPORT.md`,
  `w3c/tests/results/summary.md`, `w3c/tests/results/T1.json`,
  `w3c/infra/gen_cert.json`, `w3c/ADVERSARY_REPORT.md`,
  `w3c/adversary/{C_own_seed_cert_grid,D_own_seed_showdown,E_ceiling_edge_probe}.json`.

### A13. Certified multi-distance digram-class residue: d=1 AND d=2 (B13 upgraded; W5 + W5-A)
Any valid theory MUST reproduce digram-class dependence that survives folio-clustered
uncertainty at BOTH distances d=1 and d=2 — the corpus memory profile per the W5 DESIGN's
pre-committed upgrade text: **certified multi-distance residue structure (d=1 AND d=2)**.
The d=2 leg (the B13 statistic, pooled Δ_d2 = MI(pooled d=2 pair table) − mean within-
folio-permuted table MI): obs S_d2 = 0.016749 ZL / 0.016312 IT (37,988 / 37,309 same-folio
row-distance-2 pairs; bit-identical to W3b T1 obs), effect Δ = .006334 ZL / .006492 IT.
Preregistered as a certify-or-kill power round (joint power target ≥ .80; projected .943,
ZL .987 / IT .957) with an armed kill rule — the design was empowered to retire B13 and
certified it instead. Certification record:
- **Permutation-clear at SIX independent seed sets** (n_ge = 0/1000 each, both
  translits): W3 builder, W3-A 777003, W3b builder, W3b-A 777004, W5 builder 20261004,
  W5-A 777006. W5 gap to nearest null +.0041 ZL / +.0047 IT.
- **Folio-cluster bootstrap basic+BCa lower bounds > 0 in FOUR independent seed sets**
  (12/12 builder folio-grain intervals + adversary): three disjoint builder streams
  (primary B = 4000: basic/BCa lo **+.00227/+.00404** ZL, **+.00213/+.00395** IT; rep2
  B = 2000: +.00247/+.00396, +.00204/+.00386; rep3 B = 2000: +.00250/+.00395,
  +.00196/+.00386) plus the adversary's own-seed stream with an independently re-seeded
  null-table layer (B = 4000: basic lo +.00226 ZL / +.00234 IT, BCa lo +.00384/+.00425;
  own effect .006374/.006791, null-table MC noise consistent with the frozen
  m-sensitivity analysis). P(≤0) = 0 in every folio-grain stream — 24,000 replicates
  across builder + adversary. Bias (boot mean − effect) reported and small (≤ +.0003).
- **d=1 control re-certified at every layer** (A10 unamended; 6/6 intervals, n_ge = 0).
- Knife-edge menu never fired (no scored p in [.02, .10]); the AM-W3b-3 knife-edge is
  dead at this design (AM-W5-3).
**Welds that MUST travel with any citation of this fact:**
1. **AM-W3c-4 (strengthened from the AM-W3b-2 weld by W3c + W3c-A):** "W5's d=2
   certification does not discriminate the memory axis of the recency-to-uniform
   copy+mutate family: the W3c K = 1000 sweep (adversary-verified at seed 777007)
   shows S_d2 crossing obs magnitude at p_cont ≈ 0.7 and overshooting ~3.5× by 0.9;
   d=2 residue constrains memoryless/short-memory mechanisms only." (Historical
   AM-W3b-2 wording — the one-corner probe at p_cont = 0.7, n_ge = 0/60 — is
   subsumed by the sweep.) A claim about the corpus, not a new family exclusion;
   NOT cipher, NOT language, NOT meaning.
2. **AM-W5-2 coarse-grain disclosure** (quire basic-CI dip = right-skewness artifact at
   tiny cluster counts; quoted in full above under campaign law).
3. **AM-W2-1 hard-space companion:** d=2 residue restricted to double-hard junction
   pairs is STRONGER: obs 0.022485 ZL (24,533 pairs) / 0.018955 IT (28,019 pairs),
   n_ge = 0 both.
4. **AM-W5-1 estimand history** (W3b's bootstrap leg targeted a different functional;
   "power artifact" alone is a forbidden summary).
Descriptive notes of record: influence audit (NOT_PREREG) — top folio f57v carries
15.6% ZL / 20.1% IT of the effect; dropping the top 10 influencers leaves +.00367 /
+.00346, far above the certified lower bounds — the certification is corpus-broad.
E2 line-null residue (prereg'd descriptive-only, underpowered): effect +.00286 ZL /
+.00356 IT, perm p .006/.003 (n_ge 5/2), folio basic CI ∋ 0 both (−.00142/−.00128),
BCa marginal (+.00012/+.00090), P(≤0) .025/.017 — NOT certified, filed as a
strengthened LEAD only (part of the d=2 residue persists under the stronger within-line
null at the permutation layer). Far distances stay descriptive/unscored: d=4 p .16/.10;
d=8 p .003 ZL / .062 IT (ZL-only weak far tail persists); d=16 p .046 ZL / .879 IT.
Honesty note of record (W5-A F9f, no amendment): in a fixed-corpus power round the
sanctioned pre-freeze power analysis necessarily PREVIEWS the likely outcome
(z ≈ 3.5 ⇒ certification was near-certain before freeze). Disclosed in BUILD_LOG §0;
POWER stream disjoint from every frozen-run stream (adversary-verified); the frozen rule
bound the builder regardless; the real protection is the adversary's independent seeds
and independently re-seeded null-table layer.
- Certified: W5 T1 (CERTIFIED per frozen rules) + W5-A (CONFIRMED-WITH-AMENDMENTS,
  AM-W5-1..3; B13 Tier-A upgrade granted; obs recompute exact with independent MI code;
  builder-seed replay float-exact incl. the crash boundary; own-seed certification
  reproduced).
- Evidence: `w5/tests/results/T1.json`,
  `w5/tests/results/summary.md`, `w5/DESIGN.md`,
  `w5/infra/power_analysis.json`, `w5/ADVERSARY_REPORT.md`,
  `w5/adversary/adv_w5_{A,D,E,F}.json`.

### A14. The certified digram-class residue structure is heterogeneous across section labels — the manuscript is statistically STRATIFIED (W7 + W7-A; separability from Currier INDETERMINATE)
Any valid theory MUST reproduce that the certified sequential residue structure (A10/A13)
is NOT uniform across the manuscript's codicological sections. Certified fact per the
adversary's compile wording: **"the digram-class residue structure is heterogeneous
across section labels (M_b, M_d1; omnibus folio-exchange AND rotation-robust,
Currier-stratification-robust at two seed sets), with the balneo-vs-herbal pairwise
contrast certified under the frozen folio-exchange rule only"** — carrying the AM-W7-1..4
welds verbatim (below). Master verdict: **STRATIFIED (separability from Currier
INDETERMINATE)**. A10/A13's pooled certifications are untouched (W7 measures their
SECTION decomposition, not the pooled facts).
- **T1 omnibus (load-bearing, HETEROGENEOUS):** weighted between-section dispersion Q of
  per-section residue Δ, folio-grain label permutation (nperm = 1000, seed 20261006,
  6 floor sections B/C/H/P/S/Z, 211 pooled folios). M_b: Q = 108.05 ZL / 113.34 IT,
  raw p = .001/.001, n_ge = 0, gap to nearest null 67.6/72.2. M_d1: Q = 101.66/105.36,
  p = .001/.001, n_ge = 0. M_d2 rejects at frozen Holm (.00999 ZL / .003 IT) but is NOT
  independently citable (AM-W7-3). **Rotation-robust** (the load-bearing standard per
  AM-W7-1/-5): under the exact contiguity-preserving cyclic-rotation null, one-sided
  p = .038 ZL / .019 IT (M_b) and .024 / .0095 (M_d1); M_d2 knife-edge in ZL (.0569).
  **Currier-stratification-robust** (T1c, within-Currier label permutation): M_b
  .001/.001, M_d1 .002/.003 at builder seeds; ≤ .004 at adversary seed 777008. M_d2
  collapses under Currier stratification (.617/.542) — per frozen wording it cannot be
  separated from Currier on this corpus.
- **T2 primary contrast (CONTRAST-CERTIFIED under the frozen folio-exchange rule, with
  welds):** balneological − herbal residue difference D, folio-exchange permutation +
  folio-cluster bootstrap (B = 2000, basic AND BCa must exclude 0). M_b:
  D = +.1456 ZL / +.1528 IT, p_two = .004/.002, basic CI [.0996, .1906] / [.1109, .1927],
  BCa [.1035, .1940] / [.1135, .1952]. M_d1: D = +.1046 / +.1077, p_two = .004/.002,
  basic [.0698, .1424] / [.0764, .1396], BCa [.0678, .1402] / [.0731, .1370]. M_d2 null
  (p .735/.533) — the d=2 residue is section-flat, consistent with its small pooled
  magnitude (A13). P(≤0) = 0 and |bias| ≤ .0035 on all certified cells; basic and BCa
  never disagree. Arm-broad, not few-folio: adversary leave-one-balneo-folio-out keeps
  all 19 LOO values positive (min +.1339, dropping f80v); greedy drop-top-3 leaves
  +.121/+.084 ZL and +.1315/+.0912 IT (M_b/M_d1).
- **Per-section ordering (descriptive-with-CIs only):** Δ M_b ZL: B .2855 > S .2506 >
  C .2248 > Z .1830 > P .1441 > H .1399 (IT ordering identical; M_d1 same with S edging
  B). The herbal section — the manuscript's largest — is the LOW end of the residue
  range; balneo and stars/recipes the high end: the pooled corpus statistics (A10) are
  averages over genuinely different section regimes. Per AM-W7-2(c) this ordering must
  carry: "ordering tracks Currier composition (Currier-B-dominated sections high,
  Currier-A low; a pure-hand contrast within herbal reproduces ≈half the B−H gap at
  p .004)". Cross-section comparisons quote CIs (point estimates retain second-order
  size sensitivity).
- **T3 (descriptive, no verdict weight):** balneo-vs-herbal digram-class distribution
  JSD = .1474/.1475 bits vs label-exchange null mean ≈ .029, n_ge = 0/1000 both
  translits; lexicon Jaccard B–H .236/.233 vs B–S .307/.292 — balneo shares more
  vocabulary with stars/recipes than with herbal.
- **Adversary verification (W7-A, CONFIRMED-WITH-AMENDMENTS, seed 777008):** fabrication
  screen clean (design/code/results commit separation; DESIGN untouched after freeze;
  inherited W5→W2 chain unmodified); section map independently re-parsed from the IVTFF
  source — 227 headers, 226 mapped folios, **0 section and 0 Currier mismatches**;
  independent obs recompute of all 36 per-section Δ, 6 omnibus Q, 12 contrasts, and the
  JSD exact to max |dev| 7.1e-14; builder-seed replays float-exact (0.0) for permutation
  draws spanning the crash-resume boundary, null tables, and full B = 2000 bootstrap
  CIs; own-seed replication reproduces every verdict leg (omnibus p = .002 M_b/M_d1;
  T2 p = .004 with basic+BCa excluding 0 both translits).
**Welds that MUST travel with any citation (AM-W7-1..4, verbatim):**
1. **AM-W7-1 (rotation caveat travels; campaign law for this round's citation):**
   T2's CONTRAST-CERTIFIED stands as a frozen-rule outcome (folio-exchange null +
   basic/BCa cluster bootstrap; the knife-edge menu never triggered on a
   load-bearing cell). But every citation of the W7 balneo-vs-herbal
   certification MUST carry: *"not rotation-robust: under the exact
   contiguity-preserving cyclic-rotation null the contrast does not clear .05
   (M_b p_two .068 ZL / .081 IT; M_d1 .081 / .122; adversary-recomputed exactly),
   i.e. it is not distinguishable at .05 from 'some contiguous ~19-folio window
   differs'."* The rotation-ROBUST citable claim from W7 is the T1 omnibus
   heterogeneity on M_b/M_d1 (one-sided rotation p ≤ .038 ZL / ≤ .019 IT).
2. **AM-W7-2 (Currier confound weld; genre wording forbidden):** the T2 arms are
   Currier-unbalanced (balneo 19/19 Currier-B; herbal 95/129 Currier-A). The
   Currier-controlled T2b certifies nothing (ZL M_b Holm .072; ZL M_d1 p .186) and
   every T2b cell fails the rotation item (p_two ≥ .196 — including IT M_b, raw
   p .002). Adversary probes (NOT_PREREG, seed 777008, scanned region = the two
   stated contrasts only): hand-only within herbal (H∩A vs H∩B) D ≈ −.08,
   p_two = .004 in all four M_b/M_d1 cells; section-only at fixed hand
   (B vs S∩Currier-B) null (p_two .22–.34, sign-inconsistent). Binding
   consequences: (a) the W7 contrast may NEVER be cited as a genre/content
   effect — it is a section-LABEL contrast with a demonstrated, large
   Currier-correlated component; (b) "separability INDETERMINATE" is the ceiling
   wording — no citation may lean it toward "section-specific"; (c) the
   per-section ordering B>S>C>Z>P>H must carry "ordering tracks Currier
   composition (Currier-B-dominated sections high, Currier-A low; a pure-hand
   contrast within herbal reproduces ≈half the B−H gap at p .004)".
3. **AM-W7-3 (M_d2 de-weight):** W7's M_d2 omnibus rejection stands as a
   frozen-rule outcome but is NOT independently citable as heterogeneity
   evidence (fails Currier stratification .617/.542; ZL rotation knife-edge
   .0569; contrast null). The W7 heterogeneity headline is **M_b and M_d1 only**;
   "6/6 units reject" may only be quoted with this rider.
4. **AM-W7-4 (C-cell weld):** any citation of the C-section M_d2 (ZL) estimate
   carries *"one-folio-driven: sign flips when f57v — the known W5 top
   influencer — is dropped (+.059 → −.002)"*.
AM-W7-5 (contiguity-preserving null law) is entered above under campaign law and is
forward-binding on all future contiguous-block contrast designs.
Scope (frozen): rejection means section labels carry information beyond folio
exchangeability (and, for M_b/M_d1, beyond the Currier split at the omnibus level).
Genre vs correlated production covariates: only the Currier axis was preregistered;
scribe, folio size, and line geometry remain unmodeled section correlates. Verdicts bind
to the frozen IVTFF $I mapping.
- Certified: W7 T1 (HETEROGENEOUS) + T2 (CONTRAST-CERTIFIED, M_b/M_d1) per frozen rules;
  W7-A (CONFIRMED-WITH-AMENDMENTS, AM-W7-1..5).
- Evidence: `w7/tests/results/summary.md`,
  `w7/tests/results/{T1,T2,T3}.json`,
  `w7/tests/results/NP_rotation.json`, `w7/ADVERSARY_REPORT.md`,
  `w7/adversary/adv_w7_{A,B,C,C2,D,E,F,G,H,I}.json`,
  `w7/infra/section_map.json`.

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
  paired null .024/.016, boot .051/.063). *Reinforced (unchanged) by W7-A: the
  adversary's NOT_PREREG hand-only probe within herbal (H∩A vs H∩B) fires at p = .004
  in all four M_b/M_d1 cells while the section-only probe at fixed hand is null — the
  Currier axis remains UNRESOLVED and load-bearing; the probe certifies nothing about
  it (AM-W3-3 scope).* `wp5/tests/results/summary.md`,
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
  future scribe/hand test.** *Reinforced (unchanged) by W7-A: W7's balneo-vs-herbal
  arms are Currier-unbalanced (19/19 B vs 95/129 A), the Currier-controlled T2b
  certifies nothing, and separability lands INDETERMINATE — hand/section inseparability
  again binds the wording (AM-W7-2).* `wp4/tests/results/summary.md`,
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
- **B13. → UPGRADED TO TIER-A (A13) by W5 + W5-A.** Historical record: entered as
  permutation-clear at four seed sets but folio-cluster-UNCERTIFIED (W3b builder CIs
  ∋ 0: ZL P(≤0) = .064, IT .191). W5's preregistered certify-or-kill power round
  certified the pooled B13 statistic at folio grain in both transliterations
  (adversary-confirmed at a 6th seed set with an independently re-seeded null layer);
  per AM-W5-1 the W3b non-certification was an estimand MISMATCH plus power — its
  bootstrap leg targeted a different, ~1.4–1.7× smaller functional — not evidence about
  the pooled statistic. See A13; AM-W5-1..3 bind.
- **B14. EVA space boundaries are exceptional final→initial class-independence points
  (W4 certified lead; AM-W4-3 binding wording; NOT_PREREG origin,
  adversary-recertified).** Exact wording: "At matched boundary rate and identical
  unit count, EVA space boundaries (hard+comma; ZL/IT) have boundary digram table-MI
  S_b = 0.201/0.179 (hard-only 0.171 ZL) — ~7.7×/8.6× below matched-rate random gap
  placement (1.559/1.534) and ~5.1×/5.9× below the min-PMI cohesion segmenter's own
  boundaries (1.029/1.054). The scribe's spaces mark points of exceptional
  final→initial class INDEPENDENCE, not points of low pointwise digram cohesion (EVA
  gaps' mean cross-trained PMI 0.877/0.905 vs the segmenter's selected −0.695/−0.840).
  Consistent with A10: S_b(EVA) is simultaneously ~12× its label-shuffle null (W2) and
  many-fold smaller than any tested alternative placement. Scope: relative to the
  tested family (matched-rate random; add-one-PMI min-cohesion thresholding),
  cross-trained, both translits; no natural-language reference corpus tested;
  NOT_PREREG origin (W4, direction reversed from prereg), adversary-recertified at
  seed 777005." `w4/tests/results/T2.json`,
  `w4/ADVERSARY_REPORT.md` (F7).

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
  **W6-A certified addendum to the WP9 method constraint (binding wording):**
  *stroke-level separation of the W6 class demonstrably preserves substrate (G2, two
  rounds, 38 distinct held-out pages: median footprint ≈.15 vs WP9's .777, zero
  catastrophic pages, 60/60 page-level drawing retention), but W6 certifies NO leakage
  bound and NO drawing-fidelity bound; classification fidelity is the open failure
  mode (drawing ink misclassified as text; fine drawing detail degraded near text).*
  WP9-A's thin-P1 caveat is untouched (W6 produced no certified leakage evidence to
  replace it — AM-W6-2).
  `wp9/SUMMARY.md`, `wp9/infra/verify_sample_results.json`,
  `wp9/ADVERSARY_REPORT.md`.
- **W6 (U1 revival stage 1 — stroke-level text/drawing separation INSTRUMENT):
  INSTRUMENT-FAILED (terminal) — adversary-CONFIRMED (W6-A,
  CONFIRMED-WITH-AMENDMENTS, AM-W6-1..4).** The stroke-morphology + local-VL-
  arbitration hybrid segmenter (frozen v1.8; the ONE preregistered revision v1.9 =
  exactly the DRAW_GUARD_PRIMARY guard, 13 changed lines, proven **bit-exact-shipped**
  by adversary re-render of f112r — sha256 identical to the committed round-1
  manifest, removal_frac equal to full float precision) failed round-1 G3
  groundedness **21/30 verified vs bar ≥27/30** (definite pool 65), terminal per the
  frozen verdict rule — and the FAIL is **robust to the adversary's most charitable
  re-read: flipping every questionable rejection reaches max 25/30 < 27**. Round-1 G1
  is **GATE-INFRA-FAILED** (patch probe-power 49/60 prompt v1 → 52/60 preregistered
  prompt v2, bar ≥54/60; page power 29/30 passed; honest ceiling 53/60 — 7 of the 11
  prompt-v1 "no" patches are textless, so no prompt could pass the precondition on
  this patch population), carrying the AM-W6-1 rider: *positive-control construction
  was violated by segmenter false-positive removals — this is segmenter-defect
  evidence, not probe-defect evidence* (the patch population was corrupted by the
  segmenter's own misclassification; never citable as exculpating the segmenter).
  Round 0: G1 passed at exactly 54/60 — **downgraded per AM-W6-2 to passed-by-luck**
  (≥4 of its 6 misses adversary-reconstructed as textless placements; honest ceiling
  ≤56/60; round-0 leakage 1/60 patch / 0/30 page are observations under a compromised
  power precondition, NOT citable as certified leakage evidence); G3 failed 25/30
  (pool 66; star-arm thinning on f112r/f112v + annotator errors). AM-W6-4 welds to
  any citation of the 21/30: the G3 count measures the annotate→verify CHAIN (2
  genuine drawing-damage failures, 3 annotator errors, 2 defensible calls, 2 arguable
  verifier misfires), not segmenter fidelity alone. AM-W6-3 corrects the
  duplicate-cache disclosure (25 duplicate-keyed records, not 23; identical-answer,
  zero conflicts, zero scoring effect). No semantic claim of any kind was made; U1/B1
  remain gated on a certified instrument that does not yet exist. Fabrication screen
  CLEAN (commit chain from git alone; all gate counts recompute exactly from committed
  call caches; all seeded draws replay exactly; 30/30 + 30/30 render sha256 verified).
  **CERTIFIED LEAD (W6-A, adversary-granted, scoped wording binding — blanket
  "solved" is forbidden):** *On 38 distinct held-out pages over two seeded rounds,
  the W6 stroke-level segmenter class held removal footprint to median ≈.15 (max .43,
  zero pages >0.60) with 60/60 page-level drawing retention under an
  independent-family probe — versus WP9 dilation-masking's median .777 with 22/171
  pages >90% masked. Substrate* survival *is solved for this approach class;
  substrate* fidelity *(fine drawing detail near text) and removal* targeting
  *(drawing ink misclassified as text) are explicitly NOT solved and are the proven
  failure modes.*
  **Binding prerequisites for any W6-successor instrument round (U1 revival stage-1
  requirements, updating the WP9 constraint):** (1) **Decoupled positive controls** —
  G1 probe-power patches drawn from text locations verified independently of the
  segmenter under test (probe-confirmed on originals, or a frozen text-location
  inventory), never from the segmenter's own removed-component centroids; (2) **a
  drawing-fidelity gate stronger than page-level retention** — a preregistered bar on
  drawing-detail survival (e.g. star-count preservation on S pages, or drawing-ink
  IoU original-vs-removed), since G2b provably passes while star arms are shaved;
  (3) **annotator-noise budget for G3** — an adjudication protocol, a pre-measured
  annotator error rate on TUNE with the bar set net of it, or a multi-annotator
  scheme (3+ of 9 round-1 failures were annotator errors on intact features, which a
  27/30 bar cannot absorb at pool ≈65); (4) **power-precondition margin** —
  probe-power bars passed with margin ≥2 above the bar or replicated on a second draw
  before leakage is scored (the W6 round-0 knife-edge pass is the cautionary
  precedent); (5) **family-separation disclosure** — any VL assist inside the
  segmenter declared at freeze with its family relationship to the G3 annotator
  (W6's Qwen/Qwen overlap was disclosed late, at v1.7–1.8, though verifier
  independence held throughout).
  Welded builder disclosures travel (T-section f1r-class faded ink never gate-tested;
  G1 leakage numbers do not exist for round 1; prompt-v2 ordering after the sealed
  verdict ruled acceptable record-completion, preregistration-before-run verified
  from git).
  `w6/summary.md`, `w6/DESIGN.md`,
  `w6/BUILD_LOG.md`, `w6/gates/g1_result.json`,
  `w6/gates/g1_result_r1.json`, `w6/gates/g1_result_r1v2.json`,
  `w6/gates/g2_result.json`, `w6/gates/g2_result_r1.json`,
  `w6/gates/g3_result.json`, `w6/gates/g3_result_r1.json`,
  `w6/ADVERSARY_REPORT.md`.

---

## Live threads (post-W2)

1. **The one-line-heading question (B1):** opening enrichment beyond the first line is
   permutation-strong but cluster-uncertified at every resampling grain; blind semantic
   heading annotation (U1) — the only identified discharge path — was attempted in WP9
   and exited ANNOTATION-FAILED (instrument failure, claim UNTESTED). Revival is gated
   on stroke-level text/drawing separation (WP9 method constraint); the WP9-A caveats
   (P1-thin, 14/27 domain) travel with any reuse of the masking method. **W6 (stage 1
   of the revival) built and gated a stroke-level segmenter and exited
   INSTRUMENT-FAILED (terminal, adversary-CONFIRMED):** substrate SURVIVAL is
   certified as a lead (median footprint ≈.15 vs WP9's .777, 38 distinct held-out
   pages, two rounds, 60/60 page-level retention — scoped wording in the W6 record;
   substrate fidelity and removal targeting explicitly NOT certified), but
   classification fidelity is the proven failure mode. Any successor stage-1
   instrument round is additionally gated on the five W6-A prerequisites — headlined
   by positive controls decoupled from the segmenter under test and a drawing-fidelity
   gate stronger than page-level yes/no — plus AM-W6-1..4. U1/B1 remain gated on a
   certified instrument that does not yet exist.
2. **The Currier axis (B2/B3): UNRESOLVED** — B-arm non-certifiable both directions; the
   within-H reversal is ZL-solid/IT-thin with a one-folio jackknife caveat. W7
   reinforces without resolving: the residue-stratification contrast is heavily
   Currier-loaded (AM-W7-2; hand-only probe ≈half the B−H gap at p .004, NOT_PREREG),
   and W7's separability verdict is INDETERMINATE — a Currier-balanced or
   Currier-stratified contrast with adequate power (T2b's 148→51-folio domain shrink
   conflates confound control with power loss; B9/WP4-PH1 precedent) remains the open
   design problem.
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
6. **Memory-bearing family: RESOLVED at the residue layer (W3 + W3b + W3c → A12).**
   The recency-to-uniform copy+mutate family (T&S self-citation lineage) certifies on
   the unigram surface across a τ ≥ 6000 corridor and fails S_b/S_w at every certified
   point tested — now closed up to p_cont = 0.9 by the preregistered W3c sweep (38
   certified points, n_ge = 0/1000 × 76 units), with the adversary's strip probe
   extending the failure through the certified strip to p_cont = 0.95, where single
   S_b draws touch obs but S_w stays unbridged (AM-W3c-1: S_w is the binding
   discriminator at extreme memory). Remaining open edges: mutation operator sets that
   preserve boundary-digram statistics by construction; T&S's exact (paywalled)
   line-based algorithm; the region beyond the scanned strip (p_cont > 0.98; p_exact
   outside [.55, .75] × the probed sub-region — AM-W3c-3). The phase-3 self-citation
   result remains deliberately NOT entered — W3/W3b/W3c now carry that question inside
   the certified record.
6b. **d=2 residue promotion (B13): RESOLVED — CERTIFIED (W5 + W5-A → A13).** The
   preregistered certify-or-kill power round (joint power .943 vs ≥ .80 target, armed
   kill rule) certified the pooled d=2 statistic at folio grain in both
   transliterations; six permutation seed sets, four bootstrap seed sets, adversary
   Tier-A upgrade granted. AM-W5-1..3 + AM-W3c-4 (superseding the AM-W3b-2 weld) +
   AM-W2-1 welds travel. Still open
   from this thread: the E2 line-null residue (strengthened lead only — perm p
   .006/.003 but folio CI ∋ 0); a position-conditioned boundary prong (thread 7);
   ZL-only weak far tails (d=8/d=16) remain a descriptive watch item (W5: d8 p .003
   ZL / .062 IT; d16 .046 / .879, unscored).
6c. **Section stratification (W7 + W7-A → A14): RESOLVED at the omnibus layer — the
   residue structure is STRATIFIED across section labels (rotation- and
   Currier-stratification-robust on M_b/M_d1).** Still open from this thread: (a)
   separability of the balneo-vs-herbal CONTRAST from Currier is INDETERMINATE
   (AM-W7-2 caps the wording; genre/content attribution forbidden); (b) the contrast
   is not rotation-robust (AM-W7-1) — a contiguity-aware contrast design satisfying
   AM-W7-5 is the required successor; (c) the d=2 residue is section-flat (contrast
   null, omnibus not independently citable per AM-W7-3) — consistent with A13's small
   pooled magnitude; (d) scribe, folio size, and line geometry remain unmodeled
   section correlates (frozen scope).
7. **Soft word segmentation (W2-A NOT_PREREG lead): TESTED AND DISCHARGED NEGATIVE
   (W4 + W4-A → AM-W4-1..6, B14).** W4 put the lead under preregistration and it lost
   its load-bearing prongs. Master verdict: **MIXED by the frozen letter (T1b FAIL
   blocks POSITIVE; T2 letter-STRENGTHENED blocks NEGATIVE); citable reading NEGATIVE
   per AM-W4-2** — EVA hard-space tokenization SURVIVES its first direct challenge: no
   tested cohesion segmentation beats it, and the challenge machinery's one positive
   leg (T2 STRENGTHENED) is a demonstrated construction artifact (a wordless
   first-order-Markov surrogate reproduces the full S_w gain; non-evidential, never
   citable without the surrogate disclosure). The comma "high-cohesion" gloss is
   struck (AM-W4-1): comma junctions are table-MI-distinctive (0.532 stands) but sit
   at LOWER pointwise cohesion than hard junctions (Δ = −0.167, reversed at 1/1001) —
   the adversary amended and discharged his own W2-A lead. T1b failed in both arms
   with the AM-W4-6 overlap disclosure (88.2% of ZL contested gaps are commas; the
   independent IT arm also fails, CI on the wrong side of 0.5). The emergent certified
   lead is B14 (the scribe's spaces as exceptional class-independence points). Scope:
   the tested family is per-gap add-one PMI with rate-matched global thresholding,
   cross-transliteration/cross-fold trained; richer segmenters (branching entropy,
   higher-order context, Bayesian) are NOT excluded. Still live from W2-A:
   position-conditioning *strengthens* the boundary residue (stratified S_b
   0.280/0.250 vs pooled 0.200/0.178), so a position-conditioned boundary prong
   remains the more powerful future design; folio mixing's share of S_w is quantified
   at ≈ 0.035 bits.

*Compiled from: WP2 (2026-09-18), WP2-A (2026-09-18), WP3 (2026-09-19), WP3-A (2026-09-19),
WP4 (2026-09-23), WP4-A (2026-09-23), WP5 (2026-09-23), WP5-A (2026-09-23), WP6 (2026-09-25),
WP6-A (2026-09-25), WP7 (2026-09-25), WP7-A (2026-09-25), WP8 (2026-09-26), WP8-A
(2026-09-26), WP8b (2026-09-26), WP8b-A (2026-09-26), WP8c (2026-09-26), WP8c-A
(2026-09-26), WP9 (2026-09-26), WP9-A (2026-09-26), W2 (2026-09-29), W2-A (2026-09-29),
W3 (2026-09-29), W3-A (2026-09-29), W3b (2026-09-29), W3b-A (2026-09-29), W4 (2026-09-29),
W4-A (2026-09-29), W5 (2026-09-29), W5-A (2026-09-29), W3c (2026-09-30), W3c-A (2026-09-30),
W6 (2026-09-30), W6-A (2026-09-30), W7 (2026-09-30), W7-A (2026-09-30).
W2 opens the W-series numbering (digram/sequence-structure arc); builder/adversary
structure unchanged, adversary record filed as `ADVERSARY_REPORT.md` at the round root.
Claims from
earlier phases not documented in these round files (e.g. the phase-3 self-citation generator
result) are deliberately NOT entered here — nothing enters the ledger that cannot be
verified against a round evidence file.*

🜂
