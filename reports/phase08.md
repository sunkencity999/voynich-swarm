# Voynich Phase 8 — confound, scribal, sectional, or content? Attacking the dialect↔drawing link directly

*2026-09-16 · workstation A · eighth phase. Companions: `phase01.md` (1) through
`phase07.md` (7). Phase 7 left two loaded facts on the table: (a) one
FDR-surviving image↔text correlate (root_prominence × or-, pooled p=8×10⁻⁵,
dialect-stratified p=1.0×10⁻³); (b) the drawings themselves track Currier
dialect (dominant roots on 66% of B vs 23% of A herbal pages, p=2.5×10⁻⁴).
Phase 8 asks what (b) actually *is* — and whether (a) survives the strongest
codicological controls available.*

## Covariates and their source

- **Scribes**: Lisa Fagin Davis's five-scribe attributions, as encoded in the
  `$H` variable of `ZL3b-n.txt` (IVTFF 2.0). voynich.nu's transliteration page
  states the ZL file includes "LFD hands in variable `$H`" (voynich.nu/transcr.html,
  fetched 2026-09-16); Davis 2020, *"How many glyphs and how many scribes?"*,
  Manuscript Studies 5(1), is the underlying attribution. No re-keying was
  needed — the mapping ships in the transliteration we have used since phase 1.
- **Quire** (`$Q`) and **page-in-quire** (`$P`): same IVTFF headers.
- Image features: `phase7_features.json` (local VL annotation of all 129
  herbal folios, phase 7; reliability 0.9–1.0). No re-annotation.
- 129 folios with features + text + headers; 127 with a Currier A/B label
  (f65r/f65v are unclassified, Scribe 3, quire H).

## The structural fact that frames everything

**Scribe and dialect are perfectly confounded in the herbal section.**
Crosstab of the 129 folios:

| | Scribe 1 | Scribe 2 | Scribe 3 | Scribe 5 |
|---|---|---|---|---|
| Currier A | **95** | 0 | 0 | 0 |
| Currier B | 0 | **20** | 6 | 6 |
| unlabeled | 0 | 0 | 2 | 0 |

There is zero within-scribe dialect variance. "Does drawing content predict
dialect *beyond scribe*?" is therefore **formally unanswerable on herbal
folios** — not by lack of power but by design-matrix singularity, and this is
itself the phase's first finding: in this section, *scribe*, *dialect*, and
(as phase 7 showed) *illustration emphasis* are one partition observed three
ways. Quire is the only covariate that cuts across it: quires D, E, F, G, Q
contain both dialects (74 of 127 labeled folios sit in mixed quires).

## Preregistered tests

The full list was fixed in `run_phase8.py`'s docstring before running.
Confirmatory family (BH-FDR q=0.05 over the 7 runnable tests; 20,000
permutations each; C2 recorded as untestable, not counted):

| # | test | stat | p | FDR |
|---|---|---|---|---|
| C1 | dialect ~ root_prominence, **stratified by quire** (n=127) | χ²=20.3 | **2.5×10⁻⁴** | ✔ |
| C2 | dialect ~ root_prominence \| scribe | — | untestable (perfect confound) | — |
| C3 | scribe {2,3,5} ~ root_prominence within B (n=32) | χ²=3.8 | 0.217 | ✘ |
| C4 | quire ~ root_prominence within Scribe 1 (n=95) | χ²=25.3 | 0.380 | ✘ |
| C5 | or- share ~ root_prominence \| **scribe** (n=129) | H=18.4 | **1.3×10⁻³** | ✔ |
| C6 | or- share ~ root_prominence \| **quire** (n=129) | H=18.4 | **1.5×10⁻⁴** | ✔ |
| C7 | or- share ~ root_prominence \| **scribe × quire** (n=129, 17 strata) | H=18.4 | **1.1×10⁻³** | ✔ |
| C8 | or- share ~ root_prominence **within Scribe 1 only**, \| quire (n=95) | H=10.0 | **3.9×10⁻³** | ✔ |

Exploratory family (separate FDR): E1 = full 9-feature × 37-family matrix
within Scribe 1, quire-stratified; E2 = same within Scribe 2 (n=20) plus an
honest power simulation. Descriptive (no FDR): logistic regression
dialect ~ root_dominant + quire dummies on the 74 mixed-quire folios.

## Results

### 1. The drawing→dialect link is not a quire artifact (C1)

Shuffling root-prominence labels *within quires* — so only the five mixed
quires contribute — leaves the association intact: **p = 2.5×10⁻⁴**. The
descriptive logistic agrees: with quire dummies in the model, a
dominant-root drawing still carries **β = 2.03** (odds ratio ≈ 7.6) for
Currier B, LRT χ²₁ = 14.2, p = 1.6×10⁻⁴. Inside the very same gatherings,
the B-dialect pages are the root-dominant pages.

### 2. …and it lives exactly at the A/B boundary, at no finer grain (C3, C4)

- Within Currier B, the three scribes (2/3/5) do **not** differ in root
  prominence (p=0.217; n=32, so only a large effect would have been seen).
- Within Scribe 1's 95 folios, root prominence does **not** vary by quire
  (p=0.380).

The visual signal is not "scribe 2 draws differently from scribe 3" and not
"later gatherings drift" — it is concentrated at the same single boundary
that separates the dialects (which is also the Scribe-1/rest boundary).
Confound, scribal, sectional, or content? The testable options thin out:
**not sectional (quire) at either level; not scribal below the A/B split;
the A/B split itself cannot be decomposed into scribe-vs-dialect here.**

### 3. The phase-7 survivor holds under every available control (C5–C8)

