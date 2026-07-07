#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer (v2)."""

FONTS = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Public+Sans:wght@400;500;600;700&display=swap"

I = {  # minimal inline icons (stroke, currentColor)
 "user":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 19.5c1.8-3.2 4.3-4.7 7.5-4.7s5.7 1.5 7.5 4.7"/></svg>',
 "target":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.6"/><path d="M12 4V2M12 22v-2M4 12H2M22 12h-2"/></svg>',
 "book":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H12v15H6.5A2.5 2.5 0 0 0 4 20.5zM20 5.5A2.5 2.5 0 0 0 17.5 3H12v15h5.5a2.5 2.5 0 0 1 2.5 2.5z"/></svg>',
 "cap":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 4 2 9l10 5 10-5-10-5z"/><path d="M6 11.5V16c0 1.6 2.7 3 6 3s6-1.4 6-3v-4.5"/><path d="M22 9v5"/></svg>',
 "trophy":'<svg class="ico" viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5a3 3 0 0 0 3 4.5M16 5h3a3 3 0 0 1-3 4.5"/><path d="M12 13v3.5M8.5 20h7M10 16.5h4v3.5h-4z"/></svg>',
 "board":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v2M8.5 21l3.5-3 3.5 3M7 8h6M7 11h9"/></svg>',
 "news":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
 "camera":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13" r="3.6"/><path d="M8.5 7l1.4-2.4h4.2L15.5 7"/></svg>',
 "mail":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7.5l9 6 9-6"/></svg>',
 "scholar":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 3 2 8.5l10 5.5 10-5.5z"/><path d="M7 11.5v5c0 1.5 2.2 2.8 5 2.8s5-1.3 5-2.8v-5"/></svg>',
 "linkedin":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M8 10.5V17M8 7.6v.1M12 17v-4a2.4 2.4 0 0 1 4.8 0v4"/></svg>',
 "orcid":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 8.5v7M9 6.7v.1M12.5 15.5v-7h2a3.5 3.5 0 0 1 0 7z"/></svg>',
 "rg":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 16V8h3a2.3 2.3 0 0 1 .9 4.4L15 16"/></svg>',
 "cuecar":'<svg class="cuecar" viewBox="0 0 36 66" fill="none" xmlns="http://www.w3.org/2000/svg"><line class="cue-road" x1="5" y1="0" x2="5" y2="66"/><line class="cue-road" x1="31" y1="0" x2="31" y2="66"/><g class="cue-body"><line class="cue-wheel" x1="11" y1="20" x2="11" y2="27"/><line class="cue-wheel" x1="25" y1="20" x2="25" y2="27"/><line class="cue-wheel" x1="11" y1="39" x2="11" y2="46"/><line class="cue-wheel" x1="25" y1="39" x2="25" y2="46"/><rect x="11.5" y="15" width="13" height="36" rx="5.5" fill="#F1EFE9" stroke="currentColor" stroke-width="1.6"/><path d="M13.5 38.5c1.4 1.8 2.8 2.6 4.5 2.6s3.1-.8 4.5-2.6" stroke="currentColor" stroke-width="1.3"/><path d="M14 24.5c1.2-1.4 2.5-2 4-2s2.8.6 4 2" stroke="currentColor" stroke-width="1.3"/><line x1="11.5" y1="33" x2="8.5" y2="31.5" stroke="currentColor" stroke-width="1.4"/><line x1="24.5" y1="33" x2="27.5" y2="31.5" stroke="currentColor" stroke-width="1.4"/></g></svg>',
}

NAV_ITEMS = [("about.html","About"),("research.html","Research"),("publications.html","Publications"),
 ("education.html","Education"),("awards.html","Awards"),("teaching.html","Teaching"),
 ("news.html","News"),("gallery.html","Gallery"),("contact.html","Contact")]

