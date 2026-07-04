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

// ---- nav tabs: prominent on the home page, compact once noticed ----
const headEl = document.getElementById('site-head');
const isHome = document.body.classList.contains('home');
if (headEl){
  if (!isHome){
    headEl.classList.add('compact');
  } else {
    const onScroll = ()=> headEl.classList.toggle('compact', window.scrollY > 60);
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  }
}

// ---- scroll cue: fades once scrolling starts, disappears near the end ----
const cue = document.getElementById('scroll-cue');
if (cue){
  const upd = ()=>{
    const y = window.scrollY;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    cue.classList.toggle('faded', y > 40 && y < max - 160);
    cue.classList.toggle('gone', y >= max - 160 || max <= 40);
  };
  window.addEventListener('scroll', upd, {passive:true});
  window.addEventListener('resize', upd);
  upd();
}

// ---- stat count-up ----
const nums = document.querySelectorAll('.num[data-to]');
const animateTo = (el)=>{
  const to = parseFloat(el.dataset.to);
  if (reduce || !hasIO){ el.textContent = to.toLocaleString(); return; }
  const t0 = performance.now(); const dur = 1100;
  const tick = (t)=>{
    const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
    el.textContent = Math.round(to*eased).toLocaleString();
    if(p<1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
};
if (nums.length && hasIO && !reduce){
  const so = new IntersectionObserver((ents,o)=>{
    ents.forEach(e=>{ if(e.isIntersecting){ animateTo(e.target); o.unobserve(e.target); }});
  },{threshold:.6});
  nums.forEach(n=>so.observe(n));
}

// ---- home stats: journal & report counts derived live from pubs-data.js ----
if (isHome && window.PUBS){
  const nJ = window.PUBS.filter(p=>p.type==='journal').length;
  const nR = window.PUBS.filter(p=>p.type==='report').length;
  const sj = document.getElementById('stat-journal'), sr = document.getElementById('stat-report');
  if (sj){ sj.dataset.to = nJ; sj.textContent = nJ.toLocaleString(); }
  if (sr){ sr.dataset.to = nR; sr.textContent = nR.toLocaleString(); }
}

// ---- Google Scholar stats (refreshed daily via GitHub Action -> scholar.json) ----
if (isHome){
  fetch('scholar.json', {cache:'no-store'})
    .then(r => r.ok ? r.json() : null)
    .then(s => {
      if (!s) return;
      const map = {'stat-cites':'citations','stat-h':'h_index','stat-i10':'i10_index'};
      Object.entries(map).forEach(([id,key])=>{
        const el = document.getElementById(id);
        if (el && typeof s[key] === 'number'){ el.dataset.to = s[key]; el.textContent = s[key].toLocaleString(); }
      });
    }).catch(()=>{});
}

// ---- downloads metric + as-of date (metrics.json, refreshed by Action) ----
const dlNum = document.getElementById('dl-num');
if (dlNum){
  fetch('metrics.json', {cache:'no-store'})
    .then(r => r.ok ? r.json() : null)
    .then(m => {
      if (!m || typeof m.total_downloads !== 'number') return;
      dlNum.dataset.to = m.total_downloads;
      dlNum.textContent = m.total_downloads.toLocaleString();
      const a = document.getElementById('dl-asof');
      if (a && m.updated){
        const d = new Date(m.updated + 'T12:00:00');
        a.textContent = 'as of ' + (isNaN(d) ? m.updated :
          d.toLocaleDateString('en-US', {month:'short', day:'numeric', year:'numeric'}));
      }
    }).catch(()=>{});
}

// ---- scroll reveals (hiding applied by this script, so no-JS stays visible) ----
const revs = document.querySelectorAll('.reveal');
if (revs.length && hasIO && !reduce){
  const ro = new IntersectionObserver((ents,o)=>{
    ents.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); o.unobserve(e.target); }});
  },{threshold:.15});
  revs.forEach(r=>{ r.classList.add('pre'); ro.observe(r); });
}

// ---- research popovers: tap-to-toggle on touch ----
document.querySelectorAll('.grid .card .pop').forEach(pop=>{
  const card = pop.closest('.card');
  card.addEventListener('click', ()=>{
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

  const mqHTML = marq.length ? `<div class="media-marquee">` + marq.map(m=>`
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
