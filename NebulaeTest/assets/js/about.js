
/* Product rail */
(function(){
  document.querySelectorAll('.atl-prod-rail__item').forEach(function(item){
    item.addEventListener('click',function(){
      var wrap=item.closest('.atl-mega__inner--products');if(!wrap)return;
      wrap.querySelectorAll('.atl-prod-rail__item').forEach(function(i){i.classList.remove('atl-prod-rail__item--active');});
      wrap.querySelectorAll('.atl-prod-panel__body').forEach(function(p){p.classList.remove('atl-prod-panel__body--active');});
      item.classList.add('atl-prod-rail__item--active');
      var panel=wrap.querySelector('[data-panel="'+item.getAttribute('data-prod')+'"]');
      if(panel)panel.classList.add('atl-prod-panel__body--active');
    });
  });
})();
/* Scroll animations */
(function(){
  var els=document.querySelectorAll('[data-ab]');
  if(!els.length)return;
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting)e.target.classList.add('ab-vis');});
  },{threshold:0.15,rootMargin:'0px 0px -60px 0px'});
  els.forEach(function(el){io.observe(el);});
})();
/* Stats counter */
(function(){
  function animNum(el){
    if(el._done)return; el._done=true;
    var target=parseInt(el.getAttribute('data-counter'))||0;
    var suffix=el.getAttribute('data-suffix')||'';
    var start=null,dur=2000;
    function fmt(n){if(n>=1000000)return (n/1000000).toFixed(1)+'M';if(n>=1000)return (n/1000).toFixed(0)+'K';return n.toString();}
    function step(ts){
      if(!start)start=ts;
      var p=Math.min((ts-start)/dur,1),ease=1-Math.pow(1-p,3);
      el.textContent=fmt(Math.floor(target*ease))+suffix;
      if(p<1)requestAnimationFrame(step); else el.textContent=fmt(target)+suffix;
    }
    requestAnimationFrame(step);
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting)e.target.querySelectorAll('[data-counter]').forEach(animNum);
    });
  },{threshold:0.3});
  document.querySelectorAll('.ab-stats-bar').forEach(function(s){io.observe(s);});
})();

/* ─ Dark/Light mode toggle ─ */
(function(){
  var btn=document.getElementById('nblThemeToggle');
  if(!btn)return;
  var sun='<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
  var moon='<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var dark=localStorage.getItem('nblDark')==='1';
  function apply(d){document.body.classList.toggle('dark-mode',d);btn.innerHTML=d?sun:moon;localStorage.setItem('nblDark',d?'1':'0');}
  apply(dark);
  btn.addEventListener('click',function(){apply(!document.body.classList.contains('dark-mode'));});
})();


(function(){
  var hdr  = document.querySelector('.atl-sticky-header');
  var hero = document.querySelector('.ab-hero');
  function setOffset(){
    if(hdr && hero) hero.style.marginTop = hdr.offsetHeight + 'px';
  }
  window.addEventListener('load', setOffset);
  window.addEventListener('resize', setOffset);
})();