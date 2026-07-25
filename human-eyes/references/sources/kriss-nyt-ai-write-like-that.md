# Sam Kriss: Why Does A.I. Write Like … That?

## Metadata

- **URL:** https://www.nytimes.com/2025/12/03/magazine/chatbot-writing-style.html
- **Author / owner:** Sam Kriss / The New York Times Magazine
- **Published:** 2025-12-03; print version 2025-12-21
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** Magazine essay / journalism
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** Current: web article published 2025-12-03, with print version on page 36 of the 2025-12-21 Sunday Magazine under the headline “The Omniwriter”; previous library capture: complete Jina Reader Markdown retrieved 2026-05-05; no publisher revision identifier exposed
- **Full-text status:** complete
- **Snapshot:** `snapshots/kriss-nyt-ai-write-like-that.md`
- **Extraction method:** Complete 2026-05-05 Jina Reader capture preserved and rewrapped under `SNAPSHOT_TEMPLATE.md`; current canonical `curl` and Jina routes returned 403 responses, so title, metadata, paragraph order, and the beginning, middle, and end were rechecked against the search-indexed full-page archive at `https://archive.ph/yqd1G`
- **Snapshot SHA-256:** `41665c6c2456782c75e5bb4e89fa309950badcb67edaec789de44358670e68f4`
- **Model / corpus scope:** Kriss's personal examples span the original GPT in 2019, ChatGPT after its late-2022 launch, an early version of ChatGPT-5 identified only through the article, Grok, Claude, and the 2023 Bing chatbot. Prompts are quoted or paraphrased, but dates, builds, settings, repetitions, and complete raw outputs are generally absent. Indirect evidence covers PubMed abstracts in 2022-2024, political statements and parliamentary transcripts, a Society of Authors survey, a poetry-preference study, and a reported Max Planck analysis of more than 360,000 academic YouTube videos. Genres include fiction, poetry, chat, public statements, academic abstracts, corporate notices, social posts, email, and marketing copy; language is English.
- **Access limitations:** No substantive article prose is omitted. Current direct HTML was blocked by DataDome and current Jina Reader access by abuse controls. The five decorative illustration binaries and audio are not preserved; their URLs, available alt text, credits, and the 25:47 runtime are recorded. Most generated examples lack reproducible model/build settings, and the upstream studies and posts reported by the essay are indirect evidence unless separately captured in their own source records.

## Summary

Kriss's 4,713-word New York Times Magazine essay combines personal model use, close reading of generated examples, public cases, and reported studies to describe a conspicuous AI-associated register. Its useful direct evidence is a dated set of prompts, outputs, counts, counterexamples, and craft distinctions covering negative parallelism, em dashes, clustered vocabulary, spectral and quiet imagery, textile and journey metaphors, tricolons, canned rhetorical questions, generic roast formulas, forced synesthesia, and false profundity. Its strongest contribution to human-eyes is the boundary running through the essay: these constructions have long human histories, vary by model, genre, and English variety, and can spread into human language, so they cannot establish authorship. Mechanism, prevalence, preference, and language-change claims are reported or interpretive rather than independently demonstrated by this article.

## Main insights

- The opening deliberately stacks the essay's candidate cues, but the article repeatedly supplies human, regional, political, literary, and socially transmitted look-alikes.
- Kriss's 2019 GPT examples differ sharply from his later chatbot examples, making model and time scope material rather than incidental.
- The em dash and `not X, Y` family are presented as publicly salient cues, while human political communications, literary prose, the Bible, and Shakespeare prevent categorical use.
- The essay reports measurable post-ChatGPT vocabulary changes, then gives `delve` a Nigerian-English counterexample and frames cultural-transfer mechanisms as explanation rather than proof.
- Direct creative-writing examples support bounded review of names, spectral language, quietness, textile/journey imagery, tricolons, rhetorical questions, `X with Y and Z` insults, sensory abstractions, and generic profundity.
- Several examples are explicit negatives: the early GPT's accidental humour did not survive the assistant transition; the early Simpsons/tickling behaviour is said no longer to occur; AI prose can be predictable and nonsensical at once; and source attribution is often suspicion rather than verification.
- The concluding coevolution claim makes provenance inseparable from style: humans may reproduce AI-associated language without using AI on the document under review.

