#!/usr/bin/env python3
"""Builds solutions/energy-management.html from the SunSights 'Smart Energy Management Solutions' brochure (no logo / contact details used).
Shell (head/header/footer) cloned from solutions/smart-gas-meter.html. Run AFTER apply_index_header.py / build_solutions.py, then apply_footer.py.
Usage: python3 tools/build_energy_management.py"""
import re,os,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(ROOT+'/solutions/smart-gas-meter.html',encoding='utf-8').read()
E=lambda t:html.escape(t,quote=True)
T='Energy Management Solution — Smart Energy Monitoring &amp; Optimization | Nebulae'
D='Cloud-based energy management: measure, monitor, analyze, manage and optimize energy, gas, water and air consumption with live dashboards, analytics, alerts and AI-based recommendations.'
s=re.sub(r'<title>.*?</title>',f'<title>{T}</title>',s,count=1,flags=re.S)
for pat in [r'(<meta name="description" content=")[^"]*(")',r'(<meta property="og:title" content=")[^"]*(")',r'(<meta property="og:description" content=")[^"]*(")',r'(<meta name="twitter:title" content=")[^"]*(")',r'(<meta name="twitter:description" content=")[^"]*(")']:
    v=T if 'title' in pat else D
    s=re.sub(pat,lambda m:m.group(1)+v+m.group(2),s,count=1)
s=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1energy management solution, energy monitoring, energy audit, SEC analytics, TOD analysis, industrial energy optimization, IoT energy dashboard\2',s,count=1,flags=re.S)
s=s.replace('smart-gas-meter.html','energy-management.html').replace('"Smart Gas Meter"','"Energy Management Solution"')
IMG='../assets/images/solutions/'
chk='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
feat=lambda t,d:f'<li><div class="sl-feat-list__icon" style="background:rgba(79,70,229,.1);color:#4f46e5;">{chk}</div><span><strong>{t}</strong> — {d}</span></li>'
card=lambda n,t,d,c='col-12 col-sm-6 col-lg-4':f'<div class="{c}"><div class="slx-card"><div class="slx-card__n">{n}</div><h3>{t}</h3><p>{d}</p></div></div>'
fig=lambda img,cap:f'<div class="col-6 col-lg-3"><figure class="slx-fig"><div class="slx-fig__img"><img loading="lazy" src="{IMG}{img}" alt="{E(cap)}"/></div><figcaption>{cap}</figcaption></figure></div>'
seg=lambda img,t,d:f'<div class="col-12 col-md-6 col-lg-3"><div class="sl-hw-card" style="height:100%"><span class="sl-hw-card__img" style="aspect-ratio:3/2"><img style="padding:0;object-fit:cover" loading="lazy" src="{IMG}{img}" alt="{E(t)}"/></span><span class="sl-hw-card__model">{t}</span><span class="sl-hw-card__name">{d}</span></div></div>'
PLAT=[('Live IoT monitoring','Field data for energy, gas, water and air consumption.'),('Customised dashboards','Periodic reports and alerts built around your plant.'),('Trend analysis','Performance benchmarking against past and peer data.'),('Time of Day (TOD) analysis','See when energy is used and shift load to cut cost.'),
      ('Specific Energy Consumption (SEC)','Energy per unit of output, tracked over time.'),('Safe data storage','Secure storage with easy retrieval.'),('Real-time recommendations','Suggestions for energy optimization and reliability.'),('AI for Industry 4.0','Artificial intelligence built with the latest digital tools.'),('Digital plant benchmarking','Compare against the digital plant framework.')]
