# AI Fiction Is Easy to Detect Because It's Stupid and Bad, Research Finds

- **Canonical URL:** https://www.404media.co/ai-fiction-is-easy-to-detect-because-its-stupid-and-bad-research-finds/
- **Alternate access URLs:**
  - none; complete body supplied as a local Obsidian Web Clipper extraction and checked against a current web-indexed rendering of the article
- **Author / owner:** Matthew Gault
- **Publisher:** 404 Media
- **Published:** 2026-07-10 at 18:32:21 UTC; live page modified 2026-07-13 at 13:09:37 UTC
- **Retrieved:** 2026-07-14
- **Stable identifier:** Ghost post ID `6a513422bf6d4600013475f4`; UUID `3fe3be15-1418-4ead-83c3-884ea897b246`
- **Version / revision:** live revision modified 2026-07-13
- **Extraction method:** user-supplied Obsidian Web Clipper markdown; body compared with a current web-indexed rendering and metadata checked against the public article page
- **Full-text status:** complete
- **Access and transformation notes:** the direct public page, Ghost Content API, and RSS expose only a two-paragraph preview to an unauthenticated client; a current web-indexed rendering exposes the prose body, and the user-supplied clipping preserves that body with inline links. Navigation, ads, membership prompts, and related-story modules are omitted. The inline podcast iframe is retained.

## Full text

The following clipping frontmatter and body are preserved as supplied, with only a final newline added.

---
title: "AI Fiction Is Easy to Detect Because It's Stupid and Bad, Research Finds"
source: "https://www.404media.co/ai-fiction-is-easy-to-detect-because-its-stupid-and-bad-research-finds/"
author:
  - "[[Matthew Gault]]"
published: 2026-07-11
created: 2026-07-14
description: "ChatGPT uses too many dream sequences and Gemini won’t stop describing characters."
tags:
  - "clippings"