## Evidence and claims to extract

- **Direct source reviewed:** Complete New York Times Magazine web article published 2025-12-03, as preserved in the 2026-05-05 Jina Reader capture and reverified on 2026-07-16 against the search-indexed full-page archive; 38 author-prose paragraphs, two quoted-example blocks, five illustrations, and the print note were checked.
- **Method and sample:** Literary criticism and journalism based on Kriss's personal use of several unnamed or partially named model versions, selected model outputs, public statements, a viral social story of unknown provenance, a Reddit excerpt, a repeated Starbucks notice, and secondary reporting of surveys and studies. This is not a controlled sample, systematic model comparison, detector evaluation, or prevalence study. Prompt wording, settings, repetitions, selection method, and complete outputs are mostly missing.
- **Direct versus cited evidence:** C01-C07 and C11-C19 are the essay's direct observations, examples, and interpretations, with directness qualifications inside each row. C08-C10 and C20-C21 report corpus, register, transcript, preference, or coevolution evidence from other work. C03 and C19 also include reported institutional or corporate cases. C22 is the essay's synthesis from direct and cited material.
- **Important limits and counterexamples:** Old human uses of em dashes and negative parallelism; literary and political genre; Nigerian English; model drift; unknown model/build settings; prompted and selected outputs; an unattributed viral story; unverified authorship of political, Reddit, and Starbucks text; indirect quantitative results; and language feedback from models into humans. The essay supplies no document-level threshold, accuracy measure, causal model, or authorship proof.

## Skill-use audit

- **Good use:** Treat the source as dated journalism and craft criticism for candidate recognition, quoted examples, model/version metadata, genre branches, public-tell drift, human look-alikes, and the no-authorship boundary.
- **Misuse / overclaim:** Do not use one em dash, `delve`, a tricolon, a ghost, or any other named cue to infer who or what wrote a document. Do not treat Kriss's mechanism explanations or suspicions about political, Reddit, Starbucks, or viral text as verified provenance.
- **Unsupported use:** Universal rates, current-model behaviour, a document threshold, model attribution, a detector score, poetry preference, AI-use prevalence, cultural-transfer causality, regional-English classification, or a claim that models cannot produce grounded sensory writing.
- **Underused evidence:** The live product incompletely represents source/date/model scope, a single-question example, `soft`/`hum` quietness vocabulary, the `X with Y and Z` dismissive formula, unknown-provenance examples, indirect-evidence labels, and style contagion into human speech.
- **Patterns left on the table:** A future genre-aware evaluation of the dismissive `X with Y and Z` formula, explicit separation of detected candidate from verified provenance, and source-specific handling of public-tell drift and human adoption. None is ready for product implementation from this essay alone.

## Matched patterns / rules

