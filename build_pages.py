#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer (v5 - Modernized Academic & Systems Portfolio)."""

import os

FONTS = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Inter:wght@400;500;600;700&display=swap"

I = {  # inline SVGs (stroke, currentColor)
 "user":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 19.5c1.8-3.2 4.3-4.7 7.5-4.7s5.7 1.5 7.5 4.7"/></svg>',
 "target":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.6"/><path d="M12 4V2M12 22v-2M4 12H2M22 12h-2"/></svg>',
 "book":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H12v15H6.5A2.5 2.5 0 0 0 4 20.5zM20 5.5A2.5 2.5 0 0 0 17.5 3H12v15h5.5a2.5 2.5 0 0 1 2.5 2.5z"/></svg>',
 "cap":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 4 2 9l10 5 10-5-10-5z"/><path d="M6 11.5V16c0 1.6 2.7 3 6 3s6-1.4 6-3v-4.5"/><path d="M22 9v5"/></svg>',
 "trophy":'<svg class="ico" viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5a3 3 0 0 0 3 4.5M16 5h3a3 3 0 0 1-3 4.5"/><path d="M12 13v3.5M8.5 20h7M10 16.5h4v3.5h-4z"/></svg>',
 "board":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v2M8.5 21l3.5-3 3.5 3M7 8h6M7 11h9"/></svg>',
 "news":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
 "folder":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 4h5l2 3h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg>',
 "mail":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7.5l9 6 9-6"/></svg>',
 "scholar":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 3 2 8.5l10 5.5 10-5.5z"/><path d="M7 11.5v5c0 1.5 2.2 2.8 5 2.8s5-1.3 5-2.8v-5"/></svg>',
 "linkedin":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M8 10.5V17M8 7.6v.1M12 17v-4a2.4 2.4 0 0 1 4.8 0v4"/></svg>',
 "orcid":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 8.5v7M9 6.7v.1M12.5 15.5v-7h2a3.5 3.5 0 0 1 0 7z"/></svg>',
 "rg":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 16V8h3a2.3 2.3 0 0 1 .9 4.4L15 16"/></svg>',
 "cuecar":'<svg class="cuecar" viewBox="0 0 36 66" fill="none" xmlns="http://www.w3.org/2000/svg"><line class="cue-road" x1="5" y1="0" x2="5" y2="66"/><line class="cue-road" x1="31" y1="0" x2="31" y2="66"/><g class="cue-body"><line class="cue-wheel" x1="11" y1="20" x2="11" y2="27"/><line class="cue-wheel" x1="25" y1="20" x2="25" y2="27"/><line class="cue-wheel" x1="11" y1="39" x2="11" y2="46"/><line class="cue-wheel" x1="25" y1="39" x2="25" y2="46"/><rect x="11.5" y="15" width="13" height="36" rx="5.5" fill="#FAF9F6" stroke="currentColor" stroke-width="1.6"/><path d="M13.5 38.5c1.4 1.8 2.8 2.6 4.5 2.6s3.1-.8 4.5-2.6" stroke="currentColor" stroke-width="1.3"/><path d="M14 24.5c1.2-1.4 2.5-2 4-2s2.8.6 4 2" stroke="currentColor" stroke-width="1.3"/><line x1="11.5" y1="33" x2="8.5" y2="31.5" stroke="currentColor" stroke-width="1.4"/><line x1="24.5" y1="33" x2="27.5" y2="31.5" stroke="currentColor" stroke-width="1.4"/></g></svg>',
}

NAV_ITEMS = [
 ("about.html","About"),
 ("research.html","Research & Systems"),
 ("projects.html","Projects"),
 ("publications.html","Publications"),
 ("teaching.html","Teaching"),
 ("education.html","Education"),
 ("awards.html","Awards"),
 ("news.html","News"),
 ("contact.html","Contact")
]

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
    link_items = []
    for h, t in NAV_ITEMS:
        cls_attr = ' class="active"' if h == active else ''
        link_items.append(f'<li><a href="{h}"{cls_attr}>{t}</a></li>')
    links = "".join(link_items)
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
  <span>© 2026 Rahul Suryakant Sakhare, Ph.D., P.E.</span>
  <span>{right}</span>
