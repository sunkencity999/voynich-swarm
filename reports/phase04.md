# Voynich Phase 4 — Slot-Grammar Decomposition + Verbose-Cipher Attack

*2026-09-14 · workstation A · companion to `phase01.md` (phase 1, BPE morphology),
`phase02.md` (phase 2, word-order information), `phase03.md`
(phase 3, self-citation falsified). Pure python stdlib; matplotlib (via uvx)
for the chart only. No LLM calls anywhere in the analysis.*

## Question

Phases 1–3 left a specific hypothesis standing: the **verbose cipher** — each
Voynich word is a padded/structured *container* in which only part of the
glyph material carries information. That would explain super-regular
morphology (the container template), low char entropy (the padding), and weak
word-order signal (only the payload sequences meaningfully). This phase fits
an explicit slot grammar, measures where the information actually lives,
extracts the candidate payload ("residue"), and tests the padding prediction
directly.

## 1. The slot grammar

Stolfi-style positional decomposition, implemented as a 3-pass regex cascade
(`phase4_lib.py`) over the line-structured re-extraction of ZL3b-n.txt
(5,354 locus lines, 38,946 words; page variables `$L` = Currier language
retained):

```
Q AOY PREL BENCH1 E1 AO0 GALL BENCH2 E2 AO1 CORE AO2 I FIN Y
q [aoy] [dlrs] ch|sh e{1,3} [ao] k|t|p|f|ckh|cth|cph|cfh ch|sh e{1,3} [ao] [dlrs]{1,2} [ao] i{1,3} [nmlrs] y
```

- **Pass 1** (canonical, no PREL/E1/AO0): 79.7% of tokens.
- **Pass 2** (adds prefix consonant `ol-/l-` class + pre-gallows e/ao cycle,
  for `olkeedy`, `cheky`, `choky`, `lchedy`): +12.3%.
- **Pass 3** (two-consonant cores, the `-ldy` class: `choldy`, `okaldy`): +1.0%.
- **Total: 93.0% of tokens (70.0% of types) parsed by 15 ordered slots.**
  The cascade keeps canonical words in canonical slot assignments. Residual
  failures: multi-cycle compounds (`polchedy`, `daldy`), post-E2 benches
  (`qokechy`), stray single glyphs (`g x v c`).

### Per-slot inventory (36,222 parsed tokens)

| slot | entropy (bits, incl. ∅) | fill rate | values | top fills |
|---|---|---|---|---|
| Q | 0.59 | 14% | 1 | q |
| AOY | 1.49 | 48% | 3 | o, a, y |
| PREL | 0.56 | 9% | 4 | l, d, s, r |
| BENCH1 | 1.14 | 29% | 2 | ch, sh |
| E1 | 0.36 | 6% | 3 | e, ee, eee |
| AO0 | 0.32 | 5% | 2 | o, a |
| **GALL** | **1.91** | 48% | 8 | k, t, p, cth |
| BENCH2 | 0.48 | 9% | 2 | ch, sh |
| E2 | 1.24 | 31% | 3 | e, ee, eee |
| AO1 | 1.29 | 35% | 2 | o, a |
| **CORE** | **2.15** | 64% | 14 | d, l, r, s |
| AO2 | 0.79 | 18% | 2 | a, o |
| I | 0.88 | 18% | 3 | ii, i, iii |
| FIN | 1.38 | 29% | 5 | n, r, l, m |
| Y | 0.96 | 38% | 1 | y |

Sum of independent slot entropies = **15.53 bits**; actual entropy of parsed
word identities = **9.88 bits** → **5.65 bits (36%) of within-word redundancy**
carried by slot–slot coupling.

## 2. Where the information lives

### Within-word slot coupling (shuffle-corrected MI, bits)

Top pairs: `I↔FIN` **0.60**, `AO2↔FIN` 0.40, `AOY↔BENCH1` 0.24, `AOY↔GALL`
0.22, `Q↔AOY` 0.21, `FIN↔Y` 0.21, `CORE↔Y` 0.19, `AO1↔CORE` 0.18. Slots are
**strongly coupled**, especially the word-final complex (`a-ii-n` behaves as
one unit) and the prefix complex (`q-o-gallows`). The grammar's slots are not
independent choices; the effective degrees of freedom per word are ~10 bits,
not 15.5.

### Sequential structure — which slot carries the phase-2 signal?

Adjacent parsed pairs **within the same line** (29,842 pairs), all
shuffle-corrected:

- word → next word MI: **0.218 bits** (phase 2's pooled estimate was 0.182 —
  line-flattening was diluting it).
- **Across line boundaries the coupling vanishes: 0.014 bits** (n=5,353,
  ≈ noise). *The sequential signal is entirely line-bounded.*
- Slot-level channel: smeared, not concentrated. Best single slot-pair
  `Y→Q` 0.059, `CORE→AOY` 0.048, `Y→AOY` 0.041. By slot vs whole next word:
  CORE 0.13, Y 0.12, FIN 0.08, GALL 0.07. By whole word vs next word's slot:
  AOY 0.13, GALL 0.10, Q 0.08.