- `no-ai-vocabulary-clustering` (#7); partial coverage, with a three-item paragraph threshold and no register-specific source profile.
- `no-negative-parallelisms` (#9), `no-countdown-negation` (#33), and `no-staccato-sequences` (#25); direct structural overlap, including `No X. No Y. Just Z.`, but no automatic distinction between AI-associated and deliberate human uses.
- `no-forced-triads` (#10); partial and challenged coverage. The exact viral excerpt's three sentence-level tricolons produce zero #10 candidates, while the separate Bing quotation produces three coordinated-list candidates; neither short excerpt reaches #10's density threshold.
- `no-ghost-spectral-density` (#26) and `no-quietness-obsession` (#27); partial direct overlap. The quietness catalogue names `hum`, `humming`, and `soft`, but the executable check does not.
- `forced_synesthesia` (#28), `generic_metaphors` (#30), `semantic_redundancy` (#34), and `genre_specific` (#41); agent-assessed contextual overlap.
- `no-rhetorical-questions` (#29); full coverage for the approved fragment-question answer beat, with one complete occurrence producing a finding.
- `no-manufactured-insight` (#42) and `no-significance-inflation` (#1); partial overlap with empty profundity, not an exact meaning or coherence assessment.
- `no-em-dashes` (#49); exact glyph recognition, but the source's human controls and no-proof statement challenge fail-on-any generic interpretation.
- Product boundary in `human-eyes/references/process.md`; fully covers the rule that reports must not infer authorship.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H9: Field-guide voice with similar-species disambiguation per pattern.
- H12: Genre-aware threshold calibration.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
- H27: Performative profundity and aphoristic closure.

## Questions / follow-up

- Ingest the exact poetry-preference study and the Max Planck spoken-language paper separately before using C20-C21 as project evidence.
- Reconcile the Nigerian-English explanation in C09 with the separately reviewed Juzek and Ward English-variety null before any mechanism wording.
- Decide whether C15's `X with Y and Z` construction merits matched, genre-aware evaluation with comedy and human-insult controls.
- Decide whether the #27 documentation/runtime drift for `soft`, `hum`, and `humming`, the #29 one-versus-two threshold, and #49's any-occurrence policy warrant separate evaluation. No product change is authorised by this review.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/kriss-nyt-ai-write-like-that/2026-05-05-47e95385.md` | 2026-05-05 | `47e9538512a791b21285f00bf55e5514ca9fb770e2b839fa5a4d6fbabd27880e` |
| current | none found | `snapshots/kriss-nyt-ai-write-like-that.md` | 2026-07-16 | `41665c6c2456782c75e5bb4e89fa309950badcb67edaec789de44358670e68f4` |

The previous card and manifest recorded no digest. Before the snapshot was rewrapped, its on-disk SHA-256 was computed as `47e9538512a791b21285f00bf55e5514ca9fb770e2b839fa5a4d6fbabd27880e` and the bytes were confirmed identical to the committed Git object. The exact prior 30,231-byte file is archived at the path above. The current snapshot changes provenance framing and removes page chrome; the substantive article text, paragraph order, quoted examples, illustration references, and print note are unchanged.

## Decision history

- The 2026-05-05 card contained pattern mappings and open questions but no claim-keyed user decisions or implementation statuses. No product change was recorded as approved or implemented. This update replaces those untracked questions with C01-C22, all `pending` and `not started`; no prior decision is retired or carried forward as approved.
- C11 approved 2026-07-17: fix #26 double-counting and the #27 runtime/documentation divergence. Implemented in commits 13e235f (#26 token boundaries) and 7543052 (#27 token counting plus documented `hum`, `humming`, `soft`, and `settle` added).
- C07 and C17 closed 2026-07-18 via DR-123 with no product change: Elara/Kael remain source-specific corpus context rather than a name rule; the synesthesia examples and Woolf control remain covered by `forced_synesthesia` and `generic_metaphors`. Other rows remain pending.
- C15 approved 2026-07-18 via DR-124: the existing `formulaic_parallelism` agent judgement now explicitly reviews dismissive `an X with Y and Z` roast constructions when an appended attribute repeats X or does not make sense.
- C14 partial ruling 2026-07-19 via DR-19A: #25 now flags an adjacent pair of short fragments that share an opening word. The negative-modal/affirmative reversal and other sentence-level tricolon shapes remain pending.
- C14 closed 2026-07-25 via DR-19: no further product change. Each of the essay's three tricolons produces a finding (`No family. No calls. Just silence.` fails #25 and #9; `too young. Too single. Too inexperienced.` fails #25; `I may not have a husband. I may not have money. But I have love.` fails #9), and the Bing quotation's sentence-level repetition fails #51 `no-anaphora` on top of its #10 coordinated-list candidates. The source names no remaining uncovered shape.
- C14 partial ruling 2026-07-19 via DR-19B: #9 now flags two or more same-subject negative clauses followed by an explicit contrastive or emphatic affirmative turn as one candidate. Other sentence-level tricolon shapes remain pending.
- C13 approved 2026-07-20 via DR-21C: #29 now flags one complete one-to-four-word non-interrogative fragment immediately followed by an answer or evaluation of at most twelve words. The old broad ordinary-question matcher was replaced.

## Project coverage

This is the authoritative review table. Focused results below are surface-only deterministic coverage checks, not complete human-eyes Audits.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: AI-associated prose is a recognizable register made of stacked cues, but the essay's categorical moments are qualified by human history, genre, region, and social uptake. | Direct critical synthesis from selected examples; journalism, not a controlled comparison. The article supplies no accuracy or document threshold. | `overall-signal-stacking`, H3, H9, H12, and the process product boundary; **partly covered**. | The live product aggregates cues but does not establish the source's broad prevalence claim; any authorship reading would exceed both source and process. | Record the essay as field-guide and public-salience context only; require matched-register evidence before changing severity or thresholds. | pending | not started |
| C02: Kriss found 2019 GPT erratic and accidentally funny, while post-2022 assistant outputs became distinctive but boring; the earlier model could also break away from prompts. | Direct personal history and selected outputs; models, builds, settings, repetitions, and selection protocol are missing. | H25 and source metadata conventions; **partly covered** as hypotheses/documentation. | No live check represents model-era drift, playfulness, or prompt departure, and the examples cannot describe current models. | Preserve as version-drift context; take no product action. | pending | not started |
| C03: Integrated AI comments and email tools, reported author uptake, and published incidents make AI-mediated writing common enough to affect provenance review. | Mostly reported product and survey context: Society of Authors percentages and publication incidents are indirect; no underlying datasets are preserved here. | `genre_specific` journalism provenance watchlist and source-grounding guidance; **partly covered**. | The essay cannot establish current prevalence, the completeness of incident counts, or who authored any specific text. | Record as dated provenance context; require direct source records before using any numeric or incident claim. | pending | not started |
| C04: Em dashes and negative parallelism are publicly recognized cues, but Kriss says political and literary human examples do not prove AI use and notes long human histories. | Direct examples plus author commentary; political authorship is not verified and there is no measured AI-human rate. | Focused probes: `no-em-dashes` flags one U+2014; `no-negative-parallelisms` flags both `It's not a flood, it's a groundswell` and a deliberate human control. Exact candidate recognition is **fully covered**; interpretation is **challenged**. | #49 flags any em dash as a strong warning; #9 surfaces purposeful human matches. Neither runtime establishes provenance. | Keep both as candidate signals with explicit human controls; evaluate #49 any-occurrence handling and #9 context in matched genres before policy changes. | pending | not started |
| C05: Kriss proposes that em dashes may correlate with high-quality training text and that models overapply the correlation. | Author theory; no training corpus, ablation, model internals, causal test, or engineer confirmation. | No mechanism is needed for the live punctuation check; **not covered**, appropriately. | Calling the account “overfitting” does not establish this causal path, and the current source cannot support checker rationale. | Record as interpretation only; do not promote the mechanism without direct empirical evidence. | pending | not started |
| C06: An early ChatGPT converted a request for many jokes into repeated tickling, but Kriss explicitly says models no longer do this. | Direct selected anecdote and author interpretation; model/build and raw output are unavailable. The stated null is material. | H25 and `generic_metaphors` are adjacent only; **not covered** as an executable behaviour. | The example cannot support current-model behaviour or a general technical account of “overfitting.” | Preserve the retired-behaviour null and take no product action. | pending | not started |
| C07: Kriss observed recurring fiction names Elara Voss/Elena Voss and Kael and reported hundreds of post-2023 Amazon examples. | Direct observation plus an unreported Amazon search method; no denominator, genre control, date capture, or reproducible count. | `paech-antislop-sampler.md` separately reports corpus-level Elara/Kael concentration; no live name rule; **not covered**, appropriately. | A name blacklist would create severe false positives and the essay alone does not validate a rate. | Keep as source-specific fiction context; do not add a name rule. | approved | not applicable |
| C08: The essay reports post-ChatGPT PubMed increases for `delve`/`delves`, `underscore`, `highlight`, `showcase`, `intricate`, `tapestry`, `swift`, `meticulous`, and `adept`, including a 2,700% `delve` increase from 2022 to 2024. | Indirect corpus evidence; methods and exact cited work are not identified in the article text. The list mixes forms, corpora, and studies. | #7 and H24; `kobak-llm-excess-vocabulary.md`, `juzek-ward-delve.md`, and `geng-trotta-human-llm-coevolution.md` provide separately reviewed direct evidence. Focused `delves` alone passes #7 while a five-term cluster flags; **partly covered**. | A single word is below the runtime threshold; #7's generic list is not a source-specific PubMed trend and cannot reproduce the reported percentage. | Attribute quantitative claims to their direct cards, keep register/date boundaries, and do not use the essay to set #7 thresholds. | pending | not started |
| C09: `delve` is ordinary in Nigerian English, so a word that looks model-associated may be a regional human usage; the essay also relays a possible regional-training explanation. | Regional counterexample and causal interpretation reported without a direct corpus or training record. | H9, H24, and the no-authorship boundary; **partly covered**. `juzek-ward-delve.md` C06 separately reports an English-variety null that does not support the evaluator explanation. | The human look-alike is important, but this source cannot establish either a Nigerian-English concentration or a training mechanism. | Retain the false-positive caution; do not promote a demographic or causal rule, and cite the direct null when mechanism is discussed. | pending | not started |
| C10: British MPs reportedly increased `I rise to speak`, an American convention, including 26 uses on one June day; Kriss treats this as possible cultural transfer while allowing that some speakers simply copied peers. | Indirect transcript observation and interpretation; date, corpus, query, denominator, and causal identification are missing. | H24/H25 and source metadata conventions; **not covered** as a phrase or transfer analysis. | The example cannot distinguish direct AI use, AI-mediated diffusion, peer imitation, or ordinary change. | Record as an unresolved provenance/coevolution example; require direct transcript analysis before product use. | pending | not started |
| C11: In selected fiction outputs, spectral terms and quietness cluster, including seven named tokens in about 1,100 words, ten `quiet` uses in 759 words, and quiet language in a party scene. | Direct counts and short examples from an early ChatGPT-5 and Kriss's prompts; full outputs, build, settings, repetitions, and selection method are unavailable. | #26 and #27; focused ghost cluster flags #26. #27 is **partly covered** because code counts `quiet`/`settled` but omits documented `soft`, `hum`, and `humming`. | #26 double-counts substrings such as `shadow`/`shadows`; #27 documentation and runtime diverge. Neither threshold is validated by this selected sample. | Preserve as dated fiction evidence; evaluate the runtime/documentation drift and token counting with human genre controls before any fix. | approved | implemented |
| C12: AI fiction and marketing examples use tapestry/weaving, journey, threshold, temple, and `delve in` imagery as substitutes for complexity or quality. | Direct selected examples plus author interpretation; no frequency or human comparison. | #7 catches `tapestry` only in a cluster; `generic_metaphors` can assess ungrounded journey/portal imagery; **partly covered**. | `woven` and the source's explanation are not exact deterministic coverage; literal and deliberate metaphor controls matter. | Keep in #30's genre-aware review and #7 cluster context; do not add a standalone textile or journey blacklist. | pending | not started |
| C13: Chat responses can interrupt themselves with a short question-answer beat such as `And honestly? That's amazing.` | Direct example and author observation. | #29 now recognises a one-to-four-word non-interrogative fragment immediately followed by an answer or evaluation of at most twelve words, with one complete beat producing a finding. | No remaining executable gap for the approved structure. | Keep the approved fragment-question answer beat in programmatic #29. | approved | implemented |
| C14: Generated prose can overuse tricolons, including three in a little over 100 words and the literary variant `No X. No Y. Just Z.` | Direct count over a viral excerpt plus a quoted Bing example. | #25 flags adjacent short fragments sharing an opening word, including `Too young. Too single.` and `No family. No calls.` #9 flags `No X. No Y. Just Z.` and the repeated negative-to-affirmative reversal `I may not have X. I may not have Y. But I have Z.` The Bing quotation produces three #10 coordinated-list candidates. | None. Every tricolon the source supplies produces a finding; no further sentence-level shape is named. | Keep the approved #25 and #9 expansions, then address any remaining sentence-level tricolon shapes. | approved | implemented |
| C15: Lightly dismissive model prose repeatedly uses `an X with Y and Z`, with examples from ChatGPT, Grok, and Claude. | Three direct prompted examples across named products; builds, dates, settings, raw transcripts, and repetitions are absent. | The `formulaic_parallelism` agent judgement now explicitly asks for this syntactic family and flags it when an appended attribute repeats what X already implies or does not make sense. | The fixed shape is handled inside the existing formulaic-parallelism mechanism rather than as a disconnected judgement record. | Add the exact roast construction to `formulaic_parallelism`. | approved | implemented |
| C16: The `X with Y and Z` examples can be redundant or nonsensical, and selected model prose can be predictable and incoherent at once. | Direct critical reading; the broad claim and incapacity explanation are author interpretation, not a controlled result. | `semantic_redundancy`, `generic_metaphors`, `underspecified_language`, and `genre_specific` provide **partly covered** agent review. | The project does not assess logical fit of the exact roast formula, and the source cannot prove a universal model incapacity. | Use as a manual coherence prompt only; preserve the selected-example and mechanism limits. | pending | not started |
| C17: Selected outputs attach taste, colour, smell, or draping to days, grief, sorrow, emotions, dreams, and regret, while Woolf supplies a grounded human sensory comparison. | Direct selected outputs and literary human counterexample; no rate or model settings. | `forced_synesthesia` and `generic_metaphors`; **fully covered** as contextual agent-assessment questions, not deterministic findings. | The source does not validate severity or a universal human/AI distinction; genre and grounded mapping decide treatment. | Retain the examples and Woolf control in genre-aware evaluation; take no automatic rule action. | approved | not applicable |
| C18: Some model outputs gesture toward significance with mystical abstractions that do not resolve into a concrete meaning. | Direct quotation of a Reddit user's Ashal output, but post ID, model/build, prompt, and full conversation are absent; Kriss's meaning judgement is editorial. | #42, #1, #30, H27, and the existing performative-profundity opportunity; **partly covered**. | Phrase checks cannot establish whether a passage means nothing, and the source example's provenance is incomplete. | Keep H27 advisory, add the example only with provenance limits, and require matched human controls before promotion. | pending | not started |
| C19: The same Starbucks closure note appeared in five cities and stacked em dashes, weaving, rhythm, memories, and generic connection language, but Kriss's AI attribution is suspicion. | Directly quoted repeated notice plus reported local-news observation; no document provenance, generation record, or corporate confirmation. | #49, #7, #9, #30, and journalism provenance review; **partly covered** for surface features, not authorship. | Repetition across outlets may establish corporate reuse, not who drafted the note. | Use as a provenance-verification example and never as confirmed AI authorship. | pending | not started |
| C20: Kriss reports that people prefer AI-generated poetry to Shakespeare, Eliot, and Dickinson, associating preference with overt emotion and quiet/echo language. | Indirect study claim; title, sample, stimuli, procedure, effect sizes, and limitations are absent from the article text. | `walsh-ai-poetry.md` covers different corpus features, not preference; **not covered** by a directly reviewed preference source. | This article cannot support a user-preference claim or product optimisation target. | Ingest the exact study separately before any use; take no product action. | pending | not started |
| C21: A reported Max Planck study of more than 360,000 academic YouTube videos found increasing AI-associated vocabulary in human speech. | Indirect aggregate claim; the article omits paper identity, full corpus construction, words, effect sizes, controls, podcasts, and uncertainty. | H24 and H25 are **partly covered** as hypotheses; no direct source card for this spoken-language study. | Aggregate language change does not prove AI use in a speaker or document, and downstream reports expose differing 280,000/360,000 scope descriptions. | Ingest the exact reviewed revision before using the number or causal conclusion; preserve aggregate and provenance boundaries. | pending | not started |
| C22: Humans can adopt AI-associated language through exposure or peer imitation, so style cannot establish direct AI use. | Essay synthesis supported by reported coevolution work and the parliamentary counterexample; causal path remains partly indirect. | Process product boundary, H3, H9, H24, and H25; **fully covered** as a no-authorship principle, **partly covered** as empirical evidence. | The project should not collapse model influence, human imitation, editing assistance, and generation into one provenance verdict. | Add the coevolution distinction to the source-evidence map only after direct study ingestion; keep the current no-authorship boundary unchanged. | pending | not started |

## Recommendations

- C01: Record the essay as field-guide and public-salience context only; require matched-register evidence before changing severity or thresholds.
- C02: Preserve the model-era drift and take no product action.
- C03: Keep platform and prevalence claims as dated indirect provenance context until direct sources are reviewed.
- C04: Keep em dashes and negative parallelism as candidate signals with explicit human controls; evaluate #49 and #9 separately before policy changes.
- C05: Record the em-dash mechanism as interpretation only.
- C06: Preserve the stated retired-behaviour null and take no product action.
- C07: Keep Elara/Kael as source-specific fiction context and do not add a name rule.
- C08: Attribute quantitative vocabulary evidence to direct cards and keep register/date boundaries.
- C09: Retain the regional false-positive caution but do not promote a demographic or training-mechanism rule.
- C10: Keep `I rise to speak` as unresolved provenance/coevolution context until direct transcript analysis exists.
- C11: Evaluate #26/#27 token and documentation drift with human fiction controls before any product correction.
- C12: Keep textile and journey imagery in contextual #30/#7 review, not a standalone blacklist.
- C13: Keep the approved one-occurrence fragment-question answer beat in programmatic #29.
- C14: Keep the approved #25 repeated-fragment pair detector and #9 negative-to-affirmative reversal detector, then address any remaining sentence-level tricolon shapes.
- C15: Record `X with Y and Z` as a pending, matched genre-aware pattern opportunity; make no checker change.
- C16: Use redundancy and incoherence as manual coherence prompts with selected-example limits.
- C17: Retain the synesthesia examples and Woolf control in genre-aware evaluation; take no automatic rule action.
- C18: Keep performative profundity under H27 as advisory and provenance-limited.
- C19: Use the Starbucks notice only as a provenance-verification example, not confirmed AI authorship.
- C20: Ingest the exact poetry-preference study before use.
- C21: Ingest the exact Max Planck spoken-language revision before using its number or causal conclusion.
- C22: Preserve the no-authorship boundary and separate influence, imitation, assistance, and generation.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change requested.
- C02: not applicable - pending recommendation; no product change requested.
- C03: not applicable - pending recommendation; no product change requested.
- C04: not applicable - pending recommendation; no product change requested.
- C05: not applicable - pending recommendation; no product change requested.
- C06: not applicable - pending recommendation; no product change requested.
- C07: not applicable - closed 2026-07-18 via DR-123; no Elara/Kael name rule was added.
- C08: not applicable - pending recommendation; no product change requested.
- C09: not applicable - pending recommendation; no product change requested.
- C10: not applicable - pending recommendation; no product change requested.
- C11: passed - commit 13e235f corrected #26 token-boundary counting and commit 7543052 corrected #27 token counting and added the documented `hum`, `humming`, `soft`, and `settle` terms (`human-eyes/scripts/grade.py` plus regression tests in `dev/evals/tests/test_grade.py`); `python3 -m unittest dev.evals.tests.test_grade` passes on 2026-07-17.
- C12: not applicable - pending recommendation; no product change requested.
- C13: passed - DR-21C makes the source example and three structural variants fail #29 on one occurrence; ordinary and contracted interrogatives, a question-form Markdown heading, and literary dialogue pass; all 22 test files and regex robustness pass.
- C14: passed - DR-19A makes repeated short-fragment pairs fail #25; DR-19B makes the complete `I may not have X. I may not have Y. But I have Z.` frame and its approved contrastive and emphatic variants fail #9 as one candidate; incomplete frames pass. Verified 2026-07-25 that all three essay tricolons and the Bing quotation now produce findings across #25, #9, #51, and #10, closing the row.
- C15: passed - DR-124 extended `formulaic_parallelism` with the `an X with Y and Z` roast construction; `python3 dev/evals/tests/test_judgement_json.py` asserts the exact shape and the redundant-or-nonsensical appendage conditions on 2026-07-18.
- C16: not applicable - pending recommendation; no product change requested.
- C17: not applicable - closed 2026-07-18 via DR-123; existing `forced_synesthesia` and `generic_metaphors` coverage stands with the Woolf control retained.
- C18: not applicable - pending recommendation; no product change requested.
- C19: not applicable - pending recommendation; no product change requested.
- C20: not applicable - pending recommendation; no product change requested.
- C21: not applicable - pending recommendation; no product change requested.
- C22: not applicable - pending recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/kriss_nyt_reviewer_2 (fresh, read-only, source-dedicated); /root/kriss_nyt_reviewer was interrupted before reporting and did not supply a verdict
- **Findings resolved:** 2 material findings from /root/kriss_nyt_reviewer_2: C14 was corrected to distinguish the viral excerpt's zero #10 candidates from the separate Bing quotation's three coordinated-list candidates and to record both excerpts below the then-separate #10a density check (retired 2026-07-25 via DR-19G); the reviewer verified the exact drafted manifest replacement row for serial application. Focused recheck found 0 residual findings.
- **Unresolved findings:** none
