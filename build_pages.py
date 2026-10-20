#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer (Refined Modern Scholar Architecture).

Typography: Lora (Editorial Serif Headings) + Inter (Scholarly Sans Body)
Aesthetic: Authentic Academic Minimalist (No SaaS cards, no bubble chips, authentic scholarly layout)
"""

import os
import datetime
import json

try:
    with open('scholar.json', 'r', encoding='utf-8') as _sf:
        _sdata = json.load(_sf)
        _sdate = datetime.date.fromisoformat(_sdata.get('updated', datetime.date.today().isoformat()))
        as_of_month = _sdate.strftime("%B %Y")
except Exception:
    as_of_month = datetime.date.today().strftime("%B %Y")

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
 ("projects.html", "Projects"),
 ("education.html", "Education"),
 ("teaching.html", "Teaching"),
 ("awards.html", "Awards"),
 ("news.html", "News"),
 ("contact.html", "Contact")
]

def head(title, desc, body_cls, page_url=""):
    canonical = f"https://rahul-sakhare.github.io/research/{page_url}" if page_url else "https://rahul-sakhare.github.io/research/"
    image_url = "https://rahul-sakhare.github.io/research/assets/img/sakhare_headshot.jpg"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">

<!-- Open Graph / Social Sharing Meta Tags -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rahul Sakhare, Ph.D., P.E. — Academic Research Profile">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{image_url}">
<meta property="og:image:alt" content="Portrait photograph of Rahul Sakhare, Ph.D., P.E., Transportation Research Engineer at Purdue University">
<meta property="og:image:width" content="1080">
<meta property="og:image:height" content="720">

<!-- Twitter Card Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{image_url}">
<meta name="twitter:image:alt" content="Portrait photograph of Rahul Sakhare, Ph.D., P.E., Transportation Research Engineer at Purdue University">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v=9.2">
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
      <ul class="nav-links">{links}<li><a class="cv" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">CV ↗</a></li></ul>
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
{scripts}<script src="script.js?v=9.2"></script>
</body>
</html>"""

P = {}

