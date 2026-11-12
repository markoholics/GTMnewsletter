# 01 Signal map, 12 Nov 2026

**DRAFT: pending Remmy review**

Theme override for this issue (set by Mohammad): what tools to use if you are managing go to market in house. Which tools earn a place in an in-house GTM stack, which jobs they should be hired for, how to decide. Scope for this run: the whole "GTM Newsletters" label, no date limit, not just the last 7 days.

## Newsletters found

The label "GTM Newsletters" holds **201 threads** in total. I scoured newest first across roughly 150 of them (four pages of search results) before narrowing to a tool and stack focused shortlist, because a large stretch of the older mail (roughly 5 to 13 October) turned out to be several dozen self-sent "Approve LinkedIn draft:" threads from the markoholics.com address itself, with nested, repeated subject prefixes. That is personal, own-account correspondence, not an editorial newsletter, so none of it was read, and nothing in it was acted on.

Of the rest, **32 threads were shortlisted** as naming, comparing, evaluating or explaining tools, workflows, stacks or vendors. **16 of those 32 were read in full** before this run's time budget for the Collect step ran out. The 16 give strong, cross-corroborated, well-attributed material (several themes appear in four or more independent sources below), including the three best-structured sources in the whole label. The other 16 shortlisted threads (GTM Engineer Pulse #45/46, seven more GTM Engineering Newsletter issues, two GTMnow case studies, Lenny's "Claude Duet" review, two Maja Voje issues) were not opened; they are listed in the review notes as unread, not skipped for cause.

| Newsletter | Author / publisher | Emails read in full | Subjects |
|---|---|---|---|
| GTM Tool Time | Marty Berman | 3 | Sales Engagement, Reviewed; Data Enrichment, Reviewed; Lead Routing, Reviewed |
| The Signal | Brendan Short | 6 | AI market whiplash; Nooks launches Node (sponsored); AI adoption comes in waves / build vs buy; Swim lanes between RevOps and GTM Engineering; Operationalizing AI for revenue teams (Clearskies guest post); Lessons from interviewing 20 GTM operators at Sculpt |
| Growth Unhinged | Kyle Poyar | 3 | Inside Clay's GTM machine (sponsored); 5 GTM plays working right now; What's working in B2B GTM in 2026 (300-respondent survey, co-run with Maja Voje) |
| GTM Engineer Pulse | Jared, GTM Engineer School | 2 | #47, #48 |
| The GTM Engineer | Clay (published by the vendor) | 1 | How to Hire a Go-to-Market Engineer for the Agentic GTM Era |
| MRR Unlocked | Alex Estner (guest: Thibault Le Meur) | 1 | The 2 GTM AI Agents for Founder-Led Teams |

Deliberately excluded throughout: Clay's and Apollo's own promotional onboarding sequences (CATEGORY_PROMOTIONS, vendor advertising rather than editorial content), Substack system notices (new subscriber pings, "X posted new notes", live-video reminders, calendar invites), and the self-sent "Approve LinkedIn draft" noise described above.

## Tools named, grouped by job to be done

- **Sales engagement / outreach sending:** Smartlead, Instantly, Saleshandy, Outreach, Salesloft, Woodpecker, HubSpot Sales Hub, Unify, Artisan, 11x, Yesware, La Growth Machine
- **Data layer / enrichment / scoring:** Clay, Apollo.io, ZoomInfo, Hunter.io, FullEnrich, Common Room, Cognism, HubSpot Breeze Intelligence, Lusha, Keyplay, Findymail, Ocean.io, Seamless, Pocus, Prospeo, Datagma
- **Lead routing / inbound orchestration:** LeanData, Traction Complete, Distribution Engine, Openprise, Gradient Works, ZoomInfo Operations (orchestrators); Chili Piper, RevenueHero, Calendly, Cal.com, Kronologic (bookers); Fin, Qualified, Warmly, Agentforce Engagement (responders); Default (agent-native)
- **Call intelligence:** Gong, Airspeed, Fathom, Nooks
- **CRM / system of record:** Salesforce, HubSpot
- **Context / memory layer (an emerging job, named independently by several operators, not a settled category):** Clearskies (vendor), homegrown builds (Vercel's own, Thibault Le Meur's Claude-based build)
- **AI agent substrate:** Claude, Claude Code, Grok Bot, n8n, Zapier, MCP servers
- **Signals / intent:** Common Room, Sumble
- **Attribution:** Fibbler, in-house rebuilds

## Themes in three or more newsletters

