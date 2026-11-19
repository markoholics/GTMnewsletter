# 04 Image manifest

**DRAFT: pending Remmy review**

Built by `tools/newsletter-design/build.py` from `issue.json`, black, white and grey only (see `DESIGN.md`). Sources are in `design-bw/images/src/`. No scraped images, stock photography, faces or third party logos. Every PNG was viewed after rendering; the renderer printed no overflow warnings. No `news_cover` block and no BREAKING or front page covers were made, as requested.

| File | Size | Placement | Alt text (under 125 characters) | Suggested caption |
|---|---|---|---|---|
| `header-cover.png` (and `header-cover-2x.png`, 2560 x 1440) | 1280 x 720 | IMAGE 1: LinkedIn article cover. Shows only PREVIOUSLY IN GTM, Mohammad H. Rahman, 19 Nov 2026 and the title | Cover: Most AI agents can't finish what they start on your site, black type on white with a window bar | None needed on a cover. |
| `insight-card.png` | 1200 x 628 | IMAGE 2: after the paragraph on the flight-booking split | Large 2 of 24: chat only AI agents that finished a real booking task without a browser of their own, per a 20 assistant test reported by The GTM Engineering Newsletter | Reported by The GTM Engineering Newsletter, citing AI Search Leaders' test. Single source, not audited. |
| `quote-card.png` | 1200 x 628 | IMAGE 3: after the paragraph quoting Lukas Campos | Quote card: Our listing text was the whole storefront, attributed to Lukas Campos of Audioscape via The GTM Engineering Newsletter | Lukas Campos, founder of Audioscape, via The GTM Engineering Newsletter. |
| `framework.png` | 1200 x 628 | IMAGE 4: after the "what this means for your next quarter" actions | Four boxes in order: Evidence, Control, Cost and Reversal, each with the question to ask before building for an agent audience | Four questions before an agent-readiness project gets a budget line. |

Spare, not placed: `cover.png` (1280 x 720, title and standfirst card) and `newsletter-cover.jpg` (2560 x 1440). The review page is `design-bw/newsletter-bw.html`.