- Word length carries almost nothing (len→next-len 0.025; len→next-word 0.08).

**Reading:** the sequential information flows from the *end region* of a word
(CORE/FIN/Y) into the *prefix region* of the next (Q/AOY/GALL) — e.g. the
famous y-final → q-initial chaining. No single "ciphertext slot" concentrates
the signal; it is a suffix→prefix boundary coupling, smeared across the
high-entropy slots. This looks like **connection/sandhi rules between adjacent
containers**, not like one slot spelling out a hidden letter stream while the
rest is inert.

## 3. Residue extraction (candidate payload)

Slots with entropy ≥ 0.9 bits kept: **AOY BENCH1 GALL E2 AO1 CORE FIN Y**
(8 slots, 11.55 of 15.53 independent-slot bits). Shell (stripped): Q PREL E1
AO0 BENCH2 AO2 I. Residue = concatenated kept-slot fills per word: mean 3.36
glyphs of 4.29 (only 0.04% of words leave an empty residue).

| stream | H₀ | H₁ | H₂ | alphabet |
|---|---|---|---|---|
| **Voynich residue** | 3.66 | 2.64 | 2.44 | 20 |
| Latin letters | 4.00 | 3.46 | 2.94 | 20 |
| Latin, vowels stripped | 3.61 | 3.40 | 3.19 | 16 |

Rank-aligned distribution distance (χ² / JS, rank-sorted probability vectors):

| comparison | χ² | JS (bits) |
|---|---|---|
| residue vs Latin | 0.072 | 0.029 |
| residue vs Italian | 0.072 | 0.028 |
| **residue vs devoweled Latin** | **0.023** | **0.008** |
| residue vs Roman-numeral letters | 0.349 | 0.166 |
| *ref: Latin vs Italian* | 0.009 | 0.003 |
| *ref: full Voynich glyphs vs Latin* | 0.024 | 0.009 |

- **Roman-numeral-like content: rejected** (distance 15–40× the natural refs).
- The residue's unigram profile sits **closest to vowel-stripped Latin** — its
  H₀ matches (3.66 vs 3.61) and its rank profile is as close to devoweled
  Latin as full Voynich is to Latin — consistent with the medieval-abbreviation
  idea. **But this is weak-form evidence**: it is ~3× farther than two real
  languages sit from each other, and 20-symbol skewed distributions are
  generically similar under rank alignment.
- **The killer remains conditional structure: residue H₁ = 2.64 vs devoweled
  Latin 3.40.** Even after stripping the low-info shell, the payload stream is
  far too sequentially rigid to be a simple letter-substitution of abbreviated
  Latin. Whatever the residue encodes, it is not plaintext-order letters under
  monoalphabetic substitution.
- Sequential MI check: residue→next-residue **0.275** vs shell→next-shell
  0.060 — the phase-2 word-order signal rides **in the residue**, as a payload
  should. (Residue's small alphabet also makes this the least biased of the
  sequential estimates.)

## 4. Verbose-padding test — the headline

Prediction of a verbose cipher: word-identity information grows *slowly* with
word length (extra glyphs are padding). Measured (chart, right panel):

| model | slope, bits per glyph/letter (len 2–9, n≥30 bins) |
|---|---|
| Voynich, true word info (−log₂ p(word)) | **0.97** |
| Latin, true word info | **0.85** |
| Voynich, char-bigram model | 2.19 |
| Latin, char-bigram model | 3.25 |
| Voynich, independent-slot model | 1.89 |

