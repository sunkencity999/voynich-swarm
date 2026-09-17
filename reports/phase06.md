# Voynich Phase 6 — Illustration-Anchored Label Pairing

*2026-09-14 · workstation A · final phase of the six-phase campaign. Companions:
`phase01.md` (1: BPE morphology), `phase02.md` (2: word-order MI),
`phase03.md` (3: self-citation falsified), `phase04.md` (4: slot
grammar), `phase05.md` (5: embedding geometry + section families).
Python stdlib + numpy; matplotlib (uvx) for the chart. No LLM calls in any
statistic. Code: `phase6_lib.py`, `run_phase6.py` (orchestrator),
`run_phase6_step{1,2,2b,3,4,4b}.py`; checkpoints `phase6_*.json`.*

## Question

The IVTFF transliteration distinguishes **labels** — isolated words written
next to drawing elements (plants, jars, stars, nymphs, zodiac figures) — from
running paragraph text. A label plausibly *names* the thing drawn beside it.
Phase 6 asks: do labels behave like names, do they talk to their pages' text,
and can any label be pinned to a scholarly-identified referent?

## 1. Label census (IVTFF 2.0 locus types, ZL3b-n)

Locus format `<folio.num,XTT>`; TT = type. P0/P1/Pb/Pc/Pr/Pt = paragraph
text, Ca/Cc/Ri/Ro = circular/radial, and the label types (IVTFF 2.0 spec,
voynich.nu/software/ivtt/IVTFF_format.pdf): L0 (no clear drawing element),
La (astro element), Lc (**pharma container**), Lf (**pharma herb fragment**),
Ln (**nymph**), Lp (large plant), Ls (**star**), Lt (tube/tub), Lz
(**zodiac element**), Lx (extraneous — excluded).

| | count |
|---|---|
| total loci | 5,385 |
| paragraph loci | 4,130 (35,063 words) |
| **label loci** | **1,026 (1,169 words; 828 types)** |
| circular/radial loci | 226 (2,705 words) |

By type: Lz 299, L0 297, Lf 194, Ls 76, Ln 63, Lt 47, Lc 40, La 7, Lp 3.
By section: zodiac 299, pharma 234, cosmo 172, astro 116, balneo 116,
text-page rosettes 58, herbal 31. 86% of label loci are a single word;
139 label types repeat (480 tokens) — most labels are hapax-like, exactly
what a naming vocabulary over many distinct referents predicts (contrast:
running-text top word `aiin` n=471).

## 2. Labels are a morphologically distinct register

Same slot grammar (phase 4 parser), labels vs paragraph words:

| | labels | paragraphs |
|---|---|---|
| n | 1,169 | 35,063 |
| mean length | 5.17 | 4.93 |
| slot-parse rate | 0.79 | 0.94 |
| **Q slot filled** | **1.2%** | **15.6%** |
| AOY filled | 70.6% | 46.8% |
| BENCH1 filled | 11.5% | 30.1% |
| GALL filled | 56.7% | 48.2% |

First-2-glyph family enrichment (binomial z vs corpus share, n≥30):

| label-enriched | z | | label-avoidant | z |
|---|---|---|---|---|
| ot- (200/2056) | +16.7 | | **qo- (10/5193)** | **−12.4** |
| ok- (186/2227) | +13.7 | | che- (22/2634) | −6.9 |
| of- (25/87) | +8.9→13.5 | | she- (10/1783) | −6.4 |
| op- (54/361) | +12.6 | | sho- (3/742) | −4.4 |
| oe- (22/119) | +9.4 | | cho- (23/1574) | −4.0 |
| os- (11/52) | +7.3 | | lk- (2/418) | −3.2 |

