# 04 Image manifest

**DRAFT: pending Remmy review**

Built by `tools/newsletter-design/build.py` from `issue.json`, black, white and grey only (see `DESIGN.md`). Sources are in `design-bw/images/src/`. No scraped images, stock photography, faces or third party logos. Every PNG was viewed after rendering; the renderer printed no overflow warnings. No `news_cover` block and no BREAKING or front page covers were made, as requested.

| File | Size | Placement | Alt text (under 125 characters) | Suggested caption |
|---|---|---|---|---|
| `header-cover.png` (and `header-cover-2x.png`, 2560 x 1440) | 1280 x 720 | IMAGE 1: LinkedIn article cover. Shows only PREVIOUSLY IN GTM, Mohammad H. Rahman, 12 Nov 2026 and the title | Cover: Stop debating build versus buy. Ask it job by job instead, black type on white with a window bar | None needed on a cover. |
| `insight-card.png` | 1200 x 628 | IMAGE 2: after the ZoomInfo versus Clay contract paragraph | Large stat: Claude named by 110 respondents as the most impactful GTM tool, more than 3x the next vendor, per Growth Unhinged | Growth Unhinged, 2026 State of B2B GTM report, 300 respondents. Self-reported, not audited. |
| `quote-card.png` | 1200 x 628 | IMAGE 3: after the four renewal questions, before the lead routing paragraph | Quote card: The vendors sell the stopwatch, not the time, attributed to Marty Berman, GTM Tool Time | Marty Berman, GTM Tool Time, "Lead Routing, Reviewed." |
| `framework.png` | 1200 x 628 | IMAGE 4: after the lead routing paragraph, closing the renewal-test section | Four boxes in order: Job, Checkable, Compounding and Headcount, each with the question to ask | Four questions before a tool earns a seat. |

Spare, not placed: `cover.png` (1280 x 720, title and standfirst card) and `newsletter-cover.jpg` (2560 x 1440). The review page is `design-bw/newsletter-bw.html`.
