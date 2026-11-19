#!/usr/bin/env python3
"""Menu column-title icons: same icon as the same concept elsewhere on the site (industries.html / product application icons).
Edits index.html (source of truth); then run apply_index_header.py. Idempotent."""
import re,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A='width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="atl-ico-stroke" aria-hidden="true"'
I={
'Smart Metering':'<circle cx="12" cy="12" r="9"/><path d="m12 12 4-4"/><path d="M7 16h10"/>',            # = product "Smart Metering"
'Smart Infrastructure':'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',  # = Building Management System
'Energy Management':'<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',                                        # = IoT in Energy & Utilities
'Smart City':'<path d="M3 21V9l5-4 5 4v12M13 21V5l5-2 3 2v16"/><path d="M2 21h20"/>',                      # = Smart City Solutions
'Agriculture & Energy':'<path d="M12 22V12M12 12C12 12 7 9 7 4a5 5 0 0110 0c0 5-5 8-5 8z"/>',            # = Smart Agriculture
'Industrial & Automotive':'<path d="M2 20V8l6 4V8l6 4V4h4v16H2z"/><path d="M6 16h.01M10 16h.01M14 16h.01"/>', # = Industrial IoT
'Healthcare':'<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>', # = IoT in Healthcare
'Defence':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',            # = IoT in Defence
}
p=ROOT+'/index.html'; s=open(p,encoding='utf-8').read(); n=0
pat=re.compile(r'(<div class="atl-mega__col-icon[^"]*"[^>]*>)<svg.*?</svg>(\s*</div>\s*<div>\s*<p class="atl-mega__col-title">([^<]*)</p>)',re.S)
def rep(m):
    global n
    t=m.group(3).replace('&amp;','&').strip()
    if t not in I: return m.group(0)
    n+=1; return f'{m.group(1)}<svg {A}>{I[t]}</svg>{m.group(2)}'
s=pat.sub(rep,s)
open(p,'w',encoding='utf-8').write(s); print('menu icons set',n)
