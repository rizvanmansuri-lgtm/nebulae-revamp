#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_index_header.py — make index.html the SINGLE SOURCE OF TRUTH for the site menu (header).

What it does (run from the project root; safe to re-run):
  1. Extracts the header block of index.html  (<div id="nblProgressBar"> … </header>).
  2. Writes it to tools/templates/header.html (used by tools/build_pages.py for products.html and products/*.html).
  3. Replaces the header block in every other hand-written page (root pages + industries/ services/ solutions/),
     adding the right '../' prefix for pages inside a sub-folder.
Skipped on purpose: index.html (the source), test.html (unrelated page), tools/, generated pages (products.html, products/*.html — rebuilt by build_pages.py).

Usage:   python3 tools/apply_index_header.py [--dry-run]
After changing the menu in index.html: run this, then  python3 tools/build_pages.py
"""
import os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
DRY = '--dry-run' in sys.argv
BAR, STICKY, ENDC = '<div id="nblProgressBar"', 'atl-sticky-header', '<!-- /.atl-sticky-header -->'

def prefix_links(t, base):
    def fix(m):
        attr, q, v = m.group(1), m.group(2), m.group(3)
        if v == '' or re.match(r'(?:[a-z][a-z0-9+.-]*:|#|//|/)', v, re.I): return m.group(0)
        if v.startswith('./'): v = v[2:]
        return f'{attr}={q}{base}{v}{q}'
    return re.sub(r'(?<![\w-])(href|src|action)=(["\'])([^"\']*)\2', fix, t)

BURGER = ('<div class="atl-nav__right"><button class="atl-nav__burger" id="navBurger" aria-label="Menu" aria-expanded="false">'
          '<span></span><span></span><span></span></button></div>')

def ensure_burger(idx):
    """index.html's header lost its mobile hamburger together with the old right-hand CTA block, so on phones the
    menu could not be opened. Re-add ONLY the hamburger (hidden on desktop by CSS) at the old "Right: CTA" spot."""
    if 'id="navBurger"' in idx: return idx, False
    m = '<!-- Right: CTA -->'
    assert idx.count(m) == 1, 'cannot find the "Right: CTA" marker in index.html'
    return idx.replace(m, m + '\n        ' + BURGER), True

def extract_block(idx):
    a = idx.find(BAR); s = idx.find(STICKY); e = idx.find('</header>', s)
    assert a > 0 and s > a and e > s, 'index.html header markers not found'
    blk = idx[a:e + len('</header>')]
    # the only page-specific link: mobile "Home" (#home only works on the home page)
    blk = blk.replace('<a class="atl-nav__mlink" href="#home">Home</a>', '<a class="atl-nav__mlink" href="index.html">Home</a>')
    return blk

def region(s):
    """(start, end) of the header block in a page, or None."""
    sticky = s.find(STICKY)
    if sticky < 0: return None
    start = s.find(BAR)
    if start < 0 or start > sticky:
        h = s.rfind('<header', 0, sticky); start = h
        if start < 0: return None
    opened_header = s.find('<header', start, sticky) != -1
    if opened_header:
        e = s.find('</header>', sticky)
        if e < 0: return None
        return start, e + len('</header>')
    e = s.find(ENDC, sticky)
    if e < 0: return None
    end = e + len(ENDC)
    return start, end

def main():
    idx = open(ROOT + 'index.html', encoding='utf-8').read()
    idx, changed = ensure_burger(idx)
    if changed:
        print('index.html: re-added the mobile hamburger (#navBurger) to the header')
        if not DRY: open(ROOT + 'index.html', 'w', encoding='utf-8').write(idx)
    block = extract_block(idx)
    print(f'index.html header block: {len(block):,} bytes')
    if not DRY: open(ROOT + 'tools/templates/header.html', 'w', encoding='utf-8').write(block)
    GEN = {'products.html'}
    done, same, skipped = [], [], []
    files = sorted(glob.glob(ROOT + '*.html') + glob.glob(ROOT + '*/*.html'))
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        if rel in GEN or rel.startswith(('products/', 'tools/')) or rel in ('index.html', 'test.html'):
            skipped.append(rel); continue
        s = open(f, encoding='utf-8', errors='ignore').read()
        r = region(s)
        if not r: skipped.append(rel + ' (no header found)'); continue
        base = '../' * rel.count('/')
        new = prefix_links(block, base) if base else block
        if s[r[0]:r[1]] == new: same.append(rel); continue
        if not DRY: open(f, 'w', encoding='utf-8').write(s[:r[0]] + new + s[r[1]:])
        done.append(rel)
    print(f'updated {len(done)} pages, {len(same)} already identical, skipped {len(skipped)}')
    for x in skipped: print('  skipped:', x)
    return done

if __name__ == '__main__':
    main()
