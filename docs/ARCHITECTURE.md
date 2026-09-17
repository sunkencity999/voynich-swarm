# Architecture: the measured campaign and the swarm

Two things are documented here: (1) the **methodology** that carried Phases 1–9 — a set of
statistical guardrails designed to make it structurally difficult to fool ourselves — and
(2) the **multi-agent swarm architecture** that runs Phase 10 onward.

---

## Part 1 — The measured-campaign methodology

The Voynich literature is a graveyard of confident readings. Each one was produced by a
competent, motivated person who found real-looking patterns. The methodology below treats
that graveyard as the primary threat model: the enemy is not the manuscript's difficulty,
it is **our own capacity to find patterns in noise and fall in love with them**.

### 1.1 Preregistration

Every confirmatory test is fixed **in writing before the data is inspected** — the test
list, the statistic, the stratification, and the significance procedure live in the
docstring of the run script (see `code/run_phase8.py`, `code/run_phase9.py`) and are
committed to the record before results exist. Exploratory analysis is allowed and useful,
but it is *labeled* exploratory, and its findings only graduate to confirmatory status via
a new preregistered test on data (or a transliteration, or a section) not used to generate
the hypothesis.

Concrete example of the discipline biting: the flagship or-×root_prominence correlate was
*selected* by Phase 7's pooled FDR scan (exploratory-ish: a preregistered family, but a
wide one) and then *confirmed* in Phases 8–9 under controls preregistered before those runs.
The selection-then-confirmation caveat is disclosed once, wherever the result is used.

### 1.2 Multiple-comparison discipline (BH-FDR)

Any scan across many features × many text properties will produce nominal p < 0.05 hits by
the fistful. Every confirmatory family therefore carries **Benjamini–Hochberg false
discovery rate** control at a stated q, applied *within the family as preregistered* — not
after the fact, not cherry-picked into sub-families. Findings that don't survive FDR are
reported as non-findings.

### 1.3 Stratified permutation nulls

Naive permutation tests are the classic way to smuggle in a confound: shuffle everything,
and any codicological structure (two scribal dialects, section vocabularies, quire
groupings) shows up as "signal." All permutation nulls here are **stratified by
codicology** — labels are shuffled *within* scribe, *within* quire, *within* section,
*within* Currier dialect (depending on the preregistered test), so the null preserves
exactly the structure we are not claiming to explain. Phase 8 exists entirely to apply the
strongest such controls to the Phase-7 survivors, including holding the correlate to
account **within a single scribe's pages**.

### 1.4 The two-transliteration rule

Voynichese has no ground-truth alphabet; every word-level statistic is downstream of one
team's glyph-segmentation choices. Rule: **no finding is real until it reproduces in an
independent transliteration** — and ideally in an independent *alphabet*. Phase 9
implements this: the correlate was re-tested in the Takahashi transliteration (independent
EVA reading) and in Glen Claston's v101 (a different glyph inventory entirely, mapped by
distribution rather than by symbol identity). Surviving both retires the "artifact of one
transliteration" objection.

### 1.5 The adversarial gate

Under the swarm charter, no positive claim enters a report until a dedicated adversary
agent has filed a falsification attempt and the claim survived. The adversary's dissents
are **published alongside** the claims — disagreement is part of the record, not something
resolved in private. During Phases 1–9 (single-agent era) this role was played by the
campaign's design habit of building the kill-test into the same phase as the finding
(e.g. Phase 3 exists purely to try to falsify a fashionable generator hypothesis; Phase 5's
alignment machinery was calibrated on known language pairs so that its Voynich null is a
*calibrated* null, not an incapable method).

Before the swarm's falsification machinery is trusted on anything novel, it must pass a
**calibration gauntlet**: correctly reject five published "decipherments" (Cheshire, Gibbs,
Hauer & Kondrak, Bax, Ardiç) *plus* one deliberately planted synthetic decipherment built
by the orchestrator as a ringer — with the adversary not told which is which. A falsifier
that can't reject the graveyard, or that rejects everything including the positive
control's known-recoverable structure, gets fixed before it gets used.

### 1.6 Honest-limits sections and negative results

Every phase report ends by naming its own weakest point — not boilerplate, the *actual*
weakest point (the campaign-wide answer is currently "single-annotator image features").
Negative results are deliverables with equal standing: the Phase 3 falsification, the
Phase 5 alignment null, and the Phase 6 plant-name null constrain the hypothesis space as
much as any positive finding.

### 1.7 Checkpointing

