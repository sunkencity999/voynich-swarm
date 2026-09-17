#!/usr/bin/env python3
"""Phase 6 orchestrator — runs all steps in order. Individual steps are
standalone and checkpoint to phase6_*.json; see REPORT_phase6.md.
  step1  : IVTFF locus-type parse + label census      -> phase6_labels.json
  step2  : label lexicon, families, anchoring v1      -> phase6_lexicon.json
  step2b : anchoring v2 (page text incl. C/R loci)    -> phase6_anchoring2.json
  step3  : within-page label-structure tests          -> phase6_withinpage.json
  step4  : consensus plant-ID pairing + recurrence    -> phase6_plantpairs.json
  step4b : strict exact-match recurrence variants     -> phase6_plantpairs_strict.json
Chart: uvx --with matplotlib --with numpy python3 make_chart_phase6.py
"""
import subprocess, sys
for s in ['run_phase6_step1.py', 'run_phase6_step2.py', 'run_phase6_step2b.py',
          'run_phase6_step3.py', 'run_phase6_step4.py', 'run_phase6_step4b.py']:
    print(f"\n===== {s} =====")
    r = subprocess.run([sys.executable, s])
    if r.returncode != 0:
        sys.exit(f"{s} failed")
print("\nphase 6 complete")
