#!/usr/bin/env python3
"""Events: tools/events_data.json  ->  (1) news-events.html (single listing, filter All/Upcoming/Past)
(2) one detail page per event: event-<slug>.html.  Then rebuilds news-events.html.
Rules: schedule for all events; FAQ only for upcoming events; gallery only for past events; brochure for both;
every optional field simply hides its section when empty. Add an event = add an object to events_data.json,
run this, then apply_index_header.py / apply_shared_assets.py."""
import json, re, os, html, subprocess, sys, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
E_ = lambda s: html.escape(str(s), quote=True)
events = json.load(open(os.path.join(ROOT, 'tools/events_data.json'), encoding='utf-8'))
ARR = '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg>'
def url(e): return f'event-{e["slug"]}.html'
def blurb(e, n=150):
    t = e['about']; return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'
def card(e):
    booth = f' &nbsp;·&nbsp; Booth {E_(e["boothNumber"])}' if e.get('tag') == 'Exhibitor' and e.get('boothNumber') else ''
    st = ('past', 'Past', '100,116,139', '#64748b') if e['isPast'] else ('upcoming', 'Upcoming', '16,185,129', '#059669')
    return f'''<div class="col-md-6 col-lg-4 ne-item" data-status="{st[0]}"><div class="pg-card">
<a href="{url(e)}" tabindex="-1" aria-hidden="true"><img src="{E_(e["image"])}" alt="{E_(e["name"])}" class="pg-card__img" loading="lazy" width="540" height="390"/></a>
<div class="pg-card__body"><div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:.6rem;">
<span class="pg-card__tag" style="background:rgba(79,70,229,.1);color:#4f46e5;">{E_(e.get("type", "Event"))}</span>
<span class="pg-card__tag" style="background:rgba({st[2]},.12);color:{st[3]};">{st[1]}</span></div>
<h3 class="pg-card__title"><a href="{url(e)}" style="color:inherit;text-decoration:none;">{E_(e["name"])}</a></h3>
<p class="pg-card__desc">{E_(blurb(e))}</p>
<div class="pg-card__meta">📅 {E_(e["date"])} &nbsp;·&nbsp; 📍 {E_(e["location"])}{booth}</div>
<a href="{url(e)}" class="pg-card__link">{'Meet Us' if not e['isPast'] else 'View Details'} {ARR}</a></div></div></div>'''
up = [e for e in events if not e['isPast']]; past = [e for e in events if e['isPast']]
ordered = up + past
hero = '''<section class="pg-hero pg-hero--img"><div class="pg-hero__bg" style="background-image:url(assets/images/events/events-listing-hero.webp)"></div>
<div class="container" style="position:relative;z-index:2;"><nav class="pg-breadcrumb"><a href="index.html">Home</a><span>›</span><span>News &amp; Events</span></nav>
<div class="pg-eyebrow">News &amp; Events</div><h1 class="pg-hero__title">News <span>&amp; Events</span></h1>
<p class="pg-hero__desc">Where to meet the Nebulae team — exhibitions, conferences and company updates.</p></div></section>'''
filters = f'''<div class="ne-tabs" role="group" aria-label="Filter events"><button type="button" class="ne-tab active" data-f="all" aria-pressed="true">All ({len(ordered)})</button>
<button type="button" class="ne-tab" data-f="upcoming" aria-pressed="false">Upcoming ({len(up)})</button><button type="button" class="ne-tab" data-f="past" aria-pressed="false">Past ({len(past)})</button></div>'''
body = hero + f'<section class="pg-section"><div class="container">{filters}<div class="row g-4 mt-1" id="neGrid">{"".join(card(e) for e in ordered)}</div></div></section>\n'
filter_js = '''<script>
(function(){var bs=document.querySelectorAll('.ne-tab'),it=document.querySelectorAll('.ne-item');
function f(v){bs.forEach(function(b){var on=b.dataset.f===v;b.classList.toggle('active',on);b.setAttribute('aria-pressed',on);});it.forEach(function(i){i.style.display=(v==='all'||i.dataset.status===v)?'':'none';});}
bs.forEach(function(b){b.addEventListener('click',function(){f(b.dataset.f);});});})();
</script>'''
shell = rd('tools/templates/news_events_shell.html')
T = 'News &amp; Events | Nebulae IoT — Exhibitions, Conferences &amp; Updates'
D = 'Upcoming and past events where the Nebulae team exhibits or speaks — EFY Expo Gujarat 2026, Smart Meter Summit and more.'
shell = re.sub(r'<title>.*?</title>', f'<title>{T}</title>', shell, flags=re.S)
for pat in (r'(<meta name="description" content=")[^"]*', r'(<meta property="og:description" content=")[^"]*', r'(<meta name="twitter:description" content=")[^"]*'):
    shell = re.sub(pat, lambda m: m.group(1) + D, shell)