# =========================================================================
# 1. HOME (index.html) — Authentic Academic Profile Layout
# =========================================================================
P["index.html"] = head(
    "Rahul Sakhare, Ph.D., P.E. | Purdue University",
    "Rahul Sakhare, Ph.D., P.E. — Transportation Research Engineer at Purdue University. Connected vehicle trajectory data, traffic operations, work zone safety, and cloud analytics.",
    "home",
    ""
) + nav("index.html") + f"""
  <section class="wrap profile-section">
    <div class="profile-grid">
      <!-- Left Column: Portrait & Academic Coordinates -->
      <aside class="profile-sidebar">
        <div class="profile-photo-frame">
          <img src="assets/img/sakhare_headshot.jpg" alt="Portrait photograph of Rahul Sakhare, Ph.D., P.E., Transportation Research Engineer at Purdue University in professional business attire" width="1080" height="720">
        </div>
        <div class="profile-sidebar-meta">
          <p><b>Affiliation:</b><br>Joint Transportation Research Program (JTRP), Purdue University</p>
          <p><b>Office:</b><br>Hall of Discovery and Learning Research (DLR), Room 204F<br>West Lafayette, IN 47906</p>
          <p><b>Email:</b><br><a href="mailto:rsakhare@purdue.edu">rsakhare@purdue.edu</a></p>
          <p><b>Credentials:</b><br>Ph.D. Civil Eng, Purdue ('23)<br>M.Tech. &amp; B.Tech., IIT Madras ('18)</p>
          <p><b>Licensure:</b><br>Professional Engineer (P.E.), Indiana (No. PE12600619)</p>
          <p><b>Certification:</b><br><a href="https://www.credly.com/badges/5c0f6fa1-c2d6-4c57-a6d4-d926aecd16b2/public_url" target="_blank" rel="noopener">Google Cloud Certified Generative AI Leader ↗</a></p>
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
            My work translates billions of connected vehicle waypoints and commercial truck telematics into actionable safety and mobility measures deployed daily by transportation agencies for work zone operations, incident management, and capital prioritization.
          </p>
        </div>

        <!-- Understated Scholarly Metrics Summary Bar -->
        <div class="metrics-summary-bar">
          <div class="metrics-items">
            <span><a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&amp;hl=en" target="_blank" rel="noopener" title="View Google Scholar Profile"><b>Google Scholar:</b> <span id="stat-cites" data-to="543">540+</span> citations</a></span>
            <span class="dot">·</span>
            <span><b>h-index:</b> <span id="stat-h" data-to="14">14</span></span>
            <span class="dot">·</span>
            <span><b>i10-index:</b> <span id="stat-i10" data-to="19">19</span></span>
            <span class="dot">·</span>
            <span><b><span id="stat-journal" data-to="32">32</span></b> journal articles</span>
            <span class="dot">·</span>
            <span><b><span id="stat-report" data-to="22">22</span></b> technical reports</span>
          </div>
          <span class="stat-asof" id="stat-asof">as of {as_of_month}</span>
        </div>

        <!-- Selected Publications Preview -->
        <h2>Selected Publications</h2>
        <div class="pub-list">
          <div class="pub has-link" data-url="https://doi.org/10.1007/s11116-026-10736-8" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2026</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Desai, J., Gartner, C., Shellhamer, N., Ruble, T., McCoy, D., &amp; Bullock, D. M. (2026). "Deriving Systemwide Granular Segment Level Traffic Mobility Performance Metrics Using Connected Vehicle Data to Identify Improvement Opportunities." <i>Transportation</i> (Springer Nature).</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.1007/s11116-026-10736-8" target="_blank" rel="noopener">doi.org/10.1007/s11116-026-10736-8 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bsakhare2026transportation%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Desai%2C%20Jash%20and%20Gartner%2C%20Chris%20and%20Shellhamer%2C%20Nathan%20and%20Ruble%2C%20Travis%20and%20McCoy%2C%20Dave%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BDeriving%20Systemwide%20Granular%20Segment%20Level%20Traffic%20Mobility%20Performance%20Metrics%20Using%20Connected%20Vehicle%20Data%20to%20Identify%20Improvement%20Opportunities%7D%2C%0A%20%20journal%20%3D%20%7BTransportation%7D%2C%0A%20%20year%20%3D%20%7B2026%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.1007%2Fs11116-026-10736-8%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.1109/ACCESS.2024.3503368" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2024</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Desai, J., Mathew, J. K., &amp; Bullock, D. M. (2024). "Assessing the Interstate Coverage of Commercial Trucks Capable of Providing Roadway Imagery via On-Vehicle Dash Camera in the United States." <i>IEEE Access</i>, 12, 173517-173529.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.1109/ACCESS.2024.3503368" target="_blank" rel="noopener">doi.org/10.1109/ACCESS.2024.3503368 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bsakhare2024assessing%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Desai%2C%20Jash%20and%20Mathew%2C%20Jijo%20K.%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BAssessing%20the%20Interstate%20Coverage%20of%20Commercial%20Trucks%20Capable%20of%20Providing%20Roadway%20Imagery%20via%20On-Vehicle%20Dash%20Camera%20in%20the%20United%20States%7D%2C%0A%20%20journal%20%3D%20%7BIEEE%20Access%7D%2C%0A%20%20year%20%3D%20%7B2024%7D%2C%0A%20%20volume%20%3D%20%7B12%7D%2C%0A%20%20pages%20%3D%20%7B173517--173529%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.1109%2FACCESS.2024.3503368%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.1109/OJITS.2025.3650100" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2026</div>
            <div>
              <p class="cite">Desai, J. C., Gartner, C. M., <b>Sakhare, R. S.</b>, Cox, E., &amp; Bullock, D. M. (2026). "Evaluating Safety Benefits of Ramp Metering by Leveraging Connected Vehicle Data." <i>IEEE Open Journal of Intelligent Transportation Systems</i>, 7, 190-199.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.1109/OJITS.2025.3650100" target="_blank" rel="noopener">doi.org/10.1109/OJITS.2025.3650100 ↗</a>
                <button class="btn-bib" data-bib="%40article%7Bdesai2026ojits%2C%0A%20%20author%20%3D%20%7BDesai%2C%20Jairaj%20C.%20and%20Gartner%2C%20Christopher%20M.%20and%20Sakhare%2C%20Rahul%20S.%20and%20Cox%2C%20Edward%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BEvaluating%20Safety%20Benefits%20of%20Ramp%20Metering%20by%20Leveraging%20Connected%20Vehicle%20Data%7D%2C%0A%20%20journal%20%3D%20%7BIEEE%20Open%20Journal%20of%20Intelligent%20Transportation%20Systems%7D%2C%0A%20%20year%20%3D%20%7B2026%7D%2C%0A%20%20volume%20%3D%20%7B7%7D%2C%0A%20%20pages%20%3D%20%7B190--199%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.1109%2FOJITS.2025.3650100%7D%0A%7D">Copy BibTeX</button>
              </div>
            </div>
          </div>

          <div class="pub has-link" data-url="https://doi.org/10.5703/1288284317751" tabindex="0" role="link" title="Open publication in new tab">
            <div class="yr">2024</div>
            <div>
              <p class="cite"><b>Sakhare, R. S.</b>, Desai, J., Mathew, J. K., McGregor, J., Kachler, M., &amp; Bullock, D. M. (2024). <i>Measuring and Visualizing Freeway Traffic Conditions: Using Connected Vehicle Data</i> (Joint Transportation Research Program Publication No. FHWA/IN/JTRP-2024/14 / TPF-5(514)). West Lafayette, IN: Purdue University, 506 pages.</p>
              <div class="pub-actions">
                <a class="pub-doi" href="https://doi.org/10.5703/1288284317751" target="_blank" rel="noopener">doi.org/10.5703/1288284317751 ↗</a>
                <button class="btn-bib" data-bib="%40book%7Bsakhare2024measuring%2C%0A%20%20author%20%3D%20%7BSakhare%2C%20Rahul%20S.%20and%20Desai%2C%20Jash%20and%20Mathew%2C%20Jijo%20K.%20and%20McGregor%2C%20Joshua%20and%20Kachler%2C%20Michelle%20and%20Bullock%2C%20Darcy%20M.%7D%2C%0A%20%20title%20%3D%20%7BMeasuring%20and%20Visualizing%20Freeway%20Traffic%20Conditions%3A%20Using%20Connected%20Vehicle%20Data%7D%2C%0A%20%20publisher%20%3D%20%7BPurdue%20University%7D%2C%0A%20%20series%20%3D%20%7BJoint%20Transportation%20Research%20Program%20Publication%20No.%20FHWA%2FIN%2FJTRP-2024%2F14%7D%2C%0A%20%20year%20%3D%20%7B2024%7D%2C%0A%20%20url%20%3D%20%7Bhttps%3A%2F%2Fdoi.org%2F10.5703%2F1288284317751%7D%0A%7D">Copy BibTeX</button>
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
    "sub",
    "about.html"
) + nav("about.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>About Rahul Sakhare, Ph.D., P.E.</h1>
    <p style="font-size:17px;color:var(--ink-muted);margin-bottom:32px">
      Transportation Research Engineer at Purdue University's Joint Transportation Research Program, bridging civil infrastructure systems, connected vehicle telematics, and scalable data analytics.
    </p>

    <div class="profile-grid">
      <aside class="profile-sidebar">
        <div class="profile-photo-frame portrait-frame">
          <img src="assets/img/sakhare_about.png" alt="Portrait photograph of Dr. Rahul Sakhare in Purdue University doctoral academic regalia (black gown and doctoral hood)" width="422" height="471">
        </div>
        <div class="profile-sidebar-meta">
          <p><b>Current Role:</b><br>Transportation Research Engineer<br>JTRP, Purdue University</p>
          <p><b>Licensure:</b><br>Licensed Professional Engineer (P.E.), State of Indiana (No. PE12600619, June 2026)</p>
          <p><b>Certification:</b><br><a href="https://www.credly.com/badges/5c0f6fa1-c2d6-4c57-a6d4-d926aecd16b2/public_url" target="_blank" rel="noopener">Google Cloud Certified Generative AI Leader ↗</a></p>
          <p><b>Research Leadership:</b><br>Co-PI on 4 Active INDOT Grants<br>Lead Engineer on FHWA Pooled-Fund Studies</p>
          <p><b>Industry Experience:</b><br>Executive Consultant, Transportation Team<br>Ernst &amp; Young (EY) LLP (2018–2019)</p>
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
          Alongside research, I actively teach, mentor graduate and undergraduate researchers across Civil Engineering, Electrical &amp; Computer Engineering, Computer Science, and Mechanical Engineering, serve as a member of the TRB Standing Committee on Limited Access Roadway Operations (ACF13), and contribute to the annual Purdue Road School Planning Committee. Prior to doctoral research at Purdue, I gained significant industry experience as an Executive Consultant in the Transportation Team at Ernst &amp; Young (EY) LLP in New Delhi, working on infrastructure advisory and transportation consulting projects. I earned my Ph.D. in Civil Engineering from Purdue University, completed dual B.Tech. and M.Tech. degrees from IIT Madras (ranked top 0.2% in the IIT-JEE), and hold a licensed Professional Engineer (P.E.) credential in Indiana.
        </p>
        <p>
          Beyond engineering research, I have a deep passion for playing cricket. I had the privilege of captaining the Purdue University cricket team to win the 2022 NCAA T-20 Championship Trophy for the Midwest (<a href="https://www.purduecricket.com/" target="_blank" rel="noopener">Purdue Cricket Club ↗</a>). Competitive athletics has shaped my collaborative approach to leadership, high-pressure problem solving, and team mentorship.
        </p>

        <h2>Career Appointments</h2>
        <ul class="award-list">
          <li class="award-item">
            <span class="award-yr">2023 — Present</span>
            <div class="award-desc">
              <b>Transportation Research Engineer</b>
              <div class="appt-inst">Joint Transportation Research Program (JTRP), Purdue University <span class="dot">·</span> <span class="loc">West Lafayette, IN</span></div>
              <span>Leading multi-agency connected vehicle data research, cloud analytics pipelines, and agency deployments for INDOT and FHWA. Co-PI on four active INDOT research grants.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2020 — 2023</span>
            <div class="award-desc">
              <b>Graduate Research Assistant</b>
              <div class="appt-inst">Lyles School of Civil Engineering, Purdue University <span class="dot">·</span> <span class="loc">West Lafayette, IN</span></div>
              <span>Conducted doctoral research under Prof. Darcy M. Bullock on connected vehicle data for operational decision-making. Recipient of the Christopher B. &amp; Susan S. Burke Fellowship.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2018 — 2019</span>
            <div class="award-desc">
              <b>Executive Consultant — Transportation Team (Industry Experience)</b>
              <div class="appt-inst">Ernst &amp; Young (EY) LLP <span class="dot">·</span> <span class="loc">New Delhi, India</span></div>
              <span>Provided strategic advisory and technical consulting on transportation infrastructure, traffic data analysis, and public-sector civil engineering advisory projects.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2017</span>
            <div class="award-desc">
              <b>Visiting Undergraduate Research Student</b>
              <div class="appt-inst">Purdue University <span class="dot">·</span> <span class="loc">West Lafayette, IN</span></div>
              <span>Conducted invited undergraduate research on connected vehicle traffic data and transit GPS estimation under Prof. Darcy M. Bullock.</span>
            </div>
          </li>
          <li class="award-item">
            <span class="award-yr">2016</span>
            <div class="award-desc">
              <b>Summer Researcher — Purdue Undergraduate Research Experience (PURE)</b>
              <div class="appt-inst">Lyles School of Civil Engineering, Purdue University <span class="dot">·</span> <span class="loc">West Lafayette, IN</span></div>
              <span>Selected through the competitive PURE program as one of the top civil engineering students chosen across India (<a href="https://www.purdue.edu/newsroom/archive/purduetoday/releases/2016/Q3/undergraduate-research-experience-for-indian-institute-of-technology-students-addresses-grand-challenges.html" target="_blank" rel="noopener">Purdue Today feature ↗</a>).</span>
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
    "sub",
    "publications.html"
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
""" + foot('<a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&amp;hl=en" target="_blank" rel="noopener" title="View Google Scholar Profile">Google Scholar: 540+ citations · h-index 14 · i10-index 19 ↗</a>', '<script src="pubs-data.js"></script>\n')


