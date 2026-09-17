# Voynich Phase 3 — Self-Citation Falsification Test

*2026-09-13 · workstation A · companion to `phase01.md` (phase 1, BPE morphology) and
`phase02.md` (phase 2, word-order information). Pure python stdlib +
HF `tokenizers` for BPE + matplotlib for the chart. No LLM calls anywhere in the
analysis.*

## Question

Phases 1–2 established that Voynichese is decisively **not random gibberish** but is
**anomalous in both directions**: morphology *more* regular than any natural language
(phase 1), yet word order carrying *abnormally weak* and wrongly-shaped information,
plus adjacent near-repetition *enriched* where every natural language suppresses it
(phase 2). The leading "meaningless but not random" explanation for exactly this
profile is a **self-citation / autocopying generator** (Timm & Schinner 2019/2020):
a scribe manufactures each new word by copying a nearby earlier word and applying
small modifications. Perseverative copying naturally yields Zipf's law, low entropy,
and repeated near-duplicates without encoding any message.

**The falsification question:** can such a generator reproduce **all** the measured
Voynich statistics at once? If yes, meaningless generation survives as a live
hypothesis. If a faithful generator **measurably fails on metrics it was *not* tuned
to**, then those statistics carry information a copy-machine cannot fake — and the
meaning-bearing hypotheses survive the falsification attempt.

## Method

### The generator (`run_phase3.py`)

Each new word is produced by:

1. **Recency-weighted source pick.** Choose an earlier word at distance *d* back,
   with `weight(d) ∝ exp(−d/τ)` (τ = recency scale). Small τ = copy your immediate
   neighbours; large τ = copy anywhere in a wide trailing window.
2. **Exact copy** with probability `p_exact` (perseveration / verbatim repeat).
3. Otherwise **mutate** the source word with one operation, drawn to respect EVA
   structure — all tables extracted *from the Voynich corpus itself*, nothing
   hardcoded:
   - **context-conditional glyph substitution** — replace a glyph by another that
     occurs in the same left/right glyph context in real Voynichese (this captures
     confusable EVA classes — ch/sh, o/a, k/t gallows — empirically rather than by
     hand);
   - **affix swap** — replace a real high-frequency prefix/suffix (top-25 from the
     corpus: `qo- ch- o- sh- …`, `-y -dy -in -iin -edy …`) with another;
   - **deletion** / **context-conditional insertion**.
   With probability `p2` a **second** mutation is applied (compounding drift).

Seed = the manuscript's first ~12 words. Generation continues to the exact real word
count (37,942).

### Tuning — 3 knobs only

Coarse grid search over **τ ∈ {30,60,120,250}**, **p_exact ∈ {0.55,0.68,0.78,0.88}**,
**p2 ∈ {0.2,0.4,0.6}** (48 cells), scored by relative-squared-error loss against
four quantities the model most directly controls:

> unigram entropy H(W), type-token ratio (TTR), adjacent-identical rate, adjacent
> near-repeat rate.

> **Grid re-centering (important, honest note).** A first pass used
> p_exact ∈ {0.005…0.04}. That was mis-centered: with <4% exact copies almost every
> word is mutated into a brand-new type, pinning TTR at ~0.85–0.97 (real = 0.20) and
> entropy at ~15 bits (real = 10.3). The generator could not even reach its own
> tuning targets, making any held-out comparison meaningless. A quick probe showed
> the targets require p_exact ≈ 0.78, so the grid was re-centered there. This is
> still only three knobs; re-centering a search range is not adding degrees of
> freedom. Both grids are preserved in the log.

**Best fit:** τ = 250, p_exact = 0.78, p2 = 0.2 (loss 0.40).

### Held-out battery

Five independent tuned runs (seeds 101–505), mean ± σ. On each the **full phase 1 +
phase 2 battery** is recomputed with the *identical* estimators from `run_bpe.py`
and `run_wordorder.py` (HF BPE at vocab 500/1000/2000; shuffle-corrected bigram
info-gain and MI at d = 1,2,4,8,16 with N=10 shuffles; char conditional entropy
orders 0–4). These metrics were **not** used in tuning.

## Verdict table

Real Voynich from phases 1–2. Natural band = min–max over Latin/English/Italian.
"Match?" is versus **real Voynich** (✓ good, ~ partial, ✗ fail). Rows marked
**[tuned]** are inputs to the grid and are *not evidence* — they only confirm the fit
took.

