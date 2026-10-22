**DRAFT: pending Remmy review**

[IMAGE 1: cover.png, Cover: Your GTM stack needs a column called how do we know, in white serif type on navy]

# Your GTM stack needs a column called "how do we know?"

*A long read on one field, three labels and a permission rule that will do more for your AI rollout than another quarter of data cleaning.*

*By Mohammad H. Rahman*

**Your dashboard is reporting things it has never checked.**

Take a cold email dataset of 6.07 million messages. Auto-replies made up 51% of everything in the reply folder, so the human reply rate was half the headline figure (per The GTM Engineer Pulse, citing Grow Surely, one agency's client mix). Nobody lied. The number simply carried no record of how it was known.

I read sixteen GTM newsletter issues this week, and the sharpest operators in them kept circling one small habit that fixes this. It costs an afternoon, and it changes what your agents are allowed to do. This is a long read, because the habit only makes sense once you have seen where it comes from and where it breaks.

[IMAGE 2: insight-card.png, Large navy 51%: of cold email replies in a 6.07 million message dataset were auto-replies]

## A guess dressed as a record

Jay Mount, a B2B systems consultant, checked 250 contacts from a client's enriched list by hand. About 60% were right. When the platform had no direct data it fell back to an AI guess, and in his words: "Guesses sat next to real records. Both were shown with the same confidence." (per The GTM Engineer Pulse.)

Picture a rep dialling row 140. Nothing on the screen tells them which kind of row it is. That single gap is the whole problem.

His fix is cheap. Ask direct sources first, use inference only when they come back empty, and mark every row "provider record" or "AI inference" so a rep sees the guess before the call (per The GTM Engineer Pulse). Several operators interviewed at Clay's conference made the same point from the other side: AI makes bad data fail faster (per The Signal). Faster failure is a poor trade when you cannot see which cells are the shaky ones.

## What happens when the guess keeps travelling?

What happens when a guess leaves the contact list and lands in a deal review? Thibault Le Meur, who runs a GTM consultancy for founder-led European tech firms, built an agent that reads his open deals every Monday at 07:00 and answers three questions from buyer evidence alone: why do anything, why now, why us. Where there is no evidence, it writes EMPTY.

On three of his first four deals, "why us" came back EMPTY. Each buyer had told him what they wanted, and he had pitched something else. "An EMPTY is more useful to me than a good guess," he writes, and he adds that the "why us" line stung more than the two KILL verdicts did (per MRR Unlocked).

[IMAGE 3: quote-card.png, Quote card: An EMPTY is more useful to me than a good guess, attributed to Thibault Le Meur of Triscale]

What happens when the guess becomes the plan? Emilia Korczynska, co-founder of ZenABM, built her Q4 campaign on the assumption that 18 impressions would make an account engaged. The average landed at nine, and 302 accounts passed 18 against the 848 she expected. These are early numbers and hers, but pipeline stood at $8,411 against $100,000 planned (per The GTM Engineer Pulse).

Whoever said what you don't know can't hurt you clearly never built a quarter on an average nobody opened. The average summarised a distribution she had not yet looked inside.

What happens when the guess is a score that quietly decides who gets attention? Kris Billmaier, an executive vice president at Salesforce, describes scoring leads one to five, with the ones and twos at the bottom. When the company pointed an engagement agent at them, he says it drove over $100 million in pipeline in about eight months (per GTMnow, a self-reported figure from a vendor executive). A score is a guess with a number on it, and a number looks like a measurement.

In fairness, guessing is how anything gets built. monday.com's agents team shipped its voice agent at roughly 60% and learned on real leads, because you cannot simulate every customer interaction in advance (per GTM Engineering). Response time to inbound leads fell from about 25 hours to under two minutes, and the agent now books around 1,500 discovery calls a month, according to the account Alex Lindahl of Clay relays. A mammoth result, built on guesses.

But look at how they ran it. Every call and email was evaluated automatically against set criteria, and the team spent about twenty minutes of each morning on the results, because nobody can listen to 10,000 calls. The agent also started with a slice of the leads and earned more only when it matched or beat the humans on that slice. The guesses were labelled, and they had to pass a test before they were given more power.

## Observed, Inferred, Empty

Here is the habit, assembled from fragments I found across those newsletters. Give every fact your stack holds one of three labels, and let the label decide what an agent may do with it.

**Observed.** A person said or did it, and you can point to the date and the source. A buyer's words from Tuesday's call. A provider record. Observed facts may move a deal stage or send a message.

**Inferred.** A model or a rule guessed. Inferred facts may rank and draft. They may not send or move a stage. Town's growth team gives the same advice: start routines in draft mode and review before anything sends (per GTM Engineering). Kevin Payne, a GTM engineer at LawVu, grades systems as read only, draft only or write approved (per The GTM Engineer Pulse). I am grading facts.

**Empty.** Nobody knows yet. An empty field is a question for a human, and sometimes a finding, as the last section will show.

[IMAGE 4: framework.png, Three columns, Observed, Inferred and Empty, showing what an agent may and may not do with each]

## Observed is not the same as true

A label is only as good as the check behind it, and the sources are candid about where Observed goes wrong. Le Meur found that Fathom, the call recorder his agent depends on, sometimes mixed up who said what and filed a buyer's lines under his own name. His advice is to check the quotes behind any KILL against the call before acting (per MRR Unlocked).

Aviv Canaani, CRO and CMO at Datarails, checks brand attribution four ways: HubSpot, an open form question on the site, the sales rep asking live, and mentions in recorded calls. The four often disagree. Someone tagged as "Google" may tell the account executive they see Datarails on TikTok all the time (per GTMnow). Four imperfect observations that disagree are worth more than one that looks tidy.

Doug Bell applies the same discipline to brand. In his AI reputation scorecard, a company whose only citations come from its own website is capped at a score of 3, because the model has read only your brochure and nobody else has vouched for you. He also records what a model remembers separately from what it finds by searching, and never averages the two (per Cannonball GTM). Observed needs a source that is not you.

## How a guess earns a promotion

Labels would be a filing exercise if nothing ever moved between them. The useful part is the promotion rule, and the sources offer three versions of it.

Le Meur's monthly learning loop reads four weeks of deal reviews, calls and replies, and proposes an edit to one of his seven GTM files only when three different buyers have said the same thing.

In its first run, four buyers had asked for someone to do the work for them, so the loop proposed a new kind of buyer in his ICP file. It wrote the proposal down and left the file alone, because whether the edit goes in is his call (per MRR Unlocked). One buyer is an anecdote. Three is a pattern, and a person still signs it off.

Melissa Kwan, co-founder of eWebinar, treated her new positioning as a hypothesis until real prospects had tested it. When her homepage was about 90% there, she stopped and sent her COO to a conference to try the wording on people.

"Automated webinar software" made prospects ask what it meant. "On-demand video software with chat" was understood at once (per Growth Unhinged). Afterwards she reports time on the website up 50% and a first enterprise deal at $40,000 a year, against an average lifetime value of $2,650, both her own figures.

Ricardo Oliveira, a Director of GTM at SCAI in Brazil, runs 28 single-job agents and lets none of them grade its own work. His grader once docked an ideal customer profile for nine rows that were honestly labelled as guesses, so he rewrote the rubric until a labelled hypothesis cost nothing (per The GTM Engineer Pulse, self-reported). This is the design point that matters most. If admitting a guess is penalised, your team will stop admitting them, and the column you built becomes decoration.

## Where monday and Monk part ways

George Kurdin, CEO of Monk, which automates accounts receivable, says precision and security come first in finance, so his team built its own evals, guardrails and tests for the work that touches a customer's money (per GTMnow). That sits uneasily beside shipping at 60%.

The three labels settle it. The less reversible the action, the more Observed it demands.

A draft email to a web lead can run on Inferred, because a person reads it first and a bad one costs a few seconds. A payment chase cannot, because it moves a customer's money and a CFO will notice. Both are right for their own risk, and how much guesswork you can afford is contingent on what the action touches.

## Empty is where the opportunity lives

Treat Empty as a failure and your team will fill it with something plausible. Treat it as a result and it starts to pay.

Bain and Google asked 1,208 B2B buyers how they buy: 86% arrive with a list already in mind, about three names long, and 90% buy from that list (per Cannonball GTM).

Bell's team then ran 35 buyer questions through three AI assistants for 32 fleet software companies. Sixteen transport management vendors competed on the big category questions, and next to none were named on the question that can end a carrier's business: one mention, in one assistant (per Cannonball GTM). The empty cells were the most useful part of the audit. They marked a lane nobody had taken.

The same logic applies inside a company. Andreas, who runs Snowball Consult, does new work by hand on purpose, so that it does not run away from him (per The Signal). An Empty field is the signal to do exactly that: have the conversation, make the call, and let the answer arrive as Observed.

## What this means for your next quarter

Three actions you can take this week.

1. **Add a "source" field to the tables your agents write to.** Three values only: observed, inferred, empty. Start with contacts and deals, label new rows from today, and treat old rows as inferred until someone checks them. Expect it to take an afternoon.
2. **Change one rule, and protect the people who follow it.** Nothing inferred may send an email or change a deal stage. Let inferred rows draft, and let a person promote them. Make sure marking a guess costs nobody anything, or the field will quietly fill with Observed.
3. **Run Le Meur's check on your last five deals.** For each one, quote something the buyer said about why they would pick you, with the date, and check the quote against the recording. Write EMPTY where you cannot. Then hone your next call around whatever came back EMPTY.

## Sources and further reading

- [GTM Engineering & AI (Alex Lindahl): monday.com agents](https://newsletter.gtmengineering.ai/p/inside-mondays-agent-team-5-agents) and [Town's 15 tips](https://newsletter.gtmengineering.ai/p/town-hits-1b-6-personal-ai-use-cases)
- [The GTM Engineer Pulse #46 (Jared Waxman)](https://gtmengineerschool.substack.com/p/the-gtm-engineer-pulse-46)
- [MRR Unlocked (Alex), guest Thibault Le Meur](https://www.mrrunlocked.com/p/2-gtm-ai-agents-for-founder-led-sales)
- [Cannonball GTM (Doug Bell): Retrieved or Invisible](https://cannonballgtm.substack.com/p/retrieved-or-invisible-what-ai-thinks) and [The B2B Brand Reputation Scorecard](https://cannonballgtm.substack.com/p/the-b2b-brand-reputation-scorecard)
- [GTMnow Newsletter: Datarails](https://thegtmnewsletter.substack.com/p/gtm-210-outbound-to-inbound-strategy-aviv-canaani-datarails), [Monk](https://thegtmnewsletter.substack.com/p/gtm-209-ai-accounts-receivable-automation-george-kurdin-monk) and [33 GTM lessons](https://thegtmnewsletter.substack.com/p/33-gtm-lessons-founders-operators)
- [Growth Unhinged (Kyle Poyar): Melissa Kwan's positioning brain](https://www.growthunhinged.com/p/ai-brain-for-your-positioning)
- [The Signal (Brendan): 20 operators at Clay's conference](https://www.thesignal.club/p/lessons-from-interviewing-20-gtm-operators-at-sculpt)

A stack that cannot write EMPTY will write something else, and it will write it in the same confident font.

Which field in your CRM would change most if you had to attach a source to it?

#GTMEngineering #RevOps #AIAgents #B2BGrowth #FounderLedSales #DataQuality #CRM
