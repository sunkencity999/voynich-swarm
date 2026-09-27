# WP8c / WP8c-A — The rebuild round: block-aware segmentation + the coverage hard gate

*Builder: Cherubesque (seeds 665001/665002). Adversary: Smaug (seed 775001, fully
independent recompute — own hashes, own token parse, own join implementation written
from the frozen join-spec text). DESIGN frozen 2026-09-26 (v1.0) before execution;
all stage boundaries git facts.*

## Design intent

WP8b's adversary round adjudicated the failure architecture (whole-width y-profile
banding) and set four binding prerequisites for any successor. WP8c implemented them:
**block-aware segmentation** (band within ink blocks, not across the page) with a
**geometric edge-band kill**, a **hard coverage gate** (joined or-arm ≥ 15/23 census
pages, demonstrated *before* any human budget is spent), a two-annotator
certification protocol for any potential pass, and preregistered bootstrap unit +
pooled-median definitions. Verdict space included an honest early exit:
COVERAGE-FAILED, terminal.

## Master verdict: **COVERAGE-FAILED at the Stage C hard gate — terminal (adversary-confirmed, no overturns)**

| Gate | Outcome |
|---|---|
| Scan hash re-verification | PASS — 213/213 SHA256 (builder and adversary independently) |
| Stage R: rebuild | delivered — overall joined coverage **49 → 74/206** (herbal 27 → 47/128); hard-edge junk-onset class halved (21 → 11) |
| Stage C: coverage gate | **FAILED** — joined or-arm **9/23** vs bar ≥ 15 (control 65 ≥ 30 passed) |
| Stage 0 / Stage 1 | never ran — no blind sample drawn, 0/100 human budget spent, no statistic, seed streams unconsumed |
| M3 / kill rule | **still armed, still untested** |

## Finding 1 — the bar was structurally unreachable

Five of the 23 or-census pages have no dedicated single-folio canvas in the scan set
(foldout/multi-up sheets), so the structurally computable ceiling was **18/23** —
the preregistered bar of 15 was reachable only in principle, and the pipeline
managed 9. The adversary independently identified exactly the same 5 no-canvas
pages and confirmed the identical 9-page joined or-arm list. This produced a new
campaign law (below): a coverage bar must quote its structural ceiling at freeze.

## Finding 2 — coverage and onset fidelity are coupled

The rebuild's exhaustive failure-triage census (86 unjoined-or-defective lines;
partition sums exactly) shows the geometric edge kill worked as adjudicated
(edge-sliver class 21 → 11) — but the **absorbed-first-word class worsened 23 → 62**,
with census median error 4.79 glyph widths. Every repair that adds joins tends to
eat first words; every guard that protects first words drops joins. The builder's
self-disfavoring disclosure, adversary-confirmed: even had the coverage gate passed,
certification would likely have failed. This coupling is now a binding joint-gating
requirement for any successor.

## The adversary round (WP8c-A)

Smaug reproduced **every gate number exactly** — the 9/23 or-arm (identical page
list), control 65, all seven per-section coverage cells in both transliterations,
the or-census (ZL 23 / IT 25) from his own rank-1 token parse, and the full triage
partition including its median — using zero builder analysis code. He attacked the
logged deviations directly: the r4→r5 freeze decision (builder froze the build with
the *lower* or-arm count) was verified self-disfavoring from the QA logs themselves,
and the two coverage-favorable parameter deviations could only have masked deeper
failure, never manufactured a pass. Visual spot-checks on his own raw-scan crops
confirmed joined pages band correctly and excluded pages were honestly excluded.
Fabrication screen: clean.

Defects: one binding wording correction (structural exclusion count is **5**, not 6;
the ceiling arithmetic 23−5=18 was already correct) and one hygiene note (two
counting scripts committed with their outputs rather than strictly before — no
discretion existed, spec frozen upstream; now a law regardless).

## Binding amendments (WP8c-A)

- **WP8d prerequisites:** no further round in this design family without
  (a) foldout/canvas handling or a gate defined over canvassed-joinable pages,
  (b) a join rule robust to small band-count noise without corrupting onsets,
  (c) a demonstrated fix for the absorbed-first-word class — with coverage and
  fidelity gated **jointly**.
- **New campaign law:** every coverage bar must quote its structurally computable
  ceiling from frozen inputs at freeze time; a bar above its ceiling is invalid
  prereg. Counting scripts for hard gates commit before they run.

## Ledger deltas

- No-verdict record: WP8c COVERAGE-FAILED (terminal), M3 untested, kill rule armed —
  M3 now blocked four independent ways across WP7/WP8/WP8b/WP8c.
- Campaign law adopted: ceiling-quoted coverage bars + pre-committed gate counters.
- Method note: the honest-early-exit design worked — the round terminated before
  spending any human budget, exactly as preregistered.

*Evidence: `SUMMARY.md`, `BUILD_LOG.md`, `infra/coverage_report.json`,
`qa/r3_triage.json`, `verdicts-adversary/SUMMARY.md` in the round root (private
evidence tree; numbers mirrored in [CONSTRAINTS.md](../CONSTRAINTS.md)).*

🜂
