# Nature: Signs of AI-generated text found in biomedical abstracts

## Metadata

- **URL:** https://www.nature.com/articles/d41586-025-02097-6
- **Author / owner:** Smriti Mallapaty
- **Published:** 2025-07-02
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** science journalism
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** DOI 10.1038/d41586-025-02097-6
- **Version / revision:** Nature News article published 2025-07-02, no revision identifier exposed; prior reviewed capture was a paywalled teaser retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/nature-biomedical-abstracts.md`
- **Extraction method:** user-authenticated rendered-page text extraction from canonical Nature `<article>`, preserved verbatim by primary agent in local attachment and transcribed into snapshot
- **Snapshot SHA-256:** `442b81c6e2ddf77bbabee79c16275101030d4d4298632dc69d8a419729e344e9`
- **Model / corpus scope:** no model family or version identified; PubMed biomedical abstracts in 2024, with historical comparisons since 2010; cited Geng and Trotta arXiv trend through late 2024; language and abstract-length filters are not stated in this Nature article
- **Access limitations:** the canonical URL is paywalled and its public page exposes only a short teaser. Mae supplied institutional access on 2026-07-17; the primary agent preserved the complete rendered article element. Unrelated page navigation and job listings after `Reprints and permissions` were trimmed; the body, byline, figure credit, DOI line, and all three references are complete.

## Summary

This Nature News article reports the peer-reviewed Kobak et al. excess-vocabulary study and a then-preprint Geng and Trotta longitudinal analysis. It supplies a compact public account of the 2024 PubMed lower-bound estimate, named vocabulary examples, historical and subgroup comparisons, public-tell decline, and uncertainty about how LLMs were used. Its empirical claims are secondary: the already-ingested Kobak and Geng/Trotta records carry the underlying evidence and stronger qualifications. The article is useful for provenance, public framing, quoted interpretations, and the explicit distinction between aggregate signals and unknown use modes; it does not validate individual-document authorship, the live three-item vocabulary threshold, or any research-integrity inference.

## Main insights

- The article reports the updated Kobak et al. result as around one in seven 2024 biomedical abstracts, more than 200,000 of 1.5 million, while the primary paper frames 13.5% as a corpus-level lower bound rather than individually observed papers.
- It contrasts the July 2025 peer-reviewed update with the June 2024 preprint estimate of one in nine for the first half of 2024.
- It describes the historical-counterfactual method and reports 454 excess word forms in 2024, mainly stylistic verbs and adjectives, compared with 190 largely topical excess words in 2021.
- Named 2024 examples are `findings`, `crucial`, `potential`, `delves`, `showcasing`, `heighten`, `hinder`, `unparalleled`, and `invaluable`. The article does not supply each word's frequency, gap, ratio, confidence interval, or a document threshold.
- It reports heterogeneity above one in five for some countries and fields but does not provide a complete subgroup table or uncertainty.
- It reports Geng and Trotta's late-2024 decline in publicised vocabulary such as `delves`, says this could make the latest AI-use estimate an undercount, and presents deliberate removal or prompt changes as a possible explanation. Neither the undercount nor the causal explanation is quantified.
- It says estimate methods are becoming harder as writing practices adapt, but the cited Geng/Trotta record also preserves nonuniform trajectories and detector nulls that this short news article does not detail.
- Andrew Gray interprets the reported trend as continued growth in LLM-edited papers, says researchers have not grasped its scale, and hopes the paper will draw attention. These are attributed reactions, not additional measurements.
- The source explicitly says the studies cannot determine whether AI polished or translated text, generated large passages, or was used another way. A corpus-level signal therefore cannot establish authorship, oversight, or misconduct.
- The article's research-integrity concern is an attributed interpretation from Andrew Gray, not a measured integrity outcome.

## Evidence and claims to extract

- **Direct source reviewed:** complete Nature News article for DOI 10.1038/d41586-025-02097-6, captured from the canonical paywalled page through Mae's institution-authenticated Chrome session on 2026-07-17; title/deck/byline block, figure credit, 11 substantive paragraphs across two named sections, DOI line, and three references preserved
- **Method and sample:** the article itself conducts no empirical analysis. It reports Kobak et al.'s analysis of PubMed abstracts through 2024 and Geng and Trotta's arXiv analysis through late 2024. The page reports 1.5 million 2024 PubMed abstracts, more than 200,000 affected abstracts, 454 excess 2024 word forms, 190 excess 2021 word forms, and selected country/field comparisons; it does not state language, length, full subgroup methods, uncertainty, or model family.
- **Direct versus cited evidence:** C01 and the article's publication/provenance are direct. C02-C09 are reports of Kobak et al. or Geng and Trotta and remain indirect here. C10-C13 separate Mallapaty's framing and attributed expert interpretations from the cited empirical evidence. The already-ingested `kobak-llm-excess-vocabulary.md` and `geng-trotta-human-llm-coevolution.md` cards, not this article, are the project's direct research records.
- **Important limits and counterexamples:** no labelled authorship ground truth; no use-mode observation; no model identity; no document-level validation; no exact uncertainty; historical topical spikes show lexical change is not uniquely LLM-driven; field and country estimates are heterogeneous; publicised words can decline; adaptation is a possible rather than established cause; and reasonable polishing or translation cannot be separated from unsupervised generation.

## Skill-use audit

- **Good use:** secondary public framing for the Kobak and Geng/Trotta records; provenance for the Nature-derived `unparalleled` and `invaluable` examples; explicit aggregate, drift, subgroup, and unknown-use-mode cautions.
- **Misuse / overclaim:** citing one in seven as a count of individually detected AI-written abstracts; treating any named word or live checker result as proof of AI assistance, authorship, weak oversight, or misconduct; or treating the quoted 2025 forecast as a measured later result.
- **Unsupported use:** document classification, model-family attribution, a generic cross-register vocabulary blacklist, the live three-item paragraph threshold, the live Kobak density thresholds, detector accuracy, causal adaptation, use-mode prevalence, or a research-integrity verdict.
- **Underused evidence:** the project already preserves the stronger primary evidence, but the current local list substring-matches `valuable` inside `invaluable`, causing a two-word Nature example to count as three generic vocabulary items and cross the B1 threshold.
- **Patterns left on the table:** none for direct promotion from this secondary article. `heighten` and `hinder` are already present in the complete Kobak CSV, while Geng/Trotta directly carries the late-2024 drift evidence.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: directly recognizes `crucial`, substring `delve` in `delves`, `showcasing`, `unparalleled`, and `invaluable`; it also counts `valuable` inside `invaluable`. It does not locally recognize standalone `findings`, `potential`, `heighten`, or `hinder`.
- `overall-signal-stacking`: its Kobak profile recognizes all nine named words as style entries from the bundled 900-row multi-year CSV. In a focused nine-word sample, vocabulary alone scored 2 of 4 and did not trigger the aggregate finding.
- `human-eyes/references/kobak-excess-words.csv`: contains all nine named forms as style annotations, but the primary Kobak card establishes that this is a 2013-2024 union rather than a Nature-specific or 2024-only list.
- H24 `Register-specific vocabulary density`: directly captures repeated, co-occurring, dated, and register-specific vocabulary evaluation rather than flat word bans.
- H25 `Model-family versus generic-AI residue`: adjacent as a missing-source-scope control because this article names no model family or version.
- `human-eyes/references/process.md` and `dev/TESTING.md`: correctly prohibit authorship inference and separate surface coverage checks from complete Audits.
- `human-eyes/scripts/judgement.json`: no agent assessment implements longitudinal vocabulary change, use-mode inference, or research-integrity classification.

## Associated hypotheses

- H1: Continuous calibrated register-distance score per pattern.
- H3: Drop detection framing entirely.
- H7: Five-check gating grader plus advisory catalogue.
- H12: Genre-aware threshold calibration.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.

## Questions / follow-up

- Should B1 stop substring-matching `valuable` inside `invaluable` and instead count distinct, boundary-matched source terms before any threshold decision?
- Should the current Nature comment and fixture remain as provenance only, given that its three explicit tokens (`unparalleled`, `invaluable`, and practitioner-derived `meticulous`) produce four matcher entries because `valuable` substring-matches inside `invaluable`, while the source supplies no three-item paragraph threshold?
- No cited-source ingestion is needed: the Kobak Science Advances paper and the Geng/Trotta arXiv-to-ACL work already have direct cards.

## Update provenance

The legacy card did not record a snapshot digest. Its 2026-07-15 hygiene-ledger entry recorded SHA-256 `024bbc4da1b81a699d044bc5f516d2a750fabaab8926793fc86b281016b85ea0`; that digest matched the exact bytes on disk before archival. The legacy card's 2026-05-05 extraction date is used below because it had no separate retrieval field.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | DOI 10.1038/d41586-025-02097-6; paywalled teaser capture | `snapshots/archive/nature-biomedical-abstracts/2026-05-05-024bbc4d.md` | 2026-05-05 | `024bbc4da1b81a699d044bc5f516d2a750fabaab8926793fc86b281016b85ea0` |
| current | DOI 10.1038/d41586-025-02097-6 | `snapshots/nature-biomedical-abstracts.md` | 2026-07-17 | `442b81c6e2ddf77bbabee79c16275101030d4d4298632dc69d8a419729e344e9` |

## Decision history

- The 2026-05-05 pre-contract card had no claim IDs, user decisions, implementation statuses, digest, update-provenance table, or independent source-record review. Its useful secondary-source, aggregate-not-document, B1, overall-stacking, and biomedical-register mappings are reopened and qualified as C01-C13. No prior approved, rejected, or implemented decision exists.
- The complete capture shows that the teaser's headline and opening estimate were accurate but omitted methods framing, the 454-versus-190 comparison, nine named words, subgroup heterogeneity, Geng/Trotta drift, adaptation uncertainty, and the unknown-use-mode limit.
- C07 is linked to the already-approved DR-02 counting fix (`13e235f`): non-overlapping spans count per occurrence and nested entries resolve to the longest match, so `unparalleled` plus `invaluable` now produces two matches rather than a false three-item threshold failure.

## Prior-to-current comparison

- **Added:** complete article text, exact access provenance, attachment hash, archive history, 13 stable claims, direct-versus-cited boundaries, focused live-code coverage, decision states, and independent-review fields.
- **Corrected:** the article is secondary journalism rather than primary pattern evidence; one in seven is journalistic shorthand for a cited corpus lower bound; more than 200,000 is a derived scale estimate, not individually observed papers; late-2024 avoidance is a possible explanation rather than a causal result; and named words do not validate a document threshold.
- **Removed:** no substantive source claim. The legacy suggestion that `unparalleled` and `invaluable` might become candidate examples is replaced by a decision-ready review of their existing implementation and primary-source provenance.
- **Unchanged:** title, DOI, author, publication date, canonical URL, broad B1 and aggregate-stacking relevance, and the no-individual-authorship boundary.

## Project coverage

This is the authoritative review table. Focused deterministic results are surface-only coverage checks of the live code, not complete Audits or authorship results. C07 is approved and implemented via DR-02; every other recommendation remains pending for Mae. This DR-126 documentation update made no runtime change.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Nature published Mallapaty's News article on 2025-07-02 with DOI 10.1038/d41586-025-02097-6 and three references: the peer-reviewed Kobak paper, its preprint, and the Geng/Trotta preprint. | Direct page identity and reference list from the complete rendered article. The two Kobak references are versions of one work; Geng/Trotta later appeared in Findings of ACL 2025. | fully covered by this card, the snapshot, `kobak-llm-excess-vocabulary.md`, and `geng-trotta-human-llm-coevolution.md`. | The old card lacked a complete capture, DOI metadata, version relation, and directness boundary. | **adopt:** retain Nature as secondary journalism and route empirical decisions to the already-ingested primary cards; verify with source-card validation. | pending | not started |
| C02: The article reports that around one in seven 2024 biomedical abstracts were probably written with AI help and that more than 200,000 of 1.5 million PubMed abstracts contained LLM-associated words. | Indirect report of Kobak et al. The primary paper's 13.5% is a corpus-level lower bound and the annual count is a derived scale estimate, not individually observed papers, accuracy, or per-document probability. | fully covered by the Kobak card C09-C10 and the project product boundary. | The article's plain-language wording can obscure lower-bound construction and derived-count status. | **adopt:** cite the primary Kobak record for the estimate and keep lower-bound, derived-count, biomedical-register, and non-document qualifications attached; no checker change. | pending | not started |
| C03: The article contrasts a June 2024 preprint estimate of one in nine for the first half of 2024 with the July 2025 peer-reviewed update. | Indirect version-history report. Changed estimate may reflect a longer 2024 observation window and publication cycles; the article supplies no independent comparison method. | partly covered: the Kobak card covers the current peer-reviewed version and update provenance, while this Nature record supplies the reported one-in-nine first-half-2024 estimate and June 2024 chronology. | Treating the two estimates as detector drift or a direct within-method growth rate would exceed this article. | Record the version chronology only and take no product action. | pending | not started |
| C04: Undisclosed LLM use makes impact estimation difficult; black-box classifiers may be opaque and trained on data that miss current generated-writing trends. | Mallapaty's methodological framing, not an experiment conducted by Nature. It is consistent with cited research but supplies no classifier benchmark. | fully covered conceptually by H3, H25, `dev/TESTING.md`, and the no-authorship product boundary. | No source-specific detector result or error rate supports a runtime change. | Record as framing only; take no product action and do not attribute a detector result to Nature. | pending | not started |
| C05: Kobak et al. searched for excess words appearing more often than historically expected after November 2022, inspired by excess-deaths analysis. | Indirect method summary. The primary paper supplies the 2010-2024 English PubMed corpus, cleaning, length, frequency, baseline, and counterfactual details omitted here. | fully covered by Kobak card C01-C05 and H24. The live checker does not implement a historical counterfactual. | The article cannot validate the live document-level B1 or Kobak density thresholds. | Route method claims to the Kobak card; do not describe current document checks as implementations of this method. | pending | not started |
| C06: The article reports 454 2024 excess forms, mostly style words and often verbs or adjectives; common examples are `findings`, `crucial`, and `potential`, unusual examples include `delves` and `showcasing`, and later-2024 examples include `heighten`, `hinder`, `unparalleled`, and `invaluable`. | Indirect Kobak result. The article gives no per-word frequency, gap, ratio, uncertainty, model, or document threshold. All nine forms are style-labelled in the bundled Kobak union, whose primary card preserves the multi-year and year-selection limits. | Partly covered: B1 locally recognises `crucial`, `delve`, `showcasing`, `heighten`, `unparalleled`, and `invaluable` as six non-overlapping matches; the Kobak aggregate profile recognises all nine. A focused nine-word sample fails B1 with six generic matches but leaves `overall-signal-stacking` clear at 2 of 4. | Local coverage remains uneven; the source does not validate equal weights, a three-item paragraph threshold, or the 900-row union as a 2024 list. | **test-adapt:** retain the words as dated biomedical research examples, then test source-year metadata, register controls, and candidate count separately from thresholds before any further B1 change. | pending | review required |
| C07: A focused sentence containing only `unparalleled` and `invaluable` formerly crossed B1's three-item threshold because `valuable` was also found inside `invaluable`; the aggregate meta-check stayed clear. | Live-project comparison, not a Nature finding. Nature names two words but supplies no two-word or three-item rule. The primary Kobak CSV lists `unparalleled` and `invaluable`, not an extra `valuable` occurrence within the latter. | Fully covered by DR-02: `_find_ai_words` now counts non-overlapping occurrences and resolves nested entries to the longest match. The two-word sentence returns exactly `unparalleled` and `invaluable` and remains below the threshold. | No remaining substring-alias threshold bug for this fixture. The source still does not validate the project's threshold. | Retain DR-02's span-based longest-match counting and its regression coverage; do not change the threshold from this source. | approved | implemented |
| C08: The article contrasts 454 mostly stylistic 2024 excess forms with 190 mainly topical 2021 excess forms such as `mask`, while saying the post-LLM shift was more pronounced. | Indirect historical comparison. Topic-event spikes are a counterexample to treating abrupt lexical change as uniquely LLM-driven; the primary paper provides the full event-control analysis. | partly covered by Kobak card C05, H24, and the live profile's content/style metadata; no historical event-control decision exists at runtime. | The live checker cannot distinguish historical topic shifts from style shifts using the paper's method. | Preserve the topical-spike counterexample and require time, event, and register controls in any future vocabulary calibration; no immediate product change. | pending | not started |
| C09: More than one in five abstracts in some countries, including China and South Korea, and fields such as computation and bioinformatics are reported as LLM-assisted; Kobak expected the overall figure to keep rising in 2025. | Indirect subgroup report plus Kobak forecast. The article gives selected examples without a complete table, uncertainty, adjustment, or later-2025 measurement; geography and field may reflect use, editing, publication lag, or detectability. | fully covered by the more precise Kobak card C11-C14 and H12/H24. | Selected subgroup values cannot serve as priors for a specific paper, author, country, field, or later date. | Use only the primary card for subgroup detail and record the 2025 rise statement as forecast, not result; take no product action. | pending | not started |
| C10: The article reports Geng and Trotta's finding that publicised words such as `delves` became less frequent near the end of 2024, says AI use could therefore be higher than the latest estimate, and presents author removal or prompt changes as a possible explanation. | Indirect report plus Mallapaty's possible downward-bias framing. The final ACL card directly preserves group-average decline, nonuniform word trajectories, a `versatile` counterexample, prompt effects, detector nulls, and the explicit lack of causal identification. Neither Nature nor the cited study quantifies the claimed undercount. | fully covered for measured drift by `geng-trotta-human-llm-coevolution.md` C02-C04 and C09-C12, H24, H25, and the current pattern-opportunities drift row; the unquantified undercount interpretation is recorded only here. | The Nature summary can make adaptation appear more settled and uniform than the primary evidence and can make an unmeasured undercount sound estimated. | Route measured drift to the Geng/Trotta card; preserve possible undercount and deliberate avoidance only as unquantified interpretations, and do not publish evasion instructions. | pending | not started |
| C11: Geng says estimating AI impact is becoming harder as authors adapt. | Attributed expert interpretation informed by the cited preprint, not a measured universal or future impossibility result. | fully covered as strategic context by H3, H24, H25, and the Geng/Trotta card's detector-specific nulls and limits. | No later-period evidence or general detector benchmark is supplied here. | Record as interpretation only; take no product action or generic detector claim. | pending | not started |
| C12: The article says the studies cannot determine whether tools polished or translated text, generated large passages without oversight, or were used another way; Gray calls the uncertainty a research-integrity concern. | Directly reported limitation and attributed interpretation. No use-mode labels, oversight data, or integrity outcomes are measured. Reasonable and questionable uses are examples, not prevalence categories. | fully covered by the product boundary in `process.md`, H3, and Kobak card C15-C16. No judgement record classifies use mode or misconduct. | A vocabulary signal cannot establish authorship, degree of assistance, oversight, or misconduct. | **adopt:** keep unknown-use-mode and no-integrity-verdict language with every Nature mapping; take no detector or misconduct action from this source. | pending | not started |
| C13: Gray says LLM-edited papers have continued to rise, researchers have not grasped the scale, and the Kobak paper should draw attention to the issue. | Attributed expert interpretation responding to the reported study. Nature supplies no additional measurement for the claimed continuation, awareness level, or attention effect. | partly covered by the Kobak card's measured 2024 lower bound and forecast boundaries; no project check measures research awareness or attention. | The reaction can be mistaken for a later measured trend or an outcome of publication. | Record as attributed reaction only; take no product action and do not treat attention or continued rise as measured by Nature. | pending | not started |

## Recommendations

- C01: **adopt** the complete secondary-source identity and route empirical decisions to the already-ingested primary cards.
- C02: **adopt** the primary-source lower-bound, derived-count, biomedical-register, and non-document qualifications wherever the estimate is used.
- C03: Record the preprint-to-peer-reviewed chronology only; no product action.
- C04: Keep the classifier discussion as framing, not a source-specific benchmark; no product action.
- C05: Route method claims to the Kobak card and do not describe live document checks as implementations of its historical counterfactual.
- C06: **test-adapt** the nine words only with exact matching, source-year metadata, register controls, and separate candidate/threshold evaluation.
- C07: Retain the implemented DR-02 span-based longest-match counting; do not change the threshold from this source.
- C08: Preserve topical-event spikes as a counterexample and require time, event, and register controls in future calibration.
- C09: Use the primary Kobak card for subgroup evidence and keep the 2025 rise statement as forecast only.
- C10: Route measured drift to the Geng/Trotta card and retain possible undercount and deliberate avoidance as unquantified interpretations.
- C11: Record increasing difficulty as interpretation only; no generic detector claim.
- C12: **adopt** the unknown-use-mode and no-integrity-verdict boundary; make no detector or misconduct inference.
- C13: Record Gray's continued-rise, awareness, and attention statements as attributed reactions only; no product action.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change made.
- C02: not applicable - recommendation pending; no product change made.
- C03: not applicable - recommendation pending; no product change made.
- C04: not applicable - recommendation pending; no product change made.
- C05: not applicable - recommendation pending; no product change made.
- C06: not applicable - recommendation pending; existing B1 behavior remains under review.
- C07: passed - DR-02's span-based longest-match counting returns two matches for `unparalleled` plus `invaluable`, leaving the fixture below B1's threshold.
- C08: not applicable - recommendation pending; no product change made.
- C09: not applicable - recommendation pending; no product change made.
- C10: not applicable - recommendation pending; no product change made.
- C11: not applicable - recommendation pending; no product change made.
- C12: not applicable - recommendation pending; no product change made.
- C13: not applicable - recommendation pending; no product change made.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/nature_biomedical_reviewer`, fresh, source-dedicated, and strictly read-only; five-lens review followed by same-reviewer focused re-check of materially changed claims, coverage, recommendations, and statuses
- **Findings resolved:** four initial findings resolved: added Gray's continued-rise, awareness, and attention interpretation as C13; preserved Nature's unquantified possible-undercount framing in C10; corrected C03 from fully to partly covered; and corrected the fixture question to three explicit tokens, four matcher entries, and a paragraph threshold. Focused re-check returned zero residual findings.
- **Unresolved findings:** none
