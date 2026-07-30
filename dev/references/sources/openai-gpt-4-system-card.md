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

## Matched patterns / rules

- H25 `Model-family versus generic-AI residue`: partly covers version, prompt, and public-tell drift; this source adds direct early-versus-launch and English/US-centric scope.
- D1 `no-collaborative-artifacts`: partly covers the published refusal examples through `feel free to`, but not apology openings or AI-identity disclaimers.
- D3 sycophancy: the live project uses stronger direct evidence from OpenAI's 2025 GPT-4o rollback; this 2023 system card only cites sycophancy in footnote 4.
- E2 `no-excessive-hedging`: adjacent only. The source reports early-model overhedging and warns that cautious tone can foster trust, but gives no measured output-frequency phrase inventory or threshold; appendices separately prescribe conditional language in a regulated-advice classifier rubric.
- H10 `genre_specific` academic and journalism source verification plus `human-eyes/references/process.md`: partly cover unsupported or untraceable claims and closed-source preservation; they do not assess model factuality.
- `pattern-opportunities.md` apology and guardrail-macro candidate near D1: this source adds first-party rubrics and examples but no output prevalence or released matched human control.
- Product boundary: human-eyes surfaces prose and evidence problems; it does not infer authorship. This source supplies no basis to change that boundary.

## Associated hypotheses

- H25: Model-family versus generic-AI residue.
- H3: Drop detection framing entirely, supported only at the epistemic-boundary level by the absence of an authorship design.
- H12: Genre-aware threshold calibration, adjacent through context-dependent refusals and English/US-centric evaluation limits.