The single most important numbers of the phase:

- or- × root_prominence, permuted within **scribe** strata: **p = 1.3×10⁻³**
- within **quire** strata: **p = 1.5×10⁻⁴**
- within **scribe × quire** cells (17 strata — the maximal control this
  design admits): **p = 1.1×10⁻³**
- **within Scribe 1 alone** (one hand, one dialect, n=95), additionally
  quire-stratified: **H = 10.0, p = 3.9×10⁻³**

All four survive BH-FDR across the confirmatory family. The effect is
monotone inside Scribe 1 just as it is pooled (mean or- share:
minor 0.0019 → moderate 0.0090 → dominant 0.0152; pooled
0.0019 → 0.0104 → 0.0219). Whatever links or- vocabulary to drawn root
prominence, it is **not** carried by scribe identity, dialect membership,
or position in the codex: it operates *within* the output of a single
scribe writing a single dialect.

### 4. Exploratory: within-scribe image↔text structure (E1, E2)

- **E1 (Scribe 1, 333 quire-stratified tests): no FDR survivor.** Min
  p = 0.0041 — and reassuringly the top-2 cell is root_prominence × or-
  itself (p=0.0042, matching C8's independent run). Other near-misses
  (leaf_arrangement × ck- p=0.0041, leaf_arrangement × op- p=0.0052,
  root_prominence × oteo- p=0.0062) are noted for future replication only.
  With 333 tests, the BH rank-1 bar is p ≤ 1.5×10⁻⁴; the design lacks the
  power to clear it for effects of this size within one scribe — expected,
  since even the pooled survivor sat at 8×10⁻⁵ with 129 folios.
- **E2 (Scribe 2, n=20): no FDR survivor** (min p=9.5×10⁻⁴,
  stem_count × dy-, uncorrected). **Power simulation**: planting the pooled
  or-×root effect into scribe 2's actual category mix (14 dominant /
  6 moderate) yields detection at α=0.05 only **26.4%** of the time
  (500 sims). A null here is nearly uninformative; stated as such.
  Notably root_prominence × or- within scribe 2 is untestable in the
  interesting direction anyway — scribe 2 has no minor-root folios.

## What phase 8 settles

1. **The dialect↔drawing link did not collapse.** It survives the sharpest
   independent control available (quire, p=2.5×10⁻⁴) and cannot even in
   principle be reduced to "scribe habit vs dialect" in this section because
   the two are one partition. The honest taxonomy: **not a quire/sectional
   confound; scribal-vs-linguistic is undecidable on herbal data; consistent
   with two production campaigns that differed jointly in hand, spelling
   system, and illustration emphasis.**
2. **The or-×root_prominence correlate is now control-hardened.** It holds
   within a single scribe writing a single dialect, stratified by quire
   (p=3.9×10⁻³), and under scribe×quire stratification of the full corpus
   (p=1.1×10⁻³). After phase 8 the confound space for this association is
   essentially exhausted *within this annotation set*: what remains is
   annotator bias (needs a second annotator) and transliteration choice
   (needs v101 replication) — not codicology.
3. **Drawings do not distinguish scribes within B, or quires within A** —
   the illustration signal is specific to the A/B boundary, adding weight to
   "two campaigns" over "gradual drift".
4. **Decipherment claims: still zero.** Nothing here reads a word.

## Honest limits

- **The central untestability is a limit, not a result to over-read**: with
  herbal folios only, "content-driven" and "campaign-driven" (scribe+dialect+
  style moving together) remain observationally equivalent for the *dialect
  link*. Cross-section tests (pharma/balneo folios, where Davis scribes and
  Currier languages decouple partially) are the only way forward on that
  question — noted as the next external brick.
- C3 (n=32) and E2 (n=20, power 0.26) nulls are weak evidence of absence.
- Image annotations still come from one vision model at one resolution
  (phase-7 caveat stands in full). A page-style bias correlated with the A/B
  boundary would produce C1 spuriously — though it would *not* explain C8,
  which lives entirely inside Scribe 1's stylistically homogeneous pages.
- The logistic regression is descriptive (74 folios, possible quasi-separation
  tamed by ridge 10⁻⁶); permutation tests carry the inference.
- Selection history: root_prominence×or- was *selected* by phase 7's pooled
  FDR and *confirmed* here under controls preregistered before running —
  the standard selection-then-confirmation caveat applies once, not twice.

## Files

- `run_phase8.py` (preregistered test list in docstring; covariate parsing,
  stratified permutation machinery, logistic LRT, power sim) →
  `phase8_results.json`, `phase8_run.log`
- `make_chart_phase8.py` (hand-built SVG → cairosvg) → `phase8_chart.png`,
  copied to `../charts/voynich_phase8.png` (+ caption `.txt`)

---

# EIGHT-PHASE CAMPAIGN SYNTHESIS (delta)

| phase | probe | verdict |
|---|---|---|
| 1–6 | text-internal statistics | super-regular template; autocopy falsified; slot grammar; language-shaped lexicon; no reading |
| 7 | images vs text | or- tracks drawn root prominence; drawings track dialect |
| 8 | **codicological controls** | **both phase-7 findings survive quire control; the survivor holds within a single scribe (p=3.9×10⁻³); scribe⇄dialect is one partition in herbal — drawings, hands, and spelling all change together at one boundary, like two production campaigns** |

The campaign's hardest fact got harder: the or-/root-prominence link now has
no codicological escape hatch. Next bricks, in value order: second annotator
(human or architecturally different VL model); v101 transliteration
replication; cross-section scribe/dialect decoupling test; slot-aware re-test
of or- position on root-dominant pages.

🜂