# =========================================================================
# 4. PROJECTS (projects.html) — Sponsored Research Portfolio
# =========================================================================
PROJECTS_DATA = [
    {
        "code": "FHWA · TPF-5(514)",
        "title": "Work Zone Analytics",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "FHWA",
        "period": "2023–2026",
        "funding": "$890,000",
        "sponsor": "Federal Highway Administration (FHWA) Pooled Fund Consortium",
        "lead": "Indiana Department of Transportation (INDOT) & Purdue University",
        "partners": "FHWA, INDOT, Delaware DOT, Illinois DOT, Maryland SHA, Massachusetts DOT, Michigan DOT, Pennsylvania DOT, Texas DOT, Utah DOT, Wisconsin DOT",
        "desc": "Multi-state transportation pooled fund consortium developing scalable cloud-native analytics, automated performance measures, and real-time mobility dashboards using connected vehicle trajectory data across 10 participating state highway agencies.",
        "links": [
            ("FHWA Pooled Fund Study (TPF-5(514))", "https://pooledfund.org/Details/Study/746"),
            ("JTRP Monograph & Technical Publication", "https://doi.org/10.5703/1288284317751")
        ]
    },
    {
        "code": "FHWA · TPF-5(519)",
        "title": "Expansion: Enhanced Traffic Signal Performance Measures",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "FHWA",
        "period": "2023–2026",
        "funding": "$1,300,000",
        "sponsor": "Federal Highway Administration (FHWA) Pooled Fund Consortium",
        "lead": "Indiana Department of Transportation (INDOT) & Purdue University",
        "partners": "Multi-State Transportation Pooled Fund Consortium",
        "desc": "Expanding Automated Traffic Signal Performance Measures (ATSPM) across statewide arterial networks utilizing commercial probe vehicle trajectory data for split failure diagnostics, arterial coordination screening, and control delay quantification.",
        "links": [
            ("FHWA Pooled Fund Study (TPF-5(519))", "https://pooledfund.org/Details/Study/751")
        ]
    },
    {
        "code": "INDOT · SPR-5005",
        "title": "Evaluation of Asset Identification Technology",
        "role": "Co-Principal Investigator (Co-PI)",
        "role_type": "Co-PI",
        "role_class": "copi",
        "sponsor_type": "INDOT",
        "period": "2025–2027",
        "funding": "$301,966",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Asset Management Division",
        "desc": "Developing edge-computing and computer vision pipelines to analyze truck-mounted camera imagery and telematics for automated statewide roadway asset identification, inventory verification, and condition scoring.",
        "links": [
            ("JTRP Research Program", "https://engineering.purdue.edu/JTRP/Research")
        ]
    },
    {
        "code": "INDOT · SPR-5021",
        "title": "Traffic Signal Freight Prioritization via Vehicle to Infrastructure (V2I) Communications",
        "role": "Co-Principal Investigator (Co-PI)",
        "role_type": "Co-PI",
        "role_class": "copi",
        "sponsor_type": "INDOT",
        "period": "2026–2027",
        "funding": "$383,966",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Management & Commercial Telematics Providers (Drivewyze)",
        "desc": "Pioneering cloud-based vehicle-to-infrastructure (V2I) communication with third-party in-cab telematics to extend green intervals for heavy freight trucks approaching intersection decision zones, reducing hard braking, tailpipe emissions, and pavement wear.",
        "links": [
            ("JTRP Research Program", "https://engineering.purdue.edu/JTRP/Research")
        ]
    },
    {
        "code": "INDOT · SPR-5020",
        "title": "Identifying Locations with Abnormally High Wrong Way Driving or Interstate U-Turns",
        "role": "Co-Principal Investigator (Co-PI)",
        "role_type": "Co-PI",
        "role_class": "copi",
        "sponsor_type": "INDOT",
        "period": "2025–2027",
        "funding": "$224,109",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Safety & Operations",
        "desc": "Systemwide spatial screening of vehicle trajectory heading vectors and waypoint sequences to detect high-risk interchange ramps, wrong-way driving movements, and unauthorized median crossovers across Indiana interstates.",
        "links": [
            ("JTRP Research Program", "https://engineering.purdue.edu/JTRP/Research")
        ]
    },
    {
        "code": "INDOT · SPR-4928",
        "title": "Connected Vehicle Trajectory Data to Screen Network for Hard Braking and Hard Acceleration Events",
        "role": "Co-Principal Investigator (Co-PI)",
        "role_type": "Co-PI",
        "role_class": "copi",
        "sponsor_type": "INDOT",
        "period": "2024–2025",
        "funding": "$218,390",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Office of Systems Analysis and Planning",
        "desc": "Engineered systemic safety screening algorithms utilizing longitudinal acceleration telematics to identify friction hotspots, queue tails, and interchange merge conflicts before crash accumulation occurs.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/30)", "https://doi.org/10.5703/1288284318579")
        ]
    },
    {
        "code": "INDOT · SPR-4933",
        "title": "Worksite Speed Control System (WSCS)",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2024–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Construction & Work Zone Operations",
        "desc": "Empirical evaluation of worksite speed control technologies and automated speed photo enforcement systems, evaluating driver compliance, speed variance, and highway construction worker safety.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/33)", "https://doi.org/10.5703/1288284318595")
        ]
    },
    {
        "code": "INDOT · SPR-4907",
        "title": "Systemwide Asset Condition Assessment using Connected Vehicle Data",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2024–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Asset Management & Maintenance",
        "desc": "Harvested vertical acceleration sensor telemetry, chassis vibrations, and optical camera streams to monitor pavement surface roughness, detect pavement distress, and automate road asset condition scoring.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2026/04)", "https://doi.org/10.5703/1288284318612")
        ]
    },
    {
        "code": "INDOT · SPR-4857",
        "title": "Statewide Screening of Signalized Intersections for Capacity Improvements",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2023–2024",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Engineering Division",
        "desc": "Leveraged billions of vehicle trajectory records to evaluate and rank thousands of signalized intersections across Indiana, quantifying split failures, green allocation efficiency, and retiming priorities.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2024/20)", "https://doi.org/10.5703/1288284317755")
        ]
    },
    {
        "code": "INDOT · SPR-4854",
        "title": "MOT for MOT: Case Studies Documenting Lessons Learned and Opportunities for Maintenance of Traffic Improvements",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2023–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Division of Construction Management",
        "desc": "Analyzed empirical queueing, speed reductions, and crash patterns during maintenance of traffic (MOT) transitions across major interstate reconstruction corridors to improve future MOT contract designs.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/29)", "https://doi.org/10.5703/1288284318578")
        ]
    },
    {
        "code": "INDOT · SPR-4851",
        "title": "Development of Incident Management Performance Measure Database and IN-TIME Training Material",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2023–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Incident Management (IN-TIME) & Indiana State Police",
        "desc": "Synthesized multi-source traffic telemetry, CAD logs, and roadside camera feeds to build automated incident timeline metrics (roadway clearance, scene clearance, secondary crash detection) for first-responder training.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/21)", "https://doi.org/10.5703/1288284317907")
        ]
    },
    {
        "code": "INDOT · SPR-4850",
        "title": "Continued Deployment of Indiana Work Zone Analytics",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2023–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Engineering & Operations",
        "desc": "Maintained, refined, and deployed statewide automated work zone monitoring dashboards tracking daily and weekly queuing, congestion hours, speed compliance, and traveler delay across hundreds of construction contracts.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/31)", "https://doi.org/10.5703/1288284318581")
        ]
    },
    {
        "code": "INDOT · SPR-4803",
        "title": "Communication of Fixed and Mobile Warning to Commercial Trucks Using In-Cab Notification",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2023–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Freight Office & Commercial Telematics Providers (Drivewyze)",
        "desc": "Demonstrated and evaluated in-cab dynamic safety alerts delivering real-time queue warnings, sudden slowdown advisories, and rollover risk alerts directly to thousands of heavy commercial motor vehicles on Indiana interstates.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/24)", "https://doi.org/10.5703/1288284318232")
        ]
    },
    {
        "code": "INDOT · SPR-4704",
        "title": "Evaluating the Robustness of MDSS Forecast and Compliance with Recommendations",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2022–2024",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Winter Operations & Maintenance",
        "desc": "Assessed Maintenance Decision Support System (MDSS) winter storm forecasts, comparing automated recommendations against automated vehicle location (AVL) spreader records and post-storm traffic speed recovery.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2024/31)", "https://doi.org/10.5703/1288284317805")
        ]
    },
    {
        "code": "INDOT · SPR-4639",
        "title": "Connected Vehicle Centric Dashboards for TMC of the Future",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2021–2023",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Management Center (TMC)",
        "desc": "Architected next-generation traffic management center web dashboards integrating high-frequency trajectory speeds, automated anomaly detection, and queue alert triggers for real-time operations.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2023/17)", "https://doi.org/10.5703/1288284317642")
        ]
    },
    {
        "code": "INDOT · SPR-4636",
        "title": "Research Support to INDOT on I-465 Southeast Variable Speed Limit and Ramp Meter Project",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "INDOT",
        "period": "2021–2025",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Greenfield District & Traffic Operations",
        "desc": "Rigorous before-and-after operational performance assessment of Indiana’s premier dynamic variable speed limit (VSL) and ramp metering installation along the congested I-465 Southeast corridor.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2025/32)", "https://doi.org/10.5703/1288284318592")
        ]
    },
    {
        "code": "INDOT · SPR-4603",
        "title": "Crowdsourcing / Winter Operations Dashboard Upgrade",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2021–2023",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Maintenance & Public Safety",
        "desc": "Upgraded enterprise winter maintenance dashboards merging crowdsourced incident data (Waze CCP), snowplow GPS tracking, and probe speed recovery metrics to optimize winter maintenance operations.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2023/21)", "https://doi.org/10.5703/1288284317652")
        ]
    },
    {
        "code": "INDOT · SPR-4536",
        "title": "Implementation of Enhanced Probe Data (CANBUS) for Tactical Workzone and Winter Operations Management",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2020–2023",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Operations & Commercial Vehicle Telematics",
        "desc": "Investigated vehicle CANBUS sensor feeds (active wipers, anti-lock braking, electronic stability control) to provide real-time hyper-local weather detection and pavement friction assessments.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2023/18)", "https://doi.org/10.5703/1288284317643")
        ]
    },
    {
        "code": "CCAT · UTC Grant",
        "title": "Methodologies for Monitoring Work Zone Performance Measures across State Border Highways using Connected Vehicle Data",
        "role": "Research Engineer (RE)",
        "role_type": "RE",
        "role_class": "re",
        "sponsor_type": "CCAT",
        "period": "2023–2025",
        "funding": "",
        "sponsor": "Center for Connected and Automated Transportation (CCAT)",
        "lead": "USDOT Tier 1 University Transportation Center (CCAT / Purdue University)",
        "partners": "Regional State DOT Partners (INDOT, IDOT, MDOT)",
        "desc": "Bridged jurisdictional boundaries by developing methods to track queue propagation, back-of-queue secondary crashes, and travel delays extending across interstate state line borders without roadside sensors.",
        "links": [
            ("CCAT UTC Research Consortium", "https://ccat.umtri.umich.edu/")
        ]
    },
    {
        "code": "INDOT · SPR-4600",
        "title": "Impacts to Traffic Behavior from Queue Warning Truck: Current Pilot Project",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2021–2022",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Work Zone Safety Committee",
        "desc": "Field evaluation of truck-mounted dynamic message signs (queue warning trucks) equipped with digital alerts, measuring upstream traffic deceleration, driver compliance, and hard-braking mitigation.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2022/26)", "https://doi.org/10.5703/1288284317448")
        ]
    },
    {
        "code": "INDOT · SPR-4524",
        "title": "Evaluation of the Impact of On-Vehicle Digital Communication Alerts to Improve INDOT and Motorist Safety",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2020–2022",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Maintenance & HAAS Alert Safety Cloud",
        "desc": "Quantified driver deceleration behavior and earlier lane-change maneuvers in response to digital in-vehicle notifications alerting approaching motorists to maintenance and emergency responders.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2021/27)", "https://doi.org/10.5703/1288284317324")
        ]
    },
    {
        "code": "INDOT · SPR-4451",
        "title": "Integration of Probe Data Tools into TMC Operations",
        "role": "Graduate Research Assistant (GRA)",
        "role_type": "GRA",
        "role_class": "gra",
        "sponsor_type": "INDOT",
        "period": "2020–2022",
        "funding": "",
        "sponsor": "Indiana Department of Transportation (INDOT) / JTRP",
        "lead": "Joint Transportation Research Program, Purdue University",
        "partners": "INDOT Traffic Management Center (TMC)",
        "desc": "Operational integration of high-density commercial vehicle probe speed feeds into statewide TMC incident dispatch, congestion monitoring, and operator decision support.",
        "links": [
            ("JTRP Final Report (FHWA/IN/JTRP-2022/01)", "https://doi.org/10.5703/1288284317363")
        ]
    }
]

