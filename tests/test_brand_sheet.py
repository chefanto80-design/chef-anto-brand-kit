"""Renders brand-sheet.html at phone, tablet and desktop widths and checks layout.

Usage: python3 tests/test_brand_sheet.py   (needs: pip install playwright)
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

page_path = pathlib.Path(__file__).resolve().parents[1] / "brand-sheet.html"
results = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (375, 768, 1440):
        pg = b.new_page(viewport={"width": w, "height": 900})
        pg.goto(page_path.as_uri())
        sw = pg.evaluate("document.documentElement.scrollWidth")
        swatches = pg.evaluate("document.querySelectorAll('.sw').length")
        results.append((f"{w}px: no horizontal scroll", sw <= w, f"scrollWidth {sw}"))
        results.append((f"{w}px: all 5 color swatches render", swatches == 5, str(swatches)))
    b.close()
for name, ok, d in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}  ({d})")
passed = sum(ok for _, ok, _ in results)
print(f"\n{passed}/{len(results)} checks passed")
sys.exit(0 if passed == len(results) else 1)
