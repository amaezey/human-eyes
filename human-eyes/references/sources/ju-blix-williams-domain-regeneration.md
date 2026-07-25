# Ju, Blix, and Williams: Domain Regeneration

## Metadata

- **URL:** https://aclanthology.org/2025.findings-acl.120/
- **Author / owner:** Da Ju, Hagen Blix, and Adina Williams
- **Published:** 2025-07
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed conference paper
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** ACL Anthology ID 2025.findings-acl.120; DOI 10.18653/v1/2025.findings-acl.120; arXiv:2505.07784v2
- **Version / revision:** current authoritative 22-page ACL 2025 proceedings PDF; prior 2026-05-05 ACL landing-page/Jina capture
- **Full-text status:** complete
- **Snapshot:** `snapshots/ju-blix-williams-domain-regeneration.md`
- **Extraction method:** official ACL PDF downloaded with `curl`; all 22 pages converted from the embedded text layer with Poppler `pdftotext -layout`; PDF metadata and image inventory inspected with `pdfinfo` and `pdfimages -list`; pages 1, 5-8, 11, and 22 rendered with `pdftoppm` and visually compared; ACL HTML, arXiv API metadata, and the arXiv v2 PDF cross-checked
- **Snapshot SHA-256:** `33b381404724efb7515ef94c6409fd7eff0c85a101828fac011d261b9410566f`
- **Model / corpus scope:** English Wikipedia, CCNews, and ELI5; about 6.4M, 0.6M, and 0.6M human articles respectively in the parse-depth descriptive table; main Llama-2-70B-Instruct regenerations plus Llama-3.3-70B-Instruct, Llama-3.1-8B-Instruct, Mistral-Small-24B-Instruct-2501, and Ministral-8B-Instruct-2410 comparisons; first 256 Wikipedia words, first 180 CCNews words, or ELI5 title supplied to vLLM at default temperature 1.0
- **Access limitations:** none for the paper. The authoritative ACL PDF and arXiv v2 PDF are preserved. The ACL landing-page abstract and arXiv API summary still describe two domains, while both full PDFs describe and evaluate three domains including ELI5. Plot pixels remain in the preserved PDFs; captions, embedded labels, tables, prompts, examples, appendices, and all page text are in the snapshot.

## Summary

This peer-reviewed ACL paper introduces domain regeneration: models continue the beginning of a human-domain document, allowing large human and regenerated corpora to be compared while partly controlling topic and content. Across English Wikipedia, CCNews, and ELI5, the authors measure sentence length, article readability, unique dependency tags, constituency-tree depth, Yngve score, and unique constituency labels. The most stable direct result is distributional rather than lexical: regenerated text is usually less variable and has a reduced right tail, while mean direction depends on domain, metric, and sometimes model. The paper also gives qualitative Llama-2 examples of American spelling normalization, Wikipedia value judgments, factual errors, invented quotations and acronyms in news, and essay-like or promotional endings. These observations are model-, prompt-, language-, domain-, and date-bound; they do not validate a single-document authorship rule.

## Main insights

- Regenerated distributions usually narrow and lose part of the human right tail, but neither effect is universal: ELI5 parse depth is the explicit no-narrowing result, and dependency-tag distributions have no human long tail to reduce.
- Means do not move in one generic AI direction. Llama outputs tend to increase complexity means for Wikipedia and CCNews but match or reduce them for ELI5; some model-specific exceptions occur.
- The authors interpret the mean pattern as domain-complexity overshoot, not collapse to a neutral middle. This is an interpretation of measured distributions, not a directly tested training mechanism.
- Sentence length, readability, dependency-tag count, parse depth, Yngve score, and constituency-label count are separate metrics. The paper does not reduce its result to sentence-length standard deviation.
- The full paper adds ELI5, multiple Llama and Mistral variants, cleaning ablations, prompts, exact descriptive tables, nulls, limitations, and qualitative examples omitted by the prior abstract-only record.
- Qualitative examples show Americanization of British spelling, Wikipedia neutrality failures, factual mistakes, invented quotations and acronyms, explicit `In conclusion` wrap-ups, praise, sales copy, and reader address. These are manual observations, not prevalence estimates.
- The default decoding temperature was 1.0. Effects of other temperatures, including effects on the long tail, were not tested.
- Tooling and parsing can fail on extreme or malformed text. Uniform application may limit bias, but the paper does not quantify residual measurement error.
- The paper suggests possible synthetic-text detection use, but it does not train or evaluate a detector, choose thresholds, report document-level classification accuracy, or establish authorship.
- The current ACL and arXiv metadata abstracts are stale relative to their own PDFs: metadata says two domains; the PDFs say and evaluate three.
- Appendix I adds an anecdotal comparison: human CCNews examples appeared less similar to Llama continuations than the two Llama generations appeared to each other. This is illustrative, not a measured similarity result.

