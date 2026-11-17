/* =====================================================================
   nebulae-float.js — loaded on every page.
   • measures the fixed header → --nbl-hdr (banners never hide under the menu)
   • adds WhatsApp button + (if missing) Back-to-top on every page
   • Get-Quote drawer: close button, outside-click, Esc, aria state
   No dependencies; safe to load twice.
===================================================================== */
(function () {
  'use strict';
  if (window.__nblFloat) return; window.__nblFloat = true;
  var doc = document, WA = 'https://wa.me/917486031238';

  /* 1 ─ header height → CSS variable */
  function setHdr() {
    var h = doc.querySelector('.atl-sticky-header'); if (!h) return;
    var px = Math.round(h.getBoundingClientRect().height);
    if (px > 20 && px < 220) doc.documentElement.style.setProperty('--nbl-hdr', px + 'px');
  }
  setHdr();
  window.addEventListener('load', setHdr);
  window.addEventListener('resize', setHdr);
  if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(setHdr);

  function ready(fn) { if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', fn); else fn(); }

  ready(function () {
    setHdr();

    /* 2 ─ Back to top (nebulae-nav.js wires scroll/click; add a fallback if that script or the button is absent) */
    var top = doc.getElementById('nblBackTop');
    var created = false;
    if (!top) {
      created = true;
      top = doc.createElement('button'); top.id = 'nblBackTop'; top.type = 'button';
      top.setAttribute('aria-label', 'Back to top'); top.title = 'Back to top';
      top.innerHTML = '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m18 15-6-6-6 6"/></svg>';
      doc.body.appendChild(top);
    }
    function topVis() { top.classList.toggle('visible', (window.pageYOffset || doc.documentElement.scrollTop) > 400); }
    window.addEventListener('scroll', topVis, { passive: true }); topVis();
    if (created) {   /* nebulae-nav.js already wires the click (eased scroll) for buttons present in the HTML */
      top.addEventListener('click', function () {
        var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
        try { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } catch (e) { window.scrollTo(0, 0); }
      });
    }

    /* 3 ─ WhatsApp (same markup/colours as index) */
    var cta = doc.getElementById('nblStickyCta');
    if (!cta) {
      cta = doc.createElement('div'); cta.className = 'nbl-sticky-cta'; cta.id = 'nblStickyCta';
      cta.innerHTML = '<a href="' + WA + '" target="_blank" rel="noopener" class="nbl-sticky-btn nbl-sticky-btn--wa" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">' +
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>WhatsApp</a>';
      doc.body.appendChild(cta);
    }
    /* On phones the label is hidden by CSS; keep it for screen readers */
    var wa = cta.querySelector('.nbl-sticky-btn--wa'); if (wa && !wa.getAttribute('aria-label')) wa.setAttribute('aria-label', 'Chat on WhatsApp');
    if (wa && !wa.getAttribute('rel')) wa.setAttribute('rel', 'noopener');
    function ctaVis() { var s = (window.pageYOffset || doc.documentElement.scrollTop) > 400; cta.style.opacity = s ? '1' : '0'; cta.style.pointerEvents = s ? 'auto' : 'none'; cta.style.transform = s ? 'translateY(0)' : 'translateY(20px)'; cta.style.transition = 'opacity .3s,transform .3s'; }
    window.addEventListener('scroll', ctaVis, { passive: true }); ctaVis();

    /* 3b ─ accessibility: tie every orphan <label> to its field (same .fld wrapper) */
    var uid = 0;
    [].slice.call(doc.querySelectorAll('label:not([for])')).forEach(function (lb) {
      if (lb.querySelector('input,select,textarea')) return;
      var wrap = lb.parentElement, ctl = wrap && wrap.querySelector('input,select,textarea'); if (!ctl) return;
      if (!ctl.id) ctl.id = 'nblf' + (++uid);
      lb.setAttribute('for', ctl.id);
    });

    /* 4 ─ Get-Quote drawer */
    var box = doc.getElementById('nblFloatForm');
    if (box) {
      var tab = box.querySelector('.nbl-float-tab');
      var inner = box.querySelector('.nbl-float-form-inner');
      if (tab) { tab.setAttribute('role', 'button'); tab.setAttribute('tabindex', '0'); tab.setAttribute('aria-controls', 'nblFloatForm'); tab.removeAttribute('onclick'); }
      if (inner && !box.querySelector('.nbl-float-close')) {
        var x = doc.createElement('button'); x.type = 'button'; x.className = 'nbl-float-close'; x.setAttribute('aria-label', 'Close quote form'); x.title = 'Close';
        x.innerHTML = '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
        box.appendChild(x);
      }
      var closeBtn = box.querySelector('.nbl-float-close');
      function setOpen(o) {
        box.classList.toggle('open', o);
        if (tab) tab.setAttribute('aria-expanded', o ? 'true' : 'false');
        box.setAttribute('aria-hidden', o ? 'false' : 'true'); if (inner) { if (o) inner.removeAttribute('inert'); else inner.setAttribute('inert', ''); }
        if (o) { var f = box.querySelector('input,textarea'); if (f) setTimeout(function () { try { f.focus({ preventScroll: true }); } catch (e) {} }, 350); }
      }
      setOpen(false);
      window.toggleFloatForm = function () { setOpen(!box.classList.contains('open')); };
      if (tab) {
        tab.addEventListener('click', function (e) { e.stopPropagation(); window.toggleFloatForm(); });
        tab.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); window.toggleFloatForm(); } });
      }
      if (closeBtn) closeBtn.addEventListener('click', function (e) { e.stopPropagation(); setOpen(false); if (tab) tab.focus(); });
      /* outside click / tap */
      doc.addEventListener('click', function (e) { if (box.classList.contains('open') && !box.contains(e.target)) setOpen(false); });
      doc.addEventListener('keydown', function (e) { if (e.key === 'Escape' && box.classList.contains('open')) { setOpen(false); if (tab) tab.focus(); } });
      /* other scripts that remove .open (e.g. after a successful send) keep aria in sync */
      new MutationObserver(function () { var o = box.classList.contains('open'); if (tab) tab.setAttribute('aria-expanded', o ? 'true' : 'false'); box.setAttribute('aria-hidden', o ? 'false' : 'true'); if (inner) { if (o) inner.removeAttribute('inert'); else inner.setAttribute('inert', ''); } }).observe(box, { attributes: true, attributeFilter: ['class'] });
    }
  });
})();
