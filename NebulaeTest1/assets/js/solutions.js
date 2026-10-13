/* =====================================================
   solutions.js
   Solutions page JS: scroll progress, back-to-top,
   scroll-reveal animations.
   Load AFTER nebulae-nav.js.
===================================================== */

(function(){
  var bar=document.getElementById('nblProgressBar');
  if(bar)window.addEventListener('scroll',function(){var s=window.scrollY,h=document.documentElement.scrollHeight-window.innerHeight;bar.style.width=(h>0?s/h*100:0)+'%';},{passive:true});
  var btn=document.getElementById('nblBackTop');
  if(btn){window.addEventListener('scroll',function(){btn.classList.toggle('visible',window.scrollY>400);},{passive:true});btn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});}
  var nav=document.getElementById('atlNav');
  if(nav)window.addEventListener('scroll',function(){nav.classList.toggle('scrolled',window.scrollY>10);},{passive:true});
})();
window.toggleMega=function(id){document.querySelectorAll('.atl-nav__item--mega').forEach(function(i){if(i.id!==id)i.classList.remove('mega-open');});var el=document.getElementById(id);if(el)el.classList.toggle('mega-open');};
document.addEventListener('click',function(e){if(!e.target.closest('.atl-nav__item--mega'))document.querySelectorAll('.atl-nav__item--mega').forEach(function(i){i.classList.remove('mega-open');});});
(function(){var dd=document.getElementById('brochureDropdown'),btn=document.getElementById('brochureBtn');if(dd&&btn){btn.addEventListener('click',function(e){e.stopPropagation();dd.classList.toggle('open');});document.addEventListener('click',function(){dd.classList.remove('open');});}var burger=document.getElementById('navBurger'),mobile=document.getElementById('navMobile');if(burger&&mobile){burger.addEventListener('click',function(){var o=mobile.classList.toggle('open');burger.classList.toggle('open',o);burger.setAttribute('aria-expanded',o);});}})();
window.toggleMobileAcc=function(btn){var b=btn.nextElementSibling,o=b.classList.contains('open');btn.classList.toggle('open',!o);b.classList.toggle('open',!o);};
window.navClick=function(id){window.location.href='index.html#'+id;return false;};
window.mobileNavClick=function(id){var m=document.getElementById('navMobile');if(m)m.classList.remove('open');window.location.href='index.html#'+id;return false;};
(function(){document.querySelectorAll('.atl-prod-rail__item').forEach(function(item){item.addEventListener('click',function(){var wrap=item.closest('.atl-mega__inner--products');if(!wrap)return;wrap.querySelectorAll('.atl-prod-rail__item').forEach(function(i){i.classList.remove('atl-prod-rail__item--active');});wrap.querySelectorAll('.atl-prod-panel__body').forEach(function(p){p.classList.remove('atl-prod-panel__body--active');});item.classList.add('atl-prod-rail__item--active');var panel=wrap.querySelector('[data-panel="'+item.getAttribute('data-prod')+'"]');if(panel)panel.classList.add('atl-prod-panel__body--active');});});})();
(function(){
  var els=document.querySelectorAll('[data-sl]');
  if(!els.length)return;
  var io=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting)e.target.classList.add('sl-vis');});},{threshold:0.12,rootMargin:'0px 0px -60px 0px'});
  els.forEach(function(el){io.observe(el);});
})();
