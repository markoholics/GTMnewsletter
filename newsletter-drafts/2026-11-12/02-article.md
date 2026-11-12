**DRAFT: pending Remmy review**

[IMAGE 1: header-cover.png, Cover: Your GTM stack has a build-or-buy problem nobody's solved yet, black type on white with a window bar]

# Your GTM stack has a build-or-buy problem nobody's solved yet

*A read on the test that decides whether a new tool earns a seat in your go to market stack, and the habit that quietly wastes the most money in it.*

*By Mohammad H. Rahman*

**Most founders running go to market in house are not short of tools. They are short of a reason to say no to the next one.** A RevOps job posting from RingCentral names its actual working stack in plain text.

Pocus or Apollo, Clay, n8n, Claude Code, a handful of MCP servers, and Salesforce underneath it all, with a first year target of lifting the meeting set rate from 1.48% to 2% and generating $10 million in incremental pipeline across 55 reps (per GTM Engineer Pulse #48). A hiring ad as specific as that one reads like a parts list.

Six more postings in the same week each name their own real stack, and the newsletter's own tally is blunt: four of the six name Clay, three name Claude, two name an MCP server (per GTM Engineer Pulse #48). The in house stack has stopped being a slide in a board deck and become something you can read in a job description.

## The debate everyone already has a half formed opinion on

Ask a founder whether to build or buy their GTM stack and most will answer for the whole company at once, as if one philosophy covers a CRM, a dialler, and a coding agent equally well. It does not. The operators who actually run these systems have quietly dropped the either or.

At Clay's own "Sculpt" conference, twenty GTM operators were interviewed on the record, and the consensus theme was not build or buy, it was build and buy: buy the foundation, build on top of it (per The Signal, "Lessons from interviewing 20 GTM operators at Sculpt"). Brendan Short, who writes The Signal, puts his own version of the same instinct more bluntly: buy the infrastructure, build the brain (per The Signal, "AI Adoption is coming in waves").

That phrase is a good start, but it is still a slogan, not a test. A slogan tells you the shape of the answer. It does not tell you which bucket your renewal falls into on a Tuesday afternoon when a vendor is on the phone.

## What counts as infrastructure, and what the market is already repricing

Here is a test that holds up: a job is infrastructure when an outsider, not the vendor, can check whether it did the job. A job is the brain when the value comes from what your own data teaches it over time. The data enrichment category shows what happens when a market forgets the difference.

ZoomInfo, the long standing market leader, reported Q2 2026 revenue of $310.4 million, up only 1.2% year on year, alongside a $650.5 million goodwill impairment, a $643.7 million net loss, and net revenue retention of 89%, meaning its existing customers are spending roughly 11% less than they were a year ago (per GTM Tool Time, "Data Enrichment, Reviewed", citing ZoomInfo's own filings). Clay, by contrast, is the only vendor in that same review publishing dated weekly changelog entries, and its median contract on Vendr sits near $60,000 a year, nearly double ZoomInfo's median and roughly three times Apollo's (per GTM Tool Time, citing Vendr data).

Something in that category is being repriced, and the accuracy of the data has little to do with it. Every accuracy claim in enrichment traces back to a vendor with a stake in it, which is precisely why nobody can check infrastructure claims in this category against anything but another vendor's claim.

## The second tool that buys you almost nothing

Here is the habit that wastes the most money, and almost nobody has said it plainly: running two tools in the same job rarely doubles your coverage. It mostly doubles your invoice. Clay published its own waterfall test, and to its credit, published it even though the result makes stacking providers look wasteful: chaining a second enrichment provider on top of a first returned just 5 net new records out of 100 prospects tested. The other 95 were duplicates the first provider had already found (per GTM Tool Time, "Data Enrichment, Reviewed", citing Clay's own published test).

Whoever said two heads are better than one clearly never watched two enrichment providers hand back the same ninety five names twice.

The same arithmetic shows up outside enrichment, with sharper consequences. Mark Fisher traced a batch of unrouted leads to a sync collision: a HubSpot workflow was stamping a record's owner the moment it was created, which silently disabled Salesforce's own assignment rules, because those rules only fire on ownerless records (per GTM Engineer Pulse #47). Nobody chose for that to happen.

Two systems doing adjacent jobs met in the middle, and the second one did not add coverage, it quietly cancelled the first one's work. A second tool earns its seat only when you can point to the specific records or minutes it adds beyond the first, and when somebody has checked how the two actually interact. Most renewals cannot clear that bar, because nobody has ever been asked to.

## The job nobody has named on an org chart yet

If data hygiene and sending infrastructure are the clearest cases for buying, there is a newer job emerging that looks like the opposite case, and five different operators at the same conference named it independently without being asked to agree: a context layer, the thing that holds account and buyer history so an agent is not starting from zero on every call (per The Signal, "Lessons from interviewing 20 GTM operators at Sculpt"). Pouyan Salehi, the Clearskies co founder who argues this case at length in a guest post The Signal is candid about having been paid to carry (its own editor disclosed the sponsorship inline), ran a test worth noting with that caveat attached: the same model, asked the same 23 questions about 5 real accounts, answered 43% of them fully correctly using raw CRM and call transcript access, and 65% fully correctly once routed through a purpose built context layer, at the same cost per answer (per The Signal, guest post, "Operationalizing AI for revenue teams"). That is a vendor's own benchmark for its own product, so treat the exact numbers as a single, sponsored source rather than settled fact.

What is harder to dismiss is what an unsponsored founder actually built. Thibault Le Meur, who runs a GTM consultancy and was not paid by any tool to say so, built his own context layer on Claude in roughly three hours: seven template files describing his business, a weekly agent that scores open deals against three gating questions borrowed from sales methodology, quoting only real call and email text and writing "EMPTY" rather than guessing when the evidence is not there, and a monthly agent that proposes changes to his own playbook only once three or more buyers have independently said the same thing (per MRR Unlocked, "The 2 GTM AI Agents for Founder-Led Teams"). It also broke in honest, instructive ways: his pipeline tracker was stale, so the agent fell back to reading raw files; his call recorder occasionally misattributed who said what, so any negative verdict still needed a human to check the original call; and his first scheduled run hit a usage limit eight seconds in, even on a paid plan. "An EMPTY is more useful to me than a good guess," he wrote, and that single habit, refusing to let a model invent evidence it does not have, is closer to a working definition of a context layer than any vendor's slide.

## The one thing almost everyone already agrees on, and still ignores

Ask any of these operators what breaks an agent and you get the same answer in different words. Clay's own head of marketing, speaking at that conference about her own company's product, put it as plainly as anyone has: AI just makes bad data fail faster (per The Signal, "Lessons from interviewing 20 GTM operators at Sculpt"). The evidence for that is not abstract. One operator audited a $4 million pipeline the week before an AI agent was due to start acting on it, and found 73% of it dead or stale.

After cleanup, the pipeline was $1.1 million and forecast accuracy rose from 44% to 88%, by his own count (per GTM Engineer Pulse #47). His five checks before letting any agent near a CRM are worth copying wholesale: last buyer activity, how many times a close date has moved, days spent in the current stage, whether the stage has any exit criteria at all, and exactly what the agent is allowed to write.

Cognism, which ships a widely used enrichment API over MCP, builds the same caution into its product by default, keeping a "confirm before reveal" step on specifically because a prompt injected page could otherwise spend a user's own credits without them noticing (per GTM Engineer Pulse #48). The infrastructure vendors who understand this job best are the ones quietly limiting what their own tool is allowed to do.

## Where this view runs into a fair objection

Is running two providers in the same job always waste? Not quite. FullEnrich's entire product is built on chaining more than twenty enrichment providers in a waterfall, and it bills only when one of them returns a hit (per GTM Tool Time, "Data Enrichment, Reviewed").

That looks, on the surface, like the exact habit this piece argues against. It survives the objection because the economics are different: you are not paying two seat prices for the same job, you are paying a marginal fee for a marginal record, inside a single billing relationship built to handle the overlap on your behalf.

Does that mean deliberate redundancy is always fine, then, as long as it is cheap? Also not quite. The native routing rules bundled free into most CRMs are, in GTM Tool Time's own words, "cheap, present, and almost always thinner than the page implies" (per GTM Tool Time, "Lead Routing, Reviewed"), and plenty of teams run one of those alongside a dedicated router as a safety net.

That is a reasonable instinct. It is also exactly the setup that produced Mark Fisher's silent sync collision above, because nobody had mapped how the free rule and the paid one would behave once both were live on the same record.

So the test holds, but it needs one line added to it: a second tool in the same job only earns its keep when its marginal cost is genuinely marginal, and when a named person has checked how it behaves next to the first one. Pay twice for coverage you can prove, never for coverage you assume.

## The four questions worth asking before a renewal

[IMAGE 2: insight-card.png, Large stat: Claude named by 110 respondents as the most impactful GTM tool, more than 3x the next vendor, per Growth Unhinged's 2026 State of B2B GTM report]

It helps to have this in four questions rather than one slogan, because a renewal conversation moves fast and a slogan does not survive it. First, name the job in one sentence, not a feature list: what exactly is this tool hired to do. Second, ask whether an outsider could check its claim without trusting the vendor's own benchmark, the way GTM Tool Time checked a dozen enrichment vendors against their own public filings and changelogs rather than their marketing pages.

Third, ask whether the job compounds with your own data over time, the way Thibault Le Meur's weekly agent gets more specific the longer it reads his real deals, or whether it is simply rented capacity that resets at midnight. Fourth, and the one most renewals skip, ask whether something already in your stack does this exact job, and name the marginal thing the new tool adds that the old one does not.

[IMAGE 3: quote-card.png, Quote card: The vendors sell the stopwatch, not the time, attributed to Marty Berman, GTM Tool Time]

The lead routing market makes that fourth question easy to dodge and expensive to skip. None of the six leading routing vendors GTM Tool Time checked publish a response time commitment with an actual number attached. One, Distribution Engine, states plainly that it lets a customer set whatever service level they agree on, then holds the team to it automatically (per GTM Tool Time, "Lead Routing, Reviewed"). As Marty Berman, the newsletter's own reviewer, puts it: the vendors sell the stopwatch, not the time.

[IMAGE 4: framework.png, Four boxes in order: Job, Checkable, Compounding and Headcount, each with the question to ask]

## What this means for your next quarter

Three actions a founder managing GTM in house can take this week.

1. **List every tool by job, not by name, and find the duplicates.** For each job to be done in your stack, write down what marginal coverage the second tool adds beyond the first. If you cannot name a number, GTM Tool Time's own finding (5 net new records out of 100) is the bar the second tool has to clear. Most will not.
2. **Run a pipeline hygiene pass before buying anything described as AI native.** Borrow the five checks from GTM Engineer Pulse #47: last activity, close date movement, time in stage, missing exit criteria, and exactly what write access any agent gets. Do this before the next demo, not after.
3. **Pick one job this quarter to build rather than buy, and name who owns it.** It does not need to be a platform. Thibault Le Meur's working context layer took three hours on paper. Choose the smallest job where your own data is the advantage, and build the brain for that one job before you shop for another vendor to rent it from you.

## Sources and further reading

- Marty Berman, GTM Tool Time, [Data Enrichment, Reviewed](https://read.gtmtooltime.com/p/data-enrichment-reviewed): the ZoomInfo repricing, Clay's weekly changelog, and the waterfall test.
- Marty Berman, GTM Tool Time, [Lead Routing, Reviewed](https://read.gtmtooltime.com/p/lead-routing-reviewed): the stopwatch quote and the unpublished SLA commitments.
- Jared, GTM Engineer School, [The GTM Engineer Pulse #47](https://gtmengineerschool.substack.com/p/the-gtm-engineer-pulse-47): the $4 million pipeline audit and the sync collision.
- Jared, GTM Engineer School, [The GTM Engineer Pulse #48](https://gtmengineerschool.substack.com/p/the-gtm-engineer-pulse-48): the RingCentral and six other job postings, and Cognism's MCP governance.
- Brendan Short, The Signal, [AI Adoption is coming in waves](https://www.thesignal.club/p/ai-adoption-is-coming-in-waves): the build the infrastructure, build the brain framing.
- Brendan Short, The Signal, [Lessons from interviewing 20 GTM operators at Sculpt](https://www.thesignal.club/p/lessons-from-interviewing-20-gtm-operators-at-sculpt): the build and buy consensus and the context layer naming.
- Pouyan Salehi (guest post, disclosed sponsor), via The Signal, [Operationalizing AI for revenue teams](https://www.thesignal.club/p/operationalizing-ai-for-revenue-teams): the context layer benchmark (vendor sourced).
- Thibault Le Meur, via MRR Unlocked, [The 2 GTM AI Agents for Founder-Led Teams](https://www.mrrunlocked.com/p/2-gtm-ai-agents-for-founder-led-sales): the three hour build and the EMPTY rule.
- Kyle Poyar and Maja Voje, Growth Unhinged, [What's working in B2B GTM in 2026](https://www.growthunhinged.com/p/2026-state-of-b2b-gtm-report): the Claude survey finding.

A stack, properly kept, is a short list of decisions: which jobs you trust a vendor to do in the open, and which ones you would rather teach yourself.

Which job in your current stack would survive if you had to justify it with a number instead of a name?

#GoToMarket #GTMEngineering #BuildVsBuy #RevOps #B2BSaaS #StartupTools #FounderLed
