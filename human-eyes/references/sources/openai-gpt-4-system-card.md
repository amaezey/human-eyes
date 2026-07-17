# OpenAI: GPT-4 System Card

## Metadata

- **URL:** https://cdn.openai.com/papers/gpt-4-system-card.pdf
- **Author / owner:** OpenAI
- **Published:** 2023-03-14 (first canonical-PDF Internet Archive capture; the PDF has no publication-date field)
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** first-party model and system documentation
- **Evidence tier:** First-party model docs
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** current OpenAI-hosted 60-page PDF with PDF metadata CreationDate and ModDate 2024-10-16 07:50:46 AEDT, PDF SHA-256 `ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004`; Internet Archive CDX first capture timestamp `20230314165625` with later digest revisions; prior reviewed snapshot retrieved 2026-05-05 from the same canonical URL
- **Full-text status:** complete
- **Snapshot:** `snapshots/openai-gpt-4-system-card.md`
- **Extraction method:** direct PDF download with `curl`; complete text-layer extraction and structural verification with Poppler; existing Jina Reader Markdown body retained after archival; beginning, middle, Figure 11, and end rendered and visually checked
- **Snapshot SHA-256:** `4c3a576c3a7f545269868be62cd2e0c8e276cf3377ef02a05d25716a1914553d`
- **Model / corpus scope:** GPT-4 trained through August 2022; GPT-4-early instruction-following model and GPT-4-launch helpfulness/harmlessness model; mostly English and US-centric mitigation work; qualitative red teaming from August 2022, internal GPT-4-launch adversarial testing on 2023-03-10, internal factuality evaluations, 5,214 consented ChatGPT and API prompts for blinded preference comparison, safety evaluations, and cherry-picked non-zero-shot examples; custom fine-tuning and image capabilities excluded
- **Access limitations:** no substantive full-text limitation; all 60 pages, footnotes, references, figures, tables, and appendices are preserved in the authoritative PDF, while Markdown linearises multi-column layouts and records Figure 11 values separately because its raster pixels are not in the text layer; direct HTML retrieval of OpenAI's current milestone page and legacy research page returned HTTP 403, while the canonical PDF, OpenAI milestone sitemap, and Internet Archive CDX were accessible; underlying red-team transcripts, internal evaluation datasets, prompts beyond published examples, row-level factuality data, and model weights are not supplied by the report

## Summary

OpenAI's 60-page GPT-4 System Card documents GPT-4-early and GPT-4-launch safety evaluation, mitigation, deployment, and remaining limits. For human-eyes it supplies first-party, version-scoped context rather than a prose-authorship detector: next-token pretraining and RLHF can shape output behaviour; launch and early models differ; hallucinated claims may sound authoritative; hedging and refusals can create misplaced trust; and published refusal examples contain apology, identity-disclaimer, and turn-solicitation macros. Exact RBRM rubrics prescribe some refusal and regulated-advice language but selected launch outputs do not always follow those preferences. The report also offers a qualitative human-propagandist comparison, while its GPT-3 political-appeal comparison is cited-only. The examples are explicitly cherry-picked and not zero-shot, sycophancy is only a cited footnote, and the report gives no released matched human prose corpus, pattern-level human comparison, prevalence estimate, or individual-document authorship rule.

## Main insights

