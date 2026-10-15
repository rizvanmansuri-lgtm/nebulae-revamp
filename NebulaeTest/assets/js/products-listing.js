/* =====================================================
   products-listing.js — filtering + search for products.html
   Runs only when <body data-pl-page>. No globals.
   URL params: ?proto=<lora|wisun|zigbee|wifi|gsm|other>  ?type=<module|node|gateway|concentrator|filter|evk>  ?q=<text>
   (unknown values such as ?type=cloud or ?proto=ble show the "no products yet" state)
===================================================== */
(function () {
  'use strict';
  if (!document.body || !document.body.hasAttribute('data-pl-page')) return;
  /* cards are re-queried on every apply() so removing/adding a product (or marking one data-pl-off to switch it off) is always reflected */
  function liveCards() { return [].slice.call(document.querySelectorAll('.pl-card:not([data-pl-off])')); }
  var cards = liveCards();
  var chips = [].slice.call(document.querySelectorAll('.pl-chip'));
  var input = document.getElementById('plSearch');
  var countEl = document.getElementById('plCount');
  var clearBtn = document.getElementById('plClear');
  var emptyEl = document.getElementById('plEmpty');
  var emptyMsg = document.getElementById('plEmptyMsg');
  var total = cards.length;
  var known = { proto: {}, type: {} };
  chips.forEach(function (c) { var g = c.getAttribute('data-group'), v = c.getAttribute('data-value'); if (v !== 'all') known[g][v] = 1; });

  var state = { proto: 'all', type: 'all', q: '' };
  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    state = { proto: 'all', type: 'all', q: (params.get('q') || '').trim().toLowerCase() };
    ['proto', 'type'].forEach(function (k) { var v = (params.get(k) || '').toLowerCase(); if (v) state[k] = v; });
    if (input) input.value = params.get('q') || '';
  }
  readUrl();

  function syncUrl() {
    if (!window.history || !history.replaceState) return;
    var p = new URLSearchParams();
    if (state.proto !== 'all') p.set('proto', state.proto);
    if (state.type !== 'all') p.set('type', state.type);
    if (state.q) p.set('q', state.q);
    var qs = p.toString();
    try { history.replaceState(null, '', window.location.pathname + (qs ? '?' + qs : '')); } catch (e) { /* file:// or sandbox */ }
  }

  function apply() {
    cards = liveCards(); total = cards.length;
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (state.proto === 'all' || c.getAttribute('data-proto') === state.proto) &&
               (state.type === 'all' || c.getAttribute('data-type') === state.type) &&
               (!state.q || (c.getAttribute('data-search')||'').indexOf(state.q) !== -1);
      c.hidden = !ok;
      if (ok) shown++;
    });
    /* highlight the active chip (no per-chip counters — the "Showing X of Y" line is the single source of truth) */
    known = { proto: {}, type: {} };
    cards.forEach(function (card) { known.proto[card.getAttribute('data-proto')] = 1; known.type[card.getAttribute('data-type')] = 1; });
    chips.forEach(function (c) {
      var g = c.getAttribute('data-group'), v = c.getAttribute('data-value');
      c.hidden = v !== 'all' && !known[g][v];
      c.setAttribute('aria-pressed', String(state[g] === c.getAttribute('data-value')));
    });
    var filtered = state.proto !== 'all' || state.type !== 'all' || !!state.q;
    if (countEl) countEl.innerHTML = 'Showing <b>' + shown + '</b> of <b>' + total + '</b> products';
    if (clearBtn) clearBtn.hidden = !filtered;
    var unknown = (state.proto !== 'all' && !known.proto[state.proto]) || (state.type !== 'all' && !known.type[state.type]);
    if (emptyEl) emptyEl.hidden = shown !== 0;
    if (shown === 0 && emptyMsg) {
      emptyMsg.textContent = unknown
        ? 'We do not have products in this category yet. Browse the full range, or contact our sales team and we will help you find the right solution.'
        : 'No products match your current filters. Try removing a filter or searching with different words.';
    }
    syncUrl();
  }

  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      state[c.getAttribute('data-group')] = c.getAttribute('data-value');
      apply();
    });
  });
  var t;
  if (input) input.addEventListener('input', function () {
    clearTimeout(t);
    t = setTimeout(function () { state.q = input.value.trim().toLowerCase(); apply(); }, 120);
  });
  function reset() { state = { proto: 'all', type: 'all', q: '' }; if (input) input.value = ''; apply(); }
  if (clearBtn) clearBtn.addEventListener('click', reset);
  var emptyClear = document.getElementById('plEmptyClear');
  if (emptyClear) emptyClear.addEventListener('click', reset);
  apply();
  /* re-sync after bfcache restore / back-forward / tab return (browsers may restore stale input values or DOM) */
  window.addEventListener('pageshow', function (e) { if (e.persisted) { readUrl(); apply(); } });
  window.addEventListener('popstate', function () { readUrl(); apply(); });
  document.addEventListener('visibilitychange', function () { if (!document.hidden) apply(); });
})();
