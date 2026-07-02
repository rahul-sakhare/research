// ---- mobile nav ----
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links){
  toggle.addEventListener('click', ()=>{
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
  links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));
}

// ---- scrollspy (only for in-page anchors on the home page) ----
const spy = [...document.querySelectorAll('.nav-links a[data-spy]')];
if (spy.length && ('IntersectionObserver' in window)){
  const sections = spy.map(a=>document.querySelector(a.getAttribute('href').replace(/^.*#/,'#'))).filter(Boolean);
  const obs = new IntersectionObserver((ents)=>{
    ents.forEach(e=>{
      if(e.isIntersecting){
        const id = '#'+e.target.id;
        spy.forEach(a=>a.classList.toggle('active', a.getAttribute('href').endsWith(id)));
      }
    });
  },{rootMargin:'-45% 0px -50% 0px'});
  sections.forEach(s=>obs.observe(s));
}

// ---- stat count-up ----
const reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
const nums = document.querySelectorAll('.num[data-to]');
if (nums.length && ('IntersectionObserver' in window) && !reduce){
  const run = (el)=>{
    const to = parseFloat(el.dataset.to);
    const t0 = performance.now(); const dur = 1100;
    const tick = (t)=>{
      const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
      el.firstChild.textContent = Math.round(to*eased).toLocaleString();
      if(p<1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const so = new IntersectionObserver((ents,o)=>{
    ents.forEach(e=>{ if(e.isIntersecting){ run(e.target); o.unobserve(e.target); }});
  },{threshold:.6});
  nums.forEach(n=>so.observe(n));
}

// ---- publications render + filter ----
const root = document.getElementById('pub-root');
if (root && window.PUBS){
  const NAME = /(Sakhare,?\s*R\.?\s*S\.?)/g;
  const bold = (s)=> s.replace(NAME, '<b>$1</b>');
  const GROUPS = [
    {key:'journal',    label:'Journal Articles'},
    {key:'report',     label:'Technical Reports'},
    {key:'conference', label:'Conference & Workshop Presentations'},
    {key:'technical',  label:'Technical Presentations'},
    {key:'book',       label:'Monographs & Books'},
    {key:'thesis',     label:'Theses'},
  ];
  const counts = {};
  window.PUBS.forEach(p=>counts[p.type]=(counts[p.type]||0)+1);

  // build filter bar
  const bar = document.getElementById('filters');
  const mk = (key,label,n)=>`<button class="filter${key==='all'?' active':''}" data-f="${key}">${label}<span class="c">${n}</span></button>`;
  bar.innerHTML = mk('all','All',window.PUBS.length) +
    GROUPS.filter(g=>counts[g.key]).map(g=>mk(g.key,g.label.replace(' Presentations','').replace('Conference & Workshop','Conference'),counts[g.key])).join('');

  // render groups
  root.innerHTML = GROUPS.filter(g=>counts[g.key]).map(g=>{
    const items = window.PUBS.filter(p=>p.type===g.key);
    const rows = items.map(p=>{
      const badge = /Editor.s Choice|Best Paper|Project of the Year|Recognized by ITS/i.test(p.cite)
        ? '<span class="badge">Award</span>' : '';
      const doi = p.url ? `<a class="doi" href="${p.url}" target="_blank" rel="noopener">${p.url.replace(/^https?:\/\//,'')}</a>` : '';
      return `<div class="pub" data-type="${p.type}">
        <div class="yr">${p.year||''}</div>
        <div><p class="cite">${bold(p.cite)}${badge}</p>${doi}</div>
      </div>`;
    }).join('');
    return `<section class="pub-group" data-group="${g.key}">
      <h2>${g.label}</h2><div class="gcount">${items.length} ${items.length===1?'entry':'entries'}</div>${rows}</section>`;
  }).join('');

  // filter behavior
  bar.addEventListener('click',(e)=>{
    const b = e.target.closest('.filter'); if(!b) return;
    bar.querySelectorAll('.filter').forEach(f=>f.classList.toggle('active',f===b));
    const f = b.dataset.f;
    root.querySelectorAll('.pub-group').forEach(grp=>{
      grp.classList.toggle('hidden', f!=='all' && grp.dataset.group!==f);
    });
  });
}
