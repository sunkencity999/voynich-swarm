# Voynich Phase 5 — Within-Line Embedding Alignment: the Nomenclator Test

*2026-09-14 · workstation A · final phase of the five-phase campaign. Companions:
`phase01.md` (1: BPE morphology), `phase02.md` (2: word-order MI),
`phase03.md` (3: self-citation falsified), `phase04.md` (4: slot
grammar / verbose cipher). numpy/scipy only (gensim absent → PPMI+SVD by
hand, deterministic, seeded); sklearn for the t-SNE projection in the chart;
matplotlib via uvx for charts. No LLM calls anywhere in the analysis.*

## Question

Phase 4 left three hypotheses standing: **nomenclator/code-book**,
**constructed notation**, **position-aware generator**. The nomenclator's
distinctive prediction: Voynich words denote *concepts*, so their
co-occurrence geometry should look like a language's content-word geometry,
and topical structure should align with manuscript sections. This phase
builds within-line embeddings, compares the *shape* of the resulting
semantic space against real languages and nulls, tests topic–section
alignment, and attempts (with full calibration) unsupervised cross-lingual
alignment.

## 1. Corpus and embeddings

- Line-structured re-extraction of ZL3b-n.txt: **5,354 locus lines, 38,946
  words**, each line tagged with folio, Currier language ($L), and section
  from the IVTFF $I code: **H→herbal, A/Z/C→astro, B→balneo, P→pharma,
  S→recipes, T→text-only** (T excluded from section tests; mapping documented
  in `phase5_lib.py`).
- Embeddings: **PPMI + truncated SVD, d=100, window ±3, windows never cross a
  line/sentence boundary** (phase 4: sequential coupling is line-bounded,
  0.218 bits within vs 0.014 across), min-count 5, unit-normalized rows.
  Chosen over SGNS for determinism.
- Comparison spaces with *identical* hyperparameters: Latin (33.8K tokens)
  and Italian (39.0K tokens) sentence-segmented, size-matched to Voynich.
- Nulls: **word-shuffled Voynich** (global token shuffle, line lengths kept —
  destroys co-occurrence) and **line-shuffled Voynich** (section labels
  permuted over intact lines — since windows never cross lines, its
  *embedding* is identical to the real one by construction; it is the null
  for the topic test). For alignment floors: word-shuffled Latin.
- Vocab sizes at min-count 5: Voynich 997, Latin 1,177, Italian 971.

## 2. Intrinsic geometry — is the space shaped like a language's?

k=10 kNN graph over cosine similarity, all spaces d=100:

| metric | Voynich | Latin | Italian | word-shuf Voynich |
|---|---|---|---|---|
| hubness (skew of N₁₀) | 0.46 | 0.22 | 0.45 | **0.89** |
| mean NN₁ cosine | 0.469 | 0.549 | 0.451 | 0.426 |
| NN₁ cosine std | 0.088 | 0.161 | 0.078 | 0.068 |
| clustering coefficient | 0.131 | 0.194 | 0.113 | **0.098** |
| effective rank | 95.0 | 92.5 | 94.8 | 95.5 |
| top-10 eigen share | 0.170 | 0.190 | 0.169 | 0.161 |

**Voynich's semantic-space shape sits inside the natural-language band** — on
every metric it lands between Latin and Italian or right beside Italian,
while the word-shuffled null is separated in the language-like direction on
all of them (higher hubness, lower NN similarity, lower clustering). The
shuffled null does *not* collapse to pure noise (PPMI+SVD still encodes
frequency), which makes the contrast conservative: what separates Voynich
from its own shuffle is genuinely co-occurrence structure, not frequency.

**Split-half self-consistency** (odd vs even lines, independent embeddings,
relational Spearman ρ between the two halves' similarity matrices over the
top 300 shared words — `phase5_selfalign.json`):

| corpus | split-half relational ρ |
|---|---|
| Latin | 0.144 |
| **Voynich** | **0.087** |
| Italian | 0.063 |
| word-shuf Voynich | 0.028 |

