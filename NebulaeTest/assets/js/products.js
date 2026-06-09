/* =====================================================
   products.js
   Products page JS.
   Load AFTER nebulae-nav.js.
===================================================== */

/* ═══ PRODUCTS FILTER LOGIC ═══ */
var currentProto='all', currentType='all', currentSearch='', currentView='grid';
var compareItems=[];

function filterCards(){
  var cards=document.querySelectorAll('.pr-card[data-proto]');
  var q=currentSearch.toLowerCase().trim();
  var visible=0;
  cards.forEach(function(card){
    var proto=card.getAttribute('data-proto');
    var type=card.getAttribute('data-type');
    var text=card.textContent.toLowerCase();
    var show=true;
    if(currentProto!=='all'&&proto!==currentProto)show=false;
    if(currentType!=='all'&&type!==currentType)show=false;
    if(q&&!text.includes(q))show=false;
    card.style.display=show?'':'none';
    if(show)visible++;
  });
  var countEl=document.getElementById('prResultCount');
  if(countEl)countEl.textContent=visible;
  var empty=document.getElementById('prEmpty');
  if(empty)empty.style.display=visible===0?'block':'none';
  /* Show/hide proto section headers */
  document.querySelectorAll('.pr-proto-section').forEach(function(sec){
    var hasVisible=Array.from(sec.querySelectorAll('.pr-card')).some(function(c){return c.style.display!=='none';});
    sec.style.display=hasVisible?'':'none';
  });
}

/* Proto filter buttons */
document.querySelectorAll('[data-filter-proto]').forEach(function(btn){
  btn.addEventListener('click',function(){
    currentProto=btn.getAttribute('data-filter-proto');
    document.querySelectorAll('[data-filter-proto]').forEach(function(b){b.classList.remove('active');});
    btn.classList.add('active');
    filterCards();
  });
});
/* Type filter buttons */
document.querySelectorAll('[data-filter-type]').forEach(function(btn){
  btn.addEventListener('click',function(){
    currentType=btn.getAttribute('data-filter-type');
    document.querySelectorAll('[data-filter-type]').forEach(function(b){b.classList.remove('active');});
    btn.classList.add('active');
    filterCards();
  });
});
/* Search */
var searchInput=document.getElementById('prSearch');
if(searchInput){
  searchInput.addEventListener('input',function(){
    currentSearch=searchInput.value;filterCards();
  });
}
/* View toggle */
document.querySelectorAll('.pr-view-btn').forEach(function(btn){
  btn.addEventListener('click',function(){
    currentView=btn.getAttribute('data-view');
    document.querySelectorAll('.pr-view-btn').forEach(function(b){b.classList.remove('active');});
    btn.classList.add('active');
    var wrap=document.getElementById('prGrid');
    if(wrap)wrap.classList.toggle('pr-list-view',currentView==='list');
  });
});
/* Reset */
window.resetFilters=function(){
  currentProto='all';currentType='all';currentSearch='';
  document.querySelectorAll('[data-filter-proto]').forEach(function(b){b.classList.toggle('active',b.getAttribute('data-filter-proto')==='all');});
  document.querySelectorAll('[data-filter-type]').forEach(function(b){b.classList.toggle('active',b.getAttribute('data-filter-type')==='all');});
  if(searchInput)searchInput.value='';
  filterCards();
};
/* Proto chip scroll */
document.querySelectorAll('.pr-proto-chip').forEach(function(chip){
  chip.addEventListener('click',function(){
    var proto=chip.getAttribute('data-chip-proto');
    var btn=document.querySelector('[data-filter-proto="'+proto+'"]');
    if(btn){btn.click();btn.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});}
    var sec=document.getElementById('proto-'+proto);
    if(sec)sec.scrollIntoView({behavior:'smooth',block:'start'});
  });
});
/* Sort */
document.getElementById('prSort')&&document.getElementById('prSort').addEventListener('change',function(){
  var val=this.value;
  var grid=document.getElementById('prGrid');
  if(!grid)return;
  var sections=Array.from(grid.querySelectorAll('.pr-proto-section'));
  sections.forEach(function(sec){
    var cards=Array.from(sec.querySelectorAll('.pr-card'));
    if(val==='name'){cards.sort(function(a,b){return a.querySelector('.pr-card__name').textContent.localeCompare(b.querySelector('.pr-card__name').textContent);});}
    cards.forEach(function(c){sec.querySelector('.pr-grid-inner').appendChild(c);});
  });
});
