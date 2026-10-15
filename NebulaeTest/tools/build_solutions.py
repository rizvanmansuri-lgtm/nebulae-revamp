#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_solutions.py — generates the solution pages (solutions/*.html) and the HES / LMS / CCMS-EV service pages
(services/*.html) from tools/solutions_data.py (facts taken from the solutions_pdfs brochures).
Header = index.html header block, footer = index.html footer (same as every other page).
Usage (from project root):  python3 tools/build_solutions.py
Edit text/specs in tools/solutions_data.py, re-run. Images live in assets/images/solutions/.
"""
import os, re, sys, html, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
sys.path.insert(0, os.path.dirname(__file__))
from solutions_data import PAGES, RELATED
spec = importlib.util.spec_from_file_location('aih', ROOT + 'tools/apply_index_header.py'); aih = importlib.util.module_from_spec(spec); spec.loader.exec_module(aih)
idx = open(ROOT + 'index.html', encoding='utf-8').read()
HEADER_ROOT = aih.extract_block(idx)
FOOTER_ROOT = idx[idx.find('<footer'):idx.find('</footer>') + 9]
HEADER, FOOTER = aih.prefix_links(HEADER_ROOT, '../'), aih.prefix_links(FOOTER_ROOT, '../')
E = lambda s: html.escape(str(s), quote=True)
CHECK = '<svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
IMG = '../assets/images/solutions/'

def table(rows, head=('Parameter', 'Specification')):
    b = ''.join(f'<tr><td>{E(k)}</td><td>{E(v)}</td></tr>' for k, v in rows)
    return (f'<div class="slx-table-wrap"><table class="sl-compare-table"><thead><tr><th>{E(head[0])}</th><th>{E(head[1])}</th></tr></thead>'
            f'<tbody>{b}</tbody></table></div>')

def section_tables(p, n):
    out = ''
    for gi, g in enumerate(p.get('tables', [])):
        sid = g.get('id', f'tbl{gi}')
        out += f'<section class="sl-section{" sl-section--surf" if gi % 2 == 0 else ""}" id="{sid}"><div class="container">'
        out += f'<div class="sl-eyebrow-sm">{E(g["eyebrow"])}</div><h2 class="sl-section-title">{E(g["title"])}</h2>'
        if g.get('intro'): out += f'<p class="sl-section-desc" style="max-width:760px;color:#4b5563">{E(g["intro"])}</p>'
        if 'tabs' in g:
            out += '<ul class="nav slx-pills" role="tablist">'
            for ti, (lab, _) in enumerate(g['tabs']):
                out += (f'<li class="nav-item" role="presentation"><button class="nav-link{" active" if ti == 0 else ""}" data-bs-toggle="pill" '
                        f'data-bs-target="#{sid}-t{ti}" type="button" role="tab" aria-selected="{"true" if ti == 0 else "false"}">{E(lab)}</button></li>')
            out += '</ul><div class="tab-content">'
            for ti, (lab, rows) in enumerate(g['tabs']):
                out += f'<div class="tab-pane fade{" show active" if ti == 0 else ""}" id="{sid}-t{ti}" role="tabpanel">{table(rows)}</div>'
            out += '</div>'
        else:
            cols = g['cols']
            out += '<div class="row g-4 mt-1">'
            for c in cols:
                w = 12 if len(cols) == 1 else 6
                out += f'<div class="col-lg-{w}">'
                if c.get('title'): out += f'<h3 class="slx-sub">{E(c["title"])}</h3>'
                out += table(c['rows'], c.get('head', ('Parameter', 'Specification')))
                if c.get('note'): out += f'<p class="slx-note">{E(c["note"])}</p>'
                out += '</div>'
            out += '</div>'
        if g.get('note'): out += f'<p class="slx-note">{E(g["note"])}</p>'
        out += '</div></section>\n'
    return out

def build(p):
    sub = p['dir']; slug = p['slug']; ov = p['overview']; acc = p.get('accent', '#4f46e5')
    pill_html = ''.join(f'<a href="#{i}" class="sl-jump-pill">{E(l)}</a>' for i, l in p['pills'])
    feats = ''.join(f'<li><div class="sl-feat-list__icon" style="background:rgba(79,70,229,.1);color:{acc};">{CHECK}</div>'
                    f'<span><strong>{E(a)}</strong> — {E(b)}</span></li>' for a, b in ov['features'])
    metrics = ''.join(f'<div class="sl-metric"><span class="sl-metric__val">{E(v)}</span><span class="sl-metric__label">{E(l)}</span></div>' for v, l in ov['metrics'])
    stats = ''.join(f'<div class="sl-img-card__stat-item"><span class="sl-img-card__stat-num">{E(v)}</span><span class="sl-img-card__stat-label">{E(l)}</span></div>' for v, l in ov['stats'])
    chips = ''.join(f'<a href="{E(h)}" class="sl-product-chip">{E(l)}</a>' for l, h in ov.get('chips', []))
    paras = ''.join(f'<p class="sl-solution__desc" style="color:#374151;">{E(t)}</p>' for t in ov['desc'])
    h = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{E(p['title'])}</title>
  <meta name="description" content="{E(p['desc'])}" />
  <meta name="keywords" content="{E(p['keywords'])}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.nebulae.io/{sub}/{slug}.html" />
  <meta property="og:title" content="{E(p['title'])}" />
  <meta property="og:description" content="{E(p['desc'])}" />
  <meta property="og:type" content="website" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Outfit:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="../assets/css/nebulae-nav.css">
  <link rel="stylesheet" href="../assets/css/solutions.css">
  <link rel="stylesheet" href="../assets/css/solutions-extra.css">
  <style>
    .sl-hero{{padding:5rem 0 4rem}}
    .sl-arch-card{{margin-top:1.25rem}}
    .sl-arch-arrow:last-child{{display:none}}
    .sl-related{{padding:4rem 0;background:#f5f7ff}}
    .sl-related__title{{font-family:'Outfit',sans-serif;font-size:1.35rem;font-weight:800;color:#111827;margin-bottom:1.5rem}}
    .sl-rel-card{{background:#fff;border:1.5px solid #e5e7eb;border-radius:18px;padding:1.5rem;display:block;text-decoration:none;transition:all .25s;height:100%}}
    .sl-rel-card:hover{{transform:translateY(-4px);box-shadow:0 16px 48px rgba(79,70,229,.1);border-color:rgba(79,70,229,.25)}}
    .sl-rel-card__tag{{font-size:.66rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:3px 10px;border-radius:100px;margin-bottom:.75rem;display:inline-block}}
    .sl-rel-card__name{{font-family:'Outfit',sans-serif;font-size:.95rem;font-weight:700;color:#111827;margin-bottom:.4rem}}
    .sl-rel-card__desc{{font-size:.8rem;color:#6b7280;line-height:1.6}}
    .sl-rel-card__arrow{{font-size:.78rem;font-weight:700;color:#4f46e5;margin-top:.75rem;display:block}}
  </style>
</head>
<body>
{HEADER}

<!-- HERO -->
<section class="sl-hero">
  <div class="sl-hero__grid"></div>
  <div class="sl-hero__orb sl-hero__orb--1"></div>
  <div class="sl-hero__orb sl-hero__orb--2"></div>
  <div class="container">
    <div class="sl-hero__inner">
      <nav class="sl-breadcrumb" aria-label="breadcrumb">
        <a href="../index.html">Home</a><span>›</span>
        <a href="../{p['parent'][1]}">{E(p['parent'][0])}</a><span>›</span>
        <span style="color:rgba(255,255,255,.65);">{E(p['crumb'])}</span>
      </nav>
      <div class="sl-eyebrow">{E(p['eyebrow'])}</div>
      <h1 class="sl-hero__title">{E(p['h1'])}</h1>
      <p class="sl-hero__desc">{E(p['lead'])}</p>
      <div class="sl-jump-pills">{pill_html}<a href="../contact.html" class="sl-jump-pill">Get a Proposal</a></div>
    </div>
  </div>
</section>

<!-- OVERVIEW -->
<section class="sl-section" id="overview">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        <div class="slx-hero-img">
          <img src="{IMG}{ov['img']}" alt="{E(ov['alt'])}" width="900" height="560"/>
          <div class="sl-img-card__stat">{stats}</div>
        </div>
      </div>
      <div class="col-lg-6">
        <span class="sl-solution__tag" style="background:rgba(79,70,229,.1);color:{acc};">{E(ov['tag'])}</span>
        <h2 class="sl-solution__title" style="color:#111827;">{E(ov['title'])}</h2>
        {paras}
        <div class="sl-metrics">{metrics}</div>
        <ul class="sl-feat-list" id="features">{feats}</ul>
        <div class="sl-products-strip">{chips}</div>
        <div style="display:flex;gap:.75rem;margin-top:1.75rem;flex-wrap:wrap;">
          <a href="../contact.html" class="sl-sol-btn sl-sol-btn--primary">Get a Proposal</a>
          <a href="../contact.html" class="sl-sol-btn sl-sol-btn--outline">Request Datasheet</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    # gallery
    g = p.get('gallery')
    if g:
        h += f'<section class="sl-section sl-section--surf" id="{g.get("id","gallery")}"><div class="container"><div class="sl-eyebrow-sm">{E(g["eyebrow"])}</div><h2 class="sl-section-title">{E(g["title"])}</h2><div class="row g-4 mt-1">'
        for im, cap in g['items']:
            h += (f'<div class="col-12 col-md-6{" col-lg-4" if len(g["items"]) % 3 == 0 or len(g["items"]) > 4 else ""}"><figure class="slx-fig"><div class="slx-fig__img">'
                  f'<img loading="lazy" src="{IMG}{im}" alt="{E(cap)}"/></div><figcaption>{E(cap)}</figcaption></figure></div>')
        h += '</div></div></section>\n'
    # tables
    h += section_tables(p, 0)
    # architecture
    a = p.get('arch')
    if a:
        layers = ''
        for i, (lab, desc) in enumerate(a['layers']):
            if i: layers += '<div class="sl-arch-arrow">↓</div>'
            layers += (f'<div class="sl-arch-layer"><div class="sl-arch-layer__icon" style="background:rgba(79,70,229,.1);color:{acc};font:800 .85rem Outfit,sans-serif;">{i+1}</div>'
                       f'<span class="sl-arch-layer__label">{E(lab)}</span><span class="sl-arch-layer__desc">{E(desc)}</span></div>')
        img = f'<div class="slx-arch-img"><img loading="lazy" src="{IMG}{a["img"]}" alt="{E(a["title"])}"/></div>' if a.get('img') else ''
        h += (f'<section class="sl-section" id="architecture"><div class="container"><div class="row g-5 align-items-start">'
              f'<div class="col-lg-6"><div class="sl-eyebrow-sm">{E(a["eyebrow"])}</div><h2 class="sl-section-title">{E(a["title"])}</h2>'
              f'<div class="sl-arch-card">{layers}</div>'
              f'{"<p class=slx-note>"+E(a["note"])+"</p>" if a.get("note") else ""}</div><div class="col-lg-6">{img}</div></div></div></section>\n')
    # cards
    for ci, c in enumerate(p.get('cards', [])):
        h += f'<section class="sl-section{" sl-section--surf" if ci % 2 == 0 else ""}" id="{c.get("id","benefits")}"><div class="container slx-cards"><div class="sl-eyebrow-sm">{E(c["eyebrow"])}</div><h2 class="sl-section-title">{E(c["title"])}</h2>'
        if c.get('stats'):
            h += '<div class="row g-3 mt-1 mb-3">' + ''.join(f'<div class="col-6 col-md-4"><div class="slx-stat"><b>{E(v)}</b><span>{E(l)}</span></div></div>' for v, l in c['stats']) + '</div>'
        h += '<div class="row g-3 mt-1">'
        for i, (t, d) in enumerate(c['items']):
            h += f'<div class="col-12 col-sm-6 col-lg-{c.get("cols",4)}"><div class="slx-card"><div class="slx-card__n">{i+1}</div><h3>{E(t)}</h3><p>{E(d)}</p></div></div>'
        h += '</div>'
        if c.get('note'): h += f'<p class="slx-note">{E(c["note"])}</p>'
        h += '</div></section>\n'
    # related
    rel = ''
    for k in p['related']:
        tag, name, desc, href, col = RELATED[k]
        link = href if sub == 'solutions' and href.startswith('solutions/') is False else href
        rel += (f'<div class="col-6 col-md-3"><a href="../{href}" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:{col[0]};color:{col[1]};">{E(tag)}</span>'
                f'<p class="sl-rel-card__name">{E(name)}</p><p class="sl-rel-card__desc">{E(desc)}</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>')
    h += f'<section class="sl-related"><div class="container"><p class="sl-related__title">Related Solutions</p><div class="row g-3">{rel}</div></div></section>\n'
    ct, cd = p['cta']
    h += f'''<section style="padding:4rem 0;background:#fff;"><div class="container"><div class="sl-cta-wrap">
  <h2 style="font-family:'Outfit',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:800;color:#fff;margin-bottom:.75rem;">{E(ct)}</h2>
  <p style="color:rgba(255,255,255,.6);font-size:.97rem;max-width:560px;margin:0 auto 2rem;">{E(cd)}</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
    <a href="../contact.html" class="sl-sol-btn sl-sol-btn--primary">Start a Conversation</a>
    <a href="../products.html" class="sl-sol-btn sl-sol-btn--dark-outline">Browse Products →</a>
  </div></div></div></section>
{FOOTER}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="../assets/js/nebulae-nav.js"></script>
<script src="../assets/js/nebulae-page.js"></script>
</body>
</html>
'''
    return h

for p in PAGES:
    out = ROOT + p['dir'] + '/' + p['slug'] + '.html'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(build(p))
    print('built', p['dir'] + '/' + p['slug'] + '.html')

import subprocess, sys as _s
subprocess.call([_s.executable, os.path.join(ROOT, "tools/apply_shared_assets.py")])
