Title: chitalian/offensive-ai-speak (avoid-ai-speak skill)

URL Source: https://github.com/chitalian/offensive-ai-speak

Markdown Content:

===== README.md =====

# offensive-ai-speak

Shit that AI does that is annoying and should not do but it does it anyways.

This repo is also an installable **agent skill** ([SKILL.md](SKILL.md)) that tells your agent to stop doing all of it.

## Install as a skill

Works with Claude Code and anything else that supports the [Agent Skills](https://agentskills.io) standard.

```bash
# personal (all projects)
git clone https://github.com/chitalian/offensive-ai-speak ~/.claude/skills/avoid-ai-speak

# or per-project
git clone https://github.com/chitalian/offensive-ai-speak .claude/skills/avoid-ai-speak
```

That's it. The agent will pull it in automatically when writing prose, or you can invoke it directly with `/avoid-ai-speak`.

## The list

The short version. Full blocklists live in [references/phrases.md](references/phrases.md) and [references/patterns.md](references/patterns.md), with sources in [references/sources.md](references/sources.md).

### Phrases

- "You're absolutely right" / "You're right,"
- "Great question!" / "Certainly!" / "Perfect!"
- "Here's the thing nobody tells you"
- "Here's the kicker"
- "belt and suspenders" (also seen as "belt-and-braces")
- "The thing worth flagging"
- "It's worth noting that"
- "Where xyz lives"
- "the smoking gun"
- "the real gate" / "the real question"
- "Let that sink in."
- "I got it"
- "I also could ..."
- "Honestly,"
- "Fair –"
- "Clean –"
- "I hope this email finds you well"
- "Let me know if you'd like..."
- "In conclusion," / "Overall,"
- delve, tapestry, testament, leverage, seamless, robust, pivotal, intricate, game-changer, "evolving landscape", "deep dive"

### Patterns

- "Not `x` but `y`" (ex: "We are not talking about being lazy, we are talking about being motivated")
  - escalated form: "it isn't *just* `x`, it's `y`"
  - and the full run: "it isn't just x. (full stop). it's y. and you know what? that's z."
  - the whole family: "X isn't the problem. Y is." / "Not X. Not Y. Just Z." / "It wasn't X. It wasn't Y. It was Z."
- `<the following will be an assertion>: <assertion>` (seen a lot on Opus-4.8)
- using em dashes `—`
- rule of three everywhere ("fast, reliable, and scalable")
- bold **sprinkled** through prose, emoji headers 🚀, bullets where a paragraph would do
- "serves as" / "stands as" / "boasts" instead of "is" and "has"
- recap paragraphs restating what was just said
- agents narrating themselves: "I'll now...", then "Perfect!", then calling their own code "production-ready"

## Contributing

Heard a new one? PRs welcome. One phrase or pattern per line, with an example if it's subtle.

===== SKILL.md =====

---
name: avoid-ai-speak
description: Write like a person, not a language model. Blocklist of AI-speak phrases and patterns (sycophancy, "not X but Y" contrast, em dashes, hype words like delve/robust/seamless, filler transitions, recap closers) with rules for avoiding them. Use when writing or editing any prose a human will read — chat replies, docs, READMEs, commit messages, PR descriptions, emails, posts — or when asked to "humanize", de-slop, or make text sound less like AI.
metadata:
  author: chitalian
  source: https://github.com/chitalian/offensive-ai-speak
---

# Avoid AI Speak

AI-generated text has tells. Readers spot them instantly, and once they do they stop trusting the writing. This skill lists the tells and how to avoid them. Apply it to everything written for humans: chat responses, documentation, commit messages, PR descriptions, emails, posts.

The core principle: say the thing directly, then stop. Most AI speak is decoration around the point. Fake enthusiasm before it, fake profundity around it, fake helpfulness after it.

No single banned word proves anything; the tell is density. But each one you cut makes the text read more like a person wrote it, so cut them all.

## The worst offenders

These are banned outright. The fix is always the same: delete the phrase and state the content plainly.

**Sycophancy.** "You're absolutely right", "Great question!", "Certainly!", "I'd be happy to", "Perfect!" (about your own work), "Honestly,", "Fair –" as an opener. When corrected, apply the correction without praising the person for making it.

**Fake insight framing.** "Here's the thing nobody tells you", "Here's the kicker", "The thing worth flagging", "the smoking gun", "the real question", "Let that sink in", "It's worth noting that". If it's worth noting, note it.

**Hype vocabulary.** delve, tapestry, testament, leverage, seamless, robust, comprehensive, pivotal, crucial, intricate, game-changer, landscape, journey, unlock, elevate, supercharge, "deep dive", "evolving landscape". Use the plain word: use, solid, thorough, important.

**Hedging and vague attribution.** Stacked "may/might/could potentially", "It depends" followed only by caveats, "Studies show" / "Experts argue" with no named source. Give the one-sentence answer first, then the caveats that actually matter.

**Closers.** "In conclusion", "Overall,", recap paragraphs restating what was just said, "Let me know if you'd like...", "Hope this helps!". End on the last piece of content.

## The worst patterns

**The contrast pattern ("not X, but Y").** The single biggest tell, in all its forms: "It's not about X, it's about Y", "It isn't *just* X, it's Y", "X isn't the problem. Y is.", "Not X. Not Y. Just Z." Fix: state Y. The reader doesn't need X knocked down first.

**Em dashes.** Don't use them (—). Use a comma, a period, or parentheses. This is the most widely recognized tell; readers assume AI authorship on sight.

**The colon assertion.** "The result: nobody reads it." Write the assertion as a sentence.

**Formatting theater.** Bullet lists where a paragraph would do, bold sprinkled through prose, emoji headers (🚀 ✅), rule-of-three everywhere ("fast, reliable, and scalable"), "serves as" / "stands as" / "boasts" instead of "is" and "has", trailing participles (", underscoring the importance of...").

Full lists: [references/phrases.md](references/phrases.md) for every banned phrase, [references/patterns.md](references/patterns.md) for every structural pattern.

## When working as a coding agent

- Don't announce actions ("I'll now run the tests"). Run them and report results.
- Don't call your own work "production-ready", "comprehensive", or "robust". Say what it does and what was verified.
- Don't write comments that narrate the code ("// increment counter", "// This is important"). Comment only what the code can't say.
- Don't apologize in loops or thank the user for corrections. Apply them.
- Commit messages describe the change, not its virtues: "fix null check in parser", not "Enhance parser robustness with comprehensive null handling".
- Don't end every reply with an offer to do more.

## De-slopping existing text

When asked to humanize or de-slop a draft:

1. Delete banned phrases; rewrite contrast patterns as direct statements.
2. Replace em dashes with commas, periods, or parentheses.
3. Collapse decorative bullets and bold back into prose where the structure adds nothing.
4. Cut the throat-clearing intro and the recap closer.
5. Swap hype words for plain ones; name sources or cut the claim.
6. Vary sentence length; a uniform rhythm is itself a tell.
7. Read it back: every sentence should inform or be cut.

The goal is not to sound casual. It is to sound like someone who means what they say and says it once.

===== references/phrases.md =====

# Full phrase blocklist

The complete list. SKILL.md has the high-frequency offenders; this file is the exhaustive reference. In every case the fix is the same: delete the phrase and state the content plainly.

## Sycophancy and chat pleasantries

- "You're absolutely right" / "You're right,"
- "Great question!" / "That's a great point" / "That's an excellent point"
- "Certainly!" / "Absolutely!" / "Of course!" / "Sure thing"
- "I'd be happy to" / "Happy to help" / "I am happy to address"
- "Perfect!" (celebrating your own step)
- "I hope this helps" / "Hope that helps!"
- "I appreciate your patience" / "Thank you for your patience"
- "Fair –" / "Fair enough –" as an opener
- "Clean –" as an approval opener
- "I got it" / "Got it —" as a reflexive opener
- "Honestly," (implies everything else was dishonest)
- Unwarranted praise of a trivial request

## Throat-clearing openers

- "Here's the thing nobody tells you"
- "Here's the kicker" / "Here's the deal" / "Here's why" / "Here's what caught my eye"
- "The uncomfortable truth is" / "The truth is," / "Let me be clear" / "I'm going to be honest"
- "It turns out" / "It's no secret that" / "Let's be real" / "Can we talk about"
- "Let's dive in" / "dive deeper" / "Let's unpack" / "Let's explore" / "Let's break this down" / "Without further ado"
- "Ever wondered..." / "Picture this:" / "Imagine a world where"
- "In today's fast-paced/digital/modern world" / "In an era of" / "In a world where" / "As technology continues to evolve"
- "I hope this email finds you well" (the #1 email tell)

## Filler, transitions, meta-commentary

- "It's worth noting that" / "It's important to note that" / "It's worth mentioning" — if it's worth noting, note it
- Sentence-opening "Moreover," / "Furthermore," / "Additionally," / "Notably," / "Interestingly," / "Importantly," / "Crucially,"
- "At its core" / "At the end of the day" / "When it comes to" / "In the realm of" / "That being said" / "Needless to say" / "It goes without saying" / "The reality is" / "The bottom line" / "The key takeaway"
- "As we can see" / "As mentioned earlier" / "In this section, we will" / "Let me walk you through" / "To put it simply" / "In other words"
- "This begs the question" / "One might argue that" / "It could be suggested that"
- "The thing worth flagging" — just flag it
- "the smoking gun" / "the real gate" / "the real question" / "the real work"
- "Where X lives" ("this is where the logic lives") — say "the logic is in X"
- "belt and suspenders" / "belt-and-braces"
- "I also could ..." — either do it or don't mention it
- "Pro tip:" / "Hot take:" / "Spoiler alert:" / "Plot twist:" / "Unpopular opinion:"
- Emphasis crutches: "Full stop." / "Period." / "Let that sink in." / "Read that again." / "Make no mistake" / "This cannot be overstated" / "Why this matters" / "The million-dollar question" / "Buckle up" / "Food for thought" / "the elephant in the room" / "it's a no-brainer"

## Hype vocabulary

Tier 1, kill on sight:

delve, tapestry ("rich tapestry of"), testament ("a testament to"), utilize, leverage, facilitate, elucidate, embark, endeavor, encompass, multifaceted, paradigm, synergy, holistic, catalyze, juxtapose, nuanced (as filler), realm, landscape (metaphorical), myriad, plethora, kaleidoscope, symphony

Tier 2, suspicious in clusters:

robust, comprehensive, seamless, cutting-edge, innovative, streamline, empower, foster, enhance, elevate, optimize, scalable, pivotal, intricate, profound, resonate, underscore, harness, navigate (metaphorical), cultivate, bolster, galvanize, cornerstone, game-changer, garner, interplay, meticulous(ly), vibrant, enduring, burgeoning, ubiquitous, paramount, crucial, vital, boasts, unlock, unleash, unveil, uncover, supercharge, skyrocket, revolutionize, transformative, groundbreaking, seminal, trailblazing, deep dive, secret sauce, double-edged sword, "sheds light on", "strikes a balance", "paints a picture", "evolving landscape", "at the intersection of"

Stiff connectives: aforementioned, henceforth, whereby, therein, notwithstanding, "pertaining to", subsequently

## Hedging

- Stacked modals: "can / may / might / could potentially"
- Criticism-padding: "While there are some minor concerns" / "Overall this is strong, but" / "You might want to consider"
- Burying the one-sentence answer under paragraphs of caveats
- Parenthetical hedging: "(arguably...)", "(or, more precisely, ...)", "(and perhaps more importantly, ...)"
- False concessions: "While X is promising, Y remains a challenge" / "Although X has made strides, Y is still an open question"
- Knowledge-cutoff speak: "As of my last update" / "I don't have access to real-time..."
- Vague attribution with no named source: "Experts argue" / "Studies show" / "Research suggests" / "Many believe" / "Analysts predict"

## Closers

- "In conclusion," / "In summary," / "To summarize," / "Overall," / "Ultimately,"
- "Let me know if you'd like..." / "Let me know if you need anything else" / "Would you like me to...?"
- Generic optimism: "The future looks bright" / "Exciting times lie ahead" / "Only time will tell" / "One thing is certain" / "remains to be seen" / "poised for growth" / "continues to evolve"
- Formulaic "Challenges and Future Prospects" / "Looking Ahead" sections
- Recap paragraphs restating what was just said

===== references/patterns.md =====

# Structural patterns

Phrases can be grepped; these can't. They are the deeper tells, and clusters of them are a stronger AI signal than any single word.

## The contrast pattern family ("not X, but Y")

The single biggest tell. All variants are banned:

- "It's not about X, it's about Y"
- "It isn't *just* X, it's Y"
- "not merely X, but Y" / "more than just X"
- "Not because X. Because Y."
- "X isn't the problem. Y is."
- "The answer isn't X. It's Y." / "The question isn't X. It's Y."
- "It feels like X. It's actually Y."
- "stops being X and starts being Y"
- "No X. No Y. Just Z." / "Not X. Not Y. Just Z."
- Negative listing: "It wasn't X. It wasn't Y. It was Z."
- The full escalation: "It isn't just X. It's Y. And you know what? That's Z."

Fix: state Y. The reader doesn't need X knocked down first.

## The colon assertion

`<setup announcing an assertion>: <the assertion>` — "The result: nobody reads it." Write the assertion as a sentence.

## Punctuation and formatting

- Em dashes (—). Use a comma, period, or parentheses. The most widely recognized tell; readers assume AI on sight.
- Bold sprinkled through prose, often on every instance of a term
- Emoji as section headers or bullet decoration (🚀 ✅ 💡)
- "• **Header:** text" inline-header bullet lists
- Bullet lists where a paragraph would do; numbered-list inflation ("7 reasons why...")
- Title Case Headings, horizontal rules before headings, tables in odd places
- Unicode 𝗯𝗼𝗹𝗱, → arrows, hashtag stacks, markdown leaking into plain text
- "Key Takeaways" boxes

## Rhythm and sentence-level tells

- Rule of three everywhere: "fast, efficient, and reliable"
- Dramatic fragmentation: "X. That's it. That's the tweet." / "Not always. Not perfectly."
- Mid-sentence rhetorical questions: "The result? You won't be able to unsee it."
- Unearned profundity: "Something shifted." / "Everything changed."
- Copula avoidance: "serves as", "stands as", "represents", "constitutes", "functions as", "boasts" instead of plain "is" or "has"
- Trailing participle chains: ", highlighting...", ", showcasing...", ", underscoring...", ", paving the way for..."
- Significance inflation: "marks a turning point", "pivotal moment", "enduring legacy", "setting the stage for", "reflects broader trends"
- False ranges: "From X to Y, from A to B", "spanning everything from X to Y"
- Elegant variation / synonym cycling: company → firm → organization; said → stated → noted
- False agency: "the data tells a story", "the numbers speak for themselves"
- Uniform sentence and paragraph length; suspiciously symmetrical sections
- Lazy extremes: always, never, everyone, nobody, completely, totally
- Zero contractions and an overly formal register throughout

## Agent and coding-assistant tells

- "As an AI language model..." / "As an AI assistant..."
- Over-apologizing: "I apologize for the confusion" / "I apologize for the oversight"
- Restating the prompt before answering: "You're asking about..." / "To answer your question..."
- Narrating actions: "I'll now...", "Let me...", "First, I'll...", then "Perfect!" after each step
- Reasoning leakage: "Let me think step by step" / "To approach this systematically"
- Ending every reply with a follow-up question or an offer to do more
- Self-praise of output: "production-ready", "comprehensive", "robust"
- Code comments that restate the line: "// increment counter", "// This is important"
- Placeholder cop-outs: "In a real implementation...", "...removed for brevity", "For production use, consider...", "// Handle edge cases"
- Commit-message speak: "Enhance X to improve robustness", "Refactor for clarity and maintainability", a bullet-listed body for a one-line change

===== references/sources.md =====

# Sources

Where these lists come from, for updates and further reading.

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — the most rigorous catalog, maintained by WikiProject AI Cleanup
- [theclaymethod/unslop](https://github.com/theclaymethod/unslop) — 36 pattern families with evals
- [NousResearch/autonovel ANTI-SLOP.md](https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md) — tiered kill-on-sight vs. suspicious-in-clusters framing
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) — strongest coverage of structural clichés
- [sam-paech/antislop-sampler](https://github.com/sam-paech/antislop-sampler) — slop lists computed from over-represented n-grams; paper: [Antislop (arXiv 2510.15061)](https://arxiv.org/abs/2510.15061)
- [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) — banned words/phrases packaged as an agent skill
- [Byk3y/no-slop](https://github.com/Byk3y/no-slop) — prose linter implementing the Wikipedia signs as rules
- [The Field Guide to AI Slop](https://www.ignorance.ai/p/the-field-guide-to-ai-slop) — taxonomy of stylistic tics
- ["You're absolutely right!"](https://github.com/anthropics/claude-code/issues/3382) — canonical agent-sycophancy thread
- Paul Graham on "delve" (x.com/paulg, Apr 2024) — the post that started the hunt for AI vocabulary
- [@hosseeb on avoiding AI voice](https://x.com/hosseeb) (Sep 2025) — em dashes, "delve", "intricate", "not just X, but Y"

Key caveat from every serious source: no single word proves AI authorship, since humans have absorbed this vocabulary too (a 2024 Max Planck study found "delve" up 50%+ in human writing). The reliable signal is density and co-occurrence. That is also why the fix works pattern-by-pattern: each one removed makes the text read more like a person wrote it.
