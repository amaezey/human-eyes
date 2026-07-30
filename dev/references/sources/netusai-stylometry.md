# NetusAI: stylometry and AI detectors

## Metadata

- **URL:** https://netus.ai/blog/stylometry-explained-how-ai-detectors-fingerprint-your-writing
- **Author / owner:** Ejaz Ahmad / Netus AI
- **Published:** 2025-07-22T13:34:05.000+00:00
- **Retrieved:** 2026-07-16
- **Extracted:** 2026-07-16
- **Source type:** vendor explainer and product-marketing article
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** living page JSON-LD `dateModified` 2026-01-07T07:15:08.000+00:00; prior capture retrieved 2026-05-05 without a recorded revision identifier
- **Full-text status:** complete
- **Snapshot:** `snapshots/netusai-stylometry.md`
- **Extraction method:** direct canonical HTML parsed with Beautiful Soup and converted with html2text; rendered page cross-check; raw HTML and all six first-party article images preserved
- **Snapshot SHA-256:** `bee99e0f7bb74381d2060df36ef27512488210d75e87107f62d4be23bd550f24`
- **Model / corpus scope:** uncited English-language vendor guidance; mentions GPT-4, Claude 3 Opus, ChatGPT, BypassAI, ZeroGPT, Grammarly, academic and technical writing, ESL writers, marketing, listicles, product descriptions, and long-form guides; supplies no corpus, sample size, detector version, evaluation period, language comparison, calibration data, or controlled human baseline
- **Access limitations:** none for the article; linked claims were not recursively ingested and remain indirect unless already covered by a separate project source record

## Summary

Netus AI's living vendor article describes stylometry and perplexity as commercial AI-detector inputs, names sentence, vocabulary, punctuation, transition, grammar, formatting, and structural feature families, warns about false positives, and markets a detect-rewrite-retest bypass workflow. The refreshed record restores eight FAQ questions omitted by the prior Jina capture, preserves and transcribes all six images, and distinguishes article assertions, image-only assertions, examples, linked claims, and marketing advice. The page reports no method, sample, detector configuration, uncertainty, independent validation, or reproducible results, so it is candidate-feature and detector-UX context rather than pattern-validity, threshold, mechanism, or authorship evidence.

## Main insights

- The article's useful contribution is a plain-language inventory of candidate feature families and human look-alikes, not empirical proof that any listed feature distinguishes AI from human prose.
- It gives explicit false-positive cases for edited, non-native, technical, academic, marketing, and template-driven writing, but none is supported by a disclosed evaluation on this page.
- Its advice to add controlled errors, unsupported-looking specificity, decorative formatting, and detector-directed retries conflicts with human-eyes' meaning-preservation, closed-source, output-style, and non-authorship boundaries.
- The current project partly covers sentence-length variance, type-token ratio, exact repeated labels, list density, selected transitions, and formatting symbols. Those checks do not implement the vendor's claimed detector, feature definitions, or score formula.
- The page itself supplies counterexamples to categorical cues: human writing may be regular or polished, technical and academic prose may have low perplexity, and commercial classifications are probabilistic rather than definitive identification.

## Evidence and claims to extract

- **Direct source reviewed:** Canonical Netus AI article with JSON-LD `dateModified` 2026-01-07T07:15:08.000+00:00, normalized article-text SHA-256 `26f9028f0c284d0d4b506c1be444f4552ca391a237302ab2b2f24bb06af7fc52`, raw HTML, five inline images, feature image, and all eight FAQs.
- **Method and sample:** No study method or sample is reported. The page uses invented illustrative sentences, one claimed ZeroGPT score, product-interface descriptions, linked explanations, and prescriptive examples. Models and products are named without versioned testing conditions except the dated mention of Claude 3 Opus and the screenshot label `AI Bypasser (V2)`.
- **Direct versus cited evidence:** C01-C27 are claims made directly by the article or its images, but they are vendor assertions rather than direct measurements. C03, C04, C05, C08, C11, C12, and C13 link to other pages for definitions or support; those inherited claims are indirect here. C06, C07, and C09 supply no direct supporting link for their assertions. C11's 87% score and C26's 68% figure are reported without a reproducible method on this page.
- **Important limits and counterexamples:** The page discloses no dataset, human comparison, detector version, scoring implementation, threshold derivation, uncertainty, subgroup analysis, or independent validation. It admits false positives, low-perplexity legitimate genres, human-like model output, and a classification-versus-identification boundary. Its FAQ answer 3 ends with the apparent source truncation `like an A.`

## Matched patterns / rules

- G9 `sentence-length-variance`: partly covered; live code computes sentence-word-count standard deviation and uses `>4`, not the source's uniform `12-18`-word band or any commercial-detector score.
- B5 `vocabulary-diversity`: partly covered; live code computes document type-token ratio for 150+ words and flags `<=0.40`, while the source conflates lexical density, word-frequency categories, lexical diversity, pronouns, and passive voice.
- G6 `no-section-scaffolding`: partly covered; live code requires an identical short line at least three times. The source also names broader repeated templates and uniform list formatting.
- G3 `no-excessive-lists` and G4 `no-unicode-flair`: partly cover list density and decorative symbols, but the source recommends the same formatting variation that these checks can flag.
- E8 `no-formulaic-openers`, `no-signposted-conclusions`, and B1 `no-ai-vocabulary-clustering`: partly cover selected transition positions and phrases. Focused surface-only testing found no E8 match for `Therefore` or `Additionally`; `In conclusion` was found only by `no-signposted-conclusions`.
- C7 `no-em-dashes` and E5 `no-staccato-sequences`: challenge the source's explicit recommendation to inject em dashes and fragments as detector-evasion devices. The source also recommends ellipses and contractions, which have no equivalent live check.
- Agent assessments `tonal_uniformity`, `faux_specificity`, `structural_monotony`, `semantic_redundancy`, and `genre_specific`: adjacent context only; they do not reproduce NetusAI's detector claims or justify invented specificity.
- `human-eyes/references/process.md`: covers meaning preservation, closed-source factual fidelity, and complete-Audit validation; it conflicts with detector-directed edits and invented detail.

## Associated hypotheses

- H1 continuous calibrated register-distance score per pattern
- H9 field-guide voice with similar-species disambiguation per pattern
- H12 genre-aware threshold calibration
- H13 sentence-length mean as a grader check
- H22 long-tail compression and grammatical standardisation
- H23 nominalization and noun-heavy style
- H24 register-specific vocabulary density
- H25 model-family versus generic-AI residue
