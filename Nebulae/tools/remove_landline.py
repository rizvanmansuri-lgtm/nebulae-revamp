#!/usr/bin/env python3
"""Removes the Anand landline (+91-02692-232501/02) everywhere; the mobile +91 9898042339 stays.
Idempotent. Usage: python3 tools/remove_landline.py [root]"""
import re, glob, sys, os
root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
MOB_TEL, MOB_TXT = 'tel:+919898042339', '+91 9898042339'
n = 0
for f in glob.glob(root + '/**/*', recursive=True):
    if not f.endswith(('.html', '.js', '.xml', '.json', '.md', '.py', '.txt')) or 'node_modules' in f or f.endswith('remove_landline.py'): continue
    s = open(f, encoding='utf-8', errors='ignore').read(); o = s
    if '02692' not in s and '2692-232' not in s: continue
    # header top-bar link (whole anchor)
    s = re.sub(r'[ \t]*<a href="tel:\+9102692232501"[^>]*>\s*<svg.*?</svg>\s*\+91-02692-232501/02\s*</a>\n?', '', s, flags=re.S)
    s = s.replace('tel:+9102692232501', MOB_TEL)
    for t in ('+91-02692-232501 / 232502', '+91-02692-232501/02', '+91-2692-232 501 / 502', '+91-02692-232501'):
        s = s.replace(t, MOB_TXT if 'telephone' not in t else t)
    s = re.sub(r'("telephone":\s*")\+91 9898042339', r'\1+91-9898042339', s)
    s = s.replace('"telephone": "+91-02692-232501"', '"telephone": "+91-9898042339"')
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('files changed', n)
