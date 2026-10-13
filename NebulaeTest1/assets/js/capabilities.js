/* =====================================================
   capabilities.js
   Capabilities page JS: scroll-reveal, anchor nav.
   Load AFTER nebulae-nav.js.
===================================================== */
(function () {
  "use strict";

  /* ── Scroll reveal ── */
  function revealOnScroll() {
    var els = document.querySelectorAll("[data-cp]");
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, dir = el.dataset.cp || "up";
        var delay = el.dataset.cpD ? parseInt(el.dataset.cpD) * 90 : 0;
        setTimeout(function () {
          el.style.opacity = "1";
          el.style.transform = "none";
        }, delay);
        observer.unobserve(el);
      });
    }, { threshold: 0.1 });
    els.forEach(function (el) {
      var dir = el.dataset.cp || "up";
      el.style.opacity = "0";
      if (dir === "up")    el.style.transform = "translateY(28px)";
      if (dir === "left")  el.style.transform = "translateX(-28px)";
      if (dir === "right") el.style.transform = "translateX(28px)";
      if (dir === "scale") el.style.transform = "scale(.95)";
      observer.observe(el);
    });
  }

  /* ── Active anchor highlight ── */
  function initAnchorNav() {
    var btns = document.querySelectorAll(".cp-anchor-btn[href^='#']");
    if (!btns.length) return;
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          btns.forEach(function (b) { b.classList.remove("active"); });
          var active = document.querySelector('.cp-anchor-btn[href="#' + e.target.id + '"]');
          if (active) active.classList.add("active");
        }
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    btns.forEach(function (b) {
      var id = b.getAttribute("href").slice(1);
      var el = document.getElementById(id);
      if (el) observer.observe(el);
    });
    btns.forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.preventDefault();
        var id = b.getAttribute("href").slice(1);
        var el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    revealOnScroll();
    initAnchorNav();
  });
})();
