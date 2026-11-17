#!/usr/bin/env python3
"""test_listing.py — QA for products.html (needs playwright). Checks console errors, overflow at 5 widths, filters, search, URL params, empty state."""
import sys, os, functools, http.server, socketserver, threading
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BS = next((c for c in (os.path.join(ROOT, 'node_modules/bootstrap/dist/'), '/home/claude/build/node_modules/bootstrap/dist/') if os.path.exists(c + 'css/bootstrap.min.css')), None)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
def route(r):
    u = r.request.url
    if BS and 'bootstrap.min.css' in u: r.fulfill(path=BS + 'css/bootstrap.min.css', content_type='text/css')
    elif BS and 'bootstrap.bundle' in u: r.fulfill(path=BS + 'js/bootstrap.bundle.min.js', content_type='application/javascript')
    elif BS and 'fonts.g' in u: r.fulfill(body='', content_type='text/css')
    else: r.continue_()
issues = []; base = f'http://127.0.0.1:{port}/products.html'
OVER = "[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>document.documentElement.clientWidth+1&&!e.closest('.atl-mega,.atl-nav__mobile,.atl-sticky-header,#nblBackTop,.atl-brochure-menu,#nblProgressBar')}).slice(0,4).map(e=>e.className+'|'+e.tagName)"
def vis(pg): return pg.evaluate("[...document.querySelectorAll('.pl-card')].filter(c=>!c.hidden).length")
with sync_playwright() as p:
    b = p.chromium.launch()
    for (w, h) in [(1440, 900), (1024, 800), (768, 900), (390, 844), (320, 700)]:
        ctx = b.new_context(viewport={'width': w, 'height': h}); pg = ctx.new_page(); errs = []
        pg.on('console', lambda m: errs.append(m.text) if m.type in ('error', 'warning') else None)
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('response', lambda r: errs.append(f'HTTP {r.status} {r.url}') if r.status >= 400 else None)
        pg.route('**/*', route); pg.goto(base); pg.wait_for_timeout(500)
        pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(400)
        r = pg.evaluate("({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,broken:[...document.images].filter(i=>i.getAttribute('src')&&i.complete&&i.naturalWidth===0).map(i=>i.src),over:" + OVER + "})")
        if r['sw'] > r['cw']: issues.append(f'{w}px h-scroll')
        if r['broken']: issues.append(f'{w}px broken imgs {r["broken"][:3]}')
        if r['over']: issues.append(f'{w}px overflow {r["over"]}')
        if errs: issues.append(f'{w}px console/net {errs[:3]}')
        if w == 1440:
            total = vis(pg)
            if total < 20: issues.append(f'only {total} cards')
            pg.click('.pl-chip[data-group="proto"][data-value="wisun"]'); wis = vis(pg)
            if not (0 < wis < total): issues.append('protocol filter')
            pg.click('.pl-chip[data-group="type"][data-value="gateway"]'); both = vis(pg)
            if not (0 < both <= wis): issues.append('type filter')
            if 'proto=wisun' not in pg.url or 'type=gateway' not in pg.url: issues.append('url sync')
            pg.click('#plClear'); 
            if vis(pg) != total: issues.append('clear')
            pg.fill('#plSearch', 'sigfox'); pg.wait_for_timeout(300)
            if not (0 < vis(pg) < total): issues.append('search')
            pg.fill('#plSearch', 'zzzzqq'); pg.wait_for_timeout(300)
            if vis(pg) != 0 or pg.is_hidden('#plEmpty'): issues.append('empty state')
            pg.click('#plEmptyClear')
            if vis(pg) != total: issues.append('empty clear')
            pg.goto(base + '?proto=lora&type=gateway'); pg.wait_for_timeout(300)
            if vis(pg) < 3 or pg.get_attribute('.pl-chip[data-group="type"][data-value="gateway"]', 'aria-pressed') != 'true': issues.append('url params')
            pg.goto(base + '?type=cloud'); pg.wait_for_timeout(300)
            if vis(pg) != 0 or pg.is_hidden('#plEmpty'): issues.append('unknown category state')
            pg.goto(base); pg.wait_for_timeout(300)
            href = pg.get_attribute('.pl-card a.pl-card__cta', 'href'); pg.click('.pl-card a.pl-card__cta'); pg.wait_for_timeout(500)
            if '/products/' not in pg.url: issues.append('card link ' + href)
        ctx.close()
    b.close()
print('PASS products.html' if not issues else 'FAIL products.html ' + str(issues)); sys.exit(1 if issues else 0)
