# WP8 / WP8-A — The Image Round: blind start-x measurand (M3 unlock) + U4

*Builder round 2026-09-26 (seeds 663001/663002 assigned at freeze — never used: no stage-1
statistic ever ran); adversary round (Smaug) same day (own seeds 777801/777802; the audit
was exhaustive rather than sampled — full-corpus SHA256 + dimension re-verification,
independent recount, independent ICC implementation). First round beyond the frozen IVTFF
text corpus; the certification machinery for image-derived measurands was itself part of
the preregistered contract. Design frozen 2026-09-25 (v1.0, joint builder+adversary).*

## Design intent

WP7 left L5-M3 (page-initial or- as a *placed* folio-boundary mark) NON-RUNNABLE because
the start-x measurand exists in no frozen text input. WP8's contract: acquire an
admissible scan corpus (resolution floor ≥1200 px text-block width), build a **blind
deterministic CV pipeline** (classical CV only, no vision models, no token-table imports)
for a per-line start-x measurand, **certify it at a stage-0 commit boundary** (blind
60-line human spot-check; bars ICC ≥ 0.8 OR median |diff| ≤ 0.5 glyph width) — and only
then run the WP7 H-A battery verbatim against M3's still-armed kill rule. Plus U4: an
explicitly exploratory page-image memo (L5-M2 lane), no verdict weight.

## Master verdicts (adversary-adjudicated)

| Gate | Verdict |
|---|---|
| Prereg T7a/b/c (WP7 H-A verbatim) | **NON-RUNNABLE — EMPTY PREREG DOMAIN**, adversary-confirmed by independent recount |
| Stage-0 measurand certification | **MEASURAND-FAILED (NOT CERTIFIED)**, adversary-confirmed by independent ICC |
| M3 kill rule (armed since WP7) | **CANNOT FIRE — M3 remains untested** |
| Fabrication screen | **CLEAN** (60/60 sample ids reproduced from seed; 213/213 SHA256 + dims re-verified; no hidden stage-1 statistic) |

The round terminated at TWO independent preregistered gates before any permutation,
bootstrap, or outcome×class statistic was computed. That is the machinery working.

## Finding 1 — the prereg contrast domain is EMPTY (new certified fact, ledger A9)

The inherited contrast — "page-initial lines whose FIRST token is or-class vs
control-class" — has an empty or- arm over the whole corpus: **0/206 pages in ZL and
0/206 in IT** (adversary recount from a raw re-parse, own line-ranking and class rules;
controls 10/6; first slots are gallows-dominated: pc 32, po 31, ko 14). Body-line arm
(T7b): 11 lines corpus-wide per transliteration — below any floor. or- *never* supplies
the first token of a page's first line: an absolute zero that sharpens the certified
opening-depletion facts (A2/A3) at the strongest opening position.

The contains-based domain (rank-1 line CONTAINS ≥1 or- token) IS non-empty — ZL 23 / IT
25 pages (12 of ZL's 23 in Herbal) — and is filed as a census only, for a future WP8b
prereg. It was deliberately NOT run as a statistic (see gate 2).

**Campaign law adopted (adversary wording):** *existence proofs must cover the contrast
domain — both arms non-empty at preregistered floors.* WP7 (measurand missing) and WP8
(contrast empty) failed one level apart on the same omission.

## Finding 2 — the CV measurand failed certification, and the gate held

Stage −1 worked: Beinecke direct was WAF-blocked and voynich.nu serves only 344px
thumbnails (both disclosed); the round used archive.org's copy of the Beinecke 2014
digitization — 213 files at ~2700–3000 × 3700–3900 px, folio mapping **proven** against
the Wayback-frozen Yale IIIF manifest (per-file JPEG dimensions must exactly match the
same-index canvas; SHA256 manifest committed). Median text-block width 2279 px ≥ the
1200 px floor.

The blind CV start-x pipeline processed 204/204 pages (7684 line bands) but joined only
24/206 token pages (Herbal 0/128 — drawings fragment the text block). The blind 60-line
spot-check (human measurements recorded before any comparison; sample reproduced 60/60
from the logged seed by the adversary):

```
bars:    ICC ≥ 0.8  OR  median |diff| ≤ 0.5 glyph width
result:  ICC(2,1) = 0.081   median |diff| = 4.46 glyph widths   (within ½ glyph: 5/59)
adversary recompute (independent ICC implementation): 0.0814 / 4.464 gw — match
sensitivity (excl. low-confidence): 0.135 / 4.06 gw — same verdict
```

Both prongs fail by ~9×, no knife-edge. QA triage (adversary-verified on the images):
onsets landing on gutter shading, red paint admitted as ink, faint strokes missed —
pipeline-attributable. Under the preregistered terminal rule, **no start-x statistic of
any kind was computed** — including the tempting NOT_PREREG contains-variant. Balneo
confound rule: balneo actually joins second-best (.421), but the rule as written proved
vacuous (pooled median coverage 0.0) — disclosed as degenerate, not scored a pass.

## U4 exploratory memo (no verdict weight)

Candidate generation only: (1) balneo has the tightest line spacing (pitch CV .418; herbal
loosest .812); (2) first-line emphasis INVERTED — first bands ~32% *lighter* than body
text, disfavoring rubric-like darkening (L5-M2's expected sign); (3) bands-per-page /
block width as covariates. Stroke-width lane not attempted (scans below the 2000 px bar
set at freeze).

## Adversary observations for WP8b

Three minor defects logged (none affecting verdicts): wall-clock labels in one BUILD_LOG
section; a thin mtime audit trail between human file and scoring (survives here because
the outcome is self-disfavoring and the sheets are structurally blind); stage-0 code
committed minutes after the measurand ran ("written before run" ≠ "committed before
run"). WP8b requirements: commit the human spot-check file BEFORE scoring runs; ≥100 spot
lines + a preregistered CI on the ICC; fix herbal segmentation, the paint mask, and
gutter-shading onsets before recertification.

## Key numbers

| Quantity | ZL | IT |
|---|---|---|
| Pages with a rank-1 paragraph line | 206 | 206 |
| rank-1 first token = or-class | **0** | **0** |
| rank-1 first token = control class | 10 | 6 |
| Body ranks 2–4 or--initial lines | 11 | 11 |
| Contains-variant domain (pages) | 23 | 25 |
| Scans acquired / dims-proven | 213 / 213 | — |
| Spot-check ICC(2,1) (bar ≥ 0.8) | 0.081 | — |
| Spot-check median |diff| (bar ≤ 0.5 gw) | 4.46 gw | — |
