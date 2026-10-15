#!/usr/bin/env python3
"""apply_shared_assets.py — idempotent. On EVERY html page: adds nebulae-fixes.css (last in <head>), nebulae-float.js (end of <body>)
and trims the Google-Fonts link to Poppins only. Run after any builder:  python3 tools/apply_shared_assets.py"""
import os, re, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
n = 0
for f in sorted(glob.glob(ROOT + '*.html') + glob.glob(ROOT + '*/*.html')):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith('tools' + os.sep): continue
    base = '../' if os.sep in rel else './'
    s = o = open(f, encoding='utf-8').read()
    if 'nebulae-fixes.css' not in s:
        s = s.replace('</head>', f'  <link rel="stylesheet" href="{base}assets/css/nebulae-fixes.css">\n</head>', 1)
    if 'nebulae-float.js' not in s:
        s = s.replace('</body>', f'<script src="{base}assets/js/nebulae-float.js"></script>\n</body>', 1)
    # Poppins only (drop Outfit / IBM Plex Mono from the font request)
    s = re.sub(r'&family=Outfit:[^&"]*', '', s); s = re.sub(r'&family=IBM\+Plex\+Mono:[^&"]*', '', s)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('shared assets applied to', n, 'pages')
