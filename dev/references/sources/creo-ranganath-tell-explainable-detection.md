# Show, Don't TELL: Explainable AI-Generated Text Detection

## Metadata

- **URL:** https://arxiv.org/abs/2605.27921
- **Author / owner:** Aldan Creo and Suraj Ranganath
- **Published:** 2026-05-27
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Academic empirical preprint on explainable AI-generated text detection
- **Evidence tier:** Academic empirical preprint; not yet peer reviewed
- **Review mode:** new
- **Stable identifier:** arXiv:2605.27921v1; DOI 10.48550/arXiv.2605.27921
- **Version / revision:** v1, submitted 2026-05-27
- **Full-text status:** complete
- **Snapshot:** `snapshots/creo-ranganath-tell-explainable-detection.md`
- **Extraction method:** Official arXiv v1 PDF downloaded and converted from its embedded text layer with Poppler `pdftotext -layout`; ar5iv HTML used as an alternate reading and structure check; pages 1, 15, and 30 rendered for visual verification
- **Snapshot SHA-256:** `88507571b9422c2ff4f7d546b71ba1489a6dbb5979b994ba528d227045fb4980`
- **Model / corpus scope:** English binary human-versus-AI detection. Base policy GPT-OSS-120B; GPT-5.5 and GPT-5.4 used in SFT data production; Grok-4.1-Fast used as the RL credibility judge. The RL corpus aggregates 9,179,122 rows from 10 public sources across 15 reported domains, with 5,000-item validation and test sets. Table 7 reports 13 test-domain rows without explaining the difference from the 15-domain corpus description. Explanation evaluation uses 200 held-out documents, five human comments per document, and five LLM judges. Qualitative Appendix A examples compare TELL with the closed-source Pangram web detector as accessed 2026-05-26.
- **Access limitations:** none for the paper. The arXiv HTML endpoint returned 404; ar5iv was accessible but lossy for mathematical values and complex layouts. The complete 30-page official PDF is preserved and authoritative. Linked code, data, weights, interface, and cited works were not recursively ingested.
- **User queue title:** `Show, Don't TELL`
- **Title mismatch:** The work at the authoritative URL is titled `Show, Don't TELL: Explainable AI-Generated Text Detection`; the queue title omits the subtitle.

## Summary

This arXiv v1 preprint presents TELL, an English AI-generated-text detector that emits span-level natural-language explanations alongside a binary score. The authors train GPT-OSS-120B first on model-produced and human-derived annotations, then with GRPO using a model judge and a multi-domain corpus. TELL reports AUROC 0.927 and TPR 0.638 at 1% false-positive rate on a 5,000-document benchmark. Its explanations achieve a mean 72.3% listwise win rate against style-normalized human comments under five LLM judges. For human-eyes, the strongest contribution is design and evaluation evidence for specific, checkable, source-grounded findings that leave judgement with the user. The paper does not validate its qualitative span examples as a universal prose-tell taxonomy, and its own limitations include anchoring, English-only evaluation, binary full-document labels, impossible-to-explain cases, model-judge evaluation, reward hacking, source-copy corruption during training, and no direct human evaluation of explanation quality.

## Main insights

- TELL is designed around readable evidence rather than a score-only verdict, while still returning a score for comparison with other detectors.
- The authors explicitly state that detectors can fail, newer models can require retraining, and users should decide after inspecting the evidence and context.
- TELL reports AUROC 0.927 and TPR 0.638 at 1% false-positive rate. Its AUROC lead over MAGE and Pangram EditLens is not statistically significant, and per-domain results vary substantially.
- The explanation evaluation asks whether annotations are concrete, falsifiable, coherent, plausible, and grounded. Five LLM judges prefer the sampled TELL explanation to style-normalized human comments in 72.3% of pairwise comparisons on average.
- The explanation result is not a human evaluation. Human comments were rewritten into TELL-like style, and the authors say a direct human study was not run because of budget limits.
- Explanations can anchor users to a wrong output. The authors try to reduce this risk through evidence-focused prompts and balanced AI- and human-leaning annotations, but do not evaluate user reliance.
- Some failed documents contain no specific, human-verifiable tell. The authors describe explainable detection as sometimes impossible.
- The study is English-only and tests fully human against fully AI-generated documents. Multilingual transfer and mixed authorship remain open.
- Appendix A shows that contradictions, fabricated authorities, unsupported statistics, rubric claims without evidence, arithmetic errors, code errors, and invented APIs can give readers more checkable information than stylistic scores.
- Appendix A also offers human-leaning cues such as local personal detail, unfinished uncertainty, code-switching, irregular grammar, idiom, and comic rhythm. These are qualitative model outputs, not controlled estimates of cue validity.
- During RL, the model learned to append generic authority language such as calling spans common strong AI signs, and fabricated claims of familiarity with an author's punctuation. The judge rewarded credibility performance until its prompt was changed.
- The annotation judge's worked examples also assign near-categorical credibility to claims about typos, false facts, and phrases no human would write. These examples show that concrete mechanisms can still encode unsupported authorship assumptions.
- The training prompts require granular spans, exact copying, mechanism-based explanations, and both AI- and human-leaning tells. This resembles human-eyes' evidence-led report shape but serves a different binary-classification objective.
- During RL, the policy sometimes corrected source errors, repeated structural tokens, or hallucinated false output. The authors applied format fixing and a copy-and-structure loss, but do not report a failure rate.
- Appendix A's mixed-script homoglyph example concerns an adversarial or pipeline transformation that a binary human-versus-AI label cannot represent. The model's explanation does not isolate whether the substitutions came from an author, generator, encoding step, or copy pipeline.
- The paper contains reproducibility discrepancies: Appendix C prose says SFT ran for two epochs, while Table 4 lists one epoch; the stated 2,000 EditLens annotation examples plus 316 human-comment-derived examples are not reconciled with 1,440 total training examples; and the 15-domain corpus description is not reconciled with the 13 domain rows in Table 7.
- The authors disclose AI coding assistance and AI help with figures, visualizations, writing refinement, and Appendices C, E, and F. They state that all ideas and claims are their own.

