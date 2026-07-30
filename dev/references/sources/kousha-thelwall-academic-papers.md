# Kousha and Thelwall: How much are LLMs changing academic papers after ChatGPT?

## Metadata

- **URL:** https://doi.org/10.1007/s11192-026-05601-5
- **Author / owner:** Kayvan Kousha and Mike Thelwall
- **Published:** 2026-04-03 online; received 2025-09-11; accepted 2026-03-11
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** Peer-reviewed empirical study in Scientometrics; version of record
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1007/s11192-026-05601-5
- **Version / revision:** version of record published 2026-04-03; previous library capture was an arXiv:2509.09596v2 abstract page retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/kousha-thelwall-academic-papers.md`
- **Extraction method:** first-party Springer version-of-record PDF downloaded over HTTPS; all 21 pages extracted with Poppler `pdftotext -layout`; `pdfinfo`, `pdfimages -list`, and rendered pages 1, 11, and 21 checked; two Figshare v1 summary workbooks inspected with `openpyxl`
- **Snapshot SHA-256:** `39fdec1a537efea6b36428321fb05e6ba54663ebdccb2fa3feb0f81253b7db9a`
- **Model / corpus scope:** Language change associated with the post-November-2022 release of ChatGPT 3.5, not a generated-output experiment. Twelve English term families were searched in articles, reviews, and proceedings from six scholarly databases for 2015-2024. Full-text repetition, co-occurrence, and correlation analyses used more than 2.4 million open-access PMC papers from 2021 through 23 July 2025, excluding titles, abstracts, references, and supplements from the main-body counts.
- **Funding / competing interests:** No funding was provided. Both authors declared that they are members of the Distinguished Reviewers Board of Scientometrics.
- **Access limitations:** No substantive article text is inaccessible. The preserved PDF contains all 21 pages, 14 figures, two tables, Appendix A, declarations, references, and affiliations. The two compact source-data workbooks for RQ1 and RQ2-RQ4 are preserved. Five linked row-level PMC workbooks, about 529 MB combined, were not duplicated; their first-party file records and MD5 values are preserved in the Figshare metadata attachment.

## Summary

Kousha and Thelwall measure changes in 12 selected English term families across six scholarly databases, then use more than 2.4 million PMC open-access full texts to examine within-paper frequency, co-occurrence, and correlation before and after ChatGPT's public release. The paper directly supports time-sensitive, academic-register vocabulary and clustering evidence, with strong controls on provenance claims: it does not identify who used an LLM, distinguish generated from edited text, validate a document-level authorship rule, or establish human-eyes' current three-matcher-entry-per-paragraph threshold. Its largest project contribution is the full-text evidence for repeated and co-occurring term use, plus the finding that document type, length, field, section, language, platform, low starting rates, selection conditions, and 2025 reversals materially affect interpretation.

## Main insights

- The study's 12 families are `underscore`, `delve`, `showcase`, `unveil`, `intricate`, `meticulous`, `pivotal`, `heighten`, `nuance`, `bolster`, `foster`, and `interplay`, with inflected variants. Seven came from earlier literature; five came from an exploratory Environmental Science candidate screen. Results for the five added families on that selection surface are selection-conditioned, not independent confirmation.
- The article and workbooks use inconsistent shorthand for the `intricate` family: Table 1 and several sheets say `intricate[s/d/ing]`, while the correlation and co-occurrence materials say `intricat[e/ies/ely]`. The intended exact variant set is therefore not fully recoverable from the labels alone.
- Across the six databases, `delve`, `underscore`, and `intricate` had the largest 2022-2024 relative increases. `interplay` and `foster` grew much less, which argues against flattening all listed terms into one severity or rate.
- Absolute use and relative growth differ. Some STEM fields had very large percentage increases from low baselines, while some social-science and humanities fields still had higher absolute use of `delve` or `underscore`.
- PMC main-body evidence shows both more papers using the terms and more repeated use within papers. The six-or-more-use increase exceeded 10,000% for `underscore`, 5,400% for `intricate`, and 2,800% for `meticulous` from 2022 to 2025, while `delve` was less often repeated six or more times.
- The longer post-release direction is not monotonic. From 2024 to 2025, full-text prevalence fell for `delve` (5.21% to 3.72%), `showcase` (5.00% to 4.58%), `unveil` (4.05% to 2.84%), `intricate` (10.03% to 9.73%), `meticulous` (5.03% to 4.73%), and `bolster` (2.54% to 2.28%). Conditional geometric means fell for 10 of 12 families; only `underscore` and `foster` rose.
- Conditional co-occurrence is asymmetric. In 2024, 59.3% of PMC papers with `delve` also had `underscore`, but only 16.1% of papers with `underscore` also had `delve`, because `underscore` was much more common.
- Pairwise term-frequency correlations rose sharply in 2024. This is aggregate evidence of clustered language change, not proof about any individual paper's production history.
- Review articles were longer and showed more `underscore` use than research articles or case reports; the authors explicitly identify document length as a partial explanation.
- The retraction association is labelled hypothesis-generating, with many uncontrolled causes, and the paper treats translation, proofreading, and language-barrier reduction as legitimate uses.
- The authors state that their before/after design is non-causal and cannot distinguish LLM generation, LLM editing, or broader editorial and publishing-style change.

## Evidence and claims to extract

- **Direct source reviewed:** Complete Springer Nature / Scientometrics version of record, DOI 10.1007/s11192-026-05601-5, published online 2026-04-03; complete 21-page PDF; related Figshare dataset version 1 metadata and both compact aggregate workbooks; compared with arXiv:2509.09596v2 and the archived prior abstract-page snapshot.
- **Method and sample:** The authors searched inflected variants of 12 selected terms in Scopus, Web of Science, and PubMed titles/abstracts/keywords and in broader OpenAlex, Dimensions, and PMC searches. Searches were limited to articles, reviews, and proceedings from 2015-2024 and normalised by each database's annual publication count; searches ran 20 December 2024, with a Scopus control-term follow-up on 28 January 2025. The full-text follow-up downloaded more than 2.4 million PMC open-access XML publications from 2021 to 23 July 2025 and used Webometric Analyst to count main-body occurrences, excluding titles, abstracts, references, and supplements. The study reports proportions, 95% confidence intervals, geometric means, repeated-use bands, asymmetric conditional co-occurrence, and Pearson correlations.
- **Direct versus cited evidence:** C01-C21 and C23 are direct study methods, results, author interpretations, limitations, provenance facts, or project comparisons grounded in the preserved article and aggregate workbooks. C22 groups the introduction's survey, detector, readability, and prior-vocabulary claims as cited evidence only; those findings are not treated as direct results here.
- **Important limits and counterexamples:** The design is observational and before/after, with no direct causal attribution. The term set is selective and English-only; five terms were selected through an exploratory environment-specific screen, so their results on that surface are selection-conditioned; the source uses inconsistent `intricate`-variant labels; six families' full-text prevalence and 10 families' conditional geometric means fell from 2024 to 2025; fields and natural domain uses differ; OpenAlex dating behaves differently; most cross-database searches are metadata-based; PMC covers only open-access biomedical and life-science material; longer papers have more opportunity to contain terms; traditional comparison terms were pragmatically chosen and not exhaustive; no sentence-structure analysis was performed; model and language changes can make the vocabulary drift; translated abstracts and non-native-English editing can raise counts without direct generation; and the retraction result is not causal.

## Matched patterns / rules

- Pattern B1, AI vocabulary words; registry check `no-ai-vocabulary-clustering`; implementation `human-eyes/scripts/grade.py:AI_VOCABULARY`, `_find_ai_words`, and `check_ai_vocabulary`.
- Aggregate meta-check `overall-signal-stacking`; implementation `vocabulary_signal_stacking_profile`, `kobak_excess_profile`, and `check_overall_signal_stacking` in `human-eyes/scripts/grade.py`.
- Pattern H4 `no-orphaned-demonstratives` and pattern A1 `no-significance-inflation` overlap literal `underscore` constructions but test sentence function, not corpus vocabulary drift.
- `human-eyes/references/patterns.md` source-strength, cluster, and non-authorship guidance; `human-eyes/references/process.md` product boundary.
- No agent-assessment record in `human-eyes/scripts/judgement.json` evaluates term repetition or register-specific vocabulary density.

## Associated hypotheses

- H1: Calibrated register-distance score.
- H3: Reframe as a register explainer, not an AI detector.
- H12: Genre-conditional check profiles.
- H24: Register-specific vocabulary density.
