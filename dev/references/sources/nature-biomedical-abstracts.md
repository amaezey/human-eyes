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
- **Access limitations:** the canonical URL is paywalled and its public page exposes only a short teaser. Institutional access was supplied on 2026-07-17 and the complete rendered article element preserved. Unrelated page navigation and job listings after `Reprints and permissions` were trimmed; the body, byline, figure credit, DOI line, and all three references are complete.

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

- **Direct source reviewed:** complete Nature News article for DOI 10.1038/d41586-025-02097-6, captured from the canonical paywalled page through an institution-authenticated browser session on 2026-07-17; title/deck/byline block, figure credit, 11 substantive paragraphs across two named sections, DOI line, and three references preserved
- **Method and sample:** the article itself conducts no empirical analysis. It reports Kobak et al.'s analysis of PubMed abstracts through 2024 and Geng and Trotta's arXiv analysis through late 2024. The page reports 1.5 million 2024 PubMed abstracts, more than 200,000 affected abstracts, 454 excess 2024 word forms, 190 excess 2021 word forms, and selected country/field comparisons; it does not state language, length, full subgroup methods, uncertainty, or model family.
- **Direct versus cited evidence:** C01 and the article's publication/provenance are direct. C02-C09 are reports of Kobak et al. or Geng and Trotta and remain indirect here. C10-C13 separate Mallapaty's framing and attributed expert interpretations from the cited empirical evidence. The already-ingested `kobak-llm-excess-vocabulary.md` and `geng-trotta-human-llm-coevolution.md` cards, not this article, are the project's direct research records.
- **Important limits and counterexamples:** no labelled authorship ground truth; no use-mode observation; no model identity; no document-level validation; no exact uncertainty; historical topical spikes show lexical change is not uniquely LLM-driven; field and country estimates are heterogeneous; publicised words can decline; adaptation is a possible rather than established cause; and reasonable polishing or translation cannot be separated from unsupervised generation.

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

## Prior-to-current comparison

- **Added:** complete article text, exact access provenance, attachment hash, archive history, 13 stable claims, direct-versus-cited boundaries, focused live-code coverage, decision states, and independent-review fields.
- **Corrected:** the article is secondary journalism rather than primary pattern evidence; one in seven is journalistic shorthand for a cited corpus lower bound; more than 200,000 is a derived scale estimate, not individually observed papers; late-2024 avoidance is a possible explanation rather than a causal result; and named words do not validate a document threshold.
- **Removed:** no substantive source claim. The legacy suggestion that `unparalleled` and `invaluable` might become candidate examples is replaced by a decision-ready review of their existing implementation and primary-source provenance.
- **Unchanged:** title, DOI, author, publication date, canonical URL, broad B1 and aggregate-stacking relevance, and the no-individual-authorship boundary.
