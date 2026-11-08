// ---- dark / light theme toggle ----
(function(){
  const themeToggle = document.getElementById('theme-toggle');
  const getStoredTheme = () => {
    try { return localStorage.getItem('theme'); } catch(e){ return null; }
  };
  const getSystemTheme = () => {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const applyTheme = (theme, persist) => {
    document.documentElement.setAttribute('data-theme', theme);
    if (persist) {
      try { localStorage.setItem('theme', theme); } catch(e){}
    }
    if (themeToggle) {
      const isDark = theme === 'dark';
      const label = isDark ? 'Switch to light theme' : 'Switch to dark theme';
      themeToggle.setAttribute('aria-label', label);
      themeToggle.setAttribute('title', label);
    }
  };

  const initialTheme = document.documentElement.getAttribute('data-theme') || getStoredTheme() || getSystemTheme();
  applyTheme(initialTheme, false);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next, true);
    });
  }

  if (window.matchMedia) {
    try {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!getStoredTheme()) {
          applyTheme(e.matches ? 'dark' : 'light', false);
        }
      });
    } catch(err){}
  }
})();

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

// ---- nav tabs: prominent on the home page, compact once scrolled ----
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
  if (reduce || !hasIO || isNaN(to)){ el.textContent = to ? to.toLocaleString() : el.textContent; return; }
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
      const asof = document.getElementById('stat-asof');
      if (asof && s.updated){
        const d = new Date(s.updated + 'T12:00:00');
        if (!isNaN(d.getTime())){
          const monthYear = d.toLocaleDateString('en-US', {month:'long', year:'numeric'});
          asof.textContent = `as of ${monthYear}`;
        }
      }
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