OPT=[('Coverage','Facility-wide monitoring of processes, utilities and equipment.'),('Descriptive','Real-time encrypted data collection and analysis.'),('Predictive','Inefficiency detection through threshold comparison.'),('Prescriptive','Real-time optimization insights and recommendations.'),('360° awareness','Smart alerts on equipment and productivity.')]
USE=['Process monitoring and optimization in cement, metal, food &amp; beverages, auto, paper, glass and mining','Waste heat recovery','Equipment-level analytics in the automobile industry','Energy management solutions','Air compressor performance analytics','Office-space energy management with automation','Power quality improvement','Energy audits (industrial and commercial)']
body=f'''<section class="sl-hero"> <div class="sl-hero__grid"></div> <div class="sl-hero__orb sl-hero__orb--1"></div> <div class="sl-hero__orb sl-hero__orb--2"></div>
<div class="container"><div class="sl-hero__inner"><nav class="sl-breadcrumb" aria-label="breadcrumb"><a href="../index.html">Home</a><span>›</span><a href="../solutions.html">Solutions</a><span>›</span><span style="color:rgba(255,255,255,.65);">Energy Management</span></nav>
<div class="sl-eyebrow">Energy Management · Industry 4.0</div><h1 class="sl-hero__title">Energy Management Solution</h1>
<p class="sl-hero__desc">A cloud-based platform to measure, monitor, analyze, manage and optimize energy — turning live field data into cost savings, better maintenance decisions and fewer inefficiencies.</p>
<div class="sl-jump-pills"><a href="#overview" class="sl-jump-pill">Overview</a><a href="#platform" class="sl-jump-pill">Platform</a><a href="#segments" class="sl-jump-pill">Segments</a><a href="#usecases" class="sl-jump-pill">Use Cases</a><a href="../contact.html?inquiry=solution&amp;topic=Energy%20Management%20Solution" class="sl-jump-pill">Get a Proposal</a></div></div></div></section>
<section class="sl-section" id="overview"><div class="container"><div class="row align-items-center g-5">
<div class="col-lg-6"><div class="slx-hero-img"><img src="{IMG}em-plant.webp" alt="Power plant — energy management for industries and utilities" width="1280" height="480" style="width:100%;height:100%;min-height:320px;object-fit:cover"/>
<div class="sl-img-card__stat"><div class="sl-img-card__stat-item"><span class="sl-img-card__stat-num">Facility-wide</span><span class="sl-img-card__stat-label">Monitoring coverage</span></div><div class="sl-img-card__stat-item"><span class="sl-img-card__stat-num">4 utilities</span><span class="sl-img-card__stat-label">Energy · Gas · Water · Air</span></div><div class="sl-img-card__stat-item"><span class="sl-img-card__stat-num">Real-time</span><span class="sl-img-card__stat-label">Alerts &amp; insights</span></div></div></div></div>
<div class="col-lg-6"><span class="sl-solution__tag" style="background:rgba(79,70,229,.1);color:#4f46e5;">Cloud platform · Analytics · Audits</span>
<h2 class="sl-solution__title" style="color:#111827;">Smart Optimization &amp; Usage of Energy</h2>
<p class="sl-solution__desc" style="color:#374151;">Optimize costs through intelligent asset automation, redefine maintenance with data-driven strategies and find inefficiencies using energy consumption insights.</p>
<p class="sl-solution__desc" style="color:#374151;">The solution is delivered by SunSights, our solar and energy solutions brand under System Level Solutions, and runs on Nebulae IoT hardware for data collection.</p>
<ul class="sl-feat-list" id="features">{''.join(feat(a,b) for a,b in OPT)}</ul>
<div class="sl-products-strip"><a href="../services/hes-electricity-metering.html" class="sl-product-chip">HES — Electricity</a><a href="../solutions/smart-electric-meter.html" class="sl-product-chip">Smart Electric Meter</a><a href="../products.html?type=gateway" class="sl-product-chip">Gateways</a><a href="../services/nms.html" class="sl-product-chip">NMS</a></div>
<div style="display:flex;gap:.75rem;margin-top:1.75rem;flex-wrap:wrap;"><a href="../contact.html?inquiry=solution&amp;topic=Energy%20Management%20Solution" class="sl-sol-btn sl-sol-btn--primary">Get a Proposal</a><a href="../contact.html?inquiry=meeting&amp;topic=Energy%20Management%20Solution" class="sl-sol-btn sl-sol-btn--outline">Book a Meeting</a></div></div>
</div></div></section>
<section class="sl-section sl-section--surf" id="platform"><div class="container slx-cards"><div class="sl-eyebrow-sm">Platform</div><h2 class="sl-section-title">Our Platform Capabilities</h2><div class="row g-3 mt-1">{''.join(card(i+1,a,b) for i,(a,b) in enumerate(PLAT))}</div></div></section>
<section class="sl-section" id="segments"><div class="container"><div class="sl-eyebrow-sm">Key Segments</div><h2 class="sl-section-title">Industries &amp; Utilities We Serve</h2><div class="row g-3 mt-1">
{seg('em-forge.webp','Industries','Manufacturing — cement, metal, food &amp; beverages, auto, paper, glass, textile, chemicals and more.')}
{seg('em-pumps.webp','Utilities','Power generation and distribution, gas, water and similar utilities.')}
{seg('em-commercial.webp','Commercial utilities','Retail, healthcare, hospitality, education, IT parks, office complexes, clubs and theatres.')}
{seg('em-cnc.webp','Precision machines &amp; UMC','Automotive, aerospace, tool &amp; die, electronics, medical devices, heavy engineering and railways — CNC units, tool rooms, prototyping labs and advanced manufacturing facilities.')}
</div></div></section>
<section class="sl-section sl-section--surf" id="usecases"><div class="container"><div class="row g-5 align-items-start"><div class="col-lg-5"><div class="sl-eyebrow-sm">Use Cases</div><h2 class="sl-section-title">A Glimpse of Use Cases</h2>
<ul class="sl-feat-list" style="margin-top:1rem">{''.join(feat('',u).replace('<strong></strong> — ','') for u in USE)}</ul></div>
<div class="col-lg-7"><div class="row g-3">{fig('em-metal.webp','Metal &amp; fabrication')}{fig('em-food.webp','Food &amp; beverages')}{fig('em-beverage.webp','Beverage bottling')}{fig('em-warehouse.webp','Warehousing')}{fig('em-health.webp','Healthcare')}{fig('em-lab.webp','Education &amp; labs')}{fig('em-hospital-ot.webp','Hospitals')}{fig('em-forge.webp','Heavy industry')}</div></div></div></div></section>
<section class="sl-section" id="services"><div class="container slx-cards"><div class="sl-eyebrow-sm">Services</div><h2 class="sl-section-title">End-to-End Energy Services</h2><p class="sl-section-desc" style="max-width:760px;color:#4b5563">Beyond the platform, we cover comprehensive energy audits, end-to-end project management, efficient implementation and sourcing of best-in-class equipment, with access to competitive financing solutions.</p>
<div class="row g-3 mt-1">{card(1,'Supply','Rooftop solar, open access and renewable energy sourcing.','col-12 col-md-6')}{card(2,'Demand','Energy audits, real-time dashboards, energy analytics and optimization insights.','col-12 col-md-6')}</div></div></section>
<section class="sl-related"><div class="container"><p class="sl-related__title">Related Solutions</p><div class="row g-3">
<div class="col-6 col-md-4"><a href="../solutions/smart-electric-meter.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(234,88,12,.1);color:#ea580c;">AMI</span><p class="sl-rel-card__name">Smart Electric Meter</p><p class="sl-rel-card__desc">Wi-SUN / RF AMI for IS 16444 smart meters with NMS, HES and Energy+ app.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>
<div class="col-6 col-md-4"><a href="../solutions/transformer-monitoring.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(37,99,235,.1);color:#2563eb;">DISCOM</span><p class="sl-rel-card__name">Transformer Monitoring</p><p class="sl-rel-card__desc">Real-time electrical and sensor monitoring for distribution transformers.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div>
<div class="col-6 col-md-4"><a href="../services/hes-electricity-metering.html" class="sl-rel-card"><span class="sl-rel-card__tag" style="background:rgba(124,58,237,.1);color:#7c3aed;">Software</span><p class="sl-rel-card__name">HES — Electricity</p><p class="sl-rel-card__desc">Head End System for smart electricity metering networks.</p><span class="sl-rel-card__arrow">Learn more →</span></a></div></div></div></section>
<section style="padding:4rem 0;background:#fff;"><div class="container"><div class="sl-cta-wrap"><h2 style="font-family:'Outfit',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:800;color:#fff;margin-bottom:.75rem;">Ready to cut your energy cost?</h2>
<p style="color:rgba(255,255,255,.6);font-size:.97rem;max-width:560px;margin:0 auto 2rem;">Tell us about your facility and we will propose the right monitoring and optimization set-up.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;"><a href="../contact.html?inquiry=solution&amp;topic=Energy%20Management%20Solution" class="sl-sol-btn sl-sol-btn--primary">Get a Proposal</a><a href="../solutions.html" class="sl-sol-btn sl-sol-btn--dark-outline">All Solutions →</a></div></div></div></section>
'''
i=s.index('<section class="sl-hero"'); j=s.index('<footer')
s=s[:i]+body+s[j:]
open(ROOT+'/solutions/energy-management.html','w',encoding='utf-8').write(s); print('written')
