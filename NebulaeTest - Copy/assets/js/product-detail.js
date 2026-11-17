/* =====================================================
   product-detail.js
   Product Detail page JS.
   Load AFTER nebulae-nav.js.

   Runs only on pages that opt in with <body data-pd-page>
   (every generated page in /products/). Uses data-attributes and
   event listeners — no inline onclick handlers, no globals.
===================================================== */
(function () {
  'use strict';
  if (!document.body || !document.body.hasAttribute('data-pd-page')) return;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ---------- Gallery: thumbnails + lightbox ---------- */
  var mainImg = $('#pdMainImg');
  var thumbs = $$('[data-pd-thumb]');

  function setThumb(thumb) {
    if (!mainImg || !thumb) return;
    thumbs.forEach(function (t) { t.classList.toggle('active', t === thumb); });
    mainImg.src = thumb.getAttribute('data-full');
    mainImg.alt = thumb.getAttribute('data-alt') || '';
  }
  thumbs.forEach(function (t) { t.addEventListener('click', function () { setThumb(t); }); });

  var lightbox = $('#pdLightbox');
  var lightboxImg = $('#pdLightboxImg');
  var lastFocus = null;
  function openLightbox() {
    if (!lightbox || !lightboxImg || !mainImg) return;
    lastFocus = document.activeElement;
    lightboxImg.src = mainImg.currentSrc || mainImg.src;
    lightboxImg.alt = mainImg.alt;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
    var close = $('[data-pd-lb-close]', lightbox);
    if (close) close.focus();
  }
  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  var zoomBtn = $('[data-pd-zoom]');
  if (zoomBtn) zoomBtn.addEventListener('click', openLightbox);
  if (mainImg) mainImg.addEventListener('click', openLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', function (ev) {
      if (ev.target === lightbox || ev.target.hasAttribute('data-pd-lb-close')) closeLightbox();
    });
  }
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && lightbox && lightbox.classList.contains('open')) closeLightbox();
  });

  /* ---------- Quantity stepper ---------- */
  var qty = $('#pdQty');
  $$('[data-pd-qty]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (!qty) return;
      var step = parseInt(btn.getAttribute('data-pd-qty'), 10) || 0;
      var cur = parseInt(qty.value, 10) || 1;
      qty.value = Math.max(1, cur + step);
    });
  });
  if (qty) qty.addEventListener('change', function () {
    var v = parseInt(qty.value, 10);
    qty.value = isNaN(v) || v < 1 ? 1 : v;
  });

  /* ---------- Request quote -> contact page with product prefilled ---------- */
  var nameEl = $('.pd-info__name');
  $$('[data-pd-quote]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var name = nameEl ? nameEl.textContent.trim() : 'product';
      var q = qty ? (parseInt(qty.value, 10) || 1) : 1;
      window.location.href = (document.body.getAttribute('data-pd-base') || './') + 'contact.html?product=' + encodeURIComponent(name) + '&qty=' + encodeURIComponent(q);
    });
  });

  /* ---------- Copy link ---------- */
  var copyBtn = $('[data-pd-copy]');
  function flashCopied() {
    var label = copyBtn && $('span', copyBtn);
    if (!label) return;
    var old = label.textContent;
    label.textContent = 'Link Copied!';
    setTimeout(function () { label.textContent = old; }, 1800);
  }
  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:-1000px;opacity:0;';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); flashCopied(); } catch (err) { /* clipboard unavailable */ }
    document.body.removeChild(ta);
  }
  if (copyBtn) copyBtn.addEventListener('click', function () {
    var url = window.location.href.split('#')[0];
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(flashCopied, function () { fallbackCopy(url); });
    } else { fallbackCopy(url); }
  });

  /* ---------- Tabs (click, keyboard arrows, #hash deep-link) ---------- */
  var tabBtns = $$('.pd-tab-btn');
  var tabPanels = $$('.pd-tab-panel');
  function activate(name, focus) {
    var target = null;
    tabBtns.forEach(function (b) {
      var on = b.getAttribute('data-tab') === name;
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
      b.tabIndex = on ? 0 : -1;
      if (on) target = b;
    });
    tabPanels.forEach(function (p) {
      var on = p.id === 'pd-tab-' + name;
      p.classList.toggle('active', on);
      if (on) p.removeAttribute('hidden'); else p.setAttribute('hidden', '');
    });
    if (target) {
      if (focus) target.focus();
      if (target.scrollIntoView) target.scrollIntoView({ block: 'nearest', inline: 'center' });
    }
  }
  tabBtns.forEach(function (btn, i) {
    btn.addEventListener('click', function () { activate(btn.getAttribute('data-tab')); });
    btn.addEventListener('keydown', function (ev) {
      var n = tabBtns.length, next = -1;
      if (ev.key === 'ArrowRight') next = (i + 1) % n;
      else if (ev.key === 'ArrowLeft') next = (i - 1 + n) % n;
      else if (ev.key === 'Home') next = 0;
      else if (ev.key === 'End') next = n - 1;
      if (next > -1) { ev.preventDefault(); activate(tabBtns[next].getAttribute('data-tab'), true); }
    });
  });
  function fromHash() {
    var h = (window.location.hash || '').replace('#', '');
    if (h && $('#pd-tab-' + h)) {
      activate(h);
      var bar = $('#pd-tabs');
      if (bar && bar.scrollIntoView) bar.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