</footer>
{scripts}<script src="script.js"></script>
</body>
</html>"""

P = {}

# =========================================================================
# 1. HOME (index.html)
# =========================================================================
P["index.html"] = head("Rahul Sakhare, Ph.D., P.E. | Transportation Cyber-Physical Systems & Data Science",
 "Rahul Sakhare, Ph.D., P.E. — Transportation Research Engineer at Purdue University. Bridging civil infrastructure physics, distributed cloud computing, and applied machine vision.",
 "home") + nav("") + f"""
  <section class="hero wrap">
    <div class="hero-inner">
      <div>
        <p class="loc">TRANSPORTATION RESEARCH ENGINEER · <b>PURDUE UNIVERSITY</b> · LICENSED P.E. (INDIANA)</p>
        <h1>Rahul Sakhare<span class="creds">, Ph.D., P.E.</span></h1>
        <p class="tagline">Bridging <span class="flow">Physical Infrastructure</span> &amp; <span class="flow">Scalable Computing</span>.</p>
        <p class="lede">Operating at the intersection of civil infrastructure physics, distributed cloud computing, and applied machine vision. I develop scalable Transportation Cyber-Physical Systems (TCPS) deployed statewide and nationally to observe, diagnose, and optimize real-world highway networks.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="research.html">Explore Research &amp; Systems →</a>
          <a class="btn btn-ghost" href="projects.html">Funded Projects ($6M+)</a>
          <a class="btn btn-ghost" href="publications.html">Publications (91)</a>
          <a class="btn btn-ghost" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">Download CV ↗</a>
        </div>
      </div>
      <div class="hero-photo"><img src="assets/img/hero_photo.jpg" alt="Rahul Sakhare, Ph.D., P.E." width="1000" height="666"></div>
    </div>

    <!-- Live Metric Readout -->
    <div class="readout" role="group" aria-label="Research metrics">
      <div class="cell"><div class="numline"><div class="num" id="stat-cites" data-to="521">521</div></div><div class="lab">Citations</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-h" data-to="13">13</div></div><div class="lab">h-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-i10" data-to="19">19</div></div><div class="lab">i10-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-journal" data-to="31">31</div></div><div class="lab">Journal articles</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-report" data-to="22">22</div></div><div class="lab">Technical reports</div></div>
      <div class="cell"><div class="numline"><span class="pre">&gt;</span><div class="num" id="dl-num" data-to="35566">35,566</div></div><div class="lab">Downloads &amp; views</div><div class="asof" id="dl-asof">as of Jul 8, 2026</div></div>
      <div class="cell"><div class="numline"><span class="pre">$</span><div class="num" data-to="6">6.0</div><span class="pre">M+</span></div><div class="lab">Funded Research (Co-PI &amp; RE)</div></div>
    </div>

    <!-- Featured Production Systems -->
    <div style="margin-top:14px">
      <span class="eyebrow">{I["target"]} Operational Platforms</span>
      <h2>Featured Deployed Systems.</h2>
      <p style="color:var(--muted);max-width:68ch;margin:0 0 28px;font-size:17px">Production-scale software platforms, diagnostic tools, and cyber-physical systems actively utilized by state DOTs and federal programs.</p>

      <div class="systems-stack">
        <!-- System 1 -->
        <article class="sys-card">
          <div class="sys-head">
            <span class="sys-num">01 · STATEWIDE SCREENING PLATFORM</span>
            <div class="sys-badge-group">
              <span class="pill pill-accent">INDOT Central Office &amp; Districts</span>
              <span class="pill pill-blue">108B+ Annual Waypoints</span>
              <span class="pill pill-dark">24,831 Highway Miles</span>
            </div>
          </div>
          <div class="sys-content">
            <div class="sys-visual">
              <img src="assets/img/indiana_segment_pm.webp" alt="Indiana Segment-PM WebGIS Platform" loading="lazy">
            </div>
            <div class="sys-details">
              <h3>Indiana Segment-PM WebGIS Platform</h3>
              <p>Operational cloud-scale analytics platform that converts billions of connected vehicle trajectory points into granular 0.1-mile segment performance measures across the entire state highway network.</p>
              <div class="sys-metrics">
                <div class="sys-m-cell"><div class="num">0.1 mi</div><div class="lab">Spatial Resolution</div></div>
                <div class="sys-m-cell"><div class="num">0th–100th</div><div class="lab">Speed Percentiles</div></div>
                <div class="sys-m-cell"><div class="num">24,831 mi</div><div class="lab">Statewide Coverage</div></div>
                <div class="sys-m-cell"><div class="num">Daily</div><div class="lab">Agency Decision Use</div></div>
              </div>
              <p style="font-size:13.5px;color:var(--muted)"><b>Impact:</b> Replaced costly manual field studies. Actively used by INDOT capital program committees to rank and prioritize statewide safety, signal retiming, and capacity investments.</p>
              <div class="sys-links">
                <a href="research.html#system-segment-pm">Explore Architecture &amp; Methodology →</a>
              </div>
            </div>
          </div>
        </article>

        <!-- System 2 -->
        <article class="sys-card">
          <div class="sys-head">
            <span class="sys-num">02 · FORENSIC TRAFFIC ENGINE</span>
            <div class="sys-badge-group">
              <span class="pill pill-accent">FHWA Pooled-Fund TPF-5(514)</span>
              <span class="pill pill-gold">506-Page Monograph</span>
              <span class="pill pill-blue">Live Cloud Run Portal</span>
            </div>
          </div>
          <div class="sys-content">
            <div class="sys-visual">
              <img src="assets/img/heatmap_tool.webp" alt="Multi-State Heatmap Diagnostic Tool" loading="lazy">
            </div>
            <div class="sys-details">
              <h3>Multi-State Spatiotemporal Heatmap Diagnostic Tool</h3>
              <p>Interactive forensic diagnostic tool that generates 24-hour space-mean speed contours plotted against mileposts, enabling traffic engineers to visualize shockwave propagation and disentangle multi-hazard congestion causes.</p>
              <div class="sys-metrics">
                <div class="sys-m-cell"><div class="num">24 hr</div><div class="lab">Continuous Contours</div></div>
                <div class="sys-m-cell"><div class="num">$0.055</div><div class="lab">BigQuery Cost / Query</div></div>
                <div class="sys-m-cell"><div class="num">Multi-Layer</div><div class="lab">Car, Truck, IoT, Weather</div></div>
                <div class="sys-m-cell"><div class="num">Multi-State</div><div class="lab">Midwest &amp; National DOTs</div></div>
              </div>
              <p style="font-size:13.5px;color:var(--muted)"><b>Impact:</b> Evaluates road weather speed degradation during winter storms, tracks queue shockwave velocities upstream of construction zones, and serves as an authoritative national standard.</p>
              <div class="sys-links">
                <a href="https://doi.org/10.5703/1288284317751" target="_blank" rel="noopener">Access 506-Page FHWA Monograph ↗</a>
                <a href="research.html#system-heatmap">View Diagnostic Engine Details →</a>
              </div>
            </div>
          </div>
        </article>

        <!-- System 3 -->
        <article class="sys-card">
          <div class="sys-head">
            <span class="sys-num">03 · PASSIVE REALITY CAPTURE &amp; APPLIED AI</span>
            <div class="sys-badge-group">
              <span class="pill pill-accent">IEEE Access &amp; JTTs</span>
              <span class="pill pill-gold">Edge YOLO Machine Vision</span>
              <span class="pill pill-blue">Multimodal LLM Audits</span>
            </div>
          </div>
          <div class="sys-content">
            <div class="sys-visual-multi">
              <img src="assets/img/dashcam_yolo.webp" alt="Edge YOLO Deep Learning Detection in Work Zone" loading="lazy">
              <img src="assets/img/dashcam_llm.webp" alt="Multimodal LLM Natural Language Roadway Querying" loading="lazy">
            </div>
            <div class="sys-details">
              <h3>Commercial Fleet Dashcam AI &amp; Digital Twin Portal</h3>
              <p>Operational computer vision and visual analytics dashboard that ingests 1-Hz forward-facing optical dashcam imagery from commercial freight fleets, combining custom object detection models and multimodal LLMs to automate infrastructure auditing.</p>
              <div class="sys-metrics">
                <div class="sys-m-cell"><div class="num">170</div><div class="lab">Work Zones Audited Weekly</div></div>
                <div class="sys-m-cell"><div class="num">10 States</div><div class="lab">Active Freight Coverage</div></div>
                <div class="sys-m-cell"><div class="num">80–95%</div><div class="lab">24–48h Corridor Revisit</div></div>
                <div class="sys-m-cell"><div class="num">Zero Risk</div><div class="lab">Worker Shoulder Hazards</div></div>
              </div>
              <p style="font-size:13.5px;color:var(--muted)"><b>Impact:</b> Eliminates the hazard of sending maintenance personnel onto high-speed shoulders. Automatically verifies Maintenance of Traffic (MOT) plan compliance and allows engineers to query visual streams via natural language prompts.</p>
              <div class="sys-links">
                <a href="https://doi.org/10.1109/ACCESS.2024.3503368" target="_blank" rel="noopener">Read IEEE Access Study ↗</a>
                <a href="research.html#system-dashcam">Explore Machine Vision Framework →</a>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>

    <!-- Quick Navigation Directory -->
    <div class="dirgrid" style="margin-top:48px">
      <a class="dirc" href="about.html"><div class="dh">{I["user"]}<span class="t">About</span></div>
        <ul><li>Transportation Research Engineer at Purdue's Joint Transportation Research Program</li>
        <li>Licensed P.E. (Indiana) working where civil engineering meets cloud computing and applied AI</li></ul>
        <span class="go">Read background →</span></a>
      <a class="dirc" href="research.html"><div class="dh">{I["target"]}<span class="t">Research &amp; Systems</span></div>
        <ul><li>The TCPS architectural workflow, 3 core research thrusts, and production software tools</li>
        <li>Deployed statewide with INDOT and FHWA — from shockwave control to dashcam digital twins</li></ul>
        <span class="go">Explore research →</span></a>
      <a class="dirc" href="projects.html"><div class="dh">{I["folder"]}<span class="t">Funded Projects</span></div>
        <ul><li>Over $6.0M in externally funded research portfolio across FHWA, INDOT, and CCAT</li>
        <li>Active Co-PI on 4 state grants ($1.13M) and lead researcher on national pooled funds</li></ul>
        <span class="go">View grant portfolio →</span></a>
      <a class="dirc" href="publications.html"><div class="dh">{I["book"]}<span class="t">Publications</span></div>
        <ul><li>31 peer-reviewed journal articles, 22 technical reports, 1 monograph — 91 entries in all</li>
        <li>Live as-you-type search, filter pills, direct DOI links, and one-click BibTeX copy</li></ul>
        <span class="go">Browse publications →</span></a>
      <a class="dirc" href="teaching.html"><div class="dh">{I["board"]}<span class="t">Teaching &amp; Mentoring</span></div>
        <ul><li>Instructional philosophy: "Real-world telematics in the engineering classroom"</li>
        <li>Mentorship roster of graduate and undergraduate researchers across CEE, ECE, CS, and ME</li></ul>
        <span class="go">Learn more →</span></a>
      <a class="dirc" href="news.html"><div class="dh">{I["news"]}<span class="t">News &amp; Media</span></div>
        <ul><li>Research featured on the front page of The New York Times (Dec 2024)</li>
        <li>Coverage from FHWA Innovator, Google Cloud customer story, and national broadcast outlets</li></ul>
        <span class="go">See coverage →</span></a>
    </div>
  </section>
  <div class="scroll-cue" id="scroll-cue" aria-hidden="true">{I["cuecar"]}</div>
