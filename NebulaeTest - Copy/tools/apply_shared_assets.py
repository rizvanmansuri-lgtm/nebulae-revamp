#!/usr/bin/env python3
"""apply_shared_assets.py — idempotent. On EVERY html page: adds nebulae-fixes.css (last in <head>), nebulae-float.js (end of <body>)
and trims the Google-Fonts link to Poppins only. Run after any builder:  python3 tools/apply_shared_assets.py"""
import os, re, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
n = 0
_tf = ROOT + 'tools/theme.txt'
THEME = open(_tf).read().strip() if os.path.exists(_tf) else 'dark'
DRAWER = open(ROOT + 'tools/templates/quote-drawer.html', encoding='utf-8').read()
for f in sorted(glob.glob(ROOT + '*.html') + glob.glob(ROOT + '*/*.html')):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith('tools' + os.sep): continue
    base = '../' if os.sep in rel else './'
    s = o = open(f, encoding='utf-8').read()
    if 'rel="icon"' not in s and 'rel="shortcut icon"' not in s:
        s = s.replace('</head>', f'  <link rel="icon" type="image/png" href="{base}favicon.png">\n</head>', 1)
    s = re.sub(r'<h6( class="atl-footer__heading[^"]*"[^>]*)>(.*?)</h6>', r'<p\1>\2</p>', s, flags=re.S)
    if 'nebulae-fixes.css' not in s:
        s = s.replace('</head>', f'  <link rel="stylesheet" href="{base}assets/css/nebulae-fixes.css">\n</head>', 1)
    if DRAWER in s: s = s.replace(DRAWER + '\n', '').replace(DRAWER, '')   # strip first; re-placed below BEFORE the scripts that wire it
    HAS_FORMS = re.search(r'<script[^>]*nebulae-forms\.js', s); HAS_FLOAT = re.search(r'<script[^>]*nebulae-float\.js', s)
    if not HAS_FORMS:
        if HAS_FLOAT:
            s = re.sub(r'(<script[^>]*nebulae-float\.js[^>]*></script>)', f'<script src="{base}assets/js/nebulae-forms.js"></script>\n\\1', s, 1)
        else:
            s = s.replace('</body>', f'<script src="{base}assets/js/nebulae-forms.js"></script>\n</body>', 1)
    if 'id="nblFloatForm"' not in s:
        m = re.search(r'<script[^>]*nebulae-forms\.js', s)
        s = s[:m.start()] + DRAWER + '\n' + s[m.start():]
    if not re.search(r'<script[^>]*nebulae-float\.js', s):
        s = s.replace('</body>', f'<script src="{base}assets/js/nebulae-float.js"></script>\n</body>', 1)
    # theme version: the light stylesheet is linked LAST in <head> only when tools/theme.txt says 'light'
    s = re.sub(r'[ \t]*<link rel="stylesheet" href="[^"]*theme-light\.css">\n?', '', s)
    if THEME == 'light':
        s = s.replace('</head>', f'  <link rel="stylesheet" href="{base}assets/css/theme-light.css">\n</head>', 1)
    # Poppins only (drop Outfit / IBM Plex Mono from the font request)
    s = re.sub(r'&family=Outfit:[^&"]*', '', s); s = re.sub(r'&family=IBM\+Plex\+Mono:[^&"]*', '', s)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('shared assets applied to', n, 'pages')
