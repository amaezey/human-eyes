# AISLOPOPEDIA: The Complete Encyclopedia of AI-Generated Slop

## Metadata

- **URL:** https://aislopopedia.com/
- **Author / owner:** `@Saboo_Shubham_` (page metadata and footer)
- **Published:** Undated living website; footer says `© 2024`; reviewed 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** Satirical practitioner catalogue and interactive self-scoring website
- **Evidence tier:** Practitioner / editor catalogue
- **Extraction status:** Complete rendered-text capture. The 26 labelled groups contain 217 examples. The expanded confession and all ten page sections are in `snapshots/saboo-aislopedia.md`.

## What this source is useful for

AISLOPOPEDIA is a catalogue of constructions that make social and promotional prose sound AI-generated: staged revelations, binary pivots, manufactured urgency, performed vulnerability, engagement bait, generic comments, inflated corporate vocabulary, formulaic endings, and fill-in-the-blank post templates.

For human-eyes, the relevant question is whether a construction produces a recognisable AI-writing effect. The fact that humans also use a phrase does not disqualify it. Human use matters only when defining the match boundary, severity, exceptions, and rewrite—not when deciding whether the tell belongs in the catalogue.

The source is not evidence of authorship and human-eyes does not classify authorship. Its value is stylistic coverage: it gives us candidate constructions, surface variants, functional families, and rewrite targets.

## Extraction and comparison method

- The full rendered page was captured, including all 217 examples across 26 labelled families.
- Every example was mapped to the current pattern catalogue, executable checks in `human-eyes/scripts/grade.py`, and genre guidance in `human-eyes/scripts/judgement.json`.
- Every example was also run as isolated prose through the current executable checks after replacing illustrative placeholders such as `[X]`.
- “Documented” and “executable” are kept separate. A phrase appearing in `patterns.md` or another source card is not counted as detected unless the live checker surfaces it.
- The isolated probe found 28 immediate matches out of 217 examples. A further group contributes below-threshold vocabulary or emoji candidates. This means current coverage is strongest for a few established structures but weak across the source’s social-post rhetoric.

## Net new coverage

The source adds substantial material rather than a handful of edge cases.

- **Already substantially covered:** escalation ladders; several negative-parallelism forms; `let that sink in`; `read that again`; some manufactured-revelation phrases; some AI vocabulary; clustered emoji and staccato structures.
- **Partially covered and needing extensions:** throat-clearers; false-exclusivity hooks; binary contrasts; dramatic fragments; pivot phrases; qualifier sandwiches; generic closers; mic drops; corporate vocabulary; sentence templates.
- **Largely absent as executable checks:** manufactured urgency; performed vulnerability/backlash framing; false-agency clichés; calls to action; generic agreement and engagement-farming comments; humble brags; `I asked ChatGPT` post templates; time-lapse brags; artificial-scarcity claims.
- **Not suitable for incorporation:** the site’s equal-weight self-score and authorship labels. Human-eyes reports constructions and edits; it does not produce an authorship score.

## Mapping by source section

### 1. The Openers

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Throat-clearers (10) | Partial overlap with #42 manufactured insight, #50 formulaic openers, and #56 performed candour; 4/10 isolated examples trip. | Generic spoken openers and several contractions are absent. | Extend opener recognition for `can we talk about`, `let's talk about`, `we need to talk about`, `I need to say`, and contracted `nobody's/no one's talking about`. Surface the staging and rewrite by deleting it or stating the claim directly. |
| False-exclusivity hooks (10) | Conceptually adjacent to #42; 0/10 isolated examples trip. | Secrecy, suppressed-information, insider-access, and “nobody tells you” hooks are a distinct missing family. | Add an engagement-hook family covering `most people won't tell you`, `the thing nobody tells you`, `secret [industry] doesn't want you to know`, under-the-radar, and withheld-information frames. Rewrite as the actual fact plus evidence. |
| Manufactured urgency (9) | Adjacent to promotional language and dramatic transitions; 0/9 trip. | The current checker does not recognise artificial time pressure, takedown claims, save/bookmark pressure, or instant game-change framing. | Add urgency-hook patterns such as `stop what you're doing`, `save this before`, `you need to see this`, and `changed the game forever`; extend #32 to `this changes everything`. Rewrite with the real deadline or remove the pressure. |

