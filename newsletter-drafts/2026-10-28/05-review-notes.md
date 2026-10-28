# 05 Review notes

**DRAFT: pending Remmy review**
Be hard on this. Cut anything weak.

## Assumptions

- **Date range.** `label:GTM-Newsletters newer_than:7d` on 28 October 2026 worked first time (26 threads, 21 to 28 October). The quoted fallback was not needed. The run was triggered manually one day early.
- **Gmail use.** Search and read only. Nothing was replied to, archived, labelled, starred, trashed or deleted. The one send is the draft to contact@markoholics.com.
- **Emails skipped (7 of 26) and why:** your own Substack sample post and "Decide what your growth loop pays in" post, plus the earlier "DRAFT:" email you sent yourself (all yours, not newsletters); three Substack system notices (Notes digest, live video alert, new subscriber); Clay "Welcome" mail; Clay and Apollo promotional mail.
- **Read in full this run (8):** Growth Unhinged (creator wave), GTMnow (Exa), GTMnow (Datarails), GTM Engineering (monday.com agents), GTM Engineering (10 metrics and Grok Bot), Cannonball GTM (Pain Map and the Oct 27 post), The Signal (swim lanes). **Subject and snippet only (not read):** Lenny's Newsletter (3), GTM Strategist, GTM Weekly #31, GTM Engineer Pulse #46, "5 big AI GTM ideas", "3 Charts on Where Venture Money Is Going", the global tech map post. I stopped at eight because the thesis was already supported by four of them.
- **Overlap with earlier issues.** Datarails appears again for one point (four attribution signals that disagree), which the 22 Oct issue also used. Cut that paragraph if you want zero overlap. The Signal and Cannonball informed the signal map only; neither is cited.
- **Build tooling.** `DESIGN.md`, `CLAUDE.md` and `tools/newsletter-design/` are not on `main` yet. They live on `claude/newsletter-2026-10-23`, which has not been merged. I copied those files onto this branch so the build could run. The 2026-10-23 issue folder is not included, so merging this PR before the 23 Oct one is fine, but expect a trivial conflict on those shared files if both land.
- **Newsletter cover.** `newsletter-cover.jpg` was rebuilt for this issue as the script always does; it is identical in design to last week's.
- **Names inferred or not fully seen:** "GTM Engineering newsletter" (taken from the sender domain newsletter.gtmengineering.ai and the Substack link text; the exact publication title was not shown); "GTMnow Newsletter" (from the link text in the email footer; the sender address is thegtmnewsletter); Oran Akron's role as "VP of AI GTM" is not used in the article. Pronouns are avoided for everyone named. Kyle Poyar, Alex Lindahl, Marcus Holm, Oran Akron and Aviv Canaani were named in the emails.
- **Banned words.** None appear in the article. "Growth Unhinged" contains no banned word. The title of the Datarails source in Sources uses "30x", which is part of the source's own title; flagged in case you prefer to drop it.

## Numbers and claims: certainty

| Claim | Certainty | Note |
|---|---|---|
| Poyar's first sponsor deal took under a week; renewal needed reporting, procurement, months of negotiation | **Verified in source** | Growth Unhinged, 28 Oct. His own account. |
| Brands expect quantifiable return at renewal; "You land in brand marketing and expand in growth marketing" (10 words) | **Verified in source** | Appears in Growth Unhinged ("Said differently, you land in..."). |
| Report using a sheet with 48 hour and two week stats | **Verified in source** | Growth Unhinged, as a writer tip. |
| One $100,000 deal after a quarter of ads makes the CPM barely matter | **Verified in source** | Growth Unhinged. |
| Poyar has partnered with about a dozen brands | **Verified in source** | Growth Unhinged. Article says "roughly a dozen sponsors". |
| Exa passed $100M ARR, growing roughly tenfold a year for almost three years | **Single source** | GTMnow summary of the Marcus Holm episode. The source says "nearly 10x per year"; I wrote "roughly tenfold" to avoid the banned "10x". |
| Consumption model, "always on trial", comp rewards committed revenue above pay as you go, "jungle guide" | **Verified in source** | GTMnow summary of the episode. The summary quotes "you're always on trial" (4 words); I used the idea twice and the exact phrase once, attributed. |
| monday.com: about 25 hours average inbound wait in early 2025, under two minutes by the time Akron left | **Single source** | Alex Lindahl's account of a conversation with Oran Akron. Not audited. |
| 20,000+ leads a month, about 1,500 discovery calls booked a month | **Single source** | As above. |
| Agent got a slice of leads and more only when it matched or beat humans; recordings open to anyone; daily 20 minute evals; half the job was change management | **Single source** | As above. |
| Datarails: VP of Brand has no revenue KPIs, measured on ICP engagement; paid media first to earn latitude; four attribution signals that often disagree | **Verified in source** | GTMnow summary of the Aviv Canaani episode. |
| The hypothetical Series A analytics company and freelance writer | **Unverified (illustration)** | Labelled as invented in the text. No real company implied. |
| "A customer success manager's quarterly review is usually addressed to the person who bought" | **Unverified (my opinion)** | A generalisation, not from a source. Soften or cut if you disagree. |
| "The memo is the only part of you that stays in the building" if a champion leaves | **Unverified (my interpretation)** | Opinion. |
| The renewal memo habit itself | **Unverified (my synthesis)** | None of the four sources recommends it. The article says so in "Where this breaks". |