wr('news-events.html', shell.replace('<!--NE_BODY-->', body).replace('<!--NE_TABJS-->', filter_js))
# ---- detail pages
sh = rd('tools/templates/event_detail_shell.html')
GALJS = '''<script>
(function(){
  var g=document.getElementById('evGallery'); if(!g) return;
  var items=[].slice.call(g.querySelectorAll('.ev-g-item')), lb=document.getElementById('evLb'), img=document.getElementById('evLbImg'), cap=document.getElementById('evLbCap'), cur=0, last=null;
  var more=document.getElementById('evGalMore');
  if(more) more.addEventListener('click',function(){ items.forEach(function(i){i.hidden=false;}); more.parentNode.removeChild(more); });
  function show(i){ cur=(i+items.length)%items.length; var im=items[cur].querySelector('img'); img.src=im.src; img.alt=im.alt; cap.textContent=(cur+1)+' / '+items.length; }
  function open(i){ last=document.activeElement; show(i); lb.hidden=false; document.body.style.overflow='hidden'; document.getElementById('evLbX').focus(); }
  function close(){ lb.hidden=true; document.body.style.overflow=''; if(last) last.focus(); }
  items.forEach(function(b,i){ b.addEventListener('click',function(){ open(i); }); });
  document.getElementById('evLbX').addEventListener('click',close);
  document.getElementById('evLbP').addEventListener('click',function(){ show(cur-1); });
  document.getElementById('evLbN').addEventListener('click',function(){ show(cur+1); });
  lb.addEventListener('click',function(e){ if(e.target===lb) close(); });
  document.addEventListener('keydown',function(e){ if(lb.hidden) return; if(e.key==='Escape') close(); else if(e.key==='ArrowLeft') show(cur-1); else if(e.key==='ArrowRight') show(cur+1); else if(e.key==='Tab'){ var f=[].slice.call(lb.querySelectorAll('button')); var a=document.activeElement,k=f.indexOf(a); if(e.shiftKey&&k<=0){e.preventDefault();f[f.length-1].focus();} else if(!e.shiftKey&&k===f.length-1){e.preventDefault();f[0].focus();} } });
  var x0=null; lb.addEventListener('touchstart',function(e){ x0=e.touches[0].clientX; },{passive:true});
  lb.addEventListener('touchend',function(e){ if(x0===null) return; var d=e.changedTouches[0].clientX-x0; if(Math.abs(d)>50) show(cur+(d<0?1:-1)); x0=null; });
})();
</script>'''
def chips(l): return ''.join(f'<span style="display:inline-block;background:#eef2ff;color:#4338ca;border:1px solid #c7d2fe;border-radius:100px;padding:.4rem .95rem;font-size:.82rem;font-weight:700;margin:0 .45rem .55rem 0;">{E_(x)}</span>' for x in l)
def sidebar_row(k, v): return f'<div style="padding:.7rem 0;border-bottom:1px solid #eef0f5;"><div style="font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#9ca3af;">{k}</div><div style="font-size:.92rem;font-weight:600;color:#111827;margin-top:.15rem;">{v}</div></div>'
for e in events:
    st = 'Past Event' if e['isPast'] else 'Upcoming'
    stc = ('rgba(148,163,184,.2)', 'rgba(148,163,184,.4)', '#cbd5e1') if e['isPast'] else ('rgba(16,185,129,.2)', 'rgba(16,185,129,.3)', '#34d399')
    ctas = '<button type="button" class="pg-btn-outline" id="evShare" style="cursor:pointer;">Share</button>'
    ctas = (f'<a href="contact.html?inquiry=meeting&amp;topic={urllib.parse.quote(e["name"])}" class="pg-btn-primary">{"Book a Meeting" if not e["isPast"] else "Talk to Us"} {ARR}</a>') + \
           (f'<a href="{E_(e["brochure"])}" class="pg-btn-outline" target="_blank" rel="noopener">Brochure</a>' if e.get('brochure') and e['brochure'] != '#' else '') + ctas
    main = ''
    main += f'<span class="pg-section-eyebrow">About the Event</span><h2 class="pg-section-title" style="font-size:1.8rem;">{E_(e["name"])}</h2><p style="font-size:1rem;line-height:1.85;color:#4b5563;">{E_(e["about"])}</p>'
    if e.get('showcase'):
        main += f'<h3 style="font-size:1.1rem;font-weight:800;color:#111827;margin:2rem 0 .9rem;">{"On Display" if not e["isPast"] else "What We Showcased"}</h3>{chips(e["showcase"])}'
    if e.get('schedule'):
        items = ''.join(f'<div class="pg-timeline-item"><div class="pg-timeline-time">{E_(d["day"])}</div>' + ''.join(f'<div class="pg-timeline-title">{E_(i["time"])} — {E_(i["activity"])}</div>' for i in d['items']) + '</div>' for d in e['schedule'])
        main += f'<span class="pg-section-eyebrow" style="margin-top:2.5rem;display:block;">Event Schedule</span><h2 class="pg-section-title" style="font-size:1.8rem;">Schedule</h2><div class="pg-timeline mt-4">{items}</div>'
    if e['isPast'] and e.get('gallery'):
        g = e['gallery']; n = len(g); LIM = 8
        tiles = ''.join(f'<button type="button" class="ev-g-item{" ev-g-extra" if i >= LIM else ""}" data-i="{i}" aria-label="Open photo {i + 1} of {n}"{" hidden" if i >= LIM else ""}><img src="{E_(x["src"])}" alt="{E_(x.get("alt", e["name"]))} — photo {i + 1}" loading="lazy" width="400" height="400"/></button>' for i, x in enumerate(g))
        more = f'<div class="text-center mt-3"><button type="button" class="pg-btn-outline" id="evGalMore" style="color:#4f46e5;border-color:#c7d2fe;">View all {n} photos</button></div>' if n > LIM else ''
        main += f'<span class="pg-section-eyebrow" style="margin-top:2.5rem;display:block;">Gallery</span><h2 class="pg-section-title" style="font-size:1.8rem;">Event Photos <small style="font-size:.9rem;color:#9ca3af;font-weight:600;">· {n} photos</small></h2><div class="ev-gallery" id="evGallery">{tiles}</div>{more}'
        lightbox = '<div class="ev-lb" id="evLb" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden><button type="button" class="ev-lb__x" id="evLbX" aria-label="Close">×</button><button type="button" class="ev-lb__nav ev-lb__prev" id="evLbP" aria-label="Previous photo">‹</button><figure class="ev-lb__fig"><img id="evLbImg" alt=""/><figcaption id="evLbCap"></figcaption></figure><button type="button" class="ev-lb__nav ev-lb__next" id="evLbN" aria-label="Next photo">›</button></div>'
        main += lightbox
    if e.get('team'):
        main += '<span class="pg-section-eyebrow" style="margin-top:2.5rem;display:block;">Our Team</span><div class="row g-3 mt-1">' + ''.join(f'<div class="col-md-4"><div style="border:1.5px solid #e5e7eb;border-radius:16px;padding:1.25rem;text-align:center;"><strong>{E_(t["name"])}</strong><div style="font-size:.82rem;color:#4f46e5;">{E_(t.get("role", ""))}</div></div></div>' for t in e['team']) + '</div>'
    if not e['isPast'] and e.get('faq'):
        main += '<span class="pg-section-eyebrow" style="margin-top:2.5rem;display:block;">FAQ</span><h2 class="pg-section-title" style="font-size:1.8rem;">Visitor Questions</h2><div class="mt-3">' + ''.join(f'<details style="border:1.5px solid #e5e7eb;border-radius:14px;padding:1rem 1.25rem;margin-bottom:.75rem;background:#fff;"><summary style="font-weight:700;color:#111827;cursor:pointer;">{E_(f["q"])}</summary><p style="margin:.75rem 0 0;color:#4b5563;line-height:1.75;">{E_(f["a"])}</p></details>' for f in e['faq']) + '</div>'
    side = sidebar_row('Date', E_(e['date'])) + sidebar_row('Location', E_(e['location']))
    if e.get('venue'): side += sidebar_row('Venue', E_(e['venue']))
    if e['tag'] == 'Exhibitor' and e.get('boothNumber'): side += sidebar_row('Booth', E_(e['boothNumber']))
    side += sidebar_row('Type', E_(e['tag']))
    mapb = f'<div style="margin-top:1.5rem;border-radius:16px;overflow:hidden;border:1.5px solid #e5e7eb;"><iframe src="{E_(e["mapUrl"])}" width="100%" height="260" style="border:0;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map: {E_(e.get("venue", e["location"]))}"></iframe></div>' if e.get('mapUrl') and e['mapUrl'] != '#' else ''
    page = f'''<section class="pg-hero pg-hero--img" style="padding:4.5rem 0 3.5rem;"><div class="pg-hero__bg" style="background-image:url({E_(e.get("banner", ""))})"></div>
<div class="container" style="position:relative;z-index:2;"><nav class="pg-breadcrumb"><a href="index.html">Home</a><span>›</span><a href="news-events.html#events">News &amp; Events</a><span>›</span><span style="color:rgba(255,255,255,.65);">{E_(e["name"])}</span></nav>
<div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1rem;flex-wrap:wrap;"><span style="background:rgba(79,70,229,.2);border:1px solid rgba(79,70,229,.4);color:#a5b4fc;font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:.3rem .85rem;border-radius:100px;">{E_(e["tag"])}</span>
<span style="color:rgba(255,255,255,.6);font-size:.82rem;">{E_(e["date"])} · {E_(e["location"])}</span>
<span style="background:{stc[0]};border:1px solid {stc[1]};color:{stc[2]};font-size:.72rem;font-weight:700;padding:.3rem .85rem;border-radius:100px;">{st}</span></div>
<h1 class="pg-hero__title" style="font-size:clamp(1.8rem,4vw,3rem);">{E_(e["name"])}</h1>
<p class="pg-hero__desc">{E_(blurb(e, 200))}</p><div style="display:flex;gap:.85rem;flex-wrap:wrap;">{ctas}</div></div></section>
<section class="pg-section"><div class="container"><div class="row g-5"><div class="col-lg-8">{main}</div>
<div class="col-lg-4"><div style="background:#f8f9ff;border:1.5px solid #e5e7eb;border-radius:18px;padding:1.5rem;"><p style="font-size:.85rem;font-weight:800;color:#111827;margin:0 0 .5rem;text-transform:uppercase;letter-spacing:.08em;">Event Details</p>{side}</div>{mapb}</div></div></div></section>
<script>(function(){{var b=document.getElementById('evShare');if(!b)return;b.addEventListener('click',function(){{var d={{title:document.title,url:location.href}};if(navigator.share){{navigator.share(d).catch(function(){{}});}}else if(navigator.clipboard){{navigator.clipboard.writeText(location.href).then(function(){{b.textContent='Link copied';setTimeout(function(){{b.textContent='Share';}},2000);}});}}}});}})();</script>''' + (GALJS if (e['isPast'] and e.get('gallery')) else '')
    canon = f'https://www.nebulae.io/{url(e)}'
    title = f'{e["name"]} — Nebulae Event'; desc = blurb(e, 155)
    s = re.sub(r'<title>.*?</title>', f'<title>{E_(title)}</title>', sh, flags=re.S)
    for pat in (r'(<meta name="description" content=")[^"]*', r'(<meta property="og:description" content=")[^"]*', r'(<meta name="twitter:description" content=")[^"]*'):
        s = re.sub(pat, lambda m: m.group(1) + E_(desc), s)
    for pat in (r'(<meta property="og:title" content=")[^"]*', r'(<meta name="twitter:title" content=")[^"]*'):
        s = re.sub(pat, lambda m: m.group(1) + E_(title), s)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + canon, s); s = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + canon, s)
    s = re.sub(r'"name": "[^"]*", "item": "https://www.nebulae.io/event-detail.html"', f'"name": "{E_(e["name"])}", "item": "{canon}"', s)
    wr(url(e), s.replace('<!--EV_BODY-->', page))
print('events built:', [url(e) for e in events])
