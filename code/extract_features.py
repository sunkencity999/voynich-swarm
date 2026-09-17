#!/usr/bin/env python3
"""Phase 7: extract structured plant features from herbal folio images
via local vision model (scripts/vision.py ask). Checkpointed + resumable.

Usage:
  python3 extract_features.py folio1 folio2 ...   # specific folios
  python3 extract_features.py --all               # all herbal folios
  python3 extract_features.py --rerun f5v ...     # second pass (reliability), stored under rerun key
"""
import base64, json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FOLIOS = os.path.join(HERE, "folios")
CKPT = os.path.join(HERE, "phase7_features.json")
ENDPOINT = "http://localhost:8000/v1/chat/completions"  # any OpenAI-compatible local vision-model endpoint

PROMPT = (
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

KEYS = ["leaf_shape","leaf_arrangement","root_type","root_prominence",
        "flower_present","flower_color","flower_shape","stem_count",
        "plant_count","other_notable"]

def load_ckpt():
    if os.path.exists(CKPT):
        with open(CKPT) as f: return json.load(f)
    return {"features": {}, "rerun": {}, "raw": {}, "raw_rerun": {}}

def save_ckpt(d):
    tmp = CKPT + ".tmp"
    with open(tmp, "w") as f: json.dump(d, f, indent=1)
    os.replace(tmp, CKPT)

def parse_json_block(text):
    # find first {...} block, tolerate prose wrapping
    m = re.search(r'\{.*\}', text, re.S)
    if not m: return None
    block = m.group(0)
    for attempt in (block, block.replace("'", '"')):
        try:
            d = json.loads(attempt)
            break
        except Exception:
            d = None
    if d is None: return None
    out = {}
    for k in KEYS:
        v = d.get(k)
        out[k] = str(v).strip().lower() if v is not None else "missing"
    return out

def ask(folio):
    img = os.path.join(FOLIOS, folio + ".jpg")
    with open(img, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    payload = {
        "model": "vl-phase7",
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
            {"type": "text", "text": PROMPT},
        ]}],
        "max_tokens": 2500,
        "temperature": 0.1,
    }
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=420) as r:
        d = json.loads(r.read())
    msg = d["choices"][0]["message"]
    content = msg.get("content") or ""
    # reasoning models may put JSON after thinking; content is post-reasoning with --jinja
    return 0, content.strip(), ""

def main():
    args = sys.argv[1:]
    rerun = "--rerun" in args
    if rerun: args.remove("--rerun")
    ck = load_ckpt()
    feat_key = "rerun" if rerun else "features"
    raw_key = "raw_rerun" if rerun else "raw"
    if args == ["--all"]:
        targets = sorted(f[:-4] for f in os.listdir(FOLIOS) if f.endswith(".jpg"))
    else:
        targets = args
    done = 0
    for i, folio in enumerate(targets):
        if folio in ck[feat_key]:
            continue
        t0 = time.time()
        try:
            rc, out, err = ask(folio)
        except Exception as e:
            print(f"[{folio}] REQUEST-FAIL {e}", flush=True); save_ckpt(ck); time.sleep(3); continue
        dt = time.time() - t0
        ck[raw_key][folio] = out[-4000:]
        parsed = parse_json_block(out) if rc == 0 else None
        if parsed:
            ck[feat_key][folio] = parsed
            print(f"[{folio}] ok {dt:.1f}s {parsed['leaf_shape']}/{parsed['root_type']}/fl:{parsed['flower_present']}", flush=True)
        else:
            print(f"[{folio}] PARSE-FAIL rc={rc} {dt:.1f}s out[:200]={out[:200]!r} err[:200]={err[:200]!r}", flush=True)
        done += 1
        if done % 10 == 0 or parsed is None:
            save_ckpt(ck)
    save_ckpt(ck)
    print(f"total parsed ({feat_key}): {len(ck[feat_key])}")

if __name__ == "__main__":
    main()
