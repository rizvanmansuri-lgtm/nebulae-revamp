#!/usr/bin/env python3
"""Rebuild the site footer on every page (listing pages only + social icons + address).
Run from project root: python3 tools/apply_footer.py   (idempotent)"""
import re, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOC = [
 ('Facebook','https://www.facebook.com/nebulae.io','<path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.7v3h2.7V21z"/>'),
 ('X (Twitter)','https://twitter.com/nebulae_io','<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>'),
 ('Instagram','https://www.instagram.com/system_level_solutions/','<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.1"/>'),
 ('LinkedIn','https://www.linkedin.com/showcase/nebulae-io/?viewAsMember=true','<path d="M6.9 8.8H3.6V20h3.3zM5.3 3.5a1.9 1.9 0 100 3.8 1.9 1.9 0 000-3.8zM20.4 20v-6.2c0-3-1.6-4.4-3.8-4.4-1.7 0-2.5.9-2.9 1.6V8.8h-3.3V20h3.3v-6.1c0-.3 0-.6.1-.8.3-.6.8-1.2 1.8-1.2 1.2 0 1.7.9 1.7 2.3V20z"/>'),
]
def footer(p):
    soc=''.join(f'<a class="atl-footer__social" href="{u}" target="_blank" rel="noopener noreferrer" aria-label="{n}" title="{n}"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{d}</svg></a>' for n,u,d in SOC)
    return f'''<footer class="atl-footer">
  <div class="container">
    <div class="row g-4 align-items-start">
      <!-- Brand -->
      <div class="col-12 col-md-4">
        <div class="d-flex align-items-center gap-2 mb-3">
          <img loading="lazy" src="{p}assets/images/LogoWhite.png" alt="Nebulae" class="atl-footer__logo-img atl-footer__logo-color" width="205" height="69">
        </div>
        <p class="atl-footer__desc">End-to-end IoT solutions provider — from embedded hardware design and wireless modules to cloud integration and smart utility deployments across India and beyond.</p>
        <div class="atl-footer__socials">{soc}</div>
      </div>
      <!-- Company -->
      <div class="col-6 col-md-2">
        <p class="atl-footer__heading">Company</p>
        <ul class="atl-footer__list">
          <li><a href="{p}index.html">Home</a></li>
          <li><a href="{p}about.html">About Us</a></li>
          <li><a href="{p}news-events.html">News &amp; Events</a></li>
          <li><a href="{p}blog.html">Blogs</a></li>
          <li><a href="{p}case-studies.html">Case Studies</a></li>
          <li><a href="{p}faq.html">FAQ</a></li>
          <li><a href="{p}contact.html">Contact Us</a></li>
        </ul>
      </div>
      <!-- Quick Links (listing pages only) -->
      <div class="col-6 col-md-3">
        <p class="atl-footer__heading">Quick Links</p>
        <ul class="atl-footer__list">
          <li><a href="{p}products.html">Products</a></li>
          <li><a href="{p}services.html">Services</a></li>
          <li><a href="{p}solutions.html">Solutions</a></li>
          <li><a href="{p}industries.html">Industries</a></li>
          <li><a href="{p}resources.html">Resources</a></li>
        </ul>
      </div>
      <!-- Address -->
      <div class="col-12 col-md-3">
        <p class="atl-footer__heading">Address</p>
        <ul class="atl-footer__list">
          <li>Plot#32, Zone-D/4, Phase-1<br>GIDC Estate, V.U.Nagar - 388121<br>Gujarat, India</li>
          <li><a href="mailto:sales@nebulae.io">sales@nebulae.io</a></li>
          <li><a href="tel:+919898042339">+91 9898042339</a></li>
        </ul>
      </div>
    </div>
    <div class="atl-footer__bottom">
      <span>© 2026 Nebulae. All rights reserved.</span>
    </div>
  </div>
</footer>'''
def span(s):
    i=s.find('<footer class="atl-footer">')
    if i<0: return None
    d=0
    for m in re.finditer(r'<footer\b|</footer>',s[i:]):
        d+= 1 if m.group(0)!='</footer>' else -1
        if d==0: return i,i+m.end()
    j=s.find('</footer>',i)          # unbalanced stray <footer> wrapper: cut to first closer
    if j>0: return i,j+len('</footer>')
n=0
for f in glob.glob(ROOT+'/**/*.html',recursive=True):
    rel=os.path.relpath(f,ROOT)
    if rel.startswith('tools/'): continue
    s=open(f,encoding='utf-8').read(); sp=span(s)
    p='../'*rel.count(os.sep) or './'
    if not sp:
        if rel in ('product-detail.html','doc-detail.html'):   # dynamic pages had no footer
            k=s.find('<script src="https://cdn.jsdelivr.net/npm/bootstrap')
            if k<0: continue
            s=s[:k]+footer(p)+'\n'+s[k:]
        else: continue
    else:
        s=s[:sp[0]]+footer(p)+s[sp[1]:]
    open(f,'w',encoding='utf-8').write(s); n+=1
open(ROOT+'/tools/templates/footer.html','w',encoding='utf-8').write(footer('./'))
print('footers rebuilt:',n)
