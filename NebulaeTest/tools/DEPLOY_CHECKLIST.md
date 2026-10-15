# Deploy checklist — Nebulae IoT
1. EmailJS: set PUBLIC_KEY (and confirm SERVICE_ID / template IDs; add quote + newsletter templates if wanted) at the top of `assets/js/nebulae-forms.js`. In the EmailJS dashboard allow your domain. See tools/EMAILJS_SETUP.md. Send one test from contact, newsletter and quote forms on the live site.
2. Paste the 32 PDFs into `assets/docs/` (names in assets/docs/README.md). Run `python3 tools/check_links.py` — it must report 0 missing.
3. Replace placeholder content: LoRaWAN Network Server page, IoT in Logistics page, team/awards/news/blog/events/careers.
4. Replace Unsplash stock images (hot-linked) with your own files if you need guaranteed availability/licensing.
5. Confirm the brochure conflicts noted in HANDOFF.md before publishing the affected product pages.
6. Add analytics (GA4 ID) if wanted — none in the project.
7. Server: HTTPS, redirect www/non-www, gzip + long cache for /assets, custom 404 -> 404.html. Canonical/sitemap use https://www.nebulae.io — change if the domain differs. Merge sitemap-products.xml into sitemap.xml or submit both; robots.txt points to both.
8. Upload everything except `tools/` (dev only). Hard-refresh / purge CDN after upload.
9. Final pass on the live URL: menu on every page, products filters, forms, mobile.
