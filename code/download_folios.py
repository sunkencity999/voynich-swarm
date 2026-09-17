#!/usr/bin/env python3
"""Phase 7: download herbal folio images from voynich.nu (_crd.jpg, folio-keyed).

Folio -> quire dir mapping comes from voynich.nu quire index pages.
Polite: sequential, 1.1s sleep, resumable (skips existing valid files).
"""
import os, re, sys, time, urllib.request

BASE = "http://www.voynich.nu"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "folios")
os.makedirs(OUT, exist_ok=True)

# herbal folios from ZL3b-n.txt $I=H
HERBAL = ['f1v','f2r','f2v','f3r','f3v','f4r','f4v','f5r','f5v','f6r','f6v','f7r','f7v','f8r','f8v','f9r','f9v','f10r','f10v','f11r','f11v','f13r','f13v','f14r','f14v','f15r','f15v','f16r','f16v','f17r','f17v','f18r','f18v','f19r','f19v','f20r','f20v','f21r','f21v','f22r','f22v','f23r','f23v','f24r','f24v','f25r','f25v','f26r','f26v','f27r','f27v','f28r','f28v','f29r','f29v','f30r','f30v','f31r','f31v','f32r','f32v','f33r','f33v','f34r','f34v','f35r','f35v','f36r','f36v','f37r','f37v','f38r','f38v','f39r','f39v','f40r','f40v','f41r','f41v','f42r','f42v','f43r','f43v','f44r','f44v','f45r','f45v','f46r','f46v','f47r','f47v','f48r','f48v','f49r','f49v','f50r','f50v','f51r','f51v','f52r','f52v','f53r','f53v','f54r','f54v','f55r','f55v','f56r','f56v','f57r','f65r','f65v','f66v','f87r','f87v','f90r1','f90r2','f90v2','f90v1','f93r','f93v','f94r','f94v','f95r1','f95r2','f95v2','f95v1','f96r','f96v']

def fetch(url, dest=None, binary=True):
    req = urllib.request.Request(url, headers={'User-Agent': 'research-script (Voynich statistics study; polite sequential)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if dest:
        with open(dest, 'wb') as f: f.write(data)
    return data

def crd_name(folio):
    # f1v -> f001v ; f90r1 -> f090r1
    m = re.match(r'f(\d+)([rv])(\d*)$', folio)
    return "f%03d%s%s" % (int(m.group(1)), m.group(2), m.group(3))

def main():
    # 1. discover quire dirs per folio by scanning quire index pages q01..q20
    folio_to_quire = {}
    for q in range(1, 21):
        qd = "q%02d" % q
        try:
            html = fetch(f"{BASE}/{qd}/index.html").decode('utf-8', 'replace')
        except Exception as e:
            print(f"[warn] {qd}/index.html: {e}"); continue
        for m in re.finditer(r'(f\d{3}[rv]\d?)_crd\.jpg', html):
            name = m.group(1)
            # normalize f001v -> f1v
            mm = re.match(r'f0*(\d+)([rv])(\d*)', name)
            key = f"f{mm.group(1)}{mm.group(2)}{mm.group(3)}"
            folio_to_quire.setdefault(key, qd)
        time.sleep(1.1)
    print(f"discovered {len(folio_to_quire)} folio images across quire pages")

    missing_map = [f for f in HERBAL if f not in folio_to_quire]
    if missing_map:
        print("no quire mapping for:", missing_map)

    ok, fail = 0, []
    for folio in HERBAL:
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
        time.sleep(1.1)
    print(f"downloaded/present: {ok}/{len(HERBAL)}")
    if fail:
        print("FAILURES:")
        for f, why in fail: print(" ", f, why)

if __name__ == '__main__':
    main()
