# Nebulae Website — Release 1
## Page Inventory

| File                | Size   | Description                                      |
|---------------------|--------|--------------------------------------------------|
| index.html          | 406 KB | Landing page — hero, all sections, Tuya, CTA     |
| about.html          | 225 KB | About Us — story, team, timeline, certifications |
| contact.html        | 223 KB | Contact — form, offices, map, FAQ                |
| products.html       | 226 KB | Product catalogue — 24 products, filter, search  |
| product-detail.html | 233 KB | Product detail — NB-LRM-868 full spec page       |
| services.html       | 224 KB | Services — 9 services, process, tech stack       |
| solutions.html      | 237 KB | Solutions — 8 industries, comparison table       |
| blog.html           | 212 KB | Blog listing — 9 articles, filter, sidebar       |
| blog-detail.html    | 217 KB | Blog article — LoRa vs Wi-SUN deep-dive          |
| 404.html            | 179 KB | 404 error page — branded, with search            |

## Technical Notes
- All pages are **single-file HTML** — CSS + JS fully inlined, no external dependencies except Bootstrap CDN + Google Fonts
- All pages share the **same header and footer** extracted from the original Wiman/Nebulae source
- Body padding-top: 100px (desktop) / 64px (mobile) for fixed header
- All navigation JS (mega menu, mobile, brochure dropdown) included on every page

## Release 2 — Planned
- resources.html (downloads, datasheets)
- careers.html (job listings)
- privacy.html (privacy policy)
- admin.html (theme customiser — connects to all pages via localStorage)

---
Built with Nebulae brand colours: Navy #313185 · Cyan #06b6d4 · Electric #4f46e5