| metric | real Voynich | generator mean ± σ | natural band | match? |
|---|---|---|---|---|
| unigram entropy H(W) **[tuned]** | 10.32 | 11.38 ± 0.13 | 9.05 – 11.17 | ~ |
| type-token ratio **[tuned]** | 0.203 | 0.178 ± 0.009 | 0.104 – 0.271 | ✓ |
| adjacent identical rate **[tuned]** | 0.0081 | 0.0109 ± 0.0004 | 0.000 – 0.0005 | ~ |
| adjacent near-repeat (ed≤1) **[tuned]** | 0.0461 | 0.0240 ± 0.0030 | 0.0016 – 0.0201 | ✗ |
| — *held out below* — | | | | |
| bigram info-gain (MI d=1) | 0.182 | 0.121 ± 0.007 | 0.258 – 0.736 | ✗ |
| MI d=2 | 0.069 | 0.121 ± 0.005 | 0.043 – 0.280 | ✗ |
| MI d=4 | 0.056 | 0.120 ± 0.006 | 0.012 – 0.033 | ✗ |
| MI d=8 | 0.050 | 0.120 ± 0.007 | 0.000 – 0.014 | ✗ |
| MI d=16 | 0.033 | 0.119 ± 0.007 | −0.001 – 0.008 | ✗ |
| **MI *shape*** | peak→plateau (decays 0.18→0.03) | **flat ~0.12** | decays to ~0 | ✗ |
| char entropy order 0 | 3.87 | 3.87 ± 0.03 | 3.93 – 4.10 | ✓ |
| char entropy order 1 | **2.14** | **2.96 ± 0.04** | 3.11 – 3.31 | ✗ |
| char entropy order 2 | 1.88 | 2.55 ± 0.04 | 2.58 – 2.65 | ✗ |
| char entropy order 3 | 1.81 | 2.02 ± 0.06 | 1.92 – 2.21 | ~ |
| char entropy order 4 | 1.71 | 1.54 ± 0.07 | 1.49 – 1.83 | ~ |
| BPE comp @500 | 4.147 | 3.303 ± 0.056 | 3.01 – 3.16 | ✗ |
| BPE comp @1000 | 4.594 | 4.146 ± 0.106 | 3.44 – 3.81 | ~ |
| BPE comp @2000 | 4.981 | 5.357 ± 0.187 | 3.86 – 4.55 | ✗ |
| BPE Zipf slope @2000 | −0.921 | −0.733 ± 0.018 | −0.95 – −0.76 | ~ |

## Reading the numbers

**1. The generator hits its tuned targets — which is worth nothing on its own.** TTR
and adjacent-identical rate land near real Voynich; entropy is within a bit. Expected
by construction. The whole test lives in the held-out rows.

**2. The long-range MI *plateau* is reproduced only as a degenerate artifact — the
*shape* fails outright.** The task's key question was whether the generator hits
Voynich's anomalous MI plateau at d = 8–16. Superficially yes: the generator's MI is
non-zero out to d=16 (0.12), unlike natural languages which decay to ~0. But the
resemblance is spurious. Real Voynich *peaks* at d=1 (0.18) and *decays* to a low
plateau (0.03–0.05). The generator is **dead flat at ~0.12 everywhere** — no
short-range peak (it *undershoots* real d=1) and a long-range value 3–4× too high.
A flat MI is exactly what an exp-decay copy window of width τ=250 must produce:
every distance ≪ 250 is coupled equally. The generator manufactures uniform
mid-range correlation, not Voynich's peak-then-plateau signature. **Held-out: fail.**

**3. Voynich's famous low character entropy is not reproduced.** The single most
cited Voynich statistic is its very low order-1 char entropy (~2.1 bits — a glyph is
almost determined by its predecessor). The generator sits at **2.96**, up in the
natural-language band (3.1–3.3), and its order-2 value (2.55) is likewise natural-
scale, not Voynich-scale (1.88). Nothing in the knob set moves it: mutations draw
replacement glyphs from real Voynich *context* distributions, which reproduces
natural-like conditional entropy, not the manuscript's ultra-rigid template rigidity.
The generator's char-entropy *curve shape* is wrong too — real Voynich drops steeply
then flattens (front-loaded predictability); the generator decays gradually like a
language. **Held-out: fail.**

**4. It produces the wrong *kind* of repetition.** Real Voynich's phase-2 signature
was **near-repeat enrichment** (`daiin daiin`, `chol chor` — ed≤1 pairs at 2.3×
chance). The tuned generator *under*-produces near-repeats (0.024 vs 0.046) while its
*exact*-repeat enrichment ratio overshoots wildly (11.9× chance vs real 2.5×). It
copies verbatim too readily and mutates-into-a-neighbour too rarely — the opposite
mix from the manuscript. The very perseveration phenomenon self-citation was invoked
to explain comes out mis-proportioned.

