/* =====================================================
   services.js
   Services page JS: scroll-reveal animations,
   service card filter, stats counter.
   Load AFTER nebulae-nav.js.
===================================================== */

(function () {
  "use strict";

  /* ── Scroll-reveal ── */
  function revealOnScroll() {
    var els = document.querySelectorAll("[data-sv]");
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          var el = e.target;
          var dir = el.dataset.sv || "up";
          var delay = el.dataset.svD ? parseInt(el.dataset.svD) * 80 : 0;
          setTimeout(function () {
            el.style.opacity = "1";
            el.style.transform = "none";
          }, delay);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.12 });

    els.forEach(function (el) {
      var dir = el.dataset.sv || "up";
      el.style.transition = "opacity .55s ease, transform .55s ease";
      el.style.opacity = "0";
      if (dir === "up")    el.style.transform = "translateY(28px)";
      if (dir === "left")  el.style.transform = "translateX(-28px)";
      if (dir === "right") el.style.transform = "translateX(28px)";
      if (dir === "scale") el.style.transform = "scale(.95)";
      observer.observe(el);
    });
  }

  /* ── Service card filter ── */
  function initFilter() {
    var btns = document.querySelectorAll(".sv-filter-btn");
    var cards = document.querySelectorAll(".sv-card-wrap");
    btns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        btns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        var f = btn.dataset.filter;
        cards.forEach(function (c) {
          var show = f === "all" || c.dataset.cat === f;
          c.style.display = show ? "" : "none";
          c.style.opacity = show ? "1" : "0";
        });
      });
    });
  }

  /* ── Stats counter ── */
  function initCounters() {
    var els = document.querySelectorAll("[data-counter]");
    if (!els.length) return;
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        var target = parseInt(el.dataset.counter);
        var suffix = el.dataset.suffix || "";
        var start = 0;
        var step = Math.ceil(target / 40);
        var timer = setInterval(function () {
          start = Math.min(start + step, target);
          el.textContent = start + suffix;
          if (start >= target) clearInterval(timer);
        }, 30);
        observer.unobserve(el);
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { observer.observe(el); });
  }

  document.addEventListener("DOMContentLoaded", function () {
    revealOnScroll();
    initFilter();
    initCounters();
  });
  
})();
const cards = document.querySelectorAll('.sv-card');

cards.forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.classList.add('sv-card--featured');
  });

  card.addEventListener('mouseleave', () => {
    card.classList.remove('sv-card--featured');
  });
});