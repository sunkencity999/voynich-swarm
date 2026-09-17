#!/usr/bin/env python3
"""Phase 9 WP1/WP3: second-annotator feature extraction.

Annotator 2 = same local VL weights (only local VL stack available; ollama has
no vision model) but a SUBSTANTIALLY DIFFERENT instrument: different framing
(image cataloguer, not "herbal manuscript plant description"), different
response schema (0-3 numeric emphasis scales instead of categorical labels),
different key names and order. Blinded: the prompt contains no reference to
text features, dialects, scribes, sections, or any hypothesis.

Modes:
  --a2 <folios...|--all>     annotator-2 pass (any folio in folios/)
  --p7 <folios...>           phase-7 prompt pass on new folios (pharma), stored
                             separately so the ORIGINAL annotator's instrument
                             also covers pharma for within-annotator tests.

Checkpoint: phase9_features.json  {"a2": {}, "raw_a2": {}, "p7x": {}, "raw_p7x": {}}
"""
import base64, json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FOLIOS = os.path.join(HERE, "folios")
CKPT = os.path.join(HERE, "phase9_features.json")
ENDPOINT = "http://localhost:8000/v1/chat/completions"

PROMPT_A2 = (
    "You are indexing scanned pages from an old book for an image catalogue. "
    "This page contains a hand-drawn illustration and some handwriting. "
    "Consider ONLY the illustration; ignore all writing. "
    "Return strict JSON with exactly these keys:\n"
    '{"drawing_subject": "plant|plants_in_containers|human_figures|circular_diagram|animal|other",\n'
    ' "underground_parts_emphasis": 0, 1, 2 or 3,\n'
    ' "foliage_emphasis": 0, 1, 2 or 3,\n'
    ' "bloom_emphasis": 0, 1, 2 or 3,\n'
    ' "num_distinct_plants": <integer, 0 if none>,\n'
    ' "num_human_figures": <integer, 0 if none>,\n'
    ' "water_or_pools_emphasis": 0, 1, 2 or 3,\n'
    ' "containers_or_vessels": "yes|no"}\n'
    "Emphasis scale: 0 = that element is not drawn at all; 1 = present but "
    "small or peripheral; 2 = clearly drawn and roughly balanced with the rest "
    "of the illustration; 3 = the largest or most visually striking part of "
    "the illustration. Underground parts means roots, tubers, bulbs or "
    "anything drawn below the soil line. Output ONLY the JSON object."
)

# phase-7 original prompt, verbatim (for pharma coverage by annotator 1's instrument)
PROMPT_P7 = (
    "This is a page from a medieval herbal manuscript showing a plant drawing "
    "with handwritten text. Ignore the text entirely. Describe ONLY the plant "
    "drawing, as strict JSON with exactly these keys and allowed values:\n"
    '{"leaf_shape": "broad|narrow|lobed|compound|spiky|round|other|none",\n'
    ' "leaf_arrangement": "basal|alternate|opposite|whorled|unclear",\n'
    ' "root_type": "bulbous|branching|single-taproot|rhizome|tuberous|absent|other",\n'
    ' "root_prominence": "dominant|moderate|minor|absent",\n'
    ' "flower_present": "yes|no",\n'
    ' "flower_color": "red|blue|yellow|white|purple|green|brown|none|other",\n'
    ' "flower_shape": "star|bell|cluster|spike|round|other|none",\n'
    ' "stem_count": "single|multiple",\n'
    ' "plant_count": "one|several",\n'
    ' "other_notable": "<one short phrase>"}\n'
    "Choose exactly one allowed value per key. Output ONLY the JSON object, no prose."
)

A2_KEYS = ["drawing_subject","underground_parts_emphasis","foliage_emphasis",
           "bloom_emphasis","num_distinct_plants","num_human_figures",
           "water_or_pools_emphasis","containers_or_vessels"]
P7_KEYS = ["leaf_shape","leaf_arrangement","root_type","root_prominence",
           "flower_present","flower_color","flower_shape","stem_count",
           "plant_count","other_notable"]

def load_ckpt():
    if os.path.exists(CKPT):
        with open(CKPT) as f: return json.load(f)
    return {"a2": {}, "raw_a2": {}, "p7x": {}, "raw_p7x": {}}

def save_ckpt(d):
    tmp = CKPT + ".tmp"
    with open(tmp, "w") as f: json.dump(d, f, indent=1)
    os.replace(tmp, CKPT)

def parse_json_block(text, keys, intkeys=()):
    m = re.search(r'\{.*\}', text, re.S)
    if not m: return None
    block = m.group(0)
    d = None
    for attempt in (block, block.replace("'", '"')):
        try:
            d = json.loads(attempt); break
        except Exception:
            d = None
    if d is None: return None
    out = {}
    for k in keys:
        v = d.get(k)
        if k in intkeys:
            try: out[k] = int(v)
            except Exception: out[k] = "missing"
        else:
            out[k] = str(v).strip().lower() if v is not None else "missing"
    return out

def ask(folio, prompt):
    img = os.path.join(FOLIOS, folio + ".jpg")
    with open(img, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    payload = {
        "model": "vl-adhoc",
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
            {"type": "text", "text": prompt},
        ]}],
        "max_tokens": 2500,
        "temperature": 0.1,
    }
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=420) as r:
        d = json.loads(r.read())
    return (d["choices"][0]["message"].get("content") or "").strip()

INTKEYS = ("underground_parts_emphasis","foliage_emphasis","bloom_emphasis",
           "num_distinct_plants","num_human_figures","water_or_pools_emphasis")

def main():
    args = sys.argv[1:]
    mode = args.pop(0) if args and args[0] in ("--a2", "--p7") else "--a2"
    ck = load_ckpt()
    if mode == "--a2":
        feat_key, raw_key, prompt, keys, ik = "a2", "raw_a2", PROMPT_A2, A2_KEYS, INTKEYS
    else:
        feat_key, raw_key, prompt, keys, ik = "p7x", "raw_p7x", PROMPT_P7, P7_KEYS, ()
    if args == ["--all"]:
        targets = sorted(f[:-4] for f in os.listdir(FOLIOS) if f.endswith(".jpg"))
    else:
        targets = args
    done = 0
    for folio in targets:
        if folio in ck[feat_key]:
            continue
        t0 = time.time()
        try:
            out = ask(folio, prompt)
        except Exception as e:
            print(f"[{folio}] REQUEST-FAIL {e}", flush=True); save_ckpt(ck); time.sleep(3); continue
        dt = time.time() - t0
        ck[raw_key][folio] = out[-4000:]
        parsed = parse_json_block(out, keys, ik)
        if parsed:
            ck[feat_key][folio] = parsed
            brief = (f"subj:{parsed.get('drawing_subject')}/ug:{parsed.get('underground_parts_emphasis')}"
                     if mode == "--a2" else
                     f"{parsed.get('root_prominence')}/fl:{parsed.get('flower_present')}")
            print(f"[{folio}] ok {dt:.1f}s {brief}", flush=True)
        else:
            print(f"[{folio}] PARSE-FAIL {dt:.1f}s out[:200]={out[:200]!r}", flush=True)
        done += 1
        if done % 10 == 0 or parsed is None:
            save_ckpt(ck)
    save_ckpt(ck)
    print(f"total parsed ({feat_key}): {len(ck[feat_key])}")

if __name__ == "__main__":
    main()