**Labels nearly forbid `q-` (the qo- prefix is 15% of running text but 0.9%
of labels) and shun bench-initial (ch/sh) words; they favor
o+gallows (ot-/ok-/op-/of-) openings.** This confirms and quantifies a
classic observation (labels as a distinct "register") and dovetails with
phase 4's finding that `q-` participates in the line-internal
suffix→prefix chaining: **q- is connective tissue, and labels — words with
no neighbors — don't need it.** The lower parse rate (0.79) also means
labels are where the slot grammar breaks most often: rare/gnarled forms
concentrate in labels, as proper names do in real text.

### Phase-5 families: locked ≠ label-heavy

The phase-5 section-locked families (cth-/kch- herbal, lk- recipes, qoke-
pharma) are **not** the label vocabulary: the top-20 section-locked words
have label share 0.9% and the top-20 section-flat function words 1.7%, both
*below* the 3.2% corpus base rate; `lk-` and `qo(ke)-` are actively
label-avoidant. **Section-locked families live in running text; labels draw
on a third, o+gallows-fronted vocabulary.** The simple story "section-locked
family = names of the things drawn" is dead — whatever the cth-/lk-/qoke-
families encode, it is a property of the *discourse* of those sections, not
of the labelled objects.

## 3. Label→page anchoring — the headline statistic

Does a page's label word also occur in that page's running text (paragraphs
+ circular/radial loci), more than chance? Null: label sets permuted across
label-bearing pages *within the same section* (20,000 perms).

| scope | n label words | same-page rate | null | z | p |
|---|---|---|---|---|---|
| **pooled** | **1,166** | **0.155** | 0.126 ± 0.011 | **+2.6** | **0.007** |
| cosmo | 215 | 0.223 | 0.130 | +2.0 | 0.085 |
| zodiac | 350 | 0.129 | 0.109 | +1.5 | 0.092 |
| astro | 151 | 0.086 | 0.066 | +0.8 | 0.31 |
| balneo | 126 | 0.254 | 0.240 | +0.7 | 0.32 |
| **pharma** | **243** | **0.082** | 0.080 | +0.2 | 0.50 |
| herbal | 26 | 0.346 | 0.221 | +1.2 | 0.08 |

(Restricting to words of length ≥3 gives the same picture: pooled z=2.4,
p=0.016.) **Verdict: labels are anchored to their pages, but weakly.** A
~23% relative enrichment over null at z≈2.6 is real yet small; and the
section detail is telling — the signal comes from the *cosmological/zodiac*
material, while **pharma jar/ingredient labels show zero same-page
anchoring**: the words on the jars essentially never appear in the recipes
written beside them. If labels name ingredients and paragraphs discuss
them, pharma is where anchoring should be strongest. It is absent. Either
labels are not names of the discussed things, or the running text
systematically re-encodes words when they enter sentence context (cf. the
q- connective and phase 4's positional slots — a word could legitimately
change surface form between isolation and text). Both readings survive;
naive same-form anchoring does not.

## 4. Within-page label structure — a naming system's signature

If ~30 nymph/star labels around one zodiac wheel name stars of one
constellation, labels *within* a folio might share structure. Mean pairwise
normalized edit distance + shared-prefix rate, within-folio vs across-folio,
permutation null (10k):

| group | n words | pages | Δ edit-dist (within−across) | z | Δ prefix2 share | z |
|---|---|---|---|---|---|---|
| **zodiac Lz** | 341 | 12 | **−0.040** | **−14.3** | **+0.040** | **+8.1** |
| astro Ls (stars) | 80 | 4 | −0.047 | −5.9 | +0.013 | +1.0 |
| pharma Lf+Lc | 240 | 15 | −0.015 | −3.4 | +0.018 | +2.9 |
| balneo Ln+Lt | 115 | 10 | −0.005 | −0.5 | +0.009 | +0.6 |

