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
