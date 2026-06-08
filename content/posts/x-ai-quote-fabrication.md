---
title: "Anthropic Engineer or Quote Fabrication? An Open Investigation"
date: 2026-06-07T00:50:00+00:00
unlisted: true
tags: ["hot takes", "investigation", "ai-conferences"]
toc: true
description: "A 29-minute video on X claims to be a real Anthropic engineer giving a candid talk. The quote is good. The transcript says otherwise. This is an open investigation into who posted it and why."
---

> **Status: live, ongoing.** The transcript below is a significant finding, but the investigation is not closed. Who is "James Brady"? Why was this posted? Are there more of these? Last updated: 2026-06-08.

I keep seeing videos on X attributed to "An Anthropic engineer" or "An OpenAI researcher" giving a 20–30 minute talk about agent reliability, prompt injection, or some other sharp operational topic. The quotes that come out of them are perfect. They sound like the inside view. They are also extremely shareable.

Last week, one of these videos showed up in my feed again. It had 29 minutes of content. The opening line was the one I quoted in [Stop Reading What Your Coding Agent Says](https://blog.without.hosting/posts/backspine-dont-read-agent-text/):

> "Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does."

The quote is good. *Really* good. The "we measured it" half is what makes it land. It is exactly the kind of line a senior engineer at a frontier lab would say if they had actually seen the failure data.

I tried to verify it. I couldn't. This post is the open investigation.

## The case

The video is [posted on X by @0x_rody](https://x.com/0x_rody/status/2063318596202242171). It is attributed in the tweet text to "Anthropic engineer James Brady." The 29 minutes is a single Twitter-native upload. The two links in the tweet's body both resolve back to the same status — there is no separate YouTube upload, no Anthropic engineering blog post, no conference page, no LinkedIn announcement, no GitHub repo, no LinkedIn profile for a James Brady at Anthropic that surfaces in search. Just the tweet, the video, and the quote.

**The trail ends at the tweet.** That should be a yellow flag for any reader, and a red flag for any writer who would put it in their own post without flagging the source. I almost did exactly that.

## What I found so far

### 1. @0x_rody is not an Anthropic employee

Pulling the X profile metadata for the poster:

- **Handle:** `@0x_rody`
- **Name:** rody
- **Bio:** "AI tools analyst | Code & consciousness | @zscdao"
- **Location:** San Diego, CA
- **Account age:** joined April 2021 (5 years old)
- **Posts:** 158 over 5 years — roughly 2–3 tweets per month
- **Followers:** 1,283 — small account
- **Following:** 51
- **Verified:** false (X Premium)

There is no Anthropic affiliation in the bio. The account is not institutional. "AI tools analyst" is a self-description; nothing on the profile suggests employment at any lab. "Code & consciousness" is a tagline that points at a philosophical / personal-brand register, not a corporate one.

The 1,283-follower / 1,240-likes-per-tweet ratio on the Brady post is a separate anomaly: this small account pulled a 1,000% engagement spike on a single tweet. That is a structural signal worth holding onto.

### 2. @0x_rody is part of a Polymarket DAO

The bio cross-links to `@zscdao`, a separate X account:

- **Handle:** `@zscdao`
- **Name:** zerosupercycle
- **Bio:** "ZSC DAO is an organization building tools & community resources to bring Polymarket into the everyday lexicon."
- **Location:** Polymarket

Polymarket is a crypto prediction market. ZSC DAO is a community that builds tooling around it. So the source of the "Anthropic engineer" quote is *not* in the AI-lab orbit — it is in the **crypto prediction-market DAO** orbit, with an AI-tools side interest.

The non-obvious part: prediction-market DAOs have a strong incentive to publish content that the AI Twitter audience finds credible, because they sell picks, signals, and tools to that audience. An "Anthropic engineer says X" pull-quote travels far in that audience.

I am not accusing anyone of anything. I am naming a structural fit: the people who would benefit most from a sharp AI quote going viral are the people whose day job is monetizing AI Twitter's attention. That is rody's orbit, and it is a *coincidence* of incentives, not necessarily a conspiracy. But the fit is real — and it is the leading hypothesis for *why* this was posted.

### 3. The video is a quote-tweet of rody's *own* article

The first link inside the Brady tweet redirects to a **Quote Tweet** of rody's own X article. The full text:

> "Anthropic engineer James Brady:
> 'Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does.'
> In 29 minutes, he walks through the verification stack he built and the patterns the Claude Code team adopted to keep agents honest at scale. Watch the full talk, then save the config below!"

The post being quoted is rody's own article, posted **1 hour 32 minutes earlier** on the same day (2026-06-06), titled:

> "How to Make Claude Code Stop Making Stuff Up When It Doesn't Know (Exact Setup Inside)"

The article opens:

> "Claude Code lies to your face every day. Made-up functions, fake imports, 'tests pass' when nothing ran. The fix is a 4-layer setup that makes lying expensive."

These two pieces of content are the *same thesis*, in two formats. The article is rody's own Claude Code tutorial with a "4-layer honesty setup" (CLAUDE.md rules + verification layers). The tweet-with-video is the *same content* — but the pull-quote is attributed to "Anthropic engineer James Brady."

I do not have a final interpretation of what this means. I have three live hypotheses:

1. **The "James Brady" in the video is rody**, using a pseudonym or persona, dramatizing his own take. The 29 minutes is the same content as the article, just spoken.
2. **The "James Brady" is a real Anthropic engineer** whose real internal talk rody is reposting — but if so, that talk does not exist on Anthropic's `/engineering` blog, on their `/events` page, on YouTube, or on any conference site I can find.
3. **The "James Brady" is fictional**, a stock persona used to dramatize a position. The video is AI-generated and the attribution is a fiction that the algorithm rewards.

### 4. There is no James Brady at Anthropic

- **Anthropic `/engineering` blog** — every post has an author byline. None is "James Brady."
- **Anthropic `/events` page** — no "James Brady" in any speaker list.
- **Web search** — Brave, DuckDuckGo, Bing, and Google all return only the Wikipedia article for **James Brady the White House Press Secretary** (shot in the 1981 Reagan assassination attempt; died 2014). *The most indexed James Brady in the world is a man who died 12 years before the tweet was posted.* A search for "James Brady" + "Anthropic" + "agent" returns zero.

The simplest explanation: there is no James Brady at Anthropic. The name is either fictional, a pseudonym, or borrowed from elsewhere.

### 5. Anthropic does publish on agent reliability — in a different register

While looking for Brady, I found the *real* Anthropic engineering content on the same theme. None of it sounds like the Brady quote, but it is the genuine artifact:

- **"How we contain Claude across products"** — the closest match to "verification stack." Talks about caps, blast radius, containment, not "agents lying."
- **"An update on recent Claude Code quality reports"** (April 2026) — Anthropic's own honest accounting of failure modes.
- **"Scaling Managed Agents: Decoupling the brain from the hands"** (April 2026) — real engineering post on agent architecture.
- **"Harness design for long-running application development"** (March 2026) — agent design from the inside.
- **"Trustworthy agents in practice"** (April 2026) — Anthropic's own post on agent reliability. It does not use the word "lies." It uses "misread users' intent," "act with unintended consequences," and "prompt injection."

The contrast matters. The Brady quote is **sharper and more quotable** than anything in Anthropic's own engineering blog. That is not evidence of fraud — it is evidence of stylization. Real engineering writing is hedged. The Brady quote is not hedged. That puts it in a different genre from Anthropic's own writing on the topic.

### 6. The transcript: the 29-minute video is not about "agents lying"

This is the finding that shifted the investigation. I pulled the audio from the video and transcribed it through Deepgram's Nova-2 model. The transcript is 5,095 words.

**The video is a talk by someone from Elicit — the AI research assistant — about ASHPL, their domain-specific language for agentic workflows.** It is not an Anthropic talk. It is not about a "verification stack." It is not by "James Brady."

The speaker walks through:

- Why Elicit chose a DSL over freeform agent architectures;
- The ASHPL language design: a Turing-incomplete, pure functional subset of Python with domain primitives for retrieving academic papers and clinical trials;
- The event-sourcing pattern that drives iterative plan-and-execute loops;
- A live demo generating a research landscape table about foundation models for biology;
- How memoization and content-addressable storage make full-program reinterpretation efficient.

The word "lie" does not appear anywhere in the transcript. Neither does "lying," "fabrication," "caught," or "verification stack." The closest the speaker gets is a remark about trust: the mechanism of how an output is produced matters, not just the output itself. That is a general point about process legibility, not a claim about measuring agent dishonesty in production.

The talk is clearly from a conference or meetup. The speaker says "Elicit" repeatedly. The slide deck references elicit.com. The vocabulary — "research landscape," "clinical trials," "academic papers," "systematic review" — is the vocabulary of scientific research tooling, not agent-safety engineering.

**This closes one lead: we now know what is in the 29-minute video.** It is a real talk by a real person at Elicit. The quote has been superimposed onto it. The attribution to "Anthropic engineer James Brady" is text that wraps around a completely different piece of content.

But this raises the next question: **where did the video come from?** Is it a repurposed conference talk? Was it downloaded, cropped, and paired with the fabricated quote by rody, or did rody get it from somewhere else? The Elicit employee whose talk this is might not even know their video is being used this way.

## The genre

[USER: write — your read on the "long insider video + sharp pull-quote" pattern. Why does the form keep working? You have been seeing this for a year, you said. I want your voice on what is in the water, not mine.]

## Open leads

These are the next threads. I am putting them here so I (or anyone else) can pick them up.

1. **More cases.** I have seen several of these. I need the receipts: handles, dates, quotes, screenshots. The case above is one clean example; the genre is the question, not the one.
2. ~~**What is in the 29-minute video?**~~ **Resolved.** The transcript is in. It is an Elicit talk about their ASHPL DSL. The quote does not appear in it.
3. **Rody's other posts.** 158 posts over 5 years on a 1,283-follower account. There is a publishing cadence here. Going through `with_replies` and `media` would tell me if rody does this *often* (i.e., this is a content pattern) or whether this is a one-off.
4. **zscdao / Polymarket.** Is ZSC DAO monetizing AI Twitter attention? If so, the incentive structure is the actual story, not rody himself.
5. **Where did the video come from?** The Elicit talk — was it from a public conference? A meetup? Was it downloaded from YouTube or a conference site and repurposed? Finding the original upload would confirm the mismatch and potentially identify the actual speaker.
6. **Other Polymarket-DAO-adjacent accounts.** Are prediction-market communities *systematically* seeding content into AI Twitter? If so, that is its own piece.

## What I am not claiming

I am not claiming the quote is wrong. The quote is probably *true as a description of agent behavior* — the part I quoted in [Stop Reading What Your Coding Agent Says](https://blog.without.hosting/posts/backspine-dont-read-agent-text/) holds up regardless of who said it, because the structural dynamic it describes is real.

What I am claiming, with evidence:

1. **The trail of attribution ends at rody's own article.** The tweet is a quote-tweet of rody's article. The "Anthropic engineer" voice and the "rody" voice are the same thesis in two formats.
2. **"James Brady" is not a person I can verify at Anthropic.** The only indexed James Brady in the world is a 20th-century press secretary.
3. **The quote does not exist in the video.** The transcript is in. It is an Elicit talk about DSL design. The two things share no content.
4. **The genre — "long insider video + sharp pull-quote attributed to a vague insider" — is a content pattern, not a series of one-offs.** The shape of the content is too consistent to be coincidence.

## What to do if you see one of these

[USER: write — your move when you see a sharp, attributed AI quote on X. Do you screenshot it, bookmark it, share it, verify it? What is the right discipline? You were almost the next person to spread this one.]

---

*Last updated: 2026-06-08. Investigation in progress. Filing date for next update: when rody's other posts are reviewed, when the Elicit talk's original source is found, and when at least one additional case is documented.*