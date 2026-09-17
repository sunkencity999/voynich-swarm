#!/usr/bin/env python3
"""Phase 9: replication + decoupling attacks on the or- x root_prominence link.

HOST CONTEXT: run under RAM restriction (memtester holds 32GB; keep <8GB) after
repeated host crashes. Second-annotator VL extraction (WP1) is DEFERRED except
for the 20-folio partial checkpoint banked before the crash (used for a partial
agreement estimate only, exploratory). Every brick checkpoints to its own JSON.

PREREGISTERED TEST LIST — fixed 2026-09-17 BEFORE computing any or- rates from
IT/GC or any cross-section or- rates. The only data inspected beforehand:
(a) covariate-only design matrix (scribe $H x Currier $L x section $I from
ZL3b-n.txt headers, printed 2026-09-17 09:25 PDT), which showed Scribe 3 is
the unique scribe writing both dialects (S section: 2 Currier-A folios,
22 Currier-B); (b) all Phase 7/8 results (prior selections, disclosed).

Token/or- definitions (identical parser for all three transliterations):
  tokens = IVTFF locus lines, [x:y]->x, <...>/{...} stripped, @nnn;->'*',
  '!' and '%' removed, split on [.,] and whitespace, tokens containing '?'
  or '*' dropped. ZL/IT lowercased (EVA); GC kept case-sensitive (v101).
  or-token: EVA (ZL, IT) = token startswith 'or'; v101 (GC) = startswith 'oy',
  with the EVA-or <-> v101-oy mapping VERIFIED empirically by locus alignment
  (equal-token-count loci; report match fraction) before use.
  or_share(folio) = or-tokens / tokens on that folio (all loci on the page).

Confirmatory family (BH-FDR q=0.05 across these 7; perms=20,000; seed fixed):
  R1  or-(IT)  ~ root_prominence(A1), herbal, perm within scribe x quire strata
  R2  or-(IT)  ~ root_prominence(A1), Scribe 1 only, perm within quire
  R3  oy-(GC)  ~ root_prominence(A1), herbal, perm within scribe x quire strata
  R4  oy-(GC)  ~ root_prominence(A1), Scribe 1 only, perm within quire
  D1  or-(ZL) A vs B within SCRIBE 3, perm within section strata (only S mixed:
      2 A vs 22 B; same hand, same section, dialect varies). Pre-stated
      direction: dialect-driven => A folios lower or- share.
  D2  or-(ZL) ~ scribe {2,3,5} within Currier B, perm within section strata
      (H and S contribute). Scribe-driven => differs; dialect-driven => null.
  S1  medial-only or-(ZL, phase5 line corpus) ~ root_prominence(A1), Scribe 1
      only, perm within quire. Medial = tokens excluding line-first and
      line-last of every line. Line-position artifact => association vanishes.

Recorded as structurally untestable (not counted in FDR):
  D3  or- ~ scribe within Currier A, section-stratified: scribe 1's A folios
      (H/P/T) and scribe 3's A folios (S) share no section -> no mixed strata.
      Unstratified version run as EXPLORATORY only (section-confounded).

Baselines/descriptive (no FDR): B0 = or-(ZL, same simple parser) mirrors of
R1/R2, to make IT/GC comparisons apples-to-apples with phase 8's C7/C8.

Exploratory (separate BH-FDR where applicable):
  X1  partial inter-annotator agreement on the 20 banked a2 folios:
      Spearman rho underground_parts_emphasis(A2, 0-3) x root_prominence(A1,
      absent/minor=0, moderate=1, dominant=2); plus exact-tier agreement.
  X2  or- token line-position distribution (first/medial/last) by
      root_prominence tier, descriptive.
  X3  D3 unstratified (section-confounded, stated as such).
"""
import json, os, re, sys
from collections import Counter, defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
def J(p): return os.path.join(HERE, p)
sys.path.insert(0, HERE)
from run_phase7 import kw_stat, bh_fdr
from run_phase8 import load_headers, strat_perm, perm_test_kw