---
Listen to the [404 Media Podcast](https://www.404media.co/the-404-media-podcast/)

Fiction written by artificial intelligence is easy to detect because it struggles with complex story structure and tends to moralize in clunky ways, according to a preprint study from researchers at University of Maryland, College Park and Google DeepMind. They found that AI fiction has tells that go beyond stereotypical overuse of em-dashes and other obvious AI tropes and have more to do with the formulaic nature of the text itself.

“AI stories over-explain themes and favor tidy, single-track plots while human stories frame protagonists’ choices as more morally ambiguous and have increased temporal complexity,” the study, which looked at more than 50,000 AI-generated short stories, found. “Claude produces notably flat event escalation, GPT over-indexes on dream sequences, and Gemini defaults to external character description. We find that AI-generated stories cluster in a shared region of narrative space, while human-authored stories exhibit greater diversity. More broadly, these results suggest that differences in underlying narrative construction, not just writing style, can be used to separate human-written original works from AI-generated fiction.”

<iframe frameborder="no" height="200" src="https://playlist.megaphone.fm/?p=TBIEA2761282490&amp;episodes=1" width="100%"></iframe>

Basically, AI-generated fiction sucks and at the moment is easy to detect. The typical method of detection involves looking for stylistic markers such as an abundance of em-dashes, the overuse of [the word “delve,”](https://arxiv.org/abs/2412.11385?ref=404media.co) or an [obsession with goblins](https://openai.com/index/where-the-goblins-came-from/?ref=404media.co), but this project tried something different. “The idea for this project came because we are hoping to eventually move past plain text detection, into some sort of space where we can separate human ideas from AI-generated ideas,” Jenna Russell, a University of Maryland researcher and one of the study’s authors, told 404 Media. Russell is also an intern at the AI-detection company Pangram.

Russell and her team decided to attempt to detect what she called “narrative features” in AI- generated fiction. The detector is called StoryScope and it builds on NarraBench, a 2025 benchmark that suggested a taxonomy of narrative features in fiction. StoryScope looked at how fiction handled plot development, character descriptions, setting, and temporal structure to determine if something was written by a human or an AI.

“It was my first attempt at getting 'under the surface' and focusing more on ideas,” Russell said. “We wanted to see how close to typical AI-detection we could get by only relying on the narrative features, to understand if this sort of structural difference really even exists. This method also adds some interpretability to detection, which is an open question in the field. Using narrative features, we can point to certain tangible features (such as the number of subplots included in a story). I think this is why it's struck a chord recently, people can really say ‘ah these are some of the underlying traits of how AI writes fiction.’”

To test StoryScope, the researchers selected 10,272 human-written stories then reverse engineered them into writing prompts using Gemini 2.5. Then it took those thousands of prompts and fed them into Gemini 3 Flash, DeepSeek V3.2, Claude Sonnet 4.6, Kimi K2.5, and GPT 5.4. All of the data — including the prompts and the resulting AI stories — are [available on Hugging Face](https://huggingface.co/datasets/jjrussell10/storyscope?ref=404media.co).

To source the stories, the researchers used the Books3 dataset — a database of 183,000 books [collected from pirated ebooks](https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/?ref=404media.co). The dataset is the subject of [several lawsuits](https://courthousenews.com/nvidia-cant-shake-authors-claims-it-trained-ai-on-pirated-books/?ref=404media.co) and has been used to train an [unknown number](https://courthousenews.com/nvidia-cant-shake-authors-claims-it-trained-ai-on-pirated-books/?ref=404media.co) of LLMs. The StoryScope study included more than 10,000 of some of the most famous short stories ever written, many of them pulled from popular anthologies. There’s Joyce Carol Oates, Stephen King, Louis L'Amour, Charlotte Perkins, and Harlan Ellison. All have been rendered down to their base elements by AI and then regurgitated into a different LLM to see if it can replicate them.

Russell told me the dataset was controversial. “Hence why we do not release it to the public,” she said.

The study itself contained a disclosure. “We acknowledge the copyright issues related to the Books3 dataset and do not endorse its use for model training or commercial text generation,” it said. “The use of the dataset in our paper is restricted to academic purposes only and is meant to understand the narrative differences in human-written and AI-generated text to help inform discussions on AI-detection, authorship, and copyright policy.”

The various AIs, of course, can’t possibly replicate the prose of O. Henry. So what, according to StoryScope, are the narrative quirks of LLM-written simulacra of English’s grand works of fiction?

AI tools tend to over explain themes, for one.

“Narrators explicitly explain the story’s theme 77% of the time, versus 52% for humans: a grieving character’s arc will typically end with the narrator stating the lesson learned. AI dialogue serves philosophical debate more often (59% vs. 34%), and references to other works tend to be vague allusions (72% vs. 50%) rather than specific, named references. The pattern is one of over-determination: AI spells out meaning rather than trusting the reader to infer,” the study said.

AI also more often avoids subplots and fails to play with time jumps and flashbacks. The systems overwrite passages about the body and senses. “Where a human author might write that a character ‘felt afraid,’ AI renders fear as a tightening chest, cold sweat, and dimming lamplight,” the study said. Humans also spin more complicated narratives involving more characters and locations than AI can handle. Humans also reference other works of fiction, specific people and places in a way that AI struggles with.

A disclosure caught my eye at the bottom of the StoryScope study. “Large language models and coding agents (Claude Code and Codex) are used to aid with and polish writing and generate some tables and plots,” it said.

“I believe it's important to disclose AI use (and ideally think it should be more in-depth than I wrote in the paper),” Russell told me. “Most researchers are using AI, a lot of it seemingly 'slop' \[...\] but a lot of it is high-effort, good research. Also, technically you are supposed to disclose AI use for conference submissions, but most people don't. I want to help change that norm!”

She also explained a bit more about how AI agents helped shape the project. “I use AI agents to help implement the code (using the claude code / codex interfaces). I also use them as an editor during the writing process! They have access to the project codebase and the paper latex, so the agents can implement graphics for me much more quickly than I could,” she said. “They write comments and add to the paper draft, but I keep it all in different colors so I can manually review and accept/reject/edit any suggestions from AI. I am a big believer that AI can help or hurt writing, but usually helps when not used to create more internet 'slop'.”

I kept thinking about Harlan Ellison and Robert Silverberg’s story “Ship-Shape Pay-Off” being turned into an AI prompt and then spit back out by an LLM. Ellison died in 2018 and was notoriously protective of his work to the point of violence. He successfully sued James Cameron for plagiarism over *The Terminator*. I have a hard time imagining he’d be happy to see his story pumped into a machine, no matter the results.

“A lot of people, like teachers or readers, don't really care if AI was used in the writing process, but do care if the human is the one behind the heart of it,” Russell said. “A teacher wants to know if their student understood the lesson, and a reader wants to know that the creativity behind a touching story was truly the work of the human author.”

## Extraction verification

- **Beginning checked:** title, standfirst, author/date, and the first two body paragraphs were compared across the public page metadata, current web-indexed rendering, and supplied clipping.
- **Middle checked:** the StoryScope method, model list, Books3 discussion, copyright disclosure, and reported feature rates were compared between the supplied clipping and current web-indexed rendering.
- **End checked:** the AI-use disclosure, Russell's description of coding and editing assistance, Harlan Ellison discussion, and final human-creative-control quotation were compared between the supplied clipping and current web-indexed rendering.
- **Structure checked:** the supplied 49-line clipping contains the complete article body, one podcast iframe, inline links, and no article subheadings; page chrome and related-story modules were excluded.
- **Known omissions:** navigation, advertising, subscription prompts, comments, related stories, image asset, and playable podcast media; none is part of the prose evidence reviewed.

## Preserved attachments

| Path | Role in the source | SHA-256 | Preservation / extraction notes |
|---|---|---|---|
| none | The article contains a header image and an embedded podcast player, but neither bears on the prose claims reviewed. | not applicable | No attachment was required for the full-text extraction. The iframe markup remains in the preserved body. |