**Zodiac label sets are strongly folio-coherent** (p<10⁻⁴ on both metrics):
the ~30 labels around one sign share glyph material with each other far
beyond what the zodiac label lexicon as a whole predicts. Star labels do
too. This is exactly the signature of a *systematic naming scheme with a
per-page (per-constellation) component* — e.g. star names sharing a
constellation element, or serial designations. Balneo nymphs show nothing:
nymph labels are not page-systematic. (Caveat: a scribe generating
variations-on-a-theme per page produces the same signature; this test
cannot distinguish naming from local generation, but it firmly rejects
"labels drawn i.i.d. from the section lexicon.")

## 5. Consensus plant-ID pairing — the decisive-if-it-works part: **null**

Consensus set — only folios where ≥2 independent identifications agree
(ZL3b-n per-page annotations preserving Petersen/O'Neill/Holm/Zandbergen
IDs, vs Sherwood & Scott, edithsherwood.com/voynich_botanical_plants/):

| folio | consensus ID | sources |
|---|---|---|
| f1v | Atropa belladonna | Petersen (ZL: "atropa belladonna…Fuchs p.398") + Sherwood |
| f2r | Centaurea (knapweed) | Holm (ZL) + Sherwood (C. diffusa) |
| f2v | Nymphoides (water-lily type) | Zandbergen (ZL: "Nymphoides Peltata") + Sherwood |
| f9v | Viola tricolor | O'Neill/Petersen ("Herba Trinitatis", "RZ: Viola allright") + Scott/Sherwood |
| f15v | Paris quadrifolia | O'Neill (ZL) + Sherwood |
| f16r | Cannabis | ZL ("Canabis, Hemp") + Sherwood |
| f17v | Dioscorea/Tamus communis | ZL ("Tamus communis…Smilax") + Sherwood (Dioscorea) |

Candidate "name" = first word of the folio's first paragraph (herbal pages
carry almost no labels; only f2r has any: `ytoail`, `ios an on`):
`kchsy, kydainy, kooiin, fochor, poror, pocheody, pchodol`.

Tests against nulls drawn from the 119 non-consensus herbal page-initial
words:

- **(A) shared family signature:** modal first-glyph share 0.43 vs null
  0.49 ± 0.14, p=0.84. **No signature.** (Page-initial words are uniformly
  gallows-dressed anyway — phase 4's paragraph-initial ornament swamps any
  name morphology.)
- **(B) recurrence in pharma** (where plant parts reappear in jars),
  exact-or-edit-distance-1: 6/7 vs null 3.96 ± 1.28, **p=0.11**. Not
  significant — and the base rate exposes the trap: **56% of *all* herbal
  page-initial words "recur" in pharma at ed≤1**, because a rigid
  combinatorial template makes near-matches cheap.
- **Strict variants:** exact-match 0/7 (null 0.76, p=1.0); exact after
  stripping the paragraph-initial gallows ornament 1/7 vs null 3.42,
  p=0.99 — *below* chance.

**No plant-name candidate survives. Per the pre-registered gate, no
micro-decipherment sketches are offered.** The one candidate worth a
footnote: f15v (Paris quadrifolia) opens with `poror`, and pharma has label
`oror` / text `doror` — but the nulls show such coincidences are the
expected background at this morphology density, not evidence.

## 6. What phase 6 adds

1. **Labels are a real, distinct register** — q-free, bench-poor,
   o+gallows-fronted, hapax-rich, less template-conforming. The label
   lexicon is *not* the section-locked content families of phase 5.
2. **Weak but significant page anchoring** (z=2.6, p=0.007) concentrated in
   the cosmological material; **zero in pharma**, where a naming reading
   most needs it. Labels and text are about the same *sections*, but
   same-surface-form co-reference between label and page text is marginal.
3. **Zodiac/star labels are page-systematic** (z up to 14): within one
   wheel, labels share structure — a per-constellation naming scheme or a
   per-page generation theme.
4. **The Rosetta attempt honestly failed:** consensus plant folios yield no
   consistent name morphology and no above-chance travel of candidate names
   into the pharma section.

---

# SIX-PHASE CAMPAIGN SYNTHESIS

