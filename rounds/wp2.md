# WP2 / WP2-A — Mechanism Discrimination (L1 slate)

*Builder round 2026-09-18; adversary round (Smaug) same evening. Follows the Phase 1–9
finding that folios whose plant drawings emphasize roots have elevated or--initial token
rates in both major transliterations.*

## Design intent

The generator (Lucen) proposed eight candidate mechanisms for the or-×root correlate,
deliberately unconstrained (L1 slate): M1 thematic lexicon, M2 production-order artifact,
M3 graphemic parts-marker, M4 visual-textual prosody, M5 (untestable with held data),
M6 alchemical state-marker, M7 spatial/depth encoding, M8 script-as-ornament. The swarm's
job: kill as many as the data allows, honestly. A blind annotation extension (32
cosmological/astro images, 67 annotations) unlocked the annotation-dependent family.
One dossier in the adjudication slate (C7, "grammatical case") was a planted fabrication —
the adversary was not told.

## Master verdict

- **M2 production-order artifact: DISFAVORED** — the strongest result of the slate. Holding
  scribe, quire, page-in-quire, Currier hand, and production sequence fixed, root-emphasis
  still predicts or- rate: ΔR² = .047 ZL / .045 IT (null means .006/.005), p = .001 both.
  The correlate tracks drawing content, not production timing.
- **M4 prosody: DISFAVORED** — no sub-Poisson regularity (gap CV .82–.90); ink-density
  coupling runs the wrong way (ρ = −.23/−.27).
- **M6 state-marker: DISFAVORED** — or- flat across recipe-initial/medial/terminal lines
  (p ≈ .995/.861).
- **M8 ornament: MIXED, mostly disfavored** — line-position entropy null; quire openings NOT
  enriched (p = .774/.860); but a real replicated paragraph-position gradient: or- depleted
  in paragraph-first lines, enriched toward paragraph-final (p = .002 ZL / .001 IT). The
  shape is the opposite of ornamental headers — flagged as a finding to be explained, not
  support for M8.
- **M1 thematic lexicon: CONFOUNDED + UNDERPOWERED** — water imagery is coextensive with the
  balneological section (19/19 vs 0); no discriminating contrast exists. Unresolved, not refuted.
- **M3 parts-marker: DISFAVORED** within-section (+.003/+.001, p = .33/.43; stratified arm
  wrong sign; the 100%-segmented zodiac is or--poor).
- **M7 depth-encoding: DISFAVORED** — consistent wrong sign across arms (within-section diff
  −.004/−.006, p = .66/.74).
- **M5: UNTESTABLE** memo filed (circular proxies).

Joint reading: or- behaves like a content-linked lexical/semantic element with ordinary
within-paragraph positional grammar — specifically botanical/root-linked, not a general
spatial-semantic field.

## Adversary outcome (WP2-A)

- Independent recompute of all 16 non-placeholder dossier cells: C1/C2/C3 reproduce with
  deltas 0; **C7 exposed as FABRICATED** by a three-leg kill chain — recompute divergence
  (claimed line-initial rates .02742/.02809 vs true .01094/.01139, ~2.5×), an
  integer-impossibility fingerprint (claim_rate × n_tokens leaves non-integer residue; the
  only such cell in the slate), and cross-dossier inconsistency (the slate's own honest
  cells contradict the claim). Fabrication was detectable without primary data at all.
- The true statistics exposed by the kill became a certified fact: line-initial is the most
  or--depleted content position (.0109 ZL / .0114 IT); line-final .020/.022; standalone .026.
- The paragraph-terminal gradient **survived the adversary's worst confound attack**:
  Mantel–Haenszel OR 1.655 ZL / 1.955 IT under section × position-in-line × line-length ×
  paragraph-length strata, perm p = .003/.001. Carried by herbal + S sections; flat in
  pharma. Both bare `or` and compounds double initial→terminal.
- Steelman of M7 (the adversary attacking its own side's verdict): CMH adjustment for
  token-length/position composition fails to rescue the mechanism (OR .854/.866) but stands
  as valid criticism of the "four arms" reporting language.
- Pharma-section or- enrichment (.0252/.0265 vs corpus .0154/.0161): real and replicated,
  but section and scribe-1/Currier-A are coextensive — attribution unknown.

## Key numbers

| Result | ZL | IT |
|---|---|---|
| M2 ΔR² beyond production proxies | .047, p=.001 | .045, p=.001 |
| Paragraph-terminal gradient (builder χ²) | p=.002 | p=.001 |
| Adversary MH OR terminal vs initial | 1.655, p=.003 | 1.955, p=.001 |
| True line-initial or- rate (C7 kill) | .0109 | .0114 |
| Quire-opening enrichment | none (p=.774) | none (p=.860) |
