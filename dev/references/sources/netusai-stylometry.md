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

## Skill-use audit

- **Good use:** Vendor-language context for candidate feature families, detector-score caution, false-positive UX, and project tests that ask whether a coarse metric behaves consistently across genre, length, editing, and language background.
- **Misuse / overclaim:** Treating `12-18` words, `30%` transition replacement, `78%` same-length sentences, `4%` or `8-12%` idiom density, `87%` ZeroGPT output, `500+` markers, or the low-perplexity formula as validated thresholds or transferable detector logic.
- **Unsupported use:** Inferring AI authorship, proving a model family, penalising polished or non-native English, adding invented detail, setting human-eyes severity, or rewriting solely to obtain a commercial detector label.
- **Underused evidence:** The source's own admissions about technical/academic low perplexity, human false positives, classification uncertainty, and template/genre confounds are more useful than its cue list.
- **Patterns left on the table:** Passive-voice frequency, clause-order persistence after synonym swaps, exact transition phrases, and image-only `add verbs` wording remain unvalidated research candidates; the `68%` image claim lacks a visible citation and should not be promoted.

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

## Questions / follow-up

- Directly review the linked sources before using their measurements or mechanisms; this source alone cannot validate them.
- If Mae wants to revisit any candidate, use matched human/AI controls across academic, technical, marketing, ESL, edited, and template-driven prose rather than commercial detector labels.
- Determine whether the source's passive-voice and clause-order claims add anything after stronger academic stylometry sources are compared; no product change is requested here.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/netusai-stylometry/2026-05-05-dd9733d3.md` | 2026-05-05 | `dd9733d3760dd873ae408ac92707a0e5396100fd3641bb16bc088c16cce430ee` |
| current | none found | `snapshots/netusai-stylometry.md` | 2026-07-16 | `bee99e0f7bb74381d2060df36ef27512488210d75e87107f62d4be23bd550f24` |

The prior card and manifest recorded no SHA-256 or stable revision identifier. The prior snapshot's exact bytes were hashed before archive, and the archive digest above matches those bytes. The source metadata's `dateModified` predates the prior retrieval, and normalized comparison found the same article answers; the material additions are preservation repairs: all eight FAQ question prompts, the feature image, full-resolution copies and transcriptions of all source images, current provenance, and the restored tactics table structure. Formatting normalization and link syntax also changed.

## Decision history

- The prior record contained no claim IDs, user decisions, or implementation statuses. It mapped the source generally to G9, B5, G6, and H8. This update retains only qualified G9/B5/G6 mappings. The H8 mapping is retired because live H8 is placeholder residue, not grammar cleanliness. All C01-C27 recommendations are newly formalized as `pending` / `not started`; no prior approval or implementation is inferred.

## Project coverage

