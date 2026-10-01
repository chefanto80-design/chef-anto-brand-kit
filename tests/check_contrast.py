"""WCAG 2.1 contrast check for every text/background pair in the Chef Anto palette.

Usage: python3 tests/check_contrast.py
AA needs 4.5:1 for normal text and 3:1 for large text (24px+, or 18.66px+ bold).
"""
PALETTE = {
    "Warm cream": "#F6EFE4",
    "Deep olive": "#3F4A2E",
    "Paprika": "#B5482A",
    "Ink": "#1F1B16",
    "Linen": "#E7DCCB",
    "White": "#FFFFFF",
}
# (text, background, use)
PAIRS = [
    ("Ink", "Warm cream", "body text"),
    ("Deep olive", "Warm cream", "headings, links"),
    ("Warm cream", "Deep olive", "text on olive sections"),
    ("White", "Paprika", "CTA button label"),
    ("Warm cream", "Paprika", "CTA button label (cream)"),
    ("Paprika", "Warm cream", "paprika highlight text"),
    ("Ink", "Linen", "text on linen cards"),
    ("Deep olive", "Linen", "olive text on linen"),
    ("Paprika", "Linen", "paprika text on linen"),
]


def lum(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    hi, lo = sorted([lum(a), lum(b)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


# Self-test against known WCAG values before trusting the results.
assert round(ratio("#000000", "#FFFFFF"), 1) == 21.0
assert round(ratio("#777777", "#FFFFFF"), 2) == 4.48

print(f"{'Text on background':40} {'Ratio':>7}  Normal  Large   Use")
fails = 0
for fg, bg, use in PAIRS:
    r = ratio(PALETTE[fg], PALETTE[bg])
    normal = "PASS" if r >= 4.5 else "FAIL"
    large = "PASS" if r >= 3 else "FAIL"
    fails += normal == "FAIL"
    print(f"{fg + ' on ' + bg:40} {r:6.2f}:1  {normal:6}  {large:6}  {use}")
print(f"\n{len(PAIRS) - fails}/{len(PAIRS)} pairs pass AA for normal text")
