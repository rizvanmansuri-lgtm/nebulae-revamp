#!/usr/bin/env python3
"""
check_links.py — verify that every local href/src in the generated pages resolves to a real file.
Usage: python3 tools/check_links.py [--all]      (--all also checks the root site pages)
Ignores external URLs, mailto:, tel:, #anchors, javascript:, data:. Strips ?query and #hash before checking.
Exit code 1 if any generated-page link is broken. Header/footer links to pages that do not exist in the
project (e.g. service pages) are reported separately as 'site-wide' so they are not confused with product-page bugs.
"""
import os, re, sys, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
check_all = '--all' in sys.argv
files = sorted(glob.glob(ROOT + '/products/*.html')) + [ROOT + '/products.html']
if check_all: files += [f for f in sorted(glob.glob(ROOT + '/*.html')) if f not in files]
attr = re.compile(r'(?<![\w-])(?:href|src)=(["\'])([^"\']*)\1')
broken = collections.defaultdict(set); n = 0
for f in files:
    s = open(f, encoding='utf-8', errors='ignore').read()
    base = os.path.dirname(f)
    for _, v in attr.findall(s):
        if not v or re.match(r'(?:[a-z][a-z0-9+.-]*:|#|//)', v, re.I): continue
        path = v.split('#')[0].split('?')[0]
        if not path: continue
        tgt = os.path.normpath(os.path.join(ROOT if path.startswith('/') else base, path.lstrip('/') if path.startswith('/') else path))
        n += 1
        if not os.path.exists(tgt): broken[v].add(os.path.relpath(f, ROOT))
# targets that come from the shared header/footer templates are 'site-wide' (they belong to the rest of the site)
tpl = open(ROOT + '/tools/templates/header.html', encoding='utf-8').read() + open(ROOT + '/tools/templates/footer.html', encoding='utf-8').read()
tpl_targets = {os.path.normpath(v.split('#')[0].split('?')[0].lstrip('./')) for _, v in attr.findall(tpl) if v and not re.match(r'(?:[a-z][a-z0-9+.-]*:|#|//)', v, re.I)}
def is_shared(k):
    t = os.path.normpath(k.split('#')[0].split('?')[0])
    t = re.sub(r'^(\.\./|\./)+', '', t)
    return t in tpl_targets
shared = {k: v for k, v in broken.items() if is_shared(k)}
own = {k: v for k, v in broken.items() if not is_shared(k)}
print(f'checked {n} local links in {len(files)} files')
if shared:
    print(f'site-wide (header/footer) targets missing in this project: {len(shared)}')
    for k in sorted(shared): print('   ', k)
if own:
    print('BROKEN page-specific links:')
    for k, v in sorted(own.items()): print('   ', k, '<-', sorted(v)[:3])
    sys.exit(1)
print('page-specific links OK')
