#!/usr/bin/env python3
"""One unique, canonical icon per industry on industries.html (the home 'Industries' section copies from there via apply_home_industries.py).
Idempotent. Run:  python3 tools/apply_industry_icons.py && python3 tools/apply_home_industries.py"""
import re,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S='width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"'
I={
'home-security-automation':'<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/>',
'sos-devices':'<path d="M10.3 3.9 1.8 18a2 2 0 001.7 3h17a2 2 0 001.7-3L13.7 3.9a2 2 0 00-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
'smart-city-solutions':'<path d="M3 21V9l5-4 5 4v12M13 21V5l5-2 3 2v16"/><path d="M2 21h20"/>',
'building-management-system':'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
'smart-agriculture':'<path d="M12 22V12M12 12C12 12 7 9 7 4a5 5 0 0110 0c0 5-5 8-5 8z"/>',
'farm-animal-management':'<circle cx="5" cy="11" r="2"/><circle cx="9" cy="5.5" r="2"/><circle cx="15" cy="5.5" r="2"/><circle cx="19" cy="11" r="2"/><path d="M12 12c-3 0-6 3-6 6 0 2 2 3 3.5 3 1 0 1.8-.5 2.5-.5s1.5.5 2.5.5c1.5 0 3.5-1 3.5-3 0-3-3-6-6-6z"/>',
'iot-energy-utilities':'<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
'industrial-iot':'<path d="M2 20V8l6 4V8l6 4V4h4v16H2z"/><path d="M6 16h.01M10 16h.01M14 16h.01"/>',
'iot-healthcare':'<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>',
'telematics-fleet':'<polygon points="3 11 22 2 13 21 11 13 3 11"/>',
'consumer-iot':'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
'iot-in-defence':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
'iot-logistics':'<path d="M21 8 12 3 3 8v8l9 5 9-5V8z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
}
p=ROOT+'/industries.html'; s=open(p,encoding='utf-8').read(); n=0
def rep(m):
    global n; slug=m.group(2)
    if slug not in I: return m.group(0)
    n+=1; return f'{m.group(1)}<svg {S}>{I[slug]}</svg></div>'
s=re.sub(r'(<a href="industries/([a-z-]+)\.html" class="pg-ind-card">\s*<div class="pg-ind-card__icon" style="[^"]*">)<svg.*?</svg></div>',rep,s,flags=re.S)
open(p,'w',encoding='utf-8').write(s); print('industries.html icons set:',n)
