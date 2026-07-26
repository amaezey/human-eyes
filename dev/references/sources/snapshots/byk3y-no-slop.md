# no-slop

- **Canonical URL:** https://github.com/Byk3y/no-slop
- **Alternate access URLs:**
  - https://github.com/Byk3y/no-slop.git
  - https://github.com/Byk3y/no-slop/commit/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b
  - https://api.github.com/repos/Byk3y/no-slop/commits/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b
  - https://api.github.com/repos/Byk3y/no-slop/git/trees/43e4eb82fe0406d97cc2bc38963674463431ab5b?recursive=1
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/CONTRIBUTING.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/LICENSE
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/README.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/SKILL.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/agents/claude-code.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/agents/codex.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/agents/cursor.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/banned-vocabulary.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/examples/bad-examples.md
  - https://raw.githubusercontent.com/Byk3y/no-slop/98cd8fb016bf5c3467e646e23d7ce09234ec0b2b/examples/good-examples.md
- **Author / owner:** Francis / GitHub repository owner Byk3y
- **Publisher:** GitHub
- **Published:** Initial and reviewed commit authored and committed 2026-04-08T01:01:22Z
- **Retrieved:** 2026-07-15
- **Stable identifier:** commit 98cd8fb016bf5c3467e646e23d7ce09234ec0b2b
- **Version / revision:** `main` at commit `98cd8fb016bf5c3467e646e23d7ce09234ec0b2b`; root tree `43e4eb82fe0406d97cc2bc38963674463431ab5b`
- **Extraction method:** Full Git clone over HTTPS, full-history verification, GitHub commit and non-truncated recursive-tree API checks, commit-pinned raw-file verification, `git archive`, and byte-preserving UTF-8 concatenation of every tracked file
- **Full-text status:** complete
- **Access and transformation notes:** All 10 tracked files at the reviewed commit are reproduced below. They total 27,868 bytes, use mode 100644, decode as UTF-8, use LF line endings, and end in LF. Each commit-pinned raw file matched the clone byte for byte. No tracked file was omitted and no source byte, punctuation mark, or line ending was normalised. Markdown headings and four-backtick fences are snapshot wrappers, not source content.

## Commit metadata

- **Commit SHA:** `98cd8fb016bf5c3467e646e23d7ce09234ec0b2b`
- **Root tree SHA:** `43e4eb82fe0406d97cc2bc38963674463431ab5b`
- **Parents:** none, initial commit
- **Author:** `Francis <scenes_pineal.0d@icloud.com>`, 2026-04-08T01:01:22Z
- **Committer:** `Francis <scenes_pineal.0d@icloud.com>`, 2026-04-08T01:01:22Z
- **Signature verification:** unsigned
- **Commit message:**

````text
Initial release: prose linter based on Wikipedia's Signs of AI Writing

13 rules, 40+ banned words, annotated before/after examples.
Multi-agent support for Claude Code, Cursor, and Codex CLI.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
````

## Recursive tree listing

The GitHub Git Trees response at the exact recursive-tree API URL above reported `truncated: false`. Columns are mode, object type, object SHA, byte size where applicable, and path.

````text
100644 blob fef5379afd6457b388b03c5050eec0ae7edd870f 1615 CONTRIBUTING.md
100644 blob ace24e58cf62bfe095c02d8844794bef83e393ca 1062 LICENSE
100644 blob c9ab6e3d8f90a2477d8c4c62716da6d83606918f 6182 README.md
100644 blob 1bf4749c82dd738f3fd21b559d59ee00464da8cd 4321 SKILL.md
040000 tree fac10a325dbedd1a60f0b7e06b0cbd532b534365 - agents
100644 blob c3da12487facc1c450d0527e2610a12054f1aa2e 611 agents/claude-code.md
100644 blob d565cfe1c92d7c4a6eb38ec13cc7bed4d7e1ede9 1569 agents/codex.md
100644 blob 920497fd0dbc8e80f9f503a74012fbe3b0125ef1 2151 agents/cursor.md
100644 blob 23fc50087708c8c19a5639c0896a95f67dc11765 2877 banned-vocabulary.md
040000 tree b33cc8648920e52e6723be5125b8e598c1338cc8 - examples
100644 blob 642c412a2f1a0dbd991c4ff26e77de965a3f0b5b 3982 examples/bad-examples.md
100644 blob 932a1125934256ad9cb0d7d7b152dbec86d7a2de 3498 examples/good-examples.md
````

