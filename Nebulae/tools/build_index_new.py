#!/usr/bin/env python3
"""Builds index-new.html (a separate, noindex preview of a reworked home page) from index.html.
index.html is NEVER modified. To drop the experiment: delete index-new.html, assets/css/index-new.css, assets/js/index-new.js
(and optionally this script).   Rebuild after editing index.html's header/footer:  python3 tools/build_index_new.py"""
import os, re, json, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
os.chdir(ROOT)
src = open('index.html', encoding='utf-8').read()
L = src.split('\n')

def find(pat, start=0):
    for i in range(start, len(L)):
        if re.search(pat, L[i]): return i
    raise SystemExit('marker not found: ' + pat)
def block(a, b): return '\n'.join(L[a:b]) + '\n'

i_hero   = find(r'<section class="nbl-hero"')
i_logos  = find(r'═══ PARTNER / LOGO STRIP')
i_stats  = find(r'═══ STATS COUNTER')
i_tech   = find(r'═══ 3\. KEY TECHNOLOGIES')
i_comp   = find(r'═══ PROTOCOL COMPARISON')
i_prod   = find(r'═══ 4\. PRODUCT HIGHLIGHTS')
i_use    = find(r'═══ USE-CASE SELECTOR')
i_ind    = find(r'═══ INDUSTRIES QUICK LINKS')
i_upd    = find(r'═══ 5\. UPDATES')
i_sol    = find(r'═══ 7\. NEBULAE SOLUTIONS')
i_exp    = find(r'<section class="nbl-exp-section"')
i_why    = find(r'═══ 8\. WHY CHOOSE NEBULAE')
i_roi    = find(r'═══ ROI CALCULATOR')
i_cta    = find(r'═══ 9\. CTA SECTION')
i_news   = find(r'═══ NEWSLETTER SIGNUP')
i_sample = find(r'═══ SAMPLE /  EVK REQUEST')
i_foot   = find(r'═══ 10\. FOOTER')
top      = block(0, i_hero)

# ---------------------------------------------------------------- head
top = top.replace('<title>Nebulae | IoT, LoRa, Wi-SUN &amp; Smart Connectivity Solutions</title>', '<title>Nebulae | IoT Modules, Gateways &amp; Solutions (new home preview)</title>')
top = top.replace('<meta name="robots" content="index, follow" />', '<meta name="robots" content="noindex, follow" />')   # preview: keep out of search; canonical still points to the live home page
top = top.replace('</head>', '  <link rel="stylesheet" href="./assets/css/index-new.css">\n</head>', 1)
top = top.replace('<body>', '<body class="nin">', 1)

# ---------------------------------------------------------------- hero
hero = block(i_hero, i_logos)
hero = re.sub(r'(<p class="nbl-hero__desc">.*?</p>)', r'<p class="nbl-hero__desc nin-hero__plain"><strong>Nebulae designs and makes wireless IoT modules, gateways and complete solutions</strong> for utilities, cities, farms and factories — built in Anand, Gujarat.</p>\n        \1', hero, count=1, flags=re.S)
btns = '''<div class="nbl-hero__btns">
          <button type="button" class="nbl-btn-primary nin-quote-btn" data-nin-quote="General enquiry from the home page">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            Request a Quote
          </button>
          <a href="products.html" class="nbl-btn-outline">Explore Products</a>
          <a href="solutions.html" class="nbl-btn-outline">Explore Solutions</a>
        </div>'''
hero = re.sub(r'<div class="nbl-hero__btns">.*?</div>\s*(?=<div class="nbl-hero__stats">)', btns + '\n        ', hero, count=1, flags=re.S)
n_ind = len([f for f in os.listdir('industries') if f.endswith('.html')])
stats = f'''<div class="nbl-hero__stats">
          <div class="nbl-hero__stat-item"><span class="nbl-hero__stat-num">6+</span><span class="nbl-hero__stat-label">Protocols</span></div>
          <div class="nbl-hero__stat-divider"></div>
          <div class="nbl-hero__stat-item"><span class="nbl-hero__stat-num">{n_ind}</span><span class="nbl-hero__stat-label">Industries</span></div>
          <div class="nbl-hero__stat-divider"></div>
          <div class="nbl-hero__stat-item"><span class="nbl-hero__stat-num">Pan-India</span><span class="nbl-hero__stat-label">Deployments</span></div>
        </div>'''
