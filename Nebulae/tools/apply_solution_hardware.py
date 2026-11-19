#!/usr/bin/env python3
"""Adds a 'Hardware for this solution' photo strip (team product photos) to each solutions/*.html, before the Related section.
Idempotent (marker comments). Run AFTER build_solutions.py and build_pages.py:  python3 tools/apply_solution_hardware.py"""
import json,os,re,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P={p['slug']:p for p in json.load(open(ROOT+'/tools/products_index.json',encoding='utf-8'))}
MAP={
 'smart-electric-meter':['nm0221i','nln0725is','nlg8520','nlg6770in'],
 'smart-gas-meter':['nln500a','nln500b','nlg6x40g-in','amr-gas'],
 'smart-water-meter':['nln500a','nln500b','nlg6x40g-in','amr-water'],
 'smart-street-light':['nln500a','nlg6x40g-in','nlg6x40h-in','nlg8140'],
 'transformer-monitoring':['nln500a','nlg6x40h-in','nlg8400','nln500b'],
}
S,E='<!-- HW-STRIP:start -->','<!-- HW-STRIP:end -->'
for sol,slugs in MAP.items():
    f=f'{ROOT}/solutions/{sol}.html'
    if not os.path.exists(f): continue
    s=open(f,encoding='utf-8').read()
    s=re.sub(re.escape(S)+r'.*?'+re.escape(E)+r'\n?','',s,flags=re.S)
    cards=''.join(f'<div class="col-6 col-lg-3"><a class="sl-hw-card" href="../{P[k]["file"]}"><span class="sl-hw-card__img"><img src="../{P[k]["image"]}" alt="{html.escape(P[k]["name"],quote=True)}" loading="lazy"></span><span class="sl-hw-card__model">{html.escape(P[k]["model"])}</span><span class="sl-hw-card__name">{html.escape(P[k]["name"])}</span></a></div>' for k in slugs if k in P)
    sec=f'{S}\n<section class="sl-section" id="hardware"><div class="container"><div class="sl-eyebrow-sm">Hardware</div><h2 class="sl-section-title">Nebulae Hardware for This Solution</h2><div class="row g-3 mt-1">{cards}</div></div></section>\n{E}\n'
    i=s.index('<section class="sl-related"')
    open(f,'w',encoding='utf-8').write(s[:i]+sec+s[i:]); print(sol,len(slugs))
