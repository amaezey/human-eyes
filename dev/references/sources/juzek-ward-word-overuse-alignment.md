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

## Skill-use audit

- **Good use:** support H24's register-specific vocabulary-density work; require lemma-POS, model/version, corpus, date, direction, and aggregation metadata; use the preference result as bounded mechanism evidence; preserve the instruction-tuning null and `nuanced` counterexample.
- **Misuse / overclaim:** do not cite the study as proof that any word or paragraph is AI-written, that LHF alone caused the lexical profile, that evaluators prefer every high-score word, or that the current #7 threshold is validated.
- **Unsupported use:** generic prose outside English biomedical abstracts; other model families or current Llama versions; demographic or dialect tells; per-document sensitivity, specificity, calibration, or authorship; causal estimates for individual words; policy conclusions about LHF workforces.
- **Underused evidence:** the project does not retain source-specific lemma-POS weights, negative or null mechanism evidence, item-level counterexamples, or a distinction between candidate recognition and a document threshold.
- **Patterns left on the table:** model-pair lexical profiles, artifact review, evaluator-task emulation, word-by-context interaction, pair-equivalence auditing, and current-model replication remain evaluation material rather than product checks.

## Matched patterns / rules

- #7 `no-ai-vocabulary-clustering`: partial surface overlap only. Focused execution on 2026-07-15 passed a single `nuanced`; passed `nuance reliance generalizability`; failed the constructed `nuanced intricate underscore` cluster; and missed `firstly reliance generalizability radar staffing` as local #7 matches. The source does not validate #7's three-distinct-match paragraph threshold.
- `vocabulary_signal_stacking_profile`: partial aggregate overlap, but its local and Kobak lists, distinct-type thresholds, and structural combination do not implement the paper's lemma-POS LHF-Score or source comparison.
- #41 `genre_specific` academic branch and `human-eyes/references/process.md`: fully cover the need for genre-bound interpretation, source preservation, and no authorship claim; they do not add a lexical score.
- `human-eyes/scripts/judgement.json`: no direct lexical-preference assessment; its register and jargon-distribution prompts are broader qualitative controls.
- No complete human-eyes Audit was run. The deterministic calls above inspect surface coverage only, as required by `dev/TESTING.md`.

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern: supports continuous, source-calibrated lexical distance rather than a binary word verdict.
- H3 drop detection framing entirely: supports a non-authorship, revision-oriented interpretation.
- H12 genre-aware threshold calibration: strongly supports matched Scientific English and biomedical controls.
- H24 register-specific vocabulary density: directly supports model-, corpus-, POS-, and direction-specific density evaluation, with nulls and artifacts retained.
- H25 model-family versus generic-AI residue: directly supports model-pair/version provenance and warns against generic model attribution.

## Questions / follow-up

- Which publication-time repository commit and dependency environment produced the paper's results, and why does the current released focal-weight list contain 1,480 entries while the paper reports 814?
- Is the released website a later example configuration, or can the authors provide the exact 25-item, no-filler experiment build and database schema?
- Can a matched biomedical evaluation replicate the aggregate result with current models, semantically equivalent pairs, multiplicity control, and word-level interaction estimates?
- Should future H24 work treat the LHF-Score only as a candidate-ranking instrument rather than import its uncorrected weights into product behavior?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | arXiv:2508.01930v1 abstract-page capture; no digest was recorded in the prior card or manifest | `snapshots/archive/juzek-ward-word-overuse-alignment/2026-05-05-arxiv-2508.01930v1-426c3903.md` | 2026-05-05 | `426c3903bac81579aacda04806d4d60deb1a9b56d9f91712dbbbe1ddd5d49609` |
| current | arXiv:2508.01930v1; DOI 10.1007/978-3-032-19096-3_16; repository commit db52b0ee3eba6c09a4ec17d7f9e45d7d0c1db8ff | `snapshots/juzek-ward-word-overuse-alignment.md` | 2026-07-15 | `63318e86cdacd1333b61d855fc6dd1aeaf1721473cb26514fce3281613180f11` |