This is the authoritative review table. The focused deterministic evidence is from `python3 human-eyes/scripts/grade.py audit ... --surface-only --format json`; it establishes surface coverage only, not a complete human-eyes Audit or source validity.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Stylometry quantifies how a text is written rather than its meaning, using word choice, rhythm, punctuation, and structure. | Direct vendor explanation; standard framing but no method or cited primary study established here. | Project product boundary and G9/B5/G6 cover parts; partly covered. | No unified stylometry model; no need to imply one. | Record as vendor framing only; require direct academic support for mechanism claims. | pending | not started |
| C02: Writing and named AI models have identifiable fingerprints across `500+` markers that humans rarely replicate. | Direct article and image assertion; no feature list, dataset, model version, validation, or human baseline. | H25 `Model-family versus generic-AI residue` is the only adjacent inspected artifact; not covered as a generic claim. | Closed-set attribution is not generic authorship proof. | Do not adopt the number or generic fingerprint claim; retain as unsupported vendor wording. | pending | not started |
| C03: Human rhythm mixes short and complex sentences; uniform 12-18-word sentences are an AI red flag. | Direct vendor assertion plus invented examples; linked burstiness page is indirect; no counts or comparison. | G9 computes SD and passed the full article at 11.6; H13/H22 are open; partly covered. | Source band and project SD threshold are both unvalidated by this page; genre and length controls matter. | Test-adapt only through matched, genre-aware evaluation of G9/H13/H22; do not adopt 12-18 as a threshold. | pending | not started |
| C04: `Lexical density` includes filler frequency, rare/common vocabulary, pronouns, passive voice, formal diction, and colloquial spikes. | Direct taxonomy with a linked definition; terminology combines distinct measures and supplies no results. | B1 and B5 cover stock vocabulary and TTR; H23/H24 cover grammar and register; partly covered. | Pronoun/passive features absent; B5 direction already faces stronger contradictory evidence. | Keep as candidate taxonomy only; compare with academic sources before any B5, H23, or H24 test. | pending | not started |
| C05: Comma/dash/semicolon ratios, paragraph openers, bullet uniformity, pauses, dashes, and fragments distinguish styles. | Direct vendor list; no weights, thresholds, examples of ratios, or human controls. | G6, G3, G4, C7, E5, and E8 cover narrower constructions; partly covered. | The source praises punctuation that live checks can flag and equates identical formatting with machine output. | Test only exact, separately defined features with deliberate-use and genre controls; do not treat punctuation as authorship proof. | pending | not started |
| C06: AI overuses `Therefore`, `Additionally`, and `In conclusion`. | Direct vendor phrase assertion; no frequency data. | E8 recognises paragraph-opening `Therefore` and `Additionally`; G8 recognises line-opening `In conclusion`. | The three forms route through two existing position-sensitive mechanisms. | Add the missing exact `Therefore` opener to E8 and retain the existing routes for the other two. | approved | implemented |
| C07: High perplexity is human-like and low perplexity is AI-like. | Direct explanation with invented examples; no model, tokenizer, score, distribution, or threshold. | No live perplexity check; the `pattern-opportunities.md` do-not-promote row for product detector scores explicitly includes NetusAI and GPTZero perplexity; not covered. | Project intentionally avoids opaque detector-style authorship scoring. | Do not add a perplexity rule from this source. | pending | not started |
| C08: `Low Perplexity + Low Stylometric Variance = AI-Generated`, and hybrid models outperform perplexity alone. | Direct vendor formula and interpretation; no experiment or performance result. | Product boundary and pattern-opportunities non-promotion oppose detector-score transfer; not covered. | Formula lacks calibration, uncertainty, detector versions, and validation. | Do not adopt as a score, rule, severity, or report verdict. | pending | not started |
| C09: Perplexity alone fails for Claude 3 Opus and technical/academic writing. | Direct qualification; model/version named only for one example and no evidence shown. | H9/H12 and genre controls address look-alikes; partly covered as caution. | No observed failure rate or direct technical/academic sample. | Record as a false-positive/evaluation control, not model performance evidence. | pending | not started |
| C10: Human writing can share AI-like patterns and receive false positives. | Direct vendor caveat; no rate on the page. | Product boundary, process, and pattern-opportunities already require non-authorship wording; fully covered as policy. | Source adds no validated threshold or subgroup estimate. | Retain existing caveat language; no further product action from this source. | pending | not started |
| C11: Heavy grammar-tool editing erases contractions, idioms, and rhythm; a supplied rewrite scored 87% AI in ZeroGPT. | Direct anecdote and reported product output; test text, date, settings, and repeatability are incomplete. | No grammar-cleanliness rule; H8 is unrelated placeholder residue; not covered. | Score is opaque and the causal `Grammarly Effect` is untested. | Do not promote the causal or numeric claim; use only as a candidate edited-text control. | pending | not started |
| C12: Non-native English can be misread because formulaic syntax and limited slang fall outside a native-English baseline. | Direct vendor interpretation with an indirect ResearchGate link that does not establish detector bias here. | H9 `similar-species disambiguation`, H12 `genre-aware threshold calibration`, and the `pattern-opportunities.md` detector-output caveat row provide adjacent caution only; partly covered. | This page provides no language groups, detector data, or fairness analysis. | Record as a subgroup-harm prompt; rely on directly reviewed bias research for project guidance. | pending | not started |
| C13: Academic, marketing, listicle, product, and other template-driven genres risk flags through repeated structure, transitions, passive voice, and low lexical diversity. | Direct vendor assertion with a linked persona PDF for low diversity; no tested samples. | G3/G6/G9/B5 and H12 are adjacent; partly covered. | Live G6 only finds repeated exact labels; G3 measures list density, not uniformity. | Test-adapt only as genre-aware evaluation controls; do not add a generic template verdict. | pending | not started |
| C14: Vary sentence length and replace 30% of transitions to humanize text. | Direct prescriptive advice; `30%` is unsupported and examples are invented. | G9 and process guidance address rhythm while preserving meaning; partly covered. | No evidence that the percentage improves writing or detector validity. | Retain only ordinary rhythm editing where meaning and genre support it; reject the numeric quota. | pending | not started |
| C15: Inject contractions, fragments, ellipses, and em dashes as controlled flaws. | Direct evasion advice; no outcome data and no quality controls. | Directly challenges `no-em-dashes` (C7), `no-staccato-sequences` (E5), and `process.md` source-preservation guidance; contractions and ellipses have no equivalent live check. | Deliberately adding errors or mannerisms can damage prose and game detectors. | Do not adopt detector-evasion flaws; preserve deliberate source style only under existing process rules. | pending | not started |
| C16: Replace generic examples with hyper-specific details such as a named study and sample size. | Direct prescriptive example; the page does not source the example. | `faux_specificity` and closed-source process guard against invented detail; challenges current behaviour. | Adding unsupported facts violates factual fidelity. | Do not adopt invented specificity; require source-grounded detail. | pending | not started |
| C17: Break template structures by mixing bullets, arrows, bold headers, and one-line paragraphs. | Direct prescriptive evasion advice; no usability or genre test. | Directly challenges `no-unicode-flair` (G4) and `no-boldface-overuse`; `no-excessive-lists` (G3) is adjacent but measures density, while the full-article surface run left `no-inline-header-lists` clear. | One-line-paragraph variety has no equivalent live check; formatting changes can harm readability. | Do not adopt detector-directed decorative variation; preserve functional structure. | pending | not started |
| C18: Burstiness feels conversational, specificity signals expertise, and format variety implies original thinking or unconscious trust. | Direct author interpretation; no reader study or measurement. | No direct project check; not covered. | Conflates surface style with expertise, originality, and trust. | Do not promote as evidence or rewriting guidance. | pending | not started |
| C19: NetusAI reports risk zones, a voice-retention score, `4%` versus `8-12%` idiom density, minimal edits, meaning preservation, version selectors, and a highest-stealth recommendation to pass both V1 and V2 detectors. | Direct product-marketing claims and illustrative UI language; no method or audit. | No commercial-detector integration; not covered. | Metrics, ideal range, version behavior, highlighting accuracy, preservation, and dual-detector stealth are opaque. | Do not use product labels, versions, or ranges as project thresholds; independent testing would be separate work. | pending | not started |
| C20: A rapid detect-rewrite-retest loop can move blocks to `Human` and is essential for publishing; the UI distinguishes bypassing detection from ordinary paraphrasing. | Direct product workflow claim; no false-negative, quality, or preservation evaluation. | Directly challenges the complete-Audit, factual-fidelity, and non-authorship workflow in `process.md`. | Optimizing to one or two opaque detector labels can remove valid style or add unsupported content; the product distinction does not validate either route. | Do not adopt detector-directed rewriting; keep project validation source-bound and pattern-specific. | pending | not started |
| C21: Stylometry and detectors target patterns, not ideas, accuracy, or prose quality; clean writing can increase false positives. | Direct article conclusion; no quantitative support, but explicit boundary and caveat. | Product boundary and report/process wording fully cover non-authorship and factual-separation principles. | `Clean writing` remains undefined and should not become a cue. | Retain the boundary and caveat only; no new check. | pending | not started |
| C22: Academic authorship models identify among small groups, while commercial detectors estimate human-versus-AI probability rather than definitive identity. | Direct FAQ distinction; no specific academic model or detector evidence reviewed here. | Product boundary aligns; fully covered as a conceptual caution. | Closed-set, open-set, probability calibration, and product thresholds remain unspecified. | Record as vendor caution; rely on direct academic sources for technical claims. | pending | not started |
| C23: Synonym swaps do not remove rhythm, clause order, or passive-voice frequency. | Direct FAQ claim without examples or test. | Synonym cycling has no live record: former #11 was removed 2026-07-25 through DR-156. Process says lexical substitution is limited; partly covered. | Clause order and passive frequency are not measured live. | Take no further product action; use as a research prompt only if stronger sources support it. | pending | not started |
| C24: Higher ChatGPT temperature adds randomness but not enough structural change and can reduce coherence. | Direct FAQ claim; no model version, temperature values, prompts, or runs. | H25 tracks model/version evidence; otherwise not covered. | High drift and no direct experiment. | Do not promote; require versioned controlled evidence. | pending | not started |
| C25: Highly structured formats, academic essays, listicles, product descriptions, and grammar-polished long guides are most vulnerable. | Direct FAQ ranking without rates or comparison. | H12 and context gates partly cover genre variation. | `Most vulnerable` is unsupported and product-specific. | Use as a candidate sampling frame, not a ranking or user verdict. | pending | not started |
| C26: Images add claims that detectors flag `add verbs`, dashes and pauses are human, AI patterns are absent in humans, and 68% distrust AI labels on human work. | Direct image-only assertions; `68%` has no visible source and `add verbs` may be a source typo; some claims are categorical. | C7 and non-authorship guidance challenge the categorical punctuation/authorship framing; not covered otherwise. | No cited study, sample, or definitions; image claims conflict with body qualifications. | Do not promote any image-only metric or categorical claim; preserve for fidelity and counterevidence. | pending | not started |
| C27: AI labels immediately cost credibility, organic traffic, and authority. | Direct opening harm claim; no cases, measurements, causal design, or platform scope. | No prose-pattern coverage; not covered. | Business and audience effects are asserted rather than demonstrated. | Record only as vendor framing; do not use for severity or consequences. | pending | not started |