def head(title, desc, body_cls):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body class="{body_cls}">"""

def nav(active):
    links = "".join(
        f'<li><a href="{h}"{" class=\"active\"" if h==active else ""}>{t}</a></li>'
        for h,t in NAV_ITEMS)
    return f"""<header class="site-head" id="site-head">
  <nav class="wrap nav" aria-label="Primary">
    <a class="brand" href="index.html">Rahul&nbsp;Sakhare<span class="dot">.</span></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <ul class="nav-links">{links}<li><a class="cv" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">CV ↗</a></li></ul>
  </nav>
</header>
<main>"""

def foot(right="West Lafayette, IN", scripts=""):
    return f"""</main>
<footer class="foot wrap">
  <span>© 2026 Rahul Suryakant Sakhare</span>
  <span>{right}</span>
</footer>
{scripts}<script src="script.js"></script>
</body>
</html>"""

P = {}

# ================= HOME =================
P["index.html"] = head("Rahul Sakhare, Ph.D., P.E. | Transportation Engineer & Researcher",
 "Rahul Sakhare — transportation engineer and researcher at Purdue University, working across infrastructure, emerging technology, teaching, and applied research.",
 "home") + nav("") + f"""
  <section class="hero wrap">
    <div class="hero-inner">
      <div>
        <p class="loc">TRANSPORTATION RESEARCH ENGINEER · <b>PURDUE UNIVERSITY</b> · WEST LAFAYETTE, IN</p>
        <h1>Engineering <span class="flow">safer, smarter</span> transportation.</h1>
        <p class="lede">I'm a transportation engineer who pairs civil-engineering fundamentals with emerging technology — turning research into performance measures, teaching, and tools that agencies actually use, from traffic safety and work zones to winter operations.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="research.html">Explore research →</a>
          <a class="btn btn-ghost" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">Download CV</a>
          <a class="btn btn-ghost" href="contact.html">Get in touch</a>
        </div>
      </div>
      <div class="hero-photo"><img src="assets/img/hero_blend.webp" alt="Rahul Sakhare" width="760" height="701"></div>
    </div>
    <div class="readout" role="group" aria-label="Research metrics">
      <div class="cell"><div class="numline"><div class="num" id="stat-cites" data-to="476">476</div></div><div class="lab">Citations</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-h" data-to="13">13</div></div><div class="lab">h-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-i10" data-to="18">18</div></div><div class="lab">i10-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-journal" data-to="31">31</div></div><div class="lab">Journal articles</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-report" data-to="22">22</div></div><div class="lab">Technical reports</div></div>
      <div class="cell"><div class="numline"><span class="pre">&gt;</span><div class="num" id="dl-num" data-to="37532">37,532</div></div><div class="lab">Downloads &amp; views</div><div class="asof" id="dl-asof">as of Jul 1, 2026</div></div>
    </div>
    <div class="dirgrid">
      <a class="dirc" href="about.html"><div class="dh">{I["user"]}<span class="t">About</span></div>
        <ul><li>Transportation Research Engineer at Purdue's Joint Transportation Research Program</li>
        <li>Licensed PE (Indiana) working where civil engineering meets data and emerging technology</li></ul>
        <span class="go">Read more →</span></a>
      <a class="dirc" href="research.html"><div class="dh">{I["target"]}<span class="t">Research</span></div>
        <ul><li>Six focus areas spanning traffic safety, work zones, and scalable performance measures</li>
        <li>Deployed statewide with INDOT and FHWA — including the 2024 solar-eclipse mobility study</li></ul>
        <span class="go">Explore →</span></a>
      <a class="dirc" href="publications.html"><div class="dh">{I["book"]}<span class="t">Publications</span></div>
        <ul><li>31 peer-reviewed journal articles and 22 technical reports — 91 entries in all</li>
        <li>Every entry links straight to its DOI or archive</li></ul>
        <span class="go">Browse →</span></a>
      <a class="dirc" href="education.html"><div class="dh">{I["cap"]}<span class="t">Education</span></div>
        <ul><li>Ph.D. in Civil Engineering, Purdue University (2023)</li>
        <li>Dual degree — B.Tech. &amp; M.Tech. — from IIT Madras (2018)</li></ul>
        <span class="go">See degrees →</span></a>
      <a class="dirc" href="awards.html"><div class="dh">{I["trophy"]}<span class="t">Awards</span></div>
        <ul><li>Google Cloud Research Innovator, 2024 cohort</li>
        <li>ITS Midwest Project of the Year (2021) and an Editor's Choice journal award</li></ul>
        <span class="go">View honors →</span></a>
      <a class="dirc" href="teaching.html"><div class="dh">{I["board"]}<span class="t">Teaching</span></div>
        <ul><li>Course instructor under the Government of India's SPARC initiative</li>
        <li>Mentoring graduate and undergraduate researchers at JTRP</li></ul>
        <span class="go">Learn more →</span></a>
      <a class="dirc" href="news.html"><div class="dh">{I["news"]}<span class="t">News &amp; Media</span></div>
        <ul><li>Research featured on the front page of The New York Times (Dec 2024)</li>
        <li>Coverage from FHWA, Google Cloud, USDOT, and 20+ outlets</li></ul>
        <span class="go">See coverage →</span></a>
      <a class="dirc" href="gallery.html"><div class="dh">{I["camera"]}<span class="t">Gallery</span></div>
        <ul><li>Photos from the field, conferences, and campus</li>
        <li>New — images coming soon</li></ul>
        <span class="go">Take a look →</span></a>
    </div>
  </section>
  <div class="scroll-cue" id="scroll-cue" aria-hidden="true">{I["cuecar"]}</div>