hero = re.sub(r'<div class="nbl-hero__stats">.*?</div>\s*</div>\s*(?=<div class="col-lg-6" data-anim="slide-right">)', stats + '\n      </div>\n      ', hero, count=1, flags=re.S)
hero = hero.replace('<div class="nbl-hero__eyebrow">', '<a class="nin-announce" href="products/nlg7644.html"><span class="nin-announce__tag">New</span> LoRaWAN gateway with 4G + GPS — NLG7644 <span aria-hidden="true">→</span></a>\n        <div class="nbl-hero__eyebrow">', 1)
hero = re.sub(r'</section>\s*$', '<div class="nin-wave nin-wave--white" aria-hidden="true"><svg viewBox="0 0 1440 90" preserveAspectRatio="none"><path d="M0,50 C220,100 460,0 720,46 C980,92 1210,10 1440,52 L1440,90 L0,90 Z"/></svg></div>\n</section>\n', hero, count=1)
hero = hero.replace('<section class="nbl-hero" id="nbl-hero">', '<section class="nbl-hero" id="nbl-hero" aria-label="Nebulae — IoT modules, gateways and solutions">', 1)

# ---------------------------------------------------------------- logos (pause control for the moving strip)
logos = block(i_logos, i_stats)
logos = logos.replace('<h2 class="nbl-logos-label">Supported Technologies</h2>', '<h2 class="nbl-logos-label">Supported Technologies</h2>\n    <button type="button" class="nin-pause" id="ninPause" aria-pressed="false" aria-label="Pause moving logos">Pause</button>', 1)

# ---------------------------------------------------------------- stats: real values in the HTML (animation only runs when scrolled into view and motion is allowed)
stats_sec = block(i_stats, i_tech)
def fmt(n): return (f'{n // 1000}K' if n >= 1000 else str(n))
stats_sec = re.sub(r'data-counter="(\d+)" data-suffix="([^"]*)">0\+<', lambda m: f'data-counter="{m.group(1)}" data-suffix="{m.group(2)}">{fmt(int(m.group(1)))}{m.group(2)}<', stats_sec)

tech = block(i_tech, i_comp)
compare = block(i_comp, i_prod)
solutions = block(i_sol, i_exp)
expertise = block(i_exp, i_why)
why = block(i_why, i_roi)
newsletter = block(i_news, i_sample)
sample = block(i_sample, i_foot)
sample = sample.replace('<section class="nbl-sample-section">', '<section class="nbl-sample-section" id="sample">', 1)
tail = block(i_foot, len(L))

# ---------------------------------------------------------------- data
PROD = json.load(open('tools/products_index.json', encoding='utf-8'))
cnt = lambda t: sum(1 for p in PROD if p['type_key'] == t)
cats = [
  ('module', 'Wireless Hardware', 'IoT Modules', 'Certified LoRa, Wi-SUN, Zigbee, Wi-Fi and BLE modules in compact SMD and card formats.', 'assets/images/products/nln811p-1.webp', 'Browse modules'),
  ('gateway', 'Network Hardware', 'Gateways & Concentrators', 'Industrial LoRaWAN, Wi-SUN and SCADA gateways — outdoor-rated, cloud-ready, multi-channel.', 'assets/images/products/nlg7644-gateway.jpg', 'Browse gateways'),
  ('evk', 'Development Tools', 'Evaluation Kits', 'Ready-to-use kits to prototype and prove a concept before you commit to a design.', 'assets/images/products/nln0651i-1.webp', 'Browse EVKs'),
  ('node', 'Endpoint Devices', 'Nodes & Sensors', 'Stand-alone LoRaWAN end-nodes and AMR devices for metering, agriculture and monitoring.', 'assets/images/products/nln500a-1.webp', 'Browse nodes'),
]
prod_html = '''<!-- ═══ WHAT WE MAKE ═══ -->
<section class="nin-sec nin-sec--white" id="products">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">What we make</span><h2>Hardware built for the real world</h2><p>From compact surface-mount modules to rack-grade industrial gateways — every Nebulae product is engineered for reliability and long field life.</p></div>
    <div class="row g-4">
'''
for k, cat, title, desc, img, cta in cats:
    prod_html += f'''      <div class="col-sm-6 col-lg-3"><a class="nin-pcard" href="products.html?type={k}">
        <span class="nin-pcard__img"><img src="{img}" alt="{html.escape(title, quote=True)}" width="480" height="320" loading="lazy" decoding="async"></span>
        <span class="nin-pcard__body"><span class="nin-pcard__cat">{cat} · {cnt(k)} products</span><span class="nin-pcard__title">{html.escape(title)}</span><span class="nin-pcard__desc">{desc}</span><span class="nin-pcard__cta">{cta} →</span></span></a></div>
'''
prod_html += '    </div>\n  </div>\n</section>\n\n'

