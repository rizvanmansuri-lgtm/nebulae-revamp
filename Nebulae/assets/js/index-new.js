/* index-new.js — behaviour for index-new.html only. */
(function () {
  'use strict';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── counters: values are already in the HTML; with "reduce motion" skip the count-up animation ── */
  if (reduce) document.querySelectorAll('[data-counter]').forEach(function (el) { el._done = true; });

  /* ── open the quote drawer (optionally pre-filled) ── */
  function openQuote(msg) {
    var box = document.getElementById('nblFloatForm');
    var ta = document.getElementById('ffMsg');
    if (ta && msg && !ta.value) ta.value = msg;
    if (box && !box.classList.contains('open') && typeof window.toggleFloatForm === 'function') window.toggleFloatForm();
    var n = document.getElementById('ffName'); if (n) setTimeout(function () { try { n.focus(); } catch (e) {} }, 350);
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-nin-quote]');
    if (b) { e.preventDefault(); var m = b.getAttribute('data-nin-quote'); setTimeout(function () { openQuote(m); }, 60); }   // after the drawer's own outside-click handler has run
  });

  /* ── pause moving logos ── */
  var pause = document.getElementById('ninPause'), track = document.querySelector('.nbl-logos-track');
  if (pause && track) {
    pause.addEventListener('click', function () {
      var on = pause.getAttribute('aria-pressed') !== 'true';
      pause.setAttribute('aria-pressed', on); pause.textContent = on ? 'Play' : 'Pause';
      pause.setAttribute('aria-label', on ? 'Play moving logos' : 'Pause moving logos');
      track.classList.toggle('nin-paused', on);
    });
  }

  /* ── sticky sub-nav + back-to-top ── */
  var sub = document.getElementById('ninSubnav'), top = document.getElementById('ninTop'), hero = document.getElementById('nbl-hero');
  if (sub) sub.hidden = false;
  function onScroll() {
    var y = window.scrollY || 0, limit = (hero ? hero.offsetHeight : 600) * 0.8;
    if (sub) sub.classList.toggle('is-on', y > limit);
    if (top) top.hidden = y < 900;
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  if (top) top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
  if (sub && 'IntersectionObserver' in window) {
    var links = {}; sub.querySelectorAll('a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { Object.keys(links).forEach(function (k) { links[k].classList.remove('is-active'); }); var a = links[en.target.id]; if (a) a.classList.add('is-active'); }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ── product finder ── */
  var CAT = window.NIN_CATALOG || [], BY = {}; CAT.forEach(function (p) { BY[p.slug] = p; });
  // tags: apps it suits · range (short/mid/long) · power (battery/mains/any)
  var TAG = {
    'amr-gas': ['meters', 'long', 'battery'], 'amr-water': ['meters', 'long', 'battery'], 'amr-nic': ['meters', 'mid', 'mains'],
    'nm0221i-nic': ['meters', 'mid', 'mains'], 'nln0721': ['meters,city', 'mid', 'mains'], 'nln0725is': ['meters,city', 'mid', 'mains'], 'nm0221i': ['meters,city', 'mid', 'mains'],
    'nlg6770in': ['meters,city', 'mid', 'mains'], 'nlg8520': ['meters,city', 'mid', 'mains'],
    'nlg6x40g-in': ['meters,city,farm,assets', 'long', 'any'], 'nlg6x40h-in': ['meters,city,farm,assets', 'long', 'any'],
    'nlg7644': ['farm,assets,city,industrial', 'long', 'any'], 'nlg8140': ['farm,industrial', 'long', 'battery'],
    'nlg8400': ['industrial,city', 'long', 'mains'], 'nlg8600': ['industrial,city', 'long', 'mains'],
    'nln500a': ['farm,meters,assets,industrial', 'long', 'battery'], 'nln500b': ['farm,city,assets,industrial', 'long', 'battery'],
    'nm0821i': ['city,farm,industrial', 'long', 'mains'], 'nm0824i': ['city,farm,industrial', 'long', 'mains'],
    'nln111p': ['home,wearables', 'short', 'any'], 'nln811p': ['home,wearables', 'short', 'any'], 'nm0442p': ['home,industrial', 'short', 'mains'],
    'otag433': ['assets,wearables', 'mid', 'battery'], 'p2p-gateway': ['farm,industrial', 'long', 'mains'], 'sls-som-mx6': ['industrial,home', 'mid', 'mains']
  };
  var WHY = {
    meters: 'Utility meters usually run on <strong>LoRaWAN</strong> (battery nodes, km-range) or <strong>Wi-SUN</strong> mesh (mains-powered, dense networks).',
    city: 'City infrastructure is typically covered by <strong>LoRaWAN gateways</strong> or a <strong>Wi-SUN</strong> mesh, with cellular backhaul to your platform.',
    farm: 'Fields and farms need long range and low power — <strong>LoRaWAN</strong> nodes with a gateway on cellular backhaul work well.',
    home: 'Inside buildings, short-range mesh radios such as <strong>Zigbee, Thread / Matter, BLE and Wi-Fi</strong> are the usual choice.',
    assets: 'Moving assets and trackers suit <strong>LoRa</strong> or sub-GHz radios with a gateway that has <strong>4G + GPS</strong>.',
    industrial: 'Plants combine <strong>SCADA / RTU gateways</strong> with <strong>LoRa</strong> wireless sensing and Wi-Fi where wiring is hard.',
    wearables: 'Small, low-power devices suit <strong>Zigbee / BLE</strong> modules or <strong>sub-GHz</strong> tags for longer range.'
  };
  function score(slug, app, range, power) {
    var t = TAG[slug]; if (!t) return -1;
    var s = 0;
    if (t[0].split(',').indexOf(app) > -1) s += 3; else return -1;
    s += t[1] === range ? 2 : (Math.abs(['short', 'mid', 'long'].indexOf(t[1]) - ['short', 'mid', 'long'].indexOf(range)) === 1 ? 1 : 0);
    s += (t[2] === power || t[2] === 'any') ? 1 : 0;
    return s;
  }
  var out = document.getElementById('ninOut');
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function render() {
    if (!out) return;
    var app = document.getElementById('ninApp').value, range = document.getElementById('ninRange').value, power = document.getElementById('ninPower').value;
    var ranked = Object.keys(TAG).filter(function (k) { return BY[k]; }).map(function (k) { return [k, score(k, app, range, power)]; })
      .filter(function (x) { return x[1] >= 4; }).sort(function (a, b) { return b[1] - a[1]; }).slice(0, 3);
    var html = '<p class="nin-res__why">' + WHY[app] + '</p>';
    if (ranked.length) {
      html += '<ul class="nin-res__list">' + ranked.map(function (r) {
        var p = BY[r[0]]; return '<li><a class="nin-res__item" href="products/' + p.slug + '.html"><img src="' + esc(p.img) + '" alt="" width="76" height="56" loading="lazy"><span><span class="nin-res__name">' + esc(p.name) + '</span><span class="nin-res__meta">' + esc(p.type) + ' · ' + esc(p.proto) + '</span></span></a></li>';
      }).join('') + '</ul>';
    } else {
      html += '<p class="nin-res__why">No close match in the catalogue for that combination — our engineers can often adapt a design. Tell us about it.</p>';
    }
    var names = ranked.map(function (r) { return BY[r[0]].name; }).join(', ');
    html += '<div class="nin-res__btns"><button type="button" class="nin-btn nin-btn--solid" data-nin-quote="Product finder: ' + esc(document.getElementById('ninApp').selectedOptions[0].text) + ' · range ' + range + ' · ' + power + (names ? ' · suggested: ' + esc(names) : '') + '">Get a quote for this</button>'
          + '<a class="nin-btn nin-btn--ghost" href="products.html">Browse all products</a></div>';
    out.innerHTML = html;
  }
  ['ninApp', 'ninRange', 'ninPower'].forEach(function (id) { var el = document.getElementById(id); if (el) el.addEventListener('change', render); });
  render();
})();