## Evidence and claims to extract

- **Direct source reviewed:** authoritative ACL proceedings PDF for 2025.findings-acl.120, 22 pages, printed pages 2367-2388; compared with the 22-page arXiv:2505.07784v2 PDF and current first-party metadata.
- **Method and sample:** observational corpus analysis of English Wikipedia, CCNews, and ELI5. The main system is Llama-2-70B-Instruct, with Llama-3.3-70B-Instruct, Llama-3.1-8B-Instruct, Mistral-Small-24B-Instruct-2501, and Ministral-8B-Instruct-2410 in subsets. Human and regenerated corpora contain roughly 0.6M-6.6M articles per listed condition, with tens to hundreds of millions of successfully parsed sentences. Stanza supplies dependency and constituency parses; vLLM generation uses temperature 1.0. Wikipedia and CCNews prompts include the first 256 and 180 words and target at least 700 and 500 words; ELI5 receives only the title and targets at least 100 words.
- **Direct versus cited evidence:** C01-C26 and C29 are direct methods, results, examples, interpretations, or limits from this paper. C27 records claims inherited from cited work on model collapse, token/topic diversity, and POS-template homogeneity. C28 records the paper's comparison with Russell et al.'s detector tips. Neither cited source was ingested as part of this source boundary.
- **Important limits and counterexamples:** no known training inventory; no random decoding-temperature comparison; no non-English data; no closed-model results; no human-authorship classification evaluation; metric availability depends on successful parsing; article-level and sentence-level denominators differ; cleaning excludes fewer than 10% of CCNews and fewer than 15% of Wikipedia on average; readability is calculated on uncleaned articles over 100 words; Appendix A's raw-versus-filtered plots cover only dependency-tag and constituency-label counts for Wikipedia and CCNews, while depth/Yngve ablations are not plotted; ELI5 depth variance is the study's one clear no-narrowing case; dependency-tag results have no long-tail reduction because the human distribution is near-normal; qualitative examples are anecdotal.

## Skill-use audit

- **Good use:** support H22's model-, domain-, metric-, and prompt-scoped structural-variation research; qualify #52 by showing that sentence-length standard deviation is only one coarse member of a broader distributional family; supply exact qualitative examples for conclusion, significance, sales-register, source-verification, and journalism review.
- **Misuse / overclaim:** calling low sentence-length variance a proven authorship test, treating every short or narrow distribution as simplification, claiming all regenerated means shift the same way, or turning the paper's suggested detection relevance into detector accuracy.
- **Unsupported use:** vocabulary, punctuation, generic model-family attribution, causal claims about pretraining or post-training, current closed-model behavior, non-English prose, a universal severity threshold, or a single-document AI verdict.
- **Underused evidence:** explicit null and exception handling; separate mean, variance, and tail signatures; domain-specific direction; parse-feature and readability measures; exact generation and filtering conditions; qualitative factual and attribution failures.
- **Patterns left on the table:** right-tail and parse-shape evaluation beyond #52; British-to-American spelling drift; invented quotations and acronyms; factual error checks; generic value-judgment and sales-ending variants that current deterministic checks miss.

## Matched patterns / rules

