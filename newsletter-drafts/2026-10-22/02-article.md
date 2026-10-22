**DRAFT: pending Remmy review**

[IMAGE 1: cover.png, Cover: Your GTM stack needs a column called how do we know, in white serif type on navy]

# Your GTM stack needs a column called "how do we know?"

*One field, three labels and a permission rule will do more for your AI rollout than another quarter of data cleaning.*

*By Mohammad "Remmy" Rahman, Founder, Markoholics*

**Your dashboard is reporting things it has never checked.**

Take a cold email dataset of 6.07 million messages. Auto-replies made up 51% of everything in the reply folder, so the human reply rate was half the headline figure (per The GTM Engineer Pulse, citing Grow Surely, one agency's client mix). Nobody lied. The number simply carried no record of how it was known.

I read sixteen GTM newsletter issues this week, and the sharpest operators in them kept circling one small habit that fixes this. It costs an afternoon.

[IMAGE 2: insight-card.png, Large navy 51%: of cold email replies in a 6.07 million message dataset were auto-replies]

## A guess dressed as a record

Jay Mount, a B2B systems consultant, checked 250 contacts from a client's enriched list by hand. About 60% were right. When the platform had no direct data it fell back to an AI guess, and in his words: "Guesses sat next to real records. Both were shown with the same confidence." (per The GTM Engineer Pulse.)

Picture a rep dialling row 140. Nothing on the screen tells them which kind of row it is. That single gap is the whole problem.

## What happens when the guess keeps travelling?

What happens when it leaves the contact list and lands in a deal review? Thibault Le Meur, who runs a GTM consultancy for founder-led European tech firms, built an agent that reads his open deals every Monday and answers three questions from buyer evidence alone: why do anything, why now, why us. Where there is no evidence, it writes EMPTY.

On three of his first four deals, "why us" came back EMPTY. Each buyer had told him what they wanted, and he had pitched something else. "An EMPTY is more useful to me than a good guess," he writes (per MRR Unlocked).

What happens when the guess becomes the plan? Emilia Korczynska, co-founder of ZenABM, built her Q4 campaign on the assumption that 18 impressions would make an account engaged. The average landed at nine, and 302 accounts passed 18 against the 848 she expected.

Early days, and her numbers, but pipeline stood at $8,411 against $100,000 planned (per The GTM Engineer Pulse). Whoever said what you don't know can't hurt you clearly never built a quarter on an average nobody opened.

In fairness, the other side has a case. monday.com's agents team shipped its voice agent at roughly 60% and learned on real leads, because nobody can simulate a customer in advance. Response time fell from about 25 hours to under two minutes, and the agent now books around 1,500 meetings a month (per GTM Engineering, as told by monday's former VP of AI GTM). A mammoth result, built on guesses.

But look at how they ran it. Every call and email was evaluated automatically against set criteria, and the team reviewed the results each morning, because nobody can listen to 10,000 calls. The guesses were labelled, and they were reviewed.

## Observed, Inferred, Empty

Here is the habit, assembled from fragments I found across the newsletters. Give every fact your stack holds one of three labels, and let the label decide what an agent may do with it.

**Observed.** A person said or did it, and you can point to the date and the source. A buyer's words from Tuesday's call. A provider record. Observed facts may move a deal stage or send a message.

**Inferred.** A model or a rule guessed. Inferred facts may rank and draft. They may not send or move a stage. Town's growth team gives the same advice: start routines in draft mode and review before anything sends (per GTM Engineering). Kevin Payne, a GTM engineer at LawVu, grades systems as read only, draft only or write approved (per The GTM Engineer Pulse). I am grading facts.

**Empty.** Nobody knows yet. An empty field is a question for a human, and sometimes a finding. Doug Bell's reputation audit of 32 fleet software companies found 16 TMS vendors competing for the big category questions, and next to none named by three AI assistants on the question that can end a carrier's business: one mention, in one assistant (per Cannonball GTM). The empty cell was the most useful part of the audit: an open lane.

[IMAGE 3: framework.png, Three columns, Observed, Inferred and Empty, showing what an agent may and may not do with each]

Bell adds a rule I think is underrated. A brand whose only citations come from its own website is capped at a score of 3, because the model has read only your brochure and nobody else has vouched for you. Observed needs a source that is not you.

## Where monday and Monk part ways

George Kurdin, CEO of Monk, which automates accounts receivable, says precision and security come first in finance, so his team built its own evals, guardrails and tests for the work that touches a customer's money (per GTMnow). That sits uneasily beside shipping at 60%.

The three labels settle it. The less reversible the action, the more Observed it demands.

A draft email to a web lead can run on Inferred. A payment chase cannot. Both are right for their own risk.

## What this means for your next quarter

Three actions you can take this week.

1. **Add a "source" field to the tables your agents write to.** Three values only: observed, inferred, empty. Start with contacts and deals. Expect it to take an afternoon.
2. **Change one rule.** Nothing inferred may send an email or change a deal stage. Let inferred rows draft, and let a person promote them.
3. **Run Le Meur's check on your last five deals.** For each one, quote something the buyer said about why they would pick you, with the date. Write EMPTY where you cannot. Then hone your next call around whatever came back EMPTY.

## Sources and further reading

- [GTM Engineering & AI (Alex Lindahl): monday.com agents](https://newsletter.gtmengineering.ai/p/inside-mondays-agent-team-5-agents) and [Town's 15 tips](https://newsletter.gtmengineering.ai/p/town-hits-1b-6-personal-ai-use-cases)
- [The GTM Engineer Pulse #46 (Jared Waxman)](https://gtmengineerschool.substack.com/p/the-gtm-engineer-pulse-46)
- [MRR Unlocked (Alex), guest Thibault Le Meur](https://www.mrrunlocked.com/p/2-gtm-ai-agents-for-founder-led-sales)
- [Cannonball GTM (Doug Bell): Retrieved or Invisible](https://cannonballgtm.substack.com/p/retrieved-or-invisible-what-ai-thinks)
- [GTMnow Newsletter: George Kurdin, Monk](https://thegtmnewsletter.substack.com/p/gtm-209-ai-accounts-receivable-automation-george-kurdin-monk)

A stack that cannot write EMPTY will write something else, and it will write it in the same confident font.

Which field in your CRM would change most if you had to attach a source to it?

#GTMEngineering #RevOps #AIAgents #B2BGrowth #FounderLedSales #DataQuality #CRM
