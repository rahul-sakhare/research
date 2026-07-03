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

const reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
const hasIO = 'IntersectionObserver' in window;

// ---- stat count-up ----
const nums = document.querySelectorAll('.num[data-to]');
if (nums.length && hasIO && !reduce){
  const run = (el)=>{
    const to = parseFloat(el.dataset.to);
    const t0 = performance.now(); const dur = 1100;
    const tick = (t)=>{
      const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
      el.textContent = Math.round(to*eased).toLocaleString();
      if(p<1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const so = new IntersectionObserver((ents,o)=>{
    ents.forEach(e=>{ if(e.isIntersecting){ run(e.target); o.unobserve(e.target); }});
  },{threshold:.6});
  nums.forEach(n=>so.observe(n));
}

// ---- downloads metric (auto-updated weekly via GitHub Action) ----
const dlNum = document.getElementById('dl-num');
if (dlNum){
  fetch('metrics.json', {cache:'no-store'})
    .then(r => r.ok ? r.json() : null)
    .then(m => {
      if (!m || typeof m.total_downloads !== 'number') return;
      dlNum.dataset.to = m.total_downloads;
      dlNum.textContent = m.total_downloads.toLocaleString();
    }).catch(()=>{});
}

// ---- scroll reveals ----
const revs = document.querySelectorAll('.reveal');
if (revs.length && hasIO && !reduce){
  const ro = new IntersectionObserver((ents,o)=>{
    ents.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); o.unobserve(e.target); }});
  },{threshold:.15});
  revs.forEach(r=>{ r.classList.add('pre'); ro.observe(r); });
}

// ---- about photo parallax (subtle, scroll-linked) ----
const pp = document.getElementById('parallax-photo');
if (pp && !reduce){
  let ticking = false;
  const update = ()=>{
    const rect = pp.parentElement.getBoundingClientRect();
    const vh = window.innerHeight;
    const progress = Math.min(1, Math.max(0, (vh - rect.top) / (vh + rect.height)));
    pp.style.setProperty('--py', ((progress - .5) * -26) + 'px');
    ticking = false;
  };
  window.addEventListener('scroll', ()=>{ if(!ticking){ requestAnimationFrame(update); ticking = true; }}, {passive:true});
  update();
}

// ---- research popovers: tap-to-toggle on touch ----
document.querySelectorAll('.grid .card .pop').forEach(pop=>{
  const card = pop.closest('.card');
  card.addEventListener('click', (e)=>{
    if (window.matchMedia('(hover: none)').matches){
      document.querySelectorAll('.card.pop-open').forEach(c=>{ if(c!==card) c.classList.remove('pop-open'); });
      card.classList.toggle('pop-open');
    }
  });
});

// ---- publications render + filter (clickable cards) ----
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

  const bar = document.getElementById('filters');
  const mk = (key,label,n)=>`<button class="filter${key==='all'?' active':''}" data-f="${key}">${label}<span class="c">${n}</span></button>`;
  bar.innerHTML = mk('all','All',window.PUBS.length) +
    GROUPS.filter(g=>counts[g.key]).map(g=>mk(g.key,g.label.replace(' Presentations','').replace('Conference & Workshop','Conference'),counts[g.key])).join('');

  root.innerHTML = GROUPS.filter(g=>counts[g.key]).map(g=>{
    const items = window.PUBS.filter(p=>p.type===g.key);
    const rows = items.map(p=>{
      const badge = /Editor.s Choice|Best Paper|Project of the Year|Recognized by ITS/i.test(p.cite)
        ? '<span class="badge">Award</span>' : '';
      const inner = `<div class="yr">${p.year||''}</div>
        <div><p class="cite">${bold(p.cite)}${badge}</p>
        ${p.url ? `<span class="doi">${p.url.replace(/^https?:\/\//,'')}</span><span class="open">Open ↗</span>` : ''}</div>`;
      return p.url
        ? `<a class="pub" href="${p.url}" target="_blank" rel="noopener">${inner}</a>`
        : `<div class="pub">${inner}</div>`;
    }).join('');
    return `<section class="pub-group" data-group="${g.key}">
      <h2>${g.label}</h2><div class="gcount">${items.length} ${items.length===1?'entry':'entries'}</div>
      <div class="pub-list">${rows}</div></section>`;
  }).join('');

  bar.addEventListener('click',(e)=>{
    const b = e.target.closest('.filter'); if(!b) return;
    bar.querySelectorAll('.filter').forEach(f=>f.classList.toggle('active',f===b));
    const f = b.dataset.f;
    root.querySelectorAll('.pub-group').forEach(grp=>{
      grp.classList.toggle('hidden', f!=='all' && grp.dataset.group!==f);
    });
  });
}

// ---- media render + filter ----
const mroot = document.getElementById('media-root');
if (mroot && window.MEDIA){
  const KINDS = [
    {key:'press', label:'Press'},
    {key:'agency', label:'Agency Features'},
    {key:'industry', label:'Industry'},
    {key:'podcast', label:'Podcasts'},
    {key:'webinar', label:'Webinars'},
    {key:'recognition', label:'Recognition'},
  ];
  const counts = {};
  window.MEDIA.forEach(m=>counts[m.kind]=(counts[m.kind]||0)+1);

  const bar = document.getElementById('media-filters');
  const mk = (key,label,n)=>`<button class="filter${key==='all'?' active':''}" data-f="${key}">${label}<span class="c">${n}</span></button>`;
  bar.innerHTML = mk('all','All',window.MEDIA.length) +
    KINDS.filter(k=>counts[k.key]).map(k=>mk(k.key,k.label,counts[k.key])).join('');

  const marq = window.MEDIA.filter(m=>m.marquee);
  const rest = window.MEDIA.filter(m=>!m.marquee).sort((a,b)=>(b.year||0)-(a.year||0));

  const mqHTML = marq.length ? `<div class="media-marquee" data-kind="marquee">` + marq.map(m=>`
    <a class="mq" data-kind="${m.kind}" href="${m.url}" target="_blank" rel="noopener">
      <div class="kicker"><span class="src">${m.outlet}</span><span>${m.date}</span></div>
      <h3>${m.title}</h3>${m.note?`<p>${m.note}</p>`:''}
      <span class="go">Read ↗</span></a>`).join('') + `</div>` : '';

  const listHTML = `<div class="media-list">` + rest.map(m=>{
    const inner = `<span class="outlet">${m.outlet}</span>
      <span class="title">${m.title}${m.note?`<span class="note">${m.note}</span>`:''}</span>
      <span class="date">${m.date}</span>`;
    return m.url
      ? `<a class="mi" data-kind="${m.kind}" href="${m.url}" target="_blank" rel="noopener">${inner}</a>`
      : `<div class="mi" data-kind="${m.kind}">${inner}</div>`;
  }).join('') + `</div>`;

  mroot.innerHTML = mqHTML + listHTML;

  bar.addEventListener('click',(e)=>{
    const b = e.target.closest('.filter'); if(!b) return;
    bar.querySelectorAll('.filter').forEach(f=>f.classList.toggle('active',f===b));
    const f = b.dataset.f;
    mroot.querySelectorAll('.mq,.mi').forEach(it=>{
      it.classList.toggle('hidden', f!=='all' && it.dataset.kind!==f);
    });
  });
}
