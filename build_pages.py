#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer (Refined Modern Scholar Architecture).

Typography: Lora (Editorial Serif Headings) + Inter (Scholarly Sans Body)
Aesthetic: Authentic Academic Minimalist (No SaaS cards, no bubble chips, authentic scholarly layout)
"""

import os

FONTS = "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap"

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
 "doc":'<svg class="ico" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
}

NAV_ITEMS = [
 ("index.html", "Home"),
 ("about.html", "About"),
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
<link rel="stylesheet" href="styles.css?v=9.0">
<script>
(function(){{
  var t = localStorage.getItem('theme');
  if (!t) {{
    t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }}
  document.documentElement.setAttribute('data-theme', t);
}})();
</script>
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
    <a class="brand" href="index.html">Rahul Sakhare<span class="creds">, Ph.D., P.E.</span></a>
    <div class="nav-right">
      <ul class="nav-links">{links}<li><a class="cv" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">CV (PDF) ↗</a></li></ul>
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark theme" title="Toggle dark theme" type="button">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
      </button>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false" type="button">☰</button>
    </div>
  </nav>
</header>
<main>"""

def foot(right="West Lafayette, IN", scripts=""):
    return f"""</main>
<footer class="wrap site-foot">
  <span>© 2026 Rahul Suryakant Sakhare, Ph.D., P.E. · Purdue University</span>
  <span>{right}</span>
</footer>
{scripts}<script src="script.js?v=9.0"></script>
</body>
</html>"""

P = {}