- GPT models are described as next-word predictors fine-tuned with demonstration and ranking data through RLHF; this is process evidence, not a causal explanation for any current surface pattern.
- The report distinguishes GPT-4-early from GPT-4-launch and says mitigations materially changed behaviour, so source-to-pattern mappings require model, date, surface, and prompt context.
- OpenAI operationalises closed-domain hallucination as adding information outside supplied context and open-domain hallucination as confidently supplying false world knowledge. GPT-4-launch improved on internal GPT-3.5 comparisons but remained unreliable.
- OpenAI links authoritative tone and accurate surrounding detail to overreliance, then warns that hedging and refusal cues do not reliably communicate model limitations and may themselves foster trust.
- The report's sycophancy note is inherited from citation [19], not measured in the system card.
- Published launch-output examples repeatedly use apology-led refusals, `I am an AI language model`, `feel free to ask`, and offers to help with another topic. The report says the examples are cherry-picked, not zero-shot, and insufficient to show breadth.
- RLHF and rule-based reward models explicitly distinguish desired and undesired refusal style, but OpenAI also reports brittleness, overrefusal, and context-dependent harm.
- Appendix rubrics prefer an apology-first `I` refusal without reasons for one class, treat additional suggestions as a partial refusal, reject missing apologies and `we` formatting in that rubric, and require lack-of-expertise disclaimers plus conditional language in regulated advice. Selected launch outputs' `feel free to ask` language creates a direct rubric/output tension, not a compliance result.
- OpenAI reports direct safety-mitigation comparisons: 82% fewer responses to disallowed requests than GPT-3.5, 29% greater policy conformity on sensitive prompts, 0.73% versus 6.48% toxic generations on RealToxicityPrompts, and roughly 60% versus 30% TruthfulQA accuracy. These are safety and factuality outcomes, not prose-pattern rates.
- Red-team results suggest GPT-4 can rival human propagandists in some domains, especially with a human editor, but hallucinations reduce reliability; GPT-4 was not a ready-made social-engineering upgrade without target knowledge, and multilingual influence findings were preliminary. The nearby GPT-3 political-appeal comparison comes from cited studies.
- The acknowledgements disclose GPT-4 use for LaTeX formatting, summarisation, and copyediting. This is direct workflow provenance, not evidence that GPT-4 wrote the report's claims.

## Evidence and claims to extract

- **Direct source reviewed:** the current complete OpenAI-hosted PDF, 60 PDF pages numbered 41-100, sections 1-6, references [1]-[106], appendices A-F, 11 figures, table examples, footnotes, and final page-100 tool-use example; authoritative PDF SHA-256 `ca3677e1b83e255aa1296d432d374378154f230f3c296b32ee67540d571b7004`.
- **Method and sample:** qualitative red teaming by more than 50 experts, iterative model and system evaluation, targeted internal quantitative safety evaluations, internal open- and closed-domain factuality evaluations, and a blinded human-preference comparison on 5,214 consented ChatGPT and API prompts. OpenAI does not release complete underlying samples or row-level results. The report focuses on GPT-4-early and GPT-4-launch, mostly English and US-centric mitigations, and excludes custom fine-tuning and image capabilities.
- **Direct versus cited evidence:** C01-C07 and C09-C17 record direct first-party descriptions, reported evaluations, examples, interpretations, limitations, or reviewer boundaries. C08 is explicitly inherited from citation [19]. C16 also separates OpenAI's direct qualitative red-team comparison from GPT-3 political-appeal findings inherited from citations [53]-[54]. No cited work is promoted through this card.
- **Important limits and counterexamples:** examples are cherry-picked and not zero-shot; one example cannot establish breadth or prevalence; mitigations remain brittle; launch outputs still show unsafe or biased failures; refusals can overreach or worsen unequal treatment; early overcaution and excessive hedging are reported; red teamers skew English-speaking and Western; multilingual mitigations were not robustly tested; factuality remained far from perfect; and the report is not comprehensive.

## Skill-use audit

- **Good use:** model/version provenance; source-grounding and factual-verification rationale; prompt- and mitigation-sensitive behaviour context; cautious evaluation of apology and refusal macros; workflow disclosure; H25 model-family/version metadata.
- **Misuse / overclaim:** treating any published output phrase as a GPT-4 or generic-AI signature; treating RLHF as a demonstrated cause of a specific writing tell; using internal safety rates as prose-pattern prevalence; treating a refusal macro or authoritative tone as authorship proof.
- **Unsupported use:** a current-model claim, surface-pattern threshold, generic model-family attribution, frequency estimate for apologies or identity disclaimers, sycophancy prevalence, released matched pattern-level human comparison, or document-level authorship decision.
- **Underused evidence:** the distinction between closed-source fabrication and open-domain falsehood, the warning that cautious tone can foster overreliance, the exact RBRM refusal and regulated-advice rubrics, their tension with selected launch outputs, the bounded human-propagandist comparison and social-engineering null, the direct mitigation rates, and the explicit GPT-4 copyediting disclosure.
- **Patterns left on the table:** apology-led guardrail language and AI-identity disclaimers remain controlled-fixture candidates near #19; the current `no-collaborative-artifacts` check recognises `feel free to` but not `My apologies` or `I am an AI language model`. The source cannot determine whether either phrase should become a rule.

