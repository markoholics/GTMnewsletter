# 04 Image manifest

**DRAFT: pending Remmy review**

All images were built by `tools/newsletter-design/build.py` from `issue.json`, in black, white and grey only (see `DESIGN.md`). Sources are in `design-bw/images/src/`. No scraped images, stock photography, faces or third party logos. Every PNG was viewed after rendering; the renderer printed no overflow warnings.

| File | Size | Placement | Alt text (under 125 characters) | Suggested caption |
|---|---|---|---|---|
| `cover.png` | 1280 x 720 | IMAGE 1: LinkedIn article cover, top of the issue | Cover: Every buying signal has a clock. Most teams never read it, black type on white with a window bar | None needed on a cover. |
| `insight-card.png` | 1200 x 628 | IMAGE 2: after the first paragraph of "A cancellation that was public by the next morning" | Large 33 days: the time a trucking company has to fix a cancelled insurance policy, per Cannonball GTM | Reported figure, via Cannonball GTM (Doug Bell). Single source, not audited. |
| `quote-card.png` | 1200 x 628 | IMAGE 3: after the blockquote in the same section | Quote card: Public. Dated. Deadly., attributed to Doug Bell of Cannonball GTM | Doug Bell, Cannonball GTM. |
| `framework.png` | 1200 x 628 | IMAGE 4: in "Four questions for every signal", after the Owner paragraph | Four boxes in order: Threshold, Window, Reflex and Owner, each with the question to ask | Four questions for every buying signal. |

News style covers (not placed in the article): `news-cover.png` (main headline: "Every buying signal has a clock: read it before you buy more"), `news-cover-alt1.png` ("Window minus reply time: the sum most signal lists fail") and `news-cover-alt2.png` ("Time your front door before you buy another signal"), all 1280 x 720. Also `newsletter-cover.jpg` (2560 x 1440), the newsletter's own cover, in `design-bw/images/`.

The review page is `design-bw/newsletter-bw.html`.
