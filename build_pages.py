#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer (v7 - Clean Modern Academic Architecture)."""

import os

FONTS = "https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap"

I = {  # inline SVGs (stroke, currentColor)
 "user":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 19.5c1.8-3.2 4.3-4.7 7.5-4.7s5.7 1.5 7.5 4.7"/></svg>',
 "book":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H12v15H6.5A2.5 2.5 0 0 0 4 20.5zM20 5.5A2.5 2.5 0 0 0 17.5 3H12v15h5.5a2.5 2.5 0 0 1 2.5 2.5z"/></svg>',
 "cap":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 4 2 9l10 5 10-5-10-5z"/><path d="M6 11.5V16c0 1.6 2.7 3 6 3s6-1.4 6-3v-4.5"/><path d="M22 9v5"/></svg>',
 "trophy":'<svg class="ico" viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5a3 3 0 0 0 3 4.5M16 5h3a3 3 0 0 1-3 4.5"/><path d="M12 13v3.5M8.5 20h7M10 16.5h4v3.5h-4z"/></svg>',
 "board":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v2M8.5 21l3.5-3 3.5 3M7 8h6M7 11h9"/></svg>',
 "news":'<svg class="ico" viewBox="0 0 24 24"><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
 "mail":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7.5l9 6 9-6"/></svg>',
 "scholar":'<svg class="ico" viewBox="0 0 24 24"><path d="M12 3 2 8.5l10 5.5 10-5.5z"/><path d="M7 11.5v5c0 1.5 2.2 2.8 5 2.8s5-1.3 5-2.8v-5"/></svg>',
 "linkedin":'<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M8 10.5V17M8 7.6v.1M12 17v-4a2.4 2.4 0 0 1 4.8 0v4"/></svg>',
 "orcid":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 8.5v7M9 6.7v.1M12.5 15.5v-7h2a3.5 3.5 0 0 1 0 7z"/></svg>',
 "rg":'<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 16V8h3a2.3 2.3 0 0 1 .9 4.4L15 16"/></svg>',
}