Voynich's co-occurrence geometry is *reproducible* — two disjoint halves of
the manuscript induce correlated similarity structure, within the band set by
the two real languages and 3× the shuffle floor. The space is not an
artifact of one pass; it measures something stable about the text.

## 3. Topic–section test — the headline

k-means over Voynich word embeddings, k∈{10…30} silhouette-selected
(k\*=26, silhouette 0.040 — weak clusters, typical for tiny corpora, which
makes the following contrast more striking, not less):

- **Token-level cluster↔section MI = 0.149 bits** vs line-shuffled null
  **0.0036 ± 0.0006** → **z ≈ 227**. Vocabulary is massively section-structured.
- **Currier control** (is it just A/B dialect? — `phase5_currier_control.json`):
  MI(cluster; Currier lang) = 0.131 bits, so dialect explains roughly half
  the pooled signal. But *within* Currier B alone: MI = 0.051 bits, z = 66.5
  (recipes/balneo/herbal-B/astro-B); within A alone: MI = 0.079 bits, z = 67.3
  (herbal-A/pharma/recipes-A). **Section structure survives the dialect
  control decisively in both dialects.**

### Section-locked word families (top 20 by KL from corpus section profile, n≥20)

| word | n | KL bits | section (share) |
|---|---|---|---|
| oteos | 25 | 1.90 | astro (76%) |
| qokeody | 29 | 1.40 | pharma (55%) |
| olkedy | 24 | 1.33 | balneo (79%) |
| cthor | 43 | 1.33 | herbal (93%) |
| otchol | 28 | 1.30 | herbal (89%) |
| olshedy | 20 | 1.27 | balneo (75%) |
| cthy | 99 | 1.27 | herbal (93%) |
| kchy | 35 | 1.26 | herbal (91%) |
| ckhey | 26 | 1.24 | herbal (50%) / pharma (42%) |
| qol | 139 | 1.22 | balneo (76%) |
| lkaiin | 44 | 1.22 | recipes (89%) |
| ykchy | 22 | 1.22 | herbal (86%) |
| kchor | 20 | 1.21 | herbal (90%) |
| lkain | 32 | 1.20 | recipes (88%) |
| olkain | 34 | 1.19 | balneo (76%) |
| dchor | 27 | 1.15 | herbal (85%) |
| lkar | 25 | 1.13 | recipes (88%) |
| dchy | 29 | 1.13 | herbal (83%) |
| oteody | 38 | 1.12 | astro (55%) |
| qokeol | 50 | 1.11 | pharma (50%) |

The locking is **family-structured, not word-by-word**: platform-consonant
`cth-/kch-/dch-` words own the herbal section; `lk-` prefix words own
recipes; `ol…dy` words own balneo; `qoke-` words own pharma; `oteo-` words
own astro. In slot-grammar terms (phase 4), *section identity rides in
specific slot fills* — GALL+BENCH combinations for herbal, PREL=l for
recipes, AOY/PREL=ol for balneo — while the rest of the template is shared.

### Universal (section-flat) words — candidate function words

Flattest profiles among n≥100 words: **okar, r, saiin, y, or, chey, okal,
chckhy, sheey, dar, okaiin, otal, chdy, dal, shey, dain, aiin, oty, cheey,
qokar** (KL 0.03–0.16). These include the manuscript's highest-frequency
words (aiin n=471, y n=441, or n=353). High frequency + flat section profile
+ (phase 2) repetition tolerance = the profile of **function/grammar words or
notation operators**, exactly the split a nomenclator or structured notation
needs.

## 4. Cross-lingual alignment — calibrated, and honestly null

Method: entropic Gromov-Wasserstein (Peyré et al. 2016 scheme, log-domain
sinkhorn, ε annealed 1.0→0.01) between double-centered, variance-normalized
cosine-similarity matrices of the top 400 words of each space. Score:
Spearman ρ between similarities of matched pairs (relational preservation).
Calibration run *first*, in both directions:

