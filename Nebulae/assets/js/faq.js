/* faq.js — tabs, live search, deep links for faq.html (no dependencies) */
(function () {
  'use strict';
  var app = document.getElementById('faqApp'); if (!app) return;
  var tabs = [].slice.call(app.querySelectorAll('.fq-tab')), panels = { general: document.getElementById('panel-general'), technical: document.getElementById('panel-technical') };
  var input = document.getElementById('fqSearch'), status = document.getElementById('fqStatus'), empty = document.getElementById('fqEmpty');
  var current = 'general';
  function show(name, focus) {
    current = name;
    tabs.forEach(function (t) { var on = t.getAttribute('data-tab') === name; t.classList.toggle('is-on', on); t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; if (on && focus) t.focus(); });
    Object.keys(panels).forEach(function (k) { panels[k].hidden = k !== name; });
    filter();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { show(t.getAttribute('data-tab')); try { history.replaceState(null, '', '#' + t.getAttribute('data-tab')); } catch (e) {} });
    t.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); show(tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length].getAttribute('data-tab'), true); }
    });
  });
  function filter() {
    var q = (input.value || '').trim().toLowerCase(), words = q.split(/\s+/).filter(Boolean), shown = 0, panel = panels[current];
    [].slice.call(panel.querySelectorAll('.fq-item')).forEach(function (d) {
      var text = d.textContent.toLowerCase(), ok = words.every(function (w) { return text.indexOf(w) !== -1; });
      d.hidden = !ok; if (ok) shown++;
      if (words.length) d.open = ok && shown <= 5;
    });
    [].slice.call(panel.querySelectorAll('.fq-group')).forEach(function (g) { g.hidden = !g.querySelector('.fq-item:not([hidden])'); });
    var chips = panel.querySelector('.fq-chips'); if (chips) chips.hidden = !!words.length;
    empty.hidden = shown !== 0;
    status.textContent = words.length ? (shown + (shown === 1 ? ' question matches' : ' questions match') + ' “' + input.value.trim() + '”') : '';
  }
  var t; input.addEventListener('input', function () { clearTimeout(t); t = setTimeout(filter, 120); });
  function fromHash() {
    var h = (location.hash || '').replace('#', ''); if (!h) return;
    if (h === 'technical' || h === 'general') { show(h); return; }
    var el = document.getElementById(h); if (!el) return;
    var p = el.closest('.fq-panel'); if (p) show(p.id.replace('panel-', ''));
    if (el.tagName === 'DETAILS') el.open = true;
    setTimeout(function () { el.scrollIntoView({ block: 'start' }); }, 50);
  }
  window.addEventListener('hashchange', fromHash);
  show('general'); fromHash();
})();
