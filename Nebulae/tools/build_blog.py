#!/usr/bin/env python3
"""Builds blog.html + the three article pages from the existing nebulae.io blog.
Posts are the full text from https://www.nebulae.io/Home/Blogs (source URL kept in each page).
Then run apply_index_header.py / apply_shared_assets.py."""
import re, os, html
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
BASE = 'https://www.nebulae.io/Home/blogs-post?title='
POSTS = [
 dict(file='blog-nebulae-iot-platform.html', src_html='iot-platform', title="Nebulae's IoT Platform Clubs Ease of Deployment, Interoperability and Efficiency",
  date='23 May 2022', author='Rachana Patel', role='Nebulae', cat='IoT', col=('79,70,229', '#4f46e5'),
  img='assets/images/blog/internet-of-things.png', src=BASE + 'Nebulaes_IoT_Platform_Clubs_Ease_of_Deployment_Interoperability_and_Efficiency&p=F'),
 dict(file='blog-industry-4-0-smart-manufacturing.html', src_html='industry-4-0', title='Industry Standard 4.0 and Smart Manufacturing',
  date='24 May 2022', author='Nebulae Team', role='Nebulae', cat='Industry 4.0', col=('217,119,6', '#d97706'),
  img='assets/images/blog/industry-4-0.png', src=BASE + 'Industry_Standard_40_and_Smart_Manufacturing&p=F'),
 dict(file='blog-understanding-smart-metering.html', src_html='smart-metering', title='Understanding Smart Metering & its uses',
  date='30 Jun 2022', author='Nebulae Team', role='Nebulae', cat='Smart Metering', col=('6,182,212', '#0891b2'),
  img='assets/images/blog/smart-metering.png', src=BASE + 'Understanding_Smart_Metering_its_uses&p=F'),
]
def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:40]
def clean(raw):
    """Original nebulae.io article HTML -> site markup (text kept verbatim; headings become h2 with ids)."""
    b = re.sub(r'</?span>', '', raw).replace('&nbsp;', ' ')
    heads = []
    def h(t):
        t = re.sub(r'\s+', ' ', t).strip().rstrip('-').strip(); i = slug(t); heads.append((i, t)); return f'<h2 id="{i}">{t}</h2>'
    b = re.sub(r'<blockquote>\s*<p>\s*(?:<strong>)?(.*?)(?:</strong>)?\s*</p>\s*</blockquote>', lambda m: h(m.group(1)), b, flags=re.S)
    b = re.sub(r'<p>\s*<strong>(.*?)</strong>\s*</p>', lambda m: h(m.group(1)), b, flags=re.S)
    b = re.sub(r'<p>\s*</p>', '', b)
    b = b.replace('<p>', '<p id="intro">', 1)
    b = re.sub(r'<li>\s*', '<li>', b)
    return b.strip(), [('intro', 'Introduction')] + heads
for p in POSTS:
    raw = rd('tools/templates/blog_src/' + p['src_html'] + '.html')
    p['body'], p['toc'] = clean(raw)
    text = re.sub(r'<[^>]+>', ' ', raw).replace('&nbsp;', ' ')
    words = len(text.split()); p['read'] = f'{max(2, round(words / 200))} min read'
    first = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', re.search(r'<p>(.*?)</p>', raw, re.S).group(1)).replace('&nbsp;', ' ')).strip()
    p['desc'] = (first[:157].rsplit(' ', 1)[0] + '…') if len(first) > 160 else first
def tag(p): return f'<span class="pg-card__tag" style="background:rgba({p["col"][0]},.1);color:{p["col"][1]};">{p["cat"]}</span>'
def esc(s): return html.escape(s, quote=True)
CAL = '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
ARR = '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg>'
def card(p, col='col-md-6 col-lg-4'):
    return f'''<div class="{col}"><div class="pg-card">
<a href="{p["file"]}" class="pg-card__imglink" tabindex="-1" aria-hidden="true" style="display:block;"><img src="{p["img"]}" alt="{esc(p["title"])}" class="pg-card__img" loading="lazy" width="840" height="320"/></a>
<div class="pg-card__body">{tag(p)}
<h3 class="pg-card__title"><a href="{p["file"]}" style="color:inherit;text-decoration:none;">{esc(p["title"])}</a></h3>
<p class="pg-card__desc">{esc(p["desc"])}</p>
<div class="pg-card__meta">{CAL} {p["date"]} &nbsp;·&nbsp; {p["read"]}</div>
<a href="{p["file"]}" class="pg-card__link">Read More {ARR}</a>
</div></div></div>'''
def head(shell, title, desc, canon, kind='website'):
    s = re.sub(r'<title>.*?</title>', f'<title>{esc(title)}</title>', shell, flags=re.S)
    s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + esc(desc), s)
    s = re.sub(r'(<meta property="og:(?:title)" content=")[^"]*', lambda m: m.group(1) + esc(title), s)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + esc(desc), s)
    s = re.sub(r'(<meta name="twitter:title" content=")[^"]*', lambda m: m.group(1) + esc(title), s)
    s = re.sub(r'(<meta name="twitter:description" content=")[^"]*', lambda m: m.group(1) + esc(desc), s)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + canon, s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + canon, s)
    s = re.sub(r'(<meta property="og:type" content=")[^"]*', lambda m: m.group(1) + kind, s)
    return s
