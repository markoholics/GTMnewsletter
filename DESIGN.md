# PREVIOUSLY IN GTM: design guide

Set by Mohammad on 23 October 2026. It replaces the earlier navy and off-white brand colours. The reference issue is `newsletter-drafts/2026-10-23/`, and its `design-bw/` folder shows the finished design.

## Newsletter identity
- Name: **PREVIOUSLY IN GTM** (always capitals).
- Tagline: A weekly read for founders, GTM leaders and growth marketers.
- Byline: Mohammad H. Rahman. No job title, company or designation.
- The cover image of the newsletter itself is `design-bw/images/newsletter-cover.jpg` (2560 x 1440 JPEG).

## Colours: black, white and grey only
| Token | Hex | Use |
|---|---|---|
| Black | #0A0A0A | text, borders, header bars, shadow |
| White | #FFFFFF | page and card background |
| Grey 1 | #F2F2F2 | window bars, alternate card bodies |
| Grey 2 | #D4D4D4 | hairlines |
| Grey 3 | #8C8C8C | quiet labels |
| Grey 4 | #555555 | secondary text |

No colour anywhere: no accents, no tinted greys, no photography. The web page also has a dark theme made from the same greys.

## Type
- Headlines and body: Inter. Headlines weight 800, tight tracking (about -0.03em). Body 18px, line height 1.7.
- Labels: a monospace face (JetBrains Mono, falling back to DejaVu Sans Mono), uppercase, letter spaced.

## Visual language (taken from the reference video)
- **Window chrome:** a bar with three outline dots and a mono label, a 2 to 3px black border and a hard offset black shadow (masthead and cover only).
- **Header bars:** every figure has a black bar with a mono label.
- **Pull quotes:** a thick left bar (6px) and larger semibold text.
- **Diagrams:** boxed nodes, black header bars, dashed grey boxes for weak or uncertain steps, one solid black node for the point.
- **Cards:** 1200 x 628, flat, no gradients.

## Per issue image set (built by the script)
`cover.png` 1280x720 (title and byline only), `insight-card.png` (one stat and its source), `quote-card.png` (one attributed line under 15 words), `framework.png` (the model the issue proposes, 3 to 5 boxes), optional `before-after.png` (a teaching illustration, always labelled "Illustration"). Alt text under 125 characters.

## How to build an issue
1. Write the article files as before (`01` to `05`). Use the image markers `[IMAGE n: filename, alt text]` so `03-article-linkedin.html` carries the placeholders.
2. Copy `tools/newsletter-design/issue.example.json` to `newsletter-drafts/YYYY-MM-DD/issue.json` and fill it in with that issue's title, stat, quote, framework and alt text. Everything in it must be as verified as the article.
3. Run `python3 tools/newsletter-design/build.py newsletter-drafts/YYYY-MM-DD/issue.json`.
   It writes `design-bw/` with the PNGs, their HTML sources and `newsletter-bw.html` (images embedded). It needs Playwright with Chromium at `/opt/pw-browsers/chromium`; `NODE_PATH` defaults to `/opt/node22/lib/node_modules`.
4. Look at every PNG for clipped text. The renderer prints a WARNING if any card overflows its canvas.
5. Publish `newsletter-bw.html` as the review page. Do not add Copy buttons, a "Draft" tag or a pull request link to the public facing page. Keep "DRAFT: pending Remmy review" on the files in the repo.

## Do not
Use the old navy cover, Georgia, brand colours, stock photography, faces or logos.
