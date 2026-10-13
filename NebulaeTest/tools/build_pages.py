#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pages.py — generate every product detail page from tools/products/*.json

Run from the project root:   python3 tools/build_pages.py
Rebuilds ALL pages each run (so related-product links stay correct as more
products are added) and writes tools/products_index.json.

Inputs : tools/products/<slug>.json      (one per product; schema in tools/HANDOFF.md)
         tools/templates/header.html      (shared site header, verbatim from product-detail.html)
         tools/templates/footer.html      (shared site footer, verbatim from products.html)
Outputs: products/<slug>.html, products.html (listing), sitemap-products.xml, tools/products_index.json
"""
import os, sys, json, html, glob, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
SITE = 'https://www.nebulae.io'
OUTDIR = ROOT + 'products/'
IMG = '../assets/images/products/'
def up(path):
    return '../' + path[2:] if path.startswith('./') else path
e = html.escape

HEADER_ROOT = open(ROOT + 'tools/templates/header.html', encoding='utf-8').read()   # root-relative (used by products.html)
FOOTER_ROOT = open(ROOT + 'tools/templates/footer.html', encoding='utf-8').read()

def prefix_links(t, base='../'):
    """Make root-relative href/src/action values work from a sub-folder page (adds ../)."""
    def fix(m):
        attr, q, v = m.group(1), m.group(2), m.group(3)
        if v == '' or re.match(r'(?:[a-z][a-z0-9+.-]*:|#|//|/)', v, re.I): return m.group(0)
        if v.startswith('./'): v = v[2:]
        return f'{attr}={q}{base}{v}{q}'
    return re.sub(r'(?<![\w-])(href|src|action)=(["\'])([^"\']*)\2', fix, t)

HEADER = prefix_links(HEADER_ROOT)
FOOTER = prefix_links(FOOTER_ROOT)

S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"'
ICON = {
 'wifi':'<path d="M2 8a16 16 0 0 1 20 0"/><path d="M5 12a11 11 0 0 1 14 0"/><path d="M8.5 16a6 6 0 0 1 7 0"/><circle cx="12" cy="20" r="1.5" fill="currentColor"/>',
 'range':'<circle cx="12" cy="12" r="2"/><path d="M16.2 7.8a6 6 0 0 1 0 8.4M7.8 16.2a6 6 0 0 1 0-8.4M19 5a10 10 0 0 1 0 14M5 19A10 10 0 0 1 5 5"/>',
 'chip':'<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
 'grid':'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 'bolt':'<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 'lock':'<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'plug':'<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8z"/><path d="M12 18v4"/>',
 'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 'ruler':'<path d="M21.3 8.7 8.7 21.3a1 1 0 0 1-1.4 0L2.7 16.7a1 1 0 0 1 0-1.4L15.3 2.7a1 1 0 0 1 1.4 0l4.6 4.6a1 1 0 0 1 0 1.4z"/><path d="m7.5 10.5 2 2M10.5 7.5l2 2M13.5 4.5l2 2M4.5 13.5l2 2"/>',
 'download':'<path d="M12 3v12"/><path d="m8 11 4 4 4-4"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>',
 'building':'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
 'box':'<path d="M21 8 12 3 3 8v8l9 5 9-5V8z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 'leaf':'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.5-6.5"/>',
 'factory':'<path d="M2 20V8l6 4V8l6 4V4h4v16H2z"/><path d="M6 16h.01M10 16h.01M14 16h.01"/>',
 'meter':'<circle cx="12" cy="12" r="9"/><path d="m12 12 4-4"/><path d="M7 16h10"/>',
 'drop':'<path d="M12 2.7 5.6 9.1a9 9 0 1 0 12.8 0L12 2.7z"/>',
 'bulb':'<path d="M9 21h6M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
 'city':'<path d="M3 21V9l5-4 5 4v12M13 21V5l5-2 3 2v16"/><path d="M2 21h20"/>',
 'trash':'<path d="M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>',
 'sprout':'<path d="M12 22V12M12 12C12 12 7 9 7 4a5 5 0 0 1 10 0c0 5-5 8-5 8z"/>',
 'file':'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
 'mail':'<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="m22 6-10 7L2 6"/>',
 'phone':'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'link':'<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
 'send':'<path d="m22 2-11 11M22 2l-7 20-4-9-9-4 20-7z"/>',
 'check':'<path d="M20 6 9 17l-5-5"/>',
 'zoom':'<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>',
 'chev':'<path d="m9 18 6-6-6-6"/>',
 # added in batch 1
 'network':'<circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M12 7v5M12 12l-6 5M12 12l6 5"/>',
 'thermo':'<path d="M14 14.8V5a2 2 0 1 0-4 0v9.8a4 4 0 1 0 4 0z"/>',
 'home':'<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
 'gauge':'<path d="M12 14l4-4"/><path d="M3.3 19a10 10 0 1 1 17.4 0"/>',
 'server':'<rect x="2" y="3" width="20" height="7" rx="2"/><rect x="2" y="14" width="20" height="7" rx="2"/><path d="M6 6.5h.01M6 17.5h.01"/>',
 'battery':'<rect x="2" y="7" width="18" height="10" rx="2"/><path d="M22 11v2M6 10v4M10 10v4"/>',
 'cpu':'<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
 'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'truck':'<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
 'eye':'<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/>',
}
def svg(name, size=22):
    return f'<svg width="{size}" height="{size}" {S} aria-hidden="true" focusable="false">{ICON[name]}</svg>'

PROTO_LOGO = {'lora':'LoRaWAN.png','wisun':'Wi-SUN-Main-Logo.png','zigbee':'zigbee.png','wifi':'WiFi.png','ble':'Bluetooth.png'}
BADGE_CLS = {'wisun':' pd-gallery__badge--wisun','zigbee':' pd-gallery__badge--zigbee','wifi':' pd-gallery__badge--wifi','gsm':' pd-gallery__badge--gsm','ble':' pd-gallery__badge--ble'}

def load_products():
    P = {}
    for f in sorted(glob.glob(ROOT + 'tools/products/*.json')):
        j = json.load(open(f, encoding='utf-8'))
        P[j['slug']] = j
    return P

def rel_card(p):
    return (f'<div class="pd-rel-card"><div class="pd-rel-card__img"><img src="{IMG}{p["gallery"][0]["file"]}" alt="{e(p["full"], quote=True)}" loading="lazy" width="400" height="260"/></div>'
            f'<div class="pd-rel-card__body"><span class="pd-rel-card__proto" style="background:rgba(49,49,133,.1);color:#313185;">{e(p["type_label"])} · {e(p["proto_label"])}</span>'
            f'<div class="pd-rel-card__name">{e(p["model"])}</div>'
            f'<div class="pd-rel-card__desc">{e(p.get("tagline") or p["full"])}</div>'
            f'<a href="{p["slug"]}.html" class="pd-rel-card__link">View Details {svg("chev",14)}</a></div></div>')

def browse_card(p):
    logo = PROTO_LOGO.get(p['proto_key'])
    img = (f'<div class="pd-rel-card__img"><img src="../assets/images/SupportedTech/{logo}" alt="{e(p["proto_crumb"])}" loading="lazy" width="400" height="140"/></div>'
           if logo else f'<div class="pd-rel-card__img pd-rel-card__img--icon">{svg("grid",40)}</div>')
    return (f'<div class="pd-rel-card">{img}<div class="pd-rel-card__body"><span class="pd-rel-card__proto" style="background:rgba(49,49,133,.1);color:#313185;">{e(p["proto_crumb"])}</span>'
            f'<div class="pd-rel-card__name">{"All Nebulae Products" if p["proto_key"]=="other" else "All " + e(p["proto_crumb"]) + " Products"}</div>'
            f'<div class="pd-rel-card__desc">{"Browse the full range of Nebulae IoT products." if p["proto_key"]=="other" else "Browse the full range of Nebulae " + e(p["proto_crumb"]) + " modules, gateways and devices."}</div>'
            f'<a href="../products.html?proto={p["proto_key"]}" class="pd-rel-card__link">Browse Products {svg("chev",14)}</a></div></div>')

def build(p, ALL):
    M = p['model']; slug = p['slug']; url = f'{SITE}/products/{slug}.html'
    img_abs = f'{SITE}/assets/images/products/{p["gallery"][0]["file"]}'
    ld = {"@context":"https://schema.org","@type":"Product","name":p['full'],"description":p['desc'],
          "brand":{"@type":"Brand","name":"Nebulae"},"manufacturer":{"@type":"Organization","name":(p.get("maker") or {}).get("name","System Level Solutions"),"url":(p.get("maker") or {}).get("url","https://www.slscorp.com")},
          "sku":M,"mpn":M,"category":p['category'],"url":url,"image":img_abs}
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(M)} {e(p["title_name"])} — {e(p["proto_label"])} | Nebulae IoT Products</title>
  <meta name="description" content="{e(p["meta_desc"], quote=True)}"/>
  <meta name="robots" content="index, follow"/>
  <link rel="canonical" href="{url}"/>
  <link rel="icon" type="image/png" href="../favicon.png">
  <meta property="og:title" content="{e(M)} | Nebulae"/>
  <meta property="og:description" content="{e(p["meta_desc"], quote=True)}"/>
  <meta property="og:type" content="product"/>
  <meta property="og:url" content="{url}"/>
  <meta property="og:image" content="{img_abs}"/>
  <script type="application/ld+json">
  {json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Outfit:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
  <!-- Nebulae shared nav/footer styles -->
  <link rel="stylesheet" href="../assets/css/nebulae-nav.css">
  <!-- Product Detail page styles -->
  <link rel="stylesheet" href="../assets/css/product-detail.css">
</head>
<body data-pd-page="nln" data-pd-base="../">
'''
    crumb = f'''
<!-- BREADCRUMB -->
<div class="pd-top-bar">
  <div class="container">
    <nav class="pd-breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a><span aria-hidden="true">›</span>
      <a href="../products.html">Products</a><span aria-hidden="true">›</span>
      <a href="../products.html?proto={p["proto_key"]}">{e(p["proto_crumb"])}</a><span aria-hidden="true">›</span>
      <a href="../products.html?type={p["type_key"]}">{e(p["type_label"])}</a><span aria-hidden="true">›</span>
      <span class="pd-breadcrumb__current" aria-current="page">{e(M)}</span>
    </nav>
  </div>
</div>
'''
    G = p['gallery']; g0 = G[0]
    thumbs = ''
    if len(G) > 1:
        thumbs = '<div class="pd-gallery__thumbs" role="group" aria-label="Product images">' + ''.join(
            f'<button type="button" class="pd-gallery__thumb{" active" if i==0 else ""}" data-pd-thumb="{i}" data-full="{IMG}{g["file"]}" data-alt="{e(g["alt"], quote=True)}" aria-label="Show image: {e(g["label"], quote=True)}"><img src="{IMG}{g["file"]}" alt="{e(g["label"], quote=True)}" loading="{"eager" if i==0 else "lazy"}" width="72" height="72"/></button>'
            for i, g in enumerate(G)) + '</div>'
    qs = ''.join(f'<div class="pd-qs-item"><div class="pd-qs-icon">{svg(q["icon"],18)}</div><div><div class="pd-qs-label">{e(q["label"])}</div><div class="pd-qs-val">{e(q["value"])}</div></div></div>' for q in p['quick'])
    badges = ''.join(f'<span class="pd-cert-badge">{e(b)}</span>' for b in p['cert_badges'])
    primary = up(p['primary_doc']) if p['primary_doc'] else ''
    if primary:
        act_dl = f'<a href="{primary}" class="pd-action-btn" download>{svg("download",14)} Datasheet (PDF)</a>'
        spec_dl = f'<a href="{primary}" class="pd-x-btn" download>{svg("download",16)} Download PDF</a>'
    else:
        mail = f'mailto:sales@nebulae.io?subject=Datasheet%20request%20-%20{e(M)}'
        act_dl = f'<a href="{mail}" class="pd-action-btn">{svg("mail",14)} Request Datasheet</a>'
        spec_dl = f'<a href="{mail}" class="pd-x-btn">{svg("mail",16)} Request Datasheet</a>'
    stats = ''.join(f'<div class="pd-x-stat"><div class="pd-x-stat__num">{e(s["num"])}</div><div class="pd-x-stat__lbl">{e(s["label"])}</div></div>' for s in p['stats'])
    hero = f'''
<!-- HERO -->
<section class="pd-hero">
  <div class="container">
    <div class="row gx-lg-5 gy-4">
      <div class="col-lg-5">
        <div class="pd-gallery">
          <div class="pd-gallery__main">
            <img id="pdMainImg" src="{IMG}{g0["file"]}" alt="{e(g0["alt"], quote=True)}" width="700" height="700" loading="eager"/>
            <span class="pd-gallery__badge{BADGE_CLS.get(p["proto_key"],"")}">{e(p["badge"])}</span>
            <button type="button" class="pd-gallery__zoom" data-pd-zoom title="Zoom image" aria-label="Zoom image">{svg("zoom",16)}</button>
          </div>
          {thumbs}
        </div>
      </div>
      <div class="col-lg-7">
        <div class="pd-info">
          <div class="pd-info__eyebrow"><span class="pd-info__proto">{e(p["proto_label"])}</span><span class="pd-info__type">{e(p["type_label"])}</span></div>
          <h1 class="pd-info__name">{e(M)}</h1>
          <div class="pd-info__full">{e(p["full"])}</div>
          <div class="pd-info__meta"><div class="pd-info__certbadges">{badges}</div></div>
          <p class="pd-info__desc">{e(p["desc"])}</p>
          <div class="pd-quick-specs">{qs}</div>
          <div class="pd-cta-box">
            <div class="pd-cta-box__top">
              <div class="pd-cta-box__avail"><span class="pd-avail-dot"></span>Samples &amp; volume orders — contact sales</div>
              <div class="pd-cta-box__lead"><strong>Enquiries</strong>sales@nebulae.io</div>
            </div>
            <div class="pd-qty-row">
              <span class="pd-qty-label">Quantity:</span>
              <div class="pd-qty-ctrl">
                <button type="button" class="pd-qty-btn" data-pd-qty="-1" aria-label="Decrease quantity">−</button>
                <input id="pdQty" class="pd-qty-input" type="number" value="1" min="1" inputmode="numeric" aria-label="Quantity">
                <button type="button" class="pd-qty-btn" data-pd-qty="1" aria-label="Increase quantity">+</button>
              </div>
            </div>
            <div class="pd-cta-btns">
              <button type="button" class="pd-cta-btn pd-cta-btn--primary" data-pd-quote>{svg("send",16)} Request Quote</button>
              <a href="../contact.html?product={e(M)}&amp;type=sample" class="pd-cta-btn pd-cta-btn--outline">{svg("phone",16)} Request Sample</a>
            </div>
          </div>
          <div class="pd-action-row">
            {act_dl}
            <a href="mailto:sales@nebulae.io?subject=Enquiry%20-%20{e(M)}" class="pd-action-btn">{svg("mail",14)} Email Sales</a>
            <button type="button" class="pd-action-btn" data-pd-copy>{svg("link",14)} <span>Copy Link</span></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- AT A GLANCE -->
<section class="pd-x-stats" aria-label="{e(M)} at a glance">
  <div class="container"><div class="pd-x-stats__grid">{stats}</div></div>
</section>
'''
    why = ''.join(f'<div class="pd-x-why"><span class="pd-x-why__ic">{svg("check",13)}</span><div><div class="pd-x-why__t">{e(w["t"])}</div><div class="pd-x-why__d">{e(w["d"])}</div></div></div>' for w in p['why'])
    paras = ''.join(f'<p class="pd-x-p">{e(t)}</p>' for t in p['overview'])
    note = f'<p class="pd-x-note">{e(p["overview_note"])}</p>' if p.get('overview_note') else ''
    sc = p.get('showcase')
    showcase = ''
    if sc and sc.get('items'):
        figs = ''.join(f'<figure class="pd-x-fig"><div class="pd-x-fig__img"><img src="{IMG}{i["file"]}" alt="{e(i["alt"], quote=True)}" loading="lazy" width="600" height="400"/></div><figcaption>{e(i["cap"])}</figcaption></figure>' for i in sc['items'])
        showcase = f'''
      <div class="pd-x-card pd-x-card--tint pd-x-showcase">
        <h3 class="pd-x-h3">{e(sc["title"])}</h3>
        <p class="pd-x-p pd-x-p--sm">{e(sc["intro"])}</p>
        <div class="pd-x-figs pd-x-figs--{len(sc["items"])}">{figs}</div>
      </div>'''
    mk = p.get('maker')
    if mk:
        maker_html = (f'<div class="pd-x-maker"><img src="{IMG}{mk["logo"]}" alt="{e(mk["name"], quote=True)}" loading="lazy" width="120" height="55"/>'
                      f'<div><div class="pd-x-maker__t">{e(mk["line"])}</div><div class="pd-x-maker__d">{e(mk["sub"])} — <a href="{mk["url"]}" target="_blank" rel="noopener">{e(mk["url_label"])}</a></div></div></div>')
    else:
        maker_html = (f'<div class="pd-x-maker"><img src="{IMG}sls-logo.png" alt="System Level Solutions" loading="lazy" width="120" height="55"/>'
                      '<div><div class="pd-x-maker__t">Designed &amp; supported by System Level Solutions</div><div class="pd-x-maker__d">USA | India | UK — <a href="https://www.slscorp.com" target="_blank" rel="noopener">www.slscorp.com</a></div></div></div>')
    overview = f'''
    <div class="pd-tab-panel active" id="pd-tab-overview" role="tabpanel" aria-labelledby="pd-tabbtn-overview">
      <div class="row gx-lg-5 gy-4 align-items-start">
        <div class="col-lg-7">
          <h2 class="pd-x-h">About {e(M)}</h2>
          {paras}
          {note}
        </div>
        <div class="col-lg-5">
          <h3 class="pd-x-h3">Why Engineers Choose {e(M)}</h3>
          <div class="pd-x-whylist">{why}</div>
          {maker_html}
        </div>
      </div>{showcase}
    </div>'''
    rows = ''
    for g in p['specs']:
        rows += f'<tr class="pd-specs-group"><td colspan="2">{e(g["group"])}</td></tr>'
        for k, v in g['rows']:
            rows += f'<tr><td>{e(k)}</td><td>{e(v)}</td></tr>'
    specs = f'''
    <div class="pd-tab-panel" id="pd-tab-specs" role="tabpanel" aria-labelledby="pd-tabbtn-specs" hidden>
      <div class="row gx-lg-5 gy-4">
        <div class="col-lg-8">
          <h2 class="pd-x-h">Technical Specifications</h2>
          <div class="pd-specs-wrap"><table class="pd-specs-table">
            <thead><tr><th scope="col">Parameter</th><th scope="col">Value</th></tr></thead>
            <tbody>{rows}</tbody>
          </table></div>
          <p class="pd-x-note">{e(p["spec_note"])}</p>
        </div>
        <div class="col-lg-4">
          <div class="pd-x-card pd-x-card--brand">
            <h3 class="pd-x-h3 pd-x-h3--light">{"Need the full datasheet?" if primary else "Datasheet on request"}</h3>
            <p class="pd-x-p pd-x-p--sm pd-x-p--light">{"Download the " + e(M) + " product document for the complete feature list and specifications." if primary else "Contact our team for the complete " + e(M) + " datasheet."}</p>
            {spec_dl}
          </div>
        </div>
      </div>
    </div>'''
    feats = ''.join(f'<div class="pd-feat-card"><div class="pd-feat-icon" style="background:{f["bg"]};color:{f["color"]};">{svg(f["icon"],22)}</div><div><h3 class="pd-feat-title">{e(f["t"])}</h3><div class="pd-feat-desc">{e(f["d"])}</div></div></div>' for f in p['features'])
    features = f'''
    <div class="pd-tab-panel" id="pd-tab-features" role="tabpanel" aria-labelledby="pd-tabbtn-features" hidden>
      <h2 class="pd-x-h">Key Features</h2>
      <div class="pd-features-grid">{feats}</div>
    </div>'''
    colors = [('rgba(37,99,235,.1)','#2563eb'),('rgba(16,185,129,.1)','#059669'),('rgba(251,191,36,.12)','#d97706'),('rgba(124,58,237,.1)','#7c3aed')]
    docs_html = ''.join(
        f'<a href="{up(d["path"])}" class="pd-doc-card" download><div class="pd-doc-icon" style="background:{colors[i%4][0]};color:{colors[i%4][1]};">{svg("file",22)}</div>'
        f'<div><div class="pd-doc-name">{e(d["name"])}</div><div class="pd-doc-size">{e(d["sub"])}</div></div><span class="pd-doc-arrow">{svg("download",16)}</span></a>'
        for i, d in enumerate(p['docs']))
    docs = f'''
    <div class="pd-tab-panel" id="pd-tab-docs" role="tabpanel" aria-labelledby="pd-tabbtn-docs" hidden>
      <h2 class="pd-x-h">Documents &amp; Resources</h2>
      <div class="pd-docs-grid">{docs_html}</div>
      <p class="pd-x-note">Need schematics, certification reports or integration support? Contact <a href="mailto:sales@nebulae.io">sales@nebulae.io</a>.</p>
    </div>'''
    apps = ''.join(f'<div class="pd-app-card"><div class="pd-app-icon">{svg(a["icon"],24)}</div><h3 class="pd-app-title">{e(a["t"])}</h3><div class="pd-app-desc">{e(a["d"])}</div></div>' for a in p['apps'])
    applications = f'''
    <div class="pd-tab-panel" id="pd-tab-applications" role="tabpanel" aria-labelledby="pd-tabbtn-applications" hidden>
      <h2 class="pd-x-h">Ideal Applications</h2>
      <div class="pd-app-grid">{apps}</div>
    </div>'''
    contact_co = ('System Level Solutions · USA | India | UK<br>info@slscorp.com · <a href="https://www.slscorp.com" target="_blank" rel="noopener">www.slscorp.com</a>'
                  if not p.get('maker') else e(p['maker']['name']) + ' · ' + (e(p['maker'].get('contact_note','')) or 'Sales enquiries via sales@nebulae.io'))
    prow = ''.join(f'<tr><td>{e(a)}</td><td>{e(b)}</td></tr>' for a, b in p['part_rows'])
    ordering = f'''
    <div class="pd-tab-panel" id="pd-tab-ordering" role="tabpanel" aria-labelledby="pd-tabbtn-ordering" hidden>
      <div class="row gx-lg-5 gy-4">
        <div class="col-lg-6">
          <h2 class="pd-x-h">Ordering Information</h2>
          <div class="pd-specs-wrap"><table class="pd-specs-table">
            <thead><tr><th scope="col">Part Number</th><th scope="col">Description</th></tr></thead>
            <tbody>{prow}</tbody>
          </table></div>
          <p class="pd-x-note">Pricing, lead time and minimum order quantity are provided on request.</p>
        </div>
        <div class="col-lg-6">
          <div class="pd-x-card pd-x-card--brand">
            <h3 class="pd-x-h3 pd-x-h3--light">Get a Quote</h3>
            <p class="pd-x-p pd-x-p--sm pd-x-p--light">Contact our team for pricing, samples and technical support for {e(M)}.</p>
            <button type="button" class="pd-x-btn pd-x-btn--block" data-pd-quote>Request a Quote</button>
          </div>
          <div class="pd-x-card pd-x-card--tint pd-x-contact">
            <h3 class="pd-x-h3">Contact</h3>
            <ul class="pd-x-contact__list">
              <li>{svg("mail",16)}<a href="mailto:sales@nebulae.io">sales@nebulae.io</a></li>
              <li>{svg("link",16)}<a href="https://www.nebulae.io" target="_blank" rel="noopener">www.nebulae.io</a></li>
              <li>{svg("phone",16)}<a href="tel:+9102692232501">+91-2692-232 501 / 502</a></li>
            </ul>
            <div class="pd-x-contact__co">{contact_co}</div>
          </div>
        </div>
      </div>
    </div>'''
    tabnames = [('overview','Overview'),('specs','Specifications'),('features','Features'),('docs','Documents'),('applications','Applications'),('ordering','Ordering')]
    tabbtns = '\n'.join(
        f'      <button type="button" class="pd-tab-btn{" active" if i==0 else ""}" role="tab" id="pd-tabbtn-{k}" aria-controls="pd-tab-{k}" aria-selected="{"true" if i==0 else "false"}"{"" if i==0 else " tabindex=\"-1\""} data-tab="{k}">{n}</button>'
        for i, (k, n) in enumerate(tabnames))
    tabs = f'''
<!-- TABS SECTION -->
<div class="pd-tabs-section" id="pd-tabs">
  <div class="container">
    <div class="pd-tabs-bar" role="tablist" aria-label="{e(M)} details">
{tabbtns}
    </div>
{overview}
{specs}
{features}
{docs}
{applications}
{ordering}
  </div>
</div>
'''
    rel = [ALL[s] for s in p.get('related', []) if s in ALL and s != slug][:2]
    related = f'''
<!-- RELATED PRODUCTS -->
<section class="pd-related">
  <div class="container">
    <div class="atl-eyebrow" style="margin-bottom:.5rem;">You May Also Like</div>
    <h2 class="atl-section-h3" style="margin-bottom:1.5rem;">Related Products</h2>
    <div class="pd-related__grid">
      {"".join(rel_card(r) for r in rel)}
      {browse_card(p)}
    </div>
  </div>
</section>
'''
    lightbox = '''
<!-- LIGHTBOX -->
<div class="pd-lightbox" id="pdLightbox" role="dialog" aria-modal="true" aria-label="Product image preview">
  <button type="button" class="pd-lightbox__close" data-pd-lb-close aria-label="Close preview">&times;</button>
  <img id="pdLightboxImg" alt="">
</div>
'''
    scripts = '''
<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<!-- Nebulae shared nav/footer JS -->
<script src="../assets/js/nebulae-nav.js"></script>
<!-- Product Detail page JS -->
<script src="../assets/js/product-detail.js"></script>
</body>
</html>
'''
    out = head + '\n' + HEADER + '\n' + crumb + hero + tabs + related + '\n' + FOOTER + '\n' + lightbox + scripts
    os.makedirs(OUTDIR, exist_ok=True)
    open(OUTDIR + slug + '.html', 'w', encoding='utf-8').write(out)
    return len(out)


# ---------------------------------------------------------------- listing page (products.html)
PROTO_ORDER = ['lora', 'wisun', 'zigbee', 'wifi', 'gsm', 'som', 'other']
PROTO_NAME = {'lora': 'LoRa / LoRaWAN', 'wisun': 'Wi-SUN', 'zigbee': 'Zigbee', 'wifi': 'Wi-Fi', 'gsm': 'GSM / Cellular', 'som': 'SoM', 'other': 'Other'}
TYPE_ORDER = ['module', 'node', 'gateway', 'concentrator', 'filter', 'evk']
TYPE_NAME = {'module': 'Modules', 'node': 'Nodes', 'gateway': 'Gateways', 'concentrator': 'Concentrators', 'filter': 'Filters', 'evk': 'EVKs'}

def build_listing(ALL):
    items = sorted(ALL.values(), key=lambda p: (PROTO_ORDER.index(p['proto_key']) if p['proto_key'] in PROTO_ORDER else 99,
                                                TYPE_ORDER.index(p['type_key']) if p['type_key'] in TYPE_ORDER else 99, p['model']))
    n = len(items)
    pc = {k: sum(1 for p in items if p['proto_key'] == k) for k in PROTO_ORDER}
    tc = {k: sum(1 for p in items if p['type_key'] == k) for k in TYPE_ORDER}
    arrow = svg('chev', 14)
    cards = []
    for p in items:
        specs = ''.join(f'<li><b>{e(q["label"])}:</b><span>{e(q["value"])}</span></li>' for q in p['quick'][:3])
        search = ' '.join([p['model'], p['full'], p.get('tagline', ''), p['proto_label'], p['proto_crumb'], p['type_label'], p['type_key'], p['category']] + p['cert_badges']).lower()
        href = f'products/{p["slug"]}.html'
        cards.append(f'''
      <article class="pl-card" data-proto="{p["proto_key"]}" data-type="{p["type_key"]}" data-search="{e(search, quote=True)}">
        <a class="pl-card__media" href="{href}" tabindex="-1" aria-hidden="true"><img src="assets/images/products/{p["gallery"][0]["file"]}" alt="" loading="lazy" width="400" height="300"/></a>
        <div class="pl-card__body">
          <div class="pl-card__tags"><span class="pl-tag">{e(p["proto_label"])}</span><span class="pl-tag pl-tag--type">{e(p["type_label"])}</span></div>
          <h3 class="pl-card__name"><a href="{href}">{e(p["model"])}</a></h3>
          <div class="pl-card__sub">{e(p["full"])}</div>
          <p class="pl-card__desc">{e(p.get("tagline") or p["desc"])}</p>
          <ul class="pl-card__specs">{specs}</ul>
          <a class="pl-card__cta" href="{href}" aria-label="View details of {e(p["model"], quote=True)}">View details {arrow}</a>
        </div>
      </article>''')
    pchips = f'<button type="button" class="pl-chip" data-group="proto" data-value="all" aria-pressed="true">All <i>{n}</i></button>' + ''.join(
        f'<button type="button" class="pl-chip" data-group="proto" data-value="{k}" aria-pressed="false">{PROTO_NAME[k]} <i>{pc[k]}</i></button>' for k in PROTO_ORDER if pc[k])
    tchips = f'<button type="button" class="pl-chip" data-group="type" data-value="all" aria-pressed="true">All types <i>{n}</i></button>' + ''.join(
        f'<button type="button" class="pl-chip" data-group="type" data-value="{k}" aria-pressed="false">{TYPE_NAME[k]} <i>{tc[k]}</i></button>' for k in TYPE_ORDER if tc[k])
    fam = sum(1 for k in PROTO_ORDER if pc[k] and k not in ('other', 'som'))
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Nebulae IoT Products", "numberOfItems": n,
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/products/{p['slug']}.html", "name": p['full']} for i, p in enumerate(items)]}
    desc = 'Nebulae IoT products — LoRaWAN, Wi-SUN, Zigbee, Wi-Fi and cellular modules, nodes, gateways, concentrators, filters and evaluation kits from System Level Solutions.'
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Products — IoT Modules, Gateways, Nodes &amp; Concentrators | Nebulae</title>
  <meta name="description" content="{e(desc, quote=True)}"/>
  <meta name="robots" content="index, follow"/>
  <link rel="canonical" href="{SITE}/products.html"/>
  <link rel="icon" type="image/png" href="./favicon.png">
  <meta property="og:title" content="Nebulae IoT Products"/>
  <meta property="og:description" content="{e(desc, quote=True)}"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="{SITE}/products.html"/>
  <script type="application/ld+json">
  {json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Outfit:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="./assets/css/nebulae-nav.css">
  <link rel="stylesheet" href="./assets/css/products-listing.css">
</head>
<body data-pl-page>
{HEADER_ROOT}

<main>
<section class="pl-hero">
  <div class="container">
    <div class="pl-hero__eyebrow">Products</div>
    <h1 class="pl-hero__title">Nebulae IoT Products</h1>
    <p class="pl-hero__sub">Modules, nodes, gateways, concentrators, filters and evaluation kits for LoRaWAN, Wi-SUN, Zigbee, Wi-Fi and cellular networks — designed and supported by System Level Solutions.</p>
    <div class="pl-hero__stats">
      <div class="pl-hero__stat"><b>{n}</b><span>Products</span></div>
      <div class="pl-hero__stat"><b>{fam}</b><span>Wireless families</span></div>
      <div class="pl-hero__stat"><b>{sum(1 for k in TYPE_ORDER if tc[k])}</b><span>Product types</span></div>
    </div>
  </div>
</section>

<section class="pl-tools" aria-label="Filter products">
  <div class="container">
    <div class="pl-search">
      <svg width="18" height="18" {S} aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
      <input id="plSearch" type="search" placeholder="Search by model, protocol or feature…" aria-label="Search products" autocomplete="off">
    </div>
    <div class="pl-fgroup" role="group" aria-label="Filter by protocol"><span class="pl-fgroup__label">Protocol</span>{pchips}</div>
    <div class="pl-fgroup" role="group" aria-label="Filter by product type"><span class="pl-fgroup__label">Type</span>{tchips}</div>
  </div>
</section>

<section class="pl-results" aria-label="Product results">
  <div class="container">
    <div class="pl-bar">
      <div class="pl-count" id="plCount" aria-live="polite">Showing <b>{n}</b> of <b>{n}</b> products</div>
      <button type="button" class="pl-clear" id="plClear" hidden>Clear all filters</button>
    </div>
    <div class="pl-grid" id="plGrid">{"".join(cards)}
    </div>
    <div class="pl-empty" id="plEmpty" hidden>
      <h2>No products found</h2>
      <p id="plEmptyMsg">No products match your current filters.</p>
      <button type="button" class="pl-btn" id="plEmptyClear">View all products</button>
      <a class="pl-btn pl-btn--ghost" href="./contact.html">Contact sales</a>
    </div>
  </div>
</section>

<section class="pl-cta">
  <div class="container pl-cta__in">
    <div><h2>Need help choosing the right product?</h2><p>Talk to our team about samples, volume pricing and integration support — sales@nebulae.io</p></div>
    <a class="pl-btn" href="./contact.html">Contact Sales</a>
  </div>
</section>
</main>

{FOOTER_ROOT}

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="./assets/js/nebulae-nav.js"></script>
<script src="./assets/js/products-listing.js"></script>
</body>
</html>
'''
    open(ROOT + 'products.html', 'w', encoding='utf-8').write(page)
    return n

def build_sitemap(ALL):
    urls = [f'{SITE}/products.html'] + [f'{SITE}/products/{s}.html' for s in sorted(ALL)]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{"0.9" if u.endswith("products.html") else "0.8"}</priority></url>\n' for u in urls) + '</urlset>\n'
    open(ROOT + 'sitemap-products.xml', 'w', encoding='utf-8').write(x)

def validate(p):
    miss = []
    for f in [g['file'] for g in p['gallery']] + [i['file'] for i in (p.get('showcase') or {}).get('items', [])] + ['sls-logo.png']:
        if not os.path.exists(ROOT + 'assets/images/products/' + f): miss.append('image:' + f)
    for d in p['docs']:
        if not os.path.exists(ROOT + d['path'].replace('./', '', 1)): miss.append('doc:' + d['path'])
    for k in ('slug','model','full','title_name','type_key','type_label','proto_key','proto_crumb','proto_label','badge','category','meta_desc','desc','cert_badges','gallery','quick','stats','overview','why','specs','spec_note','features','apps','part_rows','docs'):
        if k not in p: miss.append('field:' + k)
    for q in p.get('quick', []) + p.get('apps', []) + p.get('features', []):
        if q.get('icon') not in ICON: miss.append('icon:' + str(q.get('icon')))
    return miss

if __name__ == '__main__':
    ALL = load_products()
    bad = False
    for s, p in ALL.items():
        m = validate(p)
        if m: print('!!', s, m); bad = True
    if bad: sys.exit('fix the above, then rebuild')
    index = []
    for s, p in ALL.items():
        n = build(p, ALL)
        index.append(dict(slug=s, file=f'products/{s}.html', model=p['model'], name=p['full'], type_key=p['type_key'], type_label=p['type_label'],
                          proto_key=p['proto_key'], proto_label=p['proto_label'], image='assets/images/products/' + p['gallery'][0]['file'], tagline=p.get('tagline', '')))
        print(f'built {s}.html ({n:,} bytes)')
    build_listing(ALL); build_sitemap(ALL)
    json.dump(index, open(ROOT + 'tools/products_index.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(len(index), 'products')