proj_cards_html = []
for p in PROJECTS_DATA:
    funding_badge = f'<span class="proj-funding">{p["funding"]}</span>' if p["funding"] else ''
    
    links_html = []
    for lbl, url in p["links"]:
        links_html.append(f'<a class="proj-link-btn" href="{url}" target="_blank" rel="noopener">{lbl} ↗</a>')
    links_block = f'<div class="proj-links">{"".join(links_html)}</div>' if links_html else ''
    
    partners_html = f'<br><b>Agency Partners:</b> {p["partners"]}' if p.get("partners") else ''
    
    card = f"""
      <article class="project-card role-{p['role_class']}" data-role="{p['role_type']}" data-sponsor="{p['sponsor_type']}">
        <div class="proj-top">
          <div class="proj-tags">
            <span class="proj-code">{p['code']}</span>
            <span class="proj-role-badge badge-{p['role_class']}">{p['role']}</span>
          </div>
          <div class="proj-meta-right">
            <span class="proj-period">{p['period']}</span>
          </div>
        </div>
        <h3>{p['title']}</h3>
        <div class="proj-meta-line">
          <b>Sponsor:</b> {p['sponsor']}<br>
          <b>Lead Entity:</b> {p['lead']}{partners_html}
        </div>
        <div class="proj-desc">
          {p['desc']}
        </div>
        {links_block}
      </article>"""
    proj_cards_html.append(card)

