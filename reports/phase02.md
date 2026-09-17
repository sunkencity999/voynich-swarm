# Voynich Phase 2 — Word-Order Information Test

*2026-09-13 · companion to `phase01.md` (phase 1, BPE morphology). Same size-matched
corpora (~225KB each): Voynich (EVA, ZL3b transliteration), Latin (Caesar),
English (Austen), Italian (Dante). Pure-python estimators, no LLM involvement.*

## Question

Phase 1 showed Voynichese **morphology** is super-regular and language-like, but BPE
is blind to word order. The strongest modern hoax/gibberish arguments (word-salad,
Rugg-grille, self-citation generators) claim Voynichese **word order carries
abnormally little information**. This phase measures that directly.

## Method

1. **Unigram entropy** H(W) and **bigram conditional entropy** H(W₂|W₁), word level.
   Raw MLE conditional entropy is badly downward-biased at ~30–45K words, so every
   order-sensitive quantity is reported against the corpus's **own word-shuffled
   baseline** (10 independent shuffles, mean ± std). The shuffle has an identical
   unigram distribution, so subtraction cancels most small-sample bias:
   `info_gain = H_shuffled(W₂|W₁) − H_real(W₂|W₁)` = bits of next-word uncertainty
   removed by knowing the previous word, bias-corrected.
2. **Mutual information at distance d** ∈ {1,2,4,8,16}: I(Wᵢ;Wᵢ₊d) = H₁+H₂−H_joint
   over all pairs d apart, same shuffle correction. Natural language shows slowly
   decaying long-range MI; pure word salad sits at the bias floor beyond d=1.
3. **Character-level conditional entropies**, order 0–4 (H(c|previous k chars), MLE
   on the space-joined corpus) — secondary confirmation of the famous low Voynich
   char entropy.
4. **Adjacent repetition**: fraction of adjacent pairs that are identical, and
   near-identical (edit distance ≤ 1) — the `daiin daiin` phenomenon — real vs
   shuffle-expected.

Code: `run_wordorder.py` → `wordorder_results.json`; chart: `make_chart_phase2.py`.
Seed 1234, N=10 shuffles.

## Results

### 1. Word-level entropies and bigram information (bits)

| corpus | words | types | H(W) | H(W₂\|W₁) real | H(W₂\|W₁) shuffled | **info gain** (±σ) |
|---|---|---|---|---|---|---|
| Voynich | 37,942 | 7,695 | 10.32 | 4.442 | 4.624 | **0.182 ± 0.004** |
| Latin | 30,880 | 8,373 | 11.17 | 3.376 | 3.634 | **0.258 ± 0.001** |
| English | 41,744 | 4,330 | 9.05 | 4.708 | 5.444 | **0.736 ± 0.006** |
| Italian | 45,631 | 7,661 | 9.72 | 4.554 | 5.022 | **0.468 ± 0.008** |

Voynich's previous word removes **0.18 bits** of next-word uncertainty — the lowest
of the four, ~25% of English and ~70% of Latin — but it is **~47σ above zero**.
Word order is weak, not absent.

### 2. Shuffle-corrected mutual information vs distance (bits)

| corpus | d=1 | d=2 | d=4 | d=8 | d=16 |
|---|---|---|---|---|---|
| Voynich | 0.182 | 0.069 | **0.056** | **0.050** | **0.033** |
| Latin | 0.258 | 0.043 | 0.012 | 0.000 | −0.001 |
| English | 0.736 | 0.280 | 0.033 | 0.014 | 0.008 |
| Italian | 0.468 | 0.096 | 0.017 | 0.016 | −0.003 |

(Shuffle-baseline σ ≈ 0.002–0.008 everywhere; values >~0.016 are >2σ real.)

Two surprises:
- **At short range Voynich is the weakest** — its d=1 MI is below even
  free-word-order, heavily-inflected Latin.
- **At long range Voynich is the strongest.** The natural languages decay to the
  noise floor by d=8; Voynich **plateaus at ~0.03–0.06 bits out to d=16**, several
  σ above zero. See the chart's log panel — a flat gold plateau crossing over the
  decaying natural-language curves at d≈4.

### 3. Character-level conditional entropy (bits/char, incl. space)

| corpus | order 0 | order 1 | order 2 | order 3 | order 4 |
|---|---|---|---|---|---|
| Voynich | 3.87 | **2.14** | 1.88 | 1.81 | 1.71 |
| Latin | 4.02 | 3.31 | 2.65 | 2.04 | 1.59 |
| English | 4.10 | 3.31 | 2.58 | 1.92 | 1.49 |
| Italian | 3.93 | 3.11 | 2.64 | 2.21 | 1.83 |

Confirmed and dramatic: Voynich's **order-1 char entropy (2.14) is ~1.2 bits below
every natural comparator** — each glyph is highly predictable from just the previous
glyph. This is the same super-regular word-template morphology phase 1's BPE
exploited, seen from the entropy side. (Note the crossover: by order 3–4 Voynich is
*within* the natural band — its predictability is front-loaded into local glyph
transitions, then flattens; natural languages keep gaining from longer context.)

