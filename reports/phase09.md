# Voynich Phase 9 — replication and decoupling: does the or-/root-prominence link survive a different transliteration, a different alphabet, and the inside of the line?

*2026-09-17 · workstation A · ninth phase. Companions: `phase01.md` (1) through
`phase08.md` (8). Phase 8 closed with the or-×root_prominence correlate
control-hardened within codicology and named the remaining threats:
single-annotator bias, transliteration choice, and the herbal section's
scribe⇄dialect confound. Phase 9 attacked all three. **Run context**: the host
crashed four times across 09-16/09-17 (suspected RAM; a memtester held 32 GB
throughout this run). One work package — the second-annotator VL re-annotation
— was started before the first crash (20/164 folios banked), then deferred by
operator instruction to keep the machine light. Everything else ran to
completion, checkpointed brick by brick.*

## Preregistration

The full test list was fixed in `run_phase9.py`'s docstring before any or-
rate was computed from the new transliterations or any cross-section or- rate
was computed at all. The only data inspected first: (a) the covariate-only
design matrix (scribe × Currier language × section from ZL3b-n.txt IVTFF
headers), needed to fix the decoupling contrasts; (b) all previously published
phase 7/8 results (disclosed prior selections). Confirmatory family, BH-FDR
q=0.05, 20,000 permutations each, seed 20260917:

- **R1/R2** — Takahashi replication: or-(IT) × root_prominence, scribe×quire-
  stratified over all 129 herbal folios (R1) and within Scribe 1 quire-
  stratified (R2).
- **R3/R4** — v101 replication: same two tests with GC (v101 alphabet) oy-
  rates.
- **D1** — decoupling, decisive direction: within **Scribe 3** (the only hand
  that wrote both dialects), Currier A vs B or- share, section-stratified.
- **D2** — decoupling, converse: within **Currier B**, or- share across
  scribes 2/3/5, section-stratified.
- **S1** — slot-aware: line-**medial**-only or- share (first and last token
  of every line removed) × root_prominence, Scribe 1, quire-stratified.
- **D3** (or- × scribe within Currier A) recorded as **structurally
  untestable** stratified — scribe 1's A folios (herbal/pharma/text) and
  scribe 3's A folios (stars) share no section; unstratified version
  exploratory only. Not counted in FDR.

## Data and methods

- **Transliterations**: `IT2a-n.txt` (Takahashi, EvaT, IVTFF 2.0, "extracted
  from LSI_ivtff_0d.txt", voynich.nu/data/) and `GC2a-n.txt` (v101 alphabet,
  IVTFF 2.0, "original file voyn101.txt", voynich.nu/data/), fetched
  2026-09-16/17. Baseline remains `ZL3b-n.txt` (Zandbergen–Landini) used
  since phase 1.
- **Uniform parser** for all three files (whole-page tokens; `[x:y]`→x,
  tags/comments stripped, `@nnn;` extended-glyph escapes and `?`-bearing
  tokens dropped, `!`/`%` fillers removed; ZL/IT lowercased, GC kept
  case-sensitive because v101 capitals are distinct glyphs). ZL re-computed
  under this same simple parser as baseline **B0** so all comparisons are
  apples-to-apples. Coverage: 129/129 herbal folios in all three files.
- **or- in v101**: EVA `r` maps to v101 `y` and EVA `y` to `9`, so EVA `or-`
  = v101 `oy-`. Verified empirically, not assumed: across 20,866
  locus-aligned token pairs (equal-token-count loci only), **85% of EVA or-
  tokens have a v101 counterpart starting `oy`** (259/305); the remainder are
  genuine transcriber disagreements (mostly `Ay`/`ay` = GC reading EVA `a`
  where ZL reads `o`) — exactly the reading variance this replication is
  meant to span.
- Image features: `phase7_features.json` (annotator 1), unchanged. Covariates:
  ZL IVTFF headers ($H scribe / $Q quire / $L Currier / $I section), as in
  phase 8.
- **The decoupling design matrix** (first time computed across the whole
  manuscript, 226 folios): Scribe 1 writes only Currier A (herbal 95, pharma
  16, text 1); Scribes 2 and 5 write only B; Scribe 4's sections carry no
  Currier labels; **Scribe 3 alone writes both** — 22 B and 2 A folios
  (f58r, f58v) inside the same section (stars/S), plus 6 B herbal folios.
  The manuscript offers exactly one same-scribe-same-section dialect
  contrast, and it is 2-vs-22.