- H22 `Long-tail compression and grammatical standardisation`: direct conceptual home for C05-C12, but still open and unimplemented.
- #52 `sentence-length-variance`: partial coverage of C06 and only coarse adjacency to C07-C12; it computes within-document sentence-word-count standard deviation, not corpus mean shift, parse distributions, or right-tail loss.
- H13 `Sentence-length mean as a grader check` and H12 `Genre-aware threshold calibration`: research homes for the mean and domain-specific direction, both open and unimplemented.
- #44 `no-signposted-conclusions`: exact coverage for line-initial `In conclusion` in C17/C19. Focused checks failed on that phrase as expected.
- #24 `no-generic-conclusions`, #4 `no-promotional-language`, #1 `no-significance-inflation`, and #34 `no-tidy-paragraph-endings`: partial or challenged coverage for C16-C20. Focused checks caught `testament` in one CCNews ending and line-initial `In conclusion`, but missed the ARKit sales ending, `His legacy endures`, the article `A` wrap-up except when isolated at line start, and the factual errors.
- #41 `genre_specific`, journalism branch, plus source-grounding and closed-source process guidance: manual coverage for C18-C20's unverifiable quotations, unsupported claims, and factual checks.
- H25 `Model-family versus generic-AI residue`: appropriate caution for the Llama-2 qualitative examples and other model comparisons; not an implemented attribution feature.

## Associated hypotheses

- H12 Genre-aware threshold calibration
- H13 Sentence-length mean as a grader check
- H22 Long-tail compression and grammatical standardisation
- H25 Model-family versus generic-AI residue

## Questions / follow-up

- Should H22 evaluation add constituency-label, dependency-tag, parse-depth, Yngve-tail, and sentence-length-tail measures with domain, model, prompt, length, and decoding metadata?
- Should qualitative source-backed variants be evaluated for #44/#24/#4/#1 and journalism review, using quoted, academic-conclusion, legitimate-news, human-sales, and human-editorial controls before any product change?
- Should the project record the stale abstract/full-PDF discrepancy as a general source-ingest test for first-party landing pages?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | ACL Anthology ID 2025.findings-acl.120; legacy landing-page/Jina capture whose abstract names two domains | `snapshots/archive/ju-blix-williams-domain-regeneration/2026-05-05-b5006e7438c4.md` | 2026-05-05 | `b5006e7438c4570f8bb86580c492b0384163137bf989d937446c00c628094ac5` |
| current | ACL Anthology ID 2025.findings-acl.120; DOI 10.18653/v1/2025.findings-acl.120; arXiv:2505.07784v2 | `snapshots/ju-blix-williams-domain-regeneration.md` | 2026-07-15 | `33b381404724efb7515ef94c6409fd7eff0c85a101828fac011d261b9410566f` |

The legacy card did not record a snapshot digest. Before replacement, the exact on-disk legacy bytes were hashed as `b5006e7438c4570f8bb86580c492b0384163137bf989d937446c00c628094ac5` and archived unchanged. Compared with that record, the current snapshot replaces page metadata and an abstract with the complete paper; adds ELI5, model variants, methods, tables, figures, prompts, ablations, examples, references, limitations, attachments, and full provenance; and corrects the prior two-domain and single-model scope. The central narrower-distribution and reduced-tail finding remains, now bounded by the paper's exceptions and conditions.

## Decision history

- The previous card had no claim IDs, user decisions, implementation statuses, evaluation lines, or document-review gate. No approved or implemented product change is carried forward.
- The prior #52 mapping is retained only as partial coverage because the live check measures one document's sentence-word-count standard deviation and does not implement the paper's corpus distributions, means, parse metrics, or tails.
- Prior H1 and H2 associations are retired from the active mapping: continuous calibration and a comparison-engine reframe are internal product proposals that this paper does not directly evaluate. H12 remains relevant, and the existing H22 is the more precise research home.
- All current recommendations are reopened as `pending` and `not started` for Mae. No checker, registry, hypothesis, guidance, test, or product file changed in this update.
- C19 approved 2026-07-25 via DR-21F: #24 now recognises the paper's three uncovered Table 10 ending and reader-address forms.

## Project coverage

