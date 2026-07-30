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

## Matched patterns / rules

- `no-ai-vocabulary-clustering` (B1); partial coverage, with a three-item paragraph threshold and no register-specific source profile.
- `no-negative-parallelisms` (B3), `no-countdown-negation` (H1), and `no-staccato-sequences` (E5); direct structural overlap, including `No X. No Y. Just Z.`, but no automatic distinction between AI-associated and deliberate human uses.
- `no-forced-triads` (B4); partial and challenged coverage. The exact viral excerpt's three sentence-level tricolons produce zero B4 candidates, while the separate Bing quotation produces three coordinated-list candidates; neither short excerpt reaches B4's density threshold.
- `no-ghost-spectral-density` (F1) and `no-quietness-obsession` (F2); partial direct overlap. The quietness catalogue names `hum`, `humming`, and `soft`, but the executable check does not.
- `forced_synesthesia` (F3), `generic_metaphors` (G2), `semantic_redundancy` (H2), and `genre_specific` (H10); agent-assessed contextual overlap.
- `no-rhetorical-questions` (G1); full coverage for the approved fragment-question answer beat, with one complete occurrence producing a finding.
- `no-manufactured-insight` (G7) and `no-significance-inflation` (A1); partial overlap with empty profundity, not an exact meaning or coherence assessment.
- `no-em-dashes` (C7); exact glyph recognition, but the source's human controls and no-proof statement challenge fail-on-any generic interpretation.
- Product boundary in `human-eyes/references/process.md`; fully covers the rule that reports must not infer authorship.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H9: Field-guide voice with similar-species disambiguation per pattern.
- H12: Genre-aware threshold calibration.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
- H27: Performative profundity and aphoristic closure.
