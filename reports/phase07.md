# Voynich Phase 7 — Image-Side Feature Pairing: does the vocabulary track the botany?

*2026-09-14 · workstation A · seventh phase of the campaign. Companions: `phase01.md`
(1) through `phase06.md` (6). This is the first phase to use non-textual
evidence — the folio images themselves — and the first to use an LLM anywhere
in the pipeline (a local vision model as a *feature annotator only*; every
statistic downstream of the annotations is classical permutation testing).*

## Question

Phase 6's synthesis named the price of further progress: external constraints.
Phase 7 buys the first one: do herbal folios that share **visual** plant
features (leaf shape, root type, flower presence/color…) also share **word
families** in their text? Any word↔image correlation is an external anchor no
amount of intra-textual statistics could provide.

## 1. Pipeline

- **Images**: all 129 herbal-section folio sides ($I=H in ZL3b-n.txt),
  downloaded folio-keyed from voynich.nu (`_crd.jpg`, 295–352×480 px; Yale's
  IIIF blocks scripted access; archive.org sets lack folio mapping). All 129
  verified JPEG, `folios/`. Bold single-plant line drawings are fully
  judgeable at this resolution (visual spot-check of 4 folios confirmed).
- **Feature extraction**: local Qwen3.8-27B VL (+mmproj), run transiently on
  the second GPU, temperature 0.1, fixed prompt demanding strict JSON with 9
  closed-vocabulary features: leaf_shape, leaf_arrangement, root_type,
  root_prominence, flower_present, flower_color, flower_shape, stem_count,
  plant_count (+ free-text other_notable, unused in stats). 129/129 parsed,
  0 failures (`extract_features.py`, `phase7_features.json`, raw responses
  retained).
- **Reliability**: 10 random folios re-annotated in a second pass.
  Per-feature self-agreement: **0.9–1.0 on all nine features** (leaf_shape
  0.9, root_type 0.9, all others 1.0). All features pass the pre-set ≥0.70
  gate; none excluded.
- **Vision-pipeline sanity (consensus plants)**: extracted features vs the
  7-plant scholarly consensus table from phase 6: **11/13 expected feature
  checks match** (e.g. f1v belladonna: broad leaves + flower ✓; f9v viola:
  flower color in {purple,blue,yellow} ✓; f15v Paris quadrifolia: whorled
  arrangement + single stem ✓). Misses: f2v root_type (drew "other" vs
  expected rhizome-class), f16r Cannabis leaf_shape ("lobed" vs
  compound/spiky — defensible for the drawing). The annotator sees what
  scholars see.
- **Text side**: per-folio word-family profiles from the phase-5 line
  corpus (herbal lines only; 3–165 tokens/folio). Families = top-30
  two-glyph prefixes in herbal text + the named phase-5 families (cth-,
  kch-, dch-, qoke-, oteo-, lk-, ol…dy) = 37 families.

## 2. Global association matrix — one cell survives

For every feature × family pair: Kruskal–Wallis H of family token-share
across feature categories (categories with <4 folios merged), permutation
p (feature labels shuffled across folios; 2,000 perms globally, all cells
with p≤0.02 re-run at **50,000 perms**), Benjamini–Hochberg FDR at q=0.05
over all **333 tests**.

**Result: exactly one cell survives FDR — `root_prominence × or-`**
(H=18.4, p=8×10⁻⁵). The or- token share of a folio's text rises
monotonically with how dominant the root is in the drawing:

| root drawn as | folios | mean or- share |
|---|---|---|
| minor | 9 | 0.002 |
| moderate | 75 | 0.010 |
| **dominant** | **44** | **0.022** |

Robust to leave-one-out (H 17.3–20.2 over all single-folio drops).
Runners-up that did **not** survive FDR: root_prominence×cth- (p=4.2×10⁻⁴,
just misses the rank-2 threshold; cth- is *lower* on dominant-root folios),
flower_present×cth- (p=1.3×10⁻³; the herbal-locked cth- family is ~1.8×
richer on **flowerless** folios), flower_color×cth- (p=2.5×10⁻³).

### The mandatory dialect control

Phase 5's lesson: everything herbal is confounded with Currier A/B. Indeed
**the drawings themselves track dialect**: dominant roots appear on **66%
of Currier-B herbal pages vs 23% of A** (χ²=20.3, permutation p=2.5×10⁻⁴)
— see §4. Since or- is B-enriched (share 0.026 in B vs 0.010 in A), the
pooled association partly rides the dialect. Controls:

- **Stratified permutation** (labels shuffled *within* dialect):
  p = 1.0×10⁻³ — survives.
- **Within Currier A alone** (n=95): H=10.05, p = 4.2×10⁻³ — survives.

Honest framing: under a *fully stratified* family-wide analysis, p=10⁻³
would not clear the 333-test FDR bar on its own. What we have is a
selection (pooled FDR) followed by a targeted confirmation (stratified
p=0.001, within-A p=0.004): **a real but modest association, needing
replication** (other transliteration, held-out annotator) before it is
load-bearing.

