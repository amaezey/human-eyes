# AI writing patterns

<!-- This file is generated from `human-eyes/scripts/patterns.json`. Edit the JSON and regenerate via `python3 dev/tools/render_patterns_md.py --write`. -->

57 patterns plus five sub-letter variants (10a, 23a, 31a, 35a, 35b) to detect and fix, plus one unnumbered aggregate meta-check (`overall-signal-stacking`). Organised by category. Each entry has words to watch, a brief description of the problem, and a before/after example. Group A and Group B entries also carry a **Detection** marker stating whether the pattern is enforced by a programmatic check, folded into another check, or left to manual / agent-judgement reading.

## Contents

- [Content patterns (1-6)](#content-patterns)
- [Language and grammar (7-12, 53)](#language-and-grammar)
- [Style (13-18, 49, 57)](#style)
- [Communication (19-21, 62)](#communication)
- [Filler and hedging (22-25, 47-48, 50)](#filler-and-hedging)
- [Sensory and atmospheric (26-28)](#sensory-and-atmospheric)
- [Structural tells (29-32, 38, 42, 44, 52)](#structural-tells)
- [Voice and register (33-37, 39-41, 43, 45-46, 51, 56)](#voice-and-register)
- [Signal stacking (meta-check)](#signal-stacking-meta-check)

---

## Evidence hierarchy from the reference audit

Use source strength when deciding severity. The ruleset should surface clusters of suspicious writing behaviours, not claim that one phrase proves AI authorship.

**Strong empirical backbone:**

- Kobak / Science Advances and the `llm-excess-vocab` dataset support lexical spike detection at corpus level, especially in scientific prose. Use vocabulary as density and clustering evidence, not as one-word proof. Source: https://github.com/berenslab/llm-excess-vocab
- Juzek and Ward's "Why does ChatGPT delve so much?" supports a narrow scientific-abstract vocabulary signal. It is credible for excess-word lists but not for confident document-level claims. Source: https://arxiv.org/abs/2412.11385
- GPTZero's 2026 paper supports the architecture: hierarchical signals, granular findings, adversarial testing, and transparent mixed evidence. It does not add a prose-style rule by itself. Source: https://arxiv.org/abs/2602.13042
- Stanford HAI's detector-bias reporting supports warnings over accusations, especially for non-native English writers. Use process evidence and user review rather than detector-style verdicts. Source: https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers

**Useful but tentative style sources:**

- GPTZero's AI Vocabulary page is useful as a phrase list, but its own framing separates vocabulary scanning from AI-probability scoring. Use all 100 public table rows only as clustering signals. Source: https://gptzero.me/ai-vocabulary
- Shreya Shankar's AI Writing essay is one of the strongest craft references: bad sentence subjects, orphaned demonstratives, empty paragraph endings, over-bulleting, flat rhythm, low information density, vagueness, and fluency without understanding. These directly support the self-audit and several programmatic checks. Source: https://www.sh-reya.com/blog/ai-writing/
- OpenAI's April 2025 GPT-4o sycophancy rollback documents sycophantic model behaviour as a shipped incident class. Source: https://openai.com/index/sycophancy-in-gpt-4o/

**Domain and provenance signals:**

- Walsh, Preus, and Gronski support poetry-specific manual checks: constrained uniformity, rhyme/quatrain defaults, first-person plural overuse, and mood-word clusters. Keep this genre-specific. Source: https://arxiv.org/abs/2410.15299
- Clarkesworld reporting supports fiction as a submission/provenance problem and a manual craft-audit area. Source: https://www.npr.org/2023/02/24/1159286436/ai-chatbot-chatgpt-magazine-clarkesworld-artificial-intelligence
- Futurism's Sports Illustrated reporting supports journalism and review-provenance checks: fake bylines, fake bios, AI headshots, affiliate product-review sludge, undisclosed generated content, and byline laundering. Source: https://futurism.com/sports-illustrated-ai-generated-writers

**2026 operating stance:**

- Em dashes are still used by human writers, but in publication-ready plain prose they are now a strong AI-style signal. Treat them as strong warnings. They must be removed at every depth (Balanced and All); preserve only when the source genuinely uses them stylistically and the preservation is disclosed.
- The best signals are clusters: GPTZero/Kobak vocabulary density, contrived contrast laundering, empty endings, vague demonstrative starts, placeholder residue, sycophantic assistant residue, unrequested headings/lists/Unicode flair, paragraph uniformity, generic email closers, and fake citations or provenance artifacts.

---

## Content patterns

### 1. Significance inflation

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance, underline/underscore/highlight/emphasise the importance/value/significance of, reflects broader, symbolizing its ongoing/enduring/lasting, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, indelible mark, deeply rooted, remarkably, strikingly, staggering/staggeringly

Inflates importance by claiming things "represent" or "contribute to" broader trends without explaining why anyone should care. Every matching importance/value frame is surfaced; the writer can then rewrite it or retain it intentionally. Literal formatting instructions such as "Underline the heading" remain clear.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

**Additional frame:** "If you're still [X], you're already behind".

**Severity:** context_warning · `no-significance-inflation`

**Detection:** Programmatic check `no-significance-inflation`.


### 2. Notability claims

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

Asserts notability by listing sources without context, as though the mention itself is the story.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

**Severity:** strong_warning · `no-notability-claims`

**Detection:** Programmatic check `no-notability-claims`.


### 3. Superficial -ing analyses

**Words and structures to watch:** sentence-opening participial clauses; highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing..., creating..., enhancing..., facilitating..., shaping..., driving..., embodying...

Formulaic present-participle phrases at the start of sentences or tacked onto their ends.

**Before:**
> Drawing on earlier research, the report proposes a new model. The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets and the Gulf coast.

**After:**
> The report draws on earlier research to propose a new model. The temple uses blue, green, and gold. According to the architect, the colours reference local bluebonnets and the Gulf coast.

**Severity:** strong_warning · `no-superficial-ing`

**Detection:** Programmatic check `no-superficial-ing`.


### 4. Promotional language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

Reads like tourism marketing rather than description.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

**Additional marketing formulas:** "game-changer", "unlock your true potential", "unstoppable", "cutting-edge", "groundbreaking", "unprecedented", "one of the best", and "there are so many possibilities".

**Severity:** context_warning · `no-promotional-language`

**Detection:** Programmatic check `no-promotional-language`.


### 5. Vague attributions

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

Attributes opinions to vague authorities without specific sources, creating illusions of consensus.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

**Severity:** strong_warning · `no-vague-attributions`

**Detection:** Programmatic check `no-vague-attributions`.


### 6. Formulaic challenges sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

Formulaic "Challenges" sections that acknowledge a problem then immediately reassure the reader things are fine.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

**Detection:** Manual self-audit only — no programmatic check or agent-judgement record.

---

## Language and grammar

**Severity:** N/A · manual self-audit only (no programmatic check; pattern is described but not enforced)

### 7. AI vocabulary words

**High-frequency words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant, realm, harness, illuminate, facilitate, bolster, streamline, shed light on, revolutionize, innovative, cutting-edge, game-changing, transformative, seamless/seamlessly, genuinely, actually (as filler intensifier), land/lands/landed (as metaphor for "how something is received"), surface/surfaced (as metaphor for "appears in the discourse"), move/moves/the move (as meta-rhetoric about what writing or argument is doing), unspoken, hidden (when used to inflate significance of something ordinary), unparalleled, invaluable, bolstered, meticulous, versatile, significant, effectively, capabilities, advancements, elucidating, firstly, reliance, generalizability, nuance/nuances/nuancing, delving, unveil/unveils/unveiled/unveiling, heighten/heightens/heightened/heightening, amidst, camaraderie, palpable, fleeting, solace, unravel, cacophony, unease, reminder, commence, leverage, elevate, align, dive into, surpass, notable, despite

**AI transition phrases** (a whole category AI overuses): "that being said", "at its core", "to put it simply", "a key takeaway is", "from a broader perspective", "in today's fast-paced world", "as technology continues to evolve", "but here's..."

These words and phrases appear far more frequently in post-2023 text than in human writing from earlier periods. They often cluster in the same paragraph, which is a strong tell. The programmatic #7 check fails at three occurrences in one paragraph. It also fails when two distinct Kousha-Thelwall families appear anywhere in the document, even across paragraphs: underscore, delve, showcase, unveil, intricate, meticulous, pivotal, heighten, nuance, bolster, foster, and interplay.

**Soft scaffold phrases:** "One useful area...", "Another useful area...", "The main strength...", "The main risk...", "Good use usually comes down to..." These phrases are not flashy, which is why they survive rewrites. They mark a generated explainer that is arranging information into bland labelled blocks instead of writing from a real line of thought.

**Tentative high-ratio phrase list:** GPTZero's 100-row AI Vocabulary client payload is based on 3.3 million texts. Use all 100 as clustering signals only. A single phrase is not proof of AI writing, but several in one paragraph is a strong smell.

Full GPTZero phrase list used by the grader:

1. provide a valuable insight
2. left an indelible mark
3. a stark reminder
4. a nuanced understanding
5. significant role in shaping
6. the complex interplay
7. broad implication
8. an unwavering commitment
9. endure a legacy
10. underscore the importance
11. play a pivotal role
12. a pivotal moment
13. navigate the complex
14. mark a turning point
15. continue to inspire
16. gain a deeper understanding
17. the transformative power
18. hold a significant
19. play a crucial role
20. particularly a concern
21. the relentless pursuit
22. emphasize the need
23. target an intervention
24. a multi-faceted approach
25. a serf reminder
26. highlight the potential
27. a significant milestone
28. implication to understand
29. potential risk associated
30. leave a lasting
31. add a layer
32. offer a valuable
33. a profound implication
34. case highlights the importance
35. finding a highlight of the importance
36. pave the way for the future
37. a significant step forward
38. face a significant
39. finding an important implication
40. emphasize the importance
41. a significant implication
42. delve deeper into
43. reply in tone
44. raise an important question
45. make an informed decision in regard to
46. far-reaching implications
47. a comprehensive framework
48. importance to consider
49. a unique blend
50. couldn't help but wonder
51. underscore the need
52. framework for understanding
53. highlight the need
54. a comprehensive understanding
55. the journey begins
56. understanding the fundamental
57. despite the face
58. a delicate balance
59. the path ahead
60. gain an insight
61. laid the groundwork
62. understand the behavior
63. renew a sense
64. aim to explore
65. present a unique challenge
66. provide a comprehensive
67. particularly with regard to
68. address the root cause
69. loom large in
70. the implication of the finding
71. approach ensures a
72. an ongoing dialogue
73. carry a weight
74. ability to navigate
75. present a significant
76. study shed light on
77. a diverse perspective
78. face an adversity
79. a comprehensive overview
80. potentially lead to
81. a broad understanding
82. contribute to the understanding
83. shape the public
84. particularly noteworthy
85. the evidence base for decision making
86. identify an area of improvement
87. analysis of the data to analyze and use
88. undergone a significant
89. need a robust
90. voice will fill
91. concern a potential
92. initiative aims to
93. offering a unique
94. a new avenue
95. despite the challenge
96. ready to embrace
97. the societal expectation
98. make accessible
99. today at a fast pace
100. stand in stark contrast

**Kobak excess vocabulary:** The grader also loads the full 900-row `kobak-excess-words.csv` file from Kobak et al.'s `llm-excess-vocab` repository. The file includes `style`, `content`, `content/style`, and `other` annotations. The aggregate signal-stacking check uses style-annotated terms as one vocabulary signal alongside the local AI-vocabulary list and all 100 GPTZero phrases. Kobak words do not fail text by themselves.

Current threshold: vocabulary signals contribute points to an overall score alongside structural signals such as manufactured insight, contrived reframes, paragraph uniformity, unrequested headings, soft scaffolding, and assistant residue; the aggregate trips at four points from any mix. This follows the paper's corpus-level logic: excess vocabulary is evidence in a pattern, not a standalone detector verdict.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonisation, remain common, especially in the south.

**Additional exact vocabulary candidates:** literally, incredibly, essentially, arguably, undeniably, remarkably, interestingly, notably, particularly, ultimately, groundbreaking, revolutionary, next-level, world-class, double down, spearhead, supercharge, reimagine, synergize.

**Additional marketing-email phrase candidates:** "thoughtful strategy", "clear messaging", and "intentional design".

**Severity:** strong_warning · `no-ai-vocabulary-clustering` (the soft-scaffold sub-bullet now also references `no-soft-scaffolding` — see #47)

**Detection:** Programmatic check `no-ai-vocabulary-clustering`.


### 8. Copula avoidance

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

Substitutes elaborate constructions for simple "is", "are", or "has".

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totalling 3,000 square feet.

**Severity:** strong_warning · `no-copula-avoidance`

**Detection:** Programmatic check `no-copula-avoidance`.


### 9. Negative parallelism

Negative parallelism includes "not X but Y", "not just X, Y", positive-then-negative reversals, comparative reframes, negation countdowns, and "X rather than Y". It remains the same signal when split across sentences, including "It's not X. It's Y.", "The target was never X. The target was Y.", negative clauses resumed by `it`, `they`, `he`, or `she`, and repeated negative clauses that turn affirmative.

The Atlantic reported Pangram's estimate that the not-X-but-Y construction appears about three times as often in AI writing as in human writing. This is evidence that the construction is an AI-overrepresented signal. Source: https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/

The checker surfaces the construction wherever it appears. It does not suppress a match based on inferred intention. Repetition matters: overlapping regexes for one source construction count once, while separate occurrences add progressively more signal-stacking evidence.

Forms include:

- "It's not X, it's Y."
- "It's not X. It's Y."
- "The target was never X. The target was Y."
- "It's Y, not X."
- "Less X than Y."
- "More Y than X."
- "Not so much X as Y."
- "Beyond X, it is Y."
- "You might think X. Actually, Y."
- "No X. No Y. Just Z."
- "I may not have X. I may not have Y. But I have Z."
- The same repeated-negative reversal with `Yet`, `However`, `Still`, `Nevertheless`, `Nonetheless`, `Even so`, `That said`, `Instead`, `In contrast`, or `On the other hand`.
- The same reversal without a connector when the affirmative turn is emphatic: "I do have Z", "What I have is Z", or "What I do have is Z".
- "Stop thinking of it as X. Start thinking of it as Y."
- "X isn't the future. Y is."
- "X is dead. Y is what's next."
- "Forget X. Focus on Y."
- "AI doesn't eliminate labour; it redistributes it."
- "Atlas didn't shrug. He drilled."
- "Not X—but Y."
- "X rather than Y."

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone throughout the track.

**Before:**
> The film is a negotiation with memory, not just a family story. Beyond grief, it becomes a meditation on what it means to belong.

**After:**
> The film uses family conflict and remembered details to show how belonging changes after someone dies.

**Before:**
> You might think the app is about saving time. Actually, it is about trust.

**After:**
> The app earns trust by showing exactly what changed and letting users undo each step.

**Additional forms:** "I stopped X and started Y" and "Teams that X will thrive. Teams that don't will be left behind".

**Severity:** strong_warning · `no-negative-parallelisms`

**Detection:** Programmatic check `no-negative-parallelisms`. Runs at Balanced and All. Matches within a sentence and across sentence boundaries. It also matches a negative clause followed by an `it`, `they`, `he`, or `she` resumption; punctuated `not X—but Y` frames using a comma, colon, semicolon, hyphen, en dash, or em dash; and every `rather than` frame. A repeated-negative reversal requires at least two negative clauses with the same explicit subject followed by an explicit or emphatic affirmative turn with that subject; the whole frame counts once. Each separate construction counts once. One occurrence contributes 2 signal-stacking points; two contribute 3; three or more contribute 4. Overlapping regex matches on the same source span are deduplicated.


### 10. Rule of three

Three-part structures are surfaced wherever they occur, including item lists, verb phrases, clauses, and quoted material. Detection records the construction; it does not decide that the writing is artificial or that the triad should be removed.

**Tolerance note:** Three-part structures are common in human rhetoric, comedy, fiction, speeches, and criticism. Treat them as an AI-associated misuse when they cluster densely, feel interchangeable, or use abstractions to simulate breadth. Preserve concrete, necessary, funny, rhythmic, quoted, or deliberately voiced triads.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels, with time for informal networking between sessions.

**Severity:** context_warning · `no-forced-triads` (the density escalation lives at #10a)

**Detection:** Programmatic check `no-forced-triads`. Candidate evidence records whether the matched span is inside quotation marks; quotation context does not suppress detection.


### 10a. Triad density

The density variant of #10 rule of three. While #10 surfaces each individual triad, #10a escalates when triads cluster across longer prose: four or more three-part item, phrase, or clause coordinations in a piece of 300+ words. This is the rate-of-triads metric — even when each individual triad reads naturally, the aggregate cadence can become mechanical.

**Before:**
> The team values clarity, directness, and rigour. Their meetings are short, focused, and outcome-driven. The retros surface what worked, what didn't, and what to try next. The roadmap balances delivery, learning, and team health.

**After:**
> The team runs short meetings and uses retros to decide what to try next. The roadmap is mostly about delivery, with deliberate space for the things the team is still learning how to do well.

**Severity:** context_warning · `no-triad-density`

**Detection:** Programmatic check `no-triad-density`. Quoted candidates remain counted and are separately marked as quoted evidence.


### 11. Synonym cycling

Excessive synonym substitution, cycling through different words for the same referent within a short span. A proposed but untested explanation is repetition-penalty or anti-repetition tuning; no cited source demonstrates the mechanism.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

**Severity:** N/A · manual self-audit only (see Detection)

**Detection:** Manual self-audit only — no programmatic check or agent-judgement record. Reliable detection requires coreference resolution to recognise that two noun phrases share a referent, which is beyond regex.


### 12. False ranges

"From X to Y" constructions where X and Y are not on a meaningful scale, creating an illusion of breadth without communicating scope.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

**Severity:** N/A · manual self-audit only (see Detection)

**Detection:** Manual self-audit only — no programmatic check or agent-judgement record. Judging whether range endpoints sit on a meaningful scale requires semantic context the grader does not have.


### 53. Vocabulary diversity

A windowed lexical-diversity metric for prose of 150+ words: the mean type-token ratio over sliding 150-word windows. On the project's calibration corpus (dev/evals/ttr-calibration-2026-07-17.md), generated prose ran more lexically diverse than human prose in every length band, so unusually high windowed diversity is the flagged direction. The check flags at 0.71; values from 0.74 sit above the observed human range and the evidence says so.

**Tolerance note:** Dense encyclopedic or fact-heavy writing can run high on windowed diversity. Treat a flag as a signal to read the prose, and preserve writing whose variety is doing real work.

**Before:**
> Each paragraph introduces fresh terminology, novel qualifiers, and untouched synonyms; no concept is ever named the same way twice.

**After:**
> Pick one name for each concept and keep it. Repetition of the right word is clarity, not weakness.

**Severity:** context_warning · `vocabulary-diversity`

**Detection:** Programmatic check `vocabulary-diversity`.

---

## Style

### 13. Boldface overuse

Emphasises phrases in boldface mechanically, bolding things that do not need visual emphasis.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

**Severity:** context_warning · `no-boldface-overuse`

**Detection:** Programmatic check `no-boldface-overuse`. Flags four or more bold spans in non-list, non-heading prose.


### 14. Inline-header lists

List items start with bolded headers followed by colons, turning prose into a slide deck. The same structure can remain after pasted formatting loses its list markers and line breaks.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimised algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimised algorithms, and adds end-to-end encryption.

**Severity:** strong_warning · `no-inline-header-lists`

**Detection:** Programmatic check `no-inline-header-lists`. Flags two or more bold-label-and-colon segments. Canonical list items count across lines; two or more unmarked segments count when they occur on the same input line. The colon may sit inside or immediately after the bold span; list markers include Markdown bullets, common Unicode bullets, `1.`, and `1)` numbering.


### 15. Title case in headings

Capitalising all main words in headings reads as formal to the point of stiffness.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

**Severity:** N/A · manual self-audit only (see Detection)

**Detection:** Manual self-audit only — no programmatic check or agent-judgement record. Markdown headings themselves are not treated as an indicator; title-case treatment can be reviewed only when the requested house style calls for sentence case.


### 16. Emojis

Decorating headings or bullet points with emojis is almost never appropriate in written content.

**Before:**
> :rocket: **Launch Phase:** The product launches in Q3
> :bulb: **Key Insight:** Users prefer simplicity
> :white_check_mark: **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity, so the next step is to schedule a follow-up meeting to discuss how that finding should shape the launch.

**Severity:** inherits context_warning from `no-unicode-flair` (see Detection)

**Detection:** Folded into the programmatic check `no-unicode-flair`.


### 17. Curly quotation marks

**Tolerance note:** Curly quotes are typography, not inherently AI writing. Normalise them in hard-mode plain output if requested. Preserve them in sourced excerpts, literary fixtures, publication text, or quoted material.

ChatGPT uses curly quotes instead of straight quotes.

**Before:**
> He said \u201cthe project is on track\u201d but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

**Severity:** context_warning · `no-curly-quotes`

**Detection:** Programmatic check `no-curly-quotes`.


### 18. Hyphenated compound modifier overuse

**Words to watch when clustered:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end

Individual hyphenations are often correct, but AI stacks four or five in a single sentence. When you encounter three or more hyphenated compound modifiers in one sentence, restructure to reduce the density.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report on our client-facing tools. Their decision-making process was well-known for being thorough and detail-oriented.

**After:**
> The team, drawn from several departments, delivered a report grounded in usage data for our client-facing tools. Their process for making decisions was known for being thorough.

**Severity:** context_warning · `no-compound-modifier-density`

**Detection:** Programmatic check `no-compound-modifier-density`. Flags three or more AI-stock hyphenated compounds in a single sentence, drawn from a watchlist of common offenders.


### 49. Em dashes

ChatGPT and similar systems use the em dash (`—`) as default mid-sentence punctuation where most human writers would use a comma, a semicolon, a period, or a parenthetical pair of dashes. A single em dash reads naturally; routine em dashes in plain web prose are a strong 2026 AI-style fingerprint.

**Tolerance note:** Em dashes are treated as a violation: the check fails on any occurrence and rewrite depths remove them. Deliberate use is a human decision, not a tool decision. Preserve one only when the author explicitly chooses to keep it, and disclose the preservation.

**Before:**
> The framework offers a unified approach — one that combines flexibility with rigour — and integrates with existing tooling without friction.

**After:**
> The framework combines flexibility with rigour, and it integrates with existing tooling without friction.

**Severity:** strong_warning · `no-em-dashes`

**Detection:** Programmatic check `no-em-dashes`. Counts U+2014 occurrences and fails on any. Distinct from #17 curly quotes (a typographic substitution at the quotation-mark level); this check targets the long-dash glyph as default mid-sentence punctuation.


### 57. Parenthetical headings

Parentheses do not belong in human-eyes headings. They usually carry a vague qualifier, private aside, or simulated doubt that should either be stated directly in the section or deleted.

**Before:**
> ## Document skills (the steady ones)

**After:**
> ## Document skills

**Severity:** hard_fail · `no-parenthetical-headings`

**Detection:** Programmatic check `no-parenthetical-headings`. Body parentheses are outside this rule.

---

## Communication

### 19. Collaborative artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

Chatbot correspondence pasted directly into content without being cleaned up.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

**Severity:** hard_fail · `no-collaborative-artifacts`

**Detection:** Programmatic check `no-collaborative-artifacts`.


### 20. Knowledge-cutoff disclaimers

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

AI disclaimers about incomplete information left in the text.

**Before:**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

**Severity:** strong_warning · `no-knowledge-cutoff-disclaimers`

**Detection:** Programmatic check `no-knowledge-cutoff-disclaimers`. Note that this does not fold into `no-collaborative-artifacts` — that check covers chat residue ("I hope this helps", "great question") but not training-update or limited-information hedges.


### 21. Sycophantic/servile tone

Overly positive, people-pleasing language that performs agreement rather than engaging with substance.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here, particularly the trade deficit data from Q3.

**Severity:** inherits hard_fail from `no-collaborative-artifacts` (see Detection)

**Detection:** Folded into the programmatic check `no-collaborative-artifacts`. The headline sycophantic phrases ("you're absolutely right", "great question!", "what a thoughtful question/observation", "that's a brilliant observation") already live in the COLLABORATIVE_ARTIFACTS pattern set; no separate check.


### 62. Formulaic social-post frames

**Frames to watch:** engagement requests ("Drop your take below", "Agree or disagree?", "Save this for later"); empty agreement and bait comments ("This is gold", "Hot take:", "I'd add a #6"); credential prefaces ("As someone who's been doing this for 10 years"); AI-experiment wrappers ("I asked ChatGPT to... and the results shocked me"); time-compression brags ("From zero to launch in 48 hours"); and artificial scarcity hooks ("I spent 100+ hours so you don't have to").

These are complete reusable platform formulas, not isolated vocabulary. Rewrite the frame around the post's actual request, evidence, experience, or constraint.

**Before:**
> I spent 100+ hours so you don't have to. Save this for later.

**After:**
> I compared the 14 tools against export quality, revision history, and price. The table below shows the results.

**Severity:** strong_warning · `no-formulaic-social-posts`

**Detection:** Programmatic check `no-formulaic-social-posts`. One complete regex-matched frame triggers a finding. Evidence reports the matched subtype: engagement request, agreement comment, engagement comment, credential preface, AI wrapper, time compression, or scarcity hook.

---

## Filler and hedging

### 22. Filler phrases

Common substitutions:
- "In order to achieve this goal" -> "To achieve this"
- "Due to the fact that it was raining" -> "Because it was raining"
- "At this point in time" -> "Now"
- "In the event that you need help" -> "If you need help"
- "The system has the ability to process" -> "The system can process"
- "It is important to note that the data shows" -> "The data shows"
- "In today's fast-paced world" -> cut entirely
- "As technology continues to evolve" -> cut entirely
- "At the end of the day" -> cut or replace with specific conclusion
- "Generally speaking" -> "Usually" or cut
- "Broadly speaking" -> "Overall" or cut
- "From a broader perspective" -> cut or state the perspective directly

**Additional frames:** "That said", "To be clear", and "With the caveat that".

**Severity:** strong_warning · `no-filler-phrases`

**Detection:** Programmatic check `no-filler-phrases`.


### 23. Excessive hedging

Over-qualifying statements to the point where the sentence commits to nothing.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

**Severity:** context_warning · `no-excessive-hedging`

**Detection:** Programmatic check `no-excessive-hedging`.

### 23a. False concession hedges

**Words to watch:** "While critics argue..., supporters say...", "the truth lies somewhere in the middle", "both sides have valid points", "it depends on context" when used to avoid a claim.

AI often performs nuance by staging two generic positions and then landing in a bland middle. Real nuance names the evidence, stakes, and tradeoffs. If the sentence only balances abstractions, rewrite it as a direct claim.

**Before:**
> While critics argue remote work weakens culture, supporters say it improves flexibility. The truth lies somewhere in the middle.

**After:**
> Remote work improves flexibility for most desk workers, but it exposes weak management habits that office routines used to hide.

**Additional frames:** "To be fair", "I'm not saying X, but", "Don't get me wrong", "This isn't to say that", and "Granted, X, but".

**Severity:** strong_warning · `no-false-concession-hedges`

**Detection:** Programmatic check `no-false-concession-hedges`.


### 24. Generic positive conclusions

Vague upbeat endings that could be appended to any article on any topic.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year, both in the southeast.

**Additional closer formulas:** "The question isn't whether, but when", "We're still early", "This is just the beginning", "The genie is out of the bottle", "Buckle up", "Welcome to the future", "Think about that", "This is the new normal", "Act accordingly", and "[X] will never be the same".

**Severity:** hard_fail · `no-generic-conclusions`

**Detection:** Programmatic check `no-generic-conclusions`.


### 25. Staccato rhythm in extended contexts

**Words to watch:** "Full stop.", "Period.", "That's it. That's the tweet.", "[One word]. That's the word.", "Too young. Too single.", "No family. No calls."

The four exact dramatic-fragment formulas fail at one occurrence. A pair of adjacent short fragments also fails when both begin with the same word. Other staccato rhythm fails when at least three consecutive sentences contain fewer than six words each.

**Tolerance note:** Staccato is not automatically bad. Preserve it when it is character voice, panic, comedy, dialogue, aphorism, or deliberate literary rhythm. Cut it when it functions as generic article emphasis.

**Before:**
> The data was clear. Unmistakably so. Every metric pointed in the same direction. And that direction was down.

**After:**
> The data pointed unambiguously in one direction: every metric was declining, and the trend had been consistent for three consecutive quarters.

**Severity:** context_warning · `no-staccato-sequences`

**Detection:** Programmatic check `no-staccato-sequences`.


### 47. Soft scaffolding

**Words to watch:** "One useful area...", "Another useful area...", "The main strength...", "The main risk...", "Good use usually comes down to...", "Comes down to giving/using/making...", "This can be helpful when...", "Especially useful when...", "In those cases,...", "With that distinction in mind,...", plus repeated report paragraph openers such as "A major priority was...", "Another area of work was...", "The committee also examined...", and "Throughout the reporting period..."

Bland transition phrases from generated explainers and reports. They are not flashy, which is why they survive rewrites — they mark prose arranging information into balanced labelled blocks instead of writing from a real line of thought. Report openers are recognised only at paragraph starts, and the document remains clear until at least two scaffold candidates occur. A single necessary transition therefore remains below threshold. Distinct from #22 filler phrases (which are stock padding) and #34 tidy paragraph endings (which close paragraphs); soft scaffolding sits between sentences and paragraphs as connective tissue.

**Before:**
> One useful area is structuring feedback. Another useful area is timing it well. The main strength of these approaches is consistency. Good use usually comes down to giving the receiver enough context.

**After:**
> Feedback works best when you can name the screen, the moment, and what surprised you. The reviewer who said "this dashboard is confusing" cost me half a day; the reviewer who said "the metric on the top-right is the one I read first and I can't tell what it's measuring" saved me a week.

**Severity:** strong_warning · `no-soft-scaffolding`

**Detection:** Programmatic check `no-soft-scaffolding`. The soft-scaffold phrase set is also referenced in pattern #7's preamble as part of AI vocabulary discussion, but it is enforced as its own check rather than folded into the vocabulary cluster.


### 48. Dense negation

**Words to watch:** clusters of "is not", "are not", "was not", "were not", "does not", "do not", "isn't", "aren't", "wasn't", "weren't", "doesn't", "don't", "not merely", "not simply", "not just" — across longer prose, not in a single sentence.

Distinct from #9 (contrived contrast in a single sentence) and #33 (countdown negation across two or three consecutive sentences). This is sustained negation density across a piece: a draft that defines itself by what it isn't, paragraph after paragraph. The check activates only on prose of 300+ words to avoid penalising short polemics where dense negation is the deliberate rhetorical move.

**Before:**
> The model isn't trying to imitate writing. It isn't merely fitting a template. It isn't just generating tokens. It's not really thinking, but it's also not just predicting next word. The output isn't original, but it isn't copied either. The system isn't conscious, but it isn't a simple lookup either. None of this is what most people assume.

**After:**
> The model is doing pattern completion at very large scale, with no internal model of meaning. The output looks like writing because the training data is writing, not because the system understands anything. Treat the result as a draft, not a thought.

**Severity:** context_warning · `no-negation-density`

**Detection:** Programmatic check `no-negation-density`. Triggers only on prose of 300+ words.


### 50. Formulaic openers

**Words to watch:** "At its core,", "At a foundational/fundamental/practical level,", "Beyond this/that/[abstract noun],", "There is also a [\…] dimension/aspect/element,", "It is worth recognising/noting/mentioning,", "From a [\…] perspective/standpoint,", "On a [\…] level,", "In a broader/wider/larger/similar context/sense/vein,", "Perhaps most importantly/significantly/notably/crucially,", "What makes this particularly/especially/uniquely [\…]", "Here's what nobody's talking about:", "Let me be clear:", "Can we talk about [X] for a second?", "Let's talk about [X].", "We need to talk about [X].", "I need to say something about [X].", "[N] things I learned from [X]", "[N] mistakes I see everyone making", "[N] lessons from [X] nobody talks about", "The [N] pillars of [X]", "[N] things I wish I knew before [X]", "Here are [N] frameworks that changed how I think about [X]"

Formulaic paragraph or headline openers that delay the claim, stage it as a disclosure, or frame it as a step up in abstraction. They survive rewrites because they are bland connectives rather than vocabulary tells, but they mark prose that stitches paragraphs together with the same handful of moves.

**Before:**
> At its core, the proposal is about consolidation. From a broader perspective, it reduces operational overhead. Perhaps most importantly, it aligns with the strategic plan.

**After:**
> The proposal consolidates three legacy tools into one, which reduces integration points and on-call rotations. It is also the move the strategic plan has been pointing at since 2025.

**Additional templates:** "In [year], [X] won't be optional. It'll be table stakes" and "The [role] of [year] will look nothing like the [role] of [earlier year]".

**Additional email openers:** "I hope this email finds you well" and "Are you tired of X? Look no further than Y".

**Severity:** strong_warning · `no-formulaic-openers`

**Detection:** Programmatic check `no-formulaic-openers`. Anchored regex against the first line of each paragraph, with optional Markdown heading markers for numbered social-post hooks; flags any paragraph whose opener fits the formulaic-opener template. Distinct from #7 AI vocabulary words (which lists opener phrases as one sub-bullet under the broader vocabulary check) and from #47 soft scaffolding (which catches between-sentence connectives like "One useful area..." rather than paragraph-opening abstractions).


### 60. Modal qualifier stacks

Several modal and frequency qualifiers inside one sentence until the claim loses commitment: "The change can potentially often improve results." Each qualifier alone is ordinary; the stack is the tell. Document-wide hedge density is #23's job; this check reads one sentence at a time.

**Before:**
> The new cache can potentially often reduce latency for most tenants.

**After:**
> The new cache reduces latency for most tenants; the gain depends on cache hit rate.

**Severity:** context_warning · `no-modal-stacks`

**Detection:** Programmatic check `no-modal-stacks`. Flags any sentence containing three or more bare modal or frequency qualifiers (can, could, may, might, potentially, possibly, often, sometimes, typically, usually, generally); capitalised May is excluded. Distinct from #23, which counts fixed hedge phrases across the whole text.

---

## Sensory and atmospheric

These patterns are especially common in descriptive, creative, and reflective writing. AI reaches for sensory language but, having no physical experience, attaches it to abstractions.

### 26. Ghost/spectral language

**Words to watch:** ghost(s), spectral, shadow(s), whisper(s), echo(es), phantom, haunting/haunted, lingering, remnant(s), trace(s) used atmospherically, unspoken, hidden (when inflating the significance of something ordinary)

AI defaults to spectral, ghostly, shadowy imagery for anything it wants to make feel deep. Everything becomes a shadow, a memory, a whisper, or an echo. One "ghost" is fine. Four in two paragraphs is a tell.

**Before:**
> The pebbles carry the ghosts of the boulders they were, resting in a quiet space between the earth and the sea. Each one is a whisper from a vanished landscape, an echo of forces that shaped the coastline.

**After:**
> The pebbles are fragments of larger rocks, broken down over centuries by water and weather. They collect in the spaces between tide lines where the current drops them.

**Severity:** context_warning · `no-ghost-spectral-density`

**Detection:** Programmatic check `no-ghost-spectral-density`.


### 27. Quietness obsession

**Words to watch:** quiet/quietly, silent/silently, softly, hum/humming, stillness, gentle, hushed, murmur, settle/settled, tender

AI inserts quietness and softness where it does not belong, often against the logic of the scene. In a 759-word essay about pebbles, one AI used "quiet" ten times. The word has become a proxy for depth.

Adjacent manufactured-insight frames include "when no one noticed", "the shift nobody noticed", "before anyone noticed", and "without anyone noticing". These usually imply privileged perception without doing the evidentiary work.

**Before:**
> There is a quiet beauty in the way the morning light settles on the table. The coffee hums softly in its cup. Outside, the world has a gentle stillness to it, as if holding its breath.

**After:**
> The morning light was on the table. The coffee was getting cold. Outside, a truck reversed into the loading bay and someone dropped a crate.

**Severity:** context_warning · `no-quietness-obsession`

**Detection:** Programmatic check `no-quietness-obsession`.


### 28. Forced synesthesia

AI blends senses inappropriately to simulate literary depth: emotions get tastes, sounds get colours, abstract concepts get textures. This happens because the model has no physical experience, so its sensory vocabulary gravitates to immaterial subjects. Real synesthetic writing is specific and grounded ("a great plateful of blue water" works because Woolf had both stood before a view and sat down to a meal). AI synesthesia is unanchored.

**Before:**
> Thursday is a liminal day that tastes of almost-Friday. Her grief hummed with the colour of old photographs. The silence had a texture, rough and amber, draped across the room like forgotten cloth.

**After:**
> Thursday felt like waiting. She kept pulling out old photographs and putting them back. The room was silent in a way that made her aware of her own breathing.

**Severity:** N/A · agent-judgement (registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `forced_synesthesia` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`) — forced synesthesia is not regex-amenable.

---

## Structural tells

### 29. Mid-sentence rhetorical questions

A one-to-four-word fragment is punctuated as a question even though it does not begin with an interrogative word or question-forming auxiliary, then an answer or evaluation follows immediately: "And honestly? That's amazing.", "The result? It's remarkable.", "Best part? It actually works." The construction manufactures conversational emphasis through a terse setup-and-answer rhythm.

**Before:**
> The result? It's simpler than you think.

**After:**
> The result is simpler than you might expect.

**Severity:** context_warning · `no-rhetorical-questions`

**Detection:** Programmatic check `no-rhetorical-questions`. One complete fragment-question answer beat triggers the finding. The fragment contains at most four words; the immediate answer contains at most twelve.


### 30. Generic/ungrounded metaphors

AI metaphors are plausible but specific to nobody. They gesture toward meaning without achieving it. Human metaphors draw from personal experience or shared cultural references. AI metaphors draw from the statistical middle.

**Before:**
> Learning the ukulele is like teaching your fingers to dance again after years of sitting still. Every chord is a puzzle piece that finally clicks into a song.

**After:**
> The first week my fingers could not stretch far enough for a G chord and I kept muting the string next to it with the side of my index finger.

When you spot a metaphor, ask: could anyone have written this, or does it come from a specific experience? If anyone could have written it, replace it with a concrete detail.

**Severity:** N/A · agent-judgement (registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `generic_metaphors` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`) — judging metaphor groundedness is not regex-amenable.


### 31. Excessive list-making

AI converts prose to bullet points when the content does not warrant it. This is driven by RLHF training: human raters reward structured-looking answers, so the model learns that bullets = quality. The result is text that looks organised but reads like a slide deck rather than writing.

When you encounter unnecessary bullet points or numbered lists, fold the content back into prose. Lists are appropriate for genuinely discrete items (ingredients, steps, specifications). They are not appropriate for flowing arguments, observations, or narrative.

**Severity:** context_warning · `no-excessive-lists`

**Detection:** Programmatic check `no-excessive-lists`.

### 31a. Unicode flair

**Words/symbols to watch:** arrows, checkmarks, stars, ornamental bullets, emoji-style symbols, `×`, and stylized Unicode letter runs such as `𝗯𝗼𝗹𝗱` or `𝘪𝘵𝘢𝘭𝘪𝘤`. Ordinary Markdown bold and italics are not included.

Decorative Unicode can make prose read like a generated checklist or social post. Each contiguous stylized-letter run counts as one candidate; the check warns at two candidates.

**Severity:** context_warning · `no-unicode-flair`

**Detection:** Programmatic check `no-unicode-flair`.


### 32. Dramatic narrative transitions

**Words to watch:** "Something shifted.", "Everything changed.", "And then, everything clicked.", "That's when it hit me.", "And that made all the difference."

Standalone sentences that claim a narrative turning point without earning it. These borrow the structure of memoir writing ("The door opened and my life was never the same") but deploy it for mundane observations. They combine staccato fragments with manufactured insight.

**Before:**
> I had been thinking about productivity all wrong. And then, something shifted. I stopped optimising for output and started optimising for energy. Everything changed.

**After:**
> I stopped trying to do more in less time and started paying attention to when I had energy and when I did not. The change was not dramatic, but over a few months the difference was obvious in my work.

**Severity:** context_warning · `no-dramatic-transitions`

**Detection:** Programmatic check `no-dramatic-transitions`.

### 38. Section scaffolding

**Structures to watch:** Identical short section labels repeated three or more times; a document whose first Markdown heading starts below level 2; a later heading that jumps more than one level deeper; or a thematic break (`---`, `***`, or `___`) immediately before a heading. YAML frontmatter delimiters are excluded.

These repeated or mechanically skipped structures can create a cookie-cutter template.

**Before:**
> 1. Build trust early
> How to make this work:
> Start with small wins...
>
> 2. Communicate clearly
> How to make this work:
> Hold regular standups...
>
> 3. Measure outcomes
> How to make this work:
> Define success metrics...

**After:**
> 1. Build trust early
> Start with small wins and let the team see results before asking for bigger commitments...
>
> 2. Communicate clearly
> The teams that got this right held short daily standups, but the format mattered less than consistency...
>
> 3. Measure outcomes
> We learned the hard way that vanity metrics kill momentum. Define what actually matters before you start tracking anything.

**Severity:** strong_warning · `no-section-scaffolding`

**Detection:** Programmatic check `no-section-scaffolding`.


### 42. Manufactured insight framing

**Words to watch:** "what's really", "the real answer", "here's what's really", "the real story is", "what's actually happening", "contrary to popular belief", "the uncomfortable truth", "what nobody is talking about", "what no one seems to realise", "what most people miss", "what (no one|nobody) noticed", "before anyone noticed", "without anyone noticing", "let that sink in", "read that again", "sit with that for a second", "I'll say it louder for the people in the back", "if you know, you know", "and that changes everything", "the real insight/challenge/takeaway/kicker/question", "a quiet/powerful/important/profound lesson", "sometimes the bravest/hardest/most important", "it/this/the experience taught me that", "what this/the failure taught me was", "the lesson I/we learned was", "X is the Y of Z", "X becomes a trap", "the language/currency/architecture of", "this isn't X. it's Y.", "that's not X. that's Y.", "the honest answer is", "here's the honest (answer|framing|truth)", "here's the (real) truth", "the real truth is", "if I'm being honest", "in all honesty", "to be (perfectly) honest,", "this is the part most people skip", "most people won't tell you this", "nobody's talking about this", "everyone's sleeping on this", "this flew under the radar", "I wasn't supposed to share this, but", "what they don't want you to know", "the thing nobody tells beginners", "the secret that [industry] doesn't want you to know", "I've been sitting on this for weeks", "Stop what you're doing", "Drop everything", "Read this before [X]", "If you haven't seen this yet", "You're going to want to bookmark this", "Save this before it gets taken down", "This changes everything", "This is bigger than people realise", "[X] just changed the game forever"

Performs revelation through phrasing — claims hidden depth or secret significance without doing the evidentiary work. Includes explicit lesson announcements ("It taught me that...", "What the failure taught me was...") and reusable aphorism templates ("Symmetry is the language of trust", "Efficiency becomes a trap", "the currency of attention"). Also includes "the real X?" rhetorical questions, performed knowingness ("read that again", "let that sink in"), pseudo-profundity ("quietly revolutionary", "the quiet part"), formulaic depth framing ("here's the thing", "the reason is straightforward"), and contrived contrast that reveals an inflated abstract payload. Also includes **performed candour** — honesty/truth framing ("the honest answer is", "here's the real truth", "if I'm being honest", "in all honesty") that dresses an ordinary statement as a hard-won admission.

**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer. Here's the real insight: the architecture of belonging changes everything.

**After:**
> Symmetric layouts often feel more predictable because repeated elements tell readers where to look. Teams can over-optimise workflow speed while ignoring whether the result helps the people using it.

**Additional frames:** "The data speaks for itself", "The market has spoken", "The numbers don't lie", "This technology wants to", "AI is coming for your [X]", "The industry is waking up to", "The results were eye-opening", "This opens up a world of", "The possibilities are endless", "And here's the kicker", "Wait, it gets better", "The plot thickens", "Enter: [X]", "X is the new Y", and "X is only as good as Y".

**Severity:** strong_warning · `no-manufactured-insight`

**Hypothesis (performed candour):** The honesty/truth-framing phrases ("the honest answer is", "here's the real truth", "if I'm being honest") are folded into `no-manufactured-insight` rather than promoted to their own numbered entry. They share the same generative move as the rest of #42 (claiming significance through phrasing rather than earning it), so a single check captures the family. Promote to a sibling entry if either signal lands: the candour regex set grows materially beyond the current handful of phrases, or audit failures cluster on candour without co-occurring with the rest of #42's mechanisms. Until then, keep folded.

**Detection:** Programmatic check `no-manufactured-insight`. It fails on any fixed manufactured-insight phrase or aphorism template, including `X is the Y of Z`, `X becomes a trap`, and `the language/currency/architecture of`. Closely related to #9 contrived contrast — manufactured insight framing is the *content* of the false reveal; #9 is the *syntactic shape*.


### 44. Signposted conclusions

**Words to watch:** "In summary,", "In conclusion,", "To summarise,", "To summarize,", "To conclude,", "To sum up,", "To wrap up,", section headings "Conclusion", "Final thoughts", "Key takeaways", "Summing up".

Explicit conclusion labels turn the ending into a generic summary. AI overuses them — both at sentence level ("In conclusion, …") and as standalone section headings. Human writers usually let the argument's last sentence carry the closing weight; explicit signposts often appear because the model has nothing left to say but still wants the piece to feel finished.

**Tolerance note:** Academic abstracts, formal reports, instructional reference material, and structured policy briefs may legitimately use "Conclusion" or "Summary" headings as navigational signposts. The check fires on prose contexts where the signpost flattens the ending; preserve when the genre genuinely calls for one.

**Before:**
> In conclusion, the policy demonstrates the value of long-term thinking and the importance of stakeholder buy-in. Key takeaways include the need for clear communication and disciplined follow-through.

**After:**
> The policy succeeded because the council kept three commitments visible: weekly progress notes, named owners on every line item, and a public deadline. Each one was easy to abandon and the team didn't.

**Severity:** context_warning · `no-signposted-conclusions`

**Detection:** Programmatic check `no-signposted-conclusions`.


### 52. Sentence length variance

A coarse rhythm metric for prose of 100+ words. Human writing varies sentence length naturally, mixing short punch sentences with longer connective passages. AI prose tends toward the centre of the distribution: most sentences land in a similar word count band, and the resulting cadence reads mechanical even when individual sentences are competent.

**Tolerance note:** Some genres legitimately run uniform: instructional steps, headlines, dialogue, dictionary entries, telegraphic memos. The check skips short-form prose under 100 words. Treat low variance as a signal, not a hard fail — preserve when the form genuinely calls for uniformity.

**Before:**
> The team uses agile methods. They run two-week sprints. Each sprint starts with planning. Each sprint ends with a retro. The team values feedback. They iterate based on what they learn.

**After:**
> The team uses agile methods, running two-week sprints that bracket each piece of work between planning and a retro. Feedback drives iteration: each sprint adjusts based on what the last one taught them.

**Severity:** context_warning · `sentence-length-variance`

**Detection:** Programmatic check `sentence-length-variance`. Computes the standard deviation of sentence word counts and fails when the SD drops below 4. Skipped on prose under 100 words and 6 sentences. Distinct from #34 paragraph-length uniformity (which measures paragraph block sizes, not sentence-level rhythm) and from #25 staccato (which targets very short standalone sentences regardless of variance).


### 59. One-line sections under headings

A heading followed by a single generic sentence, repeated across the document. Humanizer tooling treats the sentence under the heading as removable padding, which makes the shape itself the tell: sections open with a filler line instead of content. One deliberate short section is fine; the check needs the shape twice.

**Before:**
> ## Performance
>
> Speed matters.
>
> ## Security
>
> We take security seriously.

**After:**
> ## Performance
>
> The benchmark suite covers cold starts, warm paths, and the worst-case joins we see in production.

**Severity:** context_warning · `no-heading-one-liners`

**Detection:** Programmatic check `no-heading-one-liners`. Flags two or more headings each immediately followed by a paragraph consisting of a single sentence. Lists, blockquotes, and further headings do not count as the following paragraph.

---

## Voice and register

These patterns concern what AI **removes** from writing — stance, personality, specificity — rather than what it adds. LLMs systematically strip argumentative commitment and deplete personal voice even in minimal edits.

### 33. Countdown negation

**Words to watch:** "It wasn't X. It wasn't Y. It was Z.", "This isn't about... This isn't about... This is about..."

A multi-sentence rhetorical arc where AI negates two or more things before revealing the actual point, creating false suspense. Distinct from negative parallelism (#9), which is "not X; it's Y" in a single sentence. This is a sustained dramatic build.

**Before:**
> It wasn't the algorithm. It wasn't the data. It wasn't the compute budget. It was the prompt. Three words, chosen carefully, changed everything.

**After:**
> The improvement came from rewriting the prompt, not from changes to the model or data. The team had spent weeks on architecture changes before trying this.

**Before:**
> This isn't about technology. This isn't about efficiency. This is about what it means to be human in an automated world.

**After:**
> The automation question is less about the technology itself and more about how it changes the day-to-day work that people build their identity around.

**Severity:** context_warning · `no-countdown-negation`

**Detection:** Programmatic check `no-countdown-negation`.


### 34. Per-paragraph miniature conclusions

Every paragraph wraps up with a tidy summary sentence that transitions perfectly to the next. Humans digress, leave threads hanging, circle back later. AI's paragraph-level tidiness is itself a tell.

**Before:**
> The study surveyed 400 teachers across 12 districts. Most reported increased workload since 2020. The takeaway is clear: teachers are stretched thin and the trend shows no signs of reversing.
>
> The funding picture compounds this pressure. Per-pupil spending has risen by 4% nominally but fallen in real terms. This financial squeeze makes the workload problem even harder to address.

**After:**
> The study surveyed 400 teachers across 12 districts. Most reported increased workload since 2020, with marking and administrative tasks growing fastest.
>
> Per-pupil spending has risen by 4% nominally but fallen in real terms. Whether the two trends are connected is debatable, though several principals I spoke to thought so.

When you spot a paragraph where the final sentence restates the paragraph's point or transitions smoothly to the next topic, consider cutting it or replacing it with something that leaves a thread open.

Watch for endings such as "That is why...", "The takeaway is...", "The result is...", "In the end,...", "Ultimately,...", and "With that distinction in mind...". The deterministic candidate surface also recognises compact interpretive closures such as "The selection was already an interpretation" and balanced semicolon closures whose two halves each contain their own subject and linking verb. Literal states and subordinate fragments are controls. Quoted occurrences remain candidates and are marked as quoted. One can be legitimate. Three or more usually means the piece is landing every paragraph the same way.

Also check paragraph size. AI-generated longform often settles into near-identical blocks: ten paragraphs of 65-85 words, each making one balanced point. Human paragraphs usually show uneven pressure; some are short, some wander, some carry a scene or example longer than expected.

**Severity:** context_warning · `no-tidy-paragraph-endings` and context_warning · `paragraph-length-uniformity` (this pattern covers two related checks)

**Detection:** Programmatic check `no-tidy-paragraph-endings`.


### 35. Tonal uniformity / register lock

AI picks a register — professional-casual, academic-accessible, warm-but-authoritative — and never breaks from it. Human writers drift between registers: they start formal, get colloquial, make a joke that does not quite land, recover. The consistency is the tell, not any particular register.

**Before:**
> The architecture of the system reflects careful consideration of user needs. Each component has been designed with modularity in mind, allowing for straightforward maintenance. The team has prioritised clarity in the API surface, ensuring that developers can integrate with minimal friction.

**After:**
> The system is modular, which mostly works well. The API is clean — I got a prototype running in an afternoon, though I hit a wall with the auth flow that took longer to sort out. The docs say "straightforward" but that is doing some heavy lifting.

This pattern cannot be caught programmatically. During the self-audit, ask: does the whole text sit in one register? If it reads like a single voice speaking at a single speed about everything, introduce at least one register break — a moment of informality, a parenthetical doubt, a shift in sentence rhythm.

In reviews and criticism, tonal uniformity often appears as bland evaluative balance: "emotional range", "field of sympathy", "moral strength", "earns its weight", "ambitious in an old-fashioned way", "social texture", "slow revelation". Replace this with concrete claims about scenes, sentences, performances, or formal choices.

**Severity:** N/A · agent-judgement (registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `tonal_uniformity`, `referential_clarity` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`) — register lock is not regex-amenable.

### 35a. Orphaned demonstratives

**Words to watch:** "This highlights...", "This underscores...", "This demonstrates...", "That speaks to...", "These point to..."

The problem is not the word "this"; it is the vague subject. If "this" points to a whole previous paragraph, replace it with the actual noun or claim.

**Before:**
> The team missed the deadline and the launch slipped by three weeks. This highlights the importance of communication.

**After:**
> The missed deadline exposed a communication gap between product and engineering.

**Severity:** context_warning · `no-orphaned-demonstratives` (the related sentence-start chain check lives at #35b)

**Detection:** Programmatic check `no-orphaned-demonstratives`.


### 35b. Repeated 'This …' chains

Three or more consecutive sentences in a paragraph that begin with "This [verb]" — typically "This shows…", "This means…", "This highlights…", "This underscores…". Distinct from #35a orphaned demonstratives, which catches a single vague-subject `this` sentence; #35b is the chain pattern, where a paragraph keeps using `This` as the subject placeholder sentence after sentence.

**Before:**
> The framework launched in March. This brought consolidation. This reduced operational cost. This freed engineering time. This let the team focus on the next initiative.

**After:**
> The framework launched in March, consolidating tooling that had drifted across three teams since 2024. The reduced operational cost is what gave engineering room to focus on the next initiative.

**Severity:** context_warning · `no-this-chains`

**Detection:** Programmatic check `no-this-chains`. Walks each paragraph and flags 3+ consecutive sentences matching `^this\s+(?!is)\w+`. Distinct from #35a orphaned demonstratives (single-sentence vague-subject `this`); #35b is the multi-sentence chain pattern within a paragraph.


### 36. Faux specificity

AI provides examples that feel specific without actually being specific. "The way your coffee smells before you even take a sip" or "how the light hits your kitchen table in the morning" — plausible, relatable, grounded in nobody's actual experience. AI constructs these from genre conventions rather than lived experience.

Related to experiential vacancy (see Personality and soul in SKILL.md) but names the active mechanism: AI **performs** specificity rather than achieving it.

**Before:**
> There is something about the way a handwritten letter feels in your hands — the weight of the paper, the slight smudge of ink, the care in every stroke. It reminds you that someone took the time to sit down and think of you.

**After:**
> My grandmother wrote to me every month until she died. Her handwriting got worse each year — by the end I could only read about half the words. I kept every letter in a shoebox under my bed.

When you spot a "specific" detail, ask: could anyone have written this, or does it come from a particular person's experience? If it reads like a stock photo in prose form, replace it with something that could not have been generated from genre conventions.

**Severity:** N/A · agent-judgement (registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `faux_specificity` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`) — distinguishing genuine specificity from genre-convention filler is not regex-amenable.


### 37. Neutrality collapse

LLMs systematically strip argumentative stance, defaulting to balanced treatment of everything. "There are compelling arguments on both sides" where the original had a clear position. Distinct from generic positive conclusions (#24) — this is about the **removal** of opinion, not the addition of optimism.

LLM use sharply increases the share of essays that remain neutral, and LLMs frequently change the writer's conclusions even when instructed to only fix grammar.

**Before (human original):**
> Remote work is better for most knowledge workers. The evidence is overwhelming and the objections are mostly about control, not productivity.

**After AI "editing":**
> Remote work offers several advantages for knowledge workers, though in-office collaboration also has its merits. The evidence suggests benefits in both directions, and the optimal approach likely depends on the specific context and team dynamics.

**How to fix:**
> Remote work is better for most knowledge workers. The productivity data from Stanford and Owl Labs both point the same way, and the main counterarguments — spontaneous collaboration, mentorship, culture — have not held up well in studies that actually measured them.

When rewriting, compare your rewrite's conclusions to the input's conclusions. If the stance shifted toward neutral, you have introduced the same distortion the research documents. Restore the original position.

**Severity:** N/A · agent-judgement (registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `neutrality_collapse` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`). The surface false-balance phrasing piece is partly covered by `check_false_concession` (#23a); expanding regex coverage of stance erasure is out of scope here.

### 39. Template and placeholder residue

**Words and structures to watch:** `{client_name}`, `[Company Name]`, `[insert date]`, `<source>`, "Hi {name}", `Insert Table 1 here`, `turn0search0`, private-use citation wrappers, `_generated-reference-identifier_`, `contentReference`, `oaicite`, `oai_citation`, source-name `+1` suffixes, `[attached_file:1]`, `[web:1]`, Grok citation-card markup, `【85†L261-269】`, `[cite: 3, 12]`, `attributableIndex`, and `:::writing{...}`.

These are unfinished template, publishing, citation, or rendering residues. Replace placeholders with real values when known, remove production instructions from finished prose, and strip platform markup while preserving any underlying source information.

**Severity:** hard_fail · `no-placeholder-residue`

**Detection:** Programmatic check `no-placeholder-residue`.

### 40. Rubric echoing

**Words to watch:** "the author creates a tone", "I can tell because", "this quote shows that", "according to the rubric", "meets the criteria".

Common in AI-generated student essays. It mirrors assignment language instead of analysing the text. Preserve only if the piece is explicitly about the rubric.

**Severity:** context_warning · `no-rubric-echoing`

**Detection:** Programmatic check `no-rubric-echoing`.

### 41. Genre-specific manual checks

These are not reliable enough for hard regex treatment yet, but they should be part of the self-audit:

- **Academic/research:** verify citations, DOIs, dates, journals, reference order, figure/data consistency, and whether cited works actually support the claim. Plausible citation format is not evidence. In argumentative academic prose, also watch for depleted engagement markers such as missing questions, reader address, personal asides, or stance-bearing commentary.
- **Student essay:** watch for rubric language echoing back, banal thesis claims, weak or missing evidence, student-level mismatch, abrupt tone or complexity shifts, surface polish masking weak argument, draft-history gaps, and loss of the student's own interpretive agency.
- **Poetry:** watch for default quatrains, unrequested rhyme, first-person plural overuse, mood-word accumulation, form compliance without pressure, process traces that look too neat, and revisions that do not deepen the poem.
- **Fiction:** watch for flattened dialogue, "as-you-know" exposition, weak voice differentiation, parenthetical stage directions, locked POV with no pressure, scene pacing that never surprises, over-resolved endings, and generic fidelity to a target style without the source author's stranger choices.
- **Journalism:** verify unsupported claims, vague sourcing, fake or disappearing bylines, synthetic headshots, broken links, wrong dates, unverifiable quotes, undisclosed vendor or affiliate provenance, and article facts that cannot be traced to named sources.
- **Marketing/email:** watch for placeholders, generic subject lines, fake personalisation, weak domain understanding, exaggerated transformation claims, empty hype verbs, over-warm openings, unsupported business jargon, and action lists dressed up with symbols.

**Severity:** N/A · agent-judgement (polymorphic genre slot; registered in `human-eyes/scripts/judgement.json`)

**Detection:** Agent judgement `genre_specific` (scripts/judgement.json). Reserved for the agent-judgement registry (`human-eyes/scripts/judgement.json`) as a polymorphic genre slot — the agent first detects genre (academic, student essay, poetry, fiction, journalism, marketing/email, or default), then runs the matching watchlist.


### 43. Corporate AI-speak

**Words to watch:** "delivering impact", "measurable outcomes", "deliverable outcomes", "scalable, production-grade", "pragmatic approach", "drives outcomes", "cross-functional", "end-to-end (development|delivery|solution)", "translate requirements into outcomes/deliverables/solutions", "stakeholder (alignment|engagement|management)", "actionable insights", "leverage (my|our|the) experience/expertise".

Generic LinkedIn-AI corporate register. Hides specific work behind operational abstractions: "delivers", "drives", "leverages", "aligns". Often clusters in CVs, capability decks, vendor pitches, and "who we are" pages where the writer wants to sound credible without naming any actual project.

**Before:**
> Our cross-functional team leverages decades of expertise to deliver measurable outcomes through end-to-end execution and stakeholder alignment, driving actionable insights for our partners.

**After:**
> The team includes designers, engineers, and customer researchers. We worked with three local councils on their tax-collection workflows; the redesign cut average resolution time from 14 days to 6 over six months.

**Severity:** strong_warning · `no-corporate-ai-speak`

**Detection:** Programmatic check `no-corporate-ai-speak`.


### 45. Nonliteral land/surface phrasing

**Words to watch:** "the argument lands", "the idea lands", "your point lands", "where my draft landed", "lands with the reader/audience/team/stakeholders", "lands in the rubric/scale/category", "surfaces in the conversation/discussion/debate/work/writing", "what surfaces", "what surfaced", and nonliteral navigation constructions such as a manual becoming "a map out of the wilderness", a framework providing "a roadmap through uncertainty", or a guide becoming "a compass through the maze".

Treats abstract ideas as physical objects that land or surface, or turns informational objects into maps and compasses through figurative terrain. Detection surfaces the construction for contextual review; it does not decide that a grounded metaphor is artificial or must be removed. Literal maps, compasses, wildernesses, and product roadmaps remain outside the match. Distinct from #30 generic metaphors, which requires agent assessment of whether figurative language is plausible-but-unanchored.

**Before:**
> The argument lands somewhere between cautious optimism and quiet despair. What surfaces in the discussion is a recognition that no clean answer exists.

**After:**
> The argument is cautious — the writer thinks the policy will work but is not willing to predict by how much. Three of the seven examples she cites support the optimistic reading; the other four are ambiguous.

**Severity:** strong_warning · `no-nonliteral-land-surface`

**Detection:** Programmatic check `no-nonliteral-land-surface`.


### 46. Bland critical template

**Words to watch:** "the kind of contemporary novel/film/book/album/show/essay that", "doing several familiar things at once", "what makes it more than", "emotional range", "field of sympathy", "moral strengths", "earns (much of) its weight", "ambitious in an old-fashioned way", "social texture", "slow revelation of", "difficult to dismiss".

Generated literary, film, or review criticism that sounds balanced but generic. Replaces concrete claims about scenes, sentences, performances, or formal choices with portable evaluative phrases. The hallmark is a sentence that could appear in a review of any contemporary novel/film without changing a word.

**Before:**
> Tóibín's novel is the kind of contemporary book that earns its weight through emotional range and slow revelation, doing several familiar things at once with a social texture that is difficult to dismiss.

**After:**
> The opening forty pages stay close to Henry's silences — when his mother asks why he won't write home from Rome, he changes the subject three times in two paragraphs. That refusal is the book's structural engine, not its theme.

**Severity:** strong_warning · `no-bland-critical-template`

**Detection:** Programmatic check `no-bland-critical-template`. Closely related to #35 tonal uniformity in reviews and criticism — the tonal-uniformity entry mentions the same evaluative phrases ("emotional range", "field of sympathy", "moral strength") as a register signal; this check enforces them at phrase level.


### 51. Mechanical repeated sentence starts

Three or more consecutive sentences whose first word matches — "The X… The Y… The Z…", "We did… We saw… We learned…", "It was… It was… It was…". Anaphora is a real rhetorical device when it earns its weight (Lincoln, Churchill, Baldwin), but AI reaches for it as a default rhythm pattern when it has run out of structural ideas. The tell is repetition without escalation: three sentences starting the same way that do not build, contrast, or accumulate force.

**Tolerance note:** Deliberate anaphora is one of the oldest rhetorical figures in English. Preserve when the repetition is doing structural work — building, contrasting, intensifying — or when it is character voice, oratory, or quoted speech.

**Before:**
> The team adopted the new framework. The team rewrote the docs. The team trained the support staff. The team rolled out the migration in three phases.

**After:**
> Adopting the new framework meant rewriting the docs and training the support staff before the team could roll out the migration in three phases.

**Severity:** context_warning · `no-anaphora`

**Detection:** Programmatic check `no-anaphora`. Flags three or more consecutive sentences whose first word matches case-insensitively, ignoring trivial starts ("I", "A", "The", "It", "It's"). Distinct from #25 staccato rhythm (which fires on short standalone sentences regardless of opener) and from #35a orphaned demonstratives (vague-subject `this` in a single sentence) and #35b `This …` chains (paragraph-level repetition of `This` as subject).


### 56. Performed candour and vulnerability

**Frames to watch:** Honestly,; To be honest; The honest answer; Frankly,; Candidly,; Truthfully,; In all honesty; "I wasn't going to post this, but"; "This is scary to share"; "Hot take incoming (don't hate me)"; "Unpopular opinion"; "I know I'll get hate for this, but"; "I've never said this publicly before"; "This might ruffle some feathers"; "I might lose followers for this, but".

These phrases announce sincerity, vulnerability, or anticipated backlash before a claim. The announcement rarely changes the meaning and gives prose a rehearsed authenticity beat. Literal uses remain valid: an honest account is not performed candour. Quoted source text also remains unchanged.

**Before:**
> To be honest, the review process is too slow.

**After:**
> The review process is too slow.

**Severity:** strong_warning · `no-performed-candour`

**Detection:** Programmatic check `no-performed-candour`. The `performed_candour` semantic record reviews contextual uses of honest, real, actual, and genuine.


### 58. Mechanical repeated paragraph starts

The paragraph-level sibling of #51: three or more consecutive paragraphs whose first word matches. Peer-reviewer guidance flags identical paragraph starts and rigid paragraph patterns as overly uniform structure. As with sentence-level anaphora, deliberate rhetorical patterning exists; the tell is repetition without escalation.

**Before:**
> Customers want faster onboarding and clearer pricing pages.
>
> Customers also expect the invoice history to export cleanly.
>
> Customers who churn cite the same three support gaps.

**After:**
> Customers want faster onboarding, clearer pricing, and invoices that export cleanly. The ones who churn cite the same three support gaps.

**Severity:** context_warning · `no-paragraph-anaphora`

**Detection:** Programmatic check `no-paragraph-anaphora`. Flags three or more consecutive prose paragraphs whose first word matches case-insensitively, ignoring trivial starts ("I", "A", "The", "It", "It's"). Headings, list blocks, and blockquotes are not paragraphs and do not break a run. Distinct from #51, which works on consecutive sentences.

---

## Signal stacking (meta-check)

The grader also runs one meta-check that does not correspond to a single AI tell.

`overall-signal-stacking` rolls up several weak/medium signals into a single signal-stacking score. The component checks are:

- manufactured insight framing (#42)
- contrived contrast / negative parallelism (#9)
- formulaic openers (#50)
- soft scaffolding (#47)
- section scaffolding (#38)
- tidy paragraph endings (in #34)
- paragraph length uniformity (in #34)
- markdown headings in prose
- excessive lists (#31)
- assistant residue / collaborative artifacts (#19)
- generic conclusions (#24)
- bland critical template (#46)
- false concession (#23a)

Plus Kobak et al. excess-vocabulary evidence (style-annotated terms from the `kobak-excess-words.csv` reference file).

The check fires when the weighted score crosses the threshold of four points. Vocabulary and structural signals both contribute points and neither family is required on its own; vocabulary evidence carries few points, so it tips the score rather than deciding it, consistent with Kobak et al.'s corpus-level logic that excess vocabulary is evidence in a pattern rather than a verdict. Individually, each component may be weak; their combination indicates a generated piece that has been polished enough to dodge any single regex.

**Severity:** context_warning · `overall-signal-stacking`


**Detection:** Programmatic meta-check `overall-signal-stacking`. Not numbered as a single AI tell; rolls up the components above. The check exposes its component breakdown and Kobak vocabulary profile in its evidence so the writer can read which signals contributed.
