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

## Skill-use audit

- **Good use:** product-landscape context; minimum-length, version-drift, sensitivity, score-label, and vendor-evidence caveats; contrast with human-eyes' quoted-pattern and no-authorship boundary.
- **Misuse / overclaim:** treating `.03%`, `over 99%`, an 80%/100% screenshot score, phrase-frequency ranges, or a vendor study roundup as independent accuracy evidence or a human-eyes severity threshold.
- **Unsupported use:** authorship proof; a universal model/language/genre claim; individual-word or phrase validity; causal explanations; transfer of Copyleaks' opaque frequency, POS, syllable, or hyphen features into a deterministic rule; rewriting a source merely to lower a commercial detector score.
- **Underused evidence:** the existing Copyleaks mapping should name its exact 255/350-character minima, sensitivity/version scope, `.03%` current headline, and the difference between illustrative UI, vendor self-test, and direct independent evidence.
- **Patterns left on the table:** none suitable for promotion. The four feature families are only product descriptions and do not establish #7 vocabulary clustering, #18 compound-modifier density, #52 sentence-rhythm variance, or any new pattern.

## Matched patterns / rules

- `human-eyes/references/process.md` `Product boundary`: fully covers the rule that reports describe patterns and do not infer who or what wrote text.
- `human-eyes/references/process.md` `Report the result`: fully covers the prohibition on scores, confidence claims, fixed-count checklists, and authorship statements.
- Root `README.md` lines 5 and 34: distinguishes a pattern detector from a commercial AI detector; the page supplies contrast, not evidence for a pattern.
- `human-eyes/references/sources/pattern-opportunities.md` `Detector-output caveat wording`: partly covered, but Copyleaks directly supports only its own length/sensitivity/confidence conditions, not the row's generic `single data point, not a definitive answer` wording.
- `human-eyes/references/sources/pattern-opportunities.md` `Product detector scores or thresholds as rule severity`: fully covers the non-promotion of Copyleaks metrics.
- #7 `no-ai-vocabulary-clustering`, #18 `no-compound-modifier-density`, and #52 sentence-rhythm variance: not supported by Copyleaks' opaque frequency-ratio, hyphen-usage, or syllable-dispersion labels.

## Associated hypotheses

- H3 `Drop detection framing entirely`: directly informed by the contrast between commercial classifier claims and human-eyes' no-authorship boundary.
- H9 `Field-guide voice with similar-species disambiguation per pattern`: informed only as caution; Copyleaks supplies no human look-alike inventory for its named features.
- H12 `Genre-aware threshold calibration`: broad product-page genres without per-genre metrics reinforce the need not to generalize a pooled vendor headline.
- H19 `Bootstrap confidence intervals on corpus claims`: the product page's point estimates and absent uncertainty are relevant context, not evidence for a project threshold.
- H25 `Model-family versus generic-AI residue`: broad model-family claims without build identifiers reinforce version metadata requirements.

## Questions / follow-up