### 2. The Body Patterns

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Binary contrast (10) | #9 negative parallelism and #42 catch about half; 5/10 trip. | Cross-sentence `isn't just A. It's B`, imperative stop/start and forget/focus forms, and old/new replacements are incomplete. | Extend #9 with the missing syntactic forms, including `Stop thinking of X; start thinking of Y`, `Forget X; focus on Y`, and `Most people think X; actually Y`. Rewrite as one supported claim rather than a staged reversal. |
| Numbered-list hooks (6) | #31 and #38 examine list density and scaffolding; 0/6 isolated hooks trip. | AISLOPOPEDIA identifies the packaged `N lessons/mistakes/pillars/frameworks` hook itself as a social-post tell. | Add a headline/template candidate that combines numbered-hook wording with generic lesson/framework nouns. Rewrite the headline to name the actual subject and make the list items carry information. |
| Dramatic fragmentation (9) | #25, #42, and #51 catch 3/9. | Exact mic-drop fragments such as `Full stop`, `Sit with that`, and `Think about that` are absent. | Add the exact emphasis crutches as candidates without lowering the structural staccato threshold. Rewrite by deleting the command or stating the consequence it is pretending to emphasize. |
| Performed vulnerability (9) | #56 catches honesty framing; 1/9 trips. | Scary-to-share, anticipated-backlash, unpopular-opinion, follower-loss, and feather-ruffling frames are missing. | Add a performed-vulnerability/backlash family. The check concerns rhetorical performance, not whether the speaker truly feels vulnerable. Rewrite by naming the actual risk, disagreement, or evidence. |
| False agency (10) | Only incidental overlap with significance inflation; 1/10 trips. | `data speaks`, `numbers don't lie`, `market has spoken`, `AI is coming`, and analogous agency clichés are not represented as a family. | Add an evidence-free agency cliché family. Rewrite by naming who interpreted the data, what the numbers show, or which observed change supports the claim. |
| Ladder of escalation (4) | Strong coverage through staccato, anaphora, and triad checks; 4/4 trip. | No important new mechanism. | Add examples as fixtures and source support; no new check family is needed. |

### 3. The Transitions

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Pivot phrases (11) | #42 and #32 catch 4/11. | `And here's the kicker`, `but wait`, `plot thickens`, `enter: X`, `wait until you see`, and `just the beginning` are missing. | Extend manufactured-insight and dramatic-transition surfaces. Rewrite by expressing the logical connection directly. |
| Qualifier sandwiches (9) | Filler, hedging, and #23a catch 1/9. | `I'm not saying X, but Y`, `don't get me wrong`, `to be fair`, `that said`, and `this isn't to say` are underrepresented. | Extend #23a beyond formal both-sides templates to disclaimer pivots. Surface the qualification and rewrite it as a precise limitation or remove it when it merely cushions the next claim. |

### 4. The Closers

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Call-to-action slop (10) | Emoji may contribute a below-threshold candidate; 0/10 calls to action trip. | Comment/follow/repost/share/save/tag/subscribe endings are a missing social-post style family. | Add a CTA/engagement-bait check for formulaic platform endings. Rewrite by removing the engagement command or replacing it with a specific, necessary request. |
| Fake philosophical closers (9) | Adjacent to #24 and #32; 0/9 trip. | `we're still early`, `just the beginning`, `buckle up`, `welcome to the future`, and stock genie/cat endings are not recognised. | Add generic philosophical-future closers as closing-position candidates. Rewrite with a concrete implication, next step, or final fact. |
| Performative mic drops (8) | #9/#42 catch 2/8. | `Think about that`, `Act accordingly`, `new normal`, and `X will never be the same` are absent. | Add an emphatic-closer family, including closing-position matching for `Act accordingly` and `will never be the same`. Delete the pose or state exactly what changes. |

