#!/usr/bin/env python3
"""Builds services/nms.html (Network Management System) from services/lora-management-system.html as the shell.
Run from project root AFTER apply_index_header.py:  python3 tools/build_nms.py"""
import re, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(ROOT+'/services/lora-management-system.html',encoding='utf-8').read()
T='Network Management System (NMS) | Nebulae'
D='Network Management System (NMS) by Nebulae: monitor and manage gateways, concentrators and nodes with live network health, topology, alarms, remote configuration and firmware updates.'
s=re.sub(r'<title>.*?</title>',f'<title>{T}</title>',s,count=1,flags=re.S)
s=re.sub(r'(<meta name="description" content=")[^"]*(")',r'\g<1>'+D+r'\2',s,count=1)
s=re.sub(r'(<meta property="og:title" content=")[^"]*(")',r'\g<1>'+T+r'\2',s,count=1)
s=re.sub(r'(<meta property="og:description" content=")[^"]*(")',r'\g<1>'+D+r'\2',s,count=1)
s=re.sub(r'(<meta name="twitter:title" content=")[^"]*(")',r'\g<1>'+T+r'\2',s,count=1)
s=re.sub(r'(<meta name="twitter:description" content=")[^"]*(")',r'\g<1>'+D+r'\2',s,count=1)
s=s.replace('lora-management-system.html"','nms.html"').replace('LoRa Management System (LMS)"','Network Management System (NMS)"')
def feat(t,d): return f'<li><div class="sl-feat-list__icon" style="background:rgba(79,70,229,.1);color:#4f46e5;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div><span><strong>{t}</strong> — {d}</span></li>'
def card(n,t,d,cls='col-12 col-sm-6 col-lg-4'): return f'<div class="{cls}"><div class="slx-card"><div class="slx-card__n">{n}</div><h3>{t}</h3><p>{d}</p></div></div>'
F=[('Network health at a glance','live status of gateways, concentrators and nodes'),('Topology view','see how devices connect and where coverage is weak'),('Alarms &amp; notifications','instant alerts for offline devices and abnormal behaviour'),
   ('Remote configuration','change device and network parameters without a site visit'),('Firmware management','plan and track over-the-air updates across device groups'),('Reports &amp; KPIs','uptime, signal quality and delivery statistics, exportable')]
W=[('Fewer site visits','Diagnose and fix many issues remotely.'),('Faster fault detection','Know about an offline device before the customer does.'),('One view of the network','Gateways, concentrators and nodes in a single console.'),
   ('Works with your platform','APIs to connect with HES, MDMS and other back-end systems.'),('Role-based access','Separate views and permissions for operators, engineers and managers.'),('Flexible deployment','Cloud-hosted or on your own infrastructure.')]
