# 05 Review notes (v2 rerun)

**DRAFT: pending Remmy review**
Be hard on this. Cut anything weak.

## Assumptions

- **Date range.** `label:GTM-Newsletters newer_than:7d` on 28 October 2026 returned 25 threads (21 to 28 October) first time; the quoted fallback was not needed.
- **Gmail use.** Search and read only. Nothing was replied to, archived, labelled, starred, trashed or deleted. The one send is the draft email to contact@markoholics.com.
- **Rerun rules followed.** New folder `2026-10-28-v2`, new branch `claude/newsletter-2026-10-28-v2`, own draft PR. The rejected renewal memo topic, its Claim/Baseline/Slice/Schedule framework and the 22 Oct thesis are not reused. monday.com, Exa and Datarails appear again as *supporting evidence* (they are the week's strongest cases), but the thesis and sources it rests on are different. The 25 hour statistic is used once, in one paragraph; the insight card uses Cannonball's 33 days instead.
- **Emails skipped (7) and why:** earlier "DRAFT:" email to self; Mohammad's own Substack sample post and "Decide what your growth loop pays in" post; three Substack system notices; Clay "Welcome"; Apollo promotion.
- **Read in full (15):** all editorial newsletters in the label, listed in 01-signal-map.md. **Not read in full:** Lenny's "I'm not doing 996" (the email contained only a web link, no body text) and the Clay onboarding email (read, but vendor promotion, not used). The chalsarboleya post is partly paywalled and off topic; read, not used.
- **Overlap with earlier issues.** Datarails and Exa were used in the rejected 28 Oct draft; here they carry one point each.
- **Build tooling.** `main` lacks `DESIGN.md`, `CLAUDE.md` and `tools/newsletter-design/`. This branch starts from `claude/newsletter-2026-10-28` so the build could run, which means the PR against `main` also shows the earlier 22 Oct and 28 Oct files that PR carries. The v2 files are all in `newsletter-drafts/2026-10-28-v2/`. If you merge, merge the earlier PRs first or retarget this PR to `claude/newsletter-2026-10-28` for a clean diff.
- **Names inferred or not fully seen:** "The Signal" (from sender thesignalco and the URL thesignal.club; the author signs "Brendan", no surname seen); "GTMnow / The GTM Newsletter" (from the footer and sender thegtmnewsletter); "GTM Engineering newsletter" (from the domain newsletter.gtmengineering.ai); "Doug Bell" (seen in a Substack notification, and "Doug" in the post body); Maja Voje (named in the GTM Engineering weekly and signed "Maja" in GTM Strategist). Pronouns avoided for everyone named. Marcus Holm's title (CRO at Exa) and Aviv Canaani's (CRO and CMO at Datarails, written as chief revenue officer) are as shown in GTMnow.
- **Source conflicts of interest.** Alex Lindahl is Creator in Residence at Clay, a vendor in this space, and the article says so. Cannonball sells a kit; the article cites only the free post.
- **Banned words.** None in the article. The Sources section keeps source titles as published ("$1B" in the monday title, "30x" in the Datarails title); drop them if you prefer.
- **Proverb flip.** Used once ("Whoever said good things come to those who wait clearly never watched an inbound lead go cold in a queue for 25 hours.").
- **Headline ban check.** No dashes of any kind in the article body; hyphens only appear inside URLs.

## Numbers and claims: certainty

| Claim | Certainty | Note |
|---|---|---|
| Insurer cancellation posted next morning in a free public file; owner finds out ten days later; 33 days to fix | **Single source** | Cannonball GTM (Doug Bell). Regulatory details are the author's, not checked against government sources. |
| Four question bar; 12 pains tested, 7 passed | **Verified in source** | Cannonball GTM 27 Oct post. |
| Three clocks: 33 days, 45 days, 61 days | **Verified in source** | Same post. |
| "Public. Dated. Deadly." | **Verified in source** (3 words) | Cannonball GTM, one quote from that source. |
| Reply rates 0.02%, 1%, 4% or better | **Single source / methodology unseen** | Cannonball states them without showing how measured. Article says so. |
| monday.com wait about 25 hours in early 2025, under two minutes by the time Akron left | **Single source** | Alex Lindahl's account; not audited. |
| Akron believed speed to lead would lift conversion at every stage | **Verified in source** | Stated as his belief in the post. |
| Exa reps read adoption patterns and tell customers what they noticed | **Verified in source** | GTMnow summary of the Marcus Holm episode. |
| Salesforce to acquire Braze for about $5.66B; event driven engagement reading | **Verified in source** | Both GTMnow (3 Charts) and GTM Strategist give the figure; the "event driven" reading is GTMnow's. |
| RevOps system of record, GTM engineering system of action | **Verified in source** | The Signal. |
| Lindahl's conditional run tip (enrich a mobile number only if lead matches ICP) | **Verified in source** | GTM Engineering newsletter 27 Oct. |
| Datarails prospect said "I see your ads all the time" | **Verified in source** (6 words) | GTMnow summary, Aviv Canaani episode. |
| Seismic: 75% of 200 B2B leaders trust human guidance more than AI when they conflict | **Single source** | GTMnow summary of Seismic research; I did not see the report. |
| Four questions, "window at least five times your reflex", payroll example | **Unverified (my synthesis / invented illustration)** | Labelled as mine and as hypothetical in the text. |
| "A form fill is about the strongest signal a buyer can send" | **Unverified (my opinion)** | Soften if you disagree. |
| "A job change has a window shorter than most sequences" | **Unverified (my opinion)** | No source gives job change windows. |

## Weakest paragraph

"What it looks like in a small team". The payroll numbers (months, weeks, hours, 20 hours) are invented to show the arithmetic, and a sharp reader will ask where they came from. It is labelled hypothetical, but if it feels thin, cut it and let the four questions stand alone.

## Two alternative titles

1. Before you buy another signal, time how fast you can answer one (63 characters)
2. Your signal list has a shelf life, and nobody has stamped it (60 characters)

## Two alternative opening lines

1. A trucking company's insurer cancels its policy, the government publishes it by the next morning, and nobody picks up the phone for ten days.
2. Your dashboard knows a buyer's situation changed at nine. Your rep finds out on Thursday.

## Voice check: suspect generic sentences with rewrites

| Sentence | Concern | Rewrite |
|---|---|---|
| "The gap between those two moments is the most expensive number you do not track." | Slightly slogan like | "Nobody puts a line for that gap in the weekly report, and it is where the money goes." |
| "None of those writers makes the point I want to make, which is that each treats the signal as the asset." | Contrast framing, a little formal | "Each of those writers treats the signal as the asset, and I would price it as a window instead." |
| "Everyone could see the signal, so seeing it gave nobody an edge. Answering it would have." | Edges toward the banned antithesis shape | "Everyone could see the signal. Whoever called first would have had the owner to themselves." |
| "Buy fewer signals, and answer the ones you own before the clock does." | Fine as a closer; check it lands | Keep, or: "Own fewer signals and answer all of them." |
| "Hone the number to your own market, but keep some number." | Idiom stack | "Adjust the ratio to your market, and keep one." |

## Completeness check against the brief

| Item | Status |
|---|---|
| Collect: Gmail search with label, up to 25 read, newest first | Done (25 threads found, all editorial read; exceptions listed above) |
| 01 signal map with counts, 3+ newsletter themes, underrated idea, contradiction, 3 angles, one chosen | Done |
| Stress test and the two strongest rejected angles | Done (in 01) |
| 02 article, 1,800 to 2,200 words | Done (about 1,980 words including sources and hashtags) |
| Title under 70 characters (57), one sentence standfirst, byline exact, no job title | Done |
| Opens bold declarative then curiosity hook | Done |
| Short sections, 2 to 4 sentence paragraphs, one concrete example per section | Done, mostly (the opinion section has longer paragraphs; trim if you want) |
| "What this means for your next quarter" with three actions this week | Done |
| Sources section linking each newsletter used | Done (five newsletters) |
| Memorable final line, one question, 5 to 8 hashtags | Done (8 hashtags; the question comes after the closing line) |
| Image markers | Done (4) |
| 03 HTML with allowed tags only, no inline CSS or scripts, title not inside | Done |
| 04 image manifest | Done |
| 05 review notes with all required sections | Done |
| issue.json and design build, every PNG viewed | Done, no overflow warnings |
| news_cover with main headline plus two alternatives | Done |
| Review page published without Copy buttons, Draft tag or PR link | Built at `design-bw/newsletter-bw.html` (no such elements) |
| No newsletter text copied; quotes under 15 words, one per source | Done (Cannonball, GTMnow, one each) |
| No images from newsletters | Done |
| Em dashes, en dashes, hyphens as dashes | None in the article |
| "DRAFT: pending Remmy review" on repo files | Done |
| Branch, commit, draft PR | See PR |
| Artifact review page, email to contact@markoholics.com subject "DRAFT v2:" | See delivery summary |