## Results

### WP2 — the correlate is not a transliteration artifact (R1–R4: all survive FDR)

| scheme | all 129, scribe×quire strata | Scribe 1 only, quire strata | minor→moderate→dominant means |
|---|---|---|---|
| ZL (baseline B0) | H=18.5, p=8.5×10⁻⁴ | H=10.1, p=4.7×10⁻³ | .0019 → .0104 → .0218 |
| **IT Takahashi** | H=21.0, **p=1.9×10⁻³** | H=9.5, **p=6.7×10⁻³** | .0020 → .0096 → .0230 |
| **GC v101 (oy-)** | H=16.8, **p=1.6×10⁻³** | H=7.9, **p=8.7×10⁻³** | .0054 → .0103 → .0219 |

Two independent transcribers — one using an entirely different glyph alphabet
with different word-boundary decisions — reproduce the association at nearly
identical strength, with the monotone gradient intact, under the maximal
codicological stratification, and inside a single scribe's output. The
transliteration-choice threat named in phases 7 and 8 is retired.

### S1 — the correlate lives in the middle of the line (survives FDR)

Phase 4 showed line-edges carry ornament-like phenomena, and or- overlaps
line-position effects — the last internal artifact candidate. Removing the
first and last token of every line and recomputing or- share on medial tokens
only (Scribe 1, quire-stratified, folios with ≥10 medial tokens):
**H=8.7, p=7.6×10⁻³**, gradient intact (.0027 → .0073 → .0164). The link is
not a property of line boundaries; it sits in the body of the text.

### WP3 — the decoupling tests are null, and honestly so (D1, D2: no FDR)

- **D1** (Scribe 3, A vs B, same section): p=0.60. The two Currier-A folios
  (f58r/f58v) actually sit slightly **higher** in or- (mean .0172) than
  Scribe 3's 28 B folios (.0141) — the *opposite* of what dialect-driving
  predicts — but with n_A=2 the minimum achievable p in this design is ~0.004
  and the observed difference is far from it. Verdict: **no evidence either
  way; the manuscript barely contains the experiment.**
- **D2** (within B: scribes 2/3/5, section-stratified): p=0.17. Descriptively
  the spread is real-looking (scribe 2 .0257 vs scribe 3 .0141 vs scribe 5
  .0123 — or- varies almost 2× *within* dialect B across hands), which if it
  firmed up would favor scribe/campaign over dialect as the carrier — but it
  does not clear stratified permutation. Flagged for replication, claimed as
  nothing.
- **D3** within-A: structurally untestable stratified (no shared section);
  the unstratified exploratory version (p=0.42) is section-confounded and
  uninformative.

### WP1 — second annotator: partial, deferred, and honestly weak so far

20/164 folios were annotated by the blinded instrument-changed pass (same
local VL weights — the only vision stack on the box — but different framing,
schema, scales, and no exposure to text/dialect/hypothesis) before the host
crashed. On the 12 herbal folios among them, Spearman ρ between annotator 1's
root_prominence and annotator 2's underground_parts_emphasis is **0.21
(perm p=1.0)** — no better than chance on this fragment. Range restriction is
severe (11/12 folios are annotator-1 "moderate"/"dominant"), so this is close
to uninformative — but it is **not** a pass, and it means the
single-annotator threat remains fully open. Completion of the 164-folio a2
pass plus pharma/balneo p7-instrument annotation (all 35 images already
downloaded and verified) is the first brick of any phase 10.

### Confirmatory family summary

| test | p | BH-FDR |
|---|---|---|
| R1 IT, all, scribe×quire | 1.9×10⁻³ | ✔ |
| R2 IT, Scribe 1, quire | 6.7×10⁻³ | ✔ |
| R3 GC v101, all, scribe×quire | 1.6×10⁻³ | ✔ |
| R4 GC v101, Scribe 1, quire | 8.7×10⁻³ | ✔ |
| D1 Scribe 3 A vs B | 0.60 | ✘ |
| D2 within-B scribes | 0.17 | ✘ |
| S1 medial-only, Scribe 1 | 7.6×10⁻³ | ✔ |

## Per-brick verdicts