This is the authoritative review table. Give every relevant source claim or example a stable claim ID in the first cell.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The authoritative ACL and arXiv v2 PDFs evaluate three domains, while their current metadata abstracts still say two. | Direct first-party provenance discrepancy; both PDFs are 22 pages and include ELI5. | Not covered by a product check; source-ingest provenance review catches it manually. | No deterministic gate compares landing-page metadata with full-text scope. | Record the discrepancy; test a first-party metadata-versus-full-text ingest check before proposing tooling. | pending | not started |
| C02: Domain regeneration continues a supplied document opening and compares the regenerated continuation with the human original to partly control topic and content. | Direct experimental design; semantic control is partial, not equivalence. | Fully covered as evidence framing by the source-card contract and H22 comparison design. | No project metric implements this regeneration experiment. | Use as H22 evaluation design context; do not present it as a product capability. | pending | not started |
| C03: The study covers English Wikipedia, CCNews, and ELI5 with five named open-weight instruction models in different subsets and vLLM temperature 1.0. | Direct methods and Table 2 scope; training data membership is not known. | Fully covered as required source metadata; H12/H25 provide research homes. | Current checks are not model-, prompt-, or domain-calibrated from these data. | Require domain, model, prompt, temperature, and length metadata in any H22 replication. | pending | not started |
| C04: Filtering removes sentences under 3 or over 500 words and those without a verb/auxiliary; parse failures and zero-valid-length articles are excluded. Appendix A shows the same broad trend only for raw-versus-filtered dependency-tag and constituency-label plots on Wikipedia and CCNews; depth/Yngve ablations are not plotted because article-level aggregates showed minimal variation on inspection. Average exclusions are under 10% for CCNews and under 15% for Wikipedia, and readability uses uncleaned articles over 100 words. | Direct methods and bounded Appendix A ablations; residual tooling error is not quantified. | Not covered in active checks; `dev/TESTING.md` requires provenance and comparable opportunity. | No H22 protocol yet specifies parsing exclusions or ablation reporting; the reported ablations do not cover every metric or ELI5. | Add exclusion counts and raw-versus-clean ablations to a future H22 protocol without generalizing beyond the plotted measures and domains. | pending | not started |
| C05: CCNews/Wikipedia regenerations contain more sentences and words per article than human articles; ELI5 regenerations contain fewer, while words per sentence are similar overall. | Direct Table 2 descriptive result; model and domain specific. | Partly covered by H13 and length-aware testing guidance; #52 measures neither article length nor mean sentence length. | Article length and sentences per article are absent from active structural checks. | Record as evaluation metadata; do not create a length rule without matched-domain controls. | pending | not started |
| C06: Sentence-length distributions narrow and lose a heavy right tail across domains/models. For Llama-70B, regenerated sentences are longer on average for CCNews and ELI5 but shorter for Wikipedia; other-model mean shifts are inconsistent. | Direct Appendix C result and explicit qualification. | Partly covered by #52 for within-document SD, H13 for mean, and H22 for tails. | #52 has no corpus-tail measure, domain calibration, or model comparison. | Evaluate sentence mean, SD, and right-tail metrics separately under H22/H13 before changing #52. | pending | not started |
| C07: Flesch-Kincaid distributions narrow and lose the right tail for all three domains; means rise for CCNews/Wikipedia and fall for ELI5. Across Tables 5-9, human Wikipedia is simplest and Llama-3 CCNews most complex on means and medians; human CCNews has the greatest readability variation, the second-highest variation depends on the score, and Spache distinguishes the fewest dataset pairs. | Direct Figure 1, Figure 15, and Tables 5-9; readability combines sentence and syllable length. | Partly covered by H12/H22; no live readability check exists. | Readability cannot be treated as pure syntax or a universal quality direction; secondary dispersion rankings vary by score. | Record as a research feature; require genre, language, length, and metric controls before any product proposal. | pending | not started |
| C08: Unique dependency-tag counts have narrower distributions; Section 3.3 describes slightly higher means in every domain while Table 1 schematizes Wikipedia as approximately equal. There is no long-tail reduction because human distributions are near-normal. | Direct Figures 2-4 and Table 1; explicit null for tail reduction and a bounded prose/table discrepancy. | H22 is conceptual coverage only. | No dependency-tag metric or null-result representation exists in the product. | Include dependency-tag diversity and explicit no-tail cases in H22 evaluation; no active rule now. | pending | not started |
| C09: Llama-70B parse depth narrows for Wikipedia/CCNews and its mean rises in all three domains, but ELI5 is the only clear no-narrowing case. Most slight human right tails reappear in the other-model subsets, except for Mistral-24B on CCNews and Wikipedia. | Direct Figure 5, Figure 16, and results text; material null and tail-reproduction exceptions. | H22 conceptual coverage only. | No parse-depth metric; a universal narrowing claim would be false. | Preserve the ELI5 null and model-specific right-tail exceptions in any H22 design; do not promote a universal rule. | pending | not started |
| C10: Yngve distributions narrow and have reduced but still visible right tails; Wikipedia mean rises while CCNews/ELI5 means fall; other models show the same diversity/tail trend. | Direct Figure 6, Figure 17, and results text. | H22 conceptual coverage only. | No Yngve or branching-tail metric exists. | Test Yngve-tail value incrementally against #52 on matched domains before adoption. | pending | not started |
| C11: Unique constituency-label distributions narrow across domains/models and largely lose a slight human right tail; mean direction varies for CCNews and rises for Wikipedia/ELI5. | Direct Figures 7-9 and results text. | H22 conceptual coverage only. | No constituency-label metric or domain-specific mean handling exists. | Add as an H22 research candidate, not an active surface rule. | pending | not started |
| C12: Across most metrics and datasets, regenerated text is less diverse by variance and tail, while mean shift is not uniform. | Direct cross-metric synthesis; supported by the preceding metric-specific results and nulls. | Fully covered as H22's statement; only partly implemented by #52. | H22 remains open and unimplemented; #52 is too narrow to stand in for the result. | Keep Ju et al. as primary H22 evidence and evaluate richer features before product change. | pending | not started |
| C13: The authors interpret domain-specific mean shifts as complexity overshoot rather than convergence on a neutral-domain middle. | Author interpretation of observed distributions; the training-distribution mechanism is not directly tested. | Partly covered by H12 and H25 framing. | No active output distinguishes measured direction from mechanism interpretation. | Record as interpretation only; require replication before any mechanism or model-family claim. | pending | not started |
| C14: Reduced variance/tails are compatible with simplification or failure to generate rare syntactic combinations; rare left-branching structures are one example. | Qualified author interpretation, not a causal or exhaustive test. | H22 states grammatical standardisation cautiously. | The live #52 guidance speaks broadly about natural human variation but does not test rare syntax. | Keep `compatible with` wording; do not relabel every narrow distribution as simplification. | pending | not started |
| C15: Llama-2 Wikipedia continuations sometimes normalize British `-ise` spellings to American `-ize`. | Direct manual observation with three examples; no rate or human control. | Not covered; H25 is a research home for model-specific residue. | No paired source-versus-continuation spelling assessment exists. | Record as a dated Llama-2 candidate only; require paired style controls before any assessment. | pending | not started |
| C16: Llama-2 Wikipedia continuations add value judgments that violate neutral-point-of-view style. | Direct manual observation and examples; no prevalence estimate. | Partly covered by source-preservation guidance and #41 source/factual review; `neutrality_collapse` concerns stance erasure, not added praise. | Current mappings could confuse added judgment with loss of stance. | Keep separate from #37; evaluate only in paired source/rewrite or domain-style review. | pending | not started |
| C17: Llama-2 Wikipedia examples add essay-like wrap-ups, explicit conclusion labels, praise, and enduring-legacy claims. | Direct qualitative examples; anecdotal. | #44 recognises explicit conclusion labels; #24 now recognises the source's exact legacy, praise, hope, and sales-ending formulas. | The exact generic-ending variants were the executable gap. | Add the source's exact ending formulas to #24. | approved | implemented |
| C18: Llama CCNews continuations insert quotations attributed to famous people and acronyms absent from the source; original quoted articles usually contain one longer quote. | Direct manual comparison; no corpus rate or verification of every named quotation. | Fully covered as a manual journalism/source-verification concern by #41; no deterministic quote-provenance check. | Bare prose cannot establish whether a quote or acronym was supplied by the source. | Preserve paired-source verification as manual guidance; do not add lexical authorship rules. | pending | not started |
| C19: CCNews continuations add PR/sales endings, reader address, praise, and explicit `In conclusion` framing. | Direct qualitative examples and Table 10; anecdotal and model-specific. | Covered by #44/#4/#24/#1/#34. #24 now also recognises the three uncovered Table 10 forms: the `Whether you're ... or simply someone ...` audience address, `we can expect to see even more`, and `certainly worth keeping an eye on`. | None for the named surface forms. | Keep the three approved ending and reader-address frames in #24. | approved with changes | implemented |
| C20: The generated Wikipedia `A` passage contains factual/grammatical errors, including false pronoun and suffix analyses. | Direct author correction in text and footnote; one extended example. | Fully covered as a manual source-grounding/factual-verification concern; surface pattern checks miss it. | Human-eyes does not run general factual verification. | Record as a source-checking example only; do not claim factuality detection or authorship. | pending | not started |
| C21: Regenerations were never word-for-word identical to originals and did not exactly meet prompted average lengths. | Direct Appendix B observation; no detailed length-error distribution. | Not covered by prose-pattern checks; process guidance forbids assuming prompt compliance. | No prompt-versus-output binding exists in ordinary Audit. | Record as generation-protocol context; take no pattern action. | pending | not started |
| C22: Parsing and metric calculation can fail on extremely long, complicated, non-English, malformed, or link-only material; uniform processing is expected to make errors comparable. | Direct limitation plus author expectation; residual bias unmeasured. | Fully covered by testing/provenance expectations at a general level. | No project parser metric is being implemented, and comparability is not proof of no bias. | Require per-condition exclusions and sensitivity checks in future H22 work. | pending | not started |
| C23: Temperature 1.0 was used; lower temperature is presumed to reduce diversity and higher temperature may increase it, while long-tail effects are unclear. | Direct method plus explicit untested speculation. | H25 and testing provenance partly cover decoding metadata. | No temperature experiment in the paper or project validates the presumed direction. | Record the tested temperature and leave all alternative-temperature claims unresolved. | pending | not started |
| C24: Existing syntactic metrics are limited; qualitative style/content changes could motivate new metrics. | Direct limitation and future-work proposal. | Fully covered as hypothesis-only handling by H22 and source-ingest decision integrity. | Qualitative examples do not validate a metric or threshold. | Treat each qualitative family as a separate evaluation candidate, never as an implemented rule. | pending | not started |
| C25: The results may inform domain-transfer decisions, model improvement, or synthetic-text detection. | Author-stated possible implications, not an evaluated application. | Fully covered by the project's non-authorship boundary and hypothesis workflow. | The paper reports no detector, threshold, accuracy, calibration, or user study. | Record implications only; do not cite this as detector performance or authorship proof. | pending | not started |
| C26: Exact model training data are proprietary/unknown; the authors select likely training domains and cannot cover every domain or train a comparable model from scratch. | Direct design limitation and practical rationale. | Fully covered by source metadata and H25 caution. | Likely training exposure is not verified contamination or memorization. | Preserve uncertainty; do not attribute results to confirmed training membership. | pending | not started |
| C27: Model collapse, similar data patterns, repeated tokens, lower topic diversity, and prior POS-template homogeneity are inherited from cited studies. | Indirect evidence only; the cited papers are outside this ingest boundary. | Some have separate project cards, but this card does not directly validate their claims. | Recursive ingestion and mechanism adoption would exceed source scope. | Keep indirect and unresolved here; use separately reviewed primary cards for any project decision. | pending | not started |
| C28: The paper says some Wikipedia qualitative trends overlap Russell et al.'s detector tips, including formalized conclusions and spelling normalization. | Indirect comparison plus the paper's own anecdotal observations; Russell et al. is not re-reviewed here. | H25 and separate Russell source coverage are adjacent. | Overlap does not establish prevalence, specificity, or a universal detector cue. | Record overlap only; require the direct Russell review for any detector-related conclusion. | pending | not started |
| C29: Appendix I/Table 10 says anecdotally that human CCNews examples appear less similar to the Llama continuations than the two Llama generations appear to each other. | Direct author observation from two prompt-title example groups; no similarity metric, rate, or significance test. | H25 conceptually; H22 comparison framing only. | Model-specific and anecdotal; no systematic similarity measure or broader domain/model evidence. | Record as context only; if evaluated, predefine similarity and use matched human/model controls; no active rule. | pending | not started |