""" + foot("Built for research · West Lafayette, IN", '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 2. ABOUT (about.html)
# =========================================================================
P["about.html"] = head("About | Rahul Sakhare, Ph.D., P.E.",
 "About Rahul Sakhare — Transportation Research Engineer at Purdue University, bridging civil infrastructure physics, distributed cloud computing, and applied machine vision.",
 "sub") + nav("about.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["user"]} About</span>
    <h1>Engineering Rigor. Cloud Scale. Real Deployed Impact.</h1>
    <p>I operate as a dual-citizen of civil infrastructure mechanics and scalable computer systems — bridging physical transportation flow principles with distributed cloud data architectures and edge artificial intelligence.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div class="about-grid">
      <div>
        <p>I am a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP). My research foundation is built upon civil and transportation engineering physics, paired with scalable cloud architectures and machine vision. I specialize in turning massive, heterogeneous telemetry streams — including connected vehicle trajectory waypoints, commercial truck telematics, and 1-Hz optical dashcams — into actionable cyber-physical performance measures that public agencies can deploy and sustain.</p>
        <p>Over more than 20 externally funded research projects totaling over $6.0M, I have served as Co-Principal Investigator (Co-PI) on four active Indiana Department of Transportation (INDOT) research grants ($1.13M) and as lead research engineer on multi-state FHWA Pooled-Fund studies. The methodologies and platforms resulting from this work are embedded into statewide operations with INDOT and member state DOTs across the Midwest, informing real-time work zone safety alerts, network-wide 0.1-mile bottleneck screening, severe winter weather recovery, and capital program prioritization.</p>
        <p>Alongside my research program, I teach, mentor graduate and undergraduate researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering, serve on the TRB Committee on Limited Access Roadway Operations (ACF13), and contribute to the annual Purdue Road School Planning Committee. I earned my Ph.D. in Civil Engineering from Purdue University, completed dual B.Tech. and M.Tech. degrees from IIT Madras (ranked top 0.2% in the IIT-JEE), and hold a licensed Professional Engineer (P.E.) credential in Indiana.</p>
        <div class="interests">
          <span class="tag">Transportation Cyber-Physical Systems</span>
          <span class="tag">Connected Vehicle Trajectory Data</span>
          <span class="tag">Surrogate Safety &amp; Deceleration Physics</span>
          <span class="tag">Work Zone Safety &amp; Shockwave Theory</span>
          <span class="tag">Distributed Cloud Analytics (Google BigQuery)</span>
          <span class="tag">Edge Machine Vision (YOLO)</span>
          <span class="tag">Multimodal LLM Infrastructure Auditing</span>
          <span class="tag">Scalable Transportation Performance Measures</span>
        </div>
      </div>
      <aside class="about-card">
        <h3>At a Glance</h3>
        <div class="row"><b>Current Role</b><span>Transportation Research Engineer</span></div>
        <div class="row"><b>Institution</b><span>JTRP, Purdue University</span></div>
        <div class="row"><b>Licensure</b><span>Professional Engineer (P.E.), Indiana</span></div>
        <div class="row"><b>Certification</b><span>Google Cloud Generative AI Leader</span></div>
        <div class="row"><b>Grant Leadership</b><span>Co-PI on 4 Active Grants ($1.13M)</span></div>
        <div class="row"><b>Funded Volume</b><span>$6.0M+ Total Research Involvement</span></div>
        <div class="row"><b>TRB Committee</b><span>ACF13 — Limited Access Roadway Operations</span></div>
        <div class="row"><b>Conference Service</b><span>Purdue Road School Planning Committee</span></div>
      </aside>
    </div>
  </section>
  <section class="section wrap">
    <span class="eyebrow">Professional Appointments</span>
    <h2>Career &amp; Experience.</h2>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-date">Aug 2023 — Present</div>
        <div class="tl-body">
          <h3>Transportation Research Engineer (Post-Doctoral Equivalent)</h3>
          <div class="org">Joint Transportation Research Program (JTRP), Purdue University</div>
          <p>Lead multi-agency connected vehicle data research, cloud analytics pipelines, and machine vision deployments for INDOT, FHWA, and regional pooled-fund consortia. Direct Co-PI on four active research projects.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-date">Jan 2020 — May 2023</div>
        <div class="tl-body">
          <h3>Graduate Research Assistant</h3>
          <div class="org">Purdue University · Advisor: Prof. Darcy M. Bullock</div>
          <p>Doctoral research on integrating connected vehicle data for operational decision-making across mobility, work zone safety, and road weather operations. Supported by the Christopher B. &amp; Susan S. Burke Fellowship.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-date">Jul 2018 — Nov 2019</div>
        <div class="tl-body">
          <h3>Executive Consultant — Transportation Advisory</h3>
          <div class="org">Ernst &amp; Young (EY) LLP · New Delhi, India</div>
          <p>Advised public infrastructure agencies on large-scale transportation strategy, logistics, and corridor infrastructure investment programs.</p>
        </div>
      </div>
      <div class="tl-item">
        <div class="tl-date">2016 &amp; 2017</div>
        <div class="tl-body">
          <h3>Visiting Undergraduate Researcher · PURE Scholar</h3>
          <div class="org">Purdue University</div>
          <p>Selected among the top three civil engineering students across India under the Purdue Undergraduate Research Experience (PURE) program.</p>
        </div>
      </div>
    </div>
  </section>
""" + foot()