body=f'''<section class="sl-hero"> <div class="sl-hero__grid"></div> <div class="sl-hero__orb sl-hero__orb--1"></div> <div class="sl-hero__orb sl-hero__orb--2"></div>
<div class="container"> <div class="sl-hero__inner"> <nav class="sl-breadcrumb" aria-label="breadcrumb"> <a href="../index.html">Home</a><span>›</span> <a href="../services.html">Services</a><span>›</span> <span style="color:rgba(255,255,255,.65);">Network Management System</span> </nav>
<div class="sl-eyebrow">Cloud · Network Operations</div> <h1 class="sl-hero__title">Network Management System (NMS)</h1>
<p class="sl-hero__desc">Monitor, configure and maintain your IoT network from one console — live device status, topology, alarms, remote configuration and firmware updates for gateways, concentrators and nodes.</p>
<div class="sl-jump-pills"><a href="#overview" class="sl-jump-pill">Overview</a><a href="#benefits" class="sl-jump-pill">Why NMS</a><a href="../contact.html?inquiry=solution&amp;topic=Network%20Management%20System" class="sl-jump-pill">Get a Proposal</a></div> </div> </div> </section>
<section class="sl-section" id="overview"> <div class="container"> <div class="row g-5 align-items-start">
<div class="col-lg-6"> <span class="sl-solution__tag" style="background:rgba(79,70,229,.1);color:#4f46e5;">Cloud · Network operations</span>
<h2 class="sl-solution__title" style="color:#111827;">Keep every device in your network visible and under control</h2>
<p class="sl-solution__desc" style="color:#374151;">Large IoT deployments are hard to run when problems only show up as missing data. The Nebulae NMS gives your operations team a live picture of the network, so faults are found early and handled remotely.</p>
<p class="sl-solution__desc" style="color:#374151;">It is built for the networks Nebulae devices run on, including LoRaWAN and Wi-SUN, and can be tailored to your deployment and reporting needs.</p>
<div style="display:flex;gap:.75rem;margin-top:1.75rem;flex-wrap:wrap;"> <a href="../contact.html?inquiry=solution&amp;topic=Network%20Management%20System" class="sl-sol-btn sl-sol-btn--primary">Get a Proposal</a> <a href="../contact.html?inquiry=meeting&amp;topic=Network%20Management%20System" class="sl-sol-btn sl-sol-btn--outline">Request a Demo</a> </div> </div>
<div class="col-lg-6"> <ul class="sl-feat-list" id="features">{''.join(feat(*f) for f in F)}</ul>
<div class="sl-products-strip"><a href="../services/lorawan-network-server.html" class="sl-product-chip">LoRaWAN Network Server</a><a href="../services/lora-management-system.html" class="sl-product-chip">LoRa Management System</a><a href="../products.html?type=gateway" class="sl-product-chip">Gateways</a></div> </div>
</div> </div> </section>
<section class="sl-section sl-section--surf" id="benefits"><div class="container slx-cards"><div class="sl-eyebrow-sm">Why NMS</div><h2 class="sl-section-title">What You Get</h2><div class="row g-3 mt-1">{''.join(card(i+1,*w) for i,w in enumerate(W))}</div></div></section>
<section class="sl-related"><div class="container"><p class="sl-related__title">Related Services</p><div class="row g-3">
<div class="col-6 col-md-4"><a href="../services/lorawan-network-server.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(79,70,229,.1);color:#4f46e5;">Cloud</span><p class="sl-rel-card__name">LoRaWAN Network Server (LNS)</p><p class="sl-rel-card__desc">Network server for LoRaWAN gateways and devices.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>
<div class="col-6 col-md-4"><a href="../services/lora-management-system.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(13,148,136,.1);color:#0d9488;">Cloud</span><p class="sl-rel-card__name">LoRa Management System</p><p class="sl-rel-card__desc">Cloud platform for monitoring and controlling street lights.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>
<div class="col-6 col-md-4"><a href="../services/iot-cloud-integration.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(234,88,12,.1);color:#ea580c;">Integration</span><p class="sl-rel-card__name">IoT Cloud Integration</p><p class="sl-rel-card__desc">Connect devices to your cloud and back-end systems.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>
</div></div></section>
<section style="padding:4rem 0;background:#fff;"><div class="container"><div class="sl-cta-wrap">
  <h2 style="font-family:'Outfit',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:800;color:#fff;margin-bottom:.75rem;">Talk to us about your network</h2>
  <p style="color:rgba(255,255,255,.6);font-size:.97rem;max-width:560px;margin:0 auto 2rem;">Tell us about your deployment and we will propose the right NMS set-up.</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
    <a href="../contact.html?inquiry=solution&amp;topic=Network%20Management%20System" class="sl-sol-btn sl-sol-btn--primary">Start a Conversation</a>
    <a href="../services.html" class="sl-sol-btn sl-sol-btn--dark-outline">All Services →</a>
  </div></div></div></section>
'''
i=s.index('<section class="sl-hero">'); j=s.index('<footer')
s=s[:i]+body+s[j:]
open(ROOT+'/services/nms.html','w',encoding='utf-8').write(s); print('services/nms.html written')