finder = '''<!-- ═══ PRODUCT FINDER ═══ -->
<section class="nin-sec nin-sec--tint" id="finder">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">Find your product</span><h2>Tell us what you're connecting</h2><p>Three quick choices and we'll suggest the Nebulae products that usually fit. Not sure? Send us the details and an engineer will advise.</p></div>
    <div class="nin-finder" id="ninFinder">
      <form class="nin-finder__form" onsubmit="return false" aria-label="Product finder">
        <label>What are you connecting?
          <select id="ninApp">
            <option value="meters">Utility meters (water, gas, electricity)</option>
            <option value="city">Street lights &amp; smart-city infrastructure</option>
            <option value="farm">Farms, fields &amp; livestock</option>
            <option value="home">Buildings, homes &amp; security devices</option>
            <option value="assets">Vehicles, assets &amp; trackers</option>
            <option value="industrial">Industrial plant &amp; SCADA / RTU</option>
            <option value="wearables">Wearables &amp; personal-safety devices</option>
          </select></label>
        <label>How far must the signal travel?
          <select id="ninRange">
            <option value="short">Inside a building (under ~100 m)</option>
            <option value="mid" selected>Campus or neighbourhood (up to a few km)</option>
            <option value="long">City / wide area, or cellular backhaul</option>
          </select></label>
        <label>How is the device powered?
          <select id="ninPower">
            <option value="battery">Battery — must last years</option>
            <option value="mains">Mains / external supply</option>
          </select></label>
      </form>
      <div class="nin-finder__out" id="ninOut" aria-live="polite"></div>
    </div>
  </div>
</section>

'''

IND = [  # slug, name, blurb
 ('smart-city-solutions', 'Smart City', 'Street lighting, EV charging, city networks'),
 ('iot-energy-utilities', 'Energy & Utilities', 'Smart metering and grid monitoring'),
 ('smart-agriculture', 'Smart Agriculture', 'Irrigation, soil and weather sensing'),
 ('industrial-iot', 'Industrial IoT', 'SCADA RTUs, gateways, wireless sensing'),
 ('iot-healthcare', 'Healthcare', 'Connected devices, tracking, hospital networks'),
 ('home-security-automation', 'Home Security & Automation', 'Zigbee, Matter and Wi-Fi modules'),
 ('iot-logistics', 'Logistics', 'Fleet, asset tracking, cold chain'),
 ('building-management-system', 'Building Management', 'HVAC, access, energy, security'),
 ('consumer-iot', 'Consumer IoT', 'Wearables and connected gadgets'),
 ('farm-animal-management', 'Farm & Animal Management', 'Livestock tracking and monitoring'),
 ('iot-in-defence', 'Defence & Safety', 'Rugged, long-range communication'),
 ('sos-devices', 'SOS & Personal Safety', 'Emergency alert devices'),
 ('telematics-fleet', 'Telematics & Fleet', 'Vehicle tracking and fleet visibility'),
]
photos = json.load(open('tools/industry_photos.json', encoding='utf-8'))
ind_html = f'''<!-- ═══ INDUSTRIES ═══ -->
<section class="nin-sec nin-sec--white" id="industries">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">Industries we serve</span><h2>IoT for every sector</h2><p>{len(IND)} industry pages with the products, use cases and system designs we recommend for each.</p></div>
    <div class="row g-3 justify-content-center">
'''
for slug, name, blurb in IND:
    local = next((f'assets/images/industries/{slug}.{e}' for e in ('jpg', 'webp', 'png') if os.path.exists(f'assets/images/industries/{slug}.{e}')), None)
    url = local or (photos[slug] + '?auto=format&fit=crop&w=640&h=420&q=70' if slug in photos else None)
    img = f'<img src="{url}" alt="" width="640" height="420" loading="lazy" decoding="async" onerror="this.remove()">' if url else ''
    ind_html += f'''      <div class="col-6 col-md-4 col-xl-3"><a class="nin-icard" href="industries/{slug}.html"><span class="nin-icard__img">{img}</span><span class="nin-icard__body"><span class="nin-icard__title">{html.escape(name)}</span><span class="nin-icard__desc">{html.escape(blurb)}</span></span></a></div>
'''
ind_html += '    </div>\n    <p class="nin-more"><a href="industries.html">View all industries →</a></p>\n  </div>\n</section>\n\n'