1. **Transliteration replication: PASSED, decisively.** Takahashi and v101
   both reproduce or-×root_prominence under maximal stratification; the v101
   replication crosses an alphabet boundary with an empirically verified
   glyph mapping (85% locus agreement).
2. **Slot-aware re-test: PASSED.** The link survives with line-first/last
   tokens removed; it is not an ornament/line-position artifact.
3. **Cross-section decoupling: UNDERPOWERED NULL.** The manuscript contains
   exactly one same-scribe both-dialects cell (Scribe 3: 2 A vs 22 B folios)
   and it cannot decide scribe-vs-dialect at these effect sizes. The one
   directional hint (A folios high, within-B spread across scribes) leans
   *against* simple dialect-driving, uncorroborated.
4. **Second annotator: DEFERRED (host instability), partial data weak.**
   20/164 banked; the 12-folio agreement fragment (ρ=0.21) is range-restricted
   but not reassuring. This threat is not retired.

## Honest limits

- **Annotator bias is now the load-bearing caveat.** Every FDR survivor in
  this phase reuses annotator 1's root_prominence labels. Phase 9 hardened
  the *text side* of the correlate (two transcribers, two alphabets, line
  interior) but the *image side* still rests on one model's annotations, and
  the partial second-annotator fragment failed to demonstrate agreement.
- The v101 mapping loses 15% of or- tokens to genuine reading disagreements;
  since the replication still succeeds, this variance is evidently not what
  carries the effect — but a token-level sensitivity analysis was not run.
- D1's directional observation rests on two folios (f58r/f58v) and should
  never be quoted without that denominator.
- The medial-token test inherits phase 5's line segmentation and drops folios
  with <10 medial tokens (95 retained); token-position definitions coarser
  than phase 4's full slot grammar.
- All analyses remain per-folio aggregates; no claim reads any word.

## Publication readiness

What this campaign has that would interest Voynich researchers: a
preregistered, FDR-disciplined, fully reproducible pipeline (every script,
seed, and intermediate JSON on disk) establishing one image↔text correlate
that now survives quire/scribe/scribe×quire stratification, holds within a
single scribe, replicates across three transliterations including a different
glyph alphabet, and persists in line-medial text. What it still lacks before
sharing beyond a preprint/forum note: (1) **an independent annotator** —
ideally a human, or at minimum an architecturally different vision model —
re-scoring root prominence blind on all 129+35 folios, with kappa reported;
(2) higher-resolution imagery (the 300×480 px scans bound the feature set);
(3) the pharma/balneo image annotation to give the decoupling question actual
power; (4) a native-format literature check (Stolfi, Reddy & Knight, Bowern
& Lindemann, Davis) to situate or- prominence against known B-language token
gradients and rule out rediscovery; (5) ideally, engagement with the
voynich.ninja community's known criticisms of VL-model annotation. Items 1
and 3 are the same compute job — the deferred WP1 batch — and remain the
single highest-value next action.

## Files

- `run_phase9.py` (preregistration in docstring; uniform parser; all tests)
  → `phase9_results.json`, `phase9_run.log`, per-brick checkpoints
  `phase9_checkpoint_{wp2,wp3,slots,agree}.json`
- `IT2a-n.txt`, `GC2a-n.txt` (voynich.nu/data/, cited above)
- `extract_features9.py` + `phase9_features.json` (partial a2, 20 folios,
  resumable) · `download_folios_phase9.py` → 35 pharma/balneo images in
  `folios/` (verified JPEG, ready for the deferred batch)
- `make_chart_phase9.py` → `phase9_chart.png`, copied to
  `../charts/voynich_phase9.png` (+ caption)

---

# NINE-PHASE CAMPAIGN SYNTHESIS (delta)

| phase | probe | verdict |
|---|---|---|
| 1–6 | text-internal statistics | super-regular template; autocopy falsified; slot grammar; language-shaped lexicon; no reading |
| 7 | images vs text | or- tracks drawn root prominence; drawings track dialect |
| 8 | codicological controls | both findings survive quire control; survivor holds within one scribe |
| 9 | **replication + decoupling** | **or-×root replicates in Takahashi AND v101 (different alphabet), and in line-medial text; transliteration and line-position artifacts retired; scribe-vs-dialect decoupling unanswerable at manuscript-native power (one 2-vs-22 cell); second annotator still owed** |

The correlate has now survived every internal attack the data affords. Its
remaining single point of failure is the annotation instrument itself.

🜂
