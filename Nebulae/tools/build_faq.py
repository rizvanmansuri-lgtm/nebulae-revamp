#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_faq.py — generates faq.html from tools/faq_data.py. Header/footer/drawer/shared assets come from the industries.html shell
(same as every other page). Usage:  python3 tools/build_faq.py   (then python3 tools/apply_index_header.py if the menu changed)"""
import os, re, sys, html, json, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
sys.path.insert(0, os.path.dirname(__file__))
from faq_data import GENERAL, TECH
E = lambda s: html.escape(str(s), quote=True)
T = open(ROOT + 'industries.html', encoding='utf-8').read()
TITLE = 'FAQ | Nebulae IoT — Frequently Asked Questions'
DESC = 'Answers to common questions about Nebulae IoT: devices, gateways, SDKs, middleware, security, connectivity, licensing and support.'

qa_all = []; counter = [0]
def plain(ans): return ' '.join(b if isinstance(b, str) else ' '.join(b[1]) for b in ans)
def answer_html(ans):
    o = ''
    for b in ans:
        if isinstance(b, str): o += f'<p>{E(b)}</p>'
        else: o += f'<{b[0]}>' + ''.join(f'<li>{E(x)}</li>' for x in b[1]) + f'</{b[0]}>'
    return o
def item(q, ans):
    counter[0] += 1; n = counter[0]; qa_all.append((q, plain(ans)))
    return f'<details class="fq-item" id="q{n}"><summary>{E(q)}</summary><div class="fq-a">{answer_html(ans)}</div></details>'

general = ''.join(item(q, a) for q, a in GENERAL)
tech = ''
for gi, (gname, items) in enumerate(TECH):
    tech += f'<div class="fq-group" data-group><h3 class="fq-group__t" id="g{gi+1}">{E(gname)}<span class="fq-group__n">{len(items)}</span></h3>' + ''.join(item(q, a) for q, a in items) + '</div>'
chips = ''.join(f'<a class="fq-chip" href="#g{i+1}">{E(g)}</a>' for i, (g, _) in enumerate(TECH))
total = len(qa_all)

body = f'''<section class="pg-hero ">
  <div class="pg-hero__grid"></div>
  <div class="pg-hero__orb pg-hero__orb--1"></div>
  <div class="pg-hero__orb pg-hero__orb--2"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav class="pg-breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>›</span><span style="color:rgba(255,255,255,.65);">FAQ</span></nav>
    <div class="pg-eyebrow">Help · Support</div>
    <h1 class="pg-hero__title">Frequently Asked <span>Questions</span></h1>
    <p class="pg-hero__desc">Answers about Nebulae devices, gateways, SDKs and middleware. Can&rsquo;t find what you need? Our team is happy to help.</p>
  </div>
</section>
<section class="pg-section" id="faqApp">
  <div class="container fq-wrap">
    <div class="fq-bar">
      <div class="fq-tabs" role="tablist" aria-label="FAQ categories">
        <button class="fq-tab is-on" role="tab" id="tab-general" aria-selected="true" aria-controls="panel-general" data-tab="general">General <span>{len(GENERAL)}</span></button>
        <button class="fq-tab" role="tab" id="tab-technical" aria-selected="false" aria-controls="panel-technical" data-tab="technical" tabindex="-1">Technical <span>{sum(len(i) for _, i in TECH)}</span></button>
      </div>
      <div class="fq-search"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
        <input id="fqSearch" type="search" placeholder="Search {total} questions…" aria-label="Search the FAQ" autocomplete="off"></div>
    </div>
    <p class="fq-status" id="fqStatus" role="status" aria-live="polite"></p>
    <div class="fq-panel" id="panel-general" role="tabpanel" aria-labelledby="tab-general">{general}</div>
    <div class="fq-panel" id="panel-technical" role="tabpanel" aria-labelledby="tab-technical" hidden>
      <div class="fq-chips" aria-label="Jump to a section">{chips}</div>{tech}</div>
    <div class="fq-empty" id="fqEmpty" hidden><h3>No questions match your search</h3><p>Try fewer or different words, or <a href="contact.html">contact our team</a>.</p></div>
    <div class="fq-cta"><div><h2>Still have a question?</h2><p>Write to <a href="mailto:support@nebulae.io">support@nebulae.io</a> or send us a message and we&rsquo;ll get back to you.</p></div><a class="pg-btn-primary" href="contact.html">Contact Us</a></div>
  </div>
</section>
'''
ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa_all]}
a = T.find('<section class="pg-hero '); b = T.find('<footer class="atl-footer">')
assert a > 0 and b > a
out = T[:a] + body + T[b:]
out = re.sub(r'<title>[^<]*</title>', f'<title>{E(TITLE)}</title>', out, 1)
out = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + E(DESC), out, 1)
out = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\g<1>https://www.nebulae.io/faq.html', out, 1)
out = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + E(TITLE), out, 1)
out = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + E(DESC), out, 1)
out = re.sub(r'(<meta property="og:url" content=")[^"]*', r'\g<1>https://www.nebulae.io/faq.html', out, 1)
out = out.replace('</head>', '<link rel="stylesheet" href="./assets/css/faq.css">\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace('</', '<\\/') + '</script>\n</head>', 1)
out = out.replace('</body>', '<script src="./assets/js/faq.js"></script>\n</body>', 1)
open(ROOT + 'faq.html', 'w', encoding='utf-8').write(out)
print('built faq.html —', total, 'questions')
subprocess.call([sys.executable, os.path.join(ROOT, 'tools/apply_shared_assets.py')])