# =========================================================================
# 3. RESEARCH & SYSTEMS (research.html)
# =========================================================================
P["research.html"] = head("Research & Systems | Rahul Sakhare, Ph.D., P.E.",
 "Transportation Cyber-Physical Systems (TCPS) — Connected vehicle telematics, cloud network diagnostics, edge machine vision, and production software tools.",
 "sub") + nav("research.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["target"]} Research &amp; Systems</span>
    <h1>Transportation Cyber-Physical Systems (TCPS).</h1>
    <p>Operating at the convergence of civil infrastructure physics, distributed cloud computing, and applied machine vision. We build scalable data-to-decision architectures that turn billions of raw probe records and vehicle video streams into deployed operational intelligence for public agencies.</p>
  </section>

  <!-- Architectural Workflow Section -->
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <span class="eyebrow">Architectural Workflow</span>
    <h2>The TCPS Research Framework.</h2>
    <p class="intro">Our methodology integrates physical sensing, high-performance distributed computing, deep learning machine vision, and closed-loop operational actuation into one seamless cyber-physical pipeline.</p>

    <div class="arch-card">
      <img src="assets/img/tcps_workflow.webp" alt="Architectural Workflow of the Scalable Transportation Cyber-Physical Systems (TCPS) Research Framework" loading="lazy">
      <div class="arch-caption">
        <b>Figure 1: Architectural Workflow of the Scalable Transportation Cyber-Physical Systems (TCPS) Research Framework</b>
        <span>Tier 1: Telematics Ingestion · Tier 2: Cloud-Native Geospatial Aggregation (BigQuery) · Tier 3: Edge Machine Vision &amp; Multimodal AI · Tier 4: Closed-Loop Operational Decision Support</span>
      </div>
    </div>
  </section>

  <!-- Three Core Research Thrusts -->
  <section class="section wrap">
    <span class="eyebrow">Scientific Thrusts</span>
    <h2>Three Core Research Pillars.</h2>
    <div class="grid">
      <!-- Thrust 1 -->
      <div class="card" style="padding-top:20px">
        <span class="ic">THRUST 01</span>
        <h3>Connected Vehicle Telematics &amp; Dynamic Safety Systems</h3>
        <p>Freeway bottleneck queues and temporary work zones generate severe crash risks due to rapid queue formation that outpaces static roadside warnings. We develop closed-loop telematics systems that ingest high-frequency waypoints from vehicles already in the queue to model shockwave propagation velocity (v<sub>sw</sub> = Δq / Δk) and deceleration gradients in real time.</p>
        <div style="margin-top:14px;font-size:14px;color:var(--muted)">
          <p><b>Deployed Reality:</b> Deployed dynamic queue-warning trucks equipped with upstream digital alerts, delivering a documented <b>80% reduction in hard-braking events</b> upstream of bottleneck queues. Developed statewide surrogate safety screening methods linking hard braking to secondary crash prevention.</p>
        </div>
        <span class="more" style="color:var(--accent);font-weight:700">Recognized as ITS Midwest Project of the Year · Safety Editor's Choice Award</span>
      </div>

      <!-- Thrust 2 -->
      <div class="card" style="padding-top:20px">
        <span class="ic">THRUST 02</span>
        <h3>Scalable Cloud-Native Network Diagnostics &amp; Big Data Analytics</h3>
        <p>Conventional physical loop detectors and roadside sensors cover less than 15% of highway networks. Ingesting statewide probe trajectories generates over 10 billion records monthly. We engineer distributed cloud architectures using Google BigQuery geospatial polygon indexing to transform raw trajectory points into 0.1-mile segment performance metrics across 24,831 directional highway miles.</p>
        <div style="margin-top:14px;font-size:14px;color:var(--muted)">
          <p><b>Deployed Reality:</b> Authored the <b>506-page FHWA Monograph (TPF-5(514))</b> establishing standardized national references for 24-hour spatiotemporal speed heatmaps. Quantified statewide mobility degradation during severe winter storms, extreme rain events, and the 2024 total solar eclipse across 13 states.</p>
        </div>
        <span class="more" style="color:var(--accent);font-weight:700">Selected to Google Cloud Research Innovators Global Cohort · 23 CFR Part 490 Compliance</span>
      </div>

      <!-- Thrust 3 -->
      <div class="card" style="padding-top:20px">
        <span class="ic">THRUST 03</span>
        <h3>Applied Machine Vision &amp; Automated Infrastructure Digital Twins</h3>
        <p>Physical highway inspection is among the most hazardous activities in civil engineering, exposing maintenance personnel to fatal struck-by vehicle collisions. We harness routine commercial freight logistics — utilizing 1-Hz optical dashcams across freight fleets traversing 48 states — to create a passive, continuous infrastructure auditing sensor network.</p>
        <div style="margin-top:14px;font-size:14px;color:var(--muted)">
          <p><b>Deployed Reality:</b> Built an edge deep learning (YOLO) and Multimodal LLM (gemini-3.1-flash-lite) portal actively auditing <b>170 active work zones across 10 states</b> weekly for temporary traffic control compliance. Eliminates human maintenance hazards on live highway shoulders.</p>
        </div>
        <span class="more" style="color:var(--accent);font-weight:700">Published in IEEE Access &amp; Journal of Transportation Technologies · 80–95% 48h Corridor Revisit</span>
      </div>

      <!-- Cross-Cutting Impact -->
      <div class="card" style="padding-top:20px">
        <span class="ic">CROSS-CUTTING</span>
        <h3>Public Health, Emissions Equity &amp; Asset Management</h3>
        <p>Bottleneck queues and severe hard-braking cycles generate heavy transient particulate matter (PM2.5) and NOx emissions that disproportionately impact frontline environmental justice communities adjacent to freight corridors. Our speed harmonization and queue smoothing algorithms serve as active emissions-mitigation interventions.</p>
        <div style="margin-top:14px;font-size:14px;color:var(--muted)">
          <p><b>Deployed Reality:</b> Extended vehicle telematics and vertical acceleration signatures to assess statewide pavement roughness (IRI), monitor retroreflectivity degradation, and support data-driven capital investment programs.</p>
        </div>
        <span class="more" style="color:var(--accent);font-weight:700">Featured in TRB Lectern Sessions &amp; Annual Purdue Road School</span>
      </div>
    </div>
  </section>

  <!-- Production Systems Showroom -->
  <section class="section wrap" id="systems">
    <span class="eyebrow">Production Systems Showroom</span>
    <h2>Operational Platforms &amp; Software Tools.</h2>
    <p class="intro">Rather than abstract simulations, each selected system represents a tangible, production-scale software platform actively utilized by public transportation agencies.</p>

    <div class="systems-stack">
      <!-- System 1 -->
      <article class="sys-card" id="system-segment-pm">
        <div class="sys-head">
          <span class="sys-num">SYSTEM 01 · STATEWIDE SCREENING PLATFORM</span>
          <div class="sys-badge-group">
            <span class="pill pill-accent">INDOT Central Office &amp; Districts</span>
            <span class="pill pill-blue">108B+ Annual Waypoints</span>
            <span class="pill pill-dark">24,831 Highway Miles</span>
          </div>
        </div>
        <div class="sys-content">
          <div class="sys-visual">
            <img src="assets/img/indiana_segment_pm.webp" alt="Indiana Segment-PM WebGIS Platform" loading="lazy">
          </div>
          <div class="sys-details">
            <h3>Indiana Segment-PM WebGIS Platform</h3>
            <p>An operational cloud-scale analytics platform that converts billions of connected vehicle trajectory points into granular 0.1-mile segment performance measures across the entire state highway network, resolving localized friction points and intersection queues that aggregate corridor averages obscure.</p>
            <div class="sys-metrics">
              <div class="sys-m-cell"><div class="num">0.1 mi</div><div class="lab">Granular Spatial Segments</div></div>
              <div class="sys-m-cell"><div class="num">0th–100th</div><div class="lab">Full Empirical Speed Percentiles</div></div>
              <div class="sys-m-cell"><div class="num">574k+</div><div class="lab">Waypoints / Segment Sample</div></div>
              <div class="sys-m-cell"><div class="num">23 CFR 490</div><div class="lab">Federal Rule Compliance</div></div>
            </div>
            <p style="font-size:14px;color:var(--muted)"><b>Agency Use Cases:</b> Pinpoints localized bottleneck formation, evaluates interchange spillbacks, and enables district traffic engineers to make immediate operational decisions without waiting for costly manual field studies. Actively incorporated into capital investment committee assessments.</p>
            <div class="sys-links">
              <a href="https://doi.org/10.3390/futuretransp6010012" target="_blank" rel="noopener">Methodology Paper (Future Transportation 2026) ↗</a>
              <a href="projects.html#spr-4857">Associated Project: SPR-4857 →</a>
            </div>
          </div>
        </div>
      </article>

      <!-- System 2 -->
      <article class="sys-card" id="system-heatmap">
        <div class="sys-head">
          <span class="sys-num">SYSTEM 02 · FORENSIC TRAFFIC ENGINE</span>
          <div class="sys-badge-group">
            <span class="pill pill-accent">FHWA Pooled-Fund TPF-5(514)</span>
            <span class="pill pill-gold">506-Page Monograph</span>
            <span class="pill pill-blue">Live Cloud Run Diagnostic Portal</span>
          </div>
        </div>
        <div class="sys-content">
          <div class="sys-visual">
            <img src="assets/img/heatmap_tool.webp" alt="Multi-State Heatmap Diagnostic Tool" loading="lazy">
          </div>
          <div class="sys-details">
            <h3>Multi-State Spatiotemporal Heatmap Diagnostic Tool</h3>
            <p>An interactive forensic diagnostic tool that generates 24-hour space-mean speed contours plotted against mileposts, enabling traffic engineers to visualize shockwave propagation and disentangle multi-hazard congestion causes through synchronized multi-layer overlays.</p>
            <div class="sys-metrics">
              <div class="sys-m-cell"><div class="num">24 hr</div><div class="lab">Space-Mean Speed Contours</div></div>
              <div class="sys-m-cell"><div class="num">$0.055</div><div class="lab">BigQuery Cost / Execution</div></div>
              <div class="sys-m-cell"><div class="num">Multi-Layer</div><div class="lab">Car/Truck Speeds, Weather, IoT</div></div>
              <div class="sys-m-cell"><div class="num">Multi-State</div><div class="lab">Midwest &amp; National Deployment</div></div>
            </div>
            <p style="font-size:14px;color:var(--muted)"><b>Forensic Capabilities:</b> Disentangles recurrent bottleneck demand from non-recurrent events like secondary crashes, active work zone shockwaves, and winter storm recovery. The accompanying 506-page monograph serves as an authoritative national standard for connected vehicle data processing.</p>
            <div class="sys-links">
              <a href="https://doi.org/10.5703/1288284317751" target="_blank" rel="noopener">Download 506-Page Monograph (Purdue e-Pubs) ↗</a>
              <a href="projects.html#tpf-514">Associated Project: FHWA TPF-5(514) →</a>
            </div>
          </div>
        </div>
      </article>

      <!-- System 3 -->
      <article class="sys-card" id="system-dashcam">
        <div class="sys-head">
          <span class="sys-num">SYSTEM 03 · PASSIVE REALITY CAPTURE &amp; APPLIED AI</span>
          <div class="sys-badge-group">
            <span class="pill pill-accent">IEEE Access &amp; JTTs</span>
            <span class="pill pill-gold">Edge YOLO Machine Vision</span>
            <span class="pill pill-blue">Multimodal LLM Audits</span>
          </div>
        </div>
        <div class="sys-content">
          <div class="sys-visual-multi">
            <img src="assets/img/dashcam_yolo.webp" alt="Edge YOLO Deep Learning Detection in Work Zone" loading="lazy">
            <img src="assets/img/dashcam_llm.webp" alt="Multimodal LLM Natural Language Roadway Querying" loading="lazy">
          </div>
          <div class="sys-details">
            <h3>Commercial Fleet Dashcam AI &amp; Digital Twin Portal</h3>
            <p>An operational computer vision and visual analytics dashboard that ingests 1-Hz forward-facing optical dashcam imagery from commercial freight fleets, combining custom object detection models and multimodal LLMs to automate roadway infrastructure and work zone inspection.</p>
            <div class="sys-metrics">
              <div class="sys-m-cell"><div class="num">170</div><div class="lab">Work Zones Monitored Weekly</div></div>
              <div class="sys-m-cell"><div class="num">10 States</div><div class="lab">Continuous Freight Footprint</div></div>
              <div class="sys-m-cell"><div class="num">80–95%</div><div class="lab">24–48h Interstate Revisit</div></div>
              <div class="sys-m-cell"><div class="num">Zero Risk</div><div class="lab">Eliminates Worker Shoulder Hazards</div></div>
            </div>
            <p style="font-size:14px;color:var(--muted)"><b>Automated Audits &amp; Visual LLM Querying:</b> Detects displaced, knocked-down, or missing barrels and signage in active construction zones, comparing setups against approved Maintenance of Traffic (MOT) plans. Allows engineers to query visual streams via natural language prompts (e.g., <i>'Show all knocked-down barrels or missing warning signs'</i>).</p>
            <div class="sys-links">
              <a href="https://doi.org/10.1109/ACCESS.2024.3503368" target="_blank" rel="noopener">Read IEEE Access Publication ↗</a>
              <a href="https://doi.org/10.4236/jtts.2026.161006" target="_blank" rel="noopener">Read Work Zone AI Field Study (JTTs 2026) ↗</a>
              <a href="projects.html#spr-5005">Associated Project: SPR-5005 (Co-PI) →</a>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>
""" + foot()


# =========================================================================
# 4. FUNDED PROJECTS (projects.html)
# =========================================================================
PROJECTS_DATA = [
    # Active Co-PI Grants
    {"id":"INDOT SPR-5021", "title":"Traffic Signal Freight Prioritization via Vehicle to Infrastructure (V2I) Communications",
     "role":"Co-Principal Investigator (Co-PI)", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2026 – 2027", "amount":"$383,966",
     "desc":"Developing connected freight priority algorithms utilizing V2I digital telemetry to harmonize truck progression and minimize corridor emissions and deceleration delay at signalized intersections.", "tag":"copi"},
    {"id":"INDOT SPR-5005", "title":"Evaluation of Asset Identification Technology Utilizing Truck Images",
     "role":"Co-Principal Investigator (Co-PI)", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2025 – 2027", "amount":"$301,966",
     "desc":"Harnessing 1-Hz optical dashcam streams from commercial truck fleets to automate roadway asset inventory, lane line degradation tracking, and temporary traffic control inspection.", "tag":"copi"},
    {"id":"INDOT SPR-5020", "title":"Identifying Locations with Abnormally High Wrong-Way Driving or Interstate U-Turns",
     "role":"Co-Principal Investigator (Co-PI)", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2025 – 2027", "amount":"$224,109",
     "desc":"Scalable trajectory analytics screening high-frequency connected vehicle waypoints to detect and flag high-risk wrong-way driving entries and illegal median U-turns on limited-access facilities.", "tag":"copi"},
    {"id":"INDOT SPR-4928", "title":"Connected Vehicle Trajectory Data to Screen Network for Hard-Braking and Hard-Acceleration Events",
     "role":"Co-Principal Investigator (Co-PI)", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2024 – 2025", "amount":"$218,390",
     "desc":"Statewide geospatial polygon screening identifying proactive crash surrogates, quantifying hard deceleration clusters across freeway segments, interchanges, and signalized intersections.", "tag":"copi"},

    # Multi-State Pooled Fund & Federal Studies
    {"id":"FHWA TPF-5(519)", "title":"Expansion: Enhanced Traffic Signal Performance Measures (Purdue-Pooled Fund)",
     "role":"Research Engineer", "sponsor":"Federal Highway Administration (FHWA) / Multi-State Pooled Fund", "period":"2023 – 2026", "amount":"$1,300,000",
     "desc":"Nationwide multi-agency initiative expanding high-resolution vehicle trajectory performance measures to signalized arterials, corridor progression, and split-failure monitoring.", "tag":"pooled"},
    {"id":"FHWA TPF-5(514)", "title":"Work Zone Analytics (Purdue-Pooled Fund)",
     "role":"Research Engineer", "sponsor":"Federal Highway Administration (FHWA) / Multi-State Pooled Fund", "period":"2023 – 2026", "amount":"$890,000",
     "desc":"Multi-state pooled fund delivering continuous spatiotemporal speed heatmaps, queue shockwave propagation monitoring, and work zone mobility analytics across participating state DOTs. Resulted in the 506-page FHWA Monograph.", "tag":"pooled"},
    {"id":"CCAT Regional UTC", "title":"Methodologies for Monitoring Work Zone Performance Measures Across State Border Highways Using Connected Vehicle Data",
     "role":"Research Engineer", "sponsor":"Center for Connected and Automated Transportation (CCAT)", "period":"2023 – 2025", "amount":"USDOT Tier 1 UTC",
     "desc":"Multi-jurisdictional analytics resolving boundary discontinuity and evaluating cross-border work zone delay spillover between state DOT networks.", "tag":"pooled"},

    # Additional State & Operational Deployments
    {"id":"INDOT SPR-4933", "title":"Worksite Speed Control System (WSCS)",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2024 – 2025", "amount":"State Funded",
     "desc":"Empirical evaluation of automated worksite speed enforcement and digital feedback trailers using connected vehicle speed distributions.", "tag":"state"},
    {"id":"INDOT SPR-4907", "title":"Systemwide Asset Condition Assessment Using Connected Vehicle Data",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2024 – 2025", "amount":"State Funded",
     "desc":"Leveraging vehicle telematics and vertical acceleration to assess pavement roughness and road asset health statewide.", "tag":"state"},
    {"id":"INDOT SPR-4857", "title":"Statewide Screening of Signalized Intersections for Capacity Improvements",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2023 – 2024", "amount":"State Funded",
     "desc":"Network-wide screening methodology converting trajectory data into intersection control delay and split failure indices for capital improvement prioritization.", "tag":"state"},
    {"id":"INDOT SPR-4854", "title":"MOT for MOT: Maintenance of Traffic Case Studies",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2023 – 2025", "amount":"State Funded",
     "desc":"Synthesizing field performance data to establish best practices for temporary traffic control setups and contractor MOT compliance.", "tag":"state"},
    {"id":"INDOT SPR-4851", "title":"Development of Incident Management Performance Measure Database & IN-TIME Training",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2023 – 2025", "amount":"State Funded",
     "desc":"Quantifying clearance times, secondary crash risk, and secondary tow recovery resource delay to train emergency responders.", "tag":"state"},
    {"id":"INDOT SPR-4850", "title":"Continued Deployment of Indiana Work Zone Analytics",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2023 – 2025", "amount":"State Funded",
     "desc":"Operationalizing real-time work zone queue metrics mapping to the FHWA Work Zone Safety and Mobility Rule.", "tag":"state"},
    {"id":"INDOT SPR-4803", "title":"Communication of Fixed & Mobile Warning to Commercial Trucks Using In-Cab Notification",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2023 – 2025", "amount":"State Funded",
     "desc":"Evaluating driver compliance and speed reduction when emergency and queue warning messages are communicated directly into truck cabs.", "tag":"state"},
    {"id":"INDOT SPR-4704", "title":"Evaluating the Robustness of MDSS Forecast and Compliance with Recommendations",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2022 – 2024", "amount":"State Funded",
     "desc":"Winter road weather analytics matching Maintenance Decision Support System forecasts with plow telematics and speed recovery.", "tag":"state"},
    {"id":"INDOT SPR-4639", "title":"Connected Vehicle Centric Dashboards for TMC of the Future",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2021 – 2023", "amount":"State Funded",
     "desc":"Architected cloud-native traffic management center interfaces integrating live probe telemetry into daily tactical operations.", "tag":"state"},
    {"id":"INDOT SPR-4636", "title":"Research Support on I-465 Variable Speed Limit & Ramp Meter Project",
     "role":"Research Engineer", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2021 – 2025", "amount":"State Funded",
     "desc":"Before-and-after safety and flow evaluation of active traffic management (ATM) implementations on the Indianapolis beltway.", "tag":"state"},
    {"id":"INDOT SPR-4603", "title":"Crowdsourcing / Winter Operations Dashboard Upgrade",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2021 – 2023", "amount":"State Funded",
     "desc":"Developed operational winter storm mobility dashboards quantifying road recovery time for DOT leadership and media reporting.", "tag":"state"},
    {"id":"INDOT SPR-4536", "title":"Implementation of Enhanced Probe Data (CANBUS) for Tactical Workzone & Winter Operations",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2020 – 2023", "amount":"State Funded",
     "desc":"Ingested high-frequency CANBUS controller sensor data to calibrate snowplow fleet operations and assess work zone speeds.", "tag":"state"},
    {"id":"INDOT SPR-4600", "title":"Impacts to Traffic Behavior from Queue Warning Truck Pilot Project",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2021 – 2022", "amount":"State Funded",
     "desc":"Pioneered the queue-warning truck evaluation that earned the ITS Midwest Project of the Year Award.", "tag":"state"},
    {"id":"INDOT SPR-4524", "title":"Evaluation of the Impact of On-Vehicle Digital Communication Alerts to Improve Motorist Safety",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2020 – 2022", "amount":"State Funded",
     "desc":"Quantified speed reductions and driver braking reactions to digital navigation alerts broadcast from maintenance vehicles.", "tag":"state"},
    {"id":"INDOT SPR-4451", "title":"Integration of Probe Data Tools into TMC Operations",
     "role":"Graduate Research Assistant", "sponsor":"Indiana Department of Transportation (INDOT)", "period":"2020 – 2022", "amount":"State Funded",
     "desc":"Built operational screening widgets enabling TMC operators to detect real-time freeway anomalies using probe vehicle waypoints.", "tag":"state"}
]

projects_cards_html = "".join([f"""
<div class="pcard" data-tag="{p['tag']}" id="{p['id'].lower().replace(' ','-')}">
  <div class="pcard-top">
    <span class="pcard-id">{p['id']}</span>
    <span class="pcard-role {'role-copi' if p['tag']=='copi' else 'role-re'}">{p['role']}</span>
  </div>
  <h3 class="pcard-title">{p['title']}</h3>
  <div class="pcard-meta">
    <span><b>Period:</b> {p['period']}</span>
    <span><b>Sponsor:</b> {p['sponsor']}</span>
  </div>
  <p class="pcard-desc">{p['desc']}</p>
  <div class="pcard-amt">
    <span class="sponsor">{p['sponsor'].split('(')[0].strip()}</span>
    <span class="val">{p['amount']}</span>
  </div>
</div>
""" for p in PROJECTS_DATA])

P["projects.html"] = head("Funded Projects & Agency Deployments | Rahul Sakhare, Ph.D., P.E.",
 "Externally funded research projects totaling $6M+ across FHWA, INDOT, and CCAT. Co-PI on 4 active grants ($1.13M) and lead research engineer on multi-state pooled funds.",
 "sub") + nav("projects.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["folder"]} Research Portfolio</span>
    <h1>Funded Projects &amp; Agency Deployments.</h1>
    <p>A proven track record of competitive grant leadership and multi-agency project execution. Over 20 externally funded research initiatives totaling more than $6.0M across federal, state, and regional sponsors.</p>
  </section>

  <section class="section wrap" style="border-top:none;padding-top:20px">
    <!-- Portfolio Summary Banner -->
    <div class="proj-stats">
      <div class="proj-stat-box">
        <div class="num">$6.0M+</div>
        <div class="lab">Total External Funding Portfolio</div>
      </div>
      <div class="proj-stat-box">
        <div class="num">$1.13M</div>
        <div class="lab">Active Funding as Co-PI (4 Grants)</div>
      </div>
      <div class="proj-stat-box">
        <div class="num">22</div>
        <div class="lab">Externally Funded Projects</div>
      </div>
      <div class="proj-stat-box">
        <div class="num">FHWA &amp; INDOT</div>
        <div class="lab">Federal &amp; State Agency Sponsors</div>
      </div>
    </div>

    <!-- Filter Buttons -->
    <div class="proj-filters" id="proj-filters">
      <button class="proj-f-btn active" data-filter="all">All Projects (22)</button>
      <button class="proj-f-btn" data-filter="copi">Active Co-PI Grants (4)</button>
      <button class="proj-f-btn" data-filter="pooled">Multi-State Pooled Funds &amp; Federal (3)</button>
      <button class="proj-f-btn" data-filter="state">State DOT Deployments (15)</button>
    </div>

    <!-- Project Grid -->
    <div class="proj-grid" id="proj-grid">
      {projects_cards_html}
    </div>
  </section>
""" + foot()


# =========================================================================
# 5. PUBLICATIONS (publications.html)
# =========================================================================
P["publications.html"] = head("Publications | Rahul Sakhare, Ph.D., P.E.",
 "Peer-reviewed journal articles, technical reports, monographs, and conference presentations by Rahul Sakhare, Ph.D., P.E.",
 "sub") + nav("publications.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["book"]} Scientific Publications</span>
    <h1>Publications.</h1>
    <p>Peer-reviewed journal articles, technical reports for INDOT &amp; FHWA, monographs, and conference presentations spanning connected vehicle telematics, traffic safety, and cloud performance measures. Search by keyword or filter by document type.</p>
  </section>

  <!-- Sticky Search & Filter Toolbar -->
  <div class="wrap pub-toolbar">
    <div class="pub-search-wrap">
      <svg class="pub-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" class="pub-search-input" id="pub-search-input" placeholder="Search publications by title, co-author, keyword, or venue (e.g., 'work zone', 'dashcam', 'IEEE', '2026')..." autocomplete="off">
      <button class="pub-clear-btn" id="pub-clear-btn" title="Clear search">✕</button>
    </div>
    <div class="filters" id="filters"></div>
  </div>

  <div class="wrap">
    <div id="no-matches" class="hidden" style="padding:48px 0;text-align:center;color:var(--muted)">
      <h3>No matching publications found</h3>
      <p>Try refining your search query or switching categories above.</p>
    </div>
    <div id="pub-root"></div>
  </div>
""" + foot("Google Scholar: 521 citations · h-index 13 · i10-index 19",
           '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 6. TEACHING & MENTORING (teaching.html)
# =========================================================================
MENTEES = [
    {"name":"Myles Overall", "deg":"Ph.D. in Civil Engineering", "dept":"Purdue CCE",
     "topic":"Incident management performance measures, emergency clearance delay, and work zone commercial truck video analytics.",
     "proj":"INDOT SPR-4851 & JTTs 2026"},
    {"name":"Chris Gartner", "deg":"M.S. in Civil Engineering", "dept":"Purdue CCE",
     "topic":"Scalable data models for signalized intersection performance measures and statewide network screening.",
     "proj":"INDOT SPR-4857 & IEEE Access 2025"},
    {"name":"Andrew Thompson", "deg":"M.S. in Electrical & Computer Engineering", "dept":"Purdue ECE",
     "topic":"Road asset identification and condition assessment utilizing commercial truck computer vision.",
     "proj":"INDOT SPR-4907 & SPR-5005"},
    {"name":"Justin Mukai", "deg":"M.S. in Civil Engineering", "dept":"Purdue CCE",
     "topic":"Quantifying vehicle hard-braking events occurring prior to secondary crashes on interstate corridors.",
     "proj":"JTTs 2026 & INDOT SPR-4928"},
    {"name":"Thomas Driscoll", "deg":"M.S. in Mechanical Engineering", "dept":"Purdue ME",
     "topic":"Cross-border connected vehicle congestion modeling and multi-jurisdictional delay spillover.",
     "proj":"CCAT & JTTs 2025"},
    {"name":"Neelesh Gopalkrishnan", "deg":"M.S. in Computer Science", "dept":"Purdue CS",
     "topic":"Connected vehicle market penetration dashboard and scalable WebGIS trajectory query interfaces.",
     "proj":"JTRP WebGIS Analytics"},
    {"name":"Ahsmitha Sivakumar", "deg":"B.Tech. in Civil Engineering", "dept":"Purdue CCE",
     "topic":"Toll plaza performance measures and evaluation of privacy filters in probe trajectory datasets.",
     "proj":"Smart Cities 2024"},
    {"name":"Anirud Nandakumar", "deg":"B.Tech. in Civil Engineering", "dept":"Purdue CCE",
     "topic":"Normalized hard-braking evaluations at signalized intersections, roundabouts, and all-way stops.",
     "proj":"Future Transportation 2024"}
]

mentees_html = "".join([f"""
<div class="mentee-card">
  <div class="mentee-top">
    <span class="mentee-name">{m['name']}</span>
    <span class="mentee-deg">{m['deg']}</span>
  </div>
  <p class="mentee-topic">{m['topic']}</p>
  <span class="mentee-proj"><b>Project / Output:</b> {m['proj']}</span>
</div>
""" for m in MENTEES])

P["teaching.html"] = head("Teaching & Mentorship | Rahul Sakhare, Ph.D., P.E.",
 "Teaching philosophy, courses prepared to teach, and student research mentorship across Civil Engineering, ECE, CS, and Mechanical Engineering.",
 "sub") + nav("teaching.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["board"]} Teaching &amp; Mentorship</span>
    <h1>In the Classroom &amp; the Lab.</h1>
    <p>Educating the next generation of transportation systems engineers through hands-on telematics, real-world highway data, and cross-disciplinary research mentorship.</p>
  </section>

  <section class="section wrap" style="border-top:none;padding-top:20px">
    <!-- Pedagogical Philosophy Callout -->
    <div class="pedagogy-callout">
      <h3>Instructional Philosophy: Real-World Telematics in the Engineering Classroom</h3>
      <p>"The central task of engineering pedagogy is manufacturing the realization that computational analysis has immediate, tangible value in resolving real infrastructure challenges. Coursework comes alive the moment a student realizes that their analysis answers a question a real agency is trying to resolve. I build instructional modules around actual connected vehicle trajectory records from Indiana's interstate network, commercial freight dashcam streams, and highway speed heatmaps — training students to navigate the noise and ambiguities of physical infrastructure and determine what the answers actually mean for the engineers who act on them."</p>
    </div>

    <!-- Core Subject Areas -->
    <span class="eyebrow">Subject Areas</span>
    <h2>Courses &amp; Instructional Expertise.</h2>
    <div class="course-grid">
      <div class="course-card">
        <span class="c-code">Undergraduate Core</span>
        <h3>Transportation Engineering</h3>
        <p>Traffic flow fundamentals, roadway geometric design, signalized intersection capacity, highway operations, and emerging intelligent transportation systems.</p>
        <div class="c-tags">
          <span class="c-tag">CE 36100</span>
          <span class="c-tag">HCM / MUTCD</span>
          <span class="c-tag">Traffic Physics</span>
        </div>
      </div>
      <div class="course-card">
        <span class="c-code">Graduate Core</span>
        <h3>Big Data Analytics in Transportation Systems</h3>
        <p>Cloud-native spatial-temporal analytics, distributed SQL (BigQuery), connected vehicle trajectory processing, probe data validation, and performance measure engineering.</p>
        <div class="c-tags">
          <span class="c-tag">Distributed Cloud</span>
          <span class="c-tag">BigQuery</span>
          <span class="c-tag">Spatial Telematics</span>
        </div>
      </div>
      <div class="course-card">
        <span class="c-code">Graduate Elective</span>
        <h3>Traffic Flow Theory &amp; Operations</h3>
        <p>Macroscopic traffic flow theory, kinematic shockwave dynamics (LWR model), queue propagation, surrogate safety analysis, and automated speed control.</p>
        <div class="c-tags">
          <span class="c-tag">Shockwave Theory</span>
          <span class="c-tag">Surrogate Safety</span>
          <span class="c-tag">Queue Control</span>
        </div>
      </div>
    </div>

    <!-- Student Mentorship Wall -->
    <span class="eyebrow">Student Mentorship Roster</span>
    <h2>Graduate &amp; Undergraduate Researchers Co-Advised.</h2>
    <p class="intro">Proud to have mentored and co-advised talented researchers across multiple engineering disciplines — Civil, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering.</p>

    <div class="mentee-grid">
      {mentees_html}
    </div>
  </section>

  <!-- Global Teaching & Outreach -->
  <section class="section wrap">
    <span class="eyebrow">Global Workshops &amp; Guest Lectures</span>
    <h2>Academic Instruction &amp; Guest Seminars.</h2>
    <ul class="teach-list">
      <li>
        <div class="yr">2026</div>
        <div>
          <b>Guest Lecture: Connected Vehicle Data &amp; Applications</b>
          <p>CE36100 Transportation Engineering, Purdue University (April 29, 2026). Delivered guest lecture on high-frequency connected vehicle trajectory applications and statewide safety screening to undergraduate civil engineering students.</p>
        </div>
      </li>
      <li>
        <div class="yr">2024</div>
        <div>
          <b>Invited Seminar: Traffic Stream Shock Wave Identification</b>
          <p>Transportation Division, Department of Civil Engineering, IIT Madras (August 21, 2024). Lectured on methodologies for identifying shockwave type and speed in traffic streams using connected vehicle data.</p>
        </div>
      </li>
      <li>
        <div class="yr">2021</div>
        <div>
          <b>Course Instructor: SPARC International Mobility Workshop</b>
          <p>Government of India SPARC (Scheme for Promotion of Academic and Research Collaboration) initiative. Developed curriculum and instructed three session modules on connected vehicle telematics and traffic performance measures.</p>
        </div>
      </li>
      <li>
        <div class="yr">2017–2018</div>
        <div>
          <b>Teaching Assistant: CE2080 Civil Engineering Surveying</b>
          <p>Department of Civil Engineering, IIT Madras. Led laboratory sessions and field surveying tutorials under Dr. Atul Narayan.</p>
        </div>
      </li>
    </ul>
  </section>
""" + foot()


# =========================================================================
# 7. EDUCATION (education.html)
# =========================================================================
P["education.html"] = head("Education | Rahul Sakhare, Ph.D., P.E.",
 "Education — Ph.D. Purdue University; Dual Degree M.Tech. & B.Tech. IIT Madras.",
 "sub") + nav("education.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["cap"]} Academic Degrees</span>
    <h1>Education.</h1>
    <p>Doctoral training in civil infrastructure systems and connected vehicle data at Purdue, built upon a dual-degree transportation engineering foundation from IIT Madras.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div class="edu-stack">
      <a class="edu-card reveal" href="https://engineering.purdue.edu/CCE" target="_blank" rel="noopener">
        <span class="edu-visit">Visit School Website ↗</span>
        <span class="edu-when">April 2023 · West Lafayette, Indiana</span>
        <p class="edu-deg">Doctor of Philosophy (Ph.D.)</p>
        <h2 class="edu-uni">Purdue University</h2>
        <p class="edu-dept">Lyles School of Civil &amp; Construction Engineering — Transportation &amp; Infrastructure Systems</p>
        <p><b>Dissertation:</b> "Integrating Connected Vehicle Data for Operational Decision Making."<br>
        <b>Advisor:</b> Prof. Darcy M. Bullock; <b>Committee:</b> Profs. Samuel Labi, Konstantina Gkritza, and James Krogmeier.<br>
        Supported by the Christopher B. &amp; Susan S. Burke Graduate Research Assistantship.</p>
      </a>
      <a class="edu-card reveal" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">
        <span class="edu-visit">Visit Institute Website ↗</span>
        <span class="edu-when">May 2018 · Chennai, India</span>
        <p class="edu-deg">Master of Technology (M.Tech.)</p>
        <h2 class="edu-uni">Indian Institute of Technology Madras</h2>
        <p class="edu-dept">Department of Civil Engineering — Transportation Engineering</p>
        <p>Completed as part of the five-year dual-degree program. <b>Thesis:</b> "Reliable Corridor Level Travel Time Estimation Using Probe Vehicle Data." <b>Advisor:</b> Prof. Lelitha Devi Vanajakshi. Recognized with the <i>Exemplary &amp; All-Round Best Performance Award</i> in the dual-degree program.</p>
      </a>
      <a class="edu-card reveal" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">
        <span class="edu-visit">Visit Institute Website ↗</span>
        <span class="edu-when">May 2018 · Chennai, India</span>
        <p class="edu-deg">Bachelor of Technology (B.Tech.)</p>
        <h2 class="edu-uni">Indian Institute of Technology Madras</h2>
        <p class="edu-dept">Department of Civil Engineering — Minor in Management Studies</p>
        <p>Entered through the prestigious IIT Joint Entrance Examination (IIT-JEE) ranked in the top 0.2 percentile among 1.45 million candidates nationwide.</p>
      </a>
    </div>
  </section>
""" + foot()


# =========================================================================
# 8. AWARDS (awards.html)
# =========================================================================
P["awards.html"] = head("Awards & Honors | Rahul Sakhare, Ph.D., P.E.",
 "Honors and awards — Google Cloud Research Innovator, ITS Midwest Project of the Year, ITE International Championship, and more.",
 "sub") + nav("awards.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["trophy"]} Recognition</span>
    <h1>Honors &amp; Awards.</h1>
    <p>Selected accolades across research, public agency deployments, academic scholarship, and international competitions.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div class="aw-high">
      <a class="awh" href="https://cloud.google.com/blog/topics/public-sector/google-cloud-research-innovators-launch-fourth-cohort-to-drive-innovation/" target="_blank" rel="noopener">
        {I["trophy"]}
        <h3>Google Cloud Research Innovator</h3>
        <div class="by">Google Cloud · Fourth Global Cohort</div>
        <div class="yrp">2024 ↗</div>
      </a>
      <div class="awh">
        {I["trophy"]}
        <h3>Project of the Year Award</h3>
        <div class="by">ITS Midwest · Queue-Truck Navigation Alerts</div>
        <div class="yrp">2021</div>
      </div>
      <div class="awh">
        {I["trophy"]}
        <h3>Editor's Choice Award</h3>
        <div class="by">Safety (Journal) · Work Zone Monitoring</div>
        <div class="yrp">2022</div>
      </div>
      <div class="awh">
        {I["trophy"]}
        <h3>International Collegiate Championship</h3>
        <div class="by">ITE International · Traffic Bowl Winner</div>
        <div class="yrp">2020</div>
      </div>
      <div class="awh">
        {I["trophy"]}
        <h3>Edward J. Cox Memorial Scholarship</h3>
        <div class="by">Indiana ITE Section</div>
        <div class="yrp">2023</div>
      </div>
      <div class="awh">
        {I["trophy"]}
        <h3>IGS Best Paper Award &amp; Diamond Jubilee</h3>
        <div class="by">Indian Geotechnical Society</div>
        <div class="yrp">2016</div>
      </div>
    </div>

    <h2>Full Honors Timeline.</h2>
    <ul class="aw-line">
      <li><span class="yr">2026</span><div class="what"><b>PRIME Grant Award</b><span>Purdue University in support of professional development.</span></div></li>
      <li><span class="yr">2024</span><div class="what"><b><a href="https://cloud.google.com/blog/topics/public-sector/google-cloud-research-innovators-launch-fourth-cohort-to-drive-innovation/" target="_blank" rel="noopener">Google Cloud Research Innovator ↗</a></b><span>Selected to the fourth global cohort of researchers driving scientific breakthroughs with Google Cloud.</span></div></li>
      <li><span class="yr">2023</span><div class="what"><b>Edward J. Cox Memorial Scholarship</b><span>Indiana ITE Section.</span></div></li>
      <li><span class="yr">2022–23</span><div class="what"><b>Best Student Speaker Award</b><span>Purdue ITE.</span></div></li>
      <li><span class="yr">2022</span><div class="what"><b>Editor's Choice Award</b><span>"Methodology for Monitoring Work Zones Traffic Operations Using Connected Vehicle Data," Safety 8(2).</span></div></li>
      <li><span class="yr">2021</span><div class="what"><b>ITS Midwest Project of the Year</b><span>Evaluation of queue trucks with navigation alerts using connected vehicle data.</span></div></li>
      <li><span class="yr">2021 &amp; 2022</span><div class="what"><b>Elevator Pitch Event Winner</b><span>Purdue ITE.</span></div></li>
      <li><span class="yr">2021</span><div class="what"><b>Student Team Design Competition Winner</b><span>Great Lakes District ITE.</span></div></li>
      <li><span class="yr">2020</span><div class="what"><b>International Collegiate Traffic Bowl Championship</b><span>ITE International.</span></div></li>
      <li><span class="yr">2020</span><div class="what"><b>Best Poster Presentation</b><span>Sigma Xi Scientific Society, Purdue University.</span></div></li>
      <li><span class="yr">2020–2023</span><div class="what"><b>Christopher B. &amp; Susan S. Burke Fellowship</b><span>Purdue University graduate program research assistantship.</span></div></li>
      <li><span class="yr">2018</span><div class="what"><b>Exemplary &amp; All-round Best Performance, Dual-Degree Program</b><span>Civil Engineering, IIT Madras.</span></div></li>
      <li><span class="yr">2018</span><div class="what"><b>Winner, CEA Technical Events</b><span>Case Study, Prabandha, Bon Auto, and Aquanomics — IIT Madras.</span></div></li>
      <li><span class="yr">2017</span><div class="what"><b>Invited Visiting Undergraduate Student</b><span>Purdue University.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>Gold Medal in Civil Engineering</b><span>National Design and Research Forum, Institution of Engineers, India.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>Mr. H. C. Verma Diamond Jubilee Award &amp; IGS Best Paper</b><span>Indian Geotechnical Society.</span></div></li>
      <li><span class="yr">2016</span><div class="what"><b>PURE Program Scholar</b><span>Among the top three civil-engineering students chosen across India for the Purdue Undergraduate Research Experience.</span></div></li>
      <li><span class="yr">2013</span><div class="what"><b>IIT Joint Entrance Examination (IIT-JEE) — Top 0.2 Percentile</b><span>Ranked 2,445 among 1.45 million students nationwide.</span></div></li>
    </ul>
  </section>
""" + foot()


# =========================================================================
# 9. NEWS & MEDIA (news.html)
# =========================================================================
P["news.html"] = head("News & Media | Rahul Sakhare, Ph.D., P.E.",
 "Media coverage from The New York Times, FHWA Innovator, Google Cloud customer story, and national press.",
 "sub") + nav("news.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["news"]} In The Press</span>
    <h1>News &amp; Media Coverage.</h1>
    <p>National and international media coverage highlighting our connected vehicle research, work zone safety innovations, and cloud data analytics.</p>
  </section>
  <div class="wrap"><div class="filters" id="media-filters"></div></div>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu", '<script src="media-data.js"></script>\n')


# =========================================================================
# 10. CONTACT (contact.html)
# =========================================================================
P["contact.html"] = head("Contact | Rahul Sakhare, Ph.D., P.E.",
 "Contact Rahul Sakhare — Office location, scholarly profiles, and collaboration opportunities.",
 "sub") + nav("contact.html") + f"""
  <section class="contact wrap">
    <span class="eyebrow">{I["mail"]} Connect &amp; Collaborate</span>
    <h2>Let's Connect.</h2>
    <p>I welcome research collaborations, agency partnerships with state DOTs and municipal agencies, conversations with commercial fleet operators, and inquiries from prospective graduate researchers.</p>

    <div class="links">
      <a href="mailto:rsakhare@purdue.edu">{I["mail"]} rsakhare@purdue.edu</a>
      <a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">{I["scholar"]} Google Scholar</a>
      <a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">{I["linkedin"]} LinkedIn</a>
      <a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">{I["orcid"]} ORCID</a>
      <a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">{I["rg"]} ResearchGate</a>
    </div>

    <div style="margin-top:40px" class="about-card">
      <h3>Office Coordinates</h3>
      <div class="row"><b>Location</b><span>Hall of Discovery &amp; Learning Research, Room 204F</span></div>
      <div class="row"><b>Address</b><span>207 S. Martin Jischke Drive, West Lafayette, IN 47906</span></div>
      <div class="row"><b>Affiliation</b><span>Joint Transportation Research Program (JTRP), Purdue University</span></div>
    </div>

    <div class="fb-pane">
      <h3>Send a Note</h3>
      <p class="sub">Collaboration ideas, data inquiries, or comments on our research tools — messages deliver directly to my Purdue inbox.</p>
      <form class="fb-form" action="https://formsubmit.co/rsakhare@purdue.edu" method="POST">
        <input type="hidden" name="_subject" value="Website Inquiry — Rahul Sakhare Portal">
        <input type="text" name="_honey" style="display:none">
        <div class="fb-row">
          <input type="text" name="name" placeholder="Your Name (optional)" autocomplete="name">
          <input type="email" name="email" placeholder="Your Email" required autocomplete="email">
        </div>
        <textarea name="message" placeholder="Your message or collaboration topic..." required></textarea>
        <button class="btn btn-primary" type="submit">Send Message →</button>
      </form>
      <p class="fb-note">Direct inquiries: <a href="mailto:rsakhare@purdue.edu">rsakhare@purdue.edu</a></p>
    </div>
  </section>
""" + foot()

# =========================================================================
# WRITE ALL PAGES
# =========================================================================
for name, html in P.items():
    with open(name, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {name}")

print(f"\nSuccessfully built {len(P)} site pages with unified layout.")
