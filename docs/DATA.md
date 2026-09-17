# Data sources and provenance

The analysis code in `code/` expects the source corpora described below to sit in the
working directory. **None of the third-party corpora or manuscript images are committed to
this repository** — they are other people's work, redistributed under unclear or
restrictive terms. Everything here is fetchable in minutes; exact provenance for the runs
in `reports/` is recorded below.

## 1. Voynich transliterations (voynich.nu)

All transliterations come from René Zandbergen's site, in IVTFF format:
<http://www.voynich.nu/data/>

| File | What it is | Used in |
|---|---|---|
| `ZL3b-n.txt` | Zandbergen–Landini transliteration v3b (2025-05-13), IVTFF 2.0, Basic EVA, complete (all 5,389 loci) | Phases 1–8 (primary), 9 |
| `IT2a-n.txt` | Takahashi transliteration (IVTFF packaging), EVA | Phase 9 replication |
| `GC2a-n.txt` | Glen Claston transliteration, **v101 alphabet** (independent glyph inventory, not EVA) | Phase 9 replication |

Fetch:

```bash
curl -O http://www.voynich.nu/data/ZL3b-n.txt
curl -O http://www.voynich.nu/data/IT2a-n.txt
curl -O http://www.voynich.nu/data/GC2a-n.txt
```

Provenance of the record in this repo: `ZL3b-n.txt` fetched 2026-09-13 (411,671 bytes,
single fetch); verified EVA content by canonical token counts (1,165 × `daiin`,
264 × `qokeedy`). `IT2a-n.txt` and `GC2a-n.txt` fetched 2026-09-16/17 for Phase 9.

Cleaning: `code/clean_ivtff.py` (drops comment/non-locus lines, strips locus tags and
inline `<...>`/`{...}` annotations, resolves `[x:y]` alternate readings to the first
alternative, treats `.`/`,` as word separators, drops tokens with unreadables). The IVTFF
format spec lives at <http://www.voynich.nu/software/ivtt/IVTFF_format.pdf>.

## 2. Comparison corpora (Project Gutenberg)

Plain-text, cleaned identically (`code/prepare_corpora.py`), truncated to a common size
(~225 KB, set by the Latin corpus):

| Corpus | Work | Gutenberg # |
|---|---|---|
| Latin | Caesar, *Commentarii de Bello Gallico* V–VIII | 18837 |
| English | Austen, *Pride and Prejudice* | 1342 |
| Italian | Dante, *La Divina Commedia* | 1012 |

Two synthetic controls are derived from the Voynich corpus itself by
`code/prepare_corpora.py`: **charshuf** (characters shuffled corpus-wide, refilled into the
same word-length skeleton) and **wordshuf** (word order shuffled).

## 3. Folio images (Phases 7–9)

Feature annotation used scans of the herbal (and later pharmaceutical/balneological)
folios. **Images are not committed** — the manuscript scan rights position is ambiguous
(Yale Beinecke Library digital collection). Sources:

- Beinecke MS 408 digital scans: <https://collections.library.yale.edu/catalog/2002046>
- Per-folio pages with images and transliteration context: <http://www.voynich.nu/folios.html>

`code/download_folios.py` and `code/download_folios_phase9.py` fetch the folio images used
(herbal set, then 35 pharma/balneo folios) into a local `folios/` directory.

Image features were extracted by a **local vision-language model** used strictly as an
annotator (fixed prompt, temperature 0.1, strict-JSON output; see `code/extract_features.py`
and `code/extract_features9.py` — the endpoint constant points at any OpenAI-compatible
local server). The resulting annotations *are* committed: `results/phase7_features.json`,
`results/phase9_features.json` (partial second-annotator run). All downstream statistics
are classical permutation tests — no LLM is involved in any inference step.

## 4. Plant identifications (Phase 6)

- ZL per-page Plant ID annotations (Petersen / O'Neill / Holm / Voynich / Zandbergen
  attributions), embedded in `ZL3b-n.txt`; extracted to `results/phase6_zl_plantids.json`.
- E. Sherwood, *The Voynich Botanical Plants*,
  <https://www.edithsherwood.com/voynich_botanical_plants/>
- D. Scott identifications as cited by Sherwood (Kennedy & Churchill 2004, p. 164).

## 5. What is committed

- `results/*.json` — our own computed results, checkpoints, and annotations (ours, CC BY 4.0).
- `charts/*.png` + `.txt` captions — our own renders (CC BY 4.0).
- Not committed: transliteration files, raw/cleaned corpora, `.npz` intermediates
  (regenerable by the phase scripts from the sources above), run logs, and folio images.