## Full text

The following sections reproduce every tracked file at the reviewed commit. Source bytes inside each fence are unchanged.

### `CONTRIBUTING.md`

````text
# Contributing to no-slop

Thanks for helping make AI writing less detectable. Here's how to contribute.

## Adding banned words or phrases

1. Open `banned-vocabulary.md`
2. Add the word/phrase to the appropriate table
3. Include a plain alternative in the "Use instead" column
4. In your PR description, link to evidence — either the [Wikipedia article](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) or published research showing the word is overrepresented in AI text

Don't add words that are perfectly normal in human writing. The bar is: would a Wikipedia editor flag this as an AI tell?

## Adding examples

1. Add a "bad" example to `examples/bad-examples.md` with annotations for every AI pattern present
2. Add a matching "good" rewrite to `examples/good-examples.md` with a "Why this works" section
3. Examples should come from realistic contexts: project descriptions, emails, docs, blog posts, PR descriptions

## Adding rules

New rules should be backed by the Wikipedia article or equivalent evidence. Open an issue first to discuss before submitting a PR — this keeps the rule set focused.

## Adding agent support

If you use an AI tool that isn't covered in `agents/`, add a new file with install and usage instructions. Follow the format of the existing files.

## PR guidelines

- One rule, one example set, or one agent per PR
- Keep changes focused
- Test that your additions don't break existing SKILL.md formatting
- No promotional language in your PR description (practice what we preach)

## Code of conduct

Be direct, be helpful, don't waste people's time. That's it.
````

### `LICENSE`

````text
MIT License

Copyright (c) 2026 Byk3y

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

### `README.md`

````text
# no-slop