## Weakest paragraph

The customer success paragraph in "Why a memo is not a success plan" ("Surely a good customer success manager does all of this already?"). It is an assertion about how CS reviews are addressed and rests on no source. If it feels like a straw man, cut it; the section works without it.

## Alternative titles

1. Your renewal memo should exist before your first invoice
2. The page your champion will forward: draft it on day one

## Alternative opening lines

1. **The cheapest piece of evidence in your sales process is the one nobody writes until the renewal.**
2. **A first sale buys you a hearing, and a second sale needs a page.**

## Voice check: suspect sentences and rewrites

- "Those documents look similar in a template and behave differently in a meeting." Slightly neat. Rewrite: "On paper they look alike. In a budget meeting they do not."
- "A success plan describes what you hope will happen. A memo describes what a stranger will need to read." Close to a paired contrast. Rewrite as one sentence: "A success plan records hopes, while a memo is written for the stranger who must approve the spend."
- "None of that is sophisticated." Generic. Rewrite: "Nothing there needs software."
- "I would rather list them than hide them." Mild filler. Rewrite: "Here they are."
- "Read that again as a sales process rather than an engineering one." Borders on "X rather than Y". Rewrite: "Now read it as a sales process."
- Proverb flip used once ("Whoever said the first sale is the hardest clearly never had to renew one"). Keep or cut.
- The opening statement ("every first sale is a vote of faith, and every second sale is an audit") is a deliberate bold declarative; it is not an "isn't A, it's B" construction.

## Completeness check against the brief

| Item | Status |
|---|---|
| Label-only Gmail threads; promotional and system mail skipped | Done |
| 01 signal map: newsletters with counts first, 3+ newsletter themes, underrated idea, contradiction, 3 angles, one chosen and justified | Done |
| Stress test; thesis adds a point of view no source has | Done (in signal map) |
| 02 article about 1,800 to 2,200 words | Done, about 1,930 including image markers |
| Title under 70 characters | Done (53) |
| One sentence standfirst | Done |
| Byline exactly "By Mohammad H. Rahman", no designation | Done |
| Bold declarative open then curiosity hook | Done |
| Short sections, paragraphs of 2 to 4 sentences, one concrete example per section | Mostly. The "Where this breaks" and "Why a memo is not a success plan" sections use several short paragraphs; the second has a four question run. |
| "What this means for your next quarter" with three actions | Done |
| Sources and further reading linking each newsletter used | Done (four links, three newsletters; GTMnow appears twice for two episodes) |
| Memorable final line then one question | Done |
| 5 to 8 specific hashtags | Done (7) |
| [IMAGE n] markers | Done (4) |
| 03 HTML only permitted tags, no inline CSS or scripts, title not inside | Done |
| 04 manifest with alt text under 125 characters | Done |
| 05 review notes with all required parts | Done |
| Quotes under 15 words, one per source | Done (Poyar, 10 words; one short phrase from GTMnow) |
| British English, no dashes as punctuation | Checked by script; hyphens remain only inside URLs and image filenames |
| Design: black, white, grey; issue.json; build.py run; every PNG viewed | Done |
| Review page `design-bw/newsletter-bw.html` has no Copy buttons, Draft tag or PR link | Done (checked) |
| No mention of Markoholics or other ventures in the article | Done |