### 5. Comment Section Classics

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Agreement slop (8) | Conceptually related to #19 collaborative artifacts; 0/8 trip. | `Couldn't agree more`, `you nailed it`, `spot on`, and empty restatements are not covered. | Add a social-comment agreement family. The rewrite should add the reason, evidence, example, or disagreement instead of generic affirmation. |
| Engagement-farming comments (6) | No executable comment branch; 0/6 trip. | Credential-led replies, `counterpoint`, `respectfully disagree`, and reply invitations form a missing family when they add no substance. | Add comment-specific candidates and a semantic review of whether the comment contributes anything beyond the engagement move. |
| Humble-brag responses (4) | Adjacent to faux specificity; 0/4 trip. | CEO/team/tenure/conference credentials used as comment theatre are missing. | Add a credential-preface/humble-brag family for social comments. Rewrite by giving the relevant observation directly and retaining the credential only when it establishes necessary context. |

### 6. The Emoji Patterns

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Strategic single emoji (10) | #31a records 9/10 as candidates but deliberately requires a cluster. | `⚡` is missing from the recognised set. The source also clarifies social-post placement patterns. | Add `⚡`; keep single-symbol evidence separate from the cluster decision. Use placement and repetition as supporting evidence. |
| LinkedIn bullet emoji (6) | #31a records 5/6; #31 catches real list density. | `➡️` and, elsewhere on the page, `♻️` are missing. | Add `➡` and `♻` with variation-selector support. Retain the existing aggregation rule. |

### 7. The Meta-Patterns

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| `I asked ChatGPT` posts (5) | 0/5 trip. | This is a recognizable formulaic social-post wrapper even though it openly discusses AI. | Add a meta-post template family for `I asked ChatGPT to`, `ChatGPT gave me`, and staged prompt/result reveals. Rewrite as the actual experiment: prompt, output, method, result, and limitation. |
| Time-lapse brags (5) | Adjacent to promotion/faux specificity; 0/5 trip. | `X hours became Y minutes` and compressed-time achievement frames are missing. | Add a compressed-time brag family. Rewrite with the actual task, baseline, output quality, and constraints. |
| Artificial scarcity (5) | Adjacent to promotion; 0/5 trip. | Exhaustive-curation and “I read/analyzed everything so you don't have to” hooks are missing. | Add an artificial-scarcity/research-theatre family. Rewrite with the real selection method, sample size, and result. |

### 8. The Word Crimes

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Adverbs (13) | Five appear in current lexical evidence; one trips alone. | The source supplies a compact social-copy intensifier list beyond the current vocabulary set. | Add missing high-salience items to vocabulary clustering or a social-copy intensifier subfamily. Keep them as candidates whose effect strengthens in clusters. |
| Adjectives (11) | Eight appear in lexical evidence; one trips alone. | `revolutionary`, `next-level`, and `world-class` are not effective standalone candidates; `world-class` currently matters only inside a three-compound density check. | Add these to promotional/corporate vocabulary candidates and rewrite with the measurable property being claimed. |
| Verbs (10) | Four are lexical candidates; phrase-scoped leverage is executable; the rest are weak or absent. | `synergize`, `supercharge`, `reimagine`, `spearhead`, and `double down` are missing or only represented indirectly. | Add the missing corporate action verbs as clustered vocabulary; add phrase-scoped corporate matches where the construction itself is generic. Preserve literal technical senses through contextual exceptions. |

### 9. The Sentence Templates