**A prose linter that catches AI writing patterns. Based on [Wikipedia's Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).**

[![GitHub stars](https://img.shields.io/github/stars/Byk3y/no-slop?style=social)](https://github.com/Byk3y/no-slop)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Works with: Claude Code](https://img.shields.io/badge/Claude_Code-compatible-blue)]()
[![Works with: Cursor](https://img.shields.io/badge/Cursor-compatible-blue)]()
[![Works with: Codex CLI](https://img.shields.io/badge/Codex_CLI-compatible-blue)]()

---

## Before and after

**AI slop:**

> React Query is a groundbreaking library that serves as a pivotal tool in the modern frontend landscape. It seamlessly handles data fetching, caching, and synchronization, showcasing a meticulous approach to state management. The library boasts a vibrant community and has garnered significant adoption, underscoring its enduring value in the ecosystem.

**After no-slop:**

> React Query handles data fetching, caching, and background sync for React apps. You describe what data you need, and it handles refetching, deduplication, and cache invalidation. The community is large — over 40k GitHub stars — and most major React codebases have adopted it.

Same information. No slop.

---

## What it catches

| # | Rule | What it stops |
|---|---|---|
| 1 | Banned vocabulary | 40+ words like "delve," "tapestry," "pivotal," "vibrant," "leverage" |
| 2 | Simple copulas | Replacing "is/has" with "serves as," "stands as," "boasts" |
| 3 | Promotional tone | "Groundbreaking," "revolutionary," marketing-speak in technical writing |
| 4 | Vague attributions | "Experts say," "industry reports suggest" with no named source |
| 5 | Structural formulas | Rule of three, "not just X but Y," challenges-and-prospects endings |
| 6 | Participle chains | "-ing" filler: "highlighting," "showcasing," "emphasizing" |
| 7 | Elegant variation | Swapping synonyms for the same thing across sentences |
| 8 | Overstating significance | "Marks a turning point," "leaves an indelible mark" |
| 9 | Em dash overuse | More than one per paragraph |
| 10 | Collaborative language | "Let's explore," "as we can see," "we will examine" |
| 11 | Knowledge-cutoff disclaimers | "As of my last update," apologizing for gaps |
| 12 | Formatting excess | Over-bolding, emoji, title-case headings, "key takeaways" |
| 13 | Human writing habits | Contractions, varied sentence length, specifics over adjectives |

Every rule is sourced from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup from observations of thousands of AI-generated texts.

---

## Install

### Claude Code (recommended)

```bash
# Clone into your skills directory
git clone https://github.com/Byk3y/no-slop.git ~/.claude/skills/no-slop
```

That's it. Claude Code auto-discovers skills in `~/.claude/skills/`. It will activate whenever you ask it to write prose.

You can also trigger it manually:

```
/no-slop
```

### Cursor

Copy the contents of [`agents/cursor.md`](agents/cursor.md) into your `.cursorrules` file at your project root.

### Codex CLI

See [`agents/codex.md`](agents/codex.md) for setup instructions.

---

## Usage

**Automatic**: Just ask your AI to write something — a blog post, email, PR description, documentation. The skill activates on its own for writing tasks.

**Manual**: Use `/no-slop` (Claude Code) to force-activate it when auto-detection doesn't kick in.

**What it does NOT activate for**: Code generation, short chat replies, commit messages. It only applies to prose.

---

## How it works

no-slop is a constraint skill, not a rewriter. It doesn't take your text and fix it after the fact. It teaches the AI what patterns to avoid *while writing*, so the first draft comes out clean.

The rules come from Wikipedia's article on signs of AI writing — a living document maintained by editors who review thousands of AI-generated texts. This isn't one person's opinion. It's a collaboratively maintained, evidence-based list of the patterns that give AI writing away.

### File structure

```
no-slop/
├── SKILL.md                # Core rules (13 constraints)
├── banned-vocabulary.md    # 40+ banned words with plain alternatives
├── examples/
│   ├── bad-examples.md     # Annotated AI-sounding text
│   └── good-examples.md    # Human-sounding rewrites
├── agents/
│   ├── claude-code.md      # Claude Code install guide
│   ├── cursor.md           # Cursor rules format
│   └── codex.md            # Codex CLI format
├── CONTRIBUTING.md
└── LICENSE
```

---

## Why no-slop?

| | no-slop | humanizer | anti-ai-slop-writing | avoid-ai-writing |
|---|---|---|---|---|
| Approach | Constraint (prevents slop) | Rewriter (fixes after) | Banned words | Tiered word replacement |
| Source | Wikipedia (evidence-based) | Wikipedia | Wikipedia + CMU | Mixed |
| Annotated examples | Yes (before/after per rule) | One example | No | One example |
| Conditional bans | Yes (context-aware) | No | No | No |
| Multi-agent | Claude Code, Cursor, Codex | Claude Code, OpenCode | 11+ agents | Claude Code, OpenClaw |

---

## Source

All rules are derived from **[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)**, a collaboratively edited reference maintained by [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup). The article documents patterns observed across thousands of AI-generated texts by Wikipedia editors.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

- New banned words need evidence (link to Wikipedia article or published research)
- New examples need annotations explaining what's wrong and why the rewrite is better
- PRs should be focused — one rule or one example set per PR

---

## Star this repo

If no-slop made your writing better, [give it a star](https://github.com/Byk3y/no-slop). It helps others find it.

---

## License

[MIT](LICENSE)
````

### `SKILL.md`

````text
---
name: no-slop
description: Avoid AI writing patterns when producing prose. Use when writing articles, blog posts, documentation, emails, proposals, reports, README content, PR descriptions, release notes, or any long-form text. Activates for drafting, composing, or writing tasks.
---

# no-slop — Anti-AI-Detection Rules

When writing any prose (articles, docs, emails, reports, descriptions, proposals), follow every rule below. These patterns are documented tells of AI-generated text. Violating even a few destroys credibility.

## 1. Banned vocabulary

Do NOT use any word or phrase listed in [banned-vocabulary.md](banned-vocabulary.md). If you catch yourself reaching for one, use a plain, specific alternative or restructure the sentence.

## 2. Use simple copulas

Use "is," "are," "was," "has," "had." Do not substitute with:
- "serves as," "stands as," "represents," "marks"
- "boasts," "features," "offers"
- "ventured into" instead of "tried" or "ran for"

Bad: "The library serves as a foundational component in the ecosystem."
Good: "The library is the base of the stack."

## 3. No promotional tone

Write like a journalist or engineer, not a marketer. Never hype. State facts and let them speak.

Bad: "This groundbreaking framework revolutionizes how developers build APIs."
Good: "This framework generates API clients from OpenAPI specs."

## 4. No vague attributions

Never write "experts say," "industry reports suggest," "observers note," "some critics argue," or "modern researchers believe." Either name the source or drop the claim.

## 5. No structural formulas

- **No rule of three**: Do not use three-adjective or three-phrase lists as a rhetorical device. Two or four is fine. Three in a row signals AI.
- **No "not just X, but Y"**: Drop the "not only... but also" and "it's not just... it's" constructions entirely.
- **No "challenges and future prospects"**: Never end a piece with a section about challenges faced and future outlook. If challenges matter, weave them into the body.

## 6. No present-participle chains

Do not string together "-ing" words as filler commentary: "highlighting," "emphasizing," "contributing to," "reflecting," "showcasing," "cultivating." These add no information. Replace with concrete verbs or cut entirely.

Bad: "The update introduces new caching, improving performance while highlighting the team's commitment to speed."
Good: "The update adds caching. Page loads dropped from 3s to 800ms."

## 7. No elegant variation

Do not swap synonyms for the same thing across sentences to avoid repetition. If you're talking about a "server," call it a "server" every time. Do not alternate between "the server," "the machine," "the node," "the instance" for style.

## 8. No overstating significance

Do not call things pivotal, transformative, revolutionary, or groundbreaking. Do not say something "marks a turning point" or "leaves an indelible mark." If it's important, show why with evidence — don't announce it.

## 9. Em dash discipline

Use em dashes sparingly — maximum one per paragraph, and only when parentheses or a comma won't work. AI text is riddled with em dashes.

## 10. No collaborative language

Never write "let's explore," "let us delve into," "we will examine," "as we can see." Write directly. The reader is reading, not exploring with you.

## 11. No knowledge-cutoff disclaimers

Never apologize for gaps, say "as of my last update," or speculate about missing information. Either state the fact or don't.

## 12. Formatting restraint

- Do not bold excessively. Bold a term once at most when introducing it.
- Do not use emoji unless the user explicitly asks.
- Do not use title case in headings beyond the first word and proper nouns (sentence case).
- Do not create "key takeaways" sections.

## 13. Write like a human

- Vary sentence length naturally. Mix short and long.
- Start some sentences with "But," "And," "So," or "Or."
- Use contractions (don't, isn't, can't) in informal contexts.
- Be specific over general. Numbers over adjectives. Evidence over claims.
- It's OK to be blunt, dry, or even terse. Humans are.

## Examples

For concrete before/after examples showing these rules applied, see [examples/bad-examples.md](examples/bad-examples.md) and [examples/good-examples.md](examples/good-examples.md).
````

### `agents/claude-code.md`

````text
# Claude Code

## Install

Clone this repo into your Claude Code skills directory:

```bash
git clone https://github.com/Byk3y/no-slop.git ~/.claude/skills/no-slop
```

Claude Code auto-discovers skills in `~/.claude/skills/`. No restart needed.

## Usage

**Automatic**: Ask Claude to write anything — blog posts, emails, docs, PR descriptions. The skill activates on its own when it detects a writing task.

**Manual**: Type `/no-slop` in the Claude Code prompt to force-activate it.

## Update

```bash
cd ~/.claude/skills/no-slop && git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/no-slop
```
````

### `agents/codex.md`

````text
# Codex CLI

## Install

Add the no-slop rules to your Codex system prompt. Create or edit your `AGENTS.md` or system instruction file:

### Option 1: Clone and reference

```bash
git clone https://github.com/Byk3y/no-slop.git ~/.no-slop
```

Then add to your Codex instructions:

```
When writing prose, follow the rules in ~/.no-slop/SKILL.md
```

### Option 2: Inline rules

Add the following to your Codex system prompt or `instructions.md`:

```
# no-slop rules for prose writing

When writing any prose (docs, emails, READMEs, PR descriptions):

1. BANNED WORDS: Never use: delve, tapestry, pivotal, vibrant, meticulous, landscape (metaphorical), testament, underscore, intricate, interplay, garner, bolster, foster, showcase, emphasize, crucial, enhance, leverage, utilize, facilitate, streamline, robust (in prose), seamless, holistic, synergy, paradigm, ecosystem (metaphorical), groundbreaking, renowned, profound, comprehensive.

2. COPULAS: Use "is/are/has." Not "serves as," "stands as," "boasts," "features."

3. NO STRUCTURAL FORMULAS: No rule-of-three. No "not only X but also Y." No "challenges and future prospects" endings.

4. NO PARTICIPLE CHAINS: Cut "-ing" filler words (highlighting, showcasing, emphasizing).

5. NO PROMOTIONAL TONE: State facts. No hype. No vague attributions.

6. NO COLLABORATIVE LANGUAGE: No "let's explore," "we will examine."

7. FORMATTING: Minimal bold. No emoji. Sentence-case headings.

8. WRITE LIKE A HUMAN: Vary sentence length. Use contractions. Be specific.
```

## Update

```bash
cd ~/.no-slop && git pull
```
````

### `agents/cursor.md`

````text
# Cursor

## Install

Copy the rules below into your `.cursorrules` file at the root of your project. If you already have a `.cursorrules` file, append these rules to the end.

## Rules

```
# no-slop — Anti-AI writing rules
# Source: https://github.com/Byk3y/no-slop

When writing prose (docs, emails, comments, READMEs, PR descriptions), follow these rules:

BANNED WORDS: Do not use: additionally, delve, tapestry, pivotal, vibrant, meticulous, landscape (metaphorical), testament, underscore, intricate, interplay, garner, bolster, foster, showcase, emphasize, enduring, crucial, enhance, highlighting, renowned, groundbreaking, profound, comprehensive, multifaceted, leverage, utilize, facilitate, encompasses, spearhead, harness, elevate, streamline, robust (in prose), seamless, holistic, synergy, paradigm, ecosystem (metaphorical).

BANNED PHRASES: Do not use: "marks a pivotal moment," "represents a significant shift," "indelible mark," "deeply rooted," "rich history," "nestled in," "boasts a," "serves as a," "stands as a," "not just X but Y," "despite its [positive], faces challenges," "let's explore," "in today's [landscape/world/era]," "at the heart of," "it is worth noting," "a testament to," "paving the way," "plays a crucial role," "in an era where," "the intersection of," "it remains to be seen."

COPULAS: Use "is," "are," "was," "has." Do not replace with "serves as," "stands as," "represents," "boasts," "features."

STRUCTURE: No rule-of-three patterns. No "not only X but also Y." No "challenges and future prospects" endings.

PARTICIPLES: Do not chain -ing words as filler: "highlighting," "showcasing," "emphasizing," "reflecting."

TONE: No promotional language. No vague attributions ("experts say"). No overstating significance. No collaborative language ("let's explore").

FORMATTING: Minimal bold. No emoji unless asked. Sentence-case headings. No "key takeaways" sections.

STYLE: Vary sentence length. Use contractions. Start sentences with "But," "And," "So" sometimes. Be specific — numbers over adjectives.
```

## Update

Re-copy the rules from the latest version of this file after pulling the repo.
````

### `banned-vocabulary.md`

````text
# Banned Vocabulary

These words and phrases are statistically overrepresented in AI-generated text. Do not use them. Plain alternatives are listed where helpful.

## High-Frequency AI Words

| Banned | Use Instead |
|---|---|
| additionally | also, and, (or just start the next sentence) |
| delve / delve into | look at, examine, dig into |
| tapestry | (drop it — almost never needed) |
| pivotal | important, key (sparingly) |
| vibrant | (be specific: busy, loud, colorful, active) |
| meticulous / meticulously | careful, thorough |
| landscape (metaphorical) | field, area, market, space |
| testament (to) | proof, evidence, sign |
| underscore | show, prove, reinforce |
| intricate / intricacies | complex, complicated, details |
| interplay | interaction, relationship |
| garner | get, earn, attract |
| bolster / bolstered | support, strengthen, back |
| foster / fostering | encourage, support, build |
| showcase / showcasing | show, display, demonstrate |
| emphasize / emphasizing | stress, point out |
| enduring | lasting, long-running |
| crucial | important, critical, necessary |
| enhance / enhancing | improve, boost |
| highlighting | (cut it — rewrite without) |
| renowned | well-known, famous |
| groundbreaking | new, novel, first |
| profound | deep, major, significant |
| comprehensive | full, complete, thorough |
| multifaceted | complex, varied |
| leverage (verb) | use |
| utilize | use |
| facilitate | help, enable, allow |
| encompasses | includes, covers |
| spearhead | lead, start |
| harness | use |
| elevate | raise, improve |
| streamline | simplify, speed up |
| robust | strong, solid, reliable |
| seamless / seamlessly | smooth, easy |
| holistic | complete, full, whole |
| synergy | (drop it) |
| paradigm | model, approach, pattern |
| ecosystem (metaphorical) | system, community, market |

## Banned Phrases

- "marks a pivotal moment"
- "represents a significant shift"
- "indelible mark"
- "deeply rooted"
- "rich history"
- "natural beauty"
- "nestled in"
- "boasts a"
- "serves as a"
- "stands as a"
- "not just X, but Y" / "not only X, but also Y"
- "it's not... it's..."
- "despite its [positive], [subject] faces challenges"
- "let's explore"
- "let us delve into"
- "in today's [landscape/world/era]"
- "at the heart of"
- "it is worth noting"
- "a testament to"
- "paving the way"
- "plays a crucial role"
- "in an era where"
- "the intersection of"
- "a beacon of"
- "sends a strong message"
- "it remains to be seen"

## Conditional Bans

These are fine in technical/code contexts but banned in prose:

| Word | OK in | Banned in |
|---|---|---|
| key | variable names, API keys | "key factor," "key player" |
| landscape | actual geography | "the AI landscape" |
| robust | engineering specs | "a robust approach to leadership" |
| seamless | UX descriptions with data | "a seamless experience" (vague) |
````

### `examples/bad-examples.md`

````text
# Bad Examples — AI Writing Patterns

Each example below contains multiple AI tells. The bracketed annotations explain what's wrong.

---

## Example 1: Project Description

> React Query is a groundbreaking library that serves as a pivotal tool in the modern frontend landscape. It seamlessly handles data fetching, caching, and synchronization, showcasing a meticulous approach to state management. The library boasts a vibrant community and has garnered significant adoption, underscoring its enduring value in the ecosystem. Not only does it simplify complex data flows, but it also fosters a more robust development experience.

**What's wrong:**
- "groundbreaking" — promotional, overstating significance
- "serves as a pivotal tool" — copula avoidance + banned word
- "modern frontend landscape" — banned metaphorical use of "landscape"
- "seamlessly" — banned word
- "showcasing a meticulous approach" — present-participle chain + banned words
- "boasts a vibrant community" — copula avoidance + banned words
- "garnered" — banned word
- "underscoring its enduring value" — present-participle chain + banned words
- "ecosystem" — banned metaphorical use
- "Not only... but it also" — banned structural formula
- "fosters a more robust" — banned words

---

## Example 2: Blog Post Intro

> In today's rapidly evolving technological landscape, artificial intelligence stands as a testament to human ingenuity. Let's delve into the intricate interplay between machine learning and natural language processing, highlighting how these groundbreaking technologies are paving the way for a more comprehensive understanding of human communication.

**What's wrong:**
- "In today's rapidly evolving technological landscape" — banned phrase
- "stands as a testament to" — copula avoidance + banned phrase
- "Let's delve into" — collaborative language + banned phrase
- "intricate interplay" — banned words
- "highlighting" — present-participle filler
- "groundbreaking" — banned word
- "paving the way" — banned phrase
- "comprehensive understanding" — banned word

---

## Example 3: Email Draft

> I wanted to reach out regarding the Q3 infrastructure initiative. The proposed migration represents a significant shift in our approach, and it's crucial that we leverage the full potential of our cloud ecosystem. Despite its numerous advantages, the project faces challenges related to legacy system compatibility. It remains to be seen how we'll navigate these intricacies, but I'm confident this will elevate our platform to new heights.

**What's wrong:**
- "represents a significant shift" — banned phrase
- "crucial" — banned word
- "leverage" — banned word
- "ecosystem" — banned metaphorical use
- "Despite its... faces challenges" — banned structural formula
- "It remains to be seen" — banned phrase
- "intricacies" — banned word
- "elevate our platform to new heights" — promotional + banned word

---

## Example 4: Documentation

> This module plays a crucial role in facilitating seamless communication between microservices. It encompasses a robust set of utilities, including message serialization, retry logic, and circuit breaking. The holistic design of the system underscores a meticulous commitment to reliability, fostering an environment where services can interact with minimal friction. Additionally, it utilizes advanced patterns to streamline error handling.

**What's wrong:**
- "plays a crucial role" — banned phrase
- "facilitating" — banned word
- "seamless" — banned word
- "encompasses" — banned word
- "robust" — banned word (prose context)
- Rule of three: "serialization, retry logic, and circuit breaking"
- "holistic" — banned word
- "underscores" — banned word
- "meticulous commitment" — banned word
- "fostering an environment" — banned word + vague
- "Additionally" — banned sentence starter
- "utilizes" — banned word (use "uses")
- "streamline" — banned word
````

### `examples/good-examples.md`

````text
# Good Examples — Human-Sounding Rewrites

Each example below is a rewrite of the corresponding bad example from [bad-examples.md](bad-examples.md).

---

## Example 1: Project Description

> React Query handles data fetching, caching, and background sync for React apps. You describe what data you need, and it handles refetching, deduplication, and cache invalidation. The community is large — over 40k GitHub stars — and most major React codebases have adopted it.

**Why this works:**
- Opens with what it does, not how important it is
- "handles" and "is" instead of "serves as" or "boasts"
- Specific number (40k stars) instead of "vibrant community"
- No promotional adjectives
- No "not only... but also"

---

## Example 2: Blog Post Intro

> Machine learning and NLP have converged over the past five years, mostly because transformer architectures turned out to work well for both. This post covers how that happened and what it means if you're building products that process text.

**Why this works:**
- No "in today's landscape" opener
- No "let's delve into"
- States the timeframe ("past five years") instead of vague "rapidly evolving"
- Says what the post will cover, directly
- Conversational but not chummy

---

## Example 3: Email Draft

> Quick note about the Q3 infrastructure migration. We're moving the main API cluster to the new cloud provider. The main risk is compatibility with the legacy auth system — it uses a session format the new platform doesn't support natively. I've outlined two workarounds in the attached doc. Can we discuss Thursday?

**Why this works:**
- Gets to the point immediately
- Names the specific risk instead of "faces challenges"
- No "represents a significant shift" or "crucial"
- Uses "uses" instead of "leverages" or "utilizes"
- Ends with a concrete action, not "it remains to be seen"
- Contractions ("we're," "doesn't," "I've") sound natural

---

## Example 4: Documentation

> This module handles communication between microservices. It serializes messages, retries failed calls with exponential backoff, and trips a circuit breaker after five consecutive failures. Errors are caught at the transport layer and returned as typed results — callers don't need try/catch blocks.

**Why this works:**
- "handles" instead of "plays a crucial role in facilitating"
- Lists what it actually does with specifics (exponential backoff, five failures)
- "is" and "are" as copulas
- No "additionally," no "holistic," no "robust"
- One em dash, used purposefully
- Technical detail instead of vague claims about "reliability"

---

## Example 5: PR Description (bonus)

**Bad:**
> This PR represents a significant enhancement to our authentication system. It leverages modern cryptographic patterns to foster a more robust security posture, showcasing our commitment to safeguarding user data. The changes encompass token validation, session management, and rate limiting, providing a comprehensive solution that elevates our platform's security to new heights.

**Good:**
> Replaces the JWT validation logic with Ed25519 signatures. Adds per-user rate limiting (100 req/min) and moves session tokens from cookies to HttpOnly + SameSite=Strict. The old HMAC-SHA256 tokens are still accepted for 30 days during migration.

**Why this works:**
- Says exactly what changed
- Includes specific numbers and technical details
- No promotional language about "elevating" or "commitment"
- Migration plan is stated as a fact, not a "challenge"
````

## Extraction verification

- **Beginning checked:** The canonical repository, clone origin, initial commit identity, root tree, README title, before-and-after passage, rule list, installation sections, and file-structure listing were compared with the clone, commit API response, recursive tree response, and commit-pinned raw bytes.
- **Middle checked:** `SKILL.md`, all three files under `agents/`, and `banned-vocabulary.md` were inspected against the cloned tree and their exact raw URLs. Rule counts, conditional vocabulary, prompt variants, and file boundaries were checked.
- **End checked:** `examples/bad-examples.md` and `examples/good-examples.md`, including all four matched pairs and the bonus PR example, were checked against the clone and raw bytes. `CONTRIBUTING.md` and `LICENSE` were also preserved and inspected.
- **Structure checked:** The HTTPS clone is not shallow and contains the repository's complete one-commit history. `git ls-files` reported 10 tracked files totalling 27,868 bytes. The GitHub recursive tree reported 12 entries including the two directories and was not truncated. All files decoded as UTF-8, used LF line endings, ended in LF, and matched their commit-pinned raw copies. `git fsck --full --strict` completed without findings. The archive listing contains the same 10 tracked paths.
- **Known omissions:** none

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| `snapshots/attachments/byk3y-no-slop-98cd8fb.tar.gz` | Complete repository tree at the reviewed commit | `444fea547fd8d457060ce5cb850e3d2e11d739583e2eca8c7aa4555538775a40` | Created with `git archive` from commit `98cd8fb016bf5c3467e646e23d7ce09234ec0b2b`; all 10 tracked files preserved under the archive prefix `byk3y-no-slop-98cd8fb/` |