1. **Bad data breaks automation before the tool does.** GTM Engineer Pulse #47 (a $4M pipeline audit found 73% dead before an agent went live), GTM Engineer Pulse #48 (Cognism's MCP server ships "confirm-before-reveal" guardrails specifically against prompt injection), the Sculpt interviews via The Signal (Clay's own head of marketing: "AI just makes bad data fail faster"), and GTM Tool Time's enrichment review (every accuracy claim in the category traces back to a vendor with a stake in it).
2. **"Build vs buy" is being replaced by "build AND buy."** The Signal's own framing ("buy the infrastructure, build the brain"), the Sculpt interview consensus (named independently by multiple operators as "build AND buy," not either/or), Growth Unhinged's "5 GTM plays" (incident.io, Vercel and Clay's own teams all buy point infrastructure and build the connecting logic themselves), and MRR Unlocked's founder-led case study (buys a call recorder, builds the judgment layer on Claude).
3. **A "context layer" is emerging as its own job to be done, underneath the agents.** Named independently by five different operators at Sculpt (via The Signal), argued at length by Clearskies' CEO in a disclosed sponsored guest post, and illustrated in practice by Vercel's and Clay's own in-house rebuilds (Growth Unhinged).
4. **Claude has become the default substrate, fast.** Growth Unhinged's 300-respondent survey has Claude as the single most-impactful GTM tool named (110 mentions, more than 3x the next vendor, up from #4 a year ago); GTM Engineer Pulse #48's analysis of 420 GTM-engineer job postings and six individual company job ads both name Claude or Claude Code repeatedly as part of the actual in-house stack; MRR Unlocked's founder built his whole agent setup on it.

## One underrated idea from a single newsletter

GTM Tool Time's "Data Enrichment, Reviewed" ran Clay's own published waterfall test: stacking a second enrichment provider on top of a first returned only 5 net-new records out of 100 prospects, the rest were duplicates the first provider had already found. Nobody else in the label drew out the implication: buying a second tool in the same job-to-be-done category is close to buying nothing.

## One contradiction

Nooks' CEO, in a sponsored piece in The Signal, argues AI sales agents are already working (96% of its own agent-drafted emails go out unedited, meetings per rep allegedly doubled) and a Clay co-founder is quoted claiming prospects told Clay's early inbound agent more than they tell human reps. Growth Unhinged's independently run 300-respondent survey, in the same window, reports the opposite mood: cold outreach is now rated "oversaturated" and states plainly that "AI SDRs aren't living up to the early hype." Same month, opposite verdict on whether agents are actually closing the gap, and the optimistic claim comes from the vendor with the most to gain from it.

## Three candidate angles

A. **Stop asking build or buy for the whole stack. Ask it job by job.** A decision rule: buy when a job to be done is commoditised infrastructure with a checkable, external SLA; build when it is the judgment layer that compounds with your own data, and never run two paid tools doing the same job. Payoff: a founder gets a test to apply to every renewal, not just a listicle of logos.
B. **The real buying decision now is the context layer, not the CRM.** In-house teams keep re-fighting old CRM and enrichment turf wars while the job that actually determines whether agents work, holding account and buyer context so an agent does not start from zero, is still unowned. Payoff: stop relitigating the CRM, decide who owns context.
C. **Clean the data before you buy anything AI-native.** Every failure story in this label traces back to dirty CRM data, not a weak tool. Payoff: a pre-flight checklist before letting any agent touch the pipeline.

## Pick: A

Angle A is the only one that organises nearly everything the research surfaced, the enrichment stacking waste, the sales-engagement scoring mess, the lead-routing consolidation wave, Clay's and Vercel's own build patterns, and MRR Unlocked's founder-led build, into a single, repeatable test rather than a single observation. It also states a view none of the sources states outright: that the operative unit of the build-or-buy decision is the job to be done, not the company or the category, and that running two tools in one job is close to running none. B is true and well evidenced but is one layer inside A, not a whole stack strategy; C is well evidenced but is a precondition for A, not a decision rule of its own. Angle A folds B and C in as sections rather than discarding them.

## Stress test (sceptical GTM operator)

- *Obvious?* "Build versus buy" is one of the oldest debates in software. The claim here is narrower and checkable: apply the test per job to be done, not once for the whole stack, and treat a second tool in the same job as roughly worthless unless it clears a specific bar. That survives, because none of the sixteen sources state the per-job framing or the "second tool, five new records" implication as a rule.
- *Everywhere already?* The Signal and the Sculpt interviews already say "buy the infrastructure, build the brain" and "build AND buy." True, and the article credits both openly. What is missing from every source is a concrete test for sorting a given job into one bucket or the other, and the stacking-waste argument. Partly survives; the piece earns its place by adding the test and the waste argument, not by repeating the framing.
- *Would a founder change a decision?* Yes. A team paying for two enrichment tools, or evaluating a third outreach platform because its current one feels tired, now has a specific reason to cut rather than add, and a specific question to ask before buying a fourth category tool: is this job commoditised infrastructure, or is it where our own data compounds?

### Two strongest rejected angles

**B. The context layer is the real decision.** Strongest on novelty: nobody else in the label has named it as the central decision. Rejected as a whole-article thesis because its primary evidence is a disclosed sponsored benchmark (Clearskies) and five anecdotal mentions at one conference. It is real and underrated, but not yet load-bearing enough to carry 2,000 words alone; it survives inside Angle A as the clearest present-day example of a "build the brain" decision.

**C. Clean the data first.** Strongest on evidence: a $4M pipeline audit, a vendor's own MCP governance warning, and a vendor-affiliated operator all point the same way. Rejected as a standalone thesis because it has been said, in some form, by every ops writer for a decade, and on its own it is a checklist, not an argument that changes how a founder chooses between two vendors. It survives inside Angle A as the reason the test only works once the underlying data is trustworthy.

Also considered and dropped: "Claude has become the default substrate" as its own angle, because it is a strong, well-sourced finding but a single data point about which tool is winning, not a decision framework; it is used as supporting evidence inside Angle A instead.

## Vendor ties to flag before publishing (see 05 for the full list)

The GTM Engineer (published by Clay), Growth Unhinged's Clay-sponsored issue and its State of B2B GTM report (presenting/gold/silver sponsors including Ploy, Sumble, Primer, Salesforge, Passionfroot, Civic), The Signal's every issue (presented by Clay, supported by Attention, Clarify, Clearskies, Nooks, Rox, Sumble, Terret, with the Nooks and Clearskies issues specifically paid or guest-authored placements). GTM Tool Time is the one source in this set that discloses taking no vendor money and publishes its own corrections log; it carries the most weight in the article for that reason.