deeper = f'''<!-- ═══ GO DEEPER (solutions tabs collapsed so the page stays short) ═══ -->
<section class="nin-sec nin-sec--tint" id="go-deeper">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">Go deeper</span><h2>Solutions by sector</h2><p>Smart metering, smart city, industrial, building, agriculture, home, healthcare and defence — open the panel for the full detail.</p></div>
    <details class="nin-fold"><summary>Open solutions by sector</summary><div class="nin-fold__body nin-fold__body--bare">
{solutions}
    </div></details>
  </div>
</section>

'''

cta = '''<!-- ═══ CTA ═══ -->
<section class="nbl-cta-section" id="cta">
  <div class="container">
    <div class="nbl-cta-wrap">
      <h2 class="nbl-cta-title">Ready to build your<br><span>IoT solution?</span></h2>
      <p class="nbl-cta-desc">Talk to our engineers. Whether you need a single module or a complete end-to-end deployment — we'll help you scope it.</p>
      <div class="nbl-cta-btns">
        <button type="button" class="nbl-cta-btn-primary nin-quote-btn" data-nin-quote="Project enquiry from the home page">Request a Quote</button>
        <a href="contact.html" class="nbl-cta-btn-primary">Talk to an Engineer</a>
      </div>
      <div class="nbl-cta-contact-strip">
        <a href="tel:+919898042339" class="nbl-cta-contact-item">+91 9898042339</a>
        <a href="mailto:sales@nebulae.io" class="nbl-cta-contact-item">sales@nebulae.io</a>
        <a href="about.html" class="nbl-cta-contact-item">Anand, Gujarat, India</a>
      </div>
    </div>
  </div>
</section>

'''


