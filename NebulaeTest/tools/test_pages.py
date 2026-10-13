#!/usr/bin/env python3
"""
test_pages.py — browser QA for generated product pages (needs: pip install playwright; playwright install chromium)

Usage:  python3 tools/test_pages.py [slug ...] [--shots]
Checks per page at 1440/1024/768/390/320 px: console errors/warnings, page errors,
failed/4xx requests, broken <img>, horizontal overflow. Then on desktop: gallery thumbs,
lightbox, qty stepper, all 6 tabs (+ keyboard), copy-link, quote redirect, #hash deep-link.
--shots writes tools/shots/<slug>_{d,m}_<tab>.png for visual review.
If ./node_modules/bootstrap exists (npm i bootstrap@5.3.2) it is used instead of the CDN (offline sandboxes).
"""
import sys, os, json, functools, http.server, socketserver, threading
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BS = None
for c in (os.path.join(ROOT, 'node_modules/bootstrap/dist/'), '/home/claude/build/node_modules/bootstrap/dist/'):
    if os.path.exists(c + 'css/bootstrap.min.css'): BS = c; break
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
args = [a for a in sys.argv[1:] if not a.startswith('--')]; shots = '--shots' in sys.argv
slugs = args or [p['slug'] for p in json.load(open(os.path.join(ROOT, 'tools/products_index.json')))]
def route(r):
    u = r.request.url
    if BS and 'bootstrap.min.css' in u: r.fulfill(path=BS + 'css/bootstrap.min.css', content_type='text/css')
    elif BS and 'bootstrap.bundle' in u: r.fulfill(path=BS + 'js/bootstrap.bundle.min.js', content_type='application/javascript')
    elif 'fonts.g' in u and BS: r.fulfill(body='', content_type='text/css')
    else: r.continue_()
OVER = "[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>document.documentElement.clientWidth+1&&!e.closest('.pd-tabs-bar,.pd-specs-wrap,.atl-mega,.atl-nav__mobile,.atl-sticky-header,#nblBackTop,.pd-lightbox,.atl-brochure-menu,#nblProgressBar')}).slice(0,5).map(e=>e.className+'|'+e.tagName)"
fails = 0
with sync_playwright() as p:
    b = p.chromium.launch()
    for s in slugs:
        url = f'http://127.0.0.1:{port}/products/{s}.html'; issues = []
        for (w, h) in [(1440, 900), (1024, 800), (768, 900), (390, 844), (320, 700)]:
            ctx = b.new_context(viewport={'width': w, 'height': h}); pg = ctx.new_page(); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type in ('error', 'warning') else None)
            pg.on('pageerror', lambda e: errs.append('pageerror ' + str(e)))
            pg.on('requestfailed', lambda r: errs.append('failed ' + r.url) if 'fonts.g' not in r.url else None)
            pg.on('response', lambda r: errs.append(f'HTTP {r.status} {r.url}') if r.status >= 400 else None)
            pg.route('**/*', route); pg.goto(url, wait_until='load'); pg.wait_for_timeout(500)
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(300)
            r = pg.evaluate("({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,broken:[...document.images].filter(i=>i.getAttribute('src')&&i.complete&&i.naturalWidth===0).map(i=>i.src),over:" + OVER + "})")
            if r['sw'] > r['cw']: issues.append(f'{w}px h-scroll {r["sw"]}>{r["cw"]}')
            if r['broken']: issues.append(f'{w}px broken imgs {r["broken"]}')
            if r['over']: issues.append(f'{w}px overflow {r["over"]}')
            if errs: issues.append(f'{w}px console/net {errs[:3]}')
            ctx.close()
        ctx = b.new_context(viewport={'width': 1440, 'height': 900}); pg = ctx.new_page(); errs = []
        pg.on('console', lambda m: errs.append(m.text) if m.type in ('error', 'warning') else None); pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.route('**/*', route); pg.goto(url); pg.wait_for_timeout(400)
        n = pg.locator('[data-pd-thumb]').count()
        for i in range(n):
            pg.locator('[data-pd-thumb]').nth(i).click(); pg.wait_for_timeout(200)
            if not pg.evaluate("document.getElementById('pdMainImg').naturalWidth>0"): issues.append(f'thumb {i} not loading')
        pg.locator('[data-pd-zoom]').click(); pg.wait_for_timeout(200)
        if not pg.evaluate("document.getElementById('pdLightbox').classList.contains('open')&&document.getElementById('pdLightboxImg').naturalWidth>0"): issues.append('lightbox')
        pg.keyboard.press('Escape')
        pg.locator('[data-pd-qty="1"]').click(); pg.locator('[data-pd-qty="1"]').click()
        if pg.input_value('#pdQty') != '3': issues.append('qty stepper')
        for t in ['specs', 'features', 'docs', 'applications', 'ordering', 'overview']:
            pg.click(f'[data-tab="{t}"]')
            ok = pg.evaluate(f"(()=>{{const p=document.getElementById('pd-tab-{t}');return getComputedStyle(p).display!=='none'&&[...document.querySelectorAll('.pd-tab-panel')].filter(x=>x!==p&&getComputedStyle(x).display!=='none').length===0}})()")
            if not ok: issues.append('tab ' + t)
            if shots:
                os.makedirs(os.path.join(ROOT, 'tools/shots'), exist_ok=True)
                pg.add_style_tag(content='html{scroll-behavior:auto!important}')
                pg.locator('.pd-tabs-section').screenshot(path=os.path.join(ROOT, f'tools/shots/{s}_d_{t}.png'))
        pg.focus('[data-tab="overview"]'); pg.keyboard.press('ArrowRight')
        if pg.evaluate("document.querySelector('.pd-tab-btn.active').dataset.tab") != 'specs': issues.append('keyboard tabs')
        pg.context.grant_permissions(['clipboard-read', 'clipboard-write']); pg.click('[data-pd-copy]'); pg.wait_for_timeout(120)
        if 'Copied' not in pg.inner_text('[data-pd-copy]'): issues.append('copy link')
        if errs: issues.append(f'interaction console {errs[:2]}')
        pg.click('[data-pd-quote]'); pg.wait_for_timeout(300)
        if 'contact.html?product=' not in pg.url: issues.append('quote redirect')
        ctx.close()
        ctx = b.new_context(viewport={'width': 1440, 'height': 900}); pg = ctx.new_page(); pg.route('**/*', route)
        pg.goto(url + '#specs'); pg.wait_for_timeout(300)
        if pg.evaluate("document.querySelector('.pd-tab-btn.active').dataset.tab") != 'specs': issues.append('hash deep link')
        ctx.close()
        if shots:
            for (w, h, tag) in [(390, 844, 'm')]:
                ctx = b.new_context(viewport={'width': w, 'height': h}); pg = ctx.new_page(); pg.route('**/*', route); pg.goto(url); pg.wait_for_timeout(500)
                pg.screenshot(path=os.path.join(ROOT, f'tools/shots/{s}_m_top.png')); ctx.close()
        print(('PASS ' if not issues else 'FAIL ') + s, issues if issues else ''); fails += bool(issues)
    b.close()
sys.exit(1 if fails else 0)
