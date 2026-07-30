# Juzek and Ward: Word Overuse and Alignment in Large Language Models

## Metadata

- **URL:** https://arxiv.org/abs/2508.01930
- **Author / owner:** Tom S. Juzek and Zina B. Ward
- **Published:** arXiv v1 submitted 2025-08-03; accepted for BIAS 2025 at ECML PKDD; Springer CCIS version of record published 2026, pages 243-259
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed conference chapter; open author manuscript, supplementary analysis, code, and data reviewed
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** arXiv:2508.01930v1; DOI 10.1007/978-3-032-19096-3_16; repository commit db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff
- **Version / revision:** complete open arXiv v1 and author/workshop manuscript v2.0.0; supporting repository commit db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff; replaces the 2026-05-05 abstract-page capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/juzek-ward-word-overuse-alignment.md`
- **Extraction method:** complete 16-page open author manuscript extracted with Poppler `pdftotext -layout`; pages 1, 8, and 16 rendered and checked; arXiv HTML structure compared; complete 63-file supporting repository preserved and inspected at pinned commit; direct OSF supplement preserved
- **Snapshot SHA-256:** `63318e86cdacd1333b61d855fc6dd1aeaf1721473cb26514fce3281613180f11`
- **Model / corpus scope:** English Scientific English and PubMed abstracts; 9,853 sampled 2020 abstracts continued by Llama 3.2-3B Base and Instruct; about 2.3m versus 2.2m continuation words; 25,000 Llama Instruct variants reduced to 8,710; 30 experimental pairs; 400 Global South Prolific participants; supporting instruction-tuning comparison uses 0.7m tokens against 337.6m PubMed tokens
- **Access limitations:** the Springer typeset version-of-record PDF was subscription-gated; the complete open author manuscript was available. The repository omits several full intermediate corpora and generated outputs, has no locked environment or publication-time commit, and does not preserve raw participant demographics. Plain-text PDF layout is best effort; authoritative PDFs and the complete available repository are attached.

## Summary

Juzek and Ward compare Llama 3.2-3B Base and Instruct continuations of 9,853 biomedical abstracts, derive part-of-speech-specific lexical differences, and run a forced-choice preference experiment on selected high- versus low-score Llama variants. Participants preferred the high-score variants 52.4% to 47.6%, a small aggregate difference consistent with the authors' LHF hypothesis. The result is not a clean LHF ablation, a word-level causal effect, or a document-level authorship test: Base and Instruct differ in more than preference optimization, the generated pairs may differ in syntax and content, one focal word (`nuanced`) reverses the aggregate direction, and the current code/data release has several paper-code discrepancies. For human-eyes, the source supports register-, model-, part-of-speech-, and aggregate-aware vocabulary evaluation while challenging flat word lists and mechanism claims.

## Main insights

- The Base-versus-Instruct procedure is a candidate-recognition method. It does not isolate LHF and does not define a safe document threshold.
- Table 1's largest increases include `nuanced_ADJ`, `nuance_VERB`, `firstly_ADV`, `reliance_NOUN`, `generalizability_NOUN`, and `underscore_VERB`; some high-ranked entries such as `radar_NOUN` are sampling artifacts.
- The main experiment reports a small preference for high LHF-Score variants, but it tests whole generated passages, not isolated word substitutions.
- `nuanced` is a direct counterexample to a categorical word rule: high-score variants containing it were preferred less often than their paired low-score variants.
- The direct instruction-tuning supplement is a mechanism null: only a minority of the tested overuse lemmata were significantly higher in three human-created instruction datasets, so the authors found no conclusive evidence that human-written instruction data originated the overuse.
- The current repository reproduces the main chi-square counts but exposes material documentation and implementation mismatches that prevent treating it as a full reproduction.
- The study's demographic and labour explanations are hypotheses and cited context; it does not compare evaluator populations or establish dialect, age, geography, or working conditions as mechanisms.
- The paper explicitly leaves the desirability of intervention open. Its workforce-diversity and dataset-balancing suggestions are policy options, not findings for human-eyes.

## Evidence and claims to extract

- **Direct source reviewed:** all 16 pages of the complete open author/workshop manuscript, arXiv v1, direct OSF supplementary instruction-tuning analysis and image, all 63 files in the supporting repository at commit `db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff`, and Springer version-of-record metadata. The open manuscript contains sections 1-6, Related Work, sections 3.1-3.3, one numbered data table plus one equation-layout HTML table, three substantive raster figures, 73 references, and Appendix A.
- **Method and sample:** 10,000 PubMed 2020 abstracts were sampled and 9,853 with at least 40 words retained. Llama 3.2-3B Base and Instruct continued the first half, yielding about 2.3m and 2.2m words. spaCy 3.8.3 with `en_core_web_sm` 3.8.0 produced lemma-POS counts. For the preference study, 50 abstracts supplied notes for 500 Llama variants each; length and a 21-form exclusion filter left 8,710 variants, from which 30 length-matched extreme-score pairs were chosen. Four hundred participants rated 20 critical pairs each plus five control or proficiency items; exclusions left 4,039 ratings.
- **Direct versus cited evidence:** C01-C16 and C19-C20 describe direct paper, supplement, code, or released-data evidence. C17 and C21 separate the authors' interpretations and cited demographic, labour, language-change, and detection context from measured outcomes. C18 preserves the authors' open normative question. The paper's broader claims about LHF labour, English varieties, age, public backlash, AI detectors, and other overuse studies remain indirect unless their upstream sources receive separate review.
- **Important limits and counterexamples:** one model family, one language, one scientific register, no clean LHF ablation, no correction for multiple lexical tests reported, generated-pair content and syntax not formally matched, a 46.8% participant exclusion rate (187 of 400), 4,039 of 8,000 possible critical ratings retained, no preregistration or IRB identifier reported in the reviewed materials, an exploratory `nuanced` reversal, corpus artifact `radar`, and a preliminary connection to human language. The current repository uses GPT-4o-mini where the paper says GPT-4o, encodes 1,480 positive significant weights where the paper says 814 candidate words, ships website constants inconsistent with the published 25-pair no-filler task, marks a user on the fourth too-fast item where the paper says exclusion followed five or more, and drops the first filtered rating through header inference in the mixed-model script.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: partial surface overlap only. Focused execution on 2026-07-15 passed a single `nuanced`; passed `nuance reliance generalizability`; failed the constructed `nuanced intricate underscore` cluster; and missed `firstly reliance generalizability radar staffing` as local B1 matches. The source does not validate B1's three-distinct-match paragraph threshold.
- `vocabulary_signal_stacking_profile`: partial aggregate overlap, but its local and Kobak lists, distinct-type thresholds, and structural combination do not implement the paper's lemma-POS LHF-Score or source comparison.
- H10 `genre_specific` academic branch and `human-eyes/references/process.md`: fully cover the need for genre-bound interpretation, source preservation, and no authorship claim; they do not add a lexical score.
- `human-eyes/scripts/judgement.json`: no direct lexical-preference assessment; its register and jargon-distribution prompts are broader qualitative controls.
- No complete human-eyes Audit was run. The deterministic calls above inspect surface coverage only, as required by `dev/TESTING.md`.

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern: supports continuous, source-calibrated lexical distance rather than a binary word verdict.
- H3 drop detection framing entirely: supports a non-authorship, revision-oriented interpretation.
- H12 genre-aware threshold calibration: strongly supports matched Scientific English and biomedical controls.
- H24 register-specific vocabulary density: directly supports model-, corpus-, POS-, and direction-specific density evaluation, with nulls and artifacts retained.
- H25 model-family versus generic-AI residue: directly supports model-pair/version provenance and warns against generic model attribution.
