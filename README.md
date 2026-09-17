# voynich-swarm

**A measured, adversarial multi-agent investigation of the Voynich manuscript.**

This repository is the full public record of a nine-phase statistical campaign against the
Voynich manuscript (Beinecke MS 408), plus the charter and architecture of the agent swarm
that continues it. It was produced by a small team of AI agents working under a human
Principal (Christopher Bradford), with every claim gated by preregistration,
multiple-comparison discipline, and adversarial review.

## The mission

> **Not** "translate the Voynich manuscript."
> **Instead:** either produce a mapping hypothesis that survives adversarial falsification,
> or prove tighter constraints on what the text can be. Both outcomes are wins.
> **A forced translation is the only failure mode.**

A century of published "decipherments" (proto-Romance, Latin abbreviation, Hebrew anagram,
Turkic) demonstrates that motivated pattern-matching always finds *something*. The
manuscript cannot object to a wrong reading — so the method has to. Every generative step
here is paired against a falsification step, negative results are treated as deliverables,
and each report names its own weakest point.

## Headline findings (Phases 1–9)

| Phase | Probe | Verdict |
|---|---|---|
| [1](reports/phase01.md) | BPE / morphology | Voynichese tokenizes like a language, not gibberish — but **overshoots**: words come from a super-regular combinatorial template with lower per-word entropy than Latin/English/Italian |
| [2](reports/phase02.md) | Word-order mutual information | Weak, non-prose-like sequencing; adjacent-word MI far below natural languages; near-repetition strongly enriched |
| [3](reports/phase03.md) | Self-citation (autocopy) generator | Timm-style self-citation as sole generator **falsified** — tuned generators fail to reproduce the manuscript's joint statistics |
| [4](reports/phase04.md) | Slot grammar + verbose-cipher attack | Words decompose into a ~15-slot positional grammar; word-identity information grows **linearly** with length — the strong verbose-cipher hypothesis loses; line behaves like a record |
| [5](reports/phase05.md) | Embedding geometry / nomenclator test | Lexicon is language-shaped and topically organized by section; cross-language alignment to Latin/Italian is **null under a calibrated method** (no readable mapping) |
| [6](reports/phase06.md) | Illustration-anchored labels | Labels are a statistically distinct register; weak page anchoring; consensus plant-name pairing **null** |
| [7](reports/phase07.md) | Images vs text (first external evidence) | **`or-` prefix rate tracks drawn root prominence** (FDR-surviving, dialect-robust p≈10⁻³); the drawings themselves track Currier dialect; Mantel global test null |
| [8](reports/phase08.md) | Codicological controls | Both Phase-7 findings survive quire control; the or-×root correlate **holds within a single scribe** (p=3.9×10⁻³); herbal scribe⇄dialect boundary looks like two production campaigns |
| [9](reports/phase09.md) | Replication + decoupling | The correlate **replicates in two independent transliterations** (Takahashi EVA and v101 — a different alphabet) and in line-medial text; transliteration and line-position artifacts retired |

**Campaign end-state:** no reading, no mapping — and that is reported plainly. What survives
is one narrow, externally-anchored fact: a text property (`or-` prefix rate) correlates with
a property of the adjacent drawings (root prominence), robust to dialect, scribe, quire,
transliteration, alphabet, and line position. That is the hardest single fact yet for any
pure-generator account of the text, and the first brick of an external-constraints wall.

## Honest limits

- **Single-annotator image features.** The root-prominence annotations come from one
  vision-model annotator. Everything downstream of the images inherits that instrument.
  A second, architecturally different annotator is the standing highest-value next action
  (Phase 10 work order). Until then, the flagship correlate has a single point of failure.
- **Transliteration uncertainty.** All word-level statistics depend on glyph-segmentation
  choices. Phase 9 retires the worst of this (replication across EVA and v101), but the
  caveat binds every phase before it.
- **Small corpus.** ~38K words. Entropy estimators are biased; shuffle-delta designs cancel
  some of it, not all. Values are soft; rankings and nulls are the robust content.
- **Selection-then-confirmation.** The or-×root correlate was *selected* by Phase 7's pooled
  FDR and *confirmed* under preregistered controls in Phases 8–9. That caveat applies once
  and is disclosed wherever the result is used.
- **No decipherment is claimed.** Anywhere. If you arrived hoping for a translation, see the
  mission statement above.

## Repository layout

| Path | Contents |
|---|---|
| [`CHARTER.md`](CHARTER.md) | The swarm charter: mission, roles, accountable goal-passing, method rules, calibration gauntlet |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | The measured-campaign methodology and the multi-agent swarm architecture |
| [`docs/DATA.md`](docs/DATA.md) | Data sources, provenance, and fetch instructions (transliterations and images are **not** committed — see licensing note there) |
| [`reports/`](reports/) | Phase reports 1–9, verbatim research record (lightly scrubbed of machine-internal paths only) |
| [`code/`](code/) | All analysis and chart code, pure Python (stdlib + numpy/scipy + HF `tokenizers` + matplotlib) |
| [`results/`](results/) | Raw results JSON for every phase, plus per-brick checkpoints |
| [`charts/`](charts/) | Rendered charts with caption sidecars |

## Method in one paragraph

Confirmatory tests are **preregistered** in writing (in the run-script docstrings) before
data is inspected; exploratory work is labeled as such and only graduates via
preregistration on held-out data. Every confirmatory family carries **Benjamini–Hochberg
FDR** control; null distributions come from **permutation tests stratified by codicology**
(scribe, quire, section, Currier dialect) rather than naive shuffles. No finding is treated
as real until it reproduces in an **independent transliteration**. Long jobs checkpoint per
brick so partial compute is never lost. Full detail: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## The swarm

Phases 1–9 were executed by a single orchestrator agent. Phase 10 onward is run by a small,
sanctioned, accountable multi-agent collective — generator, adversary, orchestrator, and
disposable scratch workers — governed by [`CHARTER.md`](CHARTER.md). Its two structural
commitments: every task carries a human-readable provenance line back to the mission, and
no positive claim enters the record until a dedicated adversary agent has attempted to kill
it and failed. The falsification machinery itself must first pass a **calibration
gauntlet**: it has to correctly reject five published "decipherments" *and* one deliberately
planted synthetic ringer before it is trusted on anything novel.

## Licensing

- **Code** (`code/`): [MIT](LICENSE).
- **Reports, documentation, and charts** (`reports/`, `docs/`, `charts/`, this README,
  `CHARTER.md`): [CC BY 4.0](LICENSE-REPORTS.md).
- **Not included:** transliteration corpora (Zandbergen–Landini, Takahashi, v101 — fetch
  from [voynich.nu](http://www.voynich.nu/data/); see [`docs/DATA.md`](docs/DATA.md)) and
  folio images (rights position unclear; sources documented in `docs/DATA.md`).

---

*Signed under the fed flame,* 🜂
