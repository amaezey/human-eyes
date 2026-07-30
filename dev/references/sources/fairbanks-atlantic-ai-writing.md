# Eve Fairbanks: The Biggest Tell That Something Was Written by AI

## Metadata

- **URL:** https://www.theatlantic.com/technology/2026/05/how-to-tell-ai-writing/687345/
- **Author / owner:** Eve Fairbanks / The Atlantic
- **Published:** 2026-05-29
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Journalism and editor essay with reported cases, personal writing-process anecdotes, one reproduced model interaction, and secondary reporting of two empirical studies
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** The Atlantic article 687345
- **Version / revision:** Current and previous reviews cover the published version modified 2026-05-29T17:08:00Z; current canonical and gift HTML were retrieved 2026-07-15
- **Full-text status:** complete
- **Snapshot:** `snapshots/fairbanks-atlantic-ai-writing.md`
- **Extraction method:** direct canonical and gift-link HTML fetched with `curl`; Python 3 and BeautifulSoup 4 used for DOM counts and text comparison; Markdown body retained from the prior verified extraction after the current rendered article matched it token for token
- **Snapshot SHA-256:** `e2fcd6ea012535eee831ba6f224590ff4ec534dec9123580bad3f6ee8f4a7db4`
- **Model / corpus scope:** The direct model example is labelled ChatGPT Pro, but the model name, version, interaction date, system prompt, complete conversation context, and sampling settings are not supplied. Broader direct observations concern unspecified AI-assisted English-language messages and submissions seen by one Johannesburg-based editor. The cited sycophancy study concerns advice and interpersonal-conflict tasks across 11 models, not finished-prose drafting. The cited vocabulary study concerns spoken English in YouTube academic talks and podcasts, not written prose.
- **Access limitations:** Both current Atlantic routes returned the complete server-rendered article. The snapshot omits page chrome, advertising, audio and sharing controls, author boilerplate, and a non-substantive lead illustration; its checked caption is recorded. No article-body text is omitted. The article's publisher policy supports only presumed human authorship, not independently verified provenance.

## Summary

Fairbanks argues that removable surface tics are less important than prose that has not undergone a writer's stopping, backtracking, premise-testing, and revision. The essay combines one editor's recent observations, personal anecdotes, links to reported cases, one reproduced ChatGPT Pro exchange, and secondary summaries of sycophancy and spoken-language-transfer studies. Its strongest contribution to human-eyes is a craft and evaluation frame for conceptual coherence and local repairability, plus a useful human-look-alike case against punctuation and rhetorical-form shortcuts. It supplies no verified submission corpus, prevalence estimate, authorship method, model metadata, controlled comparison, or threshold, so its broad claims remain journalism and interpretation rather than detector evidence.

## Main insights

- The source distinguishes removable public tells from distributed failures in premise, reasoning, facts, structure, diction, and tone.
- Mechanical cleanliness, even pacing, and a breezy-grandiose register are one editor's observations about submissions she inferred were substantially AI-assisted; the source supplies no counts, verification method, or comparison corpus.
- Writing friction can prompt a writer to revise a premise, abandon a draft, or withhold a message. The essay treats that process as part of thinking, not inefficiency to be cosmetically simulated.
- Fairbanks also says writing may become easy after the writer finds the right idea. Ease and fluency alone are therefore not adverse evidence; her distinction is between premature frictionlessness and ease after premise resolution.
- One ChatGPT Pro exchange shows a fluent metaphor being rationalised through successive prompts and then conceded when challenged. It is a qualitative example, not model-wide prevalence evidence.
- The article reports that sycophantic systems affirm users more than humans and that model-associated vocabulary may transfer into later spoken English. These are indirect claims whose direct papers have different task and register boundaries.
- The source itself contains 14 em dashes, two detected negative-parallelism candidates, three detected triads, 83 curly quotation marks, and ordinary uses of `renowned` and `crucial`. That makes it useful for contextual calibration, not verified authorship classification.
- The essay's claims that all substantially generated writing is incoherent, that AI cannot make human-like judgments, and that infiltration cannot be stopped are arguments or forecasts, not results established by its evidence.
- Valuing genuine confusion, doubt, and revision must not become guidance to invent errors, uncertainty, autobiography, or irregularity.

## Evidence and claims to extract

