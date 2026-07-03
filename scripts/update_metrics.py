#!/usr/bin/env python3
"""
Refresh the holistic "Downloads & views" metric shown on the site.

Reads scripts/sources.json (one entry per paper: a metrics URL from PlumX,
MDPI, SCIRP, Springer, or Purdue e-Pubs), opens each in a headless browser,
extracts the rendered downloads/views/reads count, and rewrites metrics.json.

Robustness rules:
- If a page fails or no number is found, the last-known count for that paper
  (from the current metrics.json, or the seed from the CV spreadsheet) is kept,
  so the total never drops because of a scrape hiccup.
- Runs weekly via .github/workflows/update-metrics.yml, or locally:
    pip install playwright && python -m playwright install chromium
    python scripts/update_metrics.py
"""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = json.loads((ROOT / "scripts" / "sources.json").read_text(encoding="utf-8"))
OUT = ROOT / "metrics.json"

def previous_items():
    try:
        return json.loads(OUT.read_text(encoding="utf-8")).get("items", {})
    except Exception:
        return {}

PATTERNS = [
    # bepress / Purdue e-Pubs: "DOWNLOADS\n1,234"
    re.compile(r"DOWNLOADS\s*[\r\n]+\s*([\d,]+)", re.I),
    re.compile(r"([\d,]+)\s*[\r\n]+\s*Since\s+\w+\s+\d", re.I),
    # MDPI article metrics: "Article Views 12,345" / "Full-Text Views"
    re.compile(r"(?:Article|Full[- ]Text)\s+Views?\s*[:\r\n]+\s*([\d,]+)", re.I),
    re.compile(r"Viewed\s+by\s+([\d,]+)", re.I),
    # SCIRP: "Downloads: 1,234  Views: 5,678" -> sum handled below via findall
    # Springer: "Accesses 12k" or "12,345 Accesses"
    re.compile(r"([\d,]+)\s+Accesses", re.I),
    re.compile(r"Accesses\s*[\r\n]+\s*([\d.,]+)k?", re.I),
    # PlumX: "Views: 1,234"
    re.compile(r"Views?:?\s*[\r\n ]+([\d,]+)", re.I),
]
SCIRP = re.compile(r"Downloads:?\s*([\d,]+)[\s\S]{0,80}?Views:?\s*([\d,]+)", re.I)

def to_int(s):
    s = s.replace(",", "").strip()
    if s.endswith("k"):
        return int(float(s[:-1]) * 1000)
    try: return int(float(s))
    except ValueError: return None

def extract_count(text):
    m = SCIRP.search(text)
    if m:
        a, b = to_int(m.group(1)), to_int(m.group(2))
        if a is not None and b is not None:
            return a + b
    for rx in PATTERNS:
        m = rx.search(text)
        if m:
            n = to_int(m.group(1))
            if n is not None and n > 0:
                return n
    return None

def main():
    from playwright.sync_api import sync_playwright
    prev = previous_items()
    items, fresh = {}, 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent="Mozilla/5.0 (metrics-bot)")
        for s in SOURCES:
            url = s["url"]; seed = s.get("seed")
            fallback = prev.get(url, seed)
            try:
                page.goto(url, wait_until="networkidle", timeout=45000)
                page.wait_for_timeout(1800)
                n = extract_count(page.inner_text("body"))
                if n is not None and (fallback is None or n >= 0.5 * fallback):
                    items[url] = n; fresh += 1
                    print(f"[ok]   {n:>7}  {url[:90]}")
                elif fallback is not None:
                    items[url] = fallback
                    print(f"[keep] {fallback:>7}  {url[:90]}")
                else:
                    print(f"[skip] no count  {url[:90]}")
            except Exception as e:
                if fallback is not None:
                    items[url] = fallback
                    print(f"[keep] {fallback:>7}  (error) {url[:80]}")
                else:
                    print(f"[err]  {url[:80]} -> {type(e).__name__}")
        browser.close()

    total = sum(items.values())
    if total <= 0:
        print("Nothing collected; leaving metrics.json unchanged.")
        return 1
    metrics = {
        "total_downloads": total,
        "item_count": len(SOURCES),
        "counted_items": len(items),
        "fresh_scrapes": fresh,
        "updated": datetime.date.today().isoformat(),
        "source": "Publisher metrics (PlumX, MDPI, SCIRP, Springer, Purdue e-Pubs)",
        "items": items,
    }
    OUT.write_text(json.dumps(metrics, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote metrics.json: total={total:,} ({fresh} fresh, {len(items)-fresh} kept)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