projects_cards_rendered = "\n".join(proj_cards_html)

projects_script = """<script>
(function(){
  const searchInput = document.getElementById('proj-search-input');
  const clearBtn = document.getElementById('proj-clear-btn');
  const roleFilters = document.querySelectorAll('.role-filter');
  const sponsorFilters = document.querySelectorAll('.sponsor-filter');
  const cards = document.querySelectorAll('.project-card');
  const countEl = document.getElementById('proj-visible-count');
  const noMatches = document.getElementById('proj-no-matches');

  let currentRole = 'all';
  let currentSponsor = 'all';
  let currentQuery = '';

  function filterProjects() {
    let visible = 0;
    const q = currentQuery.toLowerCase().trim();

    cards.forEach(card => {
      const role = card.getAttribute('data-role');
      const sponsor = card.getAttribute('data-sponsor');
      const text = card.textContent.toLowerCase();

      const matchRole = (currentRole === 'all' || role === currentRole);
      const matchSponsor = (currentSponsor === 'all' || sponsor === currentSponsor);
      const matchQuery = (!q || text.includes(q));

      if (matchRole && matchSponsor && matchQuery) {
        card.style.display = '';
        visible++;
      } else {
        card.style.display = 'none';
      }
    });

    if (countEl) countEl.textContent = visible;
    if (noMatches) {
      if (visible === 0) noMatches.classList.remove('hidden');
      else noMatches.classList.add('hidden');
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentQuery = e.target.value;
      if (clearBtn) {
        if (currentQuery) clearBtn.classList.add('visible');
        else clearBtn.classList.remove('visible');
      }
      filterProjects();
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentQuery = '';
      clearBtn.classList.remove('visible');
      searchInput.focus();
      filterProjects();
    });
  }

  roleFilters.forEach(btn => {
    btn.addEventListener('click', () => {
      roleFilters.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentRole = btn.getAttribute('data-role');
      filterProjects();
    });
  });

  sponsorFilters.forEach(btn => {
    btn.addEventListener('click', () => {
      sponsorFilters.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentSponsor = btn.getAttribute('data-sponsor');
      filterProjects();
    });
  });
})();
</script>
"""