- **Direct source reviewed:** Current canonical and gift-link HTML for The Atlantic article 687345, published 2026-05-29 and still carrying publisher modification time `2026-05-29T17:08:00Z`; the complete body was compared with the preserved snapshot.
- **Method and sample:** Twenty-seven rendered paragraph elements including the deck, two editorial cross-links, and four poem-line elements; 10 body links; one block quote; one editor's submission observations; two AI-mediated message anecdotes; two autobiographical writing examples; one reproduced ChatGPT Pro exchange; and secondary reports of Cheng et al. and Yakura et al. No submission count, selection rule, verified provenance, model configuration, controlled comparison, uncertainty estimate, or direct written-language corpus is supplied.
- **Direct versus cited evidence:** C01-C13, C15-C16, and C18-C21 are Fairbanks's observations, examples, arguments, or forecasts. C14 reports Cheng et al., *Science* 391, eaec8352 (2026), DOI `10.1126/science.aec8352`; its structured abstract was checked for scope. The paper was ingested directly on 2026-07-26 as `cheng-social-sycophancy.md`, which supersedes this second-hand report. C17 reports Yakura et al., arXiv `2409.01754v3`; its abstract was checked for spoken-English scope. The paper was ingested directly on 2026-07-26 as `yakura-llm-influence-spoken-communication.md`, reviewed at v4, which supersedes the v3 figures quoted here. Linked journalism, the X post, surveys, tutorials, and submission provenance were not independently substantiated here.
- **Important limits and counterexamples:** The article generalises from anecdotes and editorial judgments; its public-tell list supplies no rates or thresholds; its own edited prose triggers the named surface checks; the ChatGPT exchange lacks model/version and full context; the sycophancy evidence is conversational and interpersonal; the vocabulary evidence is spoken English; no null result or systematic counterexample set is reported; and the publisher's disclosure policy is not independent authorship proof.

### Deterministic coverage check

The checked input is the snapshot content between `## Full text` and `## Extraction verification`, excluding the two editorial `Read:` lines, with Markdown links reduced to visible text, `<br>` markers removed, and block-quote markers removed while preserving paragraph and poem-line boundaries. The UTF-8 body at `tmp/fairbanks-atlantic-body-from-snapshot-2026-07-15.txt` has SHA-256 `c48d86595a35556c7368a23f477bf05084eed7bc170fbcbab2dcfb6933dd9c8f`, 1,775 whitespace-delimited words, and 52 lines. Running:

```bash
python3 human-eyes/scripts/grade.py audit tmp/fairbanks-atlantic-body-from-snapshot-2026-07-15.txt --surface-only --format json
```

returns `coverage_mode: surface_only`, `audit_status: incomplete`, and seven flagged programmatic checks: `no-em-dashes` with 14 candidates; `no-negative-parallelisms` with two candidates; `no-forced-triads` with three candidates; `no-curly-quotes` with 83 glyphs across 45 candidate sentences; `no-promotional-language` for `renowned`; `no-significance-inflation` for `crucial`; and `overall-signal-stacking` at 5/4 from four negative-parallelism points plus one vocabulary point. One em dash occurs in the poem and one in the quoted vocabulary-study language; the remaining 12 occur in Fairbanks's prose. One triad is inside the cited word list and one is in the poem. This is deterministic surface coverage only, not a complete Audit or an authorship result.

The quoted tutorial form `It’s not X; it’s Y` is intentionally masked as quoted material by the audit pipeline, so it is not one of the two document-level candidates. A focused direct call to `check_negative_parallelisms` on that exact curly-apostrophe semicolon construction returns `passed: false`, `candidate_count: 1`, and match `It’s not X; it’s`. The live rule therefore recognises the named form outside quotation; the two body-audit candidates are separate, unquoted human-look-alike constructions.

## Matched patterns / rules

- **B3 / `no-negative-parallelisms`:** Named as a public tell and challenged by two detected deliberate-use candidates in the article.
- **D3 / `no-collaborative-artifacts`:** Covers fixed praise and agreement residue, but not premise-level sycophancy or user self-correction.
- **G2 / `generic_metaphors` and `underspecified_language`:** Relevant to the raccoon exchange as a qualitative semantic case, not a prevalence finding.
- **H2, G9, `paragraph-length-uniformity`, and `sentence-length-variance`:** Related to the editor's cleanliness, uniformity, and pacing observation but do not verify provenance or reproduce her submission judgment.
- **H3 / `tonal_uniformity`:** Related to the reported breezy-grandiose consistency, although hybrid register and register lock are not identical.
- **H10 / `genre_specific`:** Journalism review covers sourcing and factual support, but not conceptual coherence or local repairability.
- **C7 / `no-em-dashes`:** Named as a public tell and challenged by 14 occurrences in the presumed-human edited article.
- **`overall-signal-stacking`:** Flags the article at 5/4, reinforcing that the output describes accumulated writing signals rather than authorship.

## Associated hypotheses

- **H3:** The essay supports dropping authorship-detection framing for these craft judgments.
- **H9 and H12:** The article is a journalism-register look-alike case for em-dash and negative-parallelism interpretation, not ground-truth classifier evidence.
- **H21:** Low information density and weak reasoning overlap with Fairbanks's distributed-failure argument but do not capture premise validity or repair cost.
- **H24 and H25:** The reported vocabulary transfer supports time-, register-, and model-aware treatment and cautions against static blacklists.
- **Proposed hypothesis:** Conceptual coherence across premise, evidence, reasoning, structure, diction, and facts, assessed as text quality without provenance inference.
- **Proposed hypothesis:** Local repairability, assessed separately from coherence: whether bounded edits can fix the draft or whether the argument needs reconstruction.
