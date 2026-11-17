#!/usr/bin/env python3
"""SEO / meta pass (metadata only — no visual change). Idempotent. Run: python3 tools/seo_fix.py
- trims over-long <title> (>65) and meta description (>160), keeping the first/primary phrase
- adds missing og:title/description/type/url/image/site_name and twitter:card/title/description/image
- adds BreadcrumbList JSON-LD where a page has none
- fixes canonical case, noindex for the product template page
Changed titles/descriptions are logged to tools/seo_changes.csv so they can be reviewed/edited."""
import os, re, glob, json, csv, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
BASE = 'https://www.nebulae.io/'
OG_DEFAULT = BASE + 'assets/images/og-nebulae.jpg'
os.chdir(ROOT)
SECTION = {'industries': ('Industries', 'industries.html'), 'solutions': ('Solutions', 'solutions.html'), 'services': ('Services', 'services.html'), 'products': ('Products', 'products.html')}
changes = []

def short_title(t):
    raw = html.unescape(t)
    if len(raw) <= 70: return t
    parts = [p.strip() for p in re.split(r'\s+[|—–]\s+', raw) if p.strip()]
    brand = 'Nebulae'
    core = [p for p in parts if not p.lower().startswith('nebulae')] or parts[:1]
    def dedupe(p):                                   # "X Y X Y Card" -> "X Y Card"
        w = p.split()
        for n in range(len(w) // 2, 1, -1):
            for i in range(0, len(w) - 2 * n + 1):
                if w[i:i + n] == w[i + n:i + 2 * n]: return ' '.join(w[:i + n] + w[i + 2 * n:])
        return p
    core = [dedupe(p) for p in core]
    out = None
    for k in range(len(core), 0, -1):
        c = ' — '.join(core[:k]) + ' | ' + brand
        if len(c) <= 70: out = c; break
        if k > 1:                                    # keep the secondary phrase but cut it at a comma / word boundary so it fits
            room = 70 - len(' — '.join(core[:k - 1])) - len(' — ') - len(' | ' + brand)
            sec = core[k - 1]
            if room >= 14 and ',' in sec[:room + 1]:
                sec = sec[:room + 1].rsplit(',', 1)[0]
                out = ' — '.join(core[:k - 1] + [sec]) + ' | ' + brand; break
    if not out:
        p = core[0]
        if len(p) > 52: p = p[:52].rsplit(' ', 1)[0].rstrip(' ,:;—-')
        out = p + ' | ' + brand
    return html.escape(out, quote=False).replace('&amp;amp;', '&amp;')

def short_desc(d):
    raw = html.unescape(d)
    if len(raw) <= 160: return d
    cut = raw[:158]
    for sep in ('. ', '; ', ' — ', ', '):
        i = cut.rfind(sep)
        if i >= 90: cut = cut[:i + (1 if sep == '. ' else 0)]; break
    else:
        cut = cut.rsplit(' ', 1)[0]
    cut = cut.rstrip(' ,;—-')
    if not cut.endswith('.'): cut += '.'
    return html.escape(cut, quote=False).replace('&amp;amp;', '&amp;').replace('"', '&quot;')

def getmeta(s, attr, val):
    m = re.search(r'<meta\b[^>]*\b%s="%s"[^>]*>' % (attr, re.escape(val)), s)
    if not m: return None, None
    c = re.search(r'content="([^"]*)"', m.group(0)); return m, (c.group(1) if c else '')

def setmeta(s, m, newval):
    return s[:m.start()] + re.sub(r'content="[^"]*"', 'content="%s"' % newval.replace('\\', '\\\\'), m.group(0)) + s[m.end():]

n = 0
for f in sorted(glob.glob('*.html') + glob.glob('*/*.html')):
    s = o = open(f, encoding='utf-8').read()
    is404 = f == '404.html'
    # ── canonical case fix
    s = s.replace('nebulae.io/Resources.html', 'nebulae.io/resources.html')
    # ── product template page must not be indexed
    if f == 'product-detail.html': s = s.replace('content="index, follow"', 'content="noindex, follow"', 1)
    # ── title
    tm = re.search(r'<title>(.*?)</title>', s, re.S)
    if tm and not is404:
        nt = short_title(tm.group(1).strip())
        if nt != tm.group(1).strip() and f != 'product-detail.html':
            changes.append((f, 'title', tm.group(1).strip(), nt)); s = s[:tm.start(1)] + nt + s[tm.end(1):]
    title = re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip() if tm else ''
    # ── description
    dm, dv = getmeta(s, 'name', 'description')
    if dm and not is404 and f != 'product-detail.html':
        nd = short_desc(dv)
        if nd != dv: changes.append((f, 'description', dv, nd)); s = setmeta(s, dm, nd); dm, dv = getmeta(s, 'name', 'description')
    desc = dv or ''
    # ── canonical (computed if absent)
    cm = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', s)
    canon = cm.group(1) if cm else (BASE if f == 'index.html' else BASE + f)
    if not is404 and f != 'product-detail.html':
        add = []
        ogt = getmeta(s, 'property', 'og:title')[0]; ogi = getmeta(s, 'property', 'og:image')[1]
        kind = 'article' if re.search(r'(blog-[a-z0-9-]+|news-detail|event-[a-z0-9-]+)\.html$', f) else 'website'
        if not ogt: add.append(f'<meta property="og:title" content="{title}"/>')
        if not getmeta(s, 'property', 'og:description')[0] and desc: add.append(f'<meta property="og:description" content="{desc}"/>')
        if not getmeta(s, 'property', 'og:type')[0]: add.append(f'<meta property="og:type" content="{kind}"/>')
        if not getmeta(s, 'property', 'og:url')[0]: add.append(f'<meta property="og:url" content="{canon}"/>')
        if not getmeta(s, 'property', 'og:site_name')[0]: add.append('<meta property="og:site_name" content="Nebulae"/>')
        if ogi is None: add.append(f'<meta property="og:image" content="{OG_DEFAULT}"/>'); ogi = OG_DEFAULT
        if not getmeta(s, 'name', 'twitter:card')[0]:
            add += ['<meta name="twitter:card" content="summary_large_image"/>', f'<meta name="twitter:title" content="{(getmeta(s, "property", "og:title")[1] or title)}"/>']
            if desc: add.append(f'<meta name="twitter:description" content="{(getmeta(s, "property", "og:description")[1] or desc)}"/>')
            add.append(f'<meta name="twitter:image" content="{ogi}"/>')
        if add: s = s.replace('</head>', '  ' + '\n  '.join(add) + '\n</head>', 1)
        # ── breadcrumb JSON-LD
        if 'BreadcrumbList' not in s and f not in ('index.html', 'index-new.html'):
            h1 = re.search(r'<h1\b[^>]*>(.*?)</h1>', s, re.S)
            name = html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip() if h1 else html.unescape(title.split('|')[0]).strip()
            name = re.sub(r'\s+', ' ', name)
            items = [('Home', BASE)]
            d = os.path.dirname(f)
            if d in SECTION: items.append((SECTION[d][0], BASE + SECTION[d][1]))
            items.append((name, canon))
            ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": a, "item": b} for i, (a, b) in enumerate(items)]}
            s = s.replace('</head>', '  <script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>\n</head>', 1)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
if changes:
    new = not os.path.exists('tools/seo_changes.csv')
    with open('tools/seo_changes.csv', 'a', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        if new: w.writerow(['page', 'field', 'old', 'new'])
        w.writerows(changes)
print('seo pass: pages changed', n, '| title/description rewrites', len(changes))