## Matched patterns / rules

- H25 `Model-family versus generic-AI residue`: partly covers version, prompt, and public-tell drift; this source adds direct early-versus-launch and English/US-centric scope.
- #19 `no-collaborative-artifacts`: partly covers the published refusal examples through `feel free to`, but not apology openings or AI-identity disclaimers.
- #21 sycophancy: the live project uses stronger direct evidence from OpenAI's 2025 GPT-4o rollback; this 2023 system card only cites sycophancy in footnote 4.
- #23 `no-excessive-hedging`: adjacent only. The source reports early-model overhedging and warns that cautious tone can foster trust, but gives no measured output-frequency phrase inventory or threshold; appendices separately prescribe conditional language in a regulated-advice classifier rubric.
- #41 `genre_specific` academic and journalism source verification plus `human-eyes/references/process.md`: partly cover unsupported or untraceable claims and closed-source preservation; they do not assess model factuality.
- `pattern-opportunities.md` apology and guardrail-macro candidate near #19: this source adds first-party rubrics and examples but no output prevalence or released matched human control.
- Product boundary: human-eyes surfaces prose and evidence problems; it does not infer authorship. This source supplies no basis to change that boundary.

## Associated hypotheses

- H25: Model-family versus generic-AI residue.
- H3: Drop detection framing entirely, supported only at the epistemic-boundary level by the absence of an authorship design.
- H12: Genre-aware threshold calibration, adjacent through context-dependent refusals and English/US-centric evaluation limits.

## Questions / follow-up

