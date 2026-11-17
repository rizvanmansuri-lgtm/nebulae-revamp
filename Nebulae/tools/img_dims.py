#!/usr/bin/env python3
"""Add intrinsic width/height to local <img> tags that lack them (prevents layout shift). Idempotent. Skips svg / remote / data."""
import os, re, glob
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
os.chdir(ROOT)
cache = {}
def dims(path):
    if path not in cache:
        try:
            with Image.open(path) as im: cache[path] = im.size
        except Exception: cache[path] = None
    return cache[path]
n = tot = 0
for f in sorted(glob.glob('*.html') + glob.glob('*/*.html')):
    s = o = open(f, encoding='utf-8').read(); base = os.path.dirname(f)
    def fix(m):
        global tot
        t = m.group(0)
        if re.search(r'\swidth=', t) and re.search(r'\sheight=', t): return t
        src = re.search(r'\ssrc="([^"]+)"', t)
        if not src or 'SupportedTech' in src.group(1) or re.match(r'(https?:|data:|//)', src.group(1)) or src.group(1).lower().endswith('.svg'): return t
        p = os.path.normpath(os.path.join(base, src.group(1).split('?')[0]))
        d = dims(p)
        if not d: return t
        t = re.sub(r'\s(width|height)="[^"]*"', '', t)
        tot += 1
        return t[:-2].rstrip() + f' width="{d[0]}" height="{d[1]}"/>' if t.endswith('/>') else t[:-1].rstrip() + f' width="{d[0]}" height="{d[1]}">'
    s = re.sub(r'<img\b[^>]*>', fix, s)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('img dims added on', tot, 'tags in', n, 'pages')
