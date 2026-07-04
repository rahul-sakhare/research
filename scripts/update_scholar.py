#!/usr/bin/env python3
"""
Refresh Google Scholar stats (citations, h-index, i10-index) into scholar.json.

Tries a plain HTTP fetch first, then a headless browser. If both fail (Scholar
sometimes rate-limits bots), the last-known values are kept unchanged.
"""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "scholar.json"
PROFILE = "https://scholar.google.com/citations?user=4crwCDoAAAAJ&hl=en"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"

def parse_stats(html):
    # Scholar's stats table: six gsc_rsb_std cells => all/since-year pairs of
    # citations, h-index, i10-index. We take the "All" column (0, 2, 4).
    vals = re.findall(r'class="gsc_rsb_std">(\d+)<', html)
    if len(vals) >= 6:
        return {"citations": int(vals[0]), "h_index": int(vals[2]), "i10_index": int(vals[4])}
    return None

def via_requests():
    import urllib.request
    req = urllib.request.Request(PROFILE, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return parse_stats(r.read().decode("utf-8", "ignore"))

def via_playwright():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(user_agent=UA)
        page.goto(PROFILE, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(1500)
        stats = parse_stats(page.content())
        b.close()
        return stats

def main():
    stats = None
    for fn in (via_requests, via_playwright):
        try:
            stats = fn()
            if stats: break
        except Exception as e:
            print(f"[warn] {fn.__name__}: {type(e).__name__}")
    if not stats:
        print("Scholar unreachable; keeping last-known scholar.json.")
        return 0
    stats["updated"] = datetime.date.today().isoformat()
    stats["source"] = "Google Scholar profile 4crwCDoAAAAJ"
    OUT.write_text(json.dumps(stats, indent=1) + "\n", encoding="utf-8")
    print(f"Wrote scholar.json: {stats['citations']} citations, h={stats['h_index']}, i10={stats['i10_index']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