| phase | probe | verdict |
|---|---|---|
| 1 | BPE / morphology | words from a super-regular template; not glyph soup |
| 2 | word-order information | weak, wrongly-shaped-for-prose sequencing; repetition enriched |
| 3 | self-citation generator | Rugg/Timm-style autocopy **falsified** on held-out fine structure |
| 4 | slot grammar / verbose cipher | 15 slots, 93% coverage; words dense, not hollow; line = record; positional ornament layer proven |
| 5 | embedding geometry | language-shaped, split-half-stable semantic space; topical section families (z≈227); function/content split; alignment powerless at 35K tokens (calibrated null) |
| 6 | labels vs drawings | labels a distinct connective-free register; weak page anchoring (z=2.6), none in pharma; zodiac naming systematicity (z≈14); plant-name pairing null |

**Where six phases leave the manuscript.** The text is a rigid combinatorial
word-template system organized as line-records, with a proven
page-positional/ornamental layer, a topically organized lexicon over a
section-flat function-word backbone, one architecture in two parameter
settings (Currier A/B) — and now: a dedicated label register that behaves
like *designations* (hapax-rich, connective-free, page-systematic in the
zodiac) while refusing to behave like *quotable names* (no same-form
recurrence between a plant's page and its pharma reappearance, no anchoring
of jar labels to jar recipes).

**Sober assessment.** Achieved: every mechanical/structural claim above is
quantified against explicit nulls, several popular hypotheses are dead
(random gibberish, word-for-word enciphered prose, autocopy, padding-heavy
verbose cipher, and now "labels are transparently the names discussed in
the adjacent text"). Not achieved: any referent pinned, any word read. The
totality still fits a nomenclator/code-book or structured notation, with
one sharpened constraint: **whatever maps isolated designations to
running-text forms is non-trivial** — the same referent does not keep its
surface form between label and sentence (q-/connective morphology is part
of it; it does not obviously explain pharma's total anchoring failure).
The honest end-state: this method family — distributional statistics at
38K tokens — has now been pushed to its power limit. Progress from here
needs either external constraints (imagery-driven priors, dated parallel
texts) or a formal model of the label↔text form mapping, not more
correlation.

## Files

- `phase6_lib.py` (IVTFF locus-type parser), `run_phase6.py` + 6 step scripts
- checkpoints: `phase6_labels.json`, `phase6_lexicon.json`,
  `phase6_anchoring2.json`, `phase6_withinpage.json`,
  `phase6_plantpairs.json`, `phase6_plantpairs_strict.json`,
  `phase6_zl_plantids.json`
- chart: `charts/voynich_labels_chart.png` (+ caption sidecar)

## Sources

- IVTFF 2.0 format spec: voynich.nu/software/ivtt/IVTFF_format.pdf (locus
  types); transliteration overview: voynich.nu/transcr.html
- ZL3b-n.txt v3b (2025-05-13), Zandbergen-Landini, incl. per-page Plant ID
  annotations (Petersen/O'Neill/Holm/Voynich/Zandbergen attributions)
- E. Sherwood, *The Voynich Botanical Plants*,
  edithsherwood.com/voynich_botanical_plants/ (pages 1–8 consulted)
- D. Scott IDs as cited by Sherwood (Kennedy & Churchill 2004, p.164);
  voynich.nu/q02/f009v_tr.txt (Petersen's Viola trinitalis note)

## Caveats

- Label word counts are small (1,169 tokens); per-section anchoring tests
  have limited power (3–15 pages/section). The pooled result is the
  reliable one.
- "First paragraph word = plant name" is a convention borrowed from real
  herbals; if the name sits elsewhere (or nowhere), test (B) tests nothing —
  null there is expected under both "no names" and "names elsewhere."
- Edit-distance-1 recurrence is shown to be uninformative at this
  morphology density; only exact-form statistics should be trusted, and
  they are null.
- Consensus plant IDs remain scholarly conjecture; the test was designed so
  that wrong IDs produce null, not false positives.
