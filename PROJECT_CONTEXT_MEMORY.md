# Rahul Sakhare, Ph.D., P.E. — Academic Website Project Context & Memory

> **Purpose:** This persistent memory file preserves the complete design context, codebase architecture, configuration history, and state for [rahul-sakhare.github.io/research](https://rahul-sakhare.github.io/research/). Any new or existing agent session can read this single file to immediately resume work with zero context loss.

---

## 1. Project Overview & Location
- **Active Directory:** `E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research\`
- **GitHub Repository:** `https://github.com/rahul-sakhare/research.git` (branch: `main`)
- **Live URL:** `https://rahul-sakhare.github.io/research/`
- **Owner / Identity:** Rahul Suryakant Sakhare, Ph.D., P.E.
  - Transportation Research Engineer at Purdue University (Joint Transportation Research Program / Lyles School of Civil Engineering)
  - Licensed Professional Engineer (P.E.), State of Indiana (PE12600619)
  - Research Focus: Connected vehicle trajectory data, work zone safety, telematics, cloud analytics, traffic operations

---

## 2. Core Architecture & Build System
The site uses a custom Python-based static site generator:
- **Primary Generator Script:** `build_pages.py`
  - Defines the global layout: `head()`, `nav()`, `foot()`.
  - Generates all 10 site pages:
    1. `index.html` (Home — Authentic Academic Minimalist layout, photo, scholar stats, selected publications)
    2. `about.html` (About — Bio, cricket hobby narrative, career appointments table)
    3. `publications.html` (Publications — 92 peer-reviewed items, interactive search, category filters, BibTeX modal)
    4. `projects.html` (Sponsored Projects — 22 grants, role tags, agency filters, funding/links)
    5. `education.html` (Education — Purdue Ph.D., IIT Madras B.Tech/M.Tech, P.E. Licensure)
    6. `teaching.html` (Teaching — Philosophy, guest lectures, mentee roster)
    7. `awards.html` (Honors & Awards — PRIME grant, Cox scholarship, ITS Project of Year)
    8. `news.html` (News & Media — NYT, Google Cloud Innovator, USDOT V2X feature)
    9. `gallery.html` (Visual Chronicle — Curated 4-5 annual photo highlights, timeline filters, "+ Discover More" accordion, full lightbox)
    10. `contact.html` (Contact — Newton quote, Purdue DLR coordinates, FormSubmit portal with redirect)
- **Styling:** `styles.css` (Lora editorial serif headings + Inter sans body, dark/light theme toggle, lightbox & gallery cards).
- **Client Script:** `script.js` (handles live publication search, filtering, gallery timeline & lightbox).
- **Data Stores:**
  - `pubs-data.js` (92 publications data array)
  - `media-data.js` (news/press clippings)
  - `gallery-data.js` (photo library with year, event, category, location, people, and highlight flags)
  - `scholar.json` (citation counts, h-index 14, i10-index 19)

---

## 3. SEO & Analytics Configuration
- **Google Search Console Verification:**
  - File: `google368a88109246cfe6.html` (verified at site root)
  - Meta tag in `<head>`: `<meta name="google-site-verification" content="google368a88109246cfe6">`
- **Sitemap & Robots:**
  - `sitemap.xml` (all 9 pages with priority weights)
  - `robots.txt` (pointing to sitemap)
- **Structured Data:**
  - Schema.org JSON-LD `Person` & `WebSite` graph embedded in `<head>`.
- **Google Analytics 4 (GA4):**
  - **Measurement ID:** `G-JX6RBVBKF6`
  - Embedded in `head()` inside `build_pages.py`:
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-JX6RBVBKF6"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-JX6RBVBKF6');
    </script>
    ```

---

## 4. Key Content & Specific Customizations Made
1. **About Page Heading:** Changed from `About Rahul Sakhare, Ph.D., P.E.` to **`About Rahul,`**.
2. **First Author Border:** Publications where Rahul is first author feature a subtle `3px solid var(--accent-gold)` left border.
3. **Cricket Hobby:** Added 3-sentence narrative in `about.html` right above Career Appointments celebrating captaining the Purdue Cricket team to the 2022 Midwest championship.
4. **Career Appointments:** Clean two-column flex layout with institution name on left and location (`West Lafayette, IN`) on right without parentheses or awkward dots.
5. **Contact Form:** FormSubmit action with `<input type="hidden" name="_next" value="https://rahul-sakhare.github.io/research/contact.html">` to prevent 404 redirects.
6. **CCAT Project:** Linked to official CCAT UMTRI page.
7. **Research Phrasing:** Changed `capital prioritization` / `capital program prioritization` to `capital project prioritization` and removed the serial comma before `and` in the research overview narrative on both Home and About pages.
8. **Teaching & Mentorship Roster:** Updated section title to `Graduate & Undergraduate Researchers Co-Advised / Mentored / Collaborated` and expanded the researcher roster to 16 researchers with INDOT SPR project numbers and publications.
9. **Visual Chronicle (`gallery.html`):** Built dedicated conference, podium, lecture, and field photo chronicle with timeline year pills, category format filtering, curated 4-5 highlights per year with "+ Discover More" accordion, full interactive Lightbox modal (keyboard arrow support), and data-driven store in `gallery-data.js`.

---

## 5. Deployment / Execution
- Script: `E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research\push_updates.bat`
  ```bat
  cd /d "E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research"
  python build_pages.py
  git add .
  git commit -m "..."
  git push origin main
  ```

