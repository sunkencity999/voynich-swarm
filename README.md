# voynich-swarm

**A measured, adversarial multi-agent investigation of the Voynich manuscript.**

This repository is the full public record of a statistical campaign against the Voynich
manuscript (Beinecke MS 408): nine solo phases, the charter and architecture of the agent
swarm that continues it, and the swarm's adversarially-verified rounds (WP1–WP8) with their
certified constraint ledger. It was produced by a small team of AI agents working under a human
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

**The campaign's core product is [`CONSTRAINTS.md`](CONSTRAINTS.md)** — the certified
constraint ledger: every structural fact that survived preregistration, adversarial
recomputation, and folio-cluster bootstrap, stated as a falsifier any candidate
translation or theory must satisfy.

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

## The swarm rounds (Phase 10 onward) — current status

The multi-agent swarm has since completed **five adversarially-verified rounds**
(2026-09-18 → 2026-09-23), each a preregistered builder battery followed by an independent
adversary round that recomputes every headline number from primary data with its own code,
nulls, and seeds. Full round records: [`rounds/`](rounds/).

| Round | Slate | Outcome |
|---|---|---|
| [WP1 — calibration gauntlet](rounds/wp1-calibration.md) | 5 published decipherments + 1 planted synthetic ringer | **All 6 correctly rejected** (18/18 verdicts across both transliterations); the falsifier earned trust before touching anything novel |
| [WP2 / WP2-A — mechanism discrimination](rounds/wp2.md) | 8 candidate mechanisms for the or-×root correlate | 6 disfavored or confounded; the correlate certified content-linked (survives full production-order conditioning, ΔR²≈.047, p=.001 both translits); a planted fabricated dossier caught by the adversary's fingerprint screen |
| [WP3 / WP3-A — the or- system](rounds/wp3.md) | linguistic vs process mechanisms (H1–H4) | Master axis: **process-leaning** — no context selectivity; or- = closed prefix family of free stems, appended as a line-final STEP; the one directional "decay" signal killed by the adversary as a forking path |
| [WP4 / WP4-A — notation mechanisms](rounds/wp4.md) | N1–N4 | No mechanism supported; discovery of **folio-opening (first-paragraph) enrichment** (p=.001/.001), the only strong unexplained signal; two knife-edge results declared non-certifiable rather than spun |
| [WP5 / WP5-A — opening-boundary battery](rounds/wp5.md) | preregistered test of the opening effect | **Folio-cluster certified**: or- is enriched in a page's first paragraph — both faces, both transliterations, robust to heading geometry, section-modulated (balneo negative); Currier-language specificity UNRESOLVED |
| [WP6 / WP6-A — incipit-index morphology test](rounds/wp6.md) | prereg test of L5-M1 ("page-initial or- is a repeated formula") | **KILLED, adversary-confirmed** — page-initial or- is *more* lexically diverse than body lines; the opening concentration is not a formula. WP7: M3 geometry + M2 image round |
| [WP7 / WP7-A — M3 geometry + variety cross-link](rounds/wp7.md) | prereg test of L5-M3 (start-x geometry) and the first-line-variety→A7 mechanism link | **H-A NON-RUNNABLE** — the start-x measurand exists in no frozen input (adversary-verified, both translits); needs a blind image-annotation round. **H-B KILLED, adversary-confirmed** — wrong-sign ρ = −0.600: first-line variety is anti-correlated with or- opening enrichment. The image/vision round is now the live path |
| [WP8 / WP8-A — image round: blind start-x + U4](rounds/wp8.md) | acquire admissible scans, certify a blind CV start-x measurand at a stage-0 gate, then run the WP7 M3 battery verbatim | **NO VERDICT, two terminal gates (adversary-confirmed):** the prereg contrast domain is EMPTY — or- NEVER supplies a page's first token (0/206 both translits, new certified fact A9) — and the CV measurand FAILED blind certification (ICC 0.081 vs ≥0.8; median error 4.46 glyph widths). No statistic computed; the stage-0 gate held. WP8b: pipeline fix + contains-based prereg (domain proven non-empty: 23/25 pages) |

**Headline certified fact:** *or- is enriched in the opening paragraph of the written
page* — page-physical (recto and verso alike, no quire structure), certified at
folio-cluster level in both transliterations, robust to geometric heading-likeness, and
section-modulated with the balneological section negative. Alongside it, the certified
profile now includes the content-linked root correlate, a corpus-wide
depleted-at-openings / enriched-at-endings positional grammar (line-final step + a
paragraph-terminal gradient), closed-prefix-family composition, and absence of linguistic
context-selectivity. Every certified fact, with effect sizes, p-values, and its
certifying round: [`CONSTRAINTS.md`](CONSTRAINTS.md).

**Live threads (L5):** (1) the one-line-heading question — enrichment beyond the opening
paragraph's first line is permutation-strong but cluster-uncertified at every resampling
grain; blind semantic heading annotation is the identified discharge path. (2) the Currier
axis — language specificity of the opening effect is unresolved in both directions.

The record keeps its failures on the front page: two fabrication plants caught (that is the
screen working), several of the campaign's own draft claims downgraded or killed by its own
adversary (H1's particle reading, H2's directional residue, WP5's "A-language retirement"
overclaim), and every knife-edge result filed as non-certifiable instead of rounded to a
conclusion.

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
| [`CONSTRAINTS.md`](CONSTRAINTS.md) | **The certified constraint ledger** — Tier-A facts any theory must reproduce, Tier-B supported-but-uncertified observations, Tier-C retired framings |
| [`rounds/`](rounds/) | Swarm round records WP1–WP8: design intent, master verdict, adversary outcome, key numbers per round |
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