## 3. Folio-similarity alignment (Mantel) — null

Do folio pairs with similar drawings have similar word profiles overall?
Visual distance = feature-mismatch share (all 9 features); text distance =
cosine on √-frequency family profiles; Spearman Mantel, 20,000 perms:

**r = 0.045, p = 0.114 — null.** Whatever links image to text is not a
broad "similar plants → similar vocabulary" effect; it is concentrated in
specific features (root prominence) and specific families (or-), below
Mantel's sensitivity.

## 4. The unplanned finding: the pictures know the dialect

Feature × Currier-language tests (χ², 20k perms, herbal A vs B):

| feature | χ² | p |
|---|---|---|
| **root_prominence** | 20.3 | **2.5×10⁻⁴** |
| flower_present | 6.6 | 0.010 |
| root_type | 7.4 | 0.29 |
| leaf_shape | 4.2 | 0.68 |

Currier-B herbal pages systematically carry more root-dominant, more
flowerless drawings. The A/B split — defined purely from *text* statistics
in the 1970s — is visible in what was *drawn*. This joins phase 5's "two
parameter settings of one machine" finding from the outside: whatever
distinguishes A from B extended to illustration emphasis, consistent with
different production campaigns, sources, or subject matter — not merely a
scribal spelling habit.

## 5. What phase 7 adds

1. **First external correlate of the campaign**: a word family (or-) tracks
   a drawn feature (root prominence) at FDR-surviving strength, direction
   monotone, surviving dialect stratification at p≈10⁻³. Consistent with —
   not proof of — content-bearing text (e.g. root-related vocabulary on
   root-focused pages). A generator model must now explain why its output
   statistics correlate with the *pictures*.
2. **The dialect is painted, not just written**: root-dominant drawings
   concentrate in Currier B (p=2.5×10⁻⁴).
3. **cth- (the herbal-locked family) leans toward flowerless folios** —
   suggestive, did not survive FDR; flagged for replication only.
4. **No broad image↔text similarity structure** (Mantel null): the linkage
   is feature-specific, not global.
5. **Decipherment claims: still zero.** Nothing here reads a word.

## Caveats (honest)

- Vision annotations come from one model at one resolution; despite 0.9–1.0
  self-agreement and 11/13 consensus-plant sanity, a systematic annotator
  bias correlated with page *style* (e.g. B-pages drawn differently overall)
  cannot be fully excluded. Human-annotated replication (or a second,
  architecturally different VL model) is the needed follow-up.
- 327×480 px scans; subtle features (leaf serration, small flowers) are at
  the annotator's perceptual floor — features used here are coarse by design.
- Text profiles on 3–165 tokens/folio are noisy; Kruskal–Wallis on shares
  handles this but power is limited — absence of other survivors is weak
  evidence of absence.
- The or- family is a 2-glyph prefix class (includes or, orain, oraiin…);
  "or-" also overlaps line-position phenomena from phase 4. A slot-aware
  re-test would sharpen this.
- Selection-then-confirmation p-values (§2) are stated as such; the fully
  stratified family-wide analysis yields no FDR survivor.

## Files

- `download_folios.py` → `folios/` (129 JPEGs, ~6 MB)
- `extract_features.py` (VL extraction, checkpointed/resumable) →
  `phase7_features.json` (features + rerun + all raw responses),
  `phase7_extract.log`
- `run_phase7.py` (reliability, association+FDR, Mantel, consensus) +
  `run_phase7_refine.py` (50k-perm refinement, stratified controls) →
  `phase7_results.json`, `phase7_mantel.npz`
- chart: `make_chart_phase7.py` → `../charts/voynich_image_pairing.png`

---

# SEVEN-PHASE CAMPAIGN SYNTHESIS

| phase | probe | verdict |
|---|---|---|
| 1 | BPE / morphology | words from a super-regular template |
| 2 | word-order MI | weak, non-prose sequencing; repetition enriched |
| 3 | self-citation generator | autocopy **falsified** |
| 4 | slot grammar | 15 slots, dense words, line = record, ornament layer |
| 5 | embedding geometry | language-shaped topical lexicon; alignment null (calibrated) |
| 6 | labels vs drawings | labels a distinct register; weak page anchoring; plant-name pairing null |
| 7 | **images vs text** | **or- tracks drawn root prominence (FDR-surviving, dialect-robust at p≈10⁻³); drawings track Currier dialect; Mantel null; still no reading** |

The campaign's end-state improves by one increment: the text is now known to
correlate — narrowly but externally — with what is drawn beside it. That is
the single hardest fact yet for any pure-generator account, and the first
brick of the "external constraints" wall that phases 5 and 6 said all future
progress must be built from. The next bricks, in order of value: human or
second-model replication of the root/or- link; slot-aware re-test; v101
transliteration replication; and a root-focused micro-study (do the or-
tokens on root-dominant pages sit in particular slots/lines?).

🜂