**5. BPE morphology: right league, wrong curve.** The generator compresses at
natural-language scale (decisively unlike char-shuffled gibberish at 2.2–2.6), and is
Zipfian — so it clears the low bar. But its compression curve is too steep: it
undershoots real Voynich at vocab 500 and overshoots it at 2000. Partial at best.

## The tensions (this is the core result)

The generator cannot satisfy the held-out metrics because the knobs are **coupled
against each other**:

- **TTR/entropy ⟂ adjacent-exact repeats.** Reaching real TTR (0.20) needs
  p_exact ≈ 0.78. At small τ that makes adjacent-*identical* repeats explode to
  7–14% (real 0.8%).
- **Adjacent repeats ⟂ MI decay.** The only way to tame the exact-repeat overshoot
  at high p_exact is a large recency window (τ=250, copy from far back). But a large
  τ **flattens the MI curve** — destroying the decay-to-plateau shape. Small τ would
  restore decay but re-explode adjacent repeats. You cannot get both.
- **Char entropy is immovable.** No setting of {τ, p_exact, p2} pulls order-1 char
  entropy from ~2.96 down to Voynich's ~2.14; it is set by the mutation model, which
  is deliberately outside the tuned knobs.

Fixing any one anomaly breaks another. The manuscript occupies a corner of the
statistic space this generator's parameters cannot jointly reach.

## Combined three-phase picture

| phase | probes | Voynich verdict |
|---|---|---|
| 1 — BPE morphology | compression, Zipf, token length | super-regular, *more* template-bound than any natural language; **not random** |
| 2 — word order | bigram info, MI d=1..16, near-repeats | real but *weak* short-range info; long-range **plateau** (topic-drift-shaped, not syntax); near-repeats **enriched** (anti-natural) |
| 3 — self-citation | can a copy-machine fake phases 1+2? | **no** — a tuned generator misses order-1 char entropy, the MI *shape*, and the near-repeat mix; internal tensions block a joint fit |

Reading all three together: Voynichese is **structured** (kills "random scribbles"),
its morphology is **too regular** and its syntax **too weak/oddly-shaped** for a
word-for-word cipher of ordinary prose (phases 1–2 disfavour that), **and** a simple
perseverative copy-generator can reproduce the gross morphology and Zipf but **not**
the fine structure that makes Voynich Voynich (phase 3). The profile that survives
all three is a **generative system with rigid word-internal rules and unusual,
slowly-varying word sequencing** — whether that system carries meaning (a constrained
real language, a nomenclator/positional encoding) or not (a *more sophisticated*
generator than the one tested here) is not settled by these data. What *is* settled:
the cheapest meaningless explanation — "a scribe just copied nearby words with
tweaks" in its simple form — **measurably fails held-out**, so meaning-bearing
hypotheses are not eliminated.

## Honest interpretation & limitations

- **Tuned metrics prove nothing.** Only the held-out failures (char entropy H1/H2,
  MI shape, near-repeat mix) carry weight. They are reported as such.
- **This is a *reimplementation*, not Timm & Schinner's exact algorithm.** Their
  published model is more elaborate (it copies whole word-token instances from the
  growing text with a richer edit model and reproduces several of these statistics in
  their own runs). A failure *here* refutes "self-citation is trivially able to fake
  everything," **not** "self-citation is impossible." A faithful port of their exact
  procedure is the obvious next step and could close some of these gaps.
- **Coarse 3-knob grid.** A wider search or a 4th–5th knob (e.g. a τ that decays a
  short-range peak on top of a long window, or a mutation model tuned toward low char
  entropy) might reduce specific tensions. The point of the coarse grid is to show
  the tensions *exist*, not to prove they are unbeatable.
- **EVA transliteration** (binding caveat from phases 1–2): glyph segmentation
  choices shape every word- and char-level number. A v101 replication would bound it.
- Single manuscript, Currier A/B pooled, ~38K words (all MLE entropies biased; the
  shuffle-delta design cancels unigram-level bias only approximately at the joint
  level). Comparison texts are edited print editions.

## Deliverables

- `phase03.md` — this file.
- `run_phase3.py` — generator + tuning grid + full battery (reproducible; seeds fixed).
- `make_chart_phase3.py`, `../charts/voynich_selfcite_chart.png` (+ `.txt` caption)
  — dark-parchment chart: MI decay + BPE compression, real vs synthetic.
- `phase3_results.json` — best params, full 48-cell grid, all held-out metrics
  (mean ± σ over 5 runs).
- `phase3_run.log` — full run log (both grid passes).
- `synth_run0.txt` — one example generated corpus (37,942 words) for inspection.

🜂