## Recommendations

- C01: Record the metadata/full-text discrepancy and test an ingest-only comparison gate before tooling changes.
- C02: Use domain regeneration as H22 design context only.
- C03: Require domain, model, prompt, temperature, and length metadata in H22 work.
- C04: Require exclusions and raw-versus-clean ablations in any parse-feature evaluation.
- C05: Record article and sentence counts as metadata, not a prose rule.
- C06: Evaluate sentence mean, SD, and right-tail metrics separately before changing #52.
- C07: Keep readability as a controlled research feature only.
- C08: Include dependency-tag diversity and its no-tail result in H22 evaluation.
- C09: Preserve the ELI5 depth null and model exceptions; do not promote a universal narrowing rule.
- C10: Test Yngve tails incrementally against #52 before adoption.
- C11: Add constituency-label diversity as an H22 research candidate only.
- C12: Retain Ju et al. as direct H22 evidence; leave active checks unchanged pending evaluation.
- C13: Record domain overshoot as author interpretation, not mechanism.
- C14: Preserve the paper's `compatible with simplification` qualification.
- C15: Record Americanization as a dated Llama-2 paired-style candidate only.
- C16: Keep added judgment separate from #37 neutrality-collapse evidence.
- C17: Add the exact legacy, praise, hope, and sales-ending formulas to #24.
- C18: Keep quote/acronym verification as paired-source manual journalism guidance.
- C19: Keep the three approved sales-ending and reader-address frames in #24.
- C20: Record factual error as source-verification context only.
- C21: Record non-identical and target-length noncompliance as protocol context only.
- C22: Require condition-level exclusion and sensitivity reporting in H22 work.
- C23: Record temperature 1.0 and leave other-temperature effects unresolved.
- C24: Treat each proposed qualitative metric as a separate pending evaluation.
- C25: Do not cite the paper as detector accuracy or authorship evidence.
- C26: Preserve uncertainty about training membership.
- C27: Use separately reviewed primary sources for inherited claims.
- C28: Treat Russell overlap as indirect until its direct source record supports a decision.
- C29: Record the Table 10 similarity observation as anecdotal Llama/CCNews context; require a predefined paired comparison before research use.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change.
- C02: not applicable - pending recommendation; no product change.
- C03: not applicable - pending recommendation; no product change.
- C04: not applicable - pending recommendation; no product change.
- C05: not applicable - pending recommendation; no product change.
- C06: not applicable - pending recommendation; no product change.
- C07: not applicable - pending recommendation; no product change.
- C08: not applicable - pending recommendation; no product change.
- C09: not applicable - pending recommendation; no product change.
- C10: not applicable - pending recommendation; no product change.
- C11: not applicable - pending recommendation; no product change.
- C12: not applicable - pending recommendation; no product change.
- C13: not applicable - pending recommendation; no product change.
- C14: not applicable - pending recommendation; no product change.
- C15: not applicable - pending recommendation; no product change.
- C16: not applicable - pending recommendation; no product change.
- C17: passed - DR-16A asserts #24 failures for the source's legacy, icon, enduring-generations, inspire-and-captivate, future-prospects, well-positioned, sales-call, hopeful, and testament formulas.
- C18: not applicable - pending recommendation; no product change.
- C19: passed - DR-21F asserts #24 failures for the audience-enumeration reader address, the forward-looking expectation closer, and the certainly-worth-watching closer, and passes for an ordinary `whether` clause and ordinary keeping-watch wording.
- C20: not applicable - pending recommendation; no product change.
- C21: not applicable - pending recommendation; no product change.
- C22: not applicable - pending recommendation; no product change.
- C23: not applicable - pending recommendation; no product change.
- C24: not applicable - pending recommendation; no product change.
- C25: not applicable - pending recommendation; no product change.
- C26: not applicable - pending recommendation; no product change.
- C27: not applicable - pending recommendation; no product change.
- C28: not applicable - pending recommendation; no product change.
- C29: not applicable - pending recommendation; no product change.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/ju_domain_regeneration_reviewer`
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** 5 material findings plus one reviewer-suggested nuance: bounded the Appendix A cleaning ablations; added exact sentence-length mean directions; restored Tables 5-9 readability rankings, dispersion qualifications, and the Spache null; separated dependency prose/table summaries; attached Mistral-24B exceptions to right-tail reproduction; added and bounded the Appendix I/Table 10 anecdote. Focused re-check found 0 residual findings.
- **Unresolved findings:** none
