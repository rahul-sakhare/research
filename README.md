# Rahul Sakhare — Academic Website

Editorial, multi-page faculty site. Every tab is its own page:
`index.html` (landing) · `about.html` · `research.html` · `publications.html` · `education.html` · `teaching.html` · `news.html` · `contact.html`

## Data files (edit these, not the HTML)
- `pubs-data.js` — all 91 publications. Add new entries as
  `{"type":"journal","year":2026,"cite":"…","url":"https://doi.org/…","note":null}`
  (types: journal, report, conference, technical, book, thesis). Your name is auto-bolded; every entry becomes a clickable card.
- `media-data.js` — press/media mentions (outlet, title, date, url, kind, optional note; `marquee:true` features it in the dark band on News & Media).
- `metrics.json` — the holistic **Downloads & views** figure on the home page (currently **37,532**, seeded from Publications.xlsx). Auto-refreshed weekly.
- `scripts/sources.json` — the 45 per-paper metric links (PlumX/MDPI/SCIRP/Springer/e-Pubs) the scraper visits.

## Rebuilding pages
Shared nav/head/footer live in `build_pages.py`. To change them once for all pages:
`python3 build_pages.py` regenerates every HTML file.

## Auto-updating Downloads & views
- `scripts/update_metrics.py` opens each source link in a headless browser, reads the rendered count, and rewrites `metrics.json`. If a page fails, the last-known count is kept, so the total never drops on a bad scrape.
- `.github/workflows/update-metrics.yml` runs it every Monday (and on demand: Actions → Update download metrics → Run workflow).
- One-time: Settings → Actions → General → Workflow permissions → **Read and write permissions**.
- Honest caveat: publisher pages change markup; expect the Action to keep most counts fresh and fall back to last-known for the rest. The 37,532 seed is accurate as of Jul 2026.

## Deployment (GitHub Pages)
Included `.nojekyll` + `.github/workflows/deploy-pages.yml`.
Settings → Pages → Source → **GitHub Actions** (recommended), or Deploy from a branch (the `.nojekyll` handles it).
If your default branch is `master`, edit the `branches:` line in both workflow files.

## Photos
`assets/img/about_photo.jpg` — the About portrait (subtle scroll parallax). Replace the file to swap it.

## University logos
`education.html` intentionally uses typographic marks — Purdue and IIT Madras names/logos are registered trademarks and official marks require brand-guideline permission. The page includes the attribution language to use if permission is granted.


---

## What updates automatically (daily)
`.github/workflows/update-stats.yml` runs **every day** and commits:
- `scholar.json` — citations, h-index, i10-index pulled from the Google Scholar profile (`scripts/update_scholar.py`). If Scholar rate-limits the bot, last-known values are kept.
- `metrics.json` — the "> Downloads & views" total and its as-of date (`scripts/update_metrics.py`).
The **Journal articles** and **Technical reports** numbers on the home page are counted live from `pubs-data.js` in the browser — update that file (e.g., from a new CV) and the stats follow automatically.

## Feedback form (Contact page)
Uses FormSubmit.co to deliver messages to rsakhare@purdue.edu with no backend. **First submission:** FormSubmit emails you an activation link — click it once and the form is live from then on. A honeypot field is included for spam; you can also manage settings at formsubmit.co.

## New pages in this version
- `awards.html` — six highlight honors plus a full timeline.
- `gallery.html` — placeholder grid; when photos are ready, replace the "Coming soon" tiles with `<img>` tags (or send them to me and I'll lay out a proper gallery).


## Download & view counts — how the number is built
The home-page "> Downloads & views" figure is the sum of:
- **Reports (23):** all-time downloads read from each report's **public Purdue e-Pubs page** (the 10.5703 DOI resolves there). All 22 technical reports + the TPF-5(514) monograph are now included in `scripts/sources.json` (8 reports that were previously missing have been added).
- **Journals (30):** views/downloads from each publisher's metric page (MDPI, SCIRP, IEEE, Springer, PlumX).

**Excluded by design:** the `jtrpafteractions` district speed-profile *snapshot* series (IDs like `202502-07`). Each snapshot lists its own ~100 downloads; counting them individually would multiply the total for what is really one running series. The exclusion is enforced in `scripts/update_metrics.py` (the `EXCLUDE` pattern) and in how `sources.json` is built.

**Why the private dashboard link isn't used:** the `dashboard.digital-commons.com/?...&.authT=...` URL is your personal, logged-in Digital Commons page. It carries a session auth token that expires and requires your live login, so an unattended weekly job can't read it (and a token shouldn't be committed to a repo). The public e-Pubs report pages give the same all-time download numbers in a way that *can* be automated.

If you want an immediate exact figure before the first Action run, open your dashboard, note the grand total **minus** the `202502-07`-style snapshots, and I can hard-seed that into `metrics.json`.