**The padding prediction fails.** True word-identity information grows
*linearly* with length, at a slightly *higher* per-glyph rate than Latin
(0.97 vs 0.85), with no plateau anywhere in the attested length range. Mean
info per glyph over the whole lexicon: Voynich 9.88/4.29 ≈ **2.3 bits/glyph**
vs Latin ≈ 1.5 bits/letter. Voynich words are, if anything, *denser* per
symbol in word-identity terms than Latin words — the opposite of hollow
containers. The glyph *stream* is redundant (bigram slope 2.19 vs 3.25 —
that's the rigid template from phases 1–2), but that redundancy does not
scale with length the way padding would: long words buy proportionally more
identity, not more filler.

## 5. Position effects — where the verbose-cipher intuition survives

Word *form* depends strongly on position on the page:

- **Paragraph-initial gallows:** first word of a paragraph (`@P` loci) has
  GALL filled **84.4%** vs **44.3%** for first words of mid-paragraph lines
  (and BENCH1 collapses 27.7%→3.4%, Q 14.5%→4.5%). The classic effect,
  localized cleanly to one slot.
- **Line-final m:** FIN=`m` at line end **15.5%** vs **1.0%** mid-line (15×).
  `m` is essentially a line-end allograph.
- Line-initial words: PREL doubled (13.6% vs 7.4%), BENCH2/AO0 enriched, E2
  suppressed; line-final words: E2 collapses (14.6% vs 34.4%), FIN enriched.
- Sequential coupling is **line-bounded** (0.218 within vs 0.014 across).

No natural-language prose modulates word *morphology* by line position —
lines are typographic accidents in real text. In the Voynich, **the line is a
hard structural unit**: sequence information does not cross it, and several
slots are page-layout-driven. At least part of every word's form is
determined by *where it sits*, not *what it says*.

## 6. Currier A vs B

Same grammar fits both: coverage A **93.0%** (11,575 words), B **93.8%**
(24,074). Per-slot JS divergence between A and B fill distributions is small
(max AO1 0.064, AOY 0.026, E2 0.024) — the **architecture is identical**, only
the parameters shift (B's famous `-edy` appetite shows up as E2/AO1/CORE
redistribution). A and B are two settings of one machine, not two systems.

## Verdict on the verbose-cipher hypothesis

**The strong form loses.** A verbose cipher in the classic sense — most glyph
material is padding, information grows sublinearly with length — is
contradicted head-on: word-identity information grows linearly at a
Latin-like (slightly higher) per-glyph rate, and the payload/shell split
shows the shell carries only ~4 of 15.5 independent-slot bits with the
sequential channel confined to the residue.

**A weaker structural form survives and sharpens.** The decomposition is
real: 15 ordered slots, 93% coverage, a genuine low-info shell (Q, PREL, E1,
AO0, BENCH2, AO2, I), and page-position dependence (paragraph-initial
gallows, line-final m, line-bounded sequencing) prove that *some* of each
word's form is non-content — positional/ornamental. But the informative
residue that remains is still **not** a substitution-ciphered letter stream:
its conditional entropy (H₁ 2.64) stays far below any natural letter stream,
vowelless Latin included, and the sequential signal is a smeared
suffix→prefix boundary coupling rather than a hidden channel in one slot.

### Four-phase combined picture

| phase | probe | result |
|---|---|---|
| 1 | BPE morphology | super-regular templates; not random |
| 2 | word order | weak, wrongly-shaped sequencing; repetition enriched |
| 3 | self-citation generator | falsified held-out; can't fake fine structure |
| 4 | slot grammar / verbose cipher | words are dense, not hollow; low-info shell + line-positional layer real; residue too rigid for simple substitution |

What now fits everything measured: Voynichese words are **dense codes drawn
from a rigid combinatorial template**, arranged with **line-as-record
structure** (sequence information lives within lines and dies at boundaries,
like entries in a list or table row) plus a **positional/ornamental layer**
(paragraph and line decorations on specific slots). What it is *not*, on
these data: random gibberish (1), word-for-word enciphered prose (1+2),
simple autocopy output (3), or a padding-heavy verbose cipher (4). The live
candidates left standing: a **nomenclator/code-book system** (each word a
dense arbitrary code for a concept — explains density, weak adjacent
coupling, line-records), a **structured constructed language/notation**, or a
sophisticated generator with position-aware rules. Meaning-bearing readings
remain unfalsified; the *page-mechanical* component is now proven.

### What phase 5 (embedding alignment) should target

1. Build word/residue embeddings from **within-line co-occurrence only**
   (cross-line context is provably noise) — sections kept separate, A/B
   separate.
2. Unsupervised cross-lingual alignment (Procrustes/MUSE-style, or simple
   distributional-neighborhood matching) of the top-N Voynich word vectors
   against Latin, Italian, and Hebrew content-word embeddings from
   size-matched corpora — score against rotation-of-shuffled-vocab nulls. A
   nomenclator predicts topical clustering alignable at the *concept* level
   even though letters never align.
3. Line-as-record test: distribution of line lengths and within-line
   positional vocabularies (do lines look like records with fielded
   positions? does slot usage vary by within-line position beyond
   first/last?).
4. Section-conditional residue statistics (herbal vs balneo vs stars):
   does the residue distribution shift with subject matter (content-like) or
   stay flat (generator-like)?

## Caveats (honest)

- The slot order is hand-designed (canonical EVA order plus two data-driven
  extensions). 93% coverage is good but the *identity* of slots is partly
  conventional: greedy regex parsing assigns ambiguous glyphs
  deterministically (e.g. `o` before core vs after), which shapes per-slot
  numbers. A different canonical order would move entropy between adjacent
  slots — the shell/residue split and the padding curves are robust to this;
  exact per-slot values are not.
- Sequential MI values are MLE with permutation correction; the word-level
  estimates (7.7K alphabet on 30K pairs) are the shakiest — rankings and the
  within/cross-line contrast are trustworthy, third decimals are not.
- Rank-aligned distribution distance is deliberately weak-form (no letter
  mapping claimed). The devoweled-Latin proximity is *compatible with*, not
  evidence for, an abbreviation system.
- 7% of tokens (30% of types — disproportionately hapax/compound words) never
  parse and are excluded from slot statistics; they are longer and rarer than
  average, so per-slot entropies are floor-biased slightly.
- EVA transliteration caveat binds everything (phases 1–3): glyph
  segmentation choices define the slot alphabet itself.

## Files

- `phase4_lib.py` — extraction, glyph tokenizer, slot grammar, estimators
- `run_phase4.py` → `phase4_results.json`, `phase4_run.log`
- `make_chart_phase4.py` → `../charts/voynich_slotgrammar_chart.png` (+ .txt)
- Prior phases: `phase01.md`, `phase02.md`, `phase03.md`

🜂