NAV_ITEMS = [
 ("index.html", "Home"),
 ("publications.html", "Publications"),
 ("education.html", "Education"),
 ("teaching.html", "Teaching"),
 ("awards.html", "Awards"),
 ("news.html", "News"),
 ("contact.html", "Contact")
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
  <span>© 2026 Rahul Suryakant Sakhare, Ph.D., P.E. · Purdue University</span>
  <span>{right}</span>
</footer>
{scripts}<script src="script.js"></script>
</body>
</html>"""

P = {}

# =========================================================================
# 1. HOME (index.html)
# =========================================================================
P["index.html"] = head("Rahul Sakhare, Ph.D., P.E. | Transportation Research Engineer",
 "Rahul Sakhare, Ph.D., P.E. — Transportation Research Engineer at Purdue University. Connected vehicle trajectory data, traffic operations, work zone safety, and cloud analytics.",
 "home") + nav("index.html") + f"""
  <section class="hero wrap">
    <div class="hero-inner">
      <div>
        <p class="loc">TRANSPORTATION RESEARCH ENGINEER · <b>PURDUE UNIVERSITY</b> · LICENSED P.E. (INDIANA)</p>
        <h1>Rahul Sakhare<span class="creds">, Ph.D., P.E.</span></h1>
        <p class="tagline">Civil Infrastructure Systems &amp; <span>Connected Vehicle Data</span></p>
        <p class="lede">
          I am a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP) and a licensed Professional Engineer (P.E.) in Indiana. My research focuses on turning high-frequency connected vehicle trajectory streams, commercial truck telematics, and roadway sensing data into operational performance measures that enhance highway mobility, work zone safety, and infrastructure reliability.
        </p>
        <div class="cta-row">
          <a class="btn btn-primary" href="publications.html">View Publications (92) →</a>
          <a class="btn btn-secondary" href="education.html">Academic Education</a>
          <a class="btn btn-ghost" href="teaching.html">Teaching &amp; Mentoring</a>
          <a class="btn btn-ghost" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">Download CV ↗</a>
        </div>
      </div>

      <!-- Right Column: Profile Portrait & Quick Coordinates -->
      <div class="hero-card">
        <div class="hero-photo-wrap">
          <img src="assets/img/hero_photo.jpg" alt="Rahul Sakhare, Ph.D., P.E." width="1000" height="666">
        </div>
        <div class="hero-meta-list">
          <div class="hero-meta-row">
            <b>Affiliation</b>
            <span>JTRP, Purdue University</span>
          </div>
          <div class="hero-meta-row">
            <b>Licensure</b>
            <span>Professional Engineer (P.E.), IN</span>
          </div>
          <div class="hero-meta-row">
            <b>Education</b>
            <span>Ph.D. Purdue ('23) · IIT Madras ('18)</span>
          </div>
          <div class="hero-meta-row">
            <b>TRB Committee</b>
            <span>ACF13 (Limited Access Roadways)</span>
          </div>
          <div class="hero-meta-row">
            <b>Contact</b>
            <span><a href="mailto:rsakhare@purdue.edu">rsakhare@purdue.edu</a></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Live Metrics Readout Strip -->
    <div class="readout" role="group" aria-label="Research metrics">
      <div class="cell"><div class="numline"><div class="num" id="stat-cites" data-to="521">521</div></div><div class="lab">Citations</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-h" data-to="13">13</div></div><div class="lab">h-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-i10" data-to="19">19</div></div><div class="lab">i10-index</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-journal" data-to="32">32</div></div><div class="lab">Journal articles</div></div>
      <div class="cell"><div class="numline"><div class="num" id="stat-report" data-to="22">22</div></div><div class="lab">Technical reports</div></div>
      <div class="cell"><div class="numline"><span class="pre">&gt;</span><div class="num" id="dl-num" data-to="35566">35,566</div></div><div class="lab">Downloads &amp; views</div><div class="asof" id="dl-asof">as of Jul 8, 2026</div></div>
      <div class="cell"><div class="numline"><span class="pre">$</span><div class="num" data-to="6">6.0</div><span class="pre">M+</span></div><div class="lab">Research Funding Portfolio</div></div>
    </div>

    <!-- Two-Column Balanced Overview (Wide-Screen Responsive) -->
    <div class="home-split">
      <!-- Left: Research Focus & Academic Background -->
      <div>
        <h2 class="home-section-title">Research Overview &amp; Practice</h2>
        <p class="home-bio-p">
          My engineering research investigates how large-scale, heterogeneous vehicle sensor data can solve pressing operational challenges in transportation systems. By combining traffic flow theory, surrogate safety physics, and scalable cloud computing pipelines, my work translates billions of trajectory waypoints into actionable measures used daily by state DOTs and transportation agencies.
        </p>
        <p class="home-bio-p">
          Over more than 20 funded research projects totaling over $6.0M, I have served as Co-Principal Investigator (Co-PI) on four active Indiana Department of Transportation (INDOT) research grants ($1.13M) and as lead research engineer on multi-state FHWA Pooled-Fund studies. These methodologies support statewide bottleneck screening, winter storm recovery, automated work zone queue warning, and capital project prioritization.
        </p>

        <div class="interest-chips">
          <span class="interest-chip">Connected Vehicle Trajectory Data</span>
          <span class="interest-chip">Traffic Flow Dynamics &amp; Shockwaves</span>
          <span class="interest-chip">Work Zone Safety &amp; Speed Control</span>
          <span class="interest-chip">Surrogate Safety &amp; Hard-Braking</span>
          <span class="interest-chip">Incident Management &amp; Tow Clearance</span>
          <span class="interest-chip">Cloud Analytics (Google BigQuery)</span>
          <span class="interest-chip">Road Weather Mobility</span>
          <span class="interest-chip">Commercial Fleet Dashcam Vision</span>
        </div>

        <a class="btn btn-secondary" href="about.html">Read Full Biography &amp; Appointments →</a>
      </div>

      <!-- Right: Recent Publications & Media Highlights -->
      <div>
        <h2 class="home-section-title">Recent Highlights</h2>
        <div class="highlight-stack">
          <div class="hl-card">
            <div class="hl-tagline"><span>Transportation (Springer Nature)</span><span class="hl-date">2026</span></div>
            <h3 class="hl-title">Deriving Systemwide Granular Segment Level Traffic Mobility Performance Metrics</h3>
            <p class="hl-desc">Translating billions of connected vehicle waypoints into granular 0.1-mile segment performance metrics across statewide highway networks.</p>
          </div>
          <div class="hl-card">
            <div class="hl-tagline"><span>Future Transportation</span><span class="hl-date">2026</span></div>
            <h3 class="hl-title">Work Zone Performance Measures Derived from Connected Vehicle Data</h3>
            <p class="hl-desc">Framework mapping connected vehicle trajectory metrics directly to the FHWA Rule on Work Zone Safety and Mobility.</p>
          </div>
          <div class="hl-card">
            <div class="hl-tagline"><span>IEEE Open Journal of ITS</span><span class="hl-date">2026</span></div>
            <h3 class="hl-title">Evaluating Safety Benefits of Ramp Metering</h3>
            <p class="hl-desc">Empirical trajectory analysis of variable speed limits and ramp metering on the I-465 beltway.</p>
          </div>
          <div class="hl-card">
            <div class="hl-tagline"><span>The New York Times</span><span class="hl-date">Dec 2024</span></div>
            <h3 class="hl-title">Front-Page Media Feature</h3>
            <p class="hl-desc">Research on connected vehicle traffic data and road congestion dynamics featured on the front page of The New York Times.</p>
          </div>
        </div>

        <a class="btn btn-ghost" href="publications.html" style="width:100%;justify-content:center;margin-top:16px">Browse All 92 Publications &amp; Reports →</a>
      </div>
    </div>

    <!-- Quick Navigation Directory Grid -->
    <div class="nav-grid">
      <a class="nav-card" href="publications.html">
        <div class="nav-card-head">{I["book"]}<span>Publications</span></div>
        <p>32 peer-reviewed journal articles, 22 technical reports, and 1 monograph. Searchable with instant BibTeX copy.</p>
        <span class="go">Browse publications →</span>
      </a>
      <a class="nav-card" href="education.html">
        <div class="nav-card-head">{I["cap"]}<span>Education</span></div>
        <p>Ph.D. from Purdue University, dual M.Tech. &amp; B.Tech. from IIT Madras, and licensed Professional Engineer (P.E.).</p>
        <span class="go">View degrees →</span>
      </a>
      <a class="nav-card" href="teaching.html">
        <div class="nav-card-head">{I["board"]}<span>Teaching &amp; Mentoring</span></div>
        <p>Instructional philosophy, course subject areas, and mentorship roster of 8 graduate and undergraduate researchers.</p>
        <span class="go">Explore teaching →</span>
      </a>
      <a class="nav-card" href="awards.html">
        <div class="nav-card-head">{I["trophy"]}<span>Awards &amp; Honors</span></div>
        <p>Google Cloud Research Innovator, ITS Midwest Project of the Year, Safety Editor's Choice, and ITE Champion.</p>
        <span class="go">View honors →</span>
      </a>
      <a class="nav-card" href="news.html">
        <div class="nav-card-head">{I["news"]}<span>News &amp; Media</span></div>
        <p>Media coverage across The New York Times, FHWA Innovator, Google Cloud customer stories, and broadcast outlets.</p>
        <span class="go">Read coverage →</span>
      </a>
      <a class="nav-card" href="contact.html">
        <div class="nav-card-head">{I["mail"]}<span>Contact</span></div>
        <p>Purdue office location, scholarly profiles, collaboration inquiries, and direct messaging portal.</p>
        <span class="go">Get in touch →</span>
      </a>
    </div>
  </section>
