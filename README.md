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