| pairing | relational ρ | coupling conc. |
|---|---|---|
| **ceiling: Latin→Italian** | **0.165** | 0.94 |
| Voynich→Latin | 0.171 | 0.92 |
| Voynich→Italian | 0.165 | 0.98 |
| floor: Voynich→shuffled-Latin | 0.165 | 0.99 |
| floor: Latin→shuffled-Latin | 0.177 | 0.94 |
| floor: shuffled-Voynich→Latin | 0.157 | 0.94 |

**The instrument has no power at this corpus size: the real-related-language
ceiling sits *inside* the shuffled-floor band.** Everything aligns to
everything at ρ≈0.16–0.18, because GW finds a permutation matching the
generic geometry any embedding cloud possesses. Two supporting diagnostics:

- Naive parameterizations were worse, not better: uncentered similarities +
  fixed ε left the coupling uniform (conc = 1/n) and all ρ ≤ 0.08 including
  the ceiling — two full failure modes documented in `phase5_align.log` /
  `phase5_selfalign*.log`.
- **Split-half self-alignment** (same corpus, same language, shared vocab —
  the easiest possible alignment task): GW top-1 accuracy recovering the
  *identity* match was 0.0–1.3% (chance 0.33%) even for Latin→Latin. If
  seed-free GW cannot re-find *the same word* across two halves of one
  corpus, it cannot find translations across languages at 35K tokens.

