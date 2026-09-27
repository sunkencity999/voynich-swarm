# WP8b / WP8b-A — The repair round: start-x recertification + contains-domain M3

*Builder: Cherubesque (seeds 664001/664002). Adversary: Smaug (seeds 778801/778802
@ B=4000 = 2× draws, 778803 disjoint human pass). DESIGN frozen 2026-09-26 (v1.0)
before execution; every stage boundary a git fact.*

## Design intent

WP8 ended at two terminal gates: an empty prereg contrast domain (→ certified fact A9)
and a CV start-x measurand that failed blind certification (ICC 0.081, herbal join
coverage 0/128). WP8b was the preregistered repair: fix the three adjudicated pipeline
failure modes (herbal plant-mask, red-paint mask, gutter-shading onset guard),
recertify under upgraded machinery (n≥100 spot lines, git-fact commit boundaries,
a new bootstrap-CI prong on the ICC), and — only if certified — run the M3 battery on
the redesigned **contains**-domain (pages whose opening line contains an or- variant;
census ZL 23 / IT 25, proven non-empty per the contrast-domain law adopted after WP8).

## Master verdict: **MEASURAND-FAILED — second consecutive negative case (adversary-confirmed, no overturns)**

| Gate | Outcome |
|---|---|
| Scan hash re-verification | PASS — 213/213 SHA256 (builder and adversary independently) |
| Stage 0a: pipeline repair | delivered — herbal joinable **0/128 → 27/128**, overall 24 → 49/206 |
| Stage 0b: certification | **FAILED all three prongs** — ICC(2,1) 0.084 (bar ≥0.8), median error **5.86 glyph widths** (bar ≤0.5), bootstrap CI lower −0.158 (bar ≥0.6) |
| Stage 1 (M3 contains-domain) | never ran; post-hoc census: or-arm floor would also have failed (7 joined < 15) |
| M3 / WP7 H-A kill rule | **still armed, still untested** |

## Finding 1 — the repair worked; the architecture is still wrong

The three frozen fixes did what they aimed at: herbal pages became joinable for the
first time (27/128), the red-pigment hole closed, and the balneo coverage rule was
non-vacuous and cleanly passed (balneo joins second-best, .368). But certification
failed by an order of magnitude anyway. The adjudicated failure architecture
(adversary ruling, binding): **whole-width y-profile band segmentation cannot certify
a blind start-x measurand on these scans** — two residual error classes trade off
directly: high-contrast page-edge/adjacent-page slivers admitted as onsets (the
contrast guard cannot kill them — they *are* high contrast), and genuine faint or
paint-adjacent first words absorbed by the plant-halo/contrast repairs (a new error
class introduced by the repair itself). The adversary reproduced the failure at ~8
glyph widths on his own disjoint, self-annotated 8-line sample — the failure is in
the pipeline, not the builder's readings.

## Finding 2 — a second independent blocker

Even a certified measurand would not have unlocked M3 at current coverage: the joined
or-arm is **7 pages** (Herbal 6, Balneo 1) of the 23-page ZL census, below the
preregistered floor of 15 (control arm 42 ≥ 30). Unlock requires or-arm coverage
≈65% of census pages — roughly triple today's herbal join rate.

## The machinery, validated twice

- **Git-fact stage boundaries** (adopted from WP8-A defects): measurement code
  committed *before* the corpus run; blind sample committed *before* human
  measurement; human measurements committed *before* the scorer existed;
  certification a separate later commit. Adversary audited every boundary by commit
  timestamp vs file mtime: all held.
- **The new CI prong is load-bearing:** even a point estimate just over the bar could
  not have certified (adversary CI lower bound −0.154 at B=4000) — the sampling-luck
  hole identified in WP8-A is closed.
- **Fabrication screen: CLEAN.** Sample and bootstrap streams reproduce exactly from
  seeds under independent adversary code; every quoted number matches the JSONs; the
  outcome is maximally self-disfavoring (the builder's new machinery killed his own
  repair, twice over); no statistic exists anywhere under the round root — seed
  664001's permutation stream was never consumed.

## Adversary defects and binding amendments (WP8b-A)

Defects (none affect any verdict): prose wall-clock drift (third occurrence — now a
campaign law: boundary times must be generated from `git log`/`stat`, never memory);
triage census not an exhaustive partition (the two named classes are real and
dominant, visually confirmed, but 16 left-tail lines carried no attribution);
builder-only annotation acceptable for FAIL, never for a PASS.

Binding amendments / **WP8c prerequisites**: (i) geometric edge-band kill +
block-aware segmentation replacing whole-width y-profile banding; (ii) or-arm
coverage ≥65% of census pages demonstrated *before* the human spot-check is spent;
(iii) preregistered ICC bootstrap resampling unit and a defined "pooled median" for
the balneo rule; (iv) a second annotator independent of the builder for any round in
which the bar could pass.

## Ledger deltas

- No-verdict record: WP8b MEASURAND-FAILED (second consecutive negative case), M3
  untested, kill rule armed.
- Campaign laws adopted: git-fact boundaries with generated timestamps; exhaustive
  triage partitions; second-annotator rule for passes.
- Method note: image-measurand certification machinery now validated end-to-end on
  two consecutive negative cases.

*Evidence: `SUMMARY.md`, `BUILD_LOG.md`, `infra/stage0_certification.json`,
`infra/coverage_report.json`, `verdicts-adversary/SUMMARY.md` in the round root
(private evidence tree; numbers mirrored in [CONSTRAINTS.md](../CONSTRAINTS.md)).*

🜂