# ---- article pages
ash = rd('tools/templates/blog_article_shell.html')
for p in POSTS:
    toc = ''.join(f'<li><a href="#{i}" class="pg-toc__link{" active" if k == 0 else ""}">{t}</a></li>' for k, (i, t) in enumerate(p['toc']))
    others = [q for q in POSTS if q is not p]
    related = ''.join(card(q, 'col-md-6') for q in others)
    initial = p['author'][0]
    body = f'''<section class="pg-hero" style="padding:4rem 0 3rem;"><div class="pg-hero__grid"></div><div class="pg-hero__orb pg-hero__orb--1"></div>
<div class="container" style="position:relative;z-index:2;"><nav class="pg-breadcrumb"><a href="index.html">Home</a><span>›</span><a href="blog.html">Blog</a><span>›</span><span style="color:rgba(255,255,255,.65);">Article</span></nav></div></section>
<section class="pg-section"><div class="container"><div class="row g-5">
<div class="col-lg-8"><div class="pg-detail-wrap">
<div class="pg-detail-header"><div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1rem;flex-wrap:wrap;">{tag(p)}<span style="font-size:.8rem;color:#9ca3af;">{p["date"]} · {p["read"]}</span></div>
<h1 class="pg-detail-title">{esc(p["title"])}</h1>
<div class="pg-detail-meta"><span>{p["author"]}</span><span>{p["date"]}</span></div></div>
<img src="{p["img"]}" alt="{esc(p["title"])}" class="pg-detail-cover" width="840" height="320"/>
<div class="pg-detail-body">
{p["body"]}
<p style="font-size:.82rem;color:#6b7280;margin-top:2rem;">Originally published on the Nebulae website — <a href="{p["src"]}" target="_blank" rel="noopener">view the original post</a>.</p>
</div>
<div class="pg-author-card"><div class="pg-author-card__avatar" style="background:linear-gradient(135deg,#4f46e5,#06b6d4);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:1.2rem;">{initial}</div>
<div><p class="pg-author-card__name">{p["author"]}</p><p class="pg-author-card__role">{p["role"]}</p></div></div>
</div></div>
<div class="col-lg-4"><div class="pg-toc"><p class="pg-toc__title">Contents</p><ul class="pg-toc__list">{toc}</ul></div>
<div style="margin-top:1.5rem;background:#f8f9ff;border:1.5px solid #e5e7eb;border-radius:16px;padding:1.5rem;">
<p style="font-size:.85rem;font-weight:800;color:#111827;margin-bottom:.85rem;text-transform:uppercase;letter-spacing:.08em;">Need Expert Advice?</p>
<p style="font-size:.83rem;color:#6b7280;line-height:1.65;margin-bottom:1rem;">Our IoT architects can help with your deployment.</p>
<a href="contact.html" class="pg-btn-primary" style="font-size:.84rem;padding:.7rem 1.25rem;">Talk to an Engineer</a></div></div>
</div></div></section>
<section class="pg-related-section"><div class="container"><h3 style="font-size:1.5rem;font-weight:800;color:#111827;margin-bottom:1.75rem;">More Articles</h3><div class="row g-4">{related}</div></div></section>'''
    page = head(ash, p['title'] + ' | Nebulae Blog', p['desc'], 'https://www.nebulae.io/' + p['file'], 'article')
    page = re.sub(r'"name": "[^"]*", "item": "https://www.nebulae.io/blog-detail.html"', f'"name": "{esc(p["title"])}", "item": "https://www.nebulae.io/{p["file"]}"', page)
    wr(p['file'], page.replace('<!--BA_BODY-->', body))
# ---- listing
lsh = rd('tools/templates/blog_list_shell.html')
hero = '''<section class="pg-hero"><div class="pg-hero__grid"></div><div class="pg-hero__orb pg-hero__orb--1"></div><div class="pg-hero__orb pg-hero__orb--2"></div>
<div class="container" style="position:relative;z-index:2;"><nav class="pg-breadcrumb"><a href="index.html">Home</a><span>›</span><span style="color:rgba(255,255,255,.65);">Blog</span></nav>
<div class="pg-eyebrow">Nebulae Blog</div><h1 class="pg-hero__title">Insights on <span>IoT &amp; Smart Metering</span></h1>
<p class="pg-hero__desc">Articles from the Nebulae team on IoT platforms, Industry 4.0 and smart metering.</p></div></section>'''
news = '''<div class="pg-newsletter mt-5"><div class="pg-newsletter__text"><h3>IoT Engineering Insights</h3><p>New articles from the Nebulae team, straight to your inbox.</p></div>
<div class="pg-newsletter__form"><input type="email" class="pg-newsletter__input" placeholder="your@email.com" aria-label="Email address"/><button class="pg-newsletter__btn">Subscribe</button></div></div>'''
lb = hero + '<section class="pg-section" id="latest"><div class="container"><div class="row g-4">' + ''.join(card(p) for p in reversed(POSTS)) + '</div>' + news + '</div></section>'
lp = head(lsh, 'Blog | Nebulae IoT — IoT Platforms, Industry 4.0 & Smart Metering', 'Articles from the Nebulae team on IoT platforms, Industry 4.0 and smart manufacturing, and smart metering (AMR / AMI).', 'https://www.nebulae.io/blog.html')
wr('blog.html', lp.replace('<!--BL_BODY-->', lb))
print('blog built:', [p['file'] for p in POSTS])