process = """<!-- ═══ HOW WE WORK ═══ -->
<section class="nin-sec nin-sec--white nin-process" id="process">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">How we work</span><h2>From idea to deployment in five steps</h2><p>One team covers hardware, firmware, certification and cloud — so you don't juggle vendors.</p></div>
    <ol class="nin-steps">
      <li><span class="nin-step__no">01</span><h3>Discuss</h3><p>Share your use case, range and power needs. We recommend the protocol and parts.</p></li>
      <li><span class="nin-step__no">02</span><h3>Design</h3><p>Schematic, PCB, antenna and firmware design — or pick a ready module.</p></li>
      <li><span class="nin-step__no">03</span><h3>Prototype</h3><p>Start on an evaluation kit and prove the concept before committing.</p></li>
      <li><span class="nin-step__no">04</span><h3>Certify &amp; build</h3><p>Compliance testing support and production-ready manufacturing.</p></li>
      <li><span class="nin-step__no">05</span><h3>Deploy &amp; support</h3><p>Field commissioning, cloud integration and ongoing engineering support.</p></li>
    </ol>
    <p class="nin-more"><a href="services.html">See all engineering services →</a></p>
  </div>
</section>

"""
eco = """<!-- ═══ ECOSYSTEM ═══ -->
<section class="nin-sec nin-sec--tint nin-eco" id="ecosystem">
  <div class="container">
    <div class="nin-head"><span class="nin-eyebrow">Works with your stack</span><h2>Open standards, familiar cloud tools</h2><p>Nebulae devices connect to the platforms and protocols your team already uses.</p></div>
    <div class="row g-3">
      <div class="col-md-6 col-lg-3"><div class="nin-eco__card"><h3>Cloud</h3><ul><li>AWS IoT Core</li><li>Azure IoT</li><li>Tuya Cloud</li></ul></div></div>
      <div class="col-md-6 col-lg-3"><div class="nin-eco__card"><h3>Data &amp; APIs</h3><ul><li>MQTT</li><li>REST API</li><li>Custom dashboards</li></ul></div></div>
      <div class="col-md-6 col-lg-3"><div class="nin-eco__card"><h3>Utility standards</h3><ul><li>DLMS / COSEM</li><li>IS 16444 metering</li><li>Wi-SUN FAN</li></ul></div></div>
      <div class="col-md-6 col-lg-3"><div class="nin-eco__card"><h3>Wireless</h3><ul><li>LoRaWAN</li><li>Zigbee / Thread / Matter</li><li>BLE, Wi-Fi, 4G LTE</li></ul></div></div>
    </div>
    <div class="nin-partners"><span>Official technology partners</span><img src="assets/images/Semtech.png" alt="Semtech" width="120" height="40" loading="lazy"><img src="assets/images/SLabs.png" alt="Silicon Labs" width="120" height="40" loading="lazy"></div>
  </div>
</section>

"""

# ---------------------------------------------------------------- scripts
tail = re.sub(r"<script>\s*new Swiper\('\.nbl-hero__bg-slider', \{(.*?)\}\);\s*</script>",
              lambda m: "<script>\nif (window.Swiper) {\n  new Swiper('.nbl-hero__bg-slider', {" + m.group(1) + "});\n}\n</script>", tail, count=1, flags=re.S)
catalog = [{'slug': p['slug'], 'name': re.sub(r'\s*\(.*?\)|\s+—.*$', '', p['name']).strip(), 'type': p['type_label'], 'proto': p['proto_label'], 'img': p['image'], 'tag': p['tagline']} for p in PROD if p['type_key'] != 'filter']
tail = tail.replace('</body>', '<script>window.NIN_CATALOG=' + json.dumps(catalog, ensure_ascii=False, separators=(',', ':')) + ';</script>\n<script src="./assets/js/index-new.js" defer></script>\n</body>', 1)

nav = '''<nav class="nin-subnav" id="ninSubnav" aria-label="On this page" hidden>
  <div class="container"><ul>
    <li><a href="#technologies">Protocols</a></li><li><a href="#compare">Compare</a></li><li><a href="#products">Products</a></li><li><a href="#finder">Find a product</a></li>
    <li><a href="#industries">Industries</a></li><li><a href="#process">How we work</a></li><li><a href="#why-nebulae">Why Nebulae</a></li><li><a href="#sample">Sample kit</a></li><li><a href="#cta">Contact</a></li>
  </ul></div>
</nav>
<button type="button" class="nin-top" id="ninTop" aria-label="Back to top" hidden><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
'''
wave = lambda c: '<div class="nin-wave nin-wave--%s" aria-hidden="true"><svg viewBox="0 0 1440 90" preserveAspectRatio="none"><path d="M0,40 C260,95 500,5 760,50 C1000,92 1220,15 1440,48 L1440,90 L0,90 Z"/></svg></div>\n' % c
compare_sec = compare.replace('<section class="nbl-compare-section" id="compare">', '<section class="nbl-compare-section nin-compare" id="compare">', 1)
out = top + hero + nav + logos + stats_sec + tech + compare_sec + prod_html + finder + ind_html + process + why + eco + expertise + deeper + sample + cta + newsletter + tail
open('index-new.html', 'w', encoding='utf-8').write(out)
print('index-new.html written:', len(out) // 1024, 'KB (index.html is', len(src) // 1024, 'KB)')
