#!/usr/bin/env python3
"""
Update download metrics for the website.

Visits each Purdue e-Pubs source (listed in scripts/sources.json), reads the
JavaScript-rendered "DOWNLOADS" count, sums them, and writes metrics.json.

Runs weekly via .github/workflows/update-metrics.yml (or locally:
    pip install playwright && python -m playwright install chromium
    python scripts/update_metrics.py
).
"""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = json.loads((ROOT / "scripts" / "sources.json").read_text(encoding="utf-8"))
OUT = ROOT / "metrics.json"

COUNT_RE = re.compile(r"DOWNLOADS\s*[\r\n]+\s*([\d,]+)", re.I)
COUNT_RE2 = re.compile(r"([\d,]+)\s*[\r\n]+\s*Since\s+\w+\s+\d", re.I)

def extract_count(text: str):
    for rx in (COUNT_RE, COUNT_RE2):
        m = rx.search(text)
        if m:
            try:
                return int(m.group(1).replace(",", ""))
            except ValueError:
                pass
    return None

def main():
    from playwright.sync_api import sync_playwright
    items, total, ok = {}, 0, 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent="Mozilla/5.0 (metrics-bot; +https://github.com)")
        for s in SOURCES:
            url = s["url"]
            try:
                page.goto(url, wait_until="networkidle", timeout=45000)
                page.wait_for_timeout(1500)  # let the download widget populate
                text = page.inner_text("body")
                n = extract_count(text)
                if n is not None:
                    items[url] = n
                    total += n
                    ok += 1
                    print(f"[ok]  {n:>6}  {url}")
                else:
                    print(f"[skip] no count  {url}")
            except Exception as e:
                print(f"[err] {url} -> {e}")
        browser.close()

    if ok == 0:
        print("No counts collected; leaving metrics.json unchanged.")
        return 1

    metrics = {
        "total_downloads": total,
        "item_count": len(SOURCES),
        "counted_items": ok,
        "updated": datetime.date.today().isoformat(),
        "source": "Purdue e-Pubs",
        "items": items,
    }
    OUT.write_text(json.dumps(metrics, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT.name}: total={total:,} from {ok}/{len(SOURCES)} items")
    return 0

if __name__ == "__main__":
    sys.exit(main())