SEED = 20260917
NPERM = 20000

# ---------------- shared parser ----------------

def parse_ivtff_folio_tokens(path, lowercase):
    """folio -> list of tokens, whole page, uniform cleaning."""
    ftok = defaultdict(list)
    for line in open(J(path), encoding="latin-1"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^<(f\d+[rv]\d?)\.[^>]*>\s*(.*)$', line)
        if not m:
            continue
        folio, text = m.group(1), m.group(2)
        text = re.sub(r'\[([^\]:]*):[^\]]*\]', r'\1', text)
        text = re.sub(r'<[^>]*>', ' ', text)
        text = re.sub(r'\{[^}]*\}', ' ', text)
        text = re.sub(r'@\d+;', '*', text)
        text = text.replace('!', '').replace('%', '')
        if lowercase:
            text = text.lower()
        for tok in re.split(r'[.,\s]+', text):
            if tok and '?' not in tok and '*' not in tok:
                ftok[folio].append(tok)
    return dict(ftok)

def parse_ivtff_locus_tokens(path, lowercase):
    """locus-id -> token list (for alignment verification)."""
    lt = {}
    for line in open(J(path), encoding="latin-1"):
        line = line.strip()
        m = re.match(r'^<(f\d+[rv]\d?\.\d+)[^>]*>\s*(.*)$', line)
        if not m:
            continue
        locus, text = m.group(1), m.group(2)
        text = re.sub(r'\[([^\]:]*):[^\]]*\]', r'\1', text)
        text = re.sub(r'<[^>]*>', ' ', text)
        text = re.sub(r'\{[^}]*\}', ' ', text)
        text = re.sub(r'@\d+;', '*', text)
        text = text.replace('!', '').replace('%', '')
        if lowercase:
            text = text.lower()
        toks = [t for t in re.split(r'[.,\s]+', text) if t]
        if toks:
            lt[locus] = toks
    return lt

def or_share_map(ftok, prefix):
    out = {}
    for f, toks in ftok.items():
        if toks:
            out[f] = sum(1 for t in toks if t.startswith(prefix)) / len(toks)
    return out

def ckpt(name, obj):
    tmp = J(name + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, J(name))
    print(f"[ckpt] {name}")

# ---------------- main ----------------

def main():
    rng = np.random.default_rng(SEED)
    hdr = load_headers()
    feats = json.load(open(J("phase7_features.json")))["features"]

    # ---- parse all three transliterations with the SAME parser ----
    zl = parse_ivtff_folio_tokens("ZL3b-n.txt", lowercase=True)
    it = parse_ivtff_folio_tokens("IT2a-n.txt", lowercase=True)
    gc = parse_ivtff_folio_tokens("GC2a-n.txt", lowercase=False)
    print(f"folios with tokens: ZL={len(zl)} IT={len(it)} GC={len(gc)}")

    # ---- verify EVA 'or' <-> v101 'oy' mapping by locus alignment ----
    zl_loc = parse_ivtff_locus_tokens("ZL3b-n.txt", True)
    gc_loc = parse_ivtff_locus_tokens("GC2a-n.txt", False)
    n_pairs = n_or = n_or_oy = 0
    oy_counter = Counter()
    for loc in set(zl_loc) & set(gc_loc):
        a, b = zl_loc[loc], gc_loc[loc]
        if len(a) != len(b):
            continue
        for ta, tb in zip(a, b):
            n_pairs += 1
            if ta.startswith("or"):
                n_or += 1
                oy_counter[tb[:2]] += 1
                if tb.startswith("oy"):
                    n_or_oy += 1
    mapping = {
        "aligned_token_pairs": n_pairs,
        "zl_or_tokens_aligned": n_or,
        "gc_counterpart_startswith_oy": n_or_oy,
        "match_fraction": round(n_or_oy / max(n_or, 1), 4),
        "gc_prefix_distribution_of_zl_or": dict(oy_counter.most_common(8)),
    }
    print("or<->oy mapping:", mapping)

    or_zl = or_share_map(zl, "or")
    or_it = or_share_map(it, "or")
    or_gc = or_share_map(gc, "oy")

    # ---- herbal frame (129 folios from phase 7) ----
    herb = sorted(set(feats) & set(zl) & set(hdr))
    scribe = {f: hdr[f].get("H", "?") for f in hdr}
    quire = {f: hdr[f].get("Q", "?") for f in hdr}
    lang = {f: hdr[f].get("L", "?") for f in hdr}
    sect = {f: hdr[f].get("I", "?") for f in hdr}
    cnt_rp = Counter(feats[f].get("root_prominence", "missing") for f in herb)
    rp = {f: (feats[f].get("root_prominence", "missing")
              if cnt_rp[feats[f].get("root_prominence", "missing")] >= 4 else "_rare")
          for f in herb}

    results = {"seed": SEED, "n_perm": NPERM,
               "parser_note": "uniform simple parser, whole-page tokens; see docstring",
               "v101_mapping_check": mapping}

    # ================= WP2: transliteration replication =================
    wp2 = {"coverage": {}}
    fam = {"B0_ZL": (or_zl, "or"), "R12_IT": (or_it, "or"), "R34_GC": (or_gc, "oy")}
    tests = {}
    for tag, (shares, pref) in fam.items():
        folios = [f for f in herb if f in shares]
        wp2["coverage"][tag] = {"herbal_folios_covered": len(folios), "of": len(herb)}
        x = [rp[f] for f in folios]
        yv = np.array([shares[f] for f in folios])
        sq = [f"{scribe[f]}|{quire[f]}" for f in folios]
        h, p = perm_test_kw(x, yv, sq, rng, NPERM)
        tests[tag + "_all_sxq"] = {"H": round(h, 3), "p": p, "n": len(folios),
                                   "n_strata": len(set(sq))}
        s1 = [f for f in folios if scribe[f] == "1"]
        x1 = [rp[f] for f in s1]
        yv1 = np.array([shares[f] for f in s1])
        q1 = [quire[f] for f in s1]
        h1, p1 = perm_test_kw(x1, yv1, q1, rng, NPERM)
        tests[tag + "_scribe1_q"] = {"H": round(h1, 3), "p": p1, "n": len(s1)}
        means = {}
        for cat in ("minor", "moderate", "dominant"):
            v = [shares[f] for f in folios if rp[f] == cat]
            if v:
                means[cat] = {"n": len(v), "mean_or_share": round(float(np.mean(v)), 5)}
        tests[tag + "_means"] = means
        print(tag, tests[tag + "_all_sxq"], tests[tag + "_scribe1_q"], means)
    wp2["tests"] = tests
    ckpt("phase9_checkpoint_wp2.json", wp2)
    results["WP2"] = wp2

    # ================= WP3: cross-section decoupling =================
    wp3 = {}
    allf = [f for f in hdr if f in or_zl]
    wp3["design_matrix"] = {f"{sect[f]}|{lang[f]}|{scribe[f]}": c for
        (f, c) in []}  # replaced below
    dm = Counter(f"{sect[f]}|{lang[f]}|{scribe[f]}" for f in allf)
    wp3["design_matrix"] = dict(sorted(dm.items()))

    # D1: within scribe 3, A vs B, section-stratified
    s3 = [f for f in allf if scribe[f] == "3" and lang[f] in ("A", "B")]
    x = [lang[f] for f in s3]
    yv = np.array([or_zl[f] for f in s3])
    st = [sect[f] for f in s3]
    h, p = perm_test_kw(x, yv, st, rng, NPERM)
    ga = [or_zl[f] for f in s3 if lang[f] == "A"]
    gb = [or_zl[f] for f in s3 if lang[f] == "B"]
    wp3["D1_scribe3_AvsB_sectstrat"] = {
        "H": round(h, 3), "p": p, "n": len(s3),
        "folios_A": sorted(f for f in s3 if lang[f] == "A"),
        "mean_or_A": round(float(np.mean(ga)), 5), "n_A": len(ga),
        "mean_or_B": round(float(np.mean(gb)), 5), "n_B": len(gb),
        "direction_dialect_driven": "A lower",
        "observed_direction": "A lower" if np.mean(ga) < np.mean(gb) else "A higher"}
    print("D1", wp3["D1_scribe3_AvsB_sectstrat"])

    # D2: within Currier B, scribe 2/3/5, section-stratified
    bf = [f for f in allf if lang[f] == "B" and scribe[f] in ("2", "3", "5")]
    x = [scribe[f] for f in bf]
    yv = np.array([or_zl[f] for f in bf])
    st = [sect[f] for f in bf]
    h, p = perm_test_kw(x, yv, st, rng, NPERM)
    mm = {s: {"n": sum(1 for f in bf if scribe[f] == s),
              "mean_or": round(float(np.mean([or_zl[f] for f in bf if scribe[f] == s])), 5)}
          for s in ("2", "3", "5")}
    wp3["D2_withinB_scribe_sectstrat"] = {"H": round(h, 3), "p": p, "n": len(bf),
                                          "per_scribe": mm,
                                          "sections": dict(Counter(st))}
    print("D2", wp3["D2_withinB_scribe_sectstrat"])

    # D3: untestable stratified; exploratory unstratified
    af = [f for f in allf if lang[f] == "A" and scribe[f] in ("1", "3")]
    x = [scribe[f] for f in af]
    yv = np.array([or_zl[f] for f in af])
    h, p = perm_test_kw(x, yv, ["all"] * len(af), rng, NPERM)
    wp3["D3_withinA_scribe"] = {
        "status": "structurally untestable stratified (no shared section between scribe-1 A and scribe-3 A)",
        "exploratory_unstratified": {"H": round(h, 3) if h else h, "p": p, "n": len(af),
            "mean_or_scribe1": round(float(np.mean([or_zl[f] for f in af if scribe[f] == '1'])), 5),
            "mean_or_scribe3": round(float(np.mean([or_zl[f] for f in af if scribe[f] == '3'])), 5),
            "caveat": "section-confounded; exploratory only"}}
    print("D3", wp3["D3_withinA_scribe"])

    # descriptive: or- share by section x dialect x scribe
    grp = defaultdict(list)
    for f in allf:
        grp[f"{sect[f]}|{lang[f]}|{scribe[f]}"].append(or_zl[f])
    wp3["or_share_by_cell"] = {k: {"n": len(v), "mean_or": round(float(np.mean(v)), 5)}
                               for k, v in sorted(grp.items()) if len(v) >= 2}
    ckpt("phase9_checkpoint_wp3.json", wp3)
    results["WP3"] = wp3

    # ================= S1: slot-aware re-test =================
    vlines = json.load(open(J("phase5_vlines.json")))
    meta = json.load(open(J("phase5_line_meta.json")))
    med = defaultdict(lambda: [0, 0])   # folio -> [medial or-, medial total]
    posdist = defaultdict(lambda: Counter())  # rp tier -> position counter
    for words, m in zip(vlines, meta):
        if m["sec"] != "herbal":
            continue
        f = m["folio"]
        for i, w in enumerate(words):
            pos = "first" if i == 0 else ("last" if i == len(words) - 1 else "medial")
            if w.startswith("or") and f in rp:
                posdist[rp[f]][pos] += 1
            if pos == "medial":
                med[f][1] += 1
                if w.startswith("or"):
                    med[f][0] += 1
    med_share = {f: c / t for f, (c, t) in med.items() if t >= 10}
    s1f = [f for f in herb if scribe[f] == "1" and f in med_share]
    x = [rp[f] for f in s1f]
    yv = np.array([med_share[f] for f in s1f])
    q1 = [quire[f] for f in s1f]
    h, p = perm_test_kw(x, yv, q1, rng, NPERM)
    slot = {"S1_medial_or_scribe1_q": {"H": round(h, 3), "p": p, "n": len(s1f),
            "note": "medial = excludes line-first and line-last tokens; folios with >=10 medial tokens"},
            "medial_means": {c: {"n": len([f for f in s1f if rp[f] == c]),
                                 "mean": round(float(np.mean([med_share[f] for f in s1f if rp[f] == c])), 5)}
                             for c in ("minor", "moderate", "dominant") if any(rp[f] == c for f in s1f)},
            "X2_or_position_by_rp": {k: dict(v) for k, v in posdist.items()}}
    print("S1", slot["S1_medial_or_scribe1_q"], slot["medial_means"])
    ckpt("phase9_checkpoint_slots.json", slot)
    results["SLOT"] = slot

    # ================= X1: partial inter-annotator agreement =================
    a2 = json.load(open(J("phase9_features.json")))["a2"]
    rmap = {"absent": 0, "minor": 0, "moderate": 1, "dominant": 2}
    pairs = []
    for f, d in a2.items():
        if f in feats and isinstance(d.get("underground_parts_emphasis"), int):
            r1 = feats[f].get("root_prominence")
            if r1 in rmap:
                pairs.append((rmap[r1], d["underground_parts_emphasis"], f))
    if len(pairs) >= 8:
        a = np.array([p[0] for p in pairs], float)
        b = np.array([p[1] for p in pairs], float)
        def rank(v):
            order = np.argsort(v, kind="mergesort")
            r = np.empty(len(v)); r[order] = np.arange(1, len(v) + 1)
            sv = v[order]; i = 0
            while i < len(v):
                j = i
                while j + 1 < len(v) and sv[j + 1] == sv[i]: j += 1
                r[order[i:j + 1]] = r[order[i:j + 1]].mean(); i = j + 1
            return r
        ra, rbv = rank(a), rank(b)
        rho = float(np.corrcoef(ra, rbv)[0, 1])
        ge = 0
        for _ in range(NPERM):
            rng.shuffle(rbv)
            if abs(np.corrcoef(ra, rbv)[0, 1]) >= abs(rho) - 1e-12:
                ge += 1
        agree = {"n": len(pairs), "spearman_rho": round(rho, 3),
                 "perm_p_two_sided": (ge + 1) / (NPERM + 1),
                 "note": "PARTIAL: 20 pre-crash folios only; WP1 completion deferred (host RAM under test)",
                 "pairs": [(f, int(x1), int(x2)) for x1, x2, f in
                           [(p[0], p[1], p[2]) for p in pairs]]}
    else:
        agree = {"status": "insufficient pairs", "n": len(pairs)}
    print("X1 agreement:", {k: agree[k] for k in agree if k != "pairs"})
    ckpt("phase9_checkpoint_agree.json", agree)
    results["X1_agreement_partial"] = agree

    # ================= confirmatory FDR =================
    conf = {
        "R1_IT_all_sxq": tests["R12_IT_all_sxq"]["p"],
        "R2_IT_scribe1_q": tests["R12_IT_scribe1_q"]["p"],
        "R3_GC_all_sxq": tests["R34_GC_all_sxq"]["p"],
        "R4_GC_scribe1_q": tests["R34_GC_scribe1_q"]["p"],
        "D1_scribe3_AvsB": wp3["D1_scribe3_AvsB_sectstrat"]["p"],
        "D2_withinB_scribe": wp3["D2_withinB_scribe_sectstrat"]["p"],
        "S1_medial_scribe1": slot["S1_medial_or_scribe1_q"]["p"],
    }
    keys = list(conf)
    pv = np.array([conf[k] for k in keys])
    surv = bh_fdr(pv, q=0.05)
    results["confirmatory_family"] = {k: {"p": conf[k], "fdr_survives": bool(s)}
                                      for k, s in zip(keys, surv)}
    print("FDR:", results["confirmatory_family"])

    ckpt("phase9_results.json", results)

if __name__ == "__main__":
    main()