- Would controlled, model-versioned, matched human and model output fixtures show that apology-led refusals or AI-identity disclaimers add useful coverage beyond `feel free to` without creating quotation, policy, or support-context false positives?
- Can an official version history identify the substantive differences among the canonical PDF's archived 2023 bytes and the current PDF whose metadata dates to 2024?
- No product change is requested or approved; all recommendations remain pending for Mae.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/openai-gpt-4-system-card/2026-05-05-507b0954.md` | 2026-05-05 | `507b0954c7805f1ae876e02137fa574fbaf8f3deef344d63b284bd6c777f64b0` |
| current | none found | `snapshots/openai-gpt-4-system-card.md` | 2026-07-17 | `4c3a576c3a7f545269868be62cd2e0c8e276cf3377ef02a05d25716a1914553d` |

## Decision history

- The 2026-05-05 card had no claim IDs, user decisions, implementation statuses, snapshot digest, update provenance, or independent source-record review. Its H3, #21, and model-version notes are reopened and qualified here. No prior approved or implemented product decision exists.
- The prior snapshot contained the complete 60-page source body but did not follow `SNAPSHOT_TEMPLATE.md`. No digest was recorded in the card or four-column manifest, so its on-disk SHA-256 was computed before replacement and the exact bytes were archived. The refreshed snapshot retains the source body, adds current provenance and extraction verification, and preserves the authoritative PDF.

## Project coverage

This is the authoritative review table. Every recommendation remains a pending decision for Mae; no product change was made.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: OpenAI describes GPT models as first trained for next-word prediction on internet text and then fine-tuned with demonstrations, rankings, and RLHF to prefer human-labelled outputs. | Direct first-party process description; high level, no released training corpus or causal test connecting the pipeline to a surface writing pattern. | partly covered by H25 and source metadata conventions; no checker should encode a training-mechanism inference. | The prior card risked letting process context stand in for pattern evidence. | Record process context only; do not infer a surface tell or authorship rule. | pending | not started |
| C02: The report separates GPT-4-early from GPT-4-launch and says safety mitigations made launch behaviour substantially different and generally safer. | Direct version-scoped comparison across safety evaluations and examples; not a prose-style comparison and not current-model evidence. | fully covered by H25's model-family/version boundary and the card's metadata. | Existing H25 remains open and no runtime finding carries source-version metadata. | Retain this as H25 provenance evidence; take no checker action. | pending | not started |
| C03: The system card combines expert qualitative red teaming with targeted internal quantitative evaluations, but its published examples are not zero-shot, are cherry-picked, and one example cannot show breadth. | Direct method and explicit limitation; underlying full prompts, transcripts, evaluation sets, and row-level data are not released. | fully covered by source-ingest evidence boundaries and the project's no-single-example authorship stance. | Any phrase promotion from an appendix example would exceed the source without controlled replication. | Require model-versioned matched fixtures before considering an example-derived pattern. | pending | not started |
| C04: Red teamers were selected for risk expertise and skewed toward highly educated, English-speaking Western participants; mitigations were mostly designed and tested in English with a US-centric viewpoint and were not robustly tested for multilingual performance. | Direct sampling and scope limitation; no population weighting or multilingual outcome table establishes the size of transfer errors. | partly covered by H12 genre calibration and H25 metadata; language and evaluator provenance are not attached to live surface findings. | Generic GPT-4 or cross-language claims would erase the stated evaluation boundary. | Keep all mappings English-, US-, model-, and date-scoped; take no product action. | pending | not started |
| C05: OpenAI distinguishes closed-domain additions outside supplied context from open-domain confidently false world claims; GPT-4-launch scored 19 points above its latest GPT-3.5 model on internal open-domain avoidance and 29 points above it on closed-domain avoidance, yet remained fallible. | Direct operational definitions and reported internal evaluation results; automatic GPT-4 classification and human evaluation were used, but sample sizes and row-level results are not published here. | partly covered by #41 source verification and the rewrite process's closed factual record; neither is a model-factuality evaluation. | Live prose review does not explicitly distinguish unsupported additions to a supplied source from false open-world claims. | Preserve the distinction as source-grounding rationale; evaluate any guidance change separately before implementation. | pending | not started |
| C06: GPT-4 can make up facts, double down, and sound more convincing through authoritative tone or accurate surrounding detail, increasing overreliance risk. | Direct first-party observed limitation and author interpretation; no prose-span threshold or human-style comparison. | partly covered by #41 checks for unsupported and untraceable claims; tone alone is not a live factuality rule. | Authoritative tone must not be converted into authorship or truth probability. | Record as rationale for evidence verification, never as a standalone surface finding. | pending | not started |
| C07: OpenAI reports that GPT-4 still hedges, early studies suggest cautious tone may foster trust, and hedging or refusal cues may be ignored or misread; GPT-4-early also overrefused and hedged excessively. | Direct report of qualitative observations and early studies, but no sample size, effect estimate, measured output-frequency phrase inventory, or published comparison is provided. Separate appendix rubrics prescribe conditional language for regulated advice. | challenges current behaviour: #23 `no-excessive-hedging` treats stacked evasive hedges as a style problem, while process guidance preserves evidence-based qualification; #41 regulated-advice handling is not a factual-calibration check. | The project distinguishes excessive from legitimate hedging but does not state that prescribed caution is not calibrated truthfulness. | Add no pattern; consider a future explanation-honesty test that separates epistemic qualification from unsupported confidence cues and evaluates the appendix's regulated-advice rubric. | pending | not started |
| C08: Footnote 4 defines sycophancy as repeating a dialogue user's preferred answer and says it can worsen with scale. | Indirect claim attributed to citation [19]; the system card supplies no sycophancy experiment, output sample, rate, or human comparator for that behaviour. | fully covered by #21's stronger direct 2025 OpenAI rollback evidence; no need to use this inherited statement as pattern support. | The prior card treated this as a source insight without marking it cited-only. | Keep C08 indirect and take no further action. | pending | not started |
| C09: Published GPT-4-launch examples repeatedly include apology-led refusals, `I am an AI language model`, `feel free to ask`, and offers to help with another topic. | Direct output examples, but deliberately selected, non-zero-shot, safety-prompt-specific, and insufficient for prevalence or generic attribution. | partly covered by #19 `no-collaborative-artifacts`, whose implementation catches `feel free to` but not apology openings or AI-identity disclaimers; the pending guardrail-macro opportunity is adjacent. | No controlled legitimate-use, quotation, policy, support, or matched-human controls establish a safe rule. | Evaluate apology and identity-disclaimer candidates with controlled fixtures; do not change #19 from these examples alone. | pending | not started |
| C10: Refusal training can reduce unsafe outputs but also overrefuse, behave inconsistently, exacerbate bias, or mis-handle context; the same words can be harmful in one genre and legitimate in another. | Direct first-party limitations and contextual examples; not a prose-authorship study. | partly covered by #41 genre-specific review and general context controls. | A bare lexical refusal rule could misclassify quoted, fictional, safety, or support prose. | Require genre, quotation, and deliberate-use controls in any future guardrail-macro evaluation. | pending | not started |
| C11: OpenAI used human demonstrations, rankings, and RBRMs with exact classifier rubrics: one desired refusal class starts with an `I` apology and inability statement without reasons, additional suggestions count as a partial refusal, and missing apology or `we` formatting is undesired; a regulated-advice rubric requires lack-of-expertise disclaimers, conditional language, and professional consultation while rejecting definitive orders. | Direct first-party classifier and training instructions plus example classifications; not production system prompts and not evidence of output compliance, prevalence, causality, or transfer to current models. Selected launch outputs still include `feel free to ask`, demonstrating rubric/output tension rather than compliance. | partly covered: #19 catches `feel free to` but not apology or AI-identity wording; #23 assesses excessive hedging but not prescribed conditional language; #41 checks genre evidence and claims, not regulated-advice safety; `process.md` preserves grounded qualification but supplies no refusal-style policy; H25 covers version scope. | `pattern-opportunities.md` currently groups this card with prompt archives and does not preserve the exact rubric/output tension. A lexical expansion without quotation, policy, support, and genre controls could create false positives. | Correct the shared opportunity wording and evaluate rubric-derived apology, identity, and conditional-language candidates with controlled fixtures before any product change. | pending | not started |
| C12: On 5,214 consented ChatGPT and API prompts, blinded labelers preferred GPT-4-launch to GPT-3.5 RLHF on 70.2% and GPT-3.5 Turbo RLHF on 61.1%; Figure 11 records all pairwise win rates. | Direct reported human-preference evaluation with sample size and blinding description; the report does not provide prompt distribution, uncertainty, row-level data, or a writing-pattern outcome. | not covered by a prose check and not needed for one. | Preference and instruction following must not be relabelled as prose quality, safety, or pattern compliance. | Record only; take no product action. | pending | not started |
| C13: OpenAI discloses that GPT-4 helped iterate LaTeX formatting, summarise text, and copyedit the system card. | Direct workflow disclosure in acknowledgements; the report does not identify affected spans or say GPT-4 authored its findings. | partly covered by source provenance conventions; no checker should infer report authorship from this disclosure. | The prior card omitted this source-specific provenance example. | Record the disclosure and preserve the direct boundary; take no product action. | pending | not started |
| C14: The report is not comprehensive, excludes custom fine-tuning and image capabilities, focuses on two model versions, and says mitigations remain brittle. | Direct explicit scope and limitation statements. | fully covered by the card metadata and source-ingest completeness boundary. | Generic claims about all GPT-4 uses, multimodal outputs, custom models, or later models remain unsupported. | Keep every recommendation within the reviewed versions and textual system-card scope. | pending | not started |
| C15: The system card supplies no released matched human prose corpus, pattern-level human comparison, phrase prevalence, stylistic threshold, causal surface-pattern test, or individual-document authorship evaluation. | Direct design boundary plus reviewer synthesis; published outputs are safety examples, not representative prose samples. C16 preserves the report's separate qualitative human-propagandist comparison without turning it into pattern evidence. | fully covered by the project's no-authorship product boundary and H3's epistemic concern. | The previous broad #21 and prompt-evidence mapping could overstate what this source proves. | Use this card for context and provenance only unless a separately reviewed matched-output study supplies direct pattern evidence. | pending | not started |
| C16: OpenAI's red-team results suggest GPT-4 can rival human propagandists in many domains, especially with a human editor, but hallucinations reduce reliability; GPT-4 was not a ready-made social-engineering upgrade without target knowledge, and multilingual influence results remained preliminary. The nearby claim that GPT-3 political appeals were nearly as effective as human appeals comes from citations [53]-[54]. | The propagandist comparison and task-specific nulls are direct qualitative first-party red-team reports without released matched text, rates, or coding. The GPT-3 human comparison is indirect and unresolved here. | not covered by a prose-pattern check; H12 and H25 are adjacent scope controls, while #41 source verification addresses claims rather than persuasion efficacy. | A broad human-writing or persuasion claim would collapse direct qualitative findings, cited GPT-3 studies, model versions, editor involvement, reliability limits, and task-specific nulls. | Record the bounded direct and cited claims separately; take no pattern or authorship action without direct matched-output review. | pending | not started |
| C17: OpenAI reports 82% fewer responses to disallowed requests than GPT-3.5, 29% greater policy conformity on sensitive requests, 0.73% versus 6.48% toxic generations on RealToxicityPrompts, and roughly 60% versus 30% TruthfulQA accuracy after hallucination mitigations. | Direct first-party reported safety and factuality results. RealToxicityPrompts contains 100,000 web snippets, but the report does not supply the other evaluation sample sizes, uncertainty, row-level data, full prompts, or complete model-build identifiers. | not covered by a prose-pattern check and not needed for one; C05 separately records internal open- and closed-domain hallucination point differences. | These rates measure safety or factuality outcomes, not refusal-macro prevalence, prose quality, human likeness, or authorship. | Record the metrics with their dataset and disclosure limits; take no prose-pattern action. | pending | not started |

## Recommendations

- C01: Record the training pipeline as context only.
- C02: Retain model/version provenance under H25.
- C03: Require controlled replication before promoting selected examples.
- C04: Keep claims English-, US-, model-, and date-scoped.
- C05: Preserve the closed- versus open-domain source-grounding distinction without changing the product.
- C06: Use authoritative-tone risk only as factual-verification rationale.
- C07: Evaluate explanation honesty and the regulated-advice conditional-language rubric separately from stylistic hedge removal before any guidance change.
- C08: Keep sycophancy indirect here and rely on separately reviewed direct evidence.
- C09: Test apology and AI-identity refusal macros with controlled fixtures before any #19 change.
- C10: Require genre, quotation, and deliberate-use controls in that evaluation.
- C11: Correct the shared opportunity wording to distinguish this system card from a prompt archive, then evaluate rubric-derived candidates with controlled fixtures before any product change.
- C12: Record preference results only.
- C13: Record the GPT-4 workflow disclosure only.
- C14: Preserve the report's version and capability exclusions.
- C15: Keep the source out of pattern and authorship claims without separate matched-output evidence.
- C16: Keep direct qualitative red-team findings, task nulls, and cited GPT-3 human comparisons separate.
- C17: Record safety and factuality metrics without converting them into prose-pattern evidence.

## Evaluation of approved changes

- C01: not applicable - pending source-record recommendation; no product change implemented.
- C02: not applicable - pending source-record recommendation; no product change implemented.
- C03: not applicable - pending source-record recommendation; no product change implemented.
- C04: not applicable - pending source-record recommendation; no product change implemented.
- C05: not applicable - pending source-record recommendation; no product change implemented.
- C06: not applicable - pending source-record recommendation; no product change implemented.
- C07: not applicable - pending source-record recommendation; no product change implemented.
- C08: not applicable - pending source-record recommendation; no product change implemented.
- C09: not applicable - pending source-record recommendation; no product change implemented.
- C10: not applicable - pending source-record recommendation; no product change implemented.
- C11: not applicable - pending source-record recommendation; no product change implemented.
- C12: not applicable - pending source-record recommendation; no product change implemented.
- C13: not applicable - pending source-record recommendation; no product change implemented.
- C14: not applicable - pending source-record recommendation; no product change implemented.
- C15: not applicable - pending source-record recommendation; no product change implemented.
- C16: not applicable - pending source-record recommendation; no product change implemented.
- C17: not applicable - pending source-record recommendation; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/openai_gpt4_system_card_reviewer`; full five-lens review followed by focused re-check of materially changed claims, provenance, coverage, recommendations, and statuses
- **Findings resolved:** five initial findings covering omitted direct and cited human comparisons plus social-engineering and multilingual nulls; omitted exact refusal and regulated-advice rubrics plus rubric/output tension; omitted safety and factuality metrics; incomplete alternate-route and revision provenance; and noncanonical C07 coverage wording; focused re-check found zero residual findings
- **Unresolved findings:** none
