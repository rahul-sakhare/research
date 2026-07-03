#!/usr/bin/env python3
"""Generate all site pages with shared head/nav/footer."""

FONTS = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Public+Sans:wght@400;500;600;700&display=swap"

NAV_ITEMS = [("index.html","Home"),("about.html","About"),("research.html","Research"),
 ("publications.html","Publications"),("education.html","Education"),("teaching.html","Teaching"),
 ("news.html","News & Media"),("contact.html","Contact")]

def head(title, desc):
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
<body>"""

def nav(active):
    links = "".join(
        f'<li><a href="{h}"{" class=\"active\"" if h==active else ""}>{t}</a></li>'
        for h,t in NAV_ITEMS)
    return f"""<header class="site-head">
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

# ---------------- HOME (landing) ----------------
P["index.html"] = head("Rahul Sakhare, Ph.D., P.E. | Transportation Research Engineer",
 "Rahul Sakhare — Transportation Research Engineer at Purdue University. Connected vehicle data, traffic safety, work zones, and surrogate safety measures.") + nav("index.html") + """
  <section class="hero wrap">
    <p class="loc">TRANSPORTATION RESEARCH ENGINEER · <b>PURDUE UNIVERSITY</b> · WEST LAFAYETTE, IN</p>
    <h1>Turning connected-vehicle data into <span class="flow">safer roads</span>.</h1>
    <p class="lede">I build scalable performance measures from billions of connected-vehicle and probe records — helping DOTs and FHWA see traffic safety and mobility in near real time, from work zones and winter storms to hard-braking risk.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="research.html">Explore research →</a>
      <a class="btn btn-ghost" href="assets/Sakhare_CV.pdf" target="_blank" rel="noopener">Download CV</a>
      <a class="btn btn-ghost" href="contact.html">Get in touch</a>
    </div>
    <div class="readout" role="group" aria-label="Research metrics">
      <div class="cell"><div class="num" data-to="476">476</div><div class="lab">Citations</div></div>
      <div class="cell"><div class="num" data-to="13">13</div><div class="lab">h-index</div></div>
      <div class="cell"><div class="num" data-to="18">18</div><div class="lab">i10-index</div></div>
      <div class="cell"><div class="num" data-to="31">31</div><div class="lab">Journal articles</div></div>
      <div class="cell"><div class="num" data-to="22">22</div><div class="lab">Technical reports</div></div>
      <div class="cell"><div class="num" id="dl-num" data-to="37532">37,532</div><div class="lab">Downloads &amp; views</div></div>
    </div>
    <nav class="dir" aria-label="Site directory">
      <a href="about.html"><span class="t">About</span><span class="d">Background, role at JTRP, and research interests</span><span class="go">→</span></a>
      <a href="research.html"><span class="t">Research</span><span class="d">Focus areas and selected impact</span><span class="go">→</span></a>
      <a href="publications.html"><span class="t">Publications</span><span class="d">91 journal articles, reports &amp; presentations</span><span class="go">→</span></a>
      <a href="education.html"><span class="t">Education</span><span class="d">Purdue · IIT Madras</span><span class="go">→</span></a>
      <a href="teaching.html"><span class="t">Teaching</span><span class="d">Instruction and mentoring</span><span class="go">→</span></a>
      <a href="news.html"><span class="t">News &amp; Media</span><span class="d">NYT, FHWA, Google Cloud and 20+ more</span><span class="go">→</span></a>
    </nav>
  </section>
""" + foot("Built for research · West Lafayette, IN")

