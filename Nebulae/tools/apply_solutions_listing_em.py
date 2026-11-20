#!/usr/bin/env python3
"""Adds Energy Management card + jump pill to solutions.html and sitemap entry. Idempotent. (solutions.html overview cards are not generated.)"""
import re,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=ROOT+'/solutions.html'; s=open(p,encoding='utf-8').read()
if 'solutions/energy-management.html" class="sl-overview-card"' not in s:
    a=s.index('<a href="solutions/transformer-monitoring.html" class="sl-overview-card">'); b=s.index('</a>\n      </div>',a)+len('</a>\n      </div>')
    card='''
      <div class="col-sm-6 col-lg-4" data-sl="up" data-sl-d="6">
        <a href="solutions/energy-management.html" class="sl-overview-card">
          <div class="sl-overview-card__img">
            <img src="assets/images/solutions/em-plant.webp" alt="Energy Management Solution" loading="lazy" width="1280" height="480"/>
            <div class="sl-overview-card__overlay"></div>
          </div>
          <div class="sl-overview-card__body">
            <div class="sl-overview-card__title">Energy Management</div>
            <div class="sl-overview-card__desc">Cloud platform to measure, monitor, analyze and optimize energy, gas, water and air consumption.</div>
            <div class="sl-overview-card__arrow">Learn More <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg></div>
          </div>
        </a>
      </div>'''
    s=s[:b]+card+s[b:]
    s=s.replace('🔌 Transformer Monitoring</a></div>','🔌 Transformer Monitoring</a><a class="sl-jump-pill" href="solutions/energy-management.html">📊 Energy Management</a></div>',1)
    open(p,'w',encoding='utf-8').write(s); print('listing updated')
sm=ROOT+'/sitemap.xml'; x=open(sm).read()
if 'solutions/energy-management.html' not in x:
    x=x.replace('</urlset>','  <url><loc>https://www.nebulae.io/solutions/energy-management.html</loc></url>\n</urlset>'); open(sm,'w').write(x); print('sitemap')
