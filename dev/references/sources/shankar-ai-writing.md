# Shreya Shankar: Writing in the Age of LLMs

## Metadata

- **URL:** https://www.sh-reya.com/blog/ai-writing/
- **Author / owner:** Shreya Shankar
- **Published:** 2025-06-16
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Practitioner craft essay
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** Canonical page with HTTP ETag `"32e39a37ce87f6c27fbac72f4c69b43c"` and Last-Modified `Thu, 02 Jul 2026 09:13:29 GMT`; previous snapshot retrieved 2026-05-05 had no recorded page revision identifier
- **Full-text status:** complete
- **Snapshot:** `snapshots/shankar-ai-writing.md`
- **Extraction method:** Direct canonical HTML verification with curl and Beautiful Soup 4.14.3; prior Markdown body retained after complete normalized-text and structure comparison
- **Snapshot SHA-256:** `7a03b57dd60c920e58e008b018889c2d28988645483cec5b0b028ed580129321`
- **Model / corpus scope:** Unquantified first-person observations from several technical papers and blog posts reviewed over the preceding couple of years; unspecified LLM tools and settings, one Gemini 2.5 Pro draft example, one unversioned GPT-4 hypothetical/example, English technical and blog prose, no measured corpus or human comparison
- **Access limitations:** None for the article body. The page supplies no study protocol, counts, prompt for most examples, model versions except Gemini 2.5 Pro, comparison corpus, links, citations, or stable first-party revision ID. Non-substantive page chrome and the duplicate table of contents were omitted.

## Summary

Shankar gives a first-person craft account of recurring problems she sees while writing and reviewing technical papers and blog posts, then supplies deliberate-use counterexamples and her own LLM-assisted writing loop. The complete static article contains 4 major sections, 17 subsections, 43 paragraphs, one block quotation, and one two-item list. It is strong practitioner evidence for editorial questions about substance, sentence subjects, reference clarity, rhythm, listification, audience knowledge, and scoped revision, but it is not a corpus study, model comparison, prevalence estimate, mechanism study, detector validation, or basis for document-level authorship inference.

## Main insights

- The direct negative craft observations are empty paragraph summaries, inappropriate listification, flat sentence rhythm, topic-misaligned grammatical subjects, low information density, vague claims and attributions, unclear demonstratives, unexplained fluency, and invented or dubious technical terminology.
- The article's central qualification is that a device associated with generated prose is not bad merely because models use it. Repetition, signposts, parallel structure, predictable headings, declarative openings, and em dashes can all help when they carry information or serve a deliberate rhetorical purpose.
- The source material complicates blanket rules: its flat-rhythm bad and good examples are both below the live sentence-variance check's eligibility boundary; the reviewer's isolated use of its two-item example list trips the list-ratio rule; one `This creates` example is recognized but below the deterministic demonstrative threshold; and the reviewer's content-bearing `In summary` control plus Shankar's intentional em dash are still failed by the live checks.
- Shankar's workflow keeps human judgment in the loop: outline the story, draft rough prose, delegate only the current bottleneck, ask for a scoped rhetorical transformation, select and edit completions, and retain responsibility for framing, depth, and contribution.
- No claim in the essay establishes frequency, causality, an RLHF mechanism, a severity level, a universal threshold, a model-family fingerprint, or authorship.

## Evidence and claims to extract

- **Direct source reviewed:** Complete canonical article HTML served 2026-07-17 with ETag `"32e39a37ce87f6c27fbac72f4c69b43c"` and Last-Modified `Thu, 02 Jul 2026 09:13:29 GMT`; preserved as `snapshots/shankar-ai-writing.md`.
- **Method and sample:** Practitioner reflection based on several unspecified technical papers and blog posts written or reviewed over roughly the prior two years. The article provides selected examples and one self-reported workflow, not a defined sample, comparison group, annotation procedure, frequency table, or outcome evaluation. Models and prompts are mostly unspecified; the low-density introduction names Gemini 2.5 Pro, and an illustrative technical passage names GPT-4 without a version.
- **Direct versus cited evidence:** C01-C23 distinguish direct author observations, examples, qualifications, interpretations, and self-reported process from reviewer analysis in the coverage columns. The page cites no external works. C10's statement that a sample term is not one Shankar has heard, C22's characterization of SWBST as often taught in early education, and C23's capability judgments remain author interpretation rather than independently verified findings. The isolated-list and content-bearing-summary controls in C03 and C13 are reviewer applications of the source's criteria, not author-labelled controls.
- **Important limits and counterexamples:** Human writers can produce the named problems, Shankar says she makes the demonstrative mistake herself, and she directly defends six often-flagged devices. There are no rates, model controls, prompt controls, longitudinal measurements, non-English evidence, genre transfer tests, reader outcomes, null tests, or authorship labels.

## Matched patterns / rules

- A5 `no-vague-attributions`
- G3 `no-excessive-lists`
- H2 `no-tidy-paragraph-endings` plus agent assessment `semantic_redundancy`
- H4 `no-orphaned-demonstratives`, H5 `no-this-chains`, and agent assessment `referential_clarity`
- G6 `no-section-scaffolding`
- H10 agent assessment `genre_specific`
- G8 `no-signposted-conclusions`
- C7 `no-em-dashes`
- H14 `no-anaphora`
- G9 `sentence-length-variance`
- Agent assessments `underspecified_language`, `formulaic_parallelism`, and `semantic_redundancy`
- `human-eyes/references/process.md` meaning preservation, structural repair, and product boundary

## Associated hypotheses

- H8 audience-aware voice via invocation surface
- H9 field-guide voice with similar-species disambiguation
- H12 genre-aware threshold calibration
- H21 low information density and wrong sentence subject
- H22 long-tail compression and grammatical standardisation
- H27 performative profundity and aphoristic closure, as adjacent ending research only