P["projects.html"] = head(
    "Sponsored Research Projects | Rahul Sakhare, Ph.D., P.E.",
    "Federal, multi-state pooled fund, and state DOT sponsored research projects led and engineered by Rahul Sakhare, Ph.D., P.E. at Purdue University.",
    "sub",
    "projects.html"
) + nav("projects.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Sponsored Research Projects</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:24px">
      Consolidated portfolio of 22 federal, multi-state pooled fund, and state DOT sponsored research projects spanning connected vehicle telemetry, work zone safety, automated traffic signal performance, systemic safety screening, and cloud infrastructure. Search by keyword or filter by scholarly role and sponsoring agency.
    </p>

    <!-- Role Definition & Framework Legend -->
    <div class="projects-legend">
      <span class="legend-title">Role Framework:</span>
      <span class="legend-item"><span class="proj-role-badge badge-copi">Co-PI</span> <b>Co-Principal Investigator</b></span>
      <span class="legend-item"><span class="proj-role-badge badge-re">RE</span> <b>Research Engineer</b></span>
      <span class="legend-item"><span class="proj-role-badge badge-gra">GRA</span> <b>Graduate Research Assistant</b></span>
    </div>

    <!-- Search & Filter Toolbar -->
    <div class="projects-toolbar">
      <div class="pub-search-wrap">
        <svg class="pub-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" class="pub-search-input" id="proj-search-input" placeholder="Search by project title, keyword, grant number, sponsor, or role (e.g. 'work zone', 'SPR-5021', 'freight', 'Drivewyze')..." autocomplete="off">
        <button class="pub-clear-btn" id="proj-clear-btn" title="Clear search">✕</button>
      </div>

      <div class="filter-group">
        <span class="filter-group-label">Role:</span>
        <div class="filters">
          <button class="filter role-filter active" data-role="all" type="button">All Roles (22)</button>
          <button class="filter role-filter" data-role="Co-PI" type="button">Co-Principal Investigator (4)</button>
          <button class="filter role-filter" data-role="RE" type="button">Research Engineer (12)</button>
          <button class="filter role-filter" data-role="GRA" type="button">Graduate Research Assistant (6)</button>
        </div>
      </div>

      <div class="filter-group">
        <span class="filter-group-label">Sponsor:</span>
        <div class="filters">
          <button class="filter sponsor-filter active" data-sponsor="all" type="button">All Sponsors</button>
          <button class="filter sponsor-filter" data-sponsor="FHWA" type="button">FHWA Pooled Funds (2)</button>
          <button class="filter sponsor-filter" data-sponsor="INDOT" type="button">INDOT / JTRP (19)</button>
          <button class="filter sponsor-filter" data-sponsor="CCAT" type="button">CCAT UTC (1)</button>
        </div>
      </div>
    </div>

    <!-- Live Counter -->
    <div style="font-size:14px;color:var(--ink-muted);margin-bottom:18px">
      Showing <b id="proj-visible-count" style="color:var(--ink-heading)">22</b> of 22 sponsored projects
    </div>

    <!-- No Matches Fallback -->
    <div id="proj-no-matches" class="hidden" style="padding:48px 0;text-align:center;color:var(--ink-muted)">
      <h3>No matching projects found</h3>
      <p>Try refining your search query or resetting the filters above.</p>
    </div>

    <!-- Projects List -->
    <div class="projects-list" id="projects-list">
{projects_cards_rendered}
    </div>
  </section>
""" + foot("Purdue University · JTRP", projects_script)


# =========================================================================
# 5. EDUCATION (education.html)
# =========================================================================
P["education.html"] = head(
    "Education & Licensure | Rahul Sakhare, Ph.D., P.E.",
    "Academic degrees from Purdue University and IIT Madras, and professional engineering licensure.",
    "sub",
    "education.html"
) + nav("education.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Education, Licensure &amp; Certification</h1>
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
        <h3><b>Doctor of Philosophy (Ph.D.) in Civil Engineering</b></h3>
        <div class="inst">Purdue University — Lyles School of Civil Engineering</div>
        <p><b>Focus Area:</b> Transportation and Infrastructure Systems (TIS)</p>
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
        <h3><b>Master of Technology (M.Tech.) in Transportation Engineering</b></h3>
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
        <h3><b>Bachelor of Technology (B.Tech.) in Civil Engineering</b></h3>
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
        <h3><b>Professional Engineer (P.E.)</b></h3>
        <div class="inst">State of Indiana — State Board of Registration for Professional Engineers</div>
        <p><b>License Number:</b> PE12600619 (Active · Issued June 2026)</p>
        <p>Discipline: Civil &amp; Transportation Engineering. Licensed professional engineer upholding public safety, technical rigor, and ethical engineering standards.</p>
      </div>
    </div>

    <div class="edu-entry">
      <div class="edu-meta">
        <span class="yr">Certification</span>
        <span>Google Cloud</span>
        <div style="margin-top:6px"><a href="https://www.credly.com/badges/5c0f6fa1-c2d6-4c57-a6d4-d926aecd16b2/public_url" target="_blank" rel="noopener">Credly Badge ↗</a></div>
      </div>
      <div class="edu-detail">
        <h3><b>Google Cloud Certified Generative AI Leader</b></h3>
        <div class="inst">Google Cloud Certification</div>
        <p>Professional certification validating expertise in enterprise AI technologies, Google Cloud infrastructure, data governance, and scalable cloud analytics for modern engineering workflows.</p>
        <p style="margin-top:8px"><a href="https://www.credly.com/badges/5c0f6fa1-c2d6-4c57-a6d4-d926aecd16b2/public_url" target="_blank" rel="noopener">View Verified Credly Badge ↗</a></p>
      </div>
    </div>
  </section>
""" + foot()


# =========================================================================
# 6. TEACHING & MENTORSHIP (teaching.html)
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
    {"name":"Ahsmitha Sivakumar", "deg":"B.Tech. in Civil Engineering", "dept":"IIT Madras Civil Engineering (PURE Scholar at Purdue)",
     "topic":"Toll plaza performance measures and evaluation of privacy filters in probe trajectory datasets.",
     "proj":"Smart Cities 2024"},
    {"name":"Anirud Nandakumar", "deg":"B.Tech. in Civil Engineering", "dept":"IIT Madras Civil Engineering (PURE Scholar at Purdue)",
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
    "sub",
    "teaching.html"
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

    <!-- Invited Lectures, Workshops & Teaching Experience -->
    <h2>Invited Lectures, Workshops &amp; Teaching Experience</h2>
    <p style="font-size:15px;color:var(--ink-muted);margin-bottom:20px">
      Classroom guest lectures, international instructional workshops, and university laboratory teaching experience:
    </p>
    <ul class="award-list" style="margin-bottom:48px">
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

    <!-- Courses Prepared to Teach / Areas of Competence -->
    <h2>Courses Prepared to Teach &amp; Areas of Competence</h2>
    <p style="font-size:15px;color:var(--ink-muted);margin-bottom:20px">
      Core undergraduate and graduate subject areas in which I have deep technical proficiency, established instructional plans, and am prepared and eager to teach:
    </p>
    <div class="teach-grid" style="margin-bottom:48px">
      <div class="teach-item">
        <span class="level">Prepared to Teach · Undergraduate Core</span>
        <h3>Transportation Engineering</h3>
        <p>Traffic flow fundamentals, roadway geometric design, signalized intersection capacity, highway operations, and emerging intelligent transportation systems (CE 36100 equivalent).</p>
      </div>
      <div class="teach-item">
        <span class="level">Prepared to Teach · Graduate Core</span>
        <h3>Big Data Analytics in Transportation Systems</h3>
        <p>Cloud-native spatial-temporal analytics, distributed SQL (BigQuery), connected vehicle trajectory processing, probe data validation, and performance measure engineering.</p>
      </div>
      <div class="teach-item">
        <span class="level">Prepared to Teach · Graduate Elective</span>
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
  </section>
""" + foot()


# =========================================================================
# 7. AWARDS (awards.html)
# =========================================================================
P["awards.html"] = head(
    "Honors & Awards | Rahul Sakhare, Ph.D., P.E.",
    "Academic, professional, and research accolades of Rahul Sakhare, Ph.D., P.E.",
    "sub",
    "awards.html"
) + nav("awards.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Honors &amp; Awards</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:28px">
      Selected accolades across engineering research, public agency deployments, academic scholarship, and international technical competitions.
    </p>

    <ul class="award-list">
      <li>
        <a class="award-item has-link" href="https://engineering.purdue.edu/Engr/People/Staff/prime-grants" target="_blank" rel="noopener" title="Open Purdue PRIME Grant announcement">
          <span class="award-yr">2026</span>
          <div class="award-desc">
            <b>PRIME Grant Award <span class="ext-hint">↗</span></b>
            <span>Purdue University in support of professional development and academic scholarship.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://cloud.google.com/blog/topics/public-sector/google-cloud-research-innovators-launch-fourth-cohort-to-drive-innovation/#:~:text=Rahul%20Suryakant%20Sakhare" target="_blank" rel="noopener" title="Open Google Cloud Research Innovators announcement highlighting Rahul Suryakant Sakhare">
          <span class="award-yr">2024</span>
          <div class="award-desc">
            <b>Google Cloud Research Innovator <span class="ext-hint">↗</span></b>
            <span>Selected to the fourth global cohort of researchers driving scientific breakthroughs with Google Cloud.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://indianaite.org/Scholarship#:~:text=Rahul%20Sakhare" target="_blank" rel="noopener" title="Open Indiana ITE scholarship listing for Rahul Sakhare">
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
        <a class="award-item has-link" href="https://www.mdpi.com/2313-576X/8/2/41" target="_blank" rel="noopener" title="Open Editor's Choice award-winning article">
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
            <b>Invited Visiting Undergraduate Student <span class="ext-hint">↗</span></b>
            <span>Purdue University, West Lafayette.</span>
          </div>
        </a>
      </li>
      <li>
        <a class="award-item has-link" href="https://www.purdue.edu/newsroom/archive/purduetoday/releases/2016/Q3/undergraduate-research-experience-for-indian-institute-of-technology-students-addresses-grand-challenges.html" target="_blank" rel="noopener" title="Open Purdue Today feature on PURE program">
          <span class="award-yr">2016</span>
          <div class="award-desc">
            <b>PURE Program Scholar <span class="ext-hint">↗</span></b>
            <span>Among top three civil engineering students chosen across India for the Purdue Undergraduate Research Experience.</span>
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
# 8. NEWS & MEDIA (news.html)
# =========================================================================
P["news.html"] = head(
    "News & Media Coverage | Rahul Sakhare, Ph.D., P.E.",
    "Media coverage from The New York Times, FHWA Innovator, Google Cloud, and transportation industry outlets.",
    "sub",
    "news.html"
) + nav("news.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>News &amp; Media Coverage</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:24px">
      National press coverage, agency highlights, and industry impact stories featuring our connected vehicle research, work zone safety innovations, and cloud data analytics.
    </p>

    <div class="filters" id="media-filters"></div>
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu", '<script src="media-data.js?v=8.8"></script>\n')


# =========================================================================
# 9. CONTACT (contact.html)
# =========================================================================
P["contact.html"] = head(
    "Contact & Coordinates | Rahul Sakhare, Ph.D., P.E.",
    "Contact Rahul Sakhare — Office location at Purdue University, scholarly profiles, and message portal.",
    "sub",
    "contact.html"
) + nav("contact.html") + f"""
  <section class="wrap" style="padding-top:36px">
    <h1>Contact &amp; Coordinates</h1>
    <p style="font-size:16px;color:var(--ink-muted);max-width:85ch;margin-bottom:20px">
      I welcome inquiries regarding research collaborations, discussions with state DOT and municipal partners, conversations with commercial fleet telematics providers, and inquiries from prospective students.
    </p>

    <!-- Scholarly Quote -->
    <blockquote class="contact-quote">
      “If I have seen further it is by standing on the shoulders of giants.”
      <cite>— Sir Isaac Newton</cite>
    </blockquote>

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
