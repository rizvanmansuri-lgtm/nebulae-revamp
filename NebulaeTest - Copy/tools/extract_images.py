#!/usr/bin/env python3
"""
extract_images.py — pull every raster image out of a PDF, apply soft-mask
transparency, drop tiny/duplicate images, and write a labelled contact sheet.

Usage:  python3 tools/extract_images.py "<file.pdf>" <outdir> [--min 90]

Outputs in <outdir>:
  img_<n>_<W>x<H>.png   composited images (RGBA if the PDF had a soft mask)
  sheet.png             contact sheet with the image numbers, for choosing
  page_<p>.png          70-dpi render of each page (to see how images are used)
Then copy the chosen ones into assets/images/products/<slug>-<name>.<ext>
(use .jpg for photos on white, .png where transparency matters).
"""
import sys, os, subprocess, tempfile, hashlib, re, shutil
from PIL import Image, ImageDraw

def run(pdf, out, minpx=90):
    os.makedirs(out, exist_ok=True)
    lst = subprocess.run(['pdfimages', '-list', pdf], capture_output=True, text=True).stdout.splitlines()[2:]
    rows = []
    for l in lst:
        p = l.split()
        if len(p) < 11: continue
        rows.append(dict(page=int(p[0]), num=int(p[1]), type=p[2], w=int(p[3]), h=int(p[4]), obj=p[10]))
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdfimages', '-png', pdf, os.path.join(tmp, 'x')], check=True)
    files = sorted(os.listdir(tmp))
    by_num = {r['num']: os.path.join(tmp, f) for r, f in zip(rows, files)}
    masks = {r['obj']: by_num[r['num']] for r in rows if r['type'] == 'smask'}
    seen, kept = set(), []
    for r in rows:
        if r['type'] != 'image': continue
        if r['w'] < minpx or r['h'] < minpx: continue
        im = Image.open(by_num[r['num']]).convert('RGB')
        if r['obj'] in masks:
            m = Image.open(masks[r['obj']]).convert('L')
            if m.size != im.size: m = m.resize(im.size)
            im = im.convert('RGBA'); im.putalpha(m)
        h = hashlib.md5(im.tobytes()).hexdigest()
        if h in seen: continue
        seen.add(h)
        name = f"img_{r['num']:02d}_{im.width}x{im.height}.png"
        im.save(os.path.join(out, name), optimize=True)
        kept.append((r['num'], r['page'], name, im))
    # contact sheet
    cell, cols = 260, 4
    n = len(kept)
    if n:
        rowsn = (n + cols - 1) // cols
        sheet = Image.new('RGB', (cols * cell, rowsn * (cell + 22)), (200, 200, 200))
        d = ImageDraw.Draw(sheet)
        for i, (num, page, name, im) in enumerate(kept):
            t = im.copy(); t.thumbnail((cell - 10, cell - 10))
            bg = Image.new('RGB', t.size, (255, 255, 255))
            if t.mode == 'RGBA': bg.paste(t, mask=t.split()[3])
            else: bg = t.convert('RGB')
            x, y = (i % cols) * cell + 5, (i // cols) * (cell + 22) + 20
            sheet.paste(bg, (x, y))
            d.text((x, y - 16), f"#{num} p{page} {im.width}x{im.height}", fill=(0, 0, 0))
        sheet.save(os.path.join(out, 'sheet.png'))
    subprocess.run(['pdftoppm', '-r', '70', '-png', pdf, os.path.join(out, 'page')], check=False)
    shutil.rmtree(tmp)
    print(f"{os.path.basename(pdf)}: {len(kept)} usable images -> {out}")

if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    mp = 90
    if '--min' in a: mp = int(a[a.index('--min') + 1])
    run(a[0], a[1], mp)
