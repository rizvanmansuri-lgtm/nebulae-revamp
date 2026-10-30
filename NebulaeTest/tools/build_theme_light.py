#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_theme_light.py — generates assets/css/theme-light.css, the LIGHT version of the site.

How it works
  1. Opens every page in headless Chromium and finds each *dark section* (dark gradient / solid background) outside the header and footer.
  2. Reads the computed colours of everything inside those sections and writes CSS that
       - swaps the section background to the light gradient  (#f8faff → #eef2ff → #f5f7ff),
       - turns white text into ink, light accent colours into readable darker ones, translucent-white cards into white cards,
       - keeps text that sits on coloured buttons / badges white.
  3. Adds the hand-designed light banner (assets/css/theme-light.base.css) and writes assets/css/theme-light.css.
Header and footer are never touched. The dark version is the default; the light file is only linked when the theme is 'light'
(python3 tools/apply_theme.py light | dark).  Re-run this script after content/section changes:  python3 tools/build_theme_light.py
Needs: pip install playwright (+ chromium) and the bootstrap files in tools/_bs (it falls back to the CDN if missing).
"""
import os, re, sys, glob, json, colorsys, functools, http.server, socketserver, threading
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep
BS = os.environ.get('NBL_BOOTSTRAP_DIR', '')          # folder containing css/bootstrap.min.css and js/bootstrap.bundle.min.js (optional)
STATE = ['active', 'is-active', 'current', 'selected', 'on', 'open', 'visible', 'in', 'is-visible', 'show', 'tab-current', 'content-current']
STATE_NOT = ''.join(f':not(.{c})' for c in STATE[:6]) + ':not([aria-selected="true"]):not([aria-pressed="true"])'

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

COLLECT = r"""
(STATE)=>{
 const num=s=>(s.match(/-?[\d.]+/g)||[]).map(Number);
 const rgba=c=>{const n=num(c);return n.length<3?null:{r:n[0],g:n[1],b:n[2],a:n.length>3?n[3]:1}};
 const lum=c=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)};
 const stopsOf=cs=>{const o=[];const b=rgba(cs.backgroundColor);if(b&&b.a>.85)o.push(b);const bi=cs.backgroundImage;
   if(bi&&bi!=='none'&&/gradient/.test(bi)){for(const m of bi.matchAll(/rgba?\([^)]+\)/g)){const c=rgba(m[0]);if(c&&c.a>.5)o.push(c)}}return o};
 const isDark=e=>{const cs=getComputedStyle(e);const s=stopsOf(cs);if(!s.length)return false;const r=e.getBoundingClientRect();
   return s.every(c=>lum(c)<.05)&&r.width>150&&r.height>30};
 const skip=e=>e.closest('header,footer,.atl-util-bar,.atl-sticky-header,.atl-footer,#nblFloatForm,#nblCookie,.nbl-form-toast,.nbl-sticky-cta,#nblBackTop,.atl-mega,.atl-nav__mobile');
 const UTIL=/^(h|w|m|p|d|g|gx|gy|col|row|container|text|bg|border|align|justify|flex|position|rounded|shadow|mt|mb|my|mx|py|px|pt|pb|order|offset|gap)(-|$)/;
 const cls=e=>[...e.classList].filter(c=>!STATE.includes(c)&&!UTIL.test(c));
 const styleSel=e=>{const st=(e.getAttribute('style')||'').replace(/\s+/g,' ').trim();const m=st.match(/background(?:-image)?\s*:\s*[^;]{0,60}/);return m?m[0].trim():null};
 const out=[];
 const all=[...document.body.querySelectorAll('*')].filter(e=>!skip(e));
 const darks=all.filter(isDark);
 const tops=darks.filter(e=>!darks.some(o=>o!==e&&o.contains(e)));
 const props=(e,pseudo)=>{const cs=getComputedStyle(e,pseudo);return{color:cs.color,bg:cs.backgroundColor,bgi:cs.backgroundImage,bc:cs.borderTopColor,bw:parseFloat(cs.borderTopWidth)||0,
   br:parseFloat(cs.borderTopLeftRadius)||0,filter:cs.filter,clip:cs.webkitBackgroundClip||cs.backgroundClip,fill:cs.webkitTextFillColor,stroke:cs.stroke,svgfill:cs.fill,content:cs.content,shadow:cs.boxShadow,ts:cs.textShadow,op:cs.opacity}};
 const effBg=(e,c)=>{let n=e;while(n&&n!==c){const cs=getComputedStyle(n);const b=rgba(cs.backgroundColor);
    if(b&&b.a>.5)return{kind:'solid',lum:lum(b),c:b};
    const bi=cs.backgroundImage;if(bi&&/gradient/.test(bi)){const st=[...bi.matchAll(/rgba?\([^)]+\)/g)].map(m=>rgba(m[0])).filter(x=>x&&x.a>.5);
      if(st.length)return{kind:'grad',lum:Math.max(...st.map(lum)),c:st[0]}}
    n=n.parentElement}return null};
 for(const c of tops){
   const base=cls(c);const ss=styleSel(c);
   if(!base.length&&!ss){out.push({warn:'dark container without class or inline background: '+c.tagName+'#'+c.id});continue}
   let sel=(base.length?'.'+base.join('.'):c.tagName.toLowerCase());
   if(ss&&(!base.length||document.querySelectorAll(sel).length>document.querySelectorAll(sel+'[style*="'+ss.replace(/"/g,'\\"')+'"]').length))sel+='[style*="'+ss.replace(/"/g,'\\"')+'"]';
   const r=c.getBoundingClientRect();
   const rec={sel,tag:c.tagName.toLowerCase(),w:Math.round(r.width),h:Math.round(r.height),tl:(c.innerText||'').trim().length,stops:stopsOf(getComputedStyle(c)),own:props(c),items:[]};
   for(const d of c.querySelectorAll('*')){
     const tag=d.tagName.toLowerCase();if(tag==='script'||tag==='style'||tag==='noscript')continue;
     const dc=cls(d);let anc=null;let p=d.parentElement;while(p&&p!==c){const pc=cls(p);if(pc.length){anc='.'+pc.join('.');break}p=p.parentElement}
     const direct=[...d.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());
     const st=d.getAttribute('style')||'';
     const m=st.match(/(?:^|[;\s])color\s*:\s*[^;]+/);
     const isActive=STATE.some(s=>d.classList.contains(s))||d.getAttribute('aria-selected')==='true';
     const item={tag,cls:dc,anc,direct,active:isActive,inl:m?m[0].replace(/^[;\s]+/,''):null,hasStyle:!!st,p:props(d),
       b:props(d,'::before'),a:props(d,'::after'),eff:effBg(d,c),svg:!!d.closest('svg')};
     out.length;rec.items.push(item)}
   out.push(rec)}
 return out}
"""

def parse(c):
    n = [float(x) for x in re.findall(r'-?[\d.]+', c or '')]
    if len(n) < 3: return None
    return (n[0], n[1], n[2], n[3] if len(n) > 3 else 1.0)
def lum(rgb):
    f = lambda v: (v / 255 / 12.92) if v / 255 <= .03928 else (((v / 255) + .055) / 1.055) ** 2.4
    return .2126 * f(rgb[0]) + .7152 * f(rgb[1]) + .0722 * f(rgb[2])
def hls(rgb): return colorsys.rgb_to_hls(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
def hexc(r, g, b): return '#%02x%02x%02x' % (round(r), round(g), round(b))
def rgba_s(r, g, b, a): return f'rgba({round(r)},{round(g)},{round(b)},{round(a, 3):g})'

def ink(a):
    """white / light-neutral text → slate ink, keeping the original emphasis (alpha)"""
    return '#0f172a' if a >= .95 else '#1e293b' if a >= .78 else '#334155' if a >= .6 else '#475569' if a >= .45 else '#64748b'
def darken_chroma(c, cap=.31):
    h, l, s = hls(c); l = min(l, cap); s = max(s, .55) if s > .2 else s
    r, g, b = colorsys.hls_to_rgb(h, l, s); a = c[3]
    return hexc(r * 255, g * 255, b * 255) if a >= .99 else rgba_s(r * 255, g * 255, b * 255, a)
def map_text(color):
    c = parse(color)
    if not c or c[3] < .03: return None
    L = lum(c); h, l, s = hls(c)
    if L > .45 and s < .28: return ink(c[3])          # white / light grey
    if L > .2 and s >= .28: return darken_chroma(c)    # cyan, light indigo, light green …
    return None
def map_gradient(bgi):
    """darken the light stops of a text-clip gradient"""
    def f(m):
        c = parse(m.group(0))
        if c and lum(c) > .12:
            return darken_chroma(c, .36)
        return m.group(0)
    return re.sub(r'rgba?\([^)]+\)', f, bgi)
def has_white_alpha(s): return bool(re.search(r'rgba\(\s*255\s*,\s*255\s*,\s*255\s*,', s or ''))

def sel_for(rec, it, pseudo=''):
    base = rec['sel']
    if it['cls']:
        tail = it['tag'] + ''.join('.' + c for c in it['cls'])
        if it['tag'] in ('div', 'span', 'p', 'a', 'li', 'section') and it['cls']: tail = ''.join('.' + c for c in it['cls'])
        key = f"{base} {tail}"
    elif it['anc']:
        key = f"{base} {it['anc']} {it['tag']}"
    else:
        key = f"{base} {it['tag']}"
    if it['inl'] and not it['cls']: key += f'[style*="{it["inl"].split(":")[0].strip()}:{it["inl"].split(":",1)[1].strip()}"]'
    return key + pseudo

def main():
    rules = {}          # selector -> {prop: value}
    kinds = {}          # container selector -> kind
    warns = set()
    def put(sel, prop, val, text=False):
        if val is None: return
        rules.setdefault((sel, text), {})[prop] = val
    handler = functools.partial(Q, directory=ROOT)
    srv = socketserver.TCPServer(('127.0.0.1', 0), handler); port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    def route(r):
        u = r.request.url
        if BS and 'bootstrap.min.css' in u: r.fulfill(path=BS + '/css/bootstrap.min.css', content_type='text/css')
        elif BS and 'bootstrap.bundle' in u: r.fulfill(path=BS + '/js/bootstrap.bundle.min.js', content_type='application/javascript')
        elif 'fonts.g' in u: r.fulfill(body='', content_type='text/css')
        elif '127.0.0.1' in u: r.continue_()
        elif BS: r.abort()
        else: r.continue_()
    pages = sorted(glob.glob(ROOT + '*.html') + glob.glob(ROOT + '*/*.html'))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_context(viewport={'width': 1440, 'height': 900}).new_page(); pg.route('**/*', route)
        for f in pages:
            rel = os.path.relpath(f, ROOT)
            pg.goto(f'http://127.0.0.1:{port}/{rel}'); pg.wait_for_timeout(450)
            pg.evaluate("document.querySelectorAll('[class*=reveal],[data-anim]').forEach(e=>e.classList.add('visible','in','is-visible'))"); pg.wait_for_timeout(350)
            for rec in pg.evaluate(COLLECT, STATE):
                if 'warn' in rec: warns.add(rel + ': ' + rec['warn']); continue
                sel = rec['sel']
                # kind
                mx = max([max(s['r'], s['g'], s['b']) for s in rec['stops']] or [0])
                bl = max([s['b'] for s in rec['stops']] or [0])
                if rec['tl'] < 15 and not re.search(r'hero', sel): continue          # image overlays etc. stay as they are
                if re.search(r'hero|nf-wrap', sel): k = 'hero'
                elif rec['w'] < 700: k = 'card'
                elif bl >= 90: k = 'band'
                else: k = 'section'
                kinds[sel] = k
                # the container's own text colour (inherited by children)
                put(sel, 'color', map_text(rec['own']['color']) or None, True)
                for it in rec['items']:
                    P = it['p']; eff = it['eff']; skip_text = False
                    if eff:
                        L = eff['lum']; c = eff['c']; h, l, s = hls((c['r'], c['g'], c['b']))
                        if .035 <= L < .45 and s > .3 and (c['a'] if 'a' in c else 1) > .5: skip_text = True      # coloured button / badge: keep its white text
                    s_main = sel_for(rec, it)
                    # ---- text colour
                    if (it['direct'] or it['svg'] or True) and not it['active'] and not skip_text:
                        v = map_text(P['color'])
                        if v and (it['direct'] or P['content'] in ('none', 'normal')) and it['direct']:
                            put(s_main, 'color', v, True)
                        fill = P['fill']
                        if P['clip'] == 'text' and fill and parse(fill) and parse(fill)[3] < .1 and 'gradient' in P['bgi']:
                            put(s_main, 'background-image', map_gradient(P['bgi']), True)
                    # ---- svg
                    if it['svg']:
                        sv = P['stroke']; fl = P['svgfill']
                        if sv and sv != 'none' and parse(sv): put(s_main, 'stroke', map_text(sv))
                        if fl and fl != 'none' and parse(fl) and not skip_text: put(s_main, 'fill', map_text(fl))
                    # ---- backgrounds
                    bgc = parse(P['bg'])
                    cardish = P['br'] >= 8 or P['bw'] > 0
                    if bgc and bgc[3] > .02 and not it['active']:
                        if bgc[0] > 240 and bgc[1] > 240 and bgc[2] > 240 and bgc[3] <= .5 and not skip_text:
                            put(s_main, 'background-color', 'rgba(255,255,255,.72)')
                            if cardish: put(s_main, 'box-shadow', '0 6px 22px rgba(79,70,229,.08)')
                        elif lum(bgc) < .04 and bgc[3] > .3:
                            put(s_main, 'background-color', '#ffffff')
                            if cardish: put(s_main, 'box-shadow', '0 6px 22px rgba(79,70,229,.10)')
                    bgi = P['bgi']
                    if bgi and bgi != 'none' and 'gradient' in bgi and P['clip'] != 'text' and not it['active']:
                        sts = [parse(m.group(0)) for m in re.finditer(r'rgba?\([^)]+\)', bgi)]
                        sts = [x for x in sts if x]
                        if sts and has_white_alpha(bgi): put(s_main, 'background-image', re.sub(r'rgba\(\s*255\s*,\s*255\s*,\s*255\s*,', 'rgba(79,70,229,', bgi))
                        elif sts and all(lum(x) < .035 for x in sts if x[3] > .5) and any(x[3] > .5 for x in sts):
                            put(s_main, 'background-image', 'linear-gradient(135deg,#ffffff,#f1f5ff)')
                            if cardish: put(s_main, 'box-shadow', '0 6px 22px rgba(79,70,229,.10)')
                    # ---- borders
                    bc = parse(P['bc'])
                    if bc and P['bw'] > 0 and bc[3] > .02 and bc[0] > 240 and bc[1] > 240 and bc[2] > 240:
                        put(s_main, 'border-color', rgba_s(79, 70, 229, min(.3, bc[3] * .9 + .06)))
                    # ---- invert filters (white logos)
                    if 'invert' in (P['filter'] or ''): put(s_main, 'filter', 'none')
                    # ---- pseudo elements
                    for key, ps in (('b', '::before'), ('a', '::after')):
                        Q_ = it[key]
                        if Q_['content'] in ('none', 'normal', ''): continue
                        sp = sel_for(rec, it, ps)
                        v = map_text(Q_['color'])
                        if v and not skip_text and Q_['content'] not in ('""', "''") and Q_['content'].strip('"\'') != '': put(sp, 'color', v, True)
                        bq = parse(Q_['bg'])
                        if bq and bq[3] > .02 and bq[0] > 240 and bq[1] > 240 and bq[2] > 240: put(sp, 'background-color', rgba_s(79, 70, 229, min(.35, bq[3] * 1.4)))
                        elif bq and bq[3] > .3 and lum(bq) < .04: put(sp, 'background-color', '#ffffff')
                        if Q_['bgi'] and 'gradient' in Q_['bgi'] and has_white_alpha(Q_['bgi']):
                            put(sp, 'background-image', re.sub(r'rgba\(\s*255\s*,\s*255\s*,\s*255\s*,', 'rgba(79,70,229,', Q_['bgi']))
        b.close()
    # ---- emit
    out = ['/* theme-light.css — GENERATED by tools/build_theme_light.py (do not edit; edit theme-light.base.css and re-run). */']
    base = open(ROOT + 'assets/css/theme-light.base.css', encoding='utf-8').read()
    hero_sels = sorted(set([s for s, k in kinds.items() if k == 'hero'] + ['.pl-hero'])); sec = sorted(s for s, k in kinds.items() if k == 'section')
    band = sorted(s for s, k in kinds.items() if k == 'band'); card = sorted(s for s, k in kinds.items() if k == 'card')
    J = lambda l: ',\n'.join(l)
    base = base.replace('/*{HERO}*/', J(hero_sels) or '.__none').replace('/*{SECTION}*/', J(sec) or '.__none').replace('/*{BAND}*/', J(band) or '.__none').replace('/*{CARD}*/', J(card) or '.__none')
    out.append(base)
    # group selectors with identical declaration sets
    groups = {}
    for (sel, text), props in sorted(rules.items()):
        if not props: continue
        decl = ';'.join(f'{k}:{v}!important' for k, v in sorted(props.items()))
        # text-colour rules: stay out of the way of active/selected states
        s2 = sel
        if text and 'color' in props and not sel.endswith(('::before', '::after')):
            s2 = sel + STATE_NOT
        groups.setdefault(decl, []).append(s2)
    out.append('/* ───── generated: contents of the converted sections ───── */')
    for decl, sels in groups.items():
        out.append(',\n'.join(sels) + '{' + decl + '}')
    css = '\n'.join(out) + '\n'
    open(ROOT + 'assets/css/theme-light.css', 'w', encoding='utf-8').write(css)
    print(f'theme-light.css: {len(css)/1024:.0f} KB | sections {len(sec)}, bands {len(band)}, cards {len(card)}, heroes {len(hero_sels)}, rule groups {len(groups)}')
    for k in ('hero', 'section', 'band', 'card'): print(' ', k, [s for s, kk in kinds.items() if kk == k])
    for w in sorted(warns): print('  WARN', w)

if __name__ == '__main__':
    main()
