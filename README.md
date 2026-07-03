# Rahul Sakhare — Academic Website

A light-themed, tab-based faculty site (Home/About, Research, Publications, Teaching, News, CV, Contact).

## Files
- `index.html` — home (about, research, experience, teaching, news preview, contact)
- `publications.html` — full, filterable publication list (reads `pubs-data.js`)
- `news.html` — media coverage
- `styles.css`, `script.js` — shared styling and behavior
- `pubs-data.js` — your publications as data (edit here to add papers)
- `assets/Sakhare_CV.pdf` — the CV linked from the "CV" tab

## Publish free on GitHub Pages
1. Create a repository. For a personal site, name it `<username>.github.io`.
2. Upload all of these files to the repository **root** (keep the `assets/` folder).
3. In the repo: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save**.
4. Your site goes live at `https://<username>.github.io/` within a minute or two.

## Updating
- **Add a publication:** add an object to `pubs-data.js`:
  `{"type":"journal","year":2026,"cite":"Authors (2026). Title. Venue, vol(iss), pp.","url":"https://doi.org/...","note":null}`
  (types: `journal`, `report`, `conference`, `technical`, `book`, `thesis`). Your name is auto-bolded.
- **Replace the CV:** overwrite `assets/Sakhare_CV.pdf` (keep the filename).
- **Edit stats/bio:** in `index.html` (the readout numbers and About text).

Fonts load from Google Fonts; no build step or dependencies required.

---

## Photos
Headshots live in `assets/img/`:
- `hero_cutout.webp` — background-removed studio headshot used in the hero (blends onto the page).
- `about_photo.jpg` — Purdue-branded photo in the About section.
To swap either, replace the file (keep the name) or point the `<img>` in `index.html` at a new file.

## Auto-updating "Report downloads" stat
The hero shows a **Report downloads** number tallied from your Purdue e-Pubs pages. It refreshes itself weekly:

- `metrics.json` — the number the site displays (seeded from your CV: 5,588).
- `scripts/sources.json` — the list of e-Pubs URLs to tally (generated from your reports).
- `scripts/update_metrics.py` — opens each page in a headless browser, reads the rendered download count, sums them, and rewrites `metrics.json`.
- `.github/workflows/update-metrics.yml` — a GitHub Action that runs the script **every Monday** (and on demand) and commits the updated `metrics.json`.

### One-time setup on GitHub
1. Push all files (including the hidden `.github/` folder) to your repo.
2. **Settings → Actions → General → Workflow permissions → “Read and write permissions” → Save** (lets the Action commit the refreshed number).
3. Go to the **Actions** tab → “Update download metrics” → **Run workflow** once to populate live totals immediately. After that it runs weekly on its own.

Notes: GitHub Actions is free for public repositories. The script tallies Purdue e-Pubs (report) downloads; journal-article views on MDPI/IEEE aren't included because those publishers report them inconsistently. To add/remove sources, edit `scripts/sources.json`.