Accordingly: **Voynich→Latin (0.171) and Voynich→Italian (0.165) are noise**,
and per the pre-registered rule — no global score above the null band → no
word-pairing claims — **we report zero candidate "translations."** This null
is a statement about statistical power at 35K tokens, *not* evidence against
the nomenclator (the calibration proves the test couldn't have detected one).

## 5. What phase 5 adds to the picture

1. **Language-band geometry**: the within-line co-occurrence space has
   natural-language shape (hubness, clustering, NN structure between Latin
   and Italian; clearly separated from its own shuffle) and is reproducible
   across manuscript halves.
2. **Real topical structure**: vocabulary is strongly section-organized
   (z≈227 pooled; z≈67 within each Currier dialect), with section identity
   carried by *morphological families* (slot-fill classes), not arbitrary
   word lists.
3. **Function/content split**: the highest-frequency words are section-flat;
   section-locked families are mid-frequency — the frequency×topicality
   profile of a lexicon with grammar words and content words.
4. **No decipherment**: unsupervised alignment is powerless at this scale —
   proven by calibration, stated plainly.

Points 1–3 are the nomenclator's predictions, confirmed. But honesty about
alternatives: a **constructed notation** with topic-specific sign families
predicts exactly the same three results, and a **position-aware generator**
survives only if its parameters drift by section *and* its output reproduces
split-half-stable co-occurrence geometry — a much more contrived object than
phase 3's falsified self-citation model, but not excluded by these tests.

---

# FINAL CAMPAIGN SYNTHESIS (phases 1–5)

**The five-phase picture.**

| phase | probe | verdict |
|---|---|---|
| 1 | BPE / morphology | words built from a super-regular template; not random glyph soup |
| 2 | word-order information | sequencing signal weak (~0.2 bits) and wrongly shaped for prose; repetition enriched |
| 3 | self-citation generator | Rugg/Timm-style autocopy **falsified** on held-out fine structure |
| 4 | slot grammar / verbose cipher | 15-slot template, 93% coverage; words are information-**dense** (padding prediction fails); line = hard record boundary; part of each word is provably layout |
| 5 | embedding geometry / alignment | semantic space language-shaped, split-half stable, **strongly section-structured** with a function/content split; cross-lingual alignment null at this scale (calibrated) |

**What the Voynich manuscript now looks like, on the totality of this
evidence:** a text written in a **rigid combinatorial word-template system**
whose words are dense, stable codes; organized as **line-records** (sequence
information lives within lines and dies at boundaries); decorated with a
**positional/ornamental layer** (paragraph-initial gallows, line-final m);
with a **topically organized lexicon** — morphological families of words own
manuscript sections the way content vocabulary owns topics in real language,
over a shared backbone of section-flat high-frequency function-like words;
and in **two parameter settings (Currier A/B) of one identical machine**.

**Best-fit hypothesis: a nomenclator-like code-book or constructed
notation** — a system where template-generated word-codes denote concepts,
composed line-by-line as entries/records rather than flowing prose. Both
sub-variants (cipher-intent code-book vs constructed notation/artificial
language) fit everything measured; these data cannot separate intent.
**Weakened but not dead:** a sophisticated position-aware generator with
section-drifting parameters (it must now also fake split-half-stable
topic geometry — increasingly contrived, but meaningfulness is not proven,
only *consistent*). **Dead on this evidence:** random gibberish (1), plain
enciphered prose word-for-word (1+2+4), simple self-citation (3),
padding-heavy verbose cipher (4), and any reading expecting sentence-like
syntax across a line break (4).

**What a phase 6 would need** (all beyond this corpus alone):
1. **Illustration-anchored labels**: the single strongest nomenclator test —
   do label-words on plant/star drawings recur in the corresponding sections'
   text? Requires image-region↔locus data (e.g. the voynichese.com label
   corpus or manual curation of `@L` loci with drawing referents).
2. **Transliteration replication**: rerun phases 1–5 on v101/Takahashi to
   show none of this is an EVA artifact (the standing caveat on everything).
3. **Statistical power for alignment**: the calibration says 35K tokens is
   ~an order of magnitude short; either a much larger comparison design
   (family of medieval herbals as one "topic-matched Latin"), seeded anchors
   (label words), or accept that alignment is out of reach.
4. **Codicological cross-check**: quire/scribe (Lisa Fagin Davis's five
   scribes) as covariates — is the A/B "two settings of one machine" result
   scribe-aligned, and is section-locking stable per scribe?

## Caveats (honest)

- EVA transliteration underlies everything; glyph segmentation choices shape
  the vocabulary itself (standing caveat, phases 1–5).
- Section labels are per-*page* illustration codes; a page's text may not
  match its picture. This biases *against* finding section structure, so the
  z≈227/67 results are conservative.
- Currier A/B and section are partially confounded (herbal-A, balneo-B…);
  the within-dialect controls are the honest numbers (0.051/0.079 bits),
  and roughly half the pooled section-MI is dialect.
- t-SNE (chart) is for visualization only; every statistic is computed in
  the full 100-d space.
- Embedding quality at 39K tokens is poor in absolute terms (silhouette
  0.04, split-half ρ 0.09) — fine for the *comparative* claims made here
  (all spaces built identically), insufficient for word-level claims, which
  is why none are made.
- The GW implementation choices (ε schedule, centering) were tuned on the
  *calibration pairs*, never on Voynich scores; the no-power conclusion is
  robust across every parameterization tried (three documented).

## Files

- `phase5_lib.py` — corpus/sections, PPMI+SVD, geometry metrics, k-means,
  silhouette, entropic GW, relational scoring
- `run_phase5.py` (stages: emb/geom/topic/align, all checkpointed) →
  `phase5_results.json`, `phase5_emb_*.npz`, `phase5_clusters.npz`,
  `phase5_align_*.npz`, `phase5_line_meta.json`, `phase5_vlines.json`
- Controls: `phase5_currier_control.{py-inline,json,log}`,
  `phase5_selfalign.json`, `phase5_selfalign*.log`, `phase5_align.log`
- Charts: `prep_chart_phase5.py` (t-SNE precompute) + `make_chart_phase5.py`
  → `../charts/voynich_semantic_space.png`,
  `../charts/voynich_alignment_scores.png` (+ caption sidecars)

🜂
