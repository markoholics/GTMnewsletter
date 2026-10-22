# 04 Image manifest

**DRAFT: pending Remmy review**

All images were built from HTML in `images/src/` using the brand colours (navy #1F4E79, near black #1A1A1A, warm grey #555555, off white #F7F5F0), rendered to PNG with Playwright, and checked visually for clipping and contrast. No scraped images, stock photography, faces or third party logos.

| File | Size | Placement | Alt text (under 125 characters) | Suggested caption |
|---|---|---|---|---|
| `cover.png` | 1280 x 720 | LinkedIn article cover image (top of the issue) | Cover: Your GTM stack needs a column called how do we know, in white serif type on navy | None needed on a cover. |
| `insight-card.png` | 1200 x 628 | Immediately after the opening, before "A guess dressed as a record" | Large navy 51%: of cold email replies in a 6.07 million message dataset were auto-replies | Half the "replies" were out-of-office messages. Source: Grow Surely, via The GTM Engineer Pulse. |
| `framework.png` | 1200 x 628 | In "Observed, Inferred, Empty", after the Empty paragraph | Three columns, Observed, Inferred and Empty, showing what an agent may and may not do with each | The permission rule: the label decides what an agent may do. |
| `quote-card.png` (optional) | 1200 x 628 | Optional: after the Le Meur paragraph, or reuse as a standalone LinkedIn post | Quote card: An EMPTY is more useful to me than a good guess, attributed to Thibault Le Meur of Triscale | Thibault Le Meur, Triscale, writing in MRR Unlocked. |

Notes
- The quote card is not marked in `02-article.md`; add `[IMAGE 4: quote-card.png, ...]` after the Le Meur paragraph if you want it inline.
- The serif headline font is Georgia in the CSS, but Georgia is not installed in this container, so the PNGs rendered in DejaVu Serif (a wider, heavier face). Re-render on a machine with Georgia if you want the exact brand look: edit nothing, just run the same Playwright script against `images/src/*.html`.
- Source credit on the insight card names the secondary source. See review notes: the 51% figure is single source.
