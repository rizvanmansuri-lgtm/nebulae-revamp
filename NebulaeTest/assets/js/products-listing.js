/* =====================================================
   products-listing.js — filtering + search for products.html
   Runs only when <body data-pl-page>. No globals.
   URL params: ?proto=<lora|wisun|zigbee|wifi|gsm|other>  ?type=<module|node|gateway|concentrator|filter|evk>  ?q=<text>
   (unknown values such as ?type=cloud or ?proto=ble show the "no products yet" state)
===================================================== */
(function () {
  'use strict';
  if (!document.body || !document.body.hasAttribute('data-pl-page')) return;
  var cards = [].slice.call(document.querySelectorAll('.pl-card'));
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
  var params = new URLSearchParams(window.location.search);
  ['proto', 'type'].forEach(function (k) { var v = (params.get(k) || '').toLowerCase(); if (v) state[k] = v; });
  state.q = (params.get('q') || '').trim().toLowerCase();
  if (input) input.value = params.get('q') || '';

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
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (state.proto === 'all' || c.getAttribute('data-proto') === state.proto) &&
               (state.type === 'all' || c.getAttribute('data-type') === state.type) &&
               (!state.q || c.getAttribute('data-search').indexOf(state.q) !== -1);
      c.hidden = !ok;
      if (ok) shown++;
    });
    chips.forEach(function (c) {
      var g = c.getAttribute('data-group'), v = c.getAttribute('data-value');
      c.setAttribute('aria-pressed', String(state[g] === v));
    });
    var filtered = state.proto !== 'all' || state.type !== 'all' || !!state.q;
    countEl.innerHTML = 'Showing <b>' + shown + '</b> of <b>' + total + '</b> products';
    clearBtn.hidden = !filtered;
    var unknown = (state.proto !== 'all' && !known.proto[state.proto]) || (state.type !== 'all' && !known.type[state.type]);
    emptyEl.hidden = shown !== 0;
    if (shown === 0) {
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
  clearBtn.addEventListener('click', reset);
  var emptyClear = document.getElementById('plEmptyClear');
  if (emptyClear) emptyClear.addEventListener('click', reset);
  apply();
})();