### 4. Adjacent repetition (% of adjacent word pairs)

| corpus | identical, real | identical, shuffled | near (ed≤1), real | near, shuffled |
|---|---|---|---|---|
| Voynich | **0.81%** | 0.32% | **4.61%** | 2.02% |
| Latin | 0.00% | 0.23% | 0.16% | 0.56% |
| English | 0.05% | 0.80% | 0.75% | 2.15% |
| Italian | 0.05% | 0.81% | 2.01% | 4.29% |

This is the sharpest qualitative split in the whole experiment:
- **All three natural languages avoid adjacent repetition** — real rates are 3–17×
  *below* chance (languages actively disfavor `the the`; scribes/editors delete it).
- **Voynich is enriched ~2.3–2.5× *above* chance** in both identical and
  near-identical adjacent pairs (`daiin daiin`, `chol chor` …). This is
  anti-natural-language behavior that no word shuffle preserves and no simple
  substitution cipher of a natural language would create.

## Chart

`voynich_wordorder_chart.png` — corrected MI decay per corpus, linear + log panels,
±2σ shuffle bands. Chart included in `charts/`.

## Interpretation (honest)

The word-order picture is **genuinely anomalous in both directions**:

1. **Pure word salad is ruled out.** Corrected bigram MI of 0.18 bits is ~47σ above
   the shuffle floor. A memoryless generator drawing words i.i.d. from the observed
   vocabulary would sit at zero. Whatever produced this text, consecutive words are
   statistically coupled.
2. **But the coupling is abnormally weak** — the weakest of the four corpora, ~¼ of
   English's, and below even Caesar's Latin, where inflection famously liberates
   word order. If Voynichese encoded a natural language with anything like normal
   syntax word-for-word, we'd expect d=1 MI in the 0.25–0.75 band. It isn't.
3. **The long-range plateau is the wrong shape for syntax.** Natural-language MI
   here decays smoothly to zero by d≈8. Voynich stays flat at ~0.05 bits to d=16.
   Flat long-range MI with weak short-range MI is the signature of **topic/state
   clustering, not grammar**: something slowly varying (page, section, plant being
   described, generator table in use) modulates word choice, while adjacent words
   barely constrain each other. Both a real-language-with-topic-drift and a
   mechanical generator whose operator changes tables/pages produce this shape —
   but grammar-driven text produces the opposite shape (strong short, decaying long).
4. **The repetition enrichment is the strongest pro-non-linguistic datum in either
   phase.** Natural languages suppress adjacent repeats; Voynich amplifies them.
   This is exactly what perseverative generation (self-citation: copy a nearby word
   with small modification — Timm & Schinner's model) predicts, and what natural
   language essentially never does at this rate.

**Combined phase 1 + 2 verdict.** Phase 1: morphology is super-regular — *more*
compressible and template-bound than any natural comparator, decisively non-random.
Phase 2: word order carries real but abnormally weak information, long-range
structure looks like topic drift rather than syntax, and adjacent near-repetition is
enriched where every natural language suppresses it. Jointly, the profile that fits
best is a **generative process with rigid word-internal rules and very loose,
locally-perseverative word sequencing** — e.g. self-citation/table-driven generation,
or a natural-language encoding that destroys word-level syntax (heavy nomenclator,
one-glyph-per-concept lists, or positional re-encoding). A word-for-word cipher of
ordinary Latin/Italian/English prose is now disfavored from two independent
directions: the morphology is too regular (phase 1) and the syntax signal is too
weak and wrongly shaped (phase 2). "Random gibberish," equally, remains dead — every
metric shows structure far above chance.

## Caveats

- **~38K words is small.** All MLE entropies are biased; the shuffle-delta design
  cancels the unigram-level bias but joint-distribution bias cancellation is
  approximate, especially at d=1 where the real text's pair distribution is more
  concentrated than the shuffle's. Values, not rankings, should be treated softly.
- **Topic clustering inflates long-range MI.** The ms has distinct sections
  (herbal/astro/balneological) with distinct vocabularies; some or all of the
  d=8–16 plateau is section vocabulary, not sentence-level structure. The natural
  comparators are each single continuous works (one author, one register), which if
  anything *understates* their long-range MI vs a multi-section codex — so the
  Voynich plateau should not be read as "more long-range structure than English."
- **EVA transliteration uncertainty** (phase 1 caveat, still binding): glyph
  segmentation choices directly shape word identity, hence every word-level number.
  The near-repeat statistic is somewhat robust (ed≤1 tolerates one glyph dispute),
  the exact MI values are not.
- Currier A/B pooled; line/paragraph boundaries were flattened by cleaning, so
  line-as-functional-unit effects (a known Voynich phenomenon) are invisible here.
- Latin comparator is unusually word-order-free; a Romance/Germanic-only comparison
  band would make Voynich's d=1 deficit look even starker.

## Files

- `run_wordorder.py`, `wordorder_results.json` — analysis + raw numbers
- `make_chart_phase2.py`, `voynich_wordorder_chart.png` — chart
- `phase01.md` — phase 1 (BPE morphology)

🜂
