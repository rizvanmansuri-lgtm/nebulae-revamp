/* =====================================================
   nebulae-page.js
   Index / landing page JS.
   Contains: tabs, modal helpers, use-case selector,
   stats counter, sticky CTA, newsletter, expertise
   accordion, sample/EVK request modal.
   Load AFTER nebulae-nav.js.
===================================================== */

document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById('tab-' + tab.dataset.tab).classList.add('active');
  });
});

(function(){var m=document.getElementById('cuThankModal');if(m)m.style.display='none';})();
function closeCuModal(){var m=document.getElementById('cuThankModal');if(m){m.style.display='none';document.body.style.overflow='';}}

/* ══ Use-Case Selector ══ */
document.querySelectorAll('.nbl-uc-tab').forEach(function(tab){
  tab.addEventListener('click',function(){
    document.querySelectorAll('.nbl-uc-tab').forEach(function(t){t.classList.remove('active');});
    document.querySelectorAll('.nbl-uc-panel').forEach(function(p){p.classList.remove('active');});
    tab.classList.add('active');
    var panel=document.getElementById('uc-'+tab.getAttribute('data-uc'));
    if(panel)panel.classList.add('active');
  });
});

 

/* ══ ROI Calculator ══ */
/*
window.calcROI=function(){
  var endpoints=parseInt(document.getElementById('roiEndpoints').value)||1000;
  var manualCost=parseInt(document.getElementById('roiManualCost').value)||500;
  var wastage=parseInt(document.getElementById('roiWastage').value)||30;
  var energySpend=parseFloat(document.getElementById('roiEnergySpend').value)||50;
  var opsSaving=Math.round(endpoints*manualCost*0.9);
  var energySaving=Math.round(energySpend*100000*(wastage/100));
  var total=opsSaving+energySaving;
  function fmt(n){if(n>=10000000)return '₹'+(n/10000000).toFixed(1)+' Cr';if(n>=100000)return '₹'+(n/100000).toFixed(1)+' L';return '₹'+n.toLocaleString('en-IN');}
  document.getElementById('roiOpsSaving').textContent=fmt(opsSaving);
  document.getElementById('roiEnergySaving').textContent=fmt(energySaving);
  document.getElementById('roiTotal').textContent=fmt(total);
};
calcROI();
*/
/* ══ Newsletter ══ */
window.subscribeNewsletter=function(){
  var inp=document.getElementById('newsletterEmail');
  if(!inp)return;
  var val=inp.value.trim();
  if(!val||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)){inp.style.borderColor='#ef4444';setTimeout(function(){inp.style.borderColor='';},2000);return;}
  inp.value='';
  inp.placeholder='Thank you! You are subscribed ✓';
  inp.style.borderColor='#06b6d4';
  setTimeout(function(){inp.placeholder='Your work email address';inp.style.borderColor='';},4000);
};

/* ══ Stats Counter ══ */
(function(){
  function animNum(el){
    if(el._done)return;
    el._done=true;
    var target=parseInt(el.getAttribute('data-counter'))||0;
    var suffix=el.getAttribute('data-suffix')||'';
    var dur=2000;
    var start=null;
    function fmt(n){if(n>=1000000)return (n/1000000).toFixed(1)+'M';if(n>=1000)return (n/1000).toFixed(0)+'K';return n.toString();}
    function step(ts){
      if(!start)start=ts;
      var p=Math.min((ts-start)/dur,1);
      var ease=1-Math.pow(1-p,3);
      var cur=Math.floor(target*ease);
      el.textContent=fmt(cur)+suffix;
      if(p<1)requestAnimationFrame(step);
      else el.textContent=fmt(target)+suffix;
    }
    requestAnimationFrame(step);
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        var els=e.target.querySelectorAll('[data-counter]');
        els.forEach(animNum);
      }
    });
  },{threshold:0.3});
  document.querySelectorAll('.nbl-stats-section').forEach(function(s){io.observe(s);});
})();

/* ══ Sticky CTA show/hide on scroll ══ */
(function(){
  var cta=document.getElementById('nblStickyCta');
  if(!cta)return;
  window.addEventListener('scroll',function(){
    if(window.scrollY>400){cta.style.opacity='1';cta.style.transform='translateY(0)';}
    else{cta.style.opacity='0';cta.style.transform='translateY(20px)';}
  },{passive:true});
  cta.style.opacity='0';cta.style.transform='translateY(20px)';
  cta.style.transition='opacity .3s,transform .3s';
})();

/* ─ Expertise accordion ─ */
(function(){
  var cards=document.querySelectorAll('.nbl-exp-card');
  window.setExpActive=function(idx){
    cards.forEach(function(c,i){c.classList.toggle('nbl-exp-active',i===idx);});
  };
})();

/* ─ Nebulae Solutions tabs (new tabs with nb- prefix) ─ */
document.querySelectorAll('.tab').forEach(function(tab){
  tab.addEventListener('click',function(){
    var row=tab.closest('.section-wrapper')||tab.closest('section');
    if(!row)return;
    row.querySelectorAll('.tab').forEach(function(t){t.classList.remove('active');});
    row.querySelectorAll('.tab-panel').forEach(function(p){p.classList.remove('active');});
    tab.classList.add('active');
    var panel=document.getElementById('tab-'+tab.getAttribute('data-tab'));
    if(panel)panel.classList.add('active');
  });
});

function openModal() {
    document.getElementById('modalBg').classList.add('open');
    document.getElementById('formView').style.display = 'block';
    document.getElementById('successView').style.display = 'none';
  }
  function closeModal() {
    document.getElementById('modalBg').classList.remove('open');
  }
  function handleBgClick(e) {
    if (e.target === document.getElementById('modalBg')) closeModal();
  }
  function submitForm() {
    var f = document.getElementById('fname').value.trim();
    var e = document.getElementById('email').value.trim();
    var r = document.getElementById('reqtype').value;
    if (!f || !e || !r) { alert('Please fill in First name, Email, and Request type.'); return; }
    document.getElementById('formView').style.display = 'none';
    document.getElementById('successView').style.display = 'block';
  }

