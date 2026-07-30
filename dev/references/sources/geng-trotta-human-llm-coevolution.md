# Geng and Trotta: Human-LLM Coevolution

## Metadata

- **URL:** https://aclanthology.org/2025.findings-acl.657/
- **Author / owner:** Mingmeng Geng and Roberto Trotta
- **Published:** July 2025; Findings of ACL conference dates 2025-07-27 to 2025-08-01
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed conference paper with academic empirical and exploratory analyses
- **Evidence tier:** peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.18653/v1/2025.findings-acl.657; ACL Anthology ID 2025.findings-acl.657
- **Version / revision:** final Findings of ACL 2025 proceedings PDF as retrieved 2026-07-15; prior record retrieved 2026-05-05 from the same ACL PDF URL without a recorded stable identifier or digest
- **Full-text status:** complete
- **Snapshot:** `snapshots/geng-trotta-human-llm-coevolution.md`
- **Extraction method:** official eight-page ACL Anthology PDF downloaded directly; embedded text checked with Poppler `pdftotext -layout`; structure inspected with `pdfinfo` and `pdfimages -list`; pages 1, 4, and 8 rendered with `pdftoppm` and visually compared; complete prior text body compared with the fresh extraction
- **Snapshot SHA-256:** `592b4e360ec6c97c5ac87d134f843bca2b5bcd1b0c361ba53322968e7bc0987f`
- **Model / corpus scope:** 1,294,653 arXiv abstracts submitted from January 2018 through December 2024, using Kaggle arXiv metadata version 214 and monthly frequencies normalised per 10,000 abstracts; a separate WithdrarXiv comparison of more than 14,000 withdrawn papers through September 2024; and the first 1,000 arXiv papers submitted in each year from 2018 through 2025, revised by GPT-4o-mini with temperature 1 and top-p 0.9 under two prompts and assessed with Binoculars. Computer-science and other arXiv categories are compared by assigning each paper to its first listed arXiv category, including for cross-listed papers. The paper reports no language filter; the analysed word examples and prompts are English.
- **Access limitations:** none for the paper. The PDF plots are raster images, so their curves are preserved in the authoritative PDF rather than reproduced as numeric series in the Markdown; all plot legends, axes, captions, and source-discussed trends were visually reviewed. The ACL page exposed no supplement or checklist.

## Summary

This eight-page Findings of ACL 2025 paper combines longitudinal word-frequency analysis with a small detector experiment. In 1,294,653 arXiv abstracts, the average frequencies of two Liang et al. word groups, covering ten list entries and nine distinct words, rose sharply and then declined after March or April 2024; several individual trajectories and the separately attributed `delve` trajectory also declined, while `versatile` continued upward. Several common or less-publicised words continued to rise, while `is` and `are` continued to fall. The authors interpret this as human selection and editing of LLM output, but explicitly acknowledge that the study is correlational and does not establish causality. In a separate GPT-4o-mini experiment, prompt-based avoidance reduced but did not eliminate selected words, and Binoculars scores did not significantly separate original abstracts from fully revised abstracts on average. For human-eyes, the paper supports dated, register-specific, aggregate vocabulary evidence and prompt-aware evaluation. It does not validate document-level authorship inference, a stable word blacklist, the current three-word paragraph threshold, or pattern B2's substitute-construction detector. The last point reverses the prior card's loose mapping: falling corpus frequency of `is` and `are` is not direct evidence that `serves as`, `stands as`, `features`, or the other live B2 constructions replace those copulas.

## Main insights

- The average frequencies of two Liang et al. groups, comprising ten entries but nine distinct words, rose sharply after ChatGPT and then declined after March or April 2024, when the authors say the prior studies drew attention to them: `realm`, `pivotal`, `intricate`, `showcasing`, `commendable`, `innovative`, `meticulous`, `notable`, and `versatile`. The individual trajectories are not uniform: several decline, but `versatile` continues upward in Figure 2b. The paper discusses `delve` as a separately reported decline from Leiter et al. and includes it in its own plots. The aggregate timing is direct; public exposure and its effect are not measured.
- Other words did not share that decline. `significant` and `additionally` kept rising, and the paper's prior eight-word group was `significant`, `crucial`, `effectively`, `additionally`, `comprehensive`, `enhance`, `capabilities`, and `valuable`.
- The authors' public-attention explanation is plausible timing-based interpretation, not causal proof. Their own Limitations section says the analysis identifies correlations and suggests questionnaires for causal study.
- Withdrawn-paper comparisons do not produce a strong counterfactual: `intricate` is higher in withdrawn abstracts, but the reported difference is not large, and the smaller withdrawn set is smoothed with a 12-month rolling average.
- `significant` and `additionally` rise in computer-science and non-computer-science abstracts and across the AI, computation-and-language, and computer-vision subcategories. The paper therefore treats the change as broader than one research topic, but does not rule out all discipline or publication-process confounds.
- GPT-4o-mini P1 revision increased certain displayed word frequencies, not every trajectory. Figure 5 shows later P1 `delve` below the original series. The authors state that P2 reduced targeted terms without eliminating them, but Figure 5 directly plots only `intricate` among P2's four prohibited words. The experiment therefore shows prompt-sensitive residue without establishing a uniform direction for every selected or prohibited word.
- Binoculars produced no average time trend on the original abstracts and no significant average score change between original and fully revised abstracts. Prompt choice also changed detector results.
- The falling frequency of `is` and `are` is an aggregate negative-frequency observation and an author-attributed example of subtle LLM influence. It is not a measured sentence-level substitution pathway and does not validate the current B2 regex family.
- The paper recommends common-word frequency for measuring change across very large publication corpora while saying that this approach is less suitable for precise detection of short texts.
- The study is narrow: one short paper, one detector, one generated-model condition, word-frequency features, arXiv abstracts, limited withdrawn-paper comparison, and observational correlations without causal identification.

