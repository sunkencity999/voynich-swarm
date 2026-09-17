# Voynich-BPE Experiment

*2026-09-13 — workstation A, plain python (HF `tokenizers` 0.22.2), no LLM calls.*

**Question:** if you train a BPE tokenizer on the Voynich manuscript's EVA transliteration, does its merge/statistical structure look like a natural language or like gibberish?

## Methodology

1. **Source:** ZL3b-n.txt (Zandbergen–Landini transliteration v3b, 13/05/2025, IVTFF 2.0, Basic EVA), single fetch from voynich.nu/data/. Verified EVA content (1165× `daiin`, 264× `qokeedy`). See PROVENANCE.md.
2. **Cleaning** (`clean_ivtff.py`): dropped `#` comment lines and non-locus lines; stripped locus tags and all inline `<...>` / `{...}` annotations; `[x:y]` alternative readings resolved to the first alternative; `.` and `,` treated as word separators; lowercased; tokens containing anything outside `[a-z]` (unreadables `?`, high-ascii codes) dropped (289 tokens). Result: **230,958 chars, 38,946 words, 7,823 unique**.
3. **Comparison corpora**, cleaned the same way (Gutenberg headers stripped, accents folded, `[a-z]+` tokens only), all truncated to **224,987 chars** (the min, set by Latin):
   - **Latin** — Caesar, *Commentarii de Bello Gallico* V–VIII (PG #18837)
   - **English** — Austen, *Pride and Prejudice* (PG #1342)
   - **Italian** — Dante, *La Divina Commedia* (PG #1012)
   - **charshuf** — Voynich with all characters shuffled across the corpus, refilled into the same word-length skeleton (preserves char frequencies + word-length distribution; destroys morphology)
   - **wordshuf** — Voynich with word order shuffled (preserves morphology; destroys syntax)
   - Hebrew/Arabic transliteration: skipped (no clean, easily obtainable size-matched source).
4. **BPE:** HF `tokenizers` BPE (whitespace pre-tokenizer), trained per corpus at vocab 500 / 1000 / 2000, each corpus encoded with its own tokenizer.

## Results

| corpus | vocab | chars/token | Zipf slope (ranks 10–500) | r² | top-100 coverage | mean vocab-entry len |
|---|---|---|---|---|---|---|
| **voynich** | 500 | **4.147** | −1.119 | 0.937 | 0.645 | 4.20 |
| | 1000 | **4.594** | −0.977 | 0.981 | 0.545 | 4.69 |
| | 2000 | **4.981** | −0.921 | 0.990 | 0.486 | 5.14 |
| latin | 500 | 3.036 | −1.071 | 0.782 | 0.629 | 3.46 |
| | 1000 | 3.717 | −0.819 | 0.992 | 0.483 | 4.16 |
| | 2000 | 4.549 | −0.764 | 0.997 | 0.372 | 4.91 |
| english | 500 | 3.162 | −1.173 | 0.762 | 0.642 | 3.30 |
| | 1000 | 3.805 | −0.948 | 0.992 | 0.558 | 4.03 |
| | 2000 | 4.482 | −0.953 | 0.998 | 0.530 | 4.69 |
| italian | 500 | 3.012 | −1.086 | 0.909 | 0.666 | 3.25 |
| | 1000 | 3.436 | −0.961 | 0.993 | 0.575 | 3.83 |
| | 2000 | 3.864 | −0.950 | 0.997 | 0.525 | 4.43 |
| charshuf | 500 | 2.168 | −1.322 | 0.964 | 0.718 | 2.40 |
| | 1000 | 2.371 | −1.217 | 0.951 | 0.599 | 2.67 |
| | 2000 | 2.604 | −1.102 | 0.940 | 0.473 | 2.85 |
| wordshuf | 500–2000 | identical to voynich | | | | |

Full numbers: `bpe_results.json`. Chart: `voynich_bpe_chart.png`.

## Reading the numbers

**1. Voynich decisively does NOT tokenize like gibberish.** The char-shuffled control collapses: compression 2.2–2.6 chars/token (vs 4.1–5.0 for Voynich), short merges (mean vocab-entry length 2.4–2.9 vs 4.2–5.1), and a flat-then-cliff Zipf curve (the dashed red bulge in the plot — too many equally-common short tokens, then nothing). BPE finds essentially no reusable substructure once morphology is destroyed. Voynichese is ~90% more compressible than its own shuffled ghost.

**2. Voynich clusters with the natural languages on every metric** — Zipf slope at vocab 2000 (−0.92, between English −0.95 and Latin −0.76, r²=0.99), top-100 coverage (0.49, inside the natural range 0.37–0.53), merged-token length distribution, and the *shape* of the compression-vs-vocab curve (smooth log-linear growth, same slope family as Latin/English/Italian).

**3. But Voynich compresses *more* than any real language at every vocab size** (4.15 at v=500 — where the natural languages sit at 3.0–3.2). It's not just "like language" — it's *super-regular*. BPE exploits its rigid word-template morphology (qo- ol- ch- prefixes, -aiin -edy -ol suffixes) more efficiently than it can exploit real Latin or English morphology. That's the quantitative face of the long-observed weirdness: Voynichese words are drawn from an unusually constrained combinatorial grammar, with lower per-word entropy than natural languages.

**4. The word-shuffled control is *exactly* identical to real Voynich** — expected, since whitespace-pre-tokenized BPE is blind to word order, but it's a useful negative result: **this method cannot see the manuscript's claimed word-order pathology at all.** Anyone claiming BPE-style statistics prove Voynichese is language is only probing morphology; the strongest gibberish arguments (low-info word order, line-as-unit effects) live precisely where BPE is blind.

## Verdict

On BPE-visible structure (morphology and token distributions), **Voynichese lands firmly on the natural-language side of the divide and nowhere near random gibberish — but it overshoots**, showing *more* internal regularity than Latin, English, or Italian. This is consistent with: a real language under a highly regular encoding, a constructed/cipher system with a word-template generator, or a "glossolalia-like" generative process with strong morphological habits. It is *inconsistent* with characters being random scribbles.

## Caveats (honest ones)

- **EVA is itself an interpretive transliteration.** Glyph segmentation choices (is `iin` one glyph or three?) directly inflate/deflate BPE's apparent gains. Some of Voynich's compression advantage may be an artifact of EVA decomposing single glyphs into multi-char sequences (e.g. `ch`, `sh`, `aiin`) that BPE then trivially re-merges. A v101-alphabet replication would bound this.
- **Similar statistics ≠ language.** Zipf laws and compressibility arise from many generative processes (including some mechanical ones, e.g. Rugg-style grille tables tuned to produce them).
- Single transliteration, single ms; the two Currier "languages" (A/B) were pooled.
- Comparison texts are edited print editions, not medieval scribal text with abbreviations — real 15th-c. Latin manuscript orthography would likely compress somewhat better than the Gutenberg edition here.
- Vocab 500–2000 on 225KB corpora is small-scale; ratios, not absolute values, carry the signal.

## Files

- `ZL3b-n.txt`, `000_README.txt`, `PROVENANCE.md` — raw source + provenance
- `clean_ivtff.py`, `prepare_corpora.py`, `run_bpe.py`, `make_chart.py` — pipeline
- `voynich_clean.txt`, `corpus_*.txt`, `corpus_stats.json` — corpora
- `bpe_results.json`, `plot_data.json`, `voynich_bpe_chart.png` — results

🜂