# =========================================================================
# 1. HOME (index.html) — Authentic Academic Profile Layout
# =========================================================================
P["index.html"] = head(
    "Rahul Sakhare, Ph.D., P.E. | Purdue University",
    "Rahul Sakhare, Ph.D., P.E. — Transportation Research Engineer at Purdue University. Connected vehicle trajectory data, traffic operations, work zone safety, and cloud analytics.",
    "home"
) + nav("index.html") + f"""
  <section class="wrap profile-section">
    <div class="profile-grid">
      <!-- Left Column: Portrait & Academic Coordinates -->
      <aside class="profile-sidebar">
        <div class="profile-photo-frame">
          <img src="assets/img/sakhare_headshot.jpg" alt="Rahul Sakhare, Ph.D., P.E." width="1080" height="720">
        </div>
        <div class="profile-sidebar-meta">
          <p><b>Affiliation:</b><br>Joint Transportation Research Program (JTRP), Purdue University</p>
          <p><b>Office:</b><br>Hall of Discovery and Learning Research (DLR), Room 204F<br>West Lafayette, IN 47906</p>
          <p><b>Email:</b><br><a href="mailto:rsakhare@purdue.edu">rsakhare@purdue.edu</a></p>
          <p><b>Credentials:</b><br>Ph.D. Civil Eng, Purdue ('23)<br>Dual M.Tech. &amp; B.Tech., IIT Madras ('18)</p>
          <p><b>Licensure:</b><br>Professional Engineer (P.E.), Indiana (No. PE12600619)</p>
          <p><b>TRB Committee:</b><br>Member of the Committee, ACF13 (Limited Access Roadway Operations)</p>
        </div>
      </aside>

      <!-- Right Column: Name, Title, Quick Links, Narrative Bio, and Highlights -->
      <div class="profile-main">
        <h1>Rahul Sakhare, Ph.D., P.E.</h1>
        <div class="profile-title">Transportation Research Engineer <span>· Purdue University</span></div>

        <!-- Academic Coordinates & Quick Profile Links -->
        <div class="profile-links">
          <a href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">{I["doc"]} Curriculum Vitae (PDF)</a>
          <a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">{I["scholar"]} Google Scholar</a>
          <a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">{I["orcid"]} ORCID</a>
          <a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">{I["linkedin"]} LinkedIn</a>
          <a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">{I["rg"]} ResearchGate</a>
          <a href="mailto:rsakhare@purdue.edu">{I["mail"]} Contact</a>
        </div>

        <!-- Scholarly Biography Narrative -->
        <div class="profile-bio">
          <p>
            I am a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP) and a licensed Professional Engineer (P.E.) in Indiana. My engineering research investigates how large-scale, heterogeneous vehicle sensor data can resolve pressing operational challenges across civil infrastructure systems.
          </p>
          <p>
            By synthesizing traffic flow theory, kinematic wave dynamics, surrogate safety physics, and scalable cloud computing pipelines, my work translates billions of high-frequency connected vehicle waypoints and commercial truck telematics into actionable measures used daily by transportation agencies. Across multiple state and national research initiatives, I have served as Co-Principal Investigator (Co-PI) on four active Indiana Department of Transportation (INDOT) research grants and as lead research engineer on multi-state FHWA Pooled-Fund studies. Methodologies developed through this research are embedded in statewide operations for work zone safety screening, winter storm mobility recovery, secondary crash prevention, and capital investment prioritization.
          </p>
        </div>

        <!-- Understated Scholarly Metrics Summary Bar -->
        <div class="metrics-summary-bar">
          <span><b>Google Scholar:</b> <span id="stat-cites" data-to="543">540+</span> citations</span>
          <span class="dot">·</span>
          <span><b>h-index:</b> <span id="stat-h" data-to="14">14</span></span>
          <span class="dot">·</span>
          <span><b>i10-index:</b> <span id="stat-i10" data-to="19">19</span></span>
          <span class="dot">·</span>
          <span><b><span id="stat-journal" data-to="32">32</span></b> journal articles</span>
          <span class="dot">·</span>
          <span><b><span id="stat-report" data-to="22">22</span></b> technical reports</span>
        </div>

        <!-- Selected Publications Preview -->
        <h2>Selected Publications</h2>
        <div class="pub-list">
          <div class="pub has-link" data-url="https://doi.org/10.1007/s11116-026-10702-6" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2026</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Li, H., &amp; Bullock, D. M. (2026). "Deriving Systemwide Granular Segment Level Traffic Mobility Performance Metrics Using Connected Vehicle Waypoint Data." <i>Transportation</i> (Springer Nature).</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.1007/s11116-026-10702-6" target="_blank" rel="noopener">doi.org/10.1007/s11116-026-10702-6 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bsakhare2026transportation%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Li%2C%20Howell%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BDeriving%20Systemwide%20Granular%20Segment%20Level%20Traffic%20Mobility%20Performance%20Metrics%20Using%20Connected%20Vehicle%20Waypoint%20Data%7D%2C%0A%20%20journal%20%3D%20%7BTransportation%7D%2C%0A%20%20year%20%3D%20%7B2026%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.1007%2Fs11116-026-10702-6%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.3390/futuretransp6010001" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2026</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Mukai, J., Desai, J., &amp; Bullock, D. M. (2026). "Work Zone Performance Measures Derived from Connected Vehicle Data." <i>Future Transportation</i>, 6(1), 1-18.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.3390/futuretransp6010001" target="_blank" rel="noopener">doi.org/10.3390/futuretransp6010001 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bsakhare2026futuretransp%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Mukai%2C%20Justin%20and%20Desai%2C%20Jash%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BWork%20Zone%20Performance%20Measures%20Derived%20from%20Connected%20Vehicle%20Data%7D%2C%0A%20%20journal%20%3D%20%7BFuture%20Transportation%7D%2C%0A%20%20year%20%3D%20%7B2026%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.3390%2Ffuturetransp6010001%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.1109/OJITS.2026.3533261" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2026</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Li, H., &amp; Bullock, D. M. (2026). "Evaluating Safety Benefits of Ramp Metering." <i>IEEE Open Journal of Intelligent Transportation Systems</i>.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.1109/OJITS.2026.3533261" target="_blank" rel="noopener">doi.org/10.1109/OJITS.2026.3533261 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bsakhare2026ojits%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Li%2C%20Howell%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BEvaluating%20Safety%20Benefits%20of%20Ramp%20Metering%7D%2C%0A%20%20journal%20%3D%20%7BIEEE%20Open%20Journal%20of%20Intelligent%20Transportation%20Systems%7D%2C%0A%20%20year%20%3D%20%7B2026%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.1109%2FOJITS.2026.3533261%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.5703/1288284317804" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2025</div>
            <div>
              <p class="cite">Bullock, D. M., <b>Sakhare, R. S.</b>, et al. (2025). <i>Big Data for Work Zone Performance Measures: Monograph on Techniques, Implementation, and Case Studies</i>. Federal Highway Administration (FHWA), 506 pages.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.5703/1288284317804" target="_blank" rel="noopener">doi.org/10.5703/1288284317804 ↗</a>
                <button class="btn-bib" data-bib="%40book%7Bbullock2025monograph%2C%0A%20%20author%20%3D%20%7BBullock%2C%20Darcy%20M.%20and%20Sakhare%2C%20Rahul%20S.%20and%20others%7D%2C%0A%20%20title%20%3D%20%7BBig%20Data%20for%20Work%20Zone%20Performance%20Measures%3A%20Monograph%20on%20Techniques%2C%20Implementation%2C%20and%20Case%20Studies%7D%2C%0A%20%20publisher%20%3D%20%7BFederal%20Highway%20Administration%7D%2C%0A%20%20year%20%3D%20%7B2025%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.5703%2F1288284317804%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>
        </div>

        <p style="margin-top:20px">
          <a href="publications.html" style="font-weight:600">View all 92 publications, technical reports, and monographs →</a>
        </p>
      </div>
    </div>
  </section>
""" + foot("West Lafayette, IN", '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 2. ABOUT (about.html)
# =========================================================================
P["about.html"] = head(
    "About | Rahul Sakhare, Ph.D., P.E.",
    "Biographical background, academic appointments, and research trajectory of Rahul Sakhare, Ph.D., P.E., Purdue University.",
    "sub"
) + nav("about.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>About Rahul Sakhare, Ph.D., P.E.</h1>
    <p style="font-size:17px;color:var(--ink-muted);margin-bottom:32px">
      Transportation Research Engineer at Purdue University's Joint Transportation Research Program, bridging civil infrastructure systems, connected vehicle telematics, and scalable data analytics.
    </p>

    <div class="profile-grid">
      <aside class="profile-sidebar">
        <div class="profile-photo-frame">
          <img src="assets/img/sakhare_headshot.jpg" alt="Rahul Sakhare, Ph.D., P.E." width="1080" height="720">
        </div>
        <div class="profile-sidebar-meta">
          <p><b>Current Role:</b><br>Transportation Research Engineer<br>JTRP, Purdue University</p>
          <p><b>Licensure:</b><br>Licensed Professional Engineer (P.E.), State of Indiana (No. PE12600619, June 2026)</p>
          <p><b>Research Leadership:</b><br>Co-PI on 4 Active INDOT Grants<br>Lead Engineer on FHWA Pooled-Fund Studies</p>
          <p><b>Professional Service:</b><br>Member of the TRB Committee ACF13 (Limited Access Roadway Operations)<br>Purdue Road School Committee</p>
        </div>
      </aside>

      <div class="profile-bio">
        <h2>Biographical Overview</h2>
        <p>
          I am a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP). My work is rooted in foundational civil and transportation engineering principles, integrated with modern scalable cloud data architectures and connected vehicle sensing streams. I specialize in turning massive, heterogeneous telemetry — including passenger car trajectory waypoints, commercial truck telematics, and roadway camera feeds — into actionable performance measures that transportation agencies can deploy and sustain.
        </p>
        <p>
          Across multiple state and national research initiatives, I have served as Co-Principal Investigator (Co-PI) on four active Indiana Department of Transportation (INDOT) research grants and as lead research engineer on multi-state FHWA Pooled-Fund studies. The methodologies and diagnostic tools resulting from this work are embedded into statewide operations with INDOT and regional DOT partners across the Midwest, informing real-time work zone safety alerts, network-wide bottleneck screening, winter storm recovery, and capital program prioritization.
        </p>
        <p>
          Alongside research, I actively teach, mentor graduate and undergraduate researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering, serve as a member of the TRB Standing Committee on Limited Access Roadway Operations (ACF13), and contribute to the annual Purdue Road School Planning Committee. I earned my Ph.D. in Civil Engineering from Purdue University, completed dual B.Tech. and M.Tech. degrees from IIT Madras (ranked top 0.2% in the IIT-JEE), and hold a licensed Professional Engineer (P.E.) credential in Indiana.
        </p>

        <h2>Career Appointments</h2>
        <ul class="award-list">
          <li class="award-item">
            <span class="award-yr">2023 — Present</span>
            <div class="award-desc">
              <b>Transportation Research Engineer</b>
              <span>Joint Transportation Research Program (JTRP), Purdue University. Leading multi-agency connected vehicle data research, cloud analytics pipelines, and agency deployments for INDOT and FHWA. Co-PI on four active INDOT research grants.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2018 — 2023</span>
            <div class="award-desc">
              <b>Graduate Research Assistant</b>
              <span>Lyles School of Civil Engineering, Purdue University. Conducted doctoral research under Prof. Darcy M. Bullock on connected vehicle data for operational decision-making. Recipient of the Christopher B. &amp; Susan S. Burke Fellowship.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2017</span>
            <div class="award-desc">
              <b>Visiting Undergraduate Research Scholar</b>
              <span>Purdue University. Selected through the Purdue Undergraduate Research Experience (PURE) program among top civil engineering candidates in India.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2013 — 2018</span>
            <div class="award-desc">
              <b>Dual Degree Scholar (B.Tech. &amp; M.Tech.)</b>
              <span>Department of Civil Engineering, Indian Institute of Technology (IIT) Madras. Awarded the Exemplary &amp; All-Round Best Performance Award in the dual-degree program.</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
""" + foot()


# =========================================================================
# 3. PUBLICATIONS (publications.html)
# =========================================================================
P["publications.html"] = head(
    "Publications | Rahul Sakhare, Ph.D., P.E.",
    "Peer-reviewed journal articles, technical reports, monographs, and conference presentations by Rahul Sakhare, Ph.D., P.E.",
    "sub"
) + nav("publications.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Publications &amp; Reports</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:24px">
      32 peer-reviewed journal articles, 22 technical research reports for INDOT &amp; FHWA, 1 monograph, and conference proceedings spanning connected vehicle data, traffic safety, and cloud computing. Search by keyword or filter by scholarly category.
    </p>

    <!-- Search & Filter Toolbar -->
    <div class="pub-toolbar">
      <div class="pub-search-wrap">
        <svg class="pub-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" class="pub-search-input" id="pub-search-input" placeholder="Search by title, co-author, venue, or year (e.g., 'work zone', 'IEEE', '2026')..." autocomplete="off">
        <button class="pub-clear-btn" id="pub-clear-btn" title="Clear search">✕</button>
      </div>
      <div class="filters" id="filters"></div>
    </div>

    <!-- Publications List Root -->
    <div id="no-matches" class="hidden" style="padding:48px 0;text-align:center;color:var(--ink-muted)">
      <h3>No matching publications found</h3>
      <p>Try refining your search query or switching categories above.</p>
    </div>
    <div id="pub-root"></div>
  </section>
""" + foot("Google Scholar: 540+ citations · h-index 14 · i10-index 19", '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 4. EDUCATION (education.html)
# =========================================================================
P["education.html"] = head(
    "Education & Licensure | Rahul Sakhare, Ph.D., P.E.",
    "Academic degrees from Purdue University and IIT Madras, and professional engineering licensure.",
    "sub"
) + nav("education.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Education &amp; Licensure</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:32px">
      Doctoral training in civil infrastructure systems and connected vehicle data at Purdue University, built upon a dual-degree foundation in transportation engineering from the Indian Institute of Technology (IIT) Madras.
    </p>

    <div class="edu-entry">
      <div class="edu-meta">
        <span class="yr">April 2023</span>
        <span>West Lafayette, Indiana</span>
        <div style="margin-top:6px"><a href="https://engineering.purdue.edu/CE" target="_blank" rel="noopener">Lyles School of Civil Eng ↗</a></div>
      </div>
      <div class="edu-detail">
        <h3>Doctor of Philosophy (Ph.D.) in Civil Engineering</h3>
        <div class="inst">Purdue University — Lyles School of Civil Engineering</div>
        <p><b>Dissertation:</b> "Integrating Connected Vehicle Data for Operational Decision Making."</p>
        <p><b>Advisor:</b> Prof. Darcy M. Bullock</p>
        <p><b>Committee:</b> Prof. Samuel Labi, Prof. Konstantina Gkritza, Prof. James Krogmeier</p>
        <p style="color:var(--ink-muted);font-size:14px">Supported by the Christopher B. &amp; Susan S. Burke Graduate Research Assistantship.</p>
      </div>
    </div>

    <div class="edu-entry">
      <div class="edu-meta">
        <span class="yr">May 2018</span>
        <span>Chennai, India</span>
        <div style="margin-top:6px"><a href="https://www.iitm.ac.in/" target="_blank" rel="noopener">IIT Madras ↗</a></div>
      </div>
      <div class="edu-detail">
        <h3>Master of Technology (M.Tech.) in Transportation Engineering</h3>
        <div class="inst">Indian Institute of Technology (IIT) Madras — Department of Civil Engineering</div>
        <p><b>Thesis:</b> "Reliable Corridor Level Travel Time Estimation Using Probe Vehicle Data."</p>
        <p><b>Advisor:</b> Prof. Lelitha Devi Vanajakshi</p>
        <p><b>Committee:</b> Prof. Gitakrishnan Ramadurai, Prof. Atul Narayan, Prof. A. Veeraragavan</p>
        <p style="color:var(--accent-gold);font-weight:600;font-size:14px">Recognized with the Exemplary &amp; All-Round Best Performance Award in the dual-degree program.</p>
      </div>
    </div>

    <div class="edu-entry">
      <div class="edu-meta">
        <span class="yr">May 2018</span>
        <span>Chennai, India</span>
        <div style="margin-top:6px"><a href="https://www.iitm.ac.in/" target="_blank" rel="noopener">IIT Madras ↗</a></div>
      </div>
      <div class="edu-detail">
        <h3>Bachelor of Technology (B.Tech.) in Civil Engineering</h3>
        <div class="inst">Indian Institute of Technology (IIT) Madras — Minor in Management Studies</div>
        <p>Admitted through the IIT Joint Entrance Examination (IIT-JEE) ranked in the top 0.2 percentile among 1.45 million applicants nationwide (All India Rank 2,445).</p>
      </div>
    </div>

    <div class="edu-entry">
      <div class="edu-meta">
        <span class="yr">June 2026</span>
        <span>State of Indiana</span>
        <div style="margin-top:6px"><a href="https://mylicense.in.gov/EVerification/" target="_blank" rel="noopener">IN PLA Verification ↗</a></div>
      </div>
      <div class="edu-detail">
        <h3>Professional Engineer (P.E.)</h3>
        <div class="inst">State of Indiana — State Board of Registration for Professional Engineers</div>
        <p><b>License Number:</b> PE12600619 (Active · Issued June 2026)</p>
        <p>Discipline: Civil &amp; Transportation Engineering. Licensed professional engineer upholding public safety, technical rigor, and ethical engineering standards.</p>
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
     "proj":"Future Transportation 2026 & INDOT SPR-4928"},
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

mentees_rows = "".join([f"""
<tr>
  <td><b>{m['name']}</b><br><span style="font-size:13px;color:var(--ink-muted)">{m['dept']}</span></td>
  <td>{m['deg']}</td>
  <td>{m['topic']}</td>
  <td><span style="font-size:13px;color:var(--accent-gold);font-weight:600">{m['proj']}</span></td>
</tr>
""" for m in MENTEES])

P["teaching.html"] = head(
    "Teaching & Mentorship | Rahul Sakhare, Ph.D., P.E.",
    "Instructional philosophy, courses prepared to teach, and student research mentorship across Civil Engineering, ECE, CS, and ME.",
    "sub"
) + nav("teaching.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Teaching &amp; Mentorship</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:24px">
      Educating emerging engineers through hands-on telemetry, real-world infrastructure data, and cross-disciplinary research mentorship.
    </p>

    <!-- Pedagogical Philosophy Quote -->
    <div class="teaching-quote">
      "The core purpose of engineering pedagogy is manufacturing the realization that computational analysis has immediate, tangible value in resolving real infrastructure challenges. Coursework comes alive the moment a student realizes that their analysis answers a question a real agency is trying to solve. I construct learning modules around actual connected vehicle trajectory records from Indiana's interstate network, commercial truck telematics, and highway speed profiles — training students to navigate the noise and ambiguities of physical infrastructure and translate data into sound engineering decisions."
    </div>

    <!-- Core Subject Areas -->
    <h2>Courses &amp; Subject Areas</h2>
    <div class="teach-grid">
      <div class="teach-item">
        <span class="level">Undergraduate Core</span>
        <h3>Transportation Engineering</h3>
        <p>Traffic flow fundamentals, roadway geometric design, signalized intersection capacity, highway operations, and emerging intelligent transportation systems (CE 36100).</p>
      </div>
      <div class="teach-item">
        <span class="level">Graduate Core</span>
        <h3>Big Data Analytics in Transportation Systems</h3>
        <p>Cloud-native spatial-temporal analytics, distributed SQL (BigQuery), connected vehicle trajectory processing, probe data validation, and performance measure engineering.</p>
      </div>
      <div class="teach-item">
        <span class="level">Graduate Elective</span>
        <h3>Traffic Flow Theory &amp; Operations</h3>
        <p>Macroscopic traffic flow theory, kinematic shockwave dynamics (LWR model), queue propagation, surrogate safety analysis, and automated speed control.</p>
      </div>
    </div>

    <!-- Student Mentorship Roster -->
    <h2>Graduate &amp; Undergraduate Researchers Co-Advised</h2>
    <p style="font-size:15px;color:var(--ink-muted);margin-bottom:16px">
      Proud to have co-advised and mentored emerging researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering:
    </p>

    <div style="overflow-x:auto">
      <table class="mentee-table">
        <thead>
          <tr>
            <th>Student</th>
            <th>Program</th>
            <th>Research Area</th>
            <th>Collaborative Output</th>
          </tr>
        </thead>
        <tbody>
          {mentees_rows}
        </tbody>
      </table>
    </div>

    <!-- Invited Lectures -->
    <h2>Invited Lectures &amp; Workshops</h2>
    <ul class="award-list">
      <li class="award-item">
        <span class="award-yr">2026</span>
        <div class="award-desc">
          <b>Guest Lecture: Connected Vehicle Data &amp; Operational Applications</b>
          <span>CE 36100 Transportation Engineering, Purdue University (April 2026). Delivered lecture on high-frequency trajectory applications, work zone safety screening, and statewide performance measures.</span>
        </div>
      </li>
      <li class="award-item">
        <span class="award-yr">2024</span>
        <div class="award-desc">
          <b>Invited Seminar: Traffic Stream Shock Wave Identification</b>
          <span>Transportation Division, Department of Civil Engineering, IIT Madras (August 2024). Lectured on methodologies for identifying shockwave type and propagation speed in traffic streams using connected vehicle data.</span>
        </div>
      </li>
      <li class="award-item">
        <span class="award-yr">2021</span>
        <div class="award-desc">
          <b>Course Instructor: SPARC International Mobility Workshop</b>
          <span>Government of India SPARC initiative. Developed curriculum and instructed three session modules on connected vehicle telematics and traffic performance measures.</span>
        </div>
      </li>
      <li class="award-item">
        <span class="award-yr">2017–2018</span>
        <div class="award-desc">
          <b>Teaching Assistant: CE2080 Civil Engineering Surveying</b>
          <span>Department of Civil Engineering, IIT Madras. Led laboratory sessions and field surveying tutorials under Dr. Atul Narayan.</span>
        </div>
      </li>
    </ul>
  </section>
""" + foot()


# =========================================================================
# 6. AWARDS (awards.html)
# =========================================================================
P["awards.html"] = head(
    "Honors & Awards | Rahul Sakhare, Ph.D., P.E.",
    "Academic, professional, and research accolades of Rahul Sakhare, Ph.D., P.E.",
    "sub"
) + nav("awards.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Honors &amp; Awards</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:28px">
      Selected accolades across engineering research, public agency deployments, academic scholarship, and international technical competitions.
    </p>

    <ul class="award-list">
      <li>
        <a class="award-item has-link" href="https://www.purdue.edu/gradschool/postdoctorates/prime-grant.php" target="_blank" rel="noopener" title="Open Purdue PRIME Grant announcement">
          <span class="award-yr">2026</span>
          <div class="award-desc">
            <b>PRIME Grant Award <span class="ext-hint">↗</span></b>
            <span>Purdue University in support of professional development and academic scholarship.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://cloud.google.com/blog/topics/public-sector/google-cloud-research-innovators-launch-fourth-cohort-to-drive-innovation/" target="_blank" rel="noopener" title="Open Google Cloud Research Innovators announcement">
          <span class="award-yr">2024</span>
          <div class="award-desc">
            <b>Google Cloud Research Innovator <span class="ext-hint">↗</span></b>
            <span>Selected to the fourth global cohort of researchers driving scientific breakthroughs with Google Cloud.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://indianaite.org/Scholarships" target="_blank" rel="noopener" title="Open Indiana ITE scholarship overview">
          <span class="award-yr">2023</span>
          <div class="award-desc">
            <b>Edward J. Cox Memorial Scholarship <span class="ext-hint">↗</span></b>
            <span>Indiana Section of the Institute of Transportation Engineers (ITE).</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://purdueite.com/" target="_blank" rel="noopener" title="Open Purdue ITE Chapter">
          <span class="award-yr">2022–2023</span>
          <div class="award-desc">
            <b>Best Student Speaker Award <span class="ext-hint">↗</span></b>
            <span>Purdue University ITE Student Chapter.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://doi.org/10.3390/safety8020039" target="_blank" rel="noopener" title="Open Editor's Choice award-winning article">
          <span class="award-yr">2022</span>
          <div class="award-desc">
            <b>Editor's Choice Award <span class="ext-hint">↗</span></b>
            <span>Safety (MDPI) for paper "Methodology for Monitoring Work Zones Traffic Operations Using Connected Vehicle Data."</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://doi.org/10.4236/jtts.2021.114035" target="_blank" rel="noopener" title="Open Project of the Year article">
          <span class="award-yr">2021</span>
          <div class="award-desc">
            <b>ITS Midwest Project of the Year <span class="ext-hint">↗</span></b>
            <span>Intelligent Transportation Society of Midwest for evaluation of queue trucks with navigation alerts using connected vehicle data.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://purdueite.com/" target="_blank" rel="noopener" title="Open Purdue ITE Chapter">
          <span class="award-yr">2021 &amp; 2022</span>
          <div class="award-desc">
            <b>Elevator Pitch Event Winner <span class="ext-hint">↗</span></b>
            <span>Purdue University ITE Student Chapter.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://greatlakesite.org/" target="_blank" rel="noopener" title="Open Great Lakes District ITE">
          <span class="award-yr">2021</span>
          <div class="award-desc">
            <b>Student Team Design Competition Winner <span class="ext-hint">↗</span></b>
            <span>Great Lakes District ITE.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://www.ite.org/membership/students/traffic-bowl/" target="_blank" rel="noopener" title="Open ITE International Traffic Bowl Championship">
          <span class="award-yr">2020</span>
          <div class="award-desc">
            <b>International Collegiate Traffic Bowl Championship <span class="ext-hint">↗</span></b>
            <span>Institute of Transportation Engineers (ITE) International.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://www.purdue.edu/discoverypark/sigmaxi/" target="_blank" rel="noopener" title="Open Purdue Sigma Xi chapter">
          <span class="award-yr">2020</span>
          <div class="award-desc">
            <b>Best Poster Presentation <span class="ext-hint">↗</span></b>
            <span>Sigma Xi Scientific Research Honor Society, Purdue University Chapter.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://engineering.purdue.edu/CE/Academics/Graduate/Scholarships" target="_blank" rel="noopener" title="Open Purdue Lyles School Graduate Scholarships">
          <span class="award-yr">2020–2023</span>
          <div class="award-desc">
            <b>Christopher B. &amp; Susan S. Burke Fellowship <span class="ext-hint">↗</span></b>
            <span>Purdue University graduate program research fellowship.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://civil.iitm.ac.in/" target="_blank" rel="noopener" title="Open IIT Madras Civil Engineering">
          <span class="award-yr">2018</span>
          <div class="award-desc">
            <b>Exemplary &amp; All-Round Best Performance Award <span class="ext-hint">↗</span></b>
            <span>Civil Engineering, Dual-Degree Program, IIT Madras.</span>
          </div>
        </a>
      </li>
      <li>
        <div class="award-item">
          <span class="award-yr">2018</span>
          <div class="award-desc">
            <b>Winner, CEA Technical Competitions</b>
            <span>Case Study, Prabandha, Bon Auto, and Aquanomics — IIT Madras.</span>
          </div>
        </div>
      </li>
      <li>
        <a class="award-item has-link" href="https://engineering.purdue.edu/JTRP" target="_blank" rel="noopener" title="Open Joint Transportation Research Program, Purdue University">
          <span class="award-yr">2017</span>
          <div class="award-desc">
            <b>Invited Visiting Undergraduate Research Scholar <span class="ext-hint">↗</span></b>
            <span>Purdue University (PURE Program).</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://www.ndrf.res.in/" target="_blank" rel="noopener" title="Open National Design and Research Forum">
          <span class="award-yr">2016</span>
          <div class="award-desc">
            <b>Gold Medal in Civil Engineering <span class="ext-hint">↗</span></b>
            <span>National Design and Research Forum, Institution of Engineers, India.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://igs.org.in/" target="_blank" rel="noopener" title="Open Indian Geotechnical Society">
          <span class="award-yr">2016</span>
          <div class="award-desc">
            <b>Mr. H. C. Verma Diamond Jubilee Award &amp; IGS Best Paper <span class="ext-hint">↗</span></b>
            <span>Indian Geotechnical Society.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://jeeadv.ac.in/" target="_blank" rel="noopener" title="Open IIT JEE Advanced Portal">
          <span class="award-yr">2013</span>
          <div class="award-desc">
            <b>IIT Joint Entrance Examination (IIT-JEE) — Top 0.2 Percentile <span class="ext-hint">↗</span></b>
            <span>Ranked 2,445 nationwide among 1.45 million examinees across India.</span>
          </div>
        </a>
      </li>
    </ul>
  </section>
""" + foot()


# =========================================================================
# 7. NEWS & MEDIA (news.html)
# =========================================================================
P["news.html"] = head(
    "News & Media Coverage | Rahul Sakhare, Ph.D., P.E.",
    "Media coverage from The New York Times, FHWA Innovator, Google Cloud, and transportation industry outlets.",
    "sub"
) + nav("news.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>News &amp; Media Coverage</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:24px">
      National press coverage, agency highlights, and industry impact stories featuring our connected vehicle research, work zone safety innovations, and cloud data analytics.
    </p>

    <div class="filters" id="media-filters"></div>
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu", '<script src="media-data.js?v=8.6"></script>\n')


# =========================================================================
# 8. CONTACT (contact.html)
# =========================================================================
P["contact.html"] = head(
    "Contact & Coordinates | Rahul Sakhare, Ph.D., P.E.",
    "Contact Rahul Sakhare — Office location at Purdue University, scholarly profiles, and message portal.",
    "sub"
) + nav("contact.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Contact &amp; Coordinates</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:32px">
      I welcome inquiries regarding research collaborations, discussions with state DOT and municipal partners, conversations with commercial fleet telematics providers, and inquiries from prospective students.
    </p>

    <div class="contact-layout">
      <!-- Left Column: Office Coordinates & Scholarly Profiles -->
      <div class="contact-block">
        <h3>Office Coordinates</h3>
        <p>
          <b>Joint Transportation Research Program (JTRP)</b><br>
          Lyles School of Civil &amp; Construction Engineering<br>
          Purdue University<br><br>
          Hall of Discovery and Learning Research (DLR), Room 204F<br>
          207 S. Martin Jischke Drive<br>
          West Lafayette, IN 47906
        </p>

        <h3 style="margin-top:32px">Scholarly Profiles</h3>
        <p><a href="mailto:rsakhare@purdue.edu">{I["mail"]} rsakhare@purdue.edu</a></p>
        <p><a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">{I["scholar"]} Google Scholar Profile ↗</a></p>
        <p><a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">{I["orcid"]} ORCID (0000-0001-7843-5707) ↗</a></p>
        <p><a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">{I["linkedin"]} LinkedIn Profile ↗</a></p>
        <p><a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">{I["rg"]} ResearchGate Profile ↗</a></p>
      </div>

      <!-- Right Column: Direct Message Form -->
      <div class="contact-block">
        <h3>Send a Direct Message</h3>
        <p style="color:var(--ink-muted);font-size:14.5px;margin-bottom:16px">
          Messages submitted through this portal are delivered directly to my Purdue email inbox.
        </p>
        <form class="contact-form" action="https://formsubmit.co/rsakhare@purdue.edu" method="POST">
          <input type="hidden" name="_subject" value="Research Website Inquiry — Rahul Sakhare Portal">
          <input type="text" name="_honey" style="display:none">
          <input type="text" name="name" placeholder="Your Name" autocomplete="name">
          <input type="email" name="email" placeholder="Your Email Address" required autocomplete="email">
          <textarea name="message" placeholder="Your message or collaboration topic..." required></textarea>
          <button class="btn-submit" type="submit">Send Message →</button>
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

print(f"\nSuccessfully generated {len(P)} site pages with Refined Modern Scholar layout.")
