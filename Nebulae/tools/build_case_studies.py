#!/usr/bin/env python3
"""Builds case-studies.html from tools/case_studies_data.json using blog.html as the shell (same header/footer/head).
Run from project root AFTER apply_index_header.py / apply_footer.py:  python3 tools/build_case_studies.py
PDFs go in assets/docs/case-studies/<slug>.pdf (see README.txt there)."""
import json, re, html, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=json.load(open(ROOT+'/tools/case_studies_data.json',encoding='utf-8')); e=html.escape
TAGC={'Industrial IoT':('79,70,229','#4f46e5'),'Smart City':('6,182,212','#0891b2'),'Railways':('217,119,6','#d97706'),'Energy':('5,150,105','#059669'),
      'Gateways':('37,99,235','#2563eb'),'Smart Devices':('124,58,237','#7c3aed'),'Networking':('13,148,136','#0d9488'),'Gaming & Arcade':('219,39,119','#db2777')}
ARR='<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg>'
def card(c):
    bg,fg=TAGC.get(c['tag'],('79,70,229','#4f46e5'))
    return f'''<div class="col-md-6 col-lg-4"><div class="pg-card">
<a href="{c['pdf']}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="{c['image']}" alt="{e(c['title'])}" class="pg-card__img" loading="lazy" width="860" height="700"/></a>
<div class="pg-card__body"><span class="pg-card__tag" style="background:rgba({bg},.1);color:{fg};">{e(c['tag'])}</span>
<h3 class="pg-card__title"><a href="{c['pdf']}" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;">{e(c['title'])}</a></h3>
<a href="{c['pdf']}" target="_blank" rel="noopener" class="pg-card__link" aria-label="Read case study (PDF): {e(c['title'])}">Read Case Study (PDF) {ARR}</a>
</div></div></div>'''
s=open(ROOT+'/blog.html',encoding='utf-8').read()
T='Case Studies | Nebulae IoT — Real-World IoT Deployments'
DESC='Real-world IoT case studies from Nebulae: industrial data acquisition, smart street lighting, waste management, railways monitoring, gateways and more.'
s=re.sub(r'<title>.*?</title>',f'<title>{T}</title>',s,count=1,flags=re.S)
s=s.replace('Blog | Nebulae IoT — IoT Platforms, Industry 4.0 &amp; Smart Metering',T)
s=re.sub(r'Articles from the Nebulae team on IoT platforms, Industry 4\.0 and smart manufacturing, and smart metering \(AMR / AMI\)\.',DESC,s)
s=s.replace('https://www.nebulae.io/blog.html','https://www.nebulae.io/case-studies.html')
s=re.sub(r'("name": ")Blog(", "item": "https://www\.nebulae\.io/)blog\.html',r'\1Case Studies\2case-studies.html',s)
i=s.index('<section class="pg-hero">'); j=s.index('<footer class="atl-footer">')
body=f'''<section class="pg-hero"><div class="pg-hero__grid"></div><div class="pg-hero__orb pg-hero__orb--1"></div><div class="pg-hero__orb pg-hero__orb--2"></div>
<div class="container" style="position:relative;z-index:2;"><nav class="pg-breadcrumb"><a href="index.html">Home</a><span>›</span><span style="color:rgba(255,255,255,.65);">Case Studies</span></nav>
<div class="pg-eyebrow">Case Studies</div><h1 class="pg-hero__title">IoT Solutions <span>in Action</span></h1>
<p class="pg-hero__desc">See how Nebulae hardware and software are deployed across industry, utilities, railways and smart cities. Each case study opens as a PDF.</p></div></section>
<section class="pg-section" id="case-studies"><div class="container"><div class="row g-4">
{chr(10).join(card(c) for c in D)}
</div></div></section>'''
s=s[:i]+body+s[j:]
open(ROOT+'/case-studies.html','w',encoding='utf-8').write(s); print('case-studies.html',len(D),'cards')