- If any third-party accuracy result is needed as evidence, ingest the exact study directly rather than the Copyleaks roundup.
- Consider a separate source ingestion for the current testing-methodology page if its full tables and model-v10 sensitivity results will inform evaluation UX; this card uses it only to bound vendor claims.
- No source access is missing for this product-page ingestion.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/copyleaks-detector/2026-05-05-d741d1d4.md` | 2026-05-05 | `d741d1d464033d66b59600dda6999683b06facaf838f3d3c6c34d37aceadc4da` |
| current | none found | `snapshots/copyleaks-detector.md` | 2026-07-15 | `19083b3076cc5fce4bca87b1066e084370be211e2431be2e03de2bff2cf5490d` |

## Decision history

- The previous unkeyed review contained no recorded user decisions or implementations. Its `0.2%` false-positive figure is retired: the current product page says `.03%`; a separate `0.2%` figure appears in one study summarized by the linked vendor roundup and cannot substitute for the live product claim.
- The prior generic mappings for confidence, customizable sensitivity, and higher character count are preserved as claim-keyed C18-C22 with exact product/version limits. No earlier product change is recorded or carried forward.

## Project coverage

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Copyleaks advertises `over 99%` accuracy and an `industry-low .03%` false-positive rate. | Direct vendor claim on a living product page. The page does not name the detector version, threshold, complete test set, uncertainty, or aggregation behind the headline. The linked internal methodology reports condition-specific values, not an independent universal result; only its sensitivity-results table is labelled model v10. | `pattern-opportunities.md` `Product detector scores or thresholds as rule severity` and `process.md` Product boundary; fully covered: human-eyes does not consume detector scores or infer authorship. | Existing Copyleaks card and index still carried `0.2%`; exact current scope and directness were absent. | Correct the source record and non-promotion mapping; do not use the metric for severity or authorship. Verify card, manifest, and opportunity row. | pending | not started |
| C02: The page says its accuracy is backed by independent third-party studies and says a July 2023 arXiv study declared Copyleaks most accurate. | Cited claim mediated by Copyleaks' own roundup. The target page supplies no direct study methods; an arXiv host is not proof of Cornell authorship or endorsement. | H3 and source-ingest directness rules; partly covered as general vendor-evidence caution. | No claim-keyed distinction between the product-page assertion, vendor roundup, and direct study evidence. | Record as indirect and unresolved here; ingest any relied-on study separately before using it. | pending | not started |
| C03: Copyleaks claims support for over 30 languages, displays human/AI percentages for English, French, German, Italian, Portuguese, and Spanish, and claims low false-positive rates for non-native English text. | Direct vendor product-page assertions and six displayed point estimates for an unnamed `latest model`. The non-native-English assertion points to a separate Copyleaks blog not ingested here, so its supporting evidence is indirect in this record. The page supplies no language-background or proficiency definition, subgroup sample, per-language sample, threshold, corpus dates, uncertainty, or raw data; the linked methodology's disclosed datasets are English-only. | H9 look-alike controls, H12 genre calibration, H19 uncertainty, H25 version metadata, and [Liang](liang-detector-bias.md) detector-bias cautions; partly covered as evidence requirements and false-positive cautions, not as validation of Copyleaks' subgroup claim. | The project lacks direct or independent evidence for the non-native-English claim and has no reason to repeat the multilingual point estimates. | Preserve both as vendor scope only; do not generalize or treat the subgroup claim as fairness evidence. Directly ingest the linked blog or require an independent matched subgroup evaluation before reliance. | pending | not started |
| C04: The page claims detection for GPT-5/GPT-4/ChatGPT, Claude, Gemini, DeepSeek, Llama, Bloom, Rytr, Jasper, and new models as released. | Direct vendor coverage claim; no model builds, release dates, decoding settings, prompt sets, per-model samples, or per-model thresholds are supplied on the target page. | H25 model-family/version drift and source metadata convention; partly covered. | Broad model coverage could be mistaken for current universal validity. | Record model names and missing versions; take no product action. | pending | not started |
| C05: Copyleaks says it detects AI text blended with human writing and identifies human and AI elements in mixed text. | Direct vendor capability claim repeated in prose and FAQ. No mixed-authorship construction, span-label protocol, boundary metric, sample, or error analysis is published on the target page. | `process.md` Product boundary; fully covered against authorship/spans. Human-eyes reports patterns, not mixed-authorship labels. | The prior card repeated mixed-text detection without recording absent validation. | Keep as vendor-product context only; do not imitate span authorship labels. | pending | not started |
| C06: AI Logic says AI Phrases reports how often document text originates from AI versus human sources, while AI Source Match finds submitted text already published elsewhere. | Direct vendor description. The page does not define the reference corpora, frequency unit, denominator, phrase-selection method, threshold, update date, or relationship between source match and generation. | Human-eyes reports exact matched constructions but has no probabilistic source matching; not covered by design. | Phrase frequency and source overlap could be confused with pattern validity or authorship. | Record the distinction; do not map AI Logic output to a human-eyes check. | pending | not started |
| C07: Preserved UI images show `AI Content Found` scores of 80% and 100%, source-match results, phrase counts, and relative phrase-frequency ranges. | Direct first-party illustrative assets. They are unlabeled examples, not evaluation cases; source texts, ground truth, model version, threshold, and expected interpretation are undisclosed. | `process.md` prohibits scores/confidence claims; fully covered. | The images were absent from the old evidence record. | Preserve the assets as product-UX examples only; take no product action. | pending | not started |
| C08: Copyleaks offers browser, Google Docs, API, and LMS surfaces; AI Logic requires a subscription, while a free account unlocks sentence-level insights, highlighted AI-written phrases, and pattern breakdowns. | Direct product-surface and access-tier claims; not prose-pattern evidence. The page distinguishes subscription-gated AI Logic from free-account sentence and pattern views. Surface and account-tier differences may imply different minima or outputs. | H25/source metadata convention; partly covered as platform metadata. | The old card grouped integrations without surface-specific boundaries, and the draft incorrectly described the sentence-level/pattern views themselves as paid. | Record the surfaces and access tiers and keep results surface/version-specific; no product change. | pending | not started |
| C09: The free workflow accepts up to 25,000 characters without login, while account plans and other surfaces have different limits. | Direct vendor product-limit claim. The FAQ separately gives extension and web-platform bounds; pricing/credit availability can change. | No live project coverage required; not covered and outside the human-eyes product path. | Marketing copy could be mistaken for a method condition. | Keep as living product metadata only; take no further action. | pending | not started |
| C10: Copyleaks names frequency ratios, parts of speech, syllable dispersion, and hyphen usage as classifier features. | Direct vendor feature-family claim. It supplies no definition, weight, direction, rate, ablation, threshold, per-language behavior, or manual feature output. Human use and deliberate punctuation are not compared. | #7 vocabulary clustering, #18 compound-modifier density, and #52 rhythm are superficially adjacent but not supported; not covered as equivalent features. | The old card incorrectly said there was no usable feature list, while a list now exists; its opacity still prevents mapping. | Record all four families and explicit non-equivalence; do not add or strengthen a check. | pending | not started |
| C11: Results show a percentage `likely AI-generated`, sentence-by-sentence highlights, and pattern breakdowns. | Direct vendor output claim. The page does not say the percentage is calibrated probability, expose threshold behavior, or provide confidence intervals. | `process.md` `Report the result` and Product boundary; fully covered by the no-score/no-authorship design. | Existing detector-caveat row did not distinguish likelihood wording from calibration evidence. | Keep product contrast; do not add a human-eyes score. | pending | not started |
| C12: Users are told to rewrite flagged phrases in their own words and rescan until results change. | Direct workflow instruction. No semantic-preservation check, factual-fidelity test, voice control, or evaluation of detector-directed rewriting is supplied. | `process.md` Preserve meaning, `voice.md` Preserve the source, and `SKILL.md` protected-literal contract; challenges the vendor workflow but is fully covered by project safeguards. | Detector-directed rewriting can become camouflage or alter meaning. | Add this source only to the explicit non-promotion/camouflage record; do not adopt the workflow. | pending | not started |
| C13: Copyleaks says false positives are minimized by distinguishing human text, using user feedback, and testing new-model detection before release. | Direct vendor process assertions without audit trail, feedback sampling, release criteria, or external verification on the target page. | H10 false-positive intake and H17 calibration golden set are adjacent; not covered as equivalent evidence. | Vendor process language could be mistaken for demonstrated fairness or robustness. | Record as unverified operational claim; take no product action. | pending | not started |
| C14: The detector uses linguistic modelling, deep learning, proprietary AI Logic, and training on `trillions of human-written documents`. | Direct vendor architecture/training-scale claim. Units, deduplication, provenance, dates, language/genre mix, licensing, train/eval separation, and model architecture are undisclosed. | No project implementation; not covered and not needed for a pattern catalogue. | The scale phrase invites unsupported mechanism and representativeness inferences. | Preserve exact vendor wording and gaps; do not use it as validity evidence. | pending | not started |
| C15: The page explains detection as recognizing LLM statistical patterns, deviations from known human patterns, and `specific AI signals`. | Direct vendor interpretation, not a reproducible scientific account. It gives no operational definition or counterexample and collapses diverse human writing into a reference class. | Root README and `process.md` Product boundary; fully covered against origin inference. | The page's explanation cannot establish that a visible deviation is AI-caused. | Record as vendor framing only; take no product action. | pending | not started |
| C16: Copyleaks claims visibility into plagiarism and paraphrased AI text, including source matching. | Direct bundled-product claim. The page does not separate plagiarism, memorized overlap, paraphrase detection, and generation classification metrics. | #41 source/provenance checks are manual factual review, not plagiarism or authorship classification; not covered as equivalent. | Source overlap could be mistaken for AI evidence, while absence of overlap proves neither originality nor human authorship. | Preserve the boundary; do not map to #41 or a prose rule. | pending | not started |
| C17: The page says the product is for AI education rather than evasion and promotes responsible, ethical, transparent use. | Direct normative marketing claim. It is not tested, and the same page instructs users to revise flagged phrases and rescan. | `process.md` and `voice.md` prohibit manufactured humanization and require source fidelity; challenges the vendor page's internal tension. | Stated intent does not remove evasion or semantic-drift risk. | Record the tension; take no further product action. | pending | not started |
| C18: The page markets results across blog posts, essays, resumes, social captions, reports, proposals, fiction, newsletters, institutional text, and other contexts. | Direct broad use-case claim. No per-genre accuracy, false-positive, calibration, minimum-length, or human-look-alike results appear on the target page. | H9 and H12; partly covered as requirements for genre/look-alike controls. | Pooled vendor metrics should not be applied across these registers. | Record genre breadth as claimed scope and absent validation; do not promote. | pending | not started |
| C19: An enterprise use case says detector output can ensure training data is exclusively `verified human-written content`. | Direct vendor use-case claim. A classifier output is not ground-truth verification; no audit, appeals, mixed/provenance protocol, or error consequence is supplied. | Product boundary; fully covered against authorship verification. | The word `verified` materially overstates what the page establishes. | Mark as unsupported verification framing; take no product action. | pending | not started |
| C20: Enterprise users can customize sensitivity to reduce false positives or find more nuanced rewrites. | Direct vendor capability claim. The target page gives no levels; the linked methodology labels its three internal sensitivity settings as model v10 and reports different FP/FN trade-offs. | H17/H19 and detector non-promotion row; partly covered as calibration context. | The old card named sensitivity but not the trade-off or version boundary. | Record as model-v10/product-specific context; do not derive a human-eyes threshold. | pending | not started |
| C21: Copyleaks claims detection of AI-generated source code, including altered code. | Direct vendor capability claim outside natural-language prose. No code benchmark or method appears on the target page. | No prose pattern coverage; not covered and out of scope. | Code attribution cannot transfer to prose or human-eyes severity. | Record as explicit product boundary; take no further action. | pending | not started |
| C22: More text is said to improve confidence; the extension accepts 350-25,000 characters and the web platform 255 characters to 2,000 pages. | Direct vendor input-boundary claim. The linked methodology evaluation includes only texts longer than 350 characters, leaving the 255-350 web band outside that disclosed test. No length curve is published. | `pattern-opportunities.md` detector caveat row; partly covered. Human-eyes has separate pattern-specific minimums, not a detector-wide authorship threshold. | Existing mapping lacked exact bounds and the disclosed-evaluation mismatch. | Update caveat mapping with exact vendor-specific limits; do not transfer them to human-eyes. | pending | not started |
| C23: Grammarly generative-rewriting features may trigger detection, while basic grammar and spell-check functions typically do not. | Direct product-page claim attributed to a linked Copyleaks blog. `May` and `typically` are qualified; the target page gives no sample, Grammarly version, feature list, rate, or independent test. | Source/assistance metadata and H25 are partly adjacent; no exact live check. | The distinction is time- and feature-specific and cannot establish authorship. | Preserve the qualification as vendor context only; no product change. | pending | not started |
| C24: Copyleaks says it continually retrains and refines models and adds new-model detection only after extensive testing. | Direct living-product process claim without releases, model cards, version history, or criteria on the target page. | H25 and source date/model metadata convention; partly covered. | A static source mapping will drift unless retrieval/version dates remain visible. | Keep living-page/version metadata and require refresh before future reliance. | pending | not started |
| C25: The page makes enterprise authenticity, integrity, compliance, security, IP, and educational-use claims. | Direct vendor marketing claims, mostly outside prose-pattern scope; the page lists certifications but this ingestion did not audit them. | No pattern coverage required; not covered and outside the source's human-eyes relevance. | Security/compliance or institutional adoption must not be treated as detector validity. | Record as out-of-scope product context; take no further action. | pending | not started |
| C26: The page omits confidence intervals, score-calibration evidence, feature definitions/ablation, mixed-text protocol, per-genre metrics, multilingual and non-native-English subgroup raw data, and model-build identifiers. | Direct completeness observation from the full product page, qualified by inspection of the linked methodology for what it does disclose. Absence on this page does not prove the material exists nowhere. | Source-ingest quality gates, H12/H19/H25, and detector non-promotion row; fully covered as evidence requirements. | The prior card summarized claims without an explicit omission inventory. | Preserve the omission inventory and require direct source review before any future recommendation. | pending | not started |

## Recommendations

- C01: Correct the current metric and keep commercial detector scores out of severity and authorship decisions.
- C02: Keep third-party validation indirect until the exact study is ingested separately.
- C03: Preserve multilingual figures and the non-native-English assertion only as version-unknown vendor claims; do not treat the linked-blog assertion as fairness evidence without direct review.
- C04: Keep model claims date- and version-bounded.
- C05: Do not imitate mixed-authorship span labels.
- C06: Keep AI Logic phrase/source outputs distinct from pattern validity.
- C07: Treat screenshots as illustrative product UX only.
- C08: Record product surface and access tier when citing a result; no product change.
- C09: Keep scan-credit and size marketing out of method claims.
- C10: Record the four opaque feature families and explicitly do not map them to #7, #18, #52, or a new check.
- C11: Preserve the no-score/no-authorship report contract.
- C12: Do not adopt detector-directed revise-and-rescan; retain source-fidelity gates.
- C13: Treat vendor process assertions as unverified operational claims.
- C14: Do not use training-scale or architecture wording as validity evidence.
- C15: Keep vendor statistical-pattern framing out of causal/authorship claims.
- C16: Keep plagiarism/source overlap distinct from AI evidence.
- C17: Record the education/evasion tension; no product change.
- C18: Require genre-specific evidence before generalization.
- C19: Reject `verified human-written` as established by this source.
- C20: Keep sensitivity trade-offs product/version-specific.
- C21: Keep source-code detection outside prose evidence.
- C22: Update Copyleaks-specific length caveats without transferring thresholds.
- C23: Preserve the qualified, time-sensitive Grammarly distinction only as vendor context.
- C24: Refresh living-page claims before future reliance.
- C25: Keep enterprise/security/compliance claims separate from detector validity.
- C26: Require missing method/evaluation evidence before any promotion.

## Evaluation of approved changes

- C01: not applicable - pending source-record recommendation; no product change requested.
- C02: not applicable - pending source-record recommendation; no product change requested.
- C03: not applicable - pending source-record recommendation; no product change requested.
- C04: not applicable - pending source-record recommendation; no product change requested.
- C05: not applicable - pending source-record recommendation; no product change requested.
- C06: not applicable - pending source-record recommendation; no product change requested.
- C07: not applicable - pending source-record recommendation; no product change requested.
- C08: not applicable - pending source-record recommendation; no product change requested.
- C09: not applicable - pending source-record recommendation; no product change requested.
- C10: not applicable - pending source-record recommendation; no product change requested.
- C11: not applicable - pending source-record recommendation; no product change requested.
- C12: not applicable - pending source-record recommendation; no product change requested.
- C13: not applicable - pending source-record recommendation; no product change requested.
- C14: not applicable - pending source-record recommendation; no product change requested.
- C15: not applicable - pending source-record recommendation; no product change requested.
- C16: not applicable - pending source-record recommendation; no product change requested.
- C17: not applicable - pending source-record recommendation; no product change requested.
- C18: not applicable - pending source-record recommendation; no product change requested.
- C19: not applicable - pending source-record recommendation; no product change requested.
- C20: not applicable - pending source-record recommendation; no product change requested.
- C21: not applicable - pending source-record recommendation; no product change requested.
- C22: not applicable - pending source-record recommendation; no product change requested.
- C23: not applicable - pending source-record recommendation; no product change requested.
- C24: not applicable - pending source-record recommendation; no product change requested.
- C25: not applicable - pending source-record recommendation; no product change requested.
- C26: not applicable - pending source-record recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: rereview_copyleaks_focused_final_once
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** removed the unsupported test-date assertion and limited model-v10 attribution to the sensitivity-results table; corrected AI Logic versus free-account access tiers; captured the linked-blog-only non-native-English false-positive claim and its evidence limits; corrected the source-ledger link.
- **Focused recheck:** `rereview_copyleaks_focused_final_once` verified all four remediations and returned PASS with no findings.
- **Unresolved findings:** none
