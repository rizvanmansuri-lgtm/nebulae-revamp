#!/usr/bin/env python3
"""Home 'Industries We Serve' section: all industries (same title + icon as industries.html), 6 per row, no Explore links / view-all button.
Run: python3 tools/apply_home_industries.py   (index.html, index1.html)"""
import re,os,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L=open(ROOT+'/industries.html',encoding='utf-8').read()
cards=re.findall(r'<a href="(industries/[a-z-]+\.html)" class="pg-ind-card">\s*<div class="pg-ind-card__icon" style="([^"]*)">(<svg.*?</svg>)</div>.*?<h3 class="pg-ind-card__title">(.*?)</h3>\s*<p class="pg-ind-card__desc">(.*?)</p>',L,re.S)
assert len(cards)==13,len(cards)
out=[]
for i,(href,st,svg,title,desc) in enumerate(cards):
    svg=svg.replace('width="20" height="20"','width="24" height="24"')
    out.append(f'      <div class="col-6 col-md-4 col-lg-2" data-anim="slide-up" data-anim-delay="{i%4+1}"><a href="{href}" class="nbl-ind-card"><div class="nbl-ind-card__icon" style="{st}">{svg}</div><h4 class="nbl-ind-card__title">{title}</h4><p class="nbl-ind-card__desc">{desc}</p></a></div>')
grid='    <div class="row g-3 justify-content-center nbl-ind-grid">\n'+'\n'.join(out)+'\n    </div>\n'
for f in ['index.html','index1.html']:
    p=os.path.join(ROOT,f)
    if not os.path.exists(p): continue
    s=open(p,encoding='utf-8').read()
    a=s.index('<section class="nbl-industries-section"'); b=s.index('</section>',a)
    sec=s[a:b]
    h=sec.index('    <div class="row g-3')
    new=sec[:h]+grid+'  </div>\n'
    s=s[:a]+new+s[b:]
    open(p,'w',encoding='utf-8').write(s); print(f,'ok')