// ---- Helper: Generate BibTeX citation string ----
function formatBibtex(p) {
  const year = p.year || 2026;
  const cite = p.cite || '';
  // Try to parse Authors, Year, Title
  const m = cite.match(/^(.*?)\s*\(\d{4}\)\.?\s*(.*?)(?:\.|$)/);
  const authors = m ? m[1].replace(/&/g, 'and').trim() : 'Sakhare, Rahul S.';
  let title = m ? m[2].trim() : cite;
  if (p.type === 'thesis') {
    title = title.replace(/\s*\((?:Doctoral dissertation|Master's thesis)\)/i, '');
  }
  const isMaster = /master/i.test(cite);
  const entryType = p.type === 'journal' ? 'article' :
    (p.type === 'report' ? 'techreport' :
    (p.type === 'book' ? 'book' :
    (p.type === 'thesis' ? (isMaster ? 'mastersthesis' : 'phdthesis') : 'inproceedings')));
  const key = 'sakhare' + year + (p.type === 'thesis' ? (isMaster ? 'ms' : 'phd') : (p.type || 'entry').slice(0,4));
  
  let bib = `@${entryType}{${key},\n  author = {${authors}},\n  title = {${title}},\n  year = {${year}}`;
  if (p.type === 'thesis') {
    const school = /Purdue/i.test(cite) ? 'Purdue University' : (/Madras/i.test(cite) ? 'Indian Institute of Technology Madras' : '');
    if (school) bib += `,\n  school = {${school}}`;
    const address = /West Lafayette/i.test(cite) ? 'West Lafayette, IN' : (/Chennai/i.test(cite) ? 'Chennai, India' : '');
    if (address) bib += `,\n  address = {${address}}`;
  }
  if (p.url) bib += `,\n  url = {${p.url}}`;
  bib += '\n}';
  return bib;
}

// ---- publications render + live search + filter + BibTeX copy ----
const root = document.getElementById('pub-root');
if (root && window.PUBS){
  const NAME = /(Sakhare,?\s*R\.?\s*S\.?)/g;
  const bold = (s)=> s.replace(NAME, '<b>$1</b>');
  const GROUPS = [
    {key:'journal',    label:'Peer-Reviewed Journal Articles'},
    {key:'report',     label:'Technical Research Reports'},
    {key:'book',       label:'Monographs & Authoritative Reference Texts'},
    {key:'conference', label:'Conference & Workshop Proceedings'},
    {key:'technical',  label:'Invited & Technical Presentations'},
    {key:'thesis',     label:'Theses'},
  ];
  const counts = {};
  window.PUBS.forEach(p=>counts[p.type]=(counts[p.type]||0)+1);

  const bar = document.getElementById('filters');
  const mk = (key,label,n)=>`<button class="filter${key==='all'?' active':''}" data-f="${key}">${label}<span class="c">${n}</span></button>`;
  if (bar){
    bar.innerHTML = mk('all','All',window.PUBS.length) +
      GROUPS.filter(g=>counts[g.key]).map(g=>mk(g.key,g.label.replace('Peer-Reviewed ','').replace('Technical Research ','').replace(' & Authoritative Reference Texts',''),counts[g.key])).join('');
  }

  // Render publications HTML
  const renderPubs = (filterKey = 'all', query = '') => {
    const q = query.toLowerCase().trim();
    let totalVisible = 0;

    root.innerHTML = GROUPS.filter(g=>counts[g.key]).map(g=>{
      let items = window.PUBS.filter(p=>p.type===g.key);
      if (q){
        items = items.filter(p => (p.cite||'').toLowerCase().includes(q) || (p.year||'').toString().includes(q) || (p.type||'').toLowerCase().includes(q) || (p.note||'').toLowerCase().includes(q));
      }
      totalVisible += items.length;

      const rows = items.map((p, idx)=>{
        const badge = /Editor.s Choice|Best Paper|Project of the Year|Recognized by ITS/i.test(p.cite)
          ? '<span class="badge">Honor / Award</span>' : '';
        const noteHtml = (p.note && !/downloads as of/i.test(p.note))
          ? `<div class="pub-note">${p.note.replace(/^(Committee:)/, '<b>$1</b>')}</div>`
          : '';
        const bibText = encodeURIComponent(formatBibtex(p));
        const pubId = `pub-${g.key}-${idx}`;
        const hasLinkCls = p.url ? ' has-link' : '';
        const isFirstAuthor = /^\s*Sakhare\b/i.test(p.cite || '');
        const firstAuthorCls = isFirstAuthor ? ' is-first-author' : '';
        const urlAttr = p.url ? ` data-url="${p.url}" tabindex="0" role="link" title="Open publication in new tab"` : '';

        return `<div class="pub${hasLinkCls}${firstAuthorCls}" id="${pubId}"${urlAttr}>
          <div class="yr">${p.year||''}</div>
          <div>
            <p class="cite">${bold(p.cite)}${badge}</p>
            ${noteHtml}
            <div class="pub-actions">
              ${p.url ? `<a class="pub-doi" href="${p.url}" target="_blank" rel="noopener"><span>${p.url.replace(/^https?:\/\//,'')}</span> ↗</a>` : ''}
              <button class="btn-bib" data-bib="${bibText}" title="Copy BibTeX citation">Copy BibTeX</button>
            </div>
          </div>
        </div>`;
      }).join('');

      const isHidden = (filterKey !== 'all' && g.key !== filterKey) || items.length === 0;
      return `<section class="pub-group${isHidden ? ' hidden' : ''}" data-group="${g.key}">
        <h2>${g.label}</h2><div class="gcount">${items.length} ${items.length===1?'entry':'entries'}</div>
        <div class="pub-list">${rows}</div></section>`;
    }).join('');

    const noMatches = document.getElementById('no-matches');
    if (noMatches){
      noMatches.classList.toggle('hidden', totalVisible > 0);
    }
  };

  renderPubs('all', '');

  // Filter button clicks
  if (bar){
    bar.addEventListener('click',(e)=>{
      const b = e.target.closest('.filter'); if(!b) return;
      bar.querySelectorAll('.filter').forEach(f=>f.classList.toggle('active',f===b));
      const f = b.dataset.f;
      const searchInput = document.getElementById('pub-search-input');
      const q = searchInput ? searchInput.value : '';
      root.querySelectorAll('.pub-group').forEach(grp=>{
        const isTypeMatch = (f === 'all' || grp.dataset.group === f);
        const hasVisibleChildren = grp.querySelectorAll('.pub').length > 0;
        grp.classList.toggle('hidden', !isTypeMatch || !hasVisibleChildren);
      });
    });
  }

  // Live search input
  const searchInput = document.getElementById('pub-search-input');
  const clearBtn = document.getElementById('pub-clear-btn');
  if (searchInput){
    searchInput.addEventListener('input', ()=>{
      const activeFilter = bar ? (bar.querySelector('.filter.active')?.dataset.f || 'all') : 'all';
      renderPubs(activeFilter, searchInput.value);
      if (clearBtn) clearBtn.classList.toggle('visible', searchInput.value.length > 0);
    });
  }
  if (clearBtn && searchInput){
    clearBtn.addEventListener('click', ()=>{
      searchInput.value = '';
      clearBtn.classList.remove('visible');
      const activeFilter = bar ? (bar.querySelector('.filter.active')?.dataset.f || 'all') : 'all';
      renderPubs(activeFilter, '');
      searchInput.focus();
    });
  }
}

// ---- Projects page filter ----
const pfilters = document.getElementById('proj-filters');
const pgrid = document.getElementById('proj-grid');
if (pfilters && pgrid){
  pfilters.addEventListener('click', (e)=>{
    const btn = e.target.closest('.proj-f-btn');
    if (!btn) return;
    pfilters.querySelectorAll('.proj-f-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    pgrid.querySelectorAll('.pcard').forEach(card => {
      const tag = card.dataset.tag;
      if (filter === 'all' || tag === filter || (filter === 'copi' && tag === 'copi') || (filter === 'pooled' && tag === 'pooled')){
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
}

// ---- media render + filter ----
const mroot = document.getElementById('media-root');
if (mroot && window.MEDIA){
  const KINDS = [
    {key:'press', label:'Press & National News'},
    {key:'agency', label:'Federal & State Agency Features'},
    {key:'industry', label:'Industry Impact'},
    {key:'podcast', label:'Podcasts'},
    {key:'webinar', label:'Webinars'},
    {key:'recognition', label:'Recognition'},
  ];
  const counts = {};
  window.MEDIA.forEach(m=>counts[m.kind]=(counts[m.kind]||0)+1);

  const bar = document.getElementById('media-filters');
  const mk = (key,label,n)=>`<button class="filter${key==='all'?' active':''}" data-f="${key}">${label}<span class="c">${n}</span></button>`;
  if (bar){
    bar.innerHTML = mk('all','All',window.MEDIA.length) +
      KINDS.filter(k=>counts[k.key]).map(k=>mk(k.key,k.label,counts[k.key])).join('');
  }

  const sortedMedia = [...window.MEDIA].sort((a,b)=>(b.year||0)-(a.year||0));

  const listHTML = `<div class="media-list">` + sortedMedia.map(m=>{
    const inner = `<span class="outlet">${m.outlet}</span>
      <span class="title">${m.title}${m.note?`<span class="note">${m.note}</span>`:''}</span>
      <span class="date">${m.date}</span>`;
    const isUsdot = (m.outlet === 'U.S. DOT ITS JPO') || (m.url && m.url.includes('its.dot.gov'));
    const cls = ['mi', m.url ? 'has-link' : 'no-link', isUsdot ? 'usdot-feature' : ''].filter(Boolean).join(' ');
    return m.url
      ? `<a class="${cls}" data-kind="${m.kind}" href="${m.url}" target="_blank" rel="noopener" title="Open article in new tab">${inner}</a>`
      : `<div class="${cls}" data-kind="${m.kind}">${inner}</div>`;
  }).join('') + `</div>`;

  mroot.innerHTML = listHTML;

  if (bar){
    bar.addEventListener('click',(e)=>{
      const b = e.target.closest('.filter'); if(!b) return;
      bar.querySelectorAll('.filter').forEach(f=>f.classList.toggle('active',f===b));
      const f = b.dataset.f;
      mroot.querySelectorAll('.mi').forEach(it=>{
        it.classList.toggle('hidden', f!=='all' && it.dataset.kind!==f);
      });
    });
  }
}

// ---- Global: Clickable list rows with links (.pub.has-link) ----
document.addEventListener('click', (e)=>{
  if (e.target.closest('.btn-bib')) return; // handled by bibtex copy
  if (e.target.closest('a')) return;        // native anchor clicks proceed naturally
  const pub = e.target.closest('.pub.has-link');
  if (pub && pub.dataset.url){
    window.open(pub.dataset.url, '_blank', 'noopener,noreferrer');
  }
});
document.addEventListener('keydown', (e)=>{
  if (e.key === 'Enter'){
    if (e.target.closest('.btn-bib') || e.target.closest('a')) return;
    const pub = e.target.closest('.pub.has-link');
    if (pub && pub.dataset.url && document.activeElement === pub){
      window.open(pub.dataset.url, '_blank', 'noopener,noreferrer');
    }
  }
});

// ---- Global BibTeX Copy Handler (Home, Publications, and all pages) ----
function copyBib(btn, text) {
  let ok = false;
  try {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.top = '0';
    ta.style.left = '0';
    ta.style.width = '2em';
    ta.style.height = '2em';
    ta.style.padding = '0';
    ta.style.border = 'none';
    ta.style.outline = 'none';
    ta.style.boxShadow = 'none';
    ta.style.background = 'transparent';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    ok = document.execCommand('copy');
    document.body.removeChild(ta);
  } catch (_) {
    ok = false;
  }

  // Modern clipboard write as secondary guarantee
  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      navigator.clipboard.writeText(text).catch(() => {});
    } catch (_) {}
  }

  // Immediate visual feedback
  if (!btn.dataset.origText) btn.dataset.origText = btn.textContent;
  btn.textContent = '✓ Copied!';
  btn.classList.add('copied');
  clearTimeout(btn._timer);
  btn._timer = setTimeout(() => {
    btn.textContent = btn.dataset.origText || 'Copy BibTeX';
    btn.classList.remove('copied');
  }, 2000);
}

document.addEventListener('click', (e) => {
  const btn = e.target.closest('.btn-bib');
  if (!btn) return;
  e.preventDefault();
  e.stopPropagation();

  const raw = btn.dataset.bib || '';
  let bib = '';
  try {
    bib = decodeURIComponent(raw);
  } catch (_) {
    bib = raw;
  }
  if (!bib) return;

  copyBib(btn, bib);
});

// ==========================================================================
// VISUAL CHRONICLE (gallery.html) HANDLER
// ==========================================================================
(function initVisualChronicle() {
  const gRoot = document.getElementById('gallery-root');
  if (!gRoot || !window.GALLERY) return;

  let activeYear = 'all';
  let activeCat = 'all';
  let currentItems = [];
  let lightboxIndex = 0;

  const years = ['all', '2026', '2025', '2024', '2023', '2022'];
  const categories = [
    { key: 'all', label: 'All Formats' },
    { key: 'podium', label: 'Podium & Lectern' },
    { key: 'poster', label: 'Posters' },
    { key: 'workshop', label: 'Workshops & Talks' },
    { key: 'awards', label: 'Milestones & Awards' },
    { key: 'field', label: 'Field Deployments' }
  ];

  // Render top filter bars
  const filterContainer = document.getElementById('gallery-filters');
  if (filterContainer) {
    let yearBtns = years.map(y => {
      const lbl = y === 'all' ? 'All Years' : (y === '2022' ? '2022 & Prior' : y);
      return `<button class="filter-btn${y === activeYear ? ' active' : ''}" data-year="${y}">${lbl}</button>`;
    }).join('');

    let catBtns = categories.map(c => {
      return `<button class="filter-btn${c.key === activeCat ? ' active' : ''}" data-cat="${c.key}">${c.label}</button>`;
    }).join('');

    filterContainer.innerHTML = `
      <div class="filter-row">
        <span class="filter-label">Year:</span>
        ${yearBtns}
      </div>
      <div class="filter-row">
        <span class="filter-label">Format:</span>
        ${catBtns}
      </div>
    `;

    filterContainer.addEventListener('click', (e) => {
      const btn = e.target.closest('.filter-btn');
      if (!btn) return;
      if (btn.dataset.year) {
        activeYear = btn.dataset.year;
        filterContainer.querySelectorAll('[data-year]').forEach(b => b.classList.toggle('active', b === btn));
      } else if (btn.dataset.cat) {
        activeCat = btn.dataset.cat;
        filterContainer.querySelectorAll('[data-cat]').forEach(b => b.classList.toggle('active', b === btn));
      }
      renderGallery();
    });
  }

  function getCategoryBadgeClass(cat) {
    return 'badge-' + (cat || 'podium');
  }

  function renderGallery() {
    const filtered = window.GALLERY.filter(item => {
      const matchesYear = (activeYear === 'all')
        ? true
        : (activeYear === '2022' ? item.year <= 2022 : item.year === parseInt(activeYear, 10));
      const matchesCat = (activeCat === 'all') ? true : item.category === activeCat;
      return matchesYear && matchesCat;
    });

    currentItems = filtered;

    if (filtered.length === 0) {
      gRoot.innerHTML = `<div style="text-align:center;padding:60px 20px;color:var(--ink-muted);">
        <p style="font-size:16px;">No entries match the selected filters.</p>
        <button class="filter-btn" onclick="document.querySelector('[data-year=\\'all\\']').click();document.querySelector('[data-cat=\\'all\\']').click();">Reset Filters</button>
      </div>`;
      return;
    }

    const yearGroups = {};
    filtered.forEach(item => {
      const yKey = item.year <= 2022 ? '2022 & Prior' : item.year.toString();
      if (!yearGroups[yKey]) yearGroups[yKey] = [];
      yearGroups[yKey].push(item);
    });

    const sortedYearKeys = Object.keys(yearGroups).sort((a, b) => {
      const valA = parseInt(a, 10) || 2020;
      const valB = parseInt(b, 10) || 2020;
      return valB - valA;
    });

    let html = '';
    sortedYearKeys.forEach(yKey => {
      const itemsInYear = yearGroups[yKey];
      const highlights = itemsInYear.filter(it => it.highlight);
      const moreItems = itemsInYear.filter(it => !it.highlight);

      const isFilteredView = activeYear !== 'all' || activeCat !== 'all';
      const initialCards = isFilteredView ? itemsInYear : (highlights.length ? highlights : itemsInYear.slice(0, 4));
      const extraCards = isFilteredView ? [] : (highlights.length ? moreItems : itemsInYear.slice(4));

      html += `<section class="gallery-year-section" id="year-section-${yKey.replace(/[^0-9]/g, '')}">`;
      html += `<div class="gallery-year-title"><span>${yKey}</span> <span class="gallery-year-count">(${itemsInYear.length} session${itemsInYear.length === 1 ? '' : 's'})</span></div>`;
      html += `<div class="gallery-grid" id="grid-${yKey.replace(/[^0-9]/g, '')}">`;

      const renderCard = (it, isExtra) => {
        const globalIdx = currentItems.indexOf(it);
        const extraCls = isExtra ? ' gallery-item-more' : '';
        const badgeCls = getCategoryBadgeClass(it.category);
        
        let imgHtml = '';
        if (it.image) {
          imgHtml = `<div class="gallery-img-frame">
            <img src="${it.image}" alt="${it.event} - ${it.date}" loading="lazy">
            <span class="gallery-badge ${badgeCls}">${it.badge}</span>
          </div>`;
        } else {
          imgHtml = `<div class="gallery-img-frame gallery-placeholder">
            <div class="placeholder-graphic">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <circle cx="8.5" cy="8.5" r="1.5"/>
                <polyline points="21 15 16 10 5 21"/>
              </svg>
              <span>${it.badge}</span>
            </div>
            <span class="gallery-badge ${badgeCls}">${it.badge}</span>
          </div>`;
        }

        let peopleHtml = '';
        if (it.people && it.people.length) {
          peopleHtml = `<div class="gallery-people"><b>With:</b> ${it.people.join(', ')}</div>`;
        }

        let linkHtml = '';
        if (it.link) {
          linkHtml = `<a href="${it.link}" target="_blank" rel="noopener" class="gallery-link" onclick="event.stopPropagation()">Session / Document ↗</a>`;
        }

        return `
          <div class="gallery-card${extraCls}" data-idx="${globalIdx}" onclick="openLightbox(${globalIdx})">
            ${imgHtml}
            <div class="gallery-body">
              <div class="gallery-meta">
                <span>${it.date}</span> · <span>${it.location}</span>
              </div>
              <h3 class="gallery-event">${it.event}</h3>
              <p class="gallery-caption">${it.caption}</p>
              ${peopleHtml}
              ${linkHtml}
            </div>
          </div>
        `;
      };

      initialCards.forEach(it => {
        html += renderCard(it, false);
      });

      if (extraCards.length > 0) {
        extraCards.forEach(it => {
          html += renderCard(it, true);
        });
      }

      html += `</div>`; // end grid

      if (extraCards.length > 0) {
        const secId = yKey.replace(/[^0-9]/g, '');
        html += `
          <div class="discover-more-wrap" id="wrap-more-${secId}">
            <button class="btn-discover-more" onclick="toggleYearMore('${secId}', this)">+ Discover ${extraCards.length} More ${yKey} Session${extraCards.length === 1 ? '' : 's'}</button>
          </div>
        `;
      }

      html += `</section>`;
    });

    gRoot.innerHTML = html;
  }

  // Toggle year extra sessions
  window.toggleYearMore = function(secId, btn) {
    const grid = document.getElementById('grid-' + secId);
    if (!grid) return;
    const moreItems = grid.querySelectorAll('.gallery-item-more');
    const isExpanded = btn.getAttribute('data-expanded') === 'true';

    if (isExpanded) {
      moreItems.forEach(el => el.classList.remove('expanded'));
      btn.setAttribute('data-expanded', 'false');
      btn.textContent = btn.getAttribute('data-orig-text') || '+ Discover More Sessions';
    } else {
      if (!btn.getAttribute('data-orig-text')) {
        btn.setAttribute('data-orig-text', btn.textContent);
      }
      moreItems.forEach(el => el.classList.add('expanded'));
      btn.setAttribute('data-expanded', 'true');
      btn.textContent = '– Show Key Highlights Only';
    }
  };

  // Lightbox Modal Setup
  const lightbox = document.getElementById('gallery-lightbox');
  const lbImg = document.getElementById('lightbox-img');
  const lbInfo = document.getElementById('lightbox-info');

  window.openLightbox = function(idx) {
    if (!currentItems || idx < 0 || idx >= currentItems.length) return;
    lightboxIndex = idx;
    const it = currentItems[lightboxIndex];

    if (it.image) {
      lbImg.src = it.image;
      lbImg.style.display = 'block';
    } else {
      lbImg.style.display = 'none';
    }

    let peopleStr = it.people && it.people.length ? `<p style="font-size:13px;color:var(--ink-muted);margin:8px 0;"><b>Attendees &amp; Collaborators:</b> ${it.people.join(', ')}</p>` : '';
    let linkStr = it.link ? `<p style="margin-top:12px;"><a href="${it.link}" target="_blank" rel="noopener" class="gallery-link" style="font-size:13px;">View Session Details &amp; Publications ↗</a></p>` : '';

    lbInfo.innerHTML = `
      <div style="font-size:12.5px;color:var(--ink-muted);font-weight:600;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:4px;">
        <span class="gallery-badge ${getCategoryBadgeClass(it.category)}" style="position:static;display:inline-block;margin-right:8px;">${it.badge}</span>
        ${it.date} · ${it.location}
      </div>
      <h2 style="font-family:var(--font-serif);font-size:22px;color:var(--ink-heading);margin:8px 0 12px 0;line-height:1.3;">${it.event}</h2>
      <p style="font-size:15px;color:var(--ink-body);line-height:1.6;margin:0 0 8px 0;">${it.caption}</p>
      ${peopleStr}
      ${linkStr}
      <div style="font-size:12px;color:var(--ink-muted);margin-top:16px;border-top:1px solid var(--border);padding-top:10px;">
        Photo ${lightboxIndex + 1} of ${currentItems.length}
      </div>
    `;

    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.closeLightbox = function() {
    if (lightbox) {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  window.nextLightbox = function() {
    if (currentItems.length <= 1) return;
    lightboxIndex = (lightboxIndex + 1) % currentItems.length;
    openLightbox(lightboxIndex);
  };

  window.prevLightbox = function() {
    if (currentItems.length <= 1) return;
    lightboxIndex = (lightboxIndex - 1 + currentItems.length) % currentItems.length;
    openLightbox(lightboxIndex);
  };

  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-box')) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') nextLightbox();
      if (e.key === 'ArrowLeft') prevLightbox();
    });
  }

  // Initial render
  renderGallery();
})();

