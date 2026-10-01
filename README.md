# Chef Anto Brand Kit 🎨

**The single source of truth for how Chef Anto looks and sounds: voice, taglines, colors, fonts, handles and platform rules. Every Chef Anto agent checks its work against it.**
Built by Chef Anto (Antoanela Alexander), Miami. *I am the heart. AI is the brain.*

## At a glance
| | |
|---|---|
| Taglines | "Born in Romania. Rebuilt in Miami." · "With What We Have" |
| Mission | Save one billion meals from food waste |
| Sign-off | Chef Anto 🌿🤓❤️ |
| Voice | A grandmother's Balkan kitchen meets modern tech: warm, personal, cozy, never over the top |
| Never | "revolutionary", "game-changer", "hurry", "deal", fake reviews, invented press |

| Color | Hex | Use |
|---|---|---|
| Warm cream | `#F6EFE4` | Background |
| Deep olive | `#3F4A2E` | Primary |
| Paprika | `#B5482A` | CTAs and highlights only |
| Ink | `#1F1B16` | Text |
| Linen | `#E7DCCB` | Soft neutral |

Fonts: Fraunces or Cormorant Garamond for headings, Inter or system sans for body.

## Files
| Path | What it is |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | Brand Kit Guardian instructions (Claude skill) |
| [`brand-sheet.html`](brand-sheet.html) | One-page visual brand sheet with swatches (open in a browser) |
| [`tests/check_contrast.py`](tests/check_contrast.py) | WCAG contrast check for every palette pair |
| [`tests/test_brand_sheet.py`](tests/test_brand_sheet.py) | Renders the brand sheet at 3 widths |

## How to use
- **As a skill:** zip the `skill` folder renamed to `chef-anto-brand-kit`, upload it in Claude's Settings → Skills. Ask "Check this post against the Chef Anto brand kit" or "Give me the brand kit".
- **As a reference:** open `brand-sheet.html` and share it with designers and collaborators.

## Test results (only tests actually run, 2026-10-01)
| # | Test | Result |
|---|---|---|
| 1 | `python3 tests/check_contrast.py` (self-tests against known WCAG values first) | ⚠️ **8/9 pairs pass AA** for normal text |
| 2 | `python3 tests/test_brand_sheet.py` (Playwright, 375/768/1440 px) | ✅ **6/6 passed**: no horizontal scroll, all 5 swatches render |

**Contrast results:**
| Text on background | Ratio | AA normal text | AA large text |
|---|---|---|---|
| Ink on Warm cream | 14.99:1 | ✅ | ✅ |
| Deep olive on Warm cream | 8.24:1 | ✅ | ✅ |
| Warm cream on Deep olive | 8.24:1 | ✅ | ✅ |
| White on Paprika (buttons) | 5.35:1 | ✅ | ✅ |
| Warm cream on Paprika | 4.68:1 | ✅ | ✅ |
| Paprika on Warm cream | 4.68:1 | ✅ | ✅ |
| Ink on Linen | 12.63:1 | ✅ | ✅ |
| Deep olive on Linen | 6.95:1 | ✅ | ✅ |
| **Paprika on Linen** | **3.95:1** | ❌ | ✅ |

**New rule from this test:** don't use small paprika text on linen. Use it only for headings 24 px and up, or put the paprika on cream instead.

**Not tested yet:** the palette is still marked "confirm with Chef Anto before first use"; logo rules are not in this repo yet.

## Run the tests
```bash
python3 tests/check_contrast.py
pip install playwright && playwright install chromium && python3 tests/test_brand_sheet.py
```

---
Chef Anto 🌿🤓❤️
