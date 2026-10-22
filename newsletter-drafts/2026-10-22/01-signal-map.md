# 01 Signal map

**DRAFT: pending Remmy review**
Run date: 22 October 2026. Window: `label:GTM-Newsletters newer_than:7d` (worked first time; 23 threads found; earliest email read is dated 15 October).

## Newsletters that fed the issue

16 emails from 10 newsletters (15 read in full; the MKT1 issue was read only to the end of its first section because of its length).

| Newsletter | Author (as shown in the email) | Emails read | Subjects |
|---|---|---|---|
| GTM Engineering & AI (Clay) | Alex Lindahl | 3 | monday.com agents (21 Oct); Town $1B and 15 tips (19 Oct); 5 big AI GTM ideas (16 Oct) |
| GTMnow Newsletter (GTMfund) | Sophie Buonassisi and team | 3 | Datarails (21 Oct); Monk (18 Oct); 33 GTM lessons (16 Oct) |
| Cannonball GTM | Doug Bell | 3 | Retrieved or Invisible (20 Oct); Brand Reputation Scorecard (16 Oct); Cannonball GTM Kit (15 Oct) |
| The GTM Engineer Pulse #46 | Jared (Jared Waxman, inferred from the issue text) | 1 | 21 Oct |
| GTM Weekly (Work-Bench) | Work-Bench team | 1 | #31 DTC ads playbook (21 Oct) |
| Growth Unhinged | Kyle Poyar, guest Melissa Kwan | 1 | AI brain for positioning (21 Oct) |
| MKT1 Newsletter | Author not visible in the part I read | 1 | 1,100+ marketing job posts (19 Oct) |
| MRR Unlocked (sender: startupbusinesstips) | Alex, guest Thibault Le Meur | 1 | The 2 GTM AI agents for founder-led teams (18 Oct) |
| The Signal | Brendan | 1 | 20 operators at Clay's Sculpt conference (17 Oct) |
| GTM Strategist | Anze | 1 | Animated LinkedIn infographics (16 Oct) |

Skipped (7 threads): Apollo promotional email; four Substack system notifications (a calendar invite, a recommendation, a "live now" alert, a Notes digest); two personal vendor threads (Pancake) that carry the label only because you replied to them. Nothing was sent, labelled, archived or deleted.

## Consensus themes (three or more newsletters)

1. **AI amplifies whatever data and definitions sit underneath it.** The Signal ("data hygiene still decides everything"), GTMnow 33 lessons (fix data before you bolt on AI), GTM Engineering/Town (define your ICP and clean data before automating), GTM Engineer Pulse (averages over things nobody opened), Growth Unhinged (the brain is only as good as its inputs). Five newsletters.
2. **Agents should run in draft or supervised mode, with evals.** GTM Engineering/monday (automated evaluation of every call and email), GTM Engineering/Town (start in draft mode), GTMnow/Monk (own evals, guardrails and tests), Pulse (read-only, draft-only, write-approved boundaries), MRR Unlocked (agent must quote evidence). Four newsletters.
3. **A shared "context layer" or single source of truth.** Growth Unhinged, The Signal (five interviewees named it), Pulse (Laurens Nys, Lindsay Rothlisberger), GTM Engineering (Ramp's Glass). Four newsletters.
4. **Human contact gains value as automation spreads.** GTMnow/Monk (in-person workshops), GTMnow 33 lessons (on site with customers), The Signal, Datarails (brand with a human voice). Four newsletters.

## Underrated idea (one newsletter only)

**The asterisk.** Cannonball GTM caps any brand's AI reputation score at 3 when its only citations are its own website, "the model reading your brochure, not the market vouching for you". It is a provenance rule for brand: a claim does not count until someone other than you has made it. Nobody else treats the source of a fact as a scoring input.

## Contradiction

**monday.com versus Monk on how much error to tolerate.** GTM Engineering reports monday's agents team shipped at roughly 60% and learned on real leads. GTMnow reports Monk's CEO saying precision and security are "tier zero" for anything touching a customer's money, so they built their own evals and guardrails first. Both are right for their own risk. Neither newsletter says how to choose.

Smaller contradiction: Datarails gives its VP of Brand no revenue KPIs, while the Pulse and MRR Unlocked insist on writing down what you count and evidencing every verdict.

## Three candidate angles

1. **Grade every fact as Observed, Inferred or Empty, and let the grade decide what an agent may do.** Reader payoff: a founder can stop an agent from moving deals or emailing prospects on guesses, in one afternoon.
2. **Brand is the shortlist: audit what AI models remember about your category's pain.** Reader payoff: a repeatable 35 question audit. (Weak for me: the method is paywalled and one newsletter owns it.)
3. **Founders should run a weekly agent deal review that quotes buyers.** Reader payoff: a Monday ritual. (Narrower, and it is one newsletter's guide.)

## Chosen angle

Angle 1. It sits underneath consensus themes 1 and 2, it resolves the monday versus Monk contradiction (permission scales with evidence and reversibility), and no source states it: each newsletter has a fragment (Mount's labels, Le Meur's EMPTY, Payne's write boundaries, Bell's asterisk, Town's draft mode) but nobody joins them into one rule.

## Stress test (argued against my own angle)

- *"Fix your data first is on every feed."* True, and a founder will nod and do nothing. The new point is that cleaning is endless and labelling is cheap: you do not need perfect data, you need to know which cells are guesses. That is a different action with a different owner.
- *"Reps will ignore a label."* Likely, if the label decorates. So the draft makes the label gate behaviour: inferred rows cannot send, spend or move a stage.
- *"This is admin."* Three values, one field, start with the tables agents write to.
- *"Would a founder change a decision?"* Yes: switch off auto-send on inferred contacts, stop agents promoting deal stages, and run a five deal evidence check this week.
- Verdict: the angle survives, but the draft must lead with the permission rule, not with "label your data".
