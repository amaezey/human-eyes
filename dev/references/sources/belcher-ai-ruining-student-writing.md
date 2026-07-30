# Wendy Laura Belcher: 10 Ways AI Is Ruining Your Students' Writing

## Metadata

- **URL:** https://www.chronicle.com/article/10-ways-ai-is-ruining-your-students-writing
- **Author / owner:** Wendy Laura Belcher
- **Published:** 2025-09-16
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Contract updated:** 2026-07-15; the preserved extraction was brought into the source-ingest contract without a fresh article scrape
- **Source type:** higher-education journalism / first-person pedagogy and practitioner observation
- **Evidence tier:** Practitioner / teacher / editor essays (reported via higher-education journalism)
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** Chronicle Advice article published 2025-09-16, preserved in the 2026-05-05 Jina Reader capture; previous record was the same article body embedded in an unnormalized page capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/belcher-ai-ruining-student-writing.md`
- **Extraction method:** preserved Jina Reader URL-to-Markdown capture; no fresh scrape; page chrome removed and complete accessible article body normalized into the snapshot template
- **Snapshot SHA-256:** `30f7de0bf57b7fbe96e11d27e772614451d01aae7e96c57b9c84ac020f8e90f4`
- **Model / corpus scope:** Belcher's first-person observations from literature teaching and repeated interactions with unspecified ChatGPT versions, Google Gemini, Google Chrome AI Overview, and Stanford University's Storm app. Examples include AI-assisted student literary-analysis papers, author-generated model outputs, and one reported search overview. No model versions, prompts except one Gemini prompt, dates for most examples, course or paper counts, comparison sample, student demographics, language scope beyond English prose, annotation protocol, or measured frequencies are supplied.
- **Access limitations:** none for the preserved article body. Decorative and repeated page elements were omitted from the normalized snapshot but remain in the archived prior capture. The article does not provide the underlying student papers, model transcripts, prompt history, the cited composition research, Belcher's 2007 *LIT Magazine* article, detector results, or empirical validation of prevalence, mechanisms, causality, or authorship accuracy.

## Summary

Belcher's Chronicle pedagogy essay gives a literature professor's ten-part account of recurring weaknesses in AI-assisted student papers: banal argument, fluent emptiness, referent cycling, abstraction chains, broken causal relations, erased interpretive agency, adjective inflation, moralizing and racist defaults, derivative argument, and factual error. It adds concrete literary-analysis examples, a directly checkable `not ... but` construction, and an important classroom response: identify the writing failures and require revision without claiming certainty about authorship. It is strong practitioner evidence for student-literary-analysis review prompts and weak evidence for general prevalence, model mechanisms, thresholds, or an authorship verdict because it supplies no documented sample or controlled comparison.

## Main insights

- The article's strongest project contribution is a genre-specific quality taxonomy for student literary analysis, not a general AI detector.
- Several observations are already represented in H10's student-essay guidance, B3 negative parallelism, H21 low information density/wrong subject, and the product's non-authorship boundary. The referent-cycling observation matched former #11, removed 2026-07-25 through DR-156.
- The live deterministic checker catches the exact trailing `symbolizing ...` clause under A3 and the exact `not as ... but as ...` example under B3, but it does not catch the exact examples for banality, fluent emptiness, referent cycling, causal inversion, erased interpreter agency, adjective inflation, or moralizing.
- The source's causal explanations about next-word prediction, repetition penalties, and resistance to correction are author interpretations without model/version or experimental evidence.
- The moralizing, racism, plagiarism, and factual-error examples are important review prompts but remain anecdotal, source- and course-bound accounts whose underlying documents or upstream evidence are not preserved here.
- Belcher explicitly advises teachers not to treat the observed flaws as proof of AI use. That framing aligns with human-eyes' existing product boundary and should govern any use of the source.

## Evidence and claims to extract

- **Direct source reviewed:** Complete Chronicle Advice article published 2025-09-16, preserved in the 2026-05-05 Jina Reader capture and normalized without a fresh scrape on 2026-07-15. The review includes the opening, all ten numbered problems and examples, the additional scientific-term and `not ... but` notes, closing remediation, inline Guardian link, and author biography.
- **Method and sample:** First-person practitioner essay based on Belcher's literature teaching, AI-assisted student papers she reports reading, and her interactions with ChatGPT, Gemini, Storm, and Chrome AI Overview. It gives several short examples but no sample size, denominators, prompt log beyond one Gemini prompt, model versions, dates for most outputs, comparison corpus, coding method, or outcome evaluation.
- **Direct versus cited evidence:** C01-C09 and C11-C16 are direct author observations, interpretations, reported classroom examples, or model-output examples. C10 partly relies on the Guardian-linked account of Ngugi wa Thiong'o's language position; that upstream source was not separately reviewed in this ingest. C11 refers to Belcher's own 2007 *LIT Magazine* argument, which is not linked or preserved. C15 invokes unspecified research and technical mechanisms without citations. These inherited or mechanistic claims remain indirect or unresolved for project decisions.
- **Important limits and counterexamples:** The article concerns English-language literature papers, not business prose, fiction, journalism, or all student genres. Belcher acknowledges that composition classes also teach variation, that varying verbs and modifiers can be useful, that her lecture does not prevent bad AI-assisted papers, and that she cannot know authorship from these flaws. Individual examples do not establish prevalence, a frequency threshold, a causal mechanism, or a document-level verdict.

## Matched patterns / rules

- A3 `no-superficial-ing` for the exact trailing `symbolizing ...` clause in C06
- B3 `no-negative-parallelisms` for the exact `not as ... but as ...` example in C14
- C05 has no live pattern: former #11 synonym cycling was removed 2026-07-25 through DR-156
- H10 `genre_specific` student-essay description and watchlist for C02, C03, C08, C11, and adjacent parts of C04 and C12
- H21 low information density and wrong sentence subject for C04, C07, and C08
- `human-eyes/references/process.md` source preservation, closed-record, and product-boundary guidance for C03, C12, and C16

## Associated hypotheses

- H3: Drop detection framing entirely
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H21: Low information density and wrong sentence subject