The previous record did not contain a SHA-256 to verify against. Before replacement, its exact on-disk bytes were hashed as `426c3903bac81579aacda04806d4d60deb1a9b56d9f91712dbbbe1ddd5d49609`, copied byte-for-byte to the archive path above, and re-hashed there to the same value. The refresh replaces an abstract-page capture with the complete open paper, direct supplement, repository evidence, and claim-keyed project comparison.

## Decision history

- The prior card had no stable claim IDs, user decisions, or implementation statuses. Its broad #7, H1, and H12 notes were analysis only, not approval. This update replaces them with C01-C21 and leaves every recommendation `pending` and `not started`; no product change is represented as authorized.
- The old claim that the abstract described participants as preferring variants containing certain words is narrowed: the direct experiment compares whole high- versus low-score generated variants, and `nuanced` supplies a contrary item-class result.

- C01 approved 2026-07-18 via DR-125: #7 now recognises `nuance`, `nuances`, `nuancing`, `firstly`, `reliance`, and `generalizability`; existing `nuanced` coverage and the paragraph threshold are unchanged.

## Project coverage

This is the authoritative review table. Every recommendation remains a pending decision for Mae.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Llama 3.2-3B Instruct differs from Base in lemma-POS frequency, with the largest reported increases headed by `nuanced_ADJ` +8342.8%, `nuance_VERB` +6301.7%, `firstly_ADV` +4794%, `reliance_NOUN` +3193.6%, and `generalizability_NOUN` +3124%. | Direct Base-versus-Instruct comparison of about 2.3m and 2.2m continuation words from 9,853 PubMed prompts; one model pair, one register, and uncorrected chi-square screening. | #7 now recognises `nuanced`, `nuance`, `nuances`, `nuancing`, `firstly`, `reliance`, and `generalizability`. | The runtime does not retain lemma-POS labels or source effect sizes in its evidence output. | Add the missing exact forms to #7 under its existing paragraph threshold. | approved | implemented |
| C02: 813 of the paper's 814 significantly higher Instruct-versus-Base items were also significantly higher than held-out human PubMed halves. | Direct second comparison in the paper, but the full human-comparison table and multiplicity treatment are not released. The current code's positive significant table and hard-coded score each contain 1,480 entries, creating an unresolved count mismatch. | partly covered by H24's human-baseline requirement and the project's non-authorship framing. | The 814 versus 1,480 discrepancy and absent full human comparison prevent importing the list or treating the overlap as independently reproduced. | Preserve the reported overlap and discrepancy; request clarification or recompute from complete corpora before any adoption. | pending | not started |
| C03: The Base-versus-Instruct contrast identifies candidates potentially associated with LHF, not a clean LHF causal effect. | Direct method and qualification. The models also differ in instruction tuning, tool optimization, and safety mitigation; DPO is only one distinction. | fully covered in process framing and H25, which separate measured behavior from model-family and mechanism claims. | The source's stronger discussion language about a primary source is not causally identified. | Keep LHF as a mechanism hypothesis and label the comparison by exact model pair; no product change. | pending | not started |
| C04: `radar_NOUN` rose 2590.6% because several sampled abstracts discussed radar and Instruct reused it while Base did not. | Direct author inspection and limitation; a concrete corpus-sampling artifact. | partly covered by H24's register and corpus controls; no active generic artifact review exists. | A ranked frequency list can elevate topic artifacts when sample size is limited. | Require source/context inspection and negative controls for high-change candidates before evaluation use. | pending | not started |
| C05: The experiment generated 25,000 variants from notes for 50 abstracts, kept 8,710 after length and 21-form filters, and selected 30 length-matched high/low LHF-Score pairs. | Direct experimental construction. Selection deliberately maximizes score deltas and does not sample ordinary model output. | partly covered by `dev/TESTING.md` provenance and matched-input requirements. | The project has no pair-equivalence audit or selection-bias record for lexical experiments. | Treat the items as enriched experimental stimuli, not prevalence examples; require semantic-equivalence review in any reuse. | pending | not started |
| C06: The LHF-Score sums occurrences weighted by positive percentage change from Base to Instruct, scaled by 1,000. | Direct equation and released implementation. The current code uses 1,480 hard-coded positive significant weights, including many domain terms and function words. | not covered: #7 and `vocabulary_signal_stacking_profile` use distinct local and Kobak lists with different thresholds and no source weights. | A raw percent-change score inflates rare baselines and does not itself provide document calibration or false-positive rates. | Do not adopt the score as a live detector; evaluate a recomputed, regularized version only within matched biomedical controls. | pending | not started |
| C07: The 30 selected high-score variants averaged 7.2 over 105 words and low-score variants 1.7 over 104 words. | Direct descriptive result after extreme-pair selection; no distribution or uncertainty for those means is reported. | not covered by a source-specific project metric. | Length matching does not guarantee content, factual, syntactic, or stylistic equivalence. | Record as stimulus construction only and pair with C16's confound boundary. | pending | not started |
| C08: Four hundred Global South Prolific participants rated 20 critical pairs plus five calibration, attention, or proficiency items; exclusions left 4,039 of 8,000 possible critical ratings. | Direct method. Sample was 231 women and 169 men, mean age 30.1, 90% Africa and 10% Southeast Asia, compensated about $15 per hour; the participant exclusion rate was 46.8% (187 of 400), while 3,961 of 8,000 possible critical ratings, or 49.5%, were not retained. | partly covered by `dev/TESTING.md` requirements to report sample, exclusions, and uncertainty. | The repository lacks raw demographics and the paper reports no preregistration or IRB identifier; the released raw ratings contain 401 user IDs rather than the reported 400. | Preserve sample and exclusion boundaries with every preference claim; do not infer population or dialect effects. | pending | not started |
| C09: High LHF-Score variants received 2,117 of 4,039 retained choices, or 52.4%, versus 47.6%; chi-square is 9.414 and p about 0.00215. | Direct main result and exactly reproducible from released aggregate counts. It is a small whole-passage preference difference after enriched stimulus selection and heavy exclusions. | not covered by a live rule; H24 can hold it as mechanism evidence. | The result does not estimate any single word's effect or validate a document classifier threshold. | Record as bounded aggregate preference evidence only; do not translate 52.4% into severity or authorship probability. | pending | not started |
| C10: The paper's mixed linear model reports intercept 0.524, N 4,038, item variance 0.006, and user variance 0.104. | Direct reported model. The released script uses linear `mixedlm` on binary outcomes and reads a headerless 4,039-row TSV with default header inference, dropping the first row and explaining N 4,038. | not covered by project behavior. | The model is not a logistic mixed model despite a misleading code comment, and no locked environment is supplied for rerun. | Preserve the model type and dropped-row explanation; do not use it as independent robustness beyond the paper's result. | pending | not started |
| C11: High-score variants containing `nuanced` were preferred 46.6%, versus 54.5% for pairs without it; the authors say more data are needed. | Direct exploratory post hoc counterexample, with no reported inferential test for the subgroup contrast. | partly covered: a single `nuanced` passes #7, while a constructed three-word cluster fails; H24 can preserve word-context interactions. | A categorical `nuanced` warning would run against this observed preference reversal and exceed the evidence. | Keep `nuanced` as an evaluation counterexample and require interaction/context analysis; do not strengthen its live treatment. | pending | not started |
| C12: 28 of 32 words collected from prior overuse literature occur in the Base-versus-Instruct list. | Direct overlap count, but the 32-word list is inherited from cited research and the overlap uses the paper's unreleased 814-item subset. | partly covered: #7 contains many surface forms and `pattern-opportunities.md` already maps the source to register-specific density. | Overlap does not supply current prevalence, independence, per-document validity, or proof of LHF causation. | Retain as corroborating candidate-recognition evidence only; upstream studies remain separate sources. | pending | not started |
| C13: Three human-created instruction-tuning datasets totaling 0.7m tokens do not show a clear majority of 29 tested overuse lemmata above a 337.6m-token PubMed baseline. | Direct OSF supplement. Six lemmata are marked significantly higher, five significantly lower, and the rest non-significant; the comparison is cross-domain and highly size-imbalanced. | not covered in live rules; H25 partly covers mechanism uncertainty. | The supplement's underlying combined dataset, analysis code, and multiplicity treatment are not preserved, so it is a bounded null rather than a reproduction. | Record as a null against simple human-instruction-data origin; take no product action. | pending | not started |
| C14: The instruction-tuning supplement reports both increases and decreases, including significantly higher `underscore_NOUN`, `showcase_NOUN`, `realm_NOUN`, `showcase_VERB`, `notable_ADJ`, and `intricate_ADJ`, but significantly lower `potential_ADJ`, `crucial_ADJ`, `pivotal_ADJ`, `significant_ADJ`, and `potential_NOUN`. | Direct supplementary table. Domain mismatch means direction may reflect instruction versus biomedical register rather than training mechanism. | partly covered conceptually by H24's increasing/decreasing and register-specific approach; the live #7 list is flat. | Flat blacklists erase direction, POS, and baseline dependence. | Preserve the table as mechanism context and require domain-matched controls before reuse. | pending | not started |
| C15: The paper's 52.4% result concerns whole generated variants, not preferences for isolated lexical items. | Direct design boundary. The authors aim to hold length and content equal, but do not manipulate one word at a time or report formal semantic equivalence. | fully covered by `human-eyes/references/process.md` meaning-preservation and evidence-boundary guidance. | Source summaries can overstate the result as participants preferring “certain words.” | Use “preferred high-score generated variants” and retain the whole-passage boundary in every citation. | pending | not started |
| C16: Other syntactic, stylistic, factual, or content differences may correlate with LHF-Score, and the experiment only imperfectly emulates LHF work. | Direct limitation. Qualitative inspection found no clear confound, but no blinded equivalence annotation or formal control is reported. | partly covered: `dev/TESTING.md` requires matched register and length, provenance, and likely genre or formatting confounds, but not semantic or factual equivalence review of experimental passage pairs. | The current items may reward or punish content changes rather than lexical density; independent semantic and factual pair review is missing. | Require independent semantic and factual pair review before using released items as fixtures. | pending | not started |
| C17: Age, geography, dialect, evaluator skimming, and style-over-content are possible explanations for the observed preference. | Author interpretation plus cited external work; none is manipulated or compared in this study. The paper itself says discrimination among explanations needs future research. | fully covered by non-authorship and bias cautions; no demographic pattern exists. | Promoting these explanations would turn untested social hypotheses into mechanism or demographic tells. | Record as indirect context only; do not add demographic or labour claims without direct-source review. | pending | not started |
| C18: Whether lexical overuse is misalignment and whether developers should intervene depend on whose preferences should govern. | Direct normative conclusion. Workforce diversification and post-collection balancing are proposed options, not evaluated outcomes. | fully covered by the project's separation of evidence from user decisions. | No human-eyes product decision follows from the paper alone. | Leave intervention and policy recommendations unadopted; record them only as author proposals. | pending | not started |
| C19: The current supporting repository is useful but not a full independent reproduction. | Direct inspection of all 63 files at commit `db52b0e`; complete raw and filtered ratings, 30 item pairs, a focal table, code, and examples are present, but full generation corpora, environment lock, fixed seeds, raw demographics, database, and publication-time revision are absent. | fully covered by the refreshed snapshot and attachment provenance. | Repository completeness must not be confused with full experimental reproducibility. | Preserve the archive and exact gaps; independently recompute before any product use. | pending | not started |
| C20: The paper and current repository disagree on GPT-4o versus GPT-4o-mini, 814 versus 1,480 focal entries, the published 25-pair no-filler task versus code constants for five critical and ten filler items, five-or-more too-fast items versus the website marking a user on the fourth, and 400 participants versus 401 raw user IDs. | Direct paper-code-data comparison. The 4,039 released filtered ratings and 2,117 versus 1,922 main counts do agree; the mixed-model script's header inference explains its 4,038 rows. | not covered by live product behavior; source-ingest provenance now records the discrepancies. | These conflicts prevent claiming exact end-to-end reproduction or a uniquely identified experimental build. | Keep the source usable for bounded findings but require author clarification or an independently reconstructed pipeline before test adoption. | pending | not started |
| C21: The authors say the candidate procedure could inform AI-generated-text detection because such methods often use atypical lexical items and distributions. | Direct author proposal, not a tested detector result. The study reports no document-level classifier, calibration, threshold, sensitivity, specificity, false-positive rate, or authorship evaluation. | fully covered in framing: `patterns.json`, `human-eyes/references/process.md`, H3, and `dev/TESTING.md` reject one-word authorship proof and require explicit non-authorship reporting. | No live behavior gap follows, and using the paper as detector validation would exceed its evidence. | Record as bounded future relevance only; do not change checks, thresholds, or authorship framing. | pending | not started |