# ---------------- ABOUT ----------------
P["about.html"] = head("About | Rahul Sakhare, Ph.D., P.E.",
 "About Rahul Sakhare — Transportation Research Engineer at Purdue University's Joint Transportation Research Program.") + nav("about.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">About</span>
    <h1>Research that reaches practice.</h1>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:20px">
    <div class="about-grid">
      <div class="reveal">
        <p>I'm a Transportation Research Engineer at Purdue University's Joint Transportation Research Program (JTRP), where I turn large-scale connected-vehicle and probe data into performance measures that transportation agencies can act on. My work spans traffic safety, work zones, winter and incident operations, and the emerging use of vehicle-based metrics — such as hard braking — as surrogate safety measures.</p>
        <p>Much of this research is deployed at statewide scale with INDOT and FHWA, and has informed how agencies monitor mobility during winter storms, work zones, and large events like the 2024 solar eclipse. I earned my Ph.D. at Purdue and my bachelor's and master's at IIT Madras, and I'm a licensed Professional Engineer in Indiana.</p>
        <div class="interests">
          <span class="tag">Connected Vehicle Data</span>
          <span class="tag">Surrogate Safety Measures</span>
          <span class="tag">Work Zone Safety</span>
          <span class="tag">Big Data Analytics</span>
          <span class="tag">Connected &amp; Autonomous Vehicles</span>
          <span class="tag">Traffic Shock Wave Theory</span>
          <span class="tag">Scalable Performance Measures</span>
        </div>
      </div>
      <div class="about-side">
        <div class="about-photo-wrap reveal"><img class="about-photo" id="parallax-photo" src="assets/img/about_photo.jpg" alt="Rahul Sakhare, Purdue University" width="780" height="856"></div>
        <aside class="about-card reveal">
          <h3>At a glance</h3>
          <div class="row"><b>Role</b><span>Transportation Research Engineer</span></div>
          <div class="row"><b>Lab</b><span>JTRP, Purdue University</span></div>
          <div class="row"><b>Based in</b><span>West Lafayette, IN</span></div>
          <div class="row"><b>License</b><span>Professional Engineer (Indiana)</span></div>
          <div class="row"><b>Certified</b><span>Google Cloud Generative AI Leader</span></div>
          <div class="row"><b>TRB committee</b><span>ACF13 — Limited Access Roadway Operations</span></div>
        </aside>
      </div>
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

# ---------------- RESEARCH ----------------
P["research.html"] = head("Research | Rahul Sakhare, Ph.D., P.E.",
 "Research focus areas — connected vehicle data, surrogate safety measures, work zones, and scalable performance measures.") + nav("research.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">Research</span>
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
        <div class="pop"><b>In practice:</b> queue-truck alerts recognized as ITS Midwest 2021 Project of the Year, automated worksite speed enforcement evaluation, and Editor's Choice work-zone monitoring methodology in <i>Safety</i>.</div></div>
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

# ---------------- PUBLICATIONS ----------------
P["publications.html"] = head("Publications | Rahul Sakhare, Ph.D., P.E.",
 "Peer-reviewed journal articles, technical reports, and conference presentations by Rahul Sakhare.") + nav("publications.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">Publications</span>
    <h1>Publications</h1>
    <p>Peer-reviewed journal articles, technical reports for INDOT &amp; FHWA, and conference presentations on connected-vehicle data, traffic safety, and performance measures. Each card links to its DOI or archive — click anywhere on it.</p>
  </section>
  <div class="wrap"><div class="filters" id="filters"></div></div>
  <div class="wrap"><div id="pub-root"></div></div>
""" + foot("Google Scholar: 476 citations · h-index 13 · i10-index 18",
           '<script src="pubs-data.js"></script>\n')

# ---------------- EDUCATION ----------------
P["education.html"] = head("Education | Rahul Sakhare, Ph.D., P.E.",
 "Education — Ph.D. Purdue University; M.Tech. and B.Tech. IIT Madras.") + nav("education.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">Education</span>
    <h1>Education.</h1>
    <p>Doctoral work at Purdue on connected-vehicle data for operational decisions, built on a transportation-engineering foundation from IIT Madras.</p>
  </section>
  <section class="section wrap" style="border-top:none;padding-top:26px">
    <div class="edu-stack">
      <article class="edu-card reveal">
        <div class="edu-mark"><span class="mono-mark">P</span><span class="mname">Purdue University</span></div>
        <div class="edu-body">
          <p class="meta">April 2023 · West Lafayette, Indiana</p>
          <h3 class="deg">Doctor of Philosophy (Ph.D.)</h3>
          <p class="inst">Purdue University — Lyles School of Civil &amp; Construction Engineering</p>
          <p>Civil Engineering, Transportation &amp; Infrastructure Systems. Dissertation: <i>Integrating Connected Vehicle Data for Operational Decision Making</i> (advisor: Prof. Darcy M. Bullock; committee: Profs. Samuel Labi, Konstantina Gkritza, James Krogmeier). Supported by the Christopher B. &amp; Susan S. Burke Graduate Research Assistantship.</p>
        </div>
      </article>
      <article class="edu-card reveal">
        <div class="edu-mark"><span class="mono-mark">IIT</span><span class="mname">IIT Madras</span></div>
        <div class="edu-body">
          <p class="meta">May 2018 · Chennai, India</p>
          <h3 class="deg">Master of Technology (M.Tech.)</h3>
          <p class="inst">Indian Institute of Technology Madras — Department of Civil Engineering</p>
          <p>Transportation Engineering. Thesis: <i>Reliable Corridor Level Travel Time Estimation Using Probe Vehicle Data</i> (advisor: Prof. Lelitha Devi Vanajakshi). Awarded for exemplary, all-round best performance in the dual-degree program.</p>
        </div>
      </article>
      <article class="edu-card reveal">
        <div class="edu-mark"><span class="mono-mark">IIT</span><span class="mname">IIT Madras</span></div>
        <div class="edu-body">
          <p class="meta">May 2017 · Chennai, India</p>
          <h3 class="deg">Bachelor of Technology (B.Tech.)</h3>
          <p class="inst">Indian Institute of Technology Madras — Department of Civil Engineering</p>
          <p>Civil Engineering with a minor in Management Studies. Entered through the IIT Joint Entrance Exam ranked in the top 0.2 percentile of 1.45 million candidates.</p>
        </div>
      </article>
    </div>
    <p class="edu-note"><b>A note on logos:</b> university names and logos are registered trademarks of Purdue University and IIT Madras. This site uses typographic marks instead of official logos, which require permission under each institution's brand-use guidelines (Purdue Marketing &amp; Communications; IIT Madras administration). If permission is obtained, the official marks can be dropped into the spaces above with the attribution "Purdue University name and logo are trademarks of Purdue University, used with permission" (and equivalent for IIT Madras).</p>
  </section>
""" + foot()

# ---------------- TEACHING ----------------
P["teaching.html"] = head("Teaching | Rahul Sakhare, Ph.D., P.E.",
 "Teaching and mentoring — SPARC mobility course, IIT Madras TA, research mentoring at Purdue JTRP.") + nav("teaching.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">Teaching &amp; mentoring</span>
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

# ---------------- NEWS & MEDIA ----------------
P["news.html"] = head("News & Media | Rahul Sakhare, Ph.D., P.E.",
 "Press coverage from The New York Times, FHWA, Google Cloud, Route Fifty, and more.") + nav("news.html") + """
  <section class="page-hero wrap">
    <span class="eyebrow">News &amp; media</span>
    <h1>In the press.</h1>
    <p>Coverage of the connected-vehicle research — from the front page of <i>The New York Times</i> to FHWA's Innovator, Google Cloud, and international outlets. Headlines link to the original stories.</p>
  </section>
  <div class="wrap"><div class="filters" id="media-filters"></div></div>
  <section class="section wrap" style="border-top:none;padding-top:24px">
    <div id="media-root"></div>
  </section>
""" + foot("Media inquiries: rsakhare@purdue.edu",
           '<script src="media-data.js"></script>\n')

# ---------------- CONTACT ----------------
P["contact.html"] = head("Contact | Rahul Sakhare, Ph.D., P.E.",
 "Contact Rahul Sakhare — email, Google Scholar, LinkedIn, ORCID, ResearchGate.") + nav("contact.html") + """
  <section class="contact wrap">
    <span class="eyebrow">Contact</span>
    <h2>Let's connect.</h2>
    <p>Open to faculty positions, research collaborations, and conversations about connected-vehicle data and transportation safety.</p>
    <div class="links">
      <a href="mailto:rsakhare@purdue.edu">✉ rsakhare@purdue.edu</a>
      <a href="https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
      <a href="https://www.linkedin.com/in/rahulsakhare/" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://orcid.org/0000-0001-7843-5707" target="_blank" rel="noopener">ORCID</a>
      <a href="https://www.researchgate.net/profile/Rahul-Suryakant-Sakhare" target="_blank" rel="noopener">ResearchGate</a>
    </div>
    <div style="margin-top:56px" class="about-card">
      <h3>Office</h3>
      <div class="row"><b>Address</b><span>Hall of Discovery &amp; Learning Research, Room 204F<br>207 S. Martin Jischke Drive, West Lafayette, IN 47906</span></div>
      <div class="row"><b>Phone</b><span>(404) 304-1885</span></div>
    </div>
  </section>
""" + foot()

for name, html in P.items():
    open(name, "w", encoding="utf-8").write(html)
    print("wrote", name, len(html), "bytes")