| Source family | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Fill-in-the-blank templates (10) | Only 1/10 instantiated examples trips. | The checker misses several recognizable social-post skeletons: `X isn't just A. It's B`, stop/start, `X is the new Y`, old-method/behind, thrive/left-behind, and short-time/long-time contrasts. | Add syntactic template recognizers rather than matching literal brackets. Give each the same rewrite target: remove the staged binary or prophecy and state the supported claim. |

### 10. The Severity Scale

| Source component | Current coverage | What is different | Incorporation route |
|---|---|---|---|
| Five self-score bands | No direct mapping; signal stacking is architecturally different. | The page treats remembered phrases as equally weighted and turns the count into an authorship joke. | Do not import the score. Incorporate the phrase families into human-eyes findings and rewrites while retaining the project’s existing output contract. |

## Concrete checker changes suggested by the comparison

### Extend existing checks

1. **#42 manufactured insight:** add contraction variants; `And here's the kicker`; `Full stop`; `Sit with that`; `Think about that`; additional secrecy and false-exclusivity hooks.
2. **#9 negative parallelism:** add cross-sentence `isn't just A. It's B`, stop/start, forget/focus, most-people/actually, old/new, and thrive/left-behind templates.
3. **#23a false concession:** add `I'm not saying X, but Y`, `don't get me wrong`, and equivalent disclaimer pivots.
4. **#32 dramatic transitions:** add `this changes everything`, `X will never be the same`, `just the beginning`, and related present-tense variants.
5. **#24 generic conclusions or a sibling closer check:** add philosophical future closers and mic-drop commands, with closing-position recognition.
6. **#31a unicode flair:** add `⚡`, `➡`, and `♻` while preserving variation-selector handling and the existing aggregation behavior.
7. **#43 corporate AI speak / #7 vocabulary:** add phrase-scoped or clustered uses of `synergize`, `supercharge`, `reimagine`, `spearhead`, `double down`, `world-class`, and `next-level`; keep `leverage` coverage and broaden its generic corporate constructions.

### Add missing functional families

1. False-exclusivity and manufactured-urgency hooks.
2. Performed vulnerability and anticipated-backlash framing.
3. Evidence-free false-agency clichés.
4. Formulaic social calls to action and engagement bait.
5. Empty agreement, engagement-farming, and credential-preface comments.
6. Time-compression brags and artificial-scarcity research theatre.
7. Formulaic `I asked ChatGPT` prompt/result posts.
8. Generic philosophical and mic-drop closers.
9. Fill-in-the-blank social-post sentence skeletons.

These can be programmatic candidates with genre and position metadata, followed by the project’s normal contextual interpretation. They do not need to be postponed merely because humans also use them.

## Rewrite logic contributed by the source

- **Staged hook:** remove the throat-clearing and state the claim.
- **False exclusivity:** replace insider theatre with the fact and its source.
- **Urgency:** name the real deadline or remove the pressure.
- **Binary pivot:** replace the staged reversal with one accurate relationship.
- **Vulnerability/backlash:** name the actual risk or disagreement.
- **False agency:** name the actor, measurement, or inference.
- **Pivot phrase:** write the causal or logical connection.
- **Qualifier sandwich:** state the real limitation precisely.
- **CTA:** remove engagement farming or make the request specific.
- **Generic comment:** add a reason, example, evidence, or genuine counterpoint.
- **Humble brag:** remove the credential frame unless it is necessary context.
- **Time/scarcity brag:** state method, scope, baseline, result, and constraint.
- **Corporate vocabulary:** replace status language with the concrete action or property.
- **Philosophical/mic-drop ending:** end on the concrete implication or fact.

## Evidence limits

The site supplies no corpus, model versions, prompts, frequencies, annotation protocol, or validation study. Those omissions limit claims about prevalence and model attribution. They do not erase the catalogue’s usefulness as a practitioner inventory of AI-sounding constructions. The source should support candidate discovery and examples, while the project’s own checks determine match boundaries, severity, and rewrites.
