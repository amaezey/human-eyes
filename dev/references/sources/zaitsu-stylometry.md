# Zaitsu et al.: Stylometry can reveal AI authorship

## Metadata

- **URL:** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335369
- **Author / owner:** Wataru Zaitsu, Mingzhe Jin, Shunichi Ishihara, Satoru Tsuge, and Mitsuyuki Inaba
- **Published:** 2025-10-27
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Peer-reviewed empirical study
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** DOI 10.1371/journal.pone.0335369; PLOS article e0335369
- **Version / revision:** Version of record published 2025-10-27; previous unversioned Jina capture retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/zaitsu-stylometry.md`
- **Extraction method:** Authoritative PLOS PDF downloaded directly; all 18 pages extracted with Poppler `pdftotext -layout`; pages 1, 9, and 18 rendered and visually checked; four first-party CSV supplements downloaded and parsed; PDF and supplements preserved as attachments.
- **Snapshot SHA-256:** `dd39c26bc3f923d9bb0a178ca11d35ce4c4524e8681caca503c6e3b550c77625`
- **Model / corpus scope:** 100 Japanese e-Gov public comments and 350 December 2024 zero-shot public-comment generations, 50 each from GPT-4o, o1, Claude 3.5, Gemini, Microsoft Copilot, Llama 3.1, and Perplexity; Study 2 collected responses on 2025-01-24 and 2025-01-25 and shows one shortest stimulus from each class to 403 Japanese adults retained from 1,103 respondents (229 men, 164 women, 10 preferring not to answer; ages 21-69, mean 47.6, median 49, SD 11.9).
- **Access limitations:** None for the version-of-record paper or four publisher supplements. The publisher materials do not include original texts, exact prompts, provider/API model identifiers or settings, Study 2 confidence ratings, or free-text comments. S1-S3 are CP932 CSV files. The prior card recorded no snapshot digest; the archived bytes match the repository's pre-update snapshot and hash to `6c6aec123a187c08ad6058141988ae6c49b30358754da02a0476e8cb83e31561`.

## Summary

This two-study Japanese public-comment paper reports strong closed-sample separation from high-dimensional function-word, POS-bigram, and phrase-pattern distributions, then finds that lay judgments over eight single stimuli are inconsistent and sometimes confidently wrong. Its useful contribution is a bounded comparison between machine-extracted distributional features and human surface impressions. It does not validate an English prose tell, sentence-rhythm rule, vocabulary-diversity direction, universal threshold, current detector, mixed-authorship decision, or document-level authorship verdict.

## Main insights

- In Study 1, 450 known-origin Japanese public comments were represented by 318 function-word, 1,107 POS-bigram, and 1,313 phrase-pattern relative-frequency features. Integrated features visually separated the sampled human and LLM groups on MDS and a random forest with leave-one-out cross-validation reported 99.8% accuracy.
- The result is closed-set, in-sample-family evidence: one language, one genre, December 2024 zero-shot generations, uneven text lengths, reused human material, no independent domain or time holdout, and no released original texts or prompts.
- The advanced-model stylometry hypothesis failed. GPT-o1 was not generally closer to humans than GPT-4o; integrated-feature distance had Cohen's d = 0.00, and only phrase patterns moved in the predicted direction.
- Llama 3.1 was the model-family counterexample, forming a distinct MDS cluster from the other six LLM labels. The paper's parameter-count explanation is speculative.
- Study 2 retained 403 of 1,103 respondents and presented only one shortest text per class. Observed correct AI judgments ranged from 25.6% for the o1 stimulus to 56.8% for Claude 3.5; the human stimulus was called human by 45.2% and AI by 47.9%.
- Five report-to-table defects constrain Study 2: prose says 31.5% correctly identified the human text while Table 1/S4 show 45.2%; prose names GPT-4o as significantly deceptive while Table 1 marks GPT-o1; prose describes Llama 3.1 as having about half GPT-4o's human-rating odds although Table 2 gives beta -0.09 (OR about 0.91) with a wide interval crossing zero; prose calls the human stimulus significantly less likely to receive "Neither" although its interval crosses zero; and converting o1's 2.39 relative odds ratio into a 70% deception probability is invalid and conflicts with the observed 59.3% human rating.
- Participants mentioned phraseology, expression, word endings, conjunctions, and punctuation, but the source provides no coding protocol, denominator per cue, cue accuracy, raw comments, or false-positive analysis. These are impressions, not validated surface rules.
- The paper does not measure sentence-length variance or type-token ratio. Its former G9 and B5 mappings should be retired; its direct project value is narrow stylometric-method context, detector-framing caution, and evidence for language-, genre-, model-, prompt-, length-, and time-bounded evaluation.

## Evidence and claims to extract

- **Direct source reviewed:** PLOS One version of record, 18 pages, DOI 10.1371/journal.pone.0335369, plus all four first-party CSV supplements: S1 function words, S2 POS bigrams, S3 phrase patterns, and S4 Study 2 judgments.
- **Method and sample:** Study 1 compares 100 reused Japanese e-Gov comments with 350 December 2024 zero-shot generations across seven named product/model labels. It normalizes within-text feature counts, visualizes symmetric Jensen-Shannon distances with two-dimensional metric MDS, and applies a 1,000-tree random forest with leave-one-out cross-validation. Study 2 uses a within-participant web survey, one shortest stimulus per class, seven-point source judgments, six-point confidence ratings, and Bayesian multinomial/ordinal models with participant random intercepts.
- **Direct versus cited evidence:** C01-C09, C11-C23, and C25-C27 are direct results, preserved-data checks, author interpretations, or reviewer analyses of this source. C10 and the phrase-pattern recall figures within it are inherited from references 10 and 11 and remain indirect here. Claims about cognitive biases, Llama training/size, market tools, and future harms are author interpretation or cited context, not direct validation.
- **Important limits and counterexamples:** The paper's strongest classifier result has no external holdout, released raw texts, exact prompts, current-version replication, mixed-authorship test, open-set unknown-model test, or cross-language/genre transfer. Study 2 has one content-confounded stimulus per class, a 63.5% exclusion rate, missing confidence/comment data, internal numerical/reporting conflicts, and a text-type/distance model whose predictors cannot be separated cleanly with one fixed stimulus per type.

## Matched patterns / rules

- `human-eyes/scripts/patterns.json` and `human-eyes/scripts/grade.py`: G9 `sentence-length-variance` and B5 `vocabulary-diversity` are not measured by this source; current source mappings are unsupported.
- `human-eyes/references/process.md`: the product boundary already says Audits describe patterns and do not infer authorship; fully covers the safe interpretation of this source.
- `dev/TESTING.md`: matched genre, length, provenance, complete-Audit, human-look-alike, and no-authorship-classification requirements cover the main controls this source lacks.
- H1 continuous calibrated register-distance score, H2 comparison-engine reframe, H3 drop detection framing, H12 genre-aware threshold calibration, H24 register-specific vocabulary density, and H25 model-family versus generic-AI residue are relevant research homes. The source is adjacent methodological evidence, not validation of a live score or rule.

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern: adjacent support for distributional comparison, but no human-eyes pattern calibration or reliability curve.
- H2 comparison-engine product reframe: adjacent support for comparisons among known groups; no validation of a two-document product output.
- H3 drop detection framing entirely: the closed-sample classifier result challenges a blanket impossibility claim but does not justify human-eyes authorship classification.
- H12 genre-aware threshold calibration: directly supported as a required control by the paper's Japanese public-comment boundary.
- H24 register-specific vocabulary density: not directly tested; the paper uses Japanese function words, POS bigrams, and phrase patterns rather than English vocabulary density.
- H25 model-family versus generic-AI residue: supported as a research question by Llama 3.1's distinct cluster and GPT-o1's stylometric null, not as a product-facing model fingerprint.
