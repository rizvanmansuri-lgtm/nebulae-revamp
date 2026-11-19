#!/usr/bin/env python3
"""Home hero tech cards: proper icons (same as the Products-menu icon per protocol); cards stay clickable.
Replaces the logo version from apply_hero_logos.py. Idempotent. Run after apply_hero_logos.py."""
import re,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H=open(ROOT+'/index.html',encoding='utf-8').read()
nav=H[H.index('<header'):H.index('</header>')]
ico={}
for m in re.finditer(r'proto=(\w+)[^>]*class="atl-prod-card[^"]*">\s*<span class="atl-prod-card__icon">(<svg.*?</svg>)',nav,re.S):
    ico.setdefault(m.group(1),m.group(2))
ico['ble']='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="atl-ico-stroke"><path d="m6.5 6.5 11 11L12 23V1l5.5 5.5-11 11"/></svg>'
pat=re.compile(r'(<a class="nbl-mini-card nbl-mini-card--(\w+)"[^>]*>)<span class="nbl-mini-card__logo">.*?</span>',re.S)
def rep(m):
    svg=ico.get(m.group(2))
    if not svg: return m.group(0)
    svg=re.sub(r'width="\d+" height="\d+"','width="22" height="22"',svg,count=1)
    return f'{m.group(1)}<div class="nbl-mini-card__icon">{svg}</div>'
for f in ['index.html','index1.html','index-new.html']:
    p=os.path.join(ROOT,f)
    if os.path.exists(p):
        s=open(p,encoding='utf-8').read(); s2,n=pat.subn(rep,s); open(p,'w',encoding='utf-8').write(s2); print(f,n)