## Recommendations

- C01: Test-adapt a recomputed source-specific lexical profile only within H24 evaluation; do not change product files.
- C02: Preserve the 813-of-814 report and 814-versus-1,480 discrepancy; clarify or recompute before adoption.
- C03: Keep LHF as a mechanism hypothesis tied to the exact model pair.
- C04: Require source/context artifact inspection and negative controls.
- C05: Treat released pairs as enriched stimuli, not prevalence examples, and audit semantic equivalence before reuse.
- C06: Do not adopt the raw LHF-Score as a live detector.
- C07: Record the score and length means as construction details only.
- C08: Keep participant, demographic, exclusion, and provenance boundaries attached to results.
- C09: Record the 52.4% result as bounded aggregate preference evidence only.
- C10: Preserve the linear-model and dropped-row details; do not claim an independent logistic robustness check.
- C11: Keep `nuanced` as a counterexample and do not strengthen its live treatment.
- C12: Treat the 28-of-32 overlap as corroborating candidate-recognition evidence only.
- C13: Preserve the instruction-tuning null and take no product action.
- C14: Retain direction, POS, and cross-domain limits for supplementary terms.
- C15: Describe the outcome as preference for whole high-score variants, not isolated words.
- C16: Require independent semantic and factual pair review before fixture use.
- C17: Keep demographic, dialect, labour, and task explanations as indirect hypotheses.
- C18: Leave intervention and policy proposals unadopted.
- C19: Treat the repository as supplementary provenance, not a full reproduction.
- C20: Resolve paper-code-data discrepancies before test or product adoption.
- C21: Preserve detection relevance as an author proposal only; make no product or authorship change.

