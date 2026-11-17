#!/usr/bin/env python3
"""apply_theme.py — switch the whole site between the two versions.
  python3 tools/apply_theme.py light   → links assets/css/theme-light.css on every page (light sections + light banners; header/footer unchanged)
  python3 tools/apply_theme.py dark    → removes the link (original dark version)
  python3 tools/apply_theme.py          → shows the current version
The choice is stored in tools/theme.txt and respected by every builder (apply_shared_assets.py)."""
import os, sys, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
f = ROOT + 'tools/theme.txt'
cur = open(f).read().strip() if os.path.exists(f) else 'dark'
if len(sys.argv) < 2: print('current version:', cur); sys.exit()
v = sys.argv[1].lower()
if v not in ('light', 'dark'): sys.exit('usage: apply_theme.py light|dark')
open(f, 'w').write(v + '\n')
if v == 'light' and not os.path.exists(ROOT + 'assets/css/theme-light.css'): sys.exit('assets/css/theme-light.css missing — run tools/build_theme_light.py first')
subprocess.call([sys.executable, ROOT + 'tools/apply_shared_assets.py'])
print('site is now the', v.upper(), 'version')