## Recommendations

- C01: Record as vendor framing only; require direct academic support for mechanisms.
- C02: Do not adopt `500+` or generic fingerprint claims.
- C03: Test-adapt G9/H13/H22 only with matched, genre-aware data.
- C04: Keep as a candidate taxonomy pending academic comparison.
- C05: Test exact punctuation and structure features separately with controls.
- C06: Add paragraph-opening `Therefore` to E8 and retain the existing `Additionally` and `In conclusion` routes.
- C07: Do not add a perplexity rule.
- C08: Do not adopt the hybrid verdict formula.
- C09: Record legitimate low-perplexity genres and dated model output as controls.
- C10: Retain existing false-positive caveat; no further action.
- C11: Do not promote the `Grammarly Effect` or 87% score.
- C12: Use directly reviewed bias research, not this page, for subgroup guidance.
- C13: Test template claims only within genre-aware evaluation.
- C14: Reject the 30% quota; preserve source-bound rhythm editing.
- C15: Do not inject flaws for detector evasion.
- C16: Do not add unsupported specificity.
- C17: Do not vary formatting solely to change a detector score.
- C18: Do not promote trust, expertise, or originality interpretations.
- C19: Do not use NetusAI metrics as project thresholds.
- C20: Do not adopt detector-directed rewriting.
- C21: Retain the patterns-versus-authorship and factual-accuracy boundary.
- C22: Record the classification-versus-identification distinction with academic support required for technical use.
- C23: Take no further action beyond existing anti-substitution process guidance.
- C24: Do not promote the temperature claim.
- C25: Use named genres only as candidate evaluation strata.
- C26: Do not promote image-only metrics or categorical claims.
- C27: Record business-harm language only as vendor framing.

## Evaluation of approved changes

- C06: passed - DR-16A asserts that paragraph-opening `Therefore` fails E8; `Additionally` and `In conclusion` retain their existing E8/G8 coverage.
- C01-C05 and C07-C27: not applicable - recommendations remain pending and no product changes were requested or made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/netusai_reviewer`; focused re-check by the same reviewer after material fixes
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** Four material findings resolved: completed the UI-image transcription and related C19/C20 claims; corrected linked-evidence directness; removed unsupported curly-typography and parenthetical-heading attribution; replaced generic coverage references with exact inspected artifacts and checks. Focused re-check found zero residual findings.
- **Unresolved findings:** none