""" + foot("West Lafayette, IN", '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 2. ABOUT (about.html)
# =========================================================================
P["about.html"] = head("About | Rahul Sakhare, Ph.D., P.E.",
 "Biographical background and academic appointments of Rahul Sakhare, Ph.D., P.E., Transportation Research Engineer at Purdue University.",
 "sub") + nav("about.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["user"]} Biography</span>
    <h1>About Rahul Sakhare, Ph.D., P.E.</h1>
    <p>Transportation Research Engineer at Purdue University's Joint Transportation Research Program, bridging civil infrastructure systems, connected vehicle telematics, and scalable data analytics.</p>
  </section>

  <section class="section wrap" style="padding-top:0">
    <div class="home-split">
      <div>
        <p class="home-bio-p">I am a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP). My work is rooted in civil and transportation engineering principles, integrated with scalable cloud data architectures and sensing systems. I specialize in turning massive, heterogeneous telemetry streams — including connected vehicle trajectory waypoints, commercial truck telematics, and roadway camera feeds — into actionable performance measures that transportation agencies can deploy and sustain.</p>
        <p class="home-bio-p">Over more than 20 externally funded research projects totaling over $6.0M, I have served as Co-Principal Investigator (Co-PI) on four active Indiana Department of Transportation (INDOT) research grants ($1.13M) and as lead research engineer on multi-state FHWA Pooled-Fund studies. The methodologies and diagnostic tools resulting from this work are embedded into statewide operations with INDOT and regional DOT partners across the Midwest, informing real-time work zone safety alerts, network-wide bottleneck screening, winter storm recovery, and capital program prioritization.</p>
        <p class="home-bio-p">Alongside research, I actively teach, mentor graduate and undergraduate researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering, serve on the TRB Committee on Limited Access Roadway Operations (ACF13), and contribute to the annual Purdue Road School Planning Committee. I earned my Ph.D. in Civil Engineering from Purdue University, completed dual B.Tech. and M.Tech. degrees from IIT Madras (ranked top 0.2% in the IIT-JEE), and hold a licensed Professional Engineer (P.E.) credential in Indiana.</p>

        <h3 style="margin-top:28px">Core Research Focus Areas</h3>
        <div class="interest-chips">
          <span class="interest-chip">Connected Vehicle Trajectory Data</span>
          <span class="interest-chip">Work Zone Safety &amp; Speed Compliance</span>
          <span class="interest-chip">Traffic Flow Dynamics &amp; Kinematic Waves</span>
          <span class="interest-chip">Surrogate Safety &amp; Deceleration Physics</span>
          <span class="interest-chip">Traffic Incident Management Performance</span>
          <span class="interest-chip">Scalable Cloud Telematics (Google BigQuery)</span>
          <span class="interest-chip">Road Weather Operations &amp; Mobility Profiling</span>
          <span class="interest-chip">Highway Asset Condition Assessment</span>
        </div>
      </div>

      <aside class="hero-card" style="height:fit-content">
        <h3 style="margin:0 0 14px">Professional Summary</h3>
        <div class="hero-meta-list">
          <div class="hero-meta-row"><b>Current Position</b><span>Transportation Research Engineer</span></div>
          <div class="hero-meta-row"><b>Institution</b><span>JTRP, Purdue University</span></div>
          <div class="hero-meta-row"><b>Licensure</b><span>Licensed Professional Engineer (P.E.), IN</span></div>
          <div class="hero-meta-row"><b>Doctorate</b><span>Ph.D. Civil Eng, Purdue ('23)</span></div>
          <div class="hero-meta-row"><b>Graduate Degree</b><span>M.Tech. Civil Eng, IIT Madras ('18)</span></div>
          <div class="hero-meta-row"><b>Undergraduate</b><span>B.Tech. Civil Eng, IIT Madras ('18)</span></div>
          <div class="hero-meta-row"><b>Grant Leadership</b><span>Co-PI on 4 Active Grants ($1.13M)</span></div>
          <div class="hero-meta-row"><b>Funded Portfolio</b><span>$6.0M+ Total Project Volume</span></div>
          <div class="hero-meta-row"><b>TRB Committee</b><span>ACF13 (Limited Access Roadways)</span></div>
          <div class="hero-meta-row"><b>Conference Role</b><span>Purdue Road School Committee</span></div>
        </div>
      </aside>
    </div>

    <!-- Career Timeline -->
    <h2 style="margin-top:56px">Career &amp; Professional Appointments</h2>
    <ul class="teach-list">
      <li>
        <div class="yr">2023 — Present</div>
        <div>
          <b>Transportation Research Engineer</b>
          <p>Joint Transportation Research Program (JTRP), Purdue University. Leading multi-agency connected vehicle data research, cloud analytics pipelines, and agency deployments for INDOT and FHWA. Co-PI on four active research grants.</p>
        </div>
      </li>
      <li>
        <div class="yr">2018 — 2023</div>
        <div>
          <b>Graduate Research Assistant</b>
          <p>Lyles School of Civil Engineering, Purdue University. Conducted doctoral research under Prof. Darcy M. Bullock on connected vehicle data for operational decision-making. Recipient of the Christopher B. &amp; Susan S. Burke Fellowship.</p>
        </div>
      </li>
      <li>
        <div class="yr">2017</div>
        <div>
          <b>Visiting Undergraduate Research Scholar</b>
          <p>Purdue University. Selected through the prestigious Purdue Undergraduate Research Experience (PURE) program among top civil engineering candidates in India.</p>
        </div>
      </li>
      <li>
        <div class="yr">2013 — 2018</div>
        <div>
          <b>Dual Degree Scholar (B.Tech. &amp; M.Tech.)</b>
          <p>Department of Civil Engineering, Indian Institute of Technology (IIT) Madras. Awarded the Exemplary &amp; All-Round Best Performance Award in the dual-degree program.</p>
        </div>
      </li>
    </ul>
  </section>
""" + foot()