""" + foot("Built for research · West Lafayette, IN", '<script src="pubs-data.js"></script>\n')

# ================= ABOUT =================
P["about.html"] = head("About | Rahul Sakhare, Ph.D., P.E.",
 "About Rahul Sakhare — Transportation Research Engineer at Purdue University's Joint Transportation Research Program.",
 "sub") + nav("about.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["user"]} About</span>
    <h1>Research that reaches practice.</h1>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div class="about-grid">
      <div>
        <p>I'm a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP). My foundation is civil and transportation engineering; my specialty is bringing emerging technology to it — most notably connected-vehicle data, which I turn into performance measures that transportation agencies can act on. The work spans traffic safety, work zones, winter and incident operations, and vehicle-based metrics such as hard braking as surrogate safety measures.</p>
        <p>Much of this research is deployed at statewide scale with INDOT and FHWA, and has informed how agencies monitor mobility during winter storms, work zones, and large events like the 2024 solar eclipse. Alongside research, I teach, mentor students, serve on TRB and Purdue Road School committees, and translate findings for practitioners and the press. I earned my Ph.D. at Purdue, my bachelor's and master's at IIT Madras, and I'm a licensed Professional Engineer in Indiana.</p>
        <div class="interests">
          <span class="tag">Transportation Engineering</span>
          <span class="tag">Connected Vehicle Data</span>
          <span class="tag">Surrogate Safety Measures</span>
          <span class="tag">Work Zone Safety</span>
          <span class="tag">Big Data Analytics</span>
          <span class="tag">Connected &amp; Autonomous Vehicles</span>
          <span class="tag">Traffic Shock Wave Theory</span>
          <span class="tag">Scalable Performance Measures</span>
        </div>
      </div>
      <aside class="about-card">
        <h3>At a glance</h3>
        <div class="row"><b>Role</b><span>Transportation Research Engineer</span></div>
        <div class="row"><b>Lab</b><span>JTRP, Purdue University</span></div>
        <div class="row"><b>Based in</b><span>West Lafayette, IN</span></div>
        <div class="row"><b>License</b><span>Professional Engineer (Indiana)</span></div>
        <div class="row"><b>Certified</b><span>Google Cloud Generative AI Leader</span></div>
        <div class="row"><b>TRB committee</b><span>ACF13 — Limited Access Roadway Operations</span></div>
      </aside>
    </div>
  </section>
  <section class="section wrap">
    <span class="eyebrow">Experience</span>
    <h2>Path so far.</h2>
    <div class="timeline">
      <div class="tl-item"><div class="tl-date">Aug 2023 — Present</div><div class="tl-body"><h3>Transportation Research Engineer</h3><div class="org">Joint Transportation Research Program, Purdue University</div><p>Lead connected-vehicle data research for INDOT and FHWA, developing statewide safety and mobility performance measures.</p></div></div>
      <div class="tl-item"><div class="tl-date">Jan 2020 — May 2023</div><div class="tl-body"><h3>Graduate Research Assistant</h3><div class="org">Purdue University · Advisor: Prof. Darcy M. Bullock</div><p>Ph.D. research on connected-vehicle data for operational decision-making across mobility, safety, and winter operations.</p></div></div>
      <div class="tl-item"><div class="tl-date">Jul 2018 — Nov 2019</div><div class="tl-body"><h3>Executive Consultant, Transportation</h3><div class="org">Ernst &amp; Young (EY) LLP · New Delhi, India</div><p>Advised on transportation strategy and infrastructure programs.</p></div></div>
      <div class="tl-item"><div class="tl-date">2016 &amp; 2017</div><div class="tl-body"><h3>Visiting Undergraduate Researcher · PURE Scholar</h3><div class="org">Purdue University</div><p>Among the top three civil-engineering students chosen across India for the Purdue Undergraduate Research Experience.</p></div></div>
    </div>
  </section>
""" + foot()

