# Copyleaks AI Detector

## Metadata

- **URL:** https://copyleaks.com/ai-detector
- **Author / owner:** Copyleaks
- **Published:** living product page; current reader metadata reports 2026-07-12
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** vendor detector product page
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** living page rendered 2026-07-15; prior reviewed page captured 2026-05-05 at the former `/ai-content-detector` URL
- **Full-text status:** complete
- **Snapshot:** `snapshots/copyleaks-detector.md`
- **Extraction method:** complete canonical-page reader Markdown retrieved with `curl`, reduced mechanically to main content, checked against the rendered first-party page at the beginning, middle, and end, with five explanatory first-party image assets and one decorative scale icon downloaded and visually inspected
- **Snapshot SHA-256:** `19083b3076cc5fce4bca87b1066e084370be211e2431be2e03de2bff2cf5490d`
- **Model / corpus scope:** product page claims GPT-5/GPT-4/ChatGPT, Claude, Gemini, DeepSeek, Llama, Bloom, Rytr, Jasper and more; over 30 languages; blogs, essays, resumes, social posts, fiction, newsletters, institutional text, and source code. It names no detector version. The current linked first-party methodology extraction (reader metadata 2026-07-14), inspected only for scope, reports English texts longer than 350 characters: a 500,000-text Data Science set and a separate 248,555-text QA set. It supplies no test date in the current extraction and labels only its sensitivity-results table as model v10.
- **Access limitations:** direct unauthenticated HTTP and a fresh automated-browser session were blocked by Cloudflare. A rendered first-party reading route exposed all main content, which matched the complete reader extraction. Page chrome and other decorative icons were excluded; five explanatory images and one decorative scale icon were preserved. Linked methodology, study-roundup, non-native-English, and Grammarly pages were inspected for scope/directness but were not ingested as part of this source.

## Summary

Copyleaks' living vendor page markets an AI-text classifier, explains its output and workflow, names four feature families, gives language, length, sensitivity, model, and use-case boundaries, and makes accuracy and false-positive claims. The complete capture is useful for detector-product contrast, version and minimum-length caveats, and scrutiny of score/explanation UX. It is not independent validation: most claims are vendor assertions, the advertised aggregate metrics are not tied on the page to a named detector version or complete reproducible dataset, linked studies are summarized by Copyleaks, and neither the product page nor its screenshots establishes authorship or validates a human-eyes rule.

## Main insights

- The page now says `over 99%` accuracy and `.03%` false positives, not the prior card's `0.2%`; the current linked vendor methodology gives English result tables and model-v10 sensitivity trade-offs, while the product page does not bind its headline to that exact test.
- Copyleaks names frequency ratios, parts of speech, syllable dispersion, and hyphen usage as classifier inputs. It provides no feature weights, operational definitions, ablation, per-feature accuracy, manual rule, or matched human comparison from which human-eyes could adopt a check.
- The page exposes minimum-length and sensitivity boundaries: 350 characters for the extension, 255 for the web platform, 25,000-character extension maximum, and 2,000-page web maximum. Its linked methodology evaluation excluded texts at or below 350 characters.
- The page claims low false-positive rates for non-native English text, but supports that subgroup assertion only through a linked Copyleaks blog not ingested here; the target page supplies no subgroup definition, sample, threshold, uncertainty, or independent comparison.
- The score and AI Logic screenshots are illustrative product UI. Phrase-frequency ranges and source matches are not calibrated authorship proof, independent pattern validity, or evidence that a highlighted phrase should be rewritten.
- The revise-and-rescan workflow can encourage detector-directed camouflage and meaning drift despite the page's statement that the product is for education rather than evasion.
- The page supplies no confidence intervals, calibration analysis, mixed-authorship evaluation protocol, per-genre metrics, feature ablation, multilingual raw data, or model-build identifiers for its broad claims.

## Evidence and claims to extract

- **Direct source reviewed:** complete Copyleaks `AI Detector` main page at canonical URL `https://copyleaks.com/ai-detector`, rendered and captured 2026-07-15, including all 13 product-page sections, 11 FAQ questions, numeric language/length claims, links, five explanatory image assets, and one decorative scale icon.
- **Method and sample:** the target source is a living vendor product page, not a study. It says the system uses linguistic modelling, deep learning, AI Logic, and training on trillions of human-written documents, but supplies no direct dataset inventory or reproducible method. The current linked first-party methodology extraction (reader metadata 2026-07-14) reports an English evaluation on texts longer than 350 characters: 300,000 human and 200,000 AI texts for Data Science, plus 229,843 human and 18,712 AI texts for QA; its teams are both internal to Copyleaks. The extraction supplies no test date and labels only its sensitivity-results table as model v10.
- **Direct versus cited evidence:** C01 and C03-C26 are direct observations of Copyleaks' own page or its preserved UI assets, not independent verification. C02 is explicitly inherited from studies summarized by a linked Copyleaks blog; those studies were not directly ingested here. Linked first-party methodology details qualify C01, C03, C18, C20, C22, and C24 but remain vendor self-evaluation rather than independent evidence.
- **Important limits and counterexamples:** the product page does not identify the detector version behind its headline, disclose per-language or non-native-English subgroup dataset sizes, publish mixed-text tests, explain score calibration, quantify genre performance, define the four named feature families, or report uncertainty. The linked methodology covers English texts over 350 characters and reports different model-v10 sensitivity trade-offs, so the headline cannot be generalized to every language, language-background subgroup, genre, length, model, paraphrase, or mixed-authorship condition. Human writing can contain every named surface feature.

## Matched patterns / rules

- `human-eyes/references/process.md` `Product boundary`: fully covers the rule that reports describe patterns and do not infer who or what wrote text.
- `human-eyes/references/process.md` `Report the result`: fully covers the prohibition on scores, confidence claims, fixed-count checklists, and authorship statements.
- Root `README.md` lines 5 and 34: distinguishes a pattern detector from a commercial AI detector; the page supplies contrast, not evidence for a pattern.
- `dev/references/sources/pattern-opportunities.md` `Detector-output caveat wording`: partly covered, but Copyleaks directly supports only its own length/sensitivity/confidence conditions, not the row's generic `single data point, not a definitive answer` wording.
- `dev/references/sources/pattern-opportunities.md` `Product detector scores or thresholds as rule severity`: fully covers the non-promotion of Copyleaks metrics.
- B1 `no-ai-vocabulary-clustering`, C6 `no-compound-modifier-density`, and G9 sentence-rhythm variance: not supported by Copyleaks' opaque frequency-ratio, hyphen-usage, or syllable-dispersion labels.

## Associated hypotheses

- H3 `Drop detection framing entirely`: directly informed by the contrast between commercial classifier claims and human-eyes' no-authorship boundary.
- H9 `Field-guide voice with similar-species disambiguation per pattern`: informed only as caution; Copyleaks supplies no human look-alike inventory for its named features.
- H12 `Genre-aware threshold calibration`: broad product-page genres without per-genre metrics reinforce the need not to generalize a pooled vendor headline.
- H19 `Bootstrap confidence intervals on corpus claims`: the product page's point estimates and absent uncertainty are relevant context, not evidence for a project threshold.
- H25 `Model-family versus generic-AI residue`: broad model-family claims without build identifiers reinforce version metadata requirements.