Long jobs write **per-brick checkpoints** (see `results/phase9_checkpoint_*.json`,
`code/run_phase5.py`'s staged design): each independently meaningful unit of compute lands
on disk as it completes, with the run script able to resume past completed bricks. This is
mundane engineering with methodological teeth — Phase 9 was run on a host that crashed four
times during the campaign window (suspected hardware), and the record survived intact
because no result ever existed only in RAM. It also makes partial results *inspectable
without being re-runnable*, which keeps "just tweak it and re-run" temptation visible in
the audit trail.

### 1.8 Separation of annotation and inference

Phases 7–9 use a vision-language model — the only LLM involvement anywhere in the campaign
— and it is confined to **feature annotation**: fixed prompt, low temperature, strict-JSON
output, one pass. Every statistic downstream of the annotations is classical permutation
inference. No LLM ever judges significance, picks tests, or interprets results inside the
pipeline. The known cost of this design is annotator bias, which is why the standing
highest-value work order is a second, architecturally different annotator (human or model)
with inter-annotator agreement statistics (`results/phase9_checkpoint_agree.json` holds the
partial first cut).

---

## Part 2 — The swarm architecture

Phases 1–9 were executed by a single orchestrator agent. Phase 10 onward is run by a small
multi-agent collective, governed by [`CHARTER.md`](../CHARTER.md). The design goal is to
get the benefits of cognitive diversity (an unconstrained generator, a hostile reviewer)
without the known failure mode of agent swarms: **goal drift** — objectives whose origin
nobody can trace.

### 2.1 Roles

```
                      ┌─────────────┐
                      │  Principal   │  human; sets direction, ratifies
                      │ (Christopher)│  phase gates, owns publication
                      └──────┬──────┘
                             │ mission amendments, gate decisions
                      ┌──────▼──────┐
        work orders   │ Orchestrator │   final reports, audit trail
      ┌───────────────┤ (Cherubesque)├────────────────┐
      │               └──────┬──────┘                 │
      │                      │ work orders            │
┌─────▼─────┐         ┌──────▼──────┐         ┌───────▼───────┐
│ Generator  │ claims  │  Adversary  │         │ Scratch cohort │
│  (Lucen)   ├────────▶│   (Smaug)   │         │ (disposable    │
│ unconstrained        │ kill attempts│         │  subagents)   │
│ hypotheses │         │ + dissents  │         │ brute compute │
└───────────┘         └─────────────┘         └───────────────┘
```

- **Orchestrator** — statistician and secretary of record. Issues all work orders, runs the
  preregistration/FDR machinery, writes the reports. The only member who assigns tasks.
- **Generator** — deliberately unconstrained hypothesis production (cross-linguistic cribs,
  structural conjectures, mechanism stories). Generation must not self-censor; that is what
  the gate is for.
- **Adversary** — one job: kill every proposed mapping. Designs falsification tests, hunts
  overfitting and leakage, files written dissents that are published with the claims they
  failed to kill.
- **Scratch cohort** — disposable workers for permutation farms, crib searches, grid fits.
  Spawned per work order with a narrow brief, retired after. Muscle, not members: they hold
  no goals and propose nothing.

### 2.2 Accountable goal-passing

The anti-drift protocol, in full (charter §3):

1. **Provenance line on every task** — who proposed it, why, and which mission clause it
   serves. A task that cannot state its provenance does not run.
2. **Single point of tasking** — only the Orchestrator issues work orders; only the
   Principal amends the mission. No lateral tasking between members.
3. **Propose ≠ adopt** — any member may propose anything; nobody may silently adopt
   anything. Adoption is an explicit, logged orchestrator decision.
4. **Total legibility** — all inter-agent traffic is plain text on logged message lanes,
   human-readable, with a standard header
   (`[swarm:voynich] <from> → <to> | task <id> | <provenance>`). The Principal is the
   silent observer of every lane.
5. **Kill switch and reconstructibility** — the Principal halts the swarm with one message;
   the Orchestrator must be able to answer "why was this being done?" for any running task
   at any time.

Two further structural choices back this up: **chat coordinates, files are the record**
(work products land in the repository, so the durable record can't diverge from what was
discussed), and **no standing autonomous loops** — the swarm runs when convened for a phase
and sleeps otherwise, so there is no idle background process to drift.

### 2.3 Why this shape

A single agent doing generation *and* review reconverges on its own priors — the same
failure that filled the decipherment graveyard, at machine speed. Splitting generation from
adversarial review across genuinely different models/temperaments, and making the review a
*gate* rather than a suggestion, buys real diversity. Bounding it all with human-legible
provenance and a human gatekeeper keeps the speed without inheriting the drift. The
calibration gauntlet (§1.5) is the swarm testing its own immune system before it is allowed
to bless anything.
