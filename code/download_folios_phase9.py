#!/usr/bin/env python3
"""Phase 9 WP3: download pharmaceutical ($I=P) and balneological ($I=B) folio
images from voynich.nu (_crd.jpg, folio-keyed), same pattern as phase 7.
Polite: sequential, 1.5s sleep, resumable (skips existing valid files).
"""
import os, re, time, urllib.request

BASE = "http://www.voynich.nu"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "folios")
os.makedirs(OUT, exist_ok=True)

PHARMA = ['f88r','f88v','f89r1','f89r2','f89v1','f89v2','f99r','f99v',
          'f100r','f100v','f101r','f101v','f102r1','f102r2','f102v1','f102v2']
BALNEO = ['f75r','f75v','f76v','f77r','f77v','f78r','f78v','f79r','f79v',
          'f80r','f80v','f81r','f81v','f82r','f82v','f83r','f83v','f84r','f84v']
# f76r carries $I=S in ZL but sits physically in the balneo quire; not needed.
TARGETS = PHARMA + BALNEO

def fetch(url, dest=None):
    req = urllib.request.Request(url, headers={'User-Agent':
        'research-script (Voynich statistics study; polite sequential)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if dest:
        with open(dest, 'wb') as f: f.write(data)
    return data

def crd_name(folio):
    m = re.match(r'f(\d+)([rv])(\d*)$', folio)
    return "f%03d%s%s" % (int(m.group(1)), m.group(2), m.group(3))

def main():
    folio_to_quire = {}
    for q in range(13, 21):   # balneo quire M, pharma quires O,S -> q13..q20 covers them
        qd = "q%02d" % q
        try:
            html = fetch(f"{BASE}/{qd}/index.html").decode('utf-8', 'replace')
        except Exception as e:
            print(f"[warn] {qd}/index.html: {e}"); continue
        for m in re.finditer(r'(f\d{3}[rv]\d?)_crd\.jpg', html):
            name = m.group(1)
            mm = re.match(r'f0*(\d+)([rv])(\d*)', name)
            key = f"f{mm.group(1)}{mm.group(2)}{mm.group(3)}"
            folio_to_quire.setdefault(key, qd)
        time.sleep(1.5)
    print(f"discovered {len(folio_to_quire)} folio images across quire pages q13-q20")

    missing = [f for f in TARGETS if f not in folio_to_quire]
    if missing:
        print("no quire mapping for:", missing)

    ok, fail = 0, []
    for folio in TARGETS:
        dest = os.path.join(OUT, folio + ".jpg")
        if os.path.exists(dest) and os.path.getsize(dest) > 20000:
            ok += 1; continue
        qd = folio_to_quire.get(folio)
        if not qd:
            fail.append((folio, 'no-quire-mapping')); continue
        url = f"{BASE}/{qd}/{crd_name(folio)}_crd.jpg"
        try:
            fetch(url, dest)
            sz = os.path.getsize(dest)
            with open(dest, 'rb') as f: magic = f.read(3)
            if sz < 20000 or magic != b'\xff\xd8\xff':
                fail.append((folio, f'bad file sz={sz}')); os.rename(dest, dest + '.bad')
            else:
                ok += 1
        except Exception as e:
            fail.append((folio, str(e)))
        time.sleep(1.5)
    print(f"downloaded/present: {ok}/{len(TARGETS)}")
    if fail:
        print("FAILURES:")
        for f, why in fail: print(" ", f, why)

if __name__ == '__main__':
    main()