## Evaluation of approved changes

- C01: passed - DR-125 adds exact #7 recognition for `nuance`, `nuances`, `nuancing`, `firstly`, `reliance`, and `generalizability`; the focused test confirms each is counted once.
- C02: not applicable - pending recommendation; no product change requested.
- C03: not applicable - pending recommendation; no product change requested.
- C04: not applicable - pending recommendation; no product change requested.
- C05: not applicable - pending recommendation; no product change requested.
- C06: not applicable - pending recommendation; no product change requested.
- C07: not applicable - pending recommendation; no product change requested.
- C08: not applicable - pending recommendation; no product change requested.
- C09: not applicable - pending recommendation; no product change requested.
- C10: not applicable - pending recommendation; no product change requested.
- C11: not applicable - pending recommendation; no product change requested.
- C12: not applicable - pending recommendation; no product change requested.
- C13: not applicable - pending recommendation; no product change requested.
- C14: not applicable - pending recommendation; no product change requested.
- C15: not applicable - pending recommendation; no product change requested.
- C16: not applicable - pending recommendation; no product change requested.
- C17: not applicable - pending recommendation; no product change requested.
- C18: not applicable - pending recommendation; no product change requested.
- C19: not applicable - pending recommendation; no product change requested.
- C20: not applicable - pending recommendation; no product change requested.
- C21: not applicable - pending recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/juzek_alignment_reviewer
- **Findings resolved:** 5 initial material findings resolved: participant-versus-rating exclusions corrected; C16 coverage narrowed; PDF extraction counts and table structure corrected; the website speed-threshold mismatch added; and detection relevance added as bounded C21. The same reviewer completed a focused recheck with 0 residual material findings.
- **Unresolved findings:** none