## Evidence and claims to extract

- **Direct source reviewed:** final Findings of ACL 2025 proceedings paper, DOI 10.18653/v1/2025.findings-acl.657, all eight pages including Figures 1-8, Table 1, Limitations, references, and Appendix A. The authoritative PDF is preserved at `snapshots/attachments/geng-trotta-human-llm-coevolution-acl-2025.pdf`, SHA-256 `3050cd0278bcbde239bca780fad71db8afdcc4eac623d985d53889c24e4d4893`.
- **Method and sample:** Kaggle arXiv metadata version 214 supplies 1,294,653 abstracts from January 2018 to December 2024, analysed monthly and normalised per 10,000 abstracts. WithdrarXiv supplies more than 14,000 withdrawn papers through September 2024, plotted as 12-month rolling averages. The detector experiment uses the first 1,000 arXiv papers submitted in each year from 2018 through 2025, GPT-4o-mini at temperature 1 and top-p 0.9, prompt P1 (`Revise the following sentences`) and prompt P2 (the same instruction with four prohibited words), and Binoculars scores.
- **Direct versus cited evidence:** C01-C11, C13-C14, C18, and C20 are direct dataset descriptions, figures, experiments, source interpretations tied to direct results, or explicit limitations. C12 is an author interpretation from direct timing evidence. C15 is an author interpretation informed by the paper's direct detector result and cited mixed-text work. C19 is the authors' forecast and interpretation, partly supported by cited work but not an inherited empirical result. C16 and C17 are broader detector, Grammarly, and experienced-user claims inherited from cited studies; they are recorded as indirect and are not used as independent product evidence.
- **Important limits and counterexamples:** the paper reports correlations rather than causality; gives no confidence intervals, uncertainty bands, statistical model, or multiple-comparison procedure for the longitudinal vocabulary curves; compares only one detector and one model condition; smooths a much smaller withdrawn set; supplies no paper-level LLM-use labels or human baseline matched on topic and publication process; and says word-frequency analysis is unsuitable for precise short-text detection. Some highlighted words decline, others keep rising, avoidance prompts do not eliminate terms, withdrawn differences are small, detector score changes are not significant, and all causal or intentional-evasion explanations remain author interpretations.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering` in `human-eyes/scripts/grade.py`: direct token coverage for seven of the nine distinct Liang words in the local list, plus eight of nine in the Kobak style list; separately, `delve` appears in both lists; five of the paper's eight Geng-Trotta words are in the local list and all eight are in the Kobak style list; no temporal or register model
- `overall-signal-stacking` and `vocabulary_signal_stacking_profile` in `human-eyes/scripts/grade.py`: aggregate vocabulary points, but not longitudinal corpus evidence or the paper's methods
- B2 `no-copula-avoidance` in `human-eyes/scripts/grade.py`: catches `serves as`, `stands as`, `functions as`, `marks a`, `represents a`, `boasts`, and `features`; it does not measure a corpus-level fall in `is` or `are`
- H10 academic genre assessment in `human-eyes/scripts/judgement.json`: checks source support and evidence quality, not temporal word-frequency change
- H1 continuous calibrated register-distance score, H3 drop detection framing, H12 genre-aware threshold calibration, H24 register-specific vocabulary density, and H25 model-family versus generic-AI residue in `dev/hypotheses.md`
- complete-audit and cross-version requirements in `dev/TESTING.md`; non-authorship and source-preservation boundaries in `human-eyes/references/process.md`

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern
- H3 drop detection framing entirely
- H12 genre-aware threshold calibration
- H24 register-specific vocabulary density
- H25 model-family versus generic-AI residue
- Proposed H24 evaluation extension: treat public-tell date, corpus window, trend direction, category, model, and prompt as required strata before vocabulary evidence affects a user-facing finding
- Proposed detector-evaluation question: do source-bound full Audits remain useful on mixed or fully revised text when opaque detector scores do not separate the conditions?