## Evidence and claims to extract

- **Direct source reviewed:** Complete arXiv:2605.27921v1 PDF, 30 pages, including figures, tables, Limitations, Ethical considerations, acknowledgements, references, prompts, qualitative examples, training details, detector benchmarks, and win-rate evaluation.
- **Method and sample:** SFT teaches the annotation format using GPT-5.5 comparisons of EditLens pairs plus Russell et al. human commentaries transformed with GPT-5.5 and GPT-5.4. GRPO uses GPT-OSS-120B, a Grok-4.1-Fast credibility judge, curriculum sampling, replay, format correction, and token-role-specific rewards. The reported RL corpus contains 9,179,122 rows from 10 sources across 15 domains, balanced AI/human validation and test sets of 5,000 each, and a 200-document explanation evaluation with five human comments and five LLM judges per document.
- **Direct versus cited evidence:** C01-C16 below use this paper's design, reported results, examples, limitations, disclosures, or internal inconsistencies. Background claims about public trust, detector incidents, trained human accuracy, anchoring research, and earlier detector performance are cited evidence and were not adopted as direct findings from those underlying works.
- **Important limits and counterexamples:** Preprint status; English-only; binary full-document labels; no mixed-authorship evaluation; no direct human evaluation of explanation quality; five LLM judges can share style preferences; human comments were model-rewritten; TELL explanations are longer on average than human comments; the evaluation ranks convincingness rather than factual correctness under an external ground truth; per-domain performance varies; some documents have no explainable tells; explanations can anchor users; the RL judge was vulnerable to reward hacking and contains categorical worked examples; the policy sometimes corrupted or hallucinated copied source text during training; qualitative pattern examples are model outputs; the homoglyph example does not isolate the source of the transformation; closed-source baselines can change; linked artifacts were not separately reviewed; and the SFT epoch, SFT sample, and domain-count reporting is internally inconsistent or unexplained.

## Matched patterns / rules

- `human-eyes/SKILL.md`, `STRATEGY.md`, and `human-eyes/references/process.md`: exact product boundary against authorship classification, scores, confidence claims, and provenance accusations.
- `README.md`: pattern evidence with exact excerpts, contextual interpretation, and user action rather than a detector score.
- `human-eyes/scripts/judgement.json` `genre_specific`: academic, student-essay, and journalism branches already review citation support, weak evidence, rubric echo, surface polish masking weak reasoning, wrong dates, unverifiable quotes, and provenance.
- `human-eyes/scripts/patterns.json` `no-rubric-echoing`, `no-vague-attributions`, `no-promotional-language`, `no-rhetorical-questions`, `no-generic-conclusions`, `no-performed-candour`, and `overall-signal-stacking`: partial surface overlap with Appendix A examples, but none checks factual truth or internal contradiction.
- `human-eyes/scripts/judgement.json` `faux_specificity`, `generic_metaphors`, `underspecified_language`, `semantic_redundancy`, and `vacuous_connection`: partial coverage of generic or unsupported-sounding prose, but not verification of facts, arithmetic, code, or citations outside genre-specific review.
- `dev/TESTING.md`: complete Audits, raw agent-assessed evidence, weak/reversed pairs, false positives, genre controls, exact version refs, and separate deterministic and agent-assessed reporting.
- `dev/hypotheses.md` H12, H16, H17, H19, H25, and H28: genre calibration, multi-judge disagreement, a hand-labelled golden set, uncertainty, model/version residue, and higher-level comparison dimensions.

## Associated hypotheses

- H3: drop detection framing entirely.
- H9: field-guide look-alike disambiguation.
- H12: genre-aware threshold calibration.
- H16: multi-judge ensemble with disagreement surfaced.
- H17: calibration golden set for grader changes.
- H19: bootstrap confidence intervals on corpus claims.
- H25: model-family versus generic-AI residue.
- H28: originality, clarity, and formality as comparison dimensions.
- Proposed hypothesis: report explanations that name checkable local evidence and survive an unsupported-claim audit are more useful than score-only or generic credibility language, but can still increase anchoring unless the interface requires independent user assessment.