# ================= RESEARCH =================
P["research.html"] = head("Research | Rahul Sakhare, Ph.D., P.E.",
 "Research focus areas — connected vehicle data, surrogate safety measures, work zones, and scalable performance measures.",
 "sub") + nav("research.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["target"]} Research</span>
    <h1>Focus areas.</h1>
    <p>Six threads run through my work — all aimed at making massive vehicle datasets usable, safe-by-design, and adoptable by agencies. Hover over any area for the detail behind it.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <div class="grid">
      <div class="card" tabindex="0"><span class="ic">01</span><h3>Connected Vehicle Data Applications</h3><p>Deriving segment-level mobility and safety metrics from billions of connected-vehicle and probe records at 3-second fidelity.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> national interstate mobility analyses, border-crossing delay monitoring, and dash-camera coverage assessment across the U.S. truck fleet — published across IEEE Access, TRIP, and Future Transportation.</div></div>
      <div class="card" tabindex="0"><span class="ic">02</span><h3>Surrogate Safety Measures</h3><p>Evaluating hard braking, hard acceleration, and deceleration as early indicators of crash risk across intersections, roundabouts, and freeways.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> Co-PI on INDOT SPR-4928 screening the network for hard-braking events; studies tying hard braking to secondary crashes and interchange crash incidents — the evidence base for proactive safety programs.</div></div>
      <div class="card" tabindex="0"><span class="ic">03</span><h3>Work Zone Safety &amp; Analytics</h3><p>Performance measures for work zones that map to the FHWA Work Zone Safety and Mobility Rule, deployed statewide in Indiana.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> queue-truck alerts recognized as ITS Midwest 2021 Project of the Year, automated worksite speed enforcement evaluation, and Editor's Choice work-zone monitoring methodology in the journal Safety.</div></div>
      <div class="card" tabindex="0"><span class="ic">04</span><h3>Incident &amp; Winter Operations</h3><p>Quantifying mobility impacts of winter storms, incidents, and recovery-resource delay to support real-time agency decisions.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> national winter-storm mobility readouts used by decision-makers and media, snowplow telematics calibration, and incident-management performance-measure databases for INDOT.</div></div>
      <div class="card" tabindex="0"><span class="ic">05</span><h3>Big Data &amp; Cloud Analytics</h3><p>Building scalable, cloud-based pipelines and dashboards that make massive trajectory datasets usable for practitioners.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> the JTRP pipeline featured in a Google Cloud customer story; connected-vehicle dashboards for the TMC of the future; selected to the Google Cloud Research Innovators 2024 cohort.</div></div>
      <div class="card" tabindex="0"><span class="ic">06</span><h3>Scalable Performance Measures</h3><p>Translating research methods into repeatable, statewide measures that DOTs and FHWA can adopt directly.</p><span class="more">Hover for detail</span>
        <div class="pop"><b>In practice:</b> interstate speed profiles, signalized-intersection screening, and pavement-condition measures now embedded in INDOT's regular reporting cycles.</div></div>
    </div>
  </section>
  <section class="section wrap">
    <span class="eyebrow">Selected impact</span>
    <h2>Work that made the news.</h2>
    <div class="feat">
      <a class="card" href="https://www.sciencedirect.com/science/article/pii/S2590198224002112" target="_blank" rel="noopener">
        <div class="kicker"><span class="src">Study · TRIP</span><span>2024</span></div>
        <h3>2024 Solar Eclipse: national mobility from 192M connected-truck records</h3>
        <p>Analyzed 192 million records from 240,000 connected trucks to quantify how the total eclipse reshaped highway congestion across 13 states.</p>
        <span class="go">Read the study ↗</span></a>
      <a class="card" href="https://rip.trb.org/View/2404035" target="_blank" rel="noopener">
        <div class="kicker"><span class="src">Project · INDOT SPR-4928 (Co-PI)</span><span>2024–25</span></div>
        <h3>Screening the network for hard-braking &amp; hard-acceleration events</h3>
        <p>Scalable methods that flag risky locations from connected-vehicle trajectories — directly tied to surrogate-safety research.</p>
        <span class="go">View project ↗</span></a>
      <a class="card" href="https://www.mdpi.com/2673-7590/6/1/12" target="_blank" rel="noopener">
        <div class="kicker"><span class="src">Study · Future Transportation</span><span>2026</span></div>
        <h3>Work-zone performance measures mapped to the FHWA Safety &amp; Mobility Rule</h3>
        <p>Turning connected-vehicle data into work-zone safety and mobility measures agencies can report against.</p>
        <span class="go">Read the study ↗</span></a>
      <a class="card" href="publications.html">
        <div class="kicker"><span class="src">Recognition · ITS Midwest</span><span>2021</span></div>
        <h3>Project of the Year — Queue-truck navigation alerts</h3>
        <p>Recognized by ITS Midwest; part of a body of work spanning 31 journal articles and 22 technical reports.</p>
        <span class="go">See all publications →</span></a>
    </div>
  </section>
""" + foot()

# ================= PUBLICATIONS =================
P["publications.html"] = head("Publications | Rahul Sakhare, Ph.D., P.E.",
 "Peer-reviewed journal articles, technical reports, and conference presentations by Rahul Sakhare.",
 "sub") + nav("publications.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["book"]} Publications</span>
    <h1>Publications</h1>
    <p>Peer-reviewed journal articles, technical reports for INDOT &amp; FHWA, and conference presentations on connected-vehicle data, traffic safety, and performance measures. Each card links to its DOI or archive — click anywhere on it.</p>
  </section>
  <div class="wrap"><div class="filters" id="filters"></div></div>
  <div class="wrap"><div id="pub-root"></div></div>
""" + foot("Google Scholar: 476 citations · h-index 13 · i10-index 18",
           '<script src="pubs-data.js"></script>\n')

# ================= EDUCATION =================
P["education.html"] = head("Education | Rahul Sakhare, Ph.D., P.E.",
 "Education — Ph.D. Purdue University; M.Tech. and B.Tech. IIT Madras (dual degree).",
 "sub") + nav("education.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["cap"]} Education</span>
    <h1>Education.</h1>
    <p>Doctoral work at Purdue on connected-vehicle data for operational decisions, built on a transportation-engineering foundation from IIT Madras.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <div class="edu-stack">
      <a class="edu-card reveal" href="https://engineering.purdue.edu/CCE" target="_blank" rel="noopener">
        <span class="edu-visit">Visit university site ↗</span>
        <span class="edu-when">April 2023 · West Lafayette, Indiana</span>
        <h2 class="edu-uni">Purdue University</h2>
        <p class="edu-deg">Doctor of Philosophy (Ph.D.)</p>
        <p class="edu-dept">Lyles School of Civil &amp; Construction Engineering — Transportation &amp; Infrastructure Systems</p>
        <p>Dissertation: "Integrating Connected Vehicle Data for Operational Decision Making." Advisor: Prof. Darcy M. Bullock; committee: Profs. Samuel Labi, Konstantina Gkritza, and James Krogmeier. Supported by the Christopher B. &amp; Susan S. Burke Graduate Research Assistantship.</p>
      </a>
      <a class="edu-card reveal" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">
        <span class="edu-visit">Visit university site ↗</span>
        <span class="edu-when">May 2018 · Chennai, India</span>
        <h2 class="edu-uni">Indian Institute of Technology Madras</h2>
        <p class="edu-deg">Master of Technology (M.Tech.)</p>
        <p class="edu-dept">Department of Civil Engineering — Transportation Engineering</p>
        <p>Completed as part of the five-year dual-degree program. Thesis: "Reliable Corridor Level Travel Time Estimation Using Probe Vehicle Data." Advisor: Prof. Lelitha Devi Vanajakshi. Recognized for exemplary, all-round best performance in the dual-degree program.</p>
      </a>
      <a class="edu-card reveal" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">
        <span class="edu-visit">Visit university site ↗</span>
        <span class="edu-when">May 2018 · Chennai, India</span>
        <h2 class="edu-uni">Indian Institute of Technology Madras</h2>
        <p class="edu-deg">Bachelor of Technology (B.Tech.)</p>
        <p class="edu-dept">Department of Civil Engineering — Minor in Management Studies</p>
        <p>Completed as part of the five-year dual-degree program alongside the M.Tech. Entered through the IIT Joint Entrance Exam ranked in the top 0.2 percentile of 1.45 million candidates.</p>
      </a>
    </div>
  </section>
""" + foot()

# ================= AWARDS =================
P["awards.html"] = head("Awards | Rahul Sakhare, Ph.D., P.E.",
 "Honors and awards — Google Cloud Research Innovator, ITS Midwest Project of the Year, Editor's Choice, and more.",
 "sub") + nav("awards.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["trophy"]} Awards</span>
    <h1>Honors &amp; awards.</h1>
    <p>Recognition across research, practice, and academics — from Google Cloud and ITS Midwest to journal editors and national competitions.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <div class="aw-high">
      <div class="awh">{I["trophy"]}<h3>Google Cloud Research Innovator</h3><div class="by">Google Cloud · fourth global cohort</div><div class="yrp">2024</div></div>
      <div class="awh">{I["trophy"]}<h3>Project of the Year — queue-truck navigation alerts</h3><div class="by">ITS Midwest</div><div class="yrp">2021</div></div>
      <div class="awh">{I["trophy"]}<h3>Editor's Choice Award — work-zone monitoring methodology</h3><div class="by">Safety (journal)</div><div class="yrp">2022</div></div>
      <div class="awh">{I["trophy"]}<h3>International Collegiate Traffic Bowl Championship</h3><div class="by">ITE International</div><div class="yrp">2020</div></div>
      <div class="awh">{I["trophy"]}<h3>Edward J. Cox Memorial Scholarship</h3><div class="by">Indiana ITE Section</div><div class="yrp">2023</div></div>
      <div class="awh">{I["trophy"]}<h3>IGS Best Paper — Geotechnical Testing Journal</h3><div class="by">Indian Geotechnical Society</div><div class="yrp">2016</div></div>
    </div>
    <h2>Timeline.</h2>
    <ul class="aw-line">
      <li><span class="yr">2024</span><div class="what"><b>Google Cloud Research Innovator</b><span>Selected to the fourth global cohort of researchers driving scientific breakthroughs with Google Cloud.</span></div></li>
      <li><span class="yr">2023</span><div class="what"><b>Edward J. Cox Memorial Scholarship</b><span>Indiana ITE Section.</span></div></li>
      <li><span class="yr">2022–23</span><div class="what"><b>Best Student Speaker Award</b><span>Purdue ITE.</span></div></li>
      <li><span class="yr">2022</span><div class="what"><b>Editor's Choice Award</b><span>"Methodology for Monitoring Work Zones Traffic Operations Using Connected Vehicle Data," Safety 8(2).</span></div></li>
      <li><span class="yr">2021</span><div class="what"><b>ITS Midwest Project of the Year</b><span>Evaluation of queue trucks with navigation alerts using connected vehicle data.</span></div></li>
      <li><span class="yr">2021 &amp; 2022</span><div class="what"><b>Elevator Pitch Event Winner</b><span>Purdue ITE.</span></div></li>
      <li><span class="yr">2021</span><div class="what"><b>Student Team Design Competition Winner</b><span>Great Lakes District ITE.</span></div></li>
      <li><span class="yr">2020</span><div class="what"><b>International Collegiate Traffic Bowl Championship</b><span>ITE International.</span></div></li>
      <li><span class="yr">2020</span><div class="what"><b>Best Poster Presentation</b><span>Sigma Xi Scientific Society, Purdue University.</span></div></li>
      <li><span class="yr">2020–2023</span><div class="what"><b>Christopher B. &amp; Susan S. Burke Graduate Research Assistantship</b><span>Purdue University.</span></div></li>
      <li><span class="yr">2018</span><div class="what"><b>Exemplary &amp; All-round Best Performance, Dual-Degree Program</b><span>Civil Engineering, IIT Madras.</span></div></li>
      <li><span class="yr">2018</span><div class="what"><b>Winner, CEA Technical Events</b><span>Case Study, Prabandha, Bon Auto, and Aquanomics — IIT Madras.</span></div></li>
      <li><span class="yr">2017</span><div class="what"><b>Invited Visiting Undergraduate Student</b><span>Purdue University.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>Gold Medal in Civil Engineering</b><span>National Design and Research Forum, Institution of Engineers, India.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>Mr. H. C. Verma Diamond Jubilee Award &amp; IGS Best Paper</b><span>Indian Geotechnical Society.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>PURE Program Scholar</b><span>Among the top three civil-engineering students chosen across India for the Purdue Undergraduate Research Experience.</span></div></li>
      <li><span class="yr">2015</span><div class="what"><b>Winner, Smart City Challenge Vellore</b><span>Engineers for Life Program, AidVision Initiative.</span></div></li>
      <li><span class="yr">2014</span><div class="what"><b>Village's Choice Award · Engineering Case Competition</b><span>Represented India at ECC, Faculty of Engineering, Chulalongkorn University, Thailand.</span></div></li>
      <li><span class="yr">2013</span><div class="what"><b>IIT Joint Entrance Exam — top 0.2 percentile</b><span>Ranked 2,445 of 1.45 million candidates.</span></div></li>
      <li><span class="yr">2011</span><div class="what"><b>Mathematical Olympiad — 4th, Junior Inter Level</b><span>Andhra Pradesh, India; scored 100% in the Secondary School Certificate examination.</span></div></li>
      <li><span class="yr">2009</span><div class="what"><b>Maharashtra Talent Search Examination Scholarship</b><span>Also MS-CIT state certificate in information technology.</span></div></li>
      <li><span class="yr">2008</span><div class="what"><b>All India Open Mathematics Scholarship</b><span>Ranked 41st across India.</span></div></li>
    </ul>
  </section>
""" + foot()

# ================= TEACHING =================
P["teaching.html"] = head("Teaching | Rahul Sakhare, Ph.D., P.E.",
 "Teaching and mentoring — SPARC mobility course, IIT Madras TA, research mentoring at Purdue JTRP.",
 "sub") + nav("teaching.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["board"]} Teaching &amp; mentoring</span>
    <h1>In the classroom &amp; the lab.</h1>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <ul class="teach-list">
      <li><div class="yr">2021</div><div><b>Instructor — SPARC Mobility Course &amp; Workshop</b><p>Developed course material and taught three session modules under the Scheme for Promotion of Academic and Research Collaboration (Government of India initiative).</p></div></li>
      <li><div class="yr">2017–2018</div><div><b>Teaching Assistant — CE2080 Surveying</b><p>Department of Civil Engineering, IIT Madras.</p></div></li>
      <li><div class="yr">Ongoing</div><div><b>Research mentoring</b><p>Mentor graduate and undergraduate researchers at JTRP; judge for the Purdue Spring Undergraduate Research Conference (2024).</p></div></li>
      <li><div class="yr">2021–2022</div><div><b>ITE Purdue Chapter — Executive Board</b><p>Chapter received the ITE Student Chapter Award from ITE International and Outstanding Student Chapter from the Great Lakes District.</p></div></li>
    </ul>
  </section>
""" + foot()

# ================= NEWS =================
P["news.html"] = head("News & Media | Rahul Sakhare, Ph.D., P.E.",
 "Press coverage from The New York Times, FHWA, Google Cloud, Route Fifty, and more.",
 "sub") + nav("news.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["news"]} News &amp; media</span>
    <h1>In the press.</h1>
    <p>Coverage of the research — from the front page of The New York Times to FHWA's Innovator, Google Cloud, and international outlets. Headlines link to the original stories.</p>
  </section>
  <div class="wrap"><div class="filters" id="media-filters"></div></div>
  <section class="section wrap" style="border-top:none;padding-top:24px">
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu", '<script src="media-data.js"></script>\n')

# ================= GALLERY =================
P["gallery.html"] = head("Gallery | Rahul Sakhare, Ph.D., P.E.",
 "Photo gallery — field work, conferences, and campus. Images coming soon.",
 "sub") + nav("gallery.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["camera"]} Gallery</span>
    <h1>Gallery.</h1>
    <p>Photos from the field, conferences, and campus are on their way. Check back soon.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <div class="gal-empty">
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
      <div class="gph">{I["camera"]}<span>Coming soon</span></div>
    </div>
  </section>
""" + foot()

# ================= CONTACT =================
P["contact.html"] = head("Contact | Rahul Sakhare, Ph.D., P.E.",
 "Contact Rahul Sakhare — email, Google Scholar, LinkedIn, ORCID, ResearchGate, and a feedback form.",
 "sub") + nav("contact.html") + f"""
  <section class="contact wrap">
    <span class="eyebrow">{I["mail"]} Contact</span>
    <h2>Let's connect.</h2>
    <p>Open to faculty positions, research collaborations, and conversations about transportation engineering and technology.</p>
    <div class="links">
      <a href="mailto:rsakhare@purdue.edu">{I["mail"]} rsakhare@purdue.edu</a>
      <a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">{I["scholar"]} Google Scholar</a>
      <a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">{I["linkedin"]} LinkedIn</a>
      <a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">{I["orcid"]} ORCID</a>
      <a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">{I["rg"]} ResearchGate</a>
    </div>
    <div style="margin-top:44px" class="about-card">
      <h3>Office</h3>
      <div class="row"><b>Address</b><span>Hall of Discovery &amp; Learning Research, Room 204F<br>207 S. Martin Jischke Drive, West Lafayette, IN 47906</span></div>
    </div>
    <div class="fb-pane">
      <h3>Send a note.</h3>
      <p class="sub">Comments, thoughts, collaboration ideas, or feedback on the site — it goes straight to my Purdue inbox.</p>
      <form class="fb-form" action="https://formsubmit.co/rsakhare@purdue.edu" method="POST">
        <input type="hidden" name="_subject" value="Website feedback — rahulsakhare site">
        <input type="text" name="_honey" style="display:none">
        <div class="fb-row">
          <input type="text" name="name" placeholder="Your name (optional)" autocomplete="name">
          <input type="email" name="email" placeholder="Your email (optional)" autocomplete="email">
        </div>
        <textarea name="message" placeholder="Your message…" required></textarea>
        <button class="btn btn-primary" type="submit">Send →</button>
      </form>
      <p class="fb-note">Prefer email? Write to <a href="mailto:rsakhare@purdue.edu">rsakhare@purdue.edu</a> directly.</p>
    </div>
  </section>
""" + foot()

for name, html in P.items():
    open(name, "w", encoding="utf-8").write(html)
    print("wrote", name)