# =========================================================================
# 3. PUBLICATIONS (publications.html)
# =========================================================================
P["publications.html"] = head("Publications | Rahul Sakhare, Ph.D., P.E.",
 "Peer-reviewed journal articles, technical reports, monographs, and conference presentations by Rahul Sakhare, Ph.D., P.E.",
 "sub") + nav("publications.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["book"]} Scholarly Works</span>
    <h1>Publications &amp; Reports.</h1>
    <p>Peer-reviewed journal articles, technical research reports for INDOT &amp; FHWA, authoritative monographs, and conference presentations spanning connected vehicle data, traffic safety, and cloud computing. Use the search bar or category filters below.</p>
  </section>

  <!-- Sticky Search & Filter Toolbar -->
  <div class="wrap pub-toolbar">
    <div class="pub-search-wrap">
      <svg class="pub-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" class="pub-search-input" id="pub-search-input" placeholder="Search publications by title, co-author, venue, or year (e.g., 'work zone', 'IEEE', '2026')..." autocomplete="off">
      <button class="pub-clear-btn" id="pub-clear-btn" title="Clear search">✕</button>
    </div>
    <div class="filters" id="filters"></div>
  </div>

  <div class="wrap">
    <div id="no-matches" class="hidden" style="padding:48px 0;text-align:center;color:var(--ink-muted)">
      <h3>No matching publications found</h3>
      <p>Try refining your search query or switching categories above.</p>
    </div>
    <div id="pub-root"></div>
  </div>
""" + foot("Google Scholar: 521 citations · h-index 13 · i10-index 19",
           '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 4. EDUCATION (education.html)
# =========================================================================
P["education.html"] = head("Education | Rahul Sakhare, Ph.D., P.E.",
 "Academic degrees from Purdue University and IIT Madras, and professional engineering licensure.",
 "sub") + nav("education.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["cap"]} Academic Credentials</span>
    <h1>Education &amp; Licensure.</h1>
    <p>Doctoral training in civil infrastructure systems and connected vehicle data at Purdue University, built upon a rigorous dual-degree foundation in transportation engineering from the Indian Institute of Technology (IIT) Madras.</p>
  </section>

  <section class="section wrap" style="padding-top:0">
    <div class="edu-stack">
      <!-- Ph.D. -->
      <div class="edu-card">
        <div class="edu-left">
          <span class="edu-when">April 2023</span>
          <span class="edu-loc">West Lafayette, Indiana</span>
          <a class="edu-visit" href="https://engineering.purdue.edu/CCE" target="_blank" rel="noopener">Lyles School of Civil Eng ↗</a>
        </div>
        <div class="edu-right">
          <h2 class="edu-deg">Doctor of Philosophy (Ph.D.) in Civil Engineering</h2>
          <div class="edu-uni">Purdue University</div>
          <div class="edu-dept">Lyles School of Civil Engineering — Transportation &amp; Infrastructure Systems</div>
          <p><b>Dissertation:</b> "Integrating Connected Vehicle Data for Operational Decision Making."</p>
          <p><b>Advisor:</b> Prof. Darcy M. Bullock</p>
          <p><b>Committee:</b> Prof. Samuel Labi, Prof. Konstantina Gkritza, Prof. James Krogmeier</p>
          <p style="color:var(--ink-muted);font-size:14px">Supported by the Christopher B. &amp; Susan S. Burke Graduate Research Assistantship.</p>
        </div>
      </div>

      <!-- M.Tech. -->
      <div class="edu-card">
        <div class="edu-left">
          <span class="edu-when">May 2018</span>
          <span class="edu-loc">Chennai, India</span>
          <a class="edu-visit" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">IIT Madras Website ↗</a>
        </div>
        <div class="edu-right">
          <h2 class="edu-deg">Master of Technology (M.Tech.) in Transportation Engineering</h2>
          <div class="edu-uni">Indian Institute of Technology (IIT) Madras</div>
          <div class="edu-dept">Department of Civil Engineering — Five-Year Dual Degree Program</div>
          <p><b>Thesis:</b> "Reliable Corridor Level Travel Time Estimation Using Probe Vehicle Data."</p>
          <p><b>Advisor:</b> Prof. Lelitha Devi Vanajakshi</p>
          <p><b>Committee:</b> Prof. Gitakrishnan Ramadurai, Prof. Atul Narayan, Prof. A. Veeraragavan</p>
          <p style="color:var(--accent);font-weight:600;font-size:14px">Recognized with the Exemplary &amp; All-Round Best Performance Award in the dual-degree program.</p>
        </div>
      </div>

      <!-- B.Tech. -->
      <div class="edu-card">
        <div class="edu-left">
          <span class="edu-when">May 2018</span>
          <span class="edu-loc">Chennai, India</span>
          <a class="edu-visit" href="https://www.iitm.ac.in/" target="_blank" rel="noopener">IIT Madras Website ↗</a>
        </div>
        <div class="edu-right">
          <h2 class="edu-deg">Bachelor of Technology (B.Tech.) in Civil Engineering</h2>
          <div class="edu-uni">Indian Institute of Technology (IIT) Madras</div>
          <div class="edu-dept">Department of Civil Engineering — Minor in Management Studies</div>
          <p>Admitted through the prestigious IIT Joint Entrance Examination (IIT-JEE) ranked in the top 0.2 percentile among 1.45 million applicants nationwide (All India Rank 2,445).</p>
        </div>
      </div>

      <!-- Professional Licensure -->
      <div class="edu-card">
        <div class="edu-left">
          <span class="edu-when">Active Credential</span>
          <span class="edu-loc">State of Indiana</span>
          <span style="font-size:12.5px;color:var(--accent);font-weight:700">Licensure Board</span>
        </div>
        <div class="edu-right">
          <h2 class="edu-deg">Professional Engineer (P.E.)</h2>
          <div class="edu-uni">State of Indiana — State Board of Registration for Professional Engineers</div>
          <div class="edu-dept">Discipline: Civil &amp; Transportation Engineering</div>
          <p>Licensed professional engineer authorized to practice civil and transportation engineering in the State of Indiana, upholding public safety, technical standards, and ethical engineering conduct.</p>
        </div>
      </div>
    </div>
  </section>
""" + foot()


# =========================================================================
# 5. TEACHING & MENTORSHIP (teaching.html)
# =========================================================================
MENTEES = [
    {"name":"Myles Overall", "deg":"Ph.D. in Civil Engineering", "dept":"Purdue Civil Eng",
     "topic":"Incident management performance measures, emergency clearance delay, and work zone commercial truck video analytics.",
     "proj":"INDOT SPR-4851 & JTTs 2026"},
    {"name":"Chris Gartner", "deg":"M.S. in Civil Engineering", "dept":"Purdue Civil Eng",
     "topic":"Scalable data models for signalized intersection performance measures and statewide network screening.",
     "proj":"INDOT SPR-4857 & IEEE Access 2025"},
    {"name":"Andrew Thompson", "deg":"M.S. in Electrical & Computer Engineering", "dept":"Purdue ECE",
     "topic":"Road asset identification and condition assessment utilizing commercial truck computer vision.",
     "proj":"INDOT SPR-4907 & SPR-5005"},
    {"name":"Justin Mukai", "deg":"M.S. in Civil Engineering", "dept":"Purdue Civil Eng",
     "topic":"Quantifying vehicle hard-braking events occurring prior to secondary crashes on interstate corridors.",
     "proj":"JTTs 2026 & INDOT SPR-4928"},
    {"name":"Thomas Driscoll", "deg":"M.S. in Mechanical Engineering", "dept":"Purdue ME",
     "topic":"Cross-border connected vehicle congestion modeling and multi-jurisdictional delay spillover.",
     "proj":"CCAT & JTTs 2025"},
    {"name":"Neelesh Gopalkrishnan", "deg":"M.S. in Computer Science", "dept":"Purdue CS",
     "topic":"Connected vehicle market penetration dashboard and scalable WebGIS trajectory query interfaces.",
     "proj":"JTRP WebGIS Analytics"},
    {"name":"Ahsmitha Sivakumar", "deg":"B.Tech. in Civil Engineering", "dept":"Purdue Civil Eng",
     "topic":"Toll plaza performance measures and evaluation of privacy filters in probe trajectory datasets.",
     "proj":"Smart Cities 2024"},
    {"name":"Anirud Nandakumar", "deg":"B.Tech. in Civil Engineering", "dept":"Purdue Civil Eng",
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
  <span class="mentee-proj"><b>Collaborative Output:</b> {m['proj']}</span>
</div>
""" for m in MENTEES])

P["teaching.html"] = head("Teaching & Mentorship | Rahul Sakhare, Ph.D., P.E.",
 "Teaching philosophy, courses prepared to teach, and student research mentorship across Civil Engineering, ECE, CS, and ME.",
 "sub") + nav("teaching.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["board"]} Education &amp; Mentorship</span>
    <h1>In the Classroom &amp; Lab.</h1>
    <p>Educating the next generation of transportation engineers through hands-on telemetry, real-world highway data, and cross-disciplinary research mentorship.</p>
  </section>

  <section class="section wrap" style="padding-top:0">
    <!-- Pedagogical Philosophy Callout -->
    <div class="pedagogy-callout">
      <h3>Instructional Philosophy: Real-World Telematics in Engineering Pedagogy</h3>
      <p>"The core purpose of engineering pedagogy is manufacturing the realization that computational analysis has immediate, tangible value in resolving real infrastructure challenges. Coursework comes alive the moment a student realizes that their analysis answers a question a real agency is trying to solve. I construct learning modules around actual connected vehicle trajectory records from Indiana's interstate network, commercial truck telematics, and highway speed profiles — training students to navigate the noise and ambiguities of physical infrastructure and translate data into sound engineering decisions."</p>
    </div>

    <!-- Core Subject Areas -->
    <span class="eyebrow">Instructional Competencies</span>
    <h2 style="margin-bottom:20px">Courses &amp; Subject Areas.</h2>
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

    <!-- Student Mentorship Roster -->
    <span class="eyebrow">Mentorship Wall</span>
    <h2 style="margin-bottom:8px">Graduate &amp; Undergraduate Researchers Co-Advised.</h2>
    <p style="color:var(--ink-muted);margin:0 0 24px;font-size:16px">Proud to have co-advised and mentored emerging researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering.</p>

    <div class="mentee-grid">
      {mentees_html}
    </div>

    <!-- Invited Lectures -->
    <h2 style="margin-top:40px">Invited Lectures &amp; Workshops</h2>
    <ul class="teach-list">
      <li>
        <div class="yr">2026</div>
        <div>
          <b>Guest Lecture: Connected Vehicle Data &amp; Applications</b>
          <p>CE36100 Transportation Engineering, Purdue University (April 2026). Delivered lecture on high-frequency connected vehicle trajectory applications and statewide safety screening to undergraduate civil engineering students.</p>
        </div>
      </li>
      <li>
        <div class="yr">2024</div>
        <div>
          <b>Invited Seminar: Traffic Stream Shock Wave Identification</b>
          <p>Transportation Division, Department of Civil Engineering, IIT Madras (August 2024). Lectured on methodologies for identifying shockwave type and propagation speed in traffic streams using connected vehicle data.</p>
        </div>
      </li>
      <li>
        <div class="yr">2021</div>
        <div>
          <b>Course Instructor: SPARC International Mobility Workshop</b>
          <p>Government of India SPARC initiative. Developed curriculum and instructed three session modules on connected vehicle telematics and traffic performance measures.</p>
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
# 6. AWARDS (awards.html)
# =========================================================================
P["awards.html"] = head("Awards & Honors | Rahul Sakhare, Ph.D., P.E.",
 "Honors and awards — Google Cloud Research Innovator, ITS Midwest Project of the Year, ITE International Championship, and more.",
 "sub") + nav("awards.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["trophy"]} Recognition</span>
    <h1>Honors &amp; Awards.</h1>
    <p>Selected accolades across research, public agency deployments, academic scholarship, and international competitions.</p>
  </section>

  <section class="section wrap" style="padding-top:0">
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

    <h2>Full Honors &amp; Awards Timeline</h2>
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
# 7. NEWS & MEDIA (news.html)
# =========================================================================
P["news.html"] = head("News & Media | Rahul Sakhare, Ph.D., P.E.",
 "Media coverage from The New York Times, FHWA Innovator, Google Cloud customer stories, and national press.",
 "sub") + nav("news.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["news"]} In The Press</span>
    <h1>News &amp; Media Coverage.</h1>
    <p>National and international media coverage highlighting our connected vehicle research, work zone safety innovations, and cloud data analytics.</p>
  </section>
  <div class="wrap"><div class="filters" id="media-filters"></div></div>
  <section class="section wrap" style="padding-top:16px">
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu", '<script src="media-data.js"></script>\n')


# =========================================================================
# 8. CONTACT (contact.html)
# =========================================================================
P["contact.html"] = head("Contact | Rahul Sakhare, Ph.D., P.E.",
 "Contact Rahul Sakhare — Office location, scholarly profiles, and collaboration opportunities.",
 "sub") + nav("contact.html") + f"""
  <section class="page-hero wrap">
    <span class="eyebrow">{I["mail"]} Connect</span>
    <h1>Contact &amp; Coordinates.</h1>
    <p>I welcome research collaborations, discussions with state DOT and municipal partners, conversations with commercial fleet operators, and inquiries from prospective students.</p>
  </section>

  <section class="section wrap" style="padding-top:0">
    <div class="contact-split">
      <!-- Left: Office Coordinates & Scholarly Links -->
      <div class="contact-info-card">
        <h3>Office Coordinates</h3>
        <p>
          <b>Joint Transportation Research Program (JTRP)</b><br>
          Lyles School of Civil &amp; Construction Engineering<br>
          Purdue University<br><br>
          Hall of Discovery and Learning Research (DLR), Room 204F<br>
          207 S. Martin Jischke Drive<br>
          West Lafayette, IN 47906
        </p>

        <h3 style="margin-top:28px">Scholarly Profiles</h3>
        <div class="contact-links">
          <a href="mailto:rsakhare@purdue.edu">{I["mail"]} rsakhare@purdue.edu</a>
          <a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">{I["scholar"]} Google Scholar Profile</a>
          <a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">{I["linkedin"]} LinkedIn Profile</a>
          <a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">{I["orcid"]} ORCID (0000-0001-7843-5707)</a>
          <a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">{I["rg"]} ResearchGate Profile</a>
        </div>
      </div>

      <!-- Right: Message Form -->
      <div class="fb-pane">
        <h3>Send a Message</h3>
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
      </div>
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
