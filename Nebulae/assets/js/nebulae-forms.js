/* ═══════════════════════════════════════════════════════════════════════════
   nebulae-forms.js — ONE file that sends every website form through EmailJS.
   Load it LAST on any page that has a form (after nebulae-nav.js / nebulae-page.js).

   Forms handled
     contact.html          full contact / quote form (#ctContactForm) — also pre-filled from ?product=&qty=&type=
     index.html            floating "Get Quote" form, Sample / EVK modal, 2 newsletter boxes
     blog.html, news-events.html  newsletter boxes

   ▶ BEFORE DEPLOY: fill the 3 values in CONFIG below (see tools/EMAILJS_SETUP.md).
   Uses the EmailJS REST API directly (no SDK / CDN script needed).
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ───────────── CONFIG — edit these before deploy ───────────── */
  var CONFIG = {
    PUBLIC_KEY:  'KMz0CeGkUnJobJMhK',      // EmailJS → Account → General → Public Key
    SERVICE_ID: 'service_5evtjim',              // EmailJS → Email Services (value from your earlier build — verify)
    TEMPLATES: {                                // EmailJS → Email Templates. Leave '' to reuse the "contact" template.
      contact:    'template_tdcdtb8',           // full contact form
      quote:      '',                           // floating quick-quote + Sample/EVK request
      newsletter: '',                           // newsletter sign-ups
      autoreply:  ''                            // customer confirmation e-mail (To = {{from_email}}). Paste the template ID to enable; '' = off
    },
    TO_EMAIL: 'sales@nebulae.io',               // sent as {{to_email}} (use it in the template's "To" field if you like)
    COOLDOWN_SEC: 20,                           // minimum seconds between two sends of the same form by the same email (anti-spam)
    TIMEOUT_MS: 15000
  };
  var API = 'https://api.emailjs.com/api/v1.0/email/send';
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  /* ───────────── helpers ───────────── */
  function $(id) { return document.getElementById(id); }
  function val(id) { var e = $(id); return e ? String(e.value || '').trim() : ''; }
  function configured() { return CONFIG.PUBLIC_KEY && CONFIG.PUBLIC_KEY.indexOf('YOUR_') !== 0 && CONFIG.SERVICE_ID.indexOf('YOUR_') !== 0; }
  function template(kind) { return CONFIG.TEMPLATES[kind] || CONFIG.TEMPLATES.contact; }
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var css = document.createElement('style');
  css.textContent =
    '.nbl-form-toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,20px);max-width:min(92vw,460px);padding:.85rem 1.2rem;border-radius:12px;font:600 .88rem/1.45 Poppins,system-ui,sans-serif;color:#fff;background:#059669;box-shadow:0 12px 40px rgba(0,0,0,.25);z-index:100000;opacity:0;pointer-events:none;transition:all .3s}' +
    '.nbl-form-toast.show{opacity:1;transform:translate(-50%,0)}.nbl-form-toast.err{background:#dc2626}' +
    '.nbl-form-alert{display:none;margin:0 0 1rem;padding:.75rem 1rem;border-radius:10px;font:500 .84rem/1.5 Poppins,system-ui,sans-serif;background:#fef2f2;color:#b91c1c;border:1px solid #fecaca}' +
    '.nbl-form-alert.show{display:block}.nbl-form-alert a{color:inherit;font-weight:700}' +
    '.nbl-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;opacity:0}';
  document.head.appendChild(css);

  var toastEl, toastTimer;
  function toast(msg, isErr) {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'nbl-form-toast'; toastEl.setAttribute('role', 'status'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.toggle('err', !!isErr); toastEl.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 5200);
  }
  function friendly(err) {
    var m = err && err.message;
    if (m === 'not-configured') return 'This form is not connected yet — please email us at ' + CONFIG.TO_EMAIL + '.';
    if (m === 'cooldown') return 'Please wait a few seconds before sending another message.';
    if (m === 'timeout') return 'The request timed out. Please check your connection and try again.';
    return 'Sorry, we could not send your message. Please try again or email ' + CONFIG.TO_EMAIL + '.';
  }

  /* honeypot — bots fill hidden fields, people never see it */
  function addHoneypot(container) {
    if (!container || container.querySelector('.nbl-hp')) return;
    var i = document.createElement('input');
    i.type = 'text'; i.name = 'website'; i.tabIndex = -1; i.autocomplete = 'off'; i.className = 'nbl-hp'; i.setAttribute('aria-hidden', 'true');
    container.appendChild(i);
  }
  function trapped(container) { var h = container && container.querySelector('.nbl-hp'); return !!(h && h.value); }

  /* the one send function used by every form */
  function send(kind, p) {
    if (!configured()) { console.warn('[nebulae-forms] EmailJS is not configured — edit CONFIG in assets/js/nebulae-forms.js'); return Promise.reject(new Error('not-configured')); }
    var ck = 'nblForm_' + kind + '_' + String(p.from_email || '').toLowerCase();
    var last = parseInt(lsGet(ck) || '0', 10);
    if (last && Date.now() - last < CONFIG.COOLDOWN_SEC * 1000) return Promise.reject(new Error('cooldown'));
    var params = {
      form_type: p.form_type || kind, subject: p.subject || p.form_type || kind,
      from_name: p.from_name || '', from_email: p.from_email || '', reply_to: p.from_email || '',
      phone: p.phone || '', company: p.company || '', quantity: p.quantity || '', protocols: p.protocols || '',
      product: p.product || '', timeline: p.timeline || '', solution: p.solution || '', details: p.details || '', message: p.message || '',
      page_url: location.href, page_title: document.title, submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST',
      to_email: CONFIG.TO_EMAIL
    };
    var ctl = ('AbortController' in window) ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctl) ctl.abort(); }, CONFIG.TIMEOUT_MS);
    return fetch(API, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, signal: ctl ? ctl.signal : undefined,
      body: JSON.stringify({ service_id: CONFIG.SERVICE_ID, template_id: template(kind), user_id: CONFIG.PUBLIC_KEY, template_params: params })
    }).then(function (r) {
      clearTimeout(timer);
      if (!r.ok) return r.text().then(function (t) { throw new Error('emailjs ' + r.status + ' ' + t); });
      lsSet(ck, String(Date.now()));
      /* customer confirmation (best effort: never blocks or fails the main send) */
      if ((kind === 'contact' || kind === 'quote') && CONFIG.TEMPLATES.autoreply && EMAIL_RE.test(params.from_email)) {
        fetch(API, { method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ service_id: CONFIG.SERVICE_ID, template_id: CONFIG.TEMPLATES.autoreply, user_id: CONFIG.PUBLIC_KEY, template_params: params }) }).catch(function () {});
      }
    }, function (e) { clearTimeout(timer); throw new Error(e && e.name === 'AbortError' ? 'timeout' : (e && e.message) || 'network'); });
  }

  /* ═════════════ 1. CONTACT PAGE ═════════════ */
  function initContact() {
    var form = $('ctContactForm'); if (!form) return;
    addHoneypot(form);
    var btn = $('ctSubmitBtn'), btnHTML = btn ? btn.innerHTML : '';
    var alertEl = document.createElement('div'); alertEl.className = 'nbl-form-alert'; alertEl.setAttribute('role', 'alert');
    if (btn) btn.parentNode.insertBefore(alertEl, btn);

    /* pre-fill when arriving from a product page: contact.html?product=NAME&qty=N&type=sample */
    try {
      var q = new URLSearchParams(location.search), prod = q.get('product'), qty = parseInt(q.get('qty'), 10), type = q.get('type');
      var msg = $('ctMessage'), sub = $('ctSubject'), qsel = $('ctQty');
      if (prod && msg && !msg.value) {
        msg.value = (type === 'sample' || q.get('inquiry') === 'sample' ? 'I would like to request a sample / evaluation unit of ' : 'I would like a quote for ') + prod + (qty > 0 ? ' — quantity: ' + qty : '') + '.\n\nProject details: ';
        msg.dispatchEvent(new Event('input'));
      }
      if (type === 'sample') { window.__ctInq = window.__ctInq || 'sample'; }
      if (prod) window.__ctTopic = window.__ctTopic || prod;
      if (q.get('inquiry')) window.__ctInq = q.get('inquiry');
      if (q.get('topic')) window.__ctTopic = q.get('topic');
      if (prod && $('ctProduct')) $('ctProduct').value = prod.slice(0, 80);
      if ($('ctSampleQty') && qty > 0) $('ctSampleQty').value = String(Math.min(qty, 5));
      if (qsel && qty > 0) { var idx = qty <= 10 ? 1 : qty <= 100 ? 2 : qty <= 1000 ? 3 : qty <= 10000 ? 4 : 5; if (qsel.options[idx]) qsel.selectedIndex = idx; }
    } catch (e) {}

    /* inquiry-type buttons (single choice) and protocol chips (multi choice): mouse + keyboard */
    var inqBtns = [].slice.call(document.querySelectorAll('.ct-inq-btn'));
    /* order = the buttons in contact.html: Buy Products, Product Samples, Solutions, Custom Development, Meeting Request, Technical Support, Partnership */
    var INQ = [
      { key: 'buy', subject: 'Product Inquiry / Quote' }, { key: 'sample', subject: 'Product Sample Request' }, { key: 'solution', subject: 'Solution Inquiry' },
      { key: 'custom', subject: 'Custom IoT Product Development' }, { key: 'meeting', subject: 'Meeting Request' },
      { key: 'support', subject: 'Technical Support' }, { key: 'partner', subject: 'Partnership / Reseller Program' }
    ];
    /* subject-specific detail fields (#ctDetails): which groups show for which subject */
    var KEYS = [['Product Inquiry','quote'],['Product Sample','sample'],['Solution','solution'],['Custom','custom'],['Meeting','meeting'],['Technical','support'],['Partnership','partner']];
    var curKey = 'other';   /* set by the active "I'm interested in" button */
    function syncDetails() {
      var box = $('ctDetails'); if (!box) return;
      var key = curKey, any = false;
      [].forEach.call(box.querySelectorAll('[data-show]'), function (el) {
        var on = el.getAttribute('data-show').split(' ').indexOf(key) > -1; el.hidden = !on; if (on) any = true;
      });
      [].forEach.call(box.querySelectorAll('[data-req]'), function (el) { el.hidden = el.getAttribute('data-req') !== key; });
      box.hidden = !any;
    }
    var autoSubject = false, topic = (window.__ctTopic || '').slice(0, 80);
    /* subject follows the inquiry type (+ the product / solution / event name when we arrive from one) */
    var setSubject = function (text) {
      var sub = $('ctSubject'); if (!sub) return;
      sub.value = text; autoSubject = true; setErr('ctSubject', '');
    };
    if (inqBtns.length) {
      var row = inqBtns[0].parentNode; row.setAttribute('role', 'radiogroup'); row.setAttribute('aria-label', 'I am interested in');
      var pick = function (i, focus, clicked) {
        inqBtns.forEach(function (b, k) { var on = k === i; b.classList.toggle('active', on); b.setAttribute('aria-checked', on ? 'true' : 'false'); b.tabIndex = on ? 0 : -1; });
        var sub = $('ctSubject'), item = INQ[i]; curKey = item ? item.key : 'other';
        if (sub && item && (!sub.value || autoSubject)) setSubject(item.subject + (topic ? ' — ' + topic : ''));
        syncDetails();
        if (focus) inqBtns[i].focus();
      };
      inqBtns.forEach(function (b, i) {
        b.setAttribute('role', 'radio');
        b.addEventListener('click', function () { pick(i, false, true); });
        b.addEventListener('keydown', function (e) {
          var k = e.key, n = inqBtns.length;
          if (k === 'ArrowRight' || k === 'ArrowDown') { e.preventDefault(); pick((i + 1) % n, true); }
          else if (k === 'ArrowLeft' || k === 'ArrowUp') { e.preventDefault(); pick((i - 1 + n) % n, true); }
        });
      });
      var cur = inqBtns.findIndex(function (b) { return b.classList.contains('active'); });
      var want = INQ.map(function (x) { return x.key; }).indexOf(String(window.__ctInq || '').toLowerCase());
      if (!topic || want < 0) { if (want < 0 && topic) want = 0; }
      pick(want >= 0 ? want : (cur < 0 ? 0 : cur));
      var subSel = $('ctSubject'); if (subSel) subSel.addEventListener('input', function () { autoSubject = false; });
    }
    syncDetails();
    [].forEach.call(document.querySelectorAll('.ct-proto-chip'), function (c) {
      c.setAttribute('role', 'checkbox'); c.setAttribute('tabindex', '0'); c.setAttribute('aria-checked', c.classList.contains('selected') ? 'true' : 'false');
      function tog() { var on = c.classList.toggle('selected'); c.setAttribute('aria-checked', on ? 'true' : 'false'); }
      c.addEventListener('click', tog);
      c.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); tog(); } });
    });
    form.addEventListener('submit', function (e) { e.preventDefault(); if (window.submitContactForm) window.submitContactForm(); });

    function setErr(id, text) {
      var el = $(id), fg = el ? el.closest('.ct-field') : null; if (!fg) return;
      fg.classList.toggle('has-error', !!text); var m = fg.querySelector('.ct-error-msg'); if (m) m.textContent = text || '';
    }
    ['ctName', 'ctEmail', 'ctPhone', 'ctCompany', 'ctSubject', 'ctMessage'].forEach(function (id) {
      var el = $(id); if (el) el.addEventListener('input', function () { setErr(id, ''); alertEl.classList.remove('show'); });
    });

    window.submitContactForm = function () {
      alertEl.classList.remove('show');
      var ok = true, digits = val('ctPhone').replace(/\D/g, '');
      function chk(id, bad, msg) { setErr(id, bad ? msg : ''); if (bad) ok = false; }
      chk('ctName', !val('ctName'), 'Please enter your full name');
      chk('ctEmail', !EMAIL_RE.test(val('ctEmail')), 'Please enter a valid email address');
      chk('ctPhone', digits.length < 8 || digits.length > 15, 'Please enter a valid phone number');
      chk('ctCompany', !val('ctCompany'), 'Please enter your company name');
      chk('ctSubject', !val('ctSubject'), 'Please enter a subject');
      chk('ctMessage', val('ctMessage').length < 20, 'Please describe your requirements (min 20 chars)');
      var key = curKey;
      chk('ctProduct', key === 'sample' && !val('ctProduct'), 'Please tell us which product you want a sample of');
      chk('ctSampleQty', key === 'sample' && !val('ctSampleQty'), 'Please select a sample quantity');
      chk('ctQty', key === 'quote' && !val('ctQty'), 'Please select an estimated quantity');
      chk('ctSolution', key === 'solution' && !val('ctSolution'), 'Please select a solution');
      chk('ctMeetDate', key === 'meeting' && !val('ctMeetDate'), 'Please choose a preferred date');
      var consent = $('ctConsent');
      if (consent && !consent.checked) { ok = false; alertEl.textContent = 'Please tick the consent box so we can contact you about your inquiry.'; alertEl.classList.add('show'); }
      if (!ok) { var first = form.querySelector('.has-error input,.has-error select,.has-error textarea'); if (first) first.focus(); return; }
      if (trapped(form)) { showSuccess(); return; }

      function details(k, pr) {
        var L = [];
        function add(label, v) { if (v) L.push(label + ': ' + v); }
        if (k === 'quote') { add('Product / Model', val('ctProduct')); add('Estimated quantity', val('ctQty')); add('Needed by', val('ctTimeline')); add('Protocols', pr); }
        if (k === 'sample') { add('Product / Model', val('ctProduct')); add('Sample quantity', val('ctSampleQty')); add('Protocols', pr); }
        if (k === 'solution') { add('Solution', val('ctSolution')); add('Project scale', val('ctScale')); add('Protocols', pr); }
        if (k === 'custom') { add('Expected volume', val('ctVolume')); add('Needed by', val('ctTimeline')); add('Protocols', pr); }
        if (k === 'meeting') { add('Preferred date', val('ctMeetDate')); add('Preferred time (IST)', val('ctMeetTime')); add('Meeting mode', val('ctMeetMode')); }
        if (k === 'support') { add('Product / Model', val('ctProduct')); add('Issue type', val('ctIssue')); }
        if (k === 'partner') { add('Partnership type', val('ctPartnerType')); add('Region', val('ctRegion')); }
        return L.join('\n') || '(none)';
      }
      var inq = document.querySelector('.ct-inq-btn.active'), inqType = inq ? inq.textContent.trim() : 'General';
      var protos = [].map.call(document.querySelectorAll('.ct-proto-chip.selected'), function (c) { return c.textContent.trim(); }).join(', ');
      btn.disabled = true; btn.textContent = 'Sending…';
      send('contact', {
        form_type: 'Contact form — ' + inqType, subject: val('ctSubject') + ' — ' + val('ctCompany'),
        from_name: val('ctName'), from_email: val('ctEmail'), phone: val('ctPhone'), company: val('ctCompany'),
        product: val('ctProduct'), quantity: key === 'sample' ? val('ctSampleQty') : (key === 'custom' ? val('ctVolume') : val('ctQty')),
        timeline: val('ctTimeline'), solution: val('ctSolution'), protocols: protos, details: details(key, protos), message: val('ctMessage')
      }).then(function () { showSuccess(inqType); }, function (e) {
        if (!e || e.message !== 'cooldown') console.error('[nebulae-forms]', e);
        alertEl.textContent = friendly(e); alertEl.classList.add('show');
        btn.disabled = false; btn.innerHTML = btnHTML;
      });
    };
    function showSuccess(inqType) {
      $('ctFormInner').style.display = 'none'; var s = $('ctSuccess'); s.style.display = 'flex';
      var t = $('ctSuccessType'), n = $('ctSuccessName');
      if (t) t.textContent = inqType || 'inquiry'; if (n) n.textContent = val('ctName').split(' ')[0] || 'there';
      btn.disabled = false; btn.innerHTML = btnHTML;
    }
  }

  /* ═════════════ 2. NEWSLETTER BOXES (index ×2, blog, events) ═════════════ */
  function newsletter(input, btn) {
    var email = input ? input.value.trim() : '';
    if (!EMAIL_RE.test(email)) { input.style.borderColor = '#ef4444'; input.focus(); setTimeout(function () { input.style.borderColor = ''; }, 2200); toast('Please enter a valid email address.', true); return; }
    if (trapped(input.parentNode)) { input.value = ''; return; }
    var old = btn.textContent; btn.disabled = true; btn.textContent = 'Subscribing…';
    send('newsletter', { form_type: 'Newsletter subscription', subject: 'Newsletter sign-up', from_name: email, from_email: email, message: 'Please add ' + email + ' to the newsletter list.' })
      .then(function () { input.value = ''; toast('Thank you! You are subscribed.'); }, function (e) { if (!e || e.message !== 'cooldown') console.error('[nebulae-forms]', e); toast(friendly(e), true); })
      .then(function () { btn.disabled = false; btn.textContent = old; });
  }
  function initNewsletters() {
    [['.nbl-newsletter-form', '.nbl-newsletter-input', '.nbl-newsletter-btn'], ['.nbl-cta-subscribe-pill', 'input', 'button'], ['.pg-newsletter__form', '.pg-newsletter__input', '.pg-newsletter__btn']].forEach(function (s) {
      document.querySelectorAll(s[0]).forEach(function (box) {
        var input = box.querySelector(s[1]), btn = box.querySelector(s[2]);
        if (!input || !btn || box.getAttribute('data-nbl-wired')) return;
        box.setAttribute('data-nbl-wired', '1'); addHoneypot(box);
        btn.removeAttribute('onclick'); btn.type = 'button';
        input.setAttribute('aria-label', 'Email address');
        btn.addEventListener('click', function (e) { e.preventDefault(); newsletter(input, btn); });
        input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); newsletter(input, btn); } });
      });
    });
    window.subscribeNewsletter = function () { var i = $('newsletterEmail'), b = i && i.parentNode.querySelector('button'); if (i && b) newsletter(i, b); };
  }

  /* ═════════════ 3. FLOATING QUICK-QUOTE (index) ═════════════ */
  function initFloat() {
    var box = $('nblFloatForm'); if (!box) return; addHoneypot(box.querySelector('.nbl-float-form-inner'));
    window.submitFloatForm = function () {
      var btn = box.querySelector('.nbl-float-submit'), name = val('ffName'), email = val('ffEmail');
      if (!name) { toast('Please enter your name.', true); $('ffName').focus(); return; }
      if (!EMAIL_RE.test(email)) { toast('Please enter a valid work email.', true); $('ffEmail').focus(); return; }
      if (trapped(box)) return;
      btn.disabled = true; btn.textContent = 'Sending…';
      send('quote', { form_type: 'Quick quote request (floating form)', subject: 'Quick quote request — ' + name, from_name: name, from_email: email, phone: val('ffPhone'), message: val('ffMsg') || '(no message)' })
        .then(function () {
          ['ffName', 'ffEmail', 'ffPhone', 'ffMsg'].forEach(function (i) { if ($(i)) $(i).value = ''; });
          btn.textContent = '✓ Sent!'; btn.style.background = '#059669';
          setTimeout(function () { btn.textContent = 'Send Request'; btn.style.background = ''; btn.disabled = false; box.classList.remove('open'); }, 2200);
        }, function (e) { if (!e || e.message !== 'cooldown') console.error('[nebulae-forms]', e); toast(friendly(e), true); btn.disabled = false; btn.textContent = 'Send Request'; });
    };
  }

  /* ═════════════ 4. SAMPLE / EVK MODAL (index) ═════════════ */
  function initSample() {
    var modal = $('modalBg'); if (!modal) return; addHoneypot($('formView'));
    var btn = modal.querySelector('.btn-submit');
    window.submitForm = function () {
      var f = val('fname'), em = val('email'), r = val('reqtype');
      if (!f || !EMAIL_RE.test(em) || !r) { toast('Please fill in First name, a valid Email, and Request type.', true); return; }
      if (trapped($('formView'))) { $('formView').style.display = 'none'; $('successView').style.display = 'block'; return; }
      var old = btn.textContent; btn.disabled = true; btn.textContent = 'Submitting…';
      send('quote', {
        form_type: 'Sample / EVK request', subject: r + ' — ' + (val('product') || 'product not specified') + ' — ' + (val('company') || f),
        from_name: (f + ' ' + val('lname')).trim(), from_email: em, phone: val('phone'), company: val('company'),
        product: val('product'), message: 'Request type: ' + r + '\nProduct / protocol: ' + (val('product') || '-') + '\n\n' + (val('msg') || '(no message)')
      }).then(function () { $('formView').style.display = 'none'; $('successView').style.display = 'block'; },
        function (e) { if (!e || e.message !== 'cooldown') console.error('[nebulae-forms]', e); toast(friendly(e), true); })
        .then(function () { btn.disabled = false; btn.textContent = old; });
    };
  }

  /* ═════════ 5. INDUSTRY PROPOSAL FORM  (form[data-nbl-proposal] on industries/*.html) ═════════ */
  function initProposal() {
    [].slice.call(document.querySelectorAll('form[data-nbl-proposal]')).forEach(function (form) {
      addHoneypot(form);
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var g = function (n) { var f = form.elements[n]; return f ? String(f.value || '').trim() : ''; };
        var btn = form.querySelector('button[type=submit]'), name = g('name'), email = g('email'), ind = form.getAttribute('data-industry') || 'Industry';
        if (!name) { toast('Please enter your name.', true); form.elements.name.focus(); return; }
        if (!EMAIL_RE.test(email)) { toast('Please enter a valid work email.', true); form.elements.email.focus(); return; }
        if (trapped(form)) return;
        var label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending…';
        send('quote', { form_type: 'Industry proposal request — ' + ind, subject: 'Proposal request (' + ind + ') — ' + name, from_name: name, from_email: email, phone: g('phone'), company: g('company'), product: ind, message: g('message') || '(no message)' })
          .then(function () { form.reset(); btn.textContent = '✓ Sent!'; toast('Thank you — we will get back to you soon.'); setTimeout(function () { btn.textContent = label; btn.disabled = false; }, 2500); },
                function (err) { if (!err || err.message !== 'cooldown') console.error('[nebulae-forms]', err); toast(friendly(err), true); btn.disabled = false; btn.textContent = label; });
      });
    });
  }
  function init() { initContact(); initNewsletters(); initFloat(); initSample(); initProposal(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();

  window.NebulaeForms = { send: send, config: CONFIG };
})();
