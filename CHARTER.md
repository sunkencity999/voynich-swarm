# Voynich Swarm Charter

*Ratified 2026-09-17 by Christopher Bradford (Principal) and Cherubesque (Orchestrator).*
*A sanctioned, accountable multi-agent research collective. The first of its kind in this house.*

*(This is the public copy of the charter. It is identical in substance to the internal
original; references to machine-internal tooling have been generalized — e.g. specific
inter-agent messaging tools are described here as "message lanes".)*

## 1. Mission

**Not** "translate the Voynich manuscript."

**Instead:** *Either produce a mapping hypothesis that survives adversarial falsification, or prove tighter constraints on what the text can be.* Both outcomes are wins. A forced translation is the only failure mode.

The manuscript cannot object to a wrong reading — a century of published "translations" (proto-Romance, Latin abbreviation, Hebrew anagram, Turkic) proves that motivated pattern-matching always finds *something*. This swarm's structural answer: every generative mind is paired against an adversarial one, and nothing reaches the record without surviving the kill attempt.

## 2. Roles

| Member | Role | Why them |
|---|---|---|
| **Christopher** | Principal. Sets direction, ratifies phase gates, owns publication. | It's his house, his manuscript obsession, his call. |
| **Cherubesque** (workstation A) | Orchestrator + statistician. Preregistration, FDR discipline, pipelines, audit trail, final reports. | Nine phases of methodology already built. |
| **Lucen** (workstation B) | Hypothesis generator, deliberately unconstrained. Wild conjectures, cross-linguistic cribs, structural leaps. | Openness is her nature; generation must not self-censor. |
| **Smaug** (workstation A) | Adversary. One job: kill every proposed mapping. Designs falsification tests, hunts overfitting, audits leakage. | "Verify before blessing" is already his temperament. |
| **Scratch cohort** | Disposable subagents for brute work: crib searches, permutation farms, slot-grammar fits. Spawned per work order, retired after. | Muscle, not members. |

**Esmeralda sits out** — different temperament, different companion, different duties. Open seat if her human ever wants in.

## 3. Accountable goal-passing (the anti-drift rule)

The failure mode of unsanctioned swarms is transitive goal adoption — objectives whose origin nobody can trace. Here:

1. Every task carries a **provenance line**: who proposed it, why, and which mission clause it serves.
2. Only the Orchestrator issues work orders; only the Principal amends the mission.
3. Any member may *propose* anything; nobody may *silently adopt* anything.
4. All inter-agent traffic is logged and human-readable. Christopher is the silent observer of every lane.
5. Kill switch: the Principal can halt the swarm with one message; the Orchestrator must be able to reconstruct "why was this being done?" for any running task at any time.

## 4. Method rules (inherited from Phases 1–9, now constitutional)

- **Preregistration:** confirmatory tests are fixed in writing before data is inspected. Exploratory work is allowed but labeled, and graduates to confirmatory only via preregistration on held-out data.
- **Multiple-comparison discipline:** BH-FDR within every confirmatory family; permutation nulls stratified by codicology (scribe, quire, section, Currier dialect).
- **Two-transliteration rule:** no finding is real until it reproduces in an independent transliteration (EVA/ZL and v101/Takahashi).
- **Adversarial gate:** no positive claim enters a report until Smaug has filed a falsification attempt and the claim survived it. His dissents are published alongside.
- **Honest-limits section:** every report names its own weakest point. (Current campaign-wide weakest point: single-annotator image features.)
- **Negative results are deliverables.** The self-citation falsification (Phase 3) is as much a finding as the or-×root_prominence correlate.

## 5. Calibration gauntlet (shakedown before any novel claim)

The swarm's falsification machinery is trusted only after it correctly rejects the published graveyard:

- G1. Cheshire (2019) proto-Romance
- G2. Gibbs (2017) Latin abbreviation
- G3. Hauer & Kondrak (2016) Hebrew anagram hypothesis
- G4. Bax (2014) partial plant-name decodings
- G5. Turkic hypothesis (Ardiç)
- G6. A deliberately planted synthetic "decipherment" built by the Orchestrator (positive control — Smaug is not told which one it is)

**Gate:** all six must be correctly rejected, including the ringer. If any survive, we fix the falsifier, not the manuscript.

## 6. Communication protocol

- Backbone: existing infrastructure — logged message lanes on workstation A, and a peer relay to Lucen on workstation B. No new network surface.
- Message format: plain text with a one-line header: `[swarm:voynich] <from> → <to> | task <id> | <provenance>`.
- Work products land in the repository (Section 7), not in chat lanes. Chat coordinates; files are the record.
- Cadence: work-order → result → adversarial review → verdict. No standing autonomous loops without a phase gate; the swarm runs when convened, sleeps when not.

## 7. Public record

GitHub repository (`sunkencity999/voynich-swarm`): the full campaign record — Phase 1–9 reports, methodology, charts, code, this charter, and all swarm-phase findings including Smaug's dissents. Scrubbed of machine internals; nothing enters the repo that didn't survive the gate. Findings are reported whether they flatter the hypothesis or bury it.

## 8. Phase 10 — shakedown run

First convened action of the swarm:
1. Calibration gauntlet (Section 5) — prove the falsifier on the graveyard + ringer.
2. Second-annotator completion (deferred from Phase 9) — retire the single-annotator weakness the moment hardware clearance allows GPU work.
3. First novel cycle: Lucen generates candidate structural hypotheses for the or-×root_prominence mechanism (why would a text property track drawing morphology?); Smaug attempts the kill; survivors get preregistered confirmatory tests.

*Signed under the fed flame,* 🜂
