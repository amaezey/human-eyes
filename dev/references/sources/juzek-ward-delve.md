# Juzek and Ward: Why Does ChatGPT “Delve” So Much?

## Metadata

- **URL:** https://aclanthology.org/2025.coling-main.426/
- **Author / owner:** Tom S. Juzek and Zina B. Ward
- **Published:** 2025-01
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** peer-reviewed conference paper with a first-party supporting-code repository
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** ACL Anthology ID 2025.coling-main.426; arXiv:2412.11385v1; DOI none found
- **Version / revision:** final COLING 2025 proceedings PDF; text token-identical to arXiv v1 and repository paper v106 after layout-marker normalization; supporting repository commit `0b7e2ba538bcc51ea538594512ef591ec24a1af1`
- **Full-text status:** complete
- **Snapshot:** `snapshots/juzek-ward-delve.md`
- **Extraction method:** official ACL PDF downloaded with `curl`; all 15 pages extracted with Poppler `pdftotext -layout`; pages 1, 8, and 15 rendered and visually checked; arXiv v1 and repository PDF text compared; supporting repository cloned, inspected, and preserved with `git archive`
- **Snapshot SHA-256:** `3626a29262151e1e4d6003787f447460e35a87e3b2e2101e062c0e4b1d11ae94`
- **Model / corpus scope:** 26.7 million PubMed abstracts and more than 5.2 billion tokens from 1975 to May 2024; 2020-versus-2024 lexical comparison; 10,000 sampled 2020 abstracts yielding 9,953 GPT-3.5-turbo-instruct abstracts; Llama-2-7b base/chat entropy comparison; exploratory preference study with 201 India-based Prolific participants and 1,822 retained ratings; appendix GPT-4o-mini generation; English biomedical scientific abstracts
- **Access limitations:** no paper pages are missing. The supporting repository does not redistribute the full hundreds-of-gigabytes corpora, a complete environment lockfile, or all analysis paths needed for push-button reproduction; the repository is a later revision and its current tree is not assumed to be the exact publication-time environment.

## Summary

Juzek and Ward identify 21 inflected focal words by intersecting statistically increased use in PubMed abstracts from 2020 to 2024 with overuse in paired GPT-3.5-generated abstracts. The paper then tests possible causes through comparison corpora, Llama base/chat entropy, and an exploratory preference experiment. It supports a dated, biomedical-scientific, aggregate vocabulary signal and a transferable research method. It does not validate a three-words-per-paragraph threshold, a generic prose blacklist, a single-document authorship verdict, or a settled RLHF mechanism. The complete paper, arXiv version, and supporting repository are now preserved; the prior record contained only ACL page metadata and the abstract.

## Main insights

- The direct corpus result is a 21-form list: `delves`, `delved`, `delving`, `showcasing`, `delve`, `boasts`, `underscores`, `comprehending`, `intricacies`, `surpassing`, `intricate`, `underscoring`, `garnered`, `showcases`, `emphasizing`, `underscore`, `realm`, `surpasses`, `groundbreaking`, `advancements`, and `aligns`.
- Each focal form met three conditions: a statistically significant 2020-to-2024 PubMed increase, no obvious content or event explanation after author review, and significant overuse in paired GPT-3.5 scientific-abstract generation. The authors do not convert those aggregate conditions into a document-level classifier.
- The 2020-to-2024 PubMed increases range from 266.97% for `aligns` to 6,697.14% for `delves`; the source reports occurrences per million for every form.
- Four comparison corpora and the International Corpus of English do not support simple training-corpus-frequency or one-English-variety explanations, but the source cannot inspect actual proprietary training or fine-tuning data.
- Llama base/chat entropy differences are consistent with fine-tuning or RLHF contributing, but do not isolate focal words, do not test ChatGPT directly, and do not rule out architecture or algorithm effects. Appendix D's Llama 3.1 Base result reverses the paper's usual base-model direction, and 70B models were not tested because of quota limits.
- The preference study's pooled critical-item result is null. Its significant result is confined to the exploratory `delve`-initial subset; the other critical items show a non-significant preference in the opposite direction.
- Forced inclusion of focal words creates a material stimulus confound. The authors specifically note that inserting `surpasses` where no comparison exists can make an abstract worse for semantic reasons.
- GPT-4o-mini preserves the general phenomenon but changes the per-word profile: `boasts` is no longer overused, `delve` is less overused, and `underscore` rises sharply. A 500-abstract role-prompt spot check reports no noticeable role effect.
- Nearly all focal forms were already increasing before ChatGPT. The paper interprets LLMs as possible accelerators of language change, not the sole origin of the vocabulary.
- The current supporting repository reproduces the four Table 1 entropy outputs in its notebook, but it is not a complete reproduction package: full corpora are absent, sampling scripts do not set random seeds, scripts use hard-coded paths, no pinned dependency environment is supplied, and the released frequency script names a 2022 file where the paper describes a 2020 comparison. More materially, `brute_force_div.py` passes word count and total token count to `chi2_contingency` instead of word and non-word counts, and substitutes an occurrences-per-million value as the count for a word absent in 2020. Its significance outputs require independent recomputation. These are reviewer observations about the later repository, not corrections asserted by the paper.

## Evidence and claims to extract

- **Direct source reviewed:** authoritative 15-page ACL proceedings PDF for Anthology ID `2025.coling-main.426`; text-equivalent arXiv v1; the complete 39-file supporting repository at commit `0b7e2ba538bcc51ea538594512ef591ec24a1af1` as supplementary implementation evidence.
- **Method and sample:** PubMed snapshot dated 2024-05-04; more than 5.2 billion inflected-form tokens in 26.7 million abstracts, with trend analysis from 1975 to May 2024; about 7,300 significant 2020-to-2024 increases; authors independently screened candidates until 50 unexplained increases remained; 10,000 random 2020 abstracts produced 9,953 GPT-3.5 summaries and regenerated abstracts; Llama 2 base/chat entropy over the human and generated sets plus Appendix D Llama 3 and 3.1 checks; 200 paired preference stimuli, 30 critical pairs, 30 distractor pairs, 201 recruited India-based participants (140 male and 61 female; mean age 31.3, SD 10.6; self-assessed English proficiency and first languages collected; average compensation $15 per hour), and 1,822 retained ratings.
- **Direct versus cited evidence:** C01-C16 are direct methods, results, examples, nulls, or author-stated limits from this paper. C17 is author interpretation that also relies on cited work about language change, evaluator labour, and model recursion; those upstream claims remain indirect here. C18 is a reviewer comparison of the preserved first-party repository with the paper and is not a paper-reported empirical result.
- **Important limits and counterexamples:** biomedical scientific-abstract scope; GPT-3.5 generation is a simulation, not known assisted abstracts; manual candidate exclusion; per-token rather than lemma list; significance testing is not a document threshold and the released chi-square implementation requires independent recomputation; proprietary training data are unavailable; Llama is a proxy; entropy differences do not isolate focal words; Llama 3.1 Base reverses the usual base-model direction and 70B models were not tested; pooled preference is null; distractors show no side preference; the split analysis is exploratory and underpowered after exclusions; forced-word prompts can damage meaning; GPT-4o-mini directions vary by word; the repository is incomplete for full reproduction.

## Skill-use audit

- **Good use:** use the paper to support source- and date-labelled vocabulary-density research in biomedical scientific abstracts, the exact 21-form candidate list, aggregate trend comparisons, model-version drift, null-result reporting, and H24's register-specific evaluation design.
- **Misuse / overclaim:** do not call one focal word, three focal words in a paragraph, or a project warning an authorship fingerprint. Do not treat the entropy comparison or preference study as proof that RLHF caused the vocabulary profile.
- **Unsupported use:** generic all-genre blacklist; single-document probability; per-paragraph severity threshold; current-model prevalence; non-English transfer; writing-quality score; training-data, architecture, or evaluator-nationality mechanism; proof that removing focal words improves prose.
- **Underused evidence:** the live project does not retain Juzek's complete 21-form list as a distinct source profile, the 2020 and 2024 occurrences-per-million values, the pooled preference null, the opposite-direction non-`delve` result, or the GPT-4o-mini word-level reversals.
- **Patterns left on the table:** model/date metadata for vocabulary lists; distinction between repeated tokens and distinct word types; register-specific baseline comparison; explicit treatment of pre-existing human trends; source-specific nulls and counterexamples; reproducibility metadata for code-backed papers.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`: partly covers 10 of the 21 exact forms through its local vocabulary matcher and fails at three distinct local matches in one paragraph, but the source supplies no three-item paragraph threshold and no `fingerprint` claim.
- `overall-signal-stacking`: the Kobak style list contains 20 of the 21 forms, while `boasts` is surfaced by B2 `no-copula-avoidance`; the aggregate check treats vocabulary as supporting evidence. Juzek does not validate structural stacking or the live score.
- A4 `no-promotional-language`: surfaces `showcasing` and `groundbreaking` in some contexts, but Juzek measures lexical overrepresentation rather than promotional meaning.
- `human-eyes/references/process.md`: its product boundary agrees that findings must not infer authorship.
- `dev/TESTING.md`: its matched-register, candidate-versus-threshold, source-provenance, and complete-Audit distinctions are the right evaluation boundary for any future use of this source.

## Associated hypotheses

- H24 register-specific vocabulary density: directly informed and materially strengthened.
- H25 model-family versus generic-AI residue: informed by the GPT-3.5 versus GPT-4o-mini differences and dated prompts.
- H1 continuous calibrated register-distance score: indirectly informed by occurrences-per-million and register baselines, but the paper does not supply a project calibration curve.
- H3 drop detection framing entirely: informed by the gap between aggregate lexical change and single-document inference.

## Questions / follow-up

- Can a matched biomedical-abstract evaluation reproduce useful separation for the exact 21 forms without the paper's generation simulation becoming the test target?
- Do repeated occurrences, distinct focal forms, or change-from-register-baseline provide the most stable signal after model and public-tell drift?
- Which publication-time repository commit and dependency versions produced the paper's full corpus results? The current repository does not identify them.
- Should the live B1 prose replace the unsupported `three or more ... is a fingerprint` wording before any source-specific list expansion is considered?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | legacy ACL page and abstract capture; no stable identifier recorded | `snapshots/archive/juzek-ward-delve/2026-05-05-799a4a83d4f6.md` | 2026-05-05 | `799a4a83d4f6654b24d371c57250b9bea354514dc4fe55c92ed14eff382f6a33` |
| current | ACL Anthology ID 2025.coling-main.426; arXiv:2412.11385v1; DOI none found | `snapshots/juzek-ward-delve.md` | 2026-07-15 | `3626a29262151e1e4d6003787f447460e35a87e3b2e2101e062c0e4b1d11ae94` |

## Decision history

- The previous card had no claim-keyed user decisions or implementation statuses. Its broad B1 and `overall-signal-stacking` mappings were analysis notes, not approvals. This update replaces them with C01-C18; C04, C09, and C16 have since been ruled, and the remaining recommendations are `pending`.
- C16 rejected 2026-07-18 via DR-126: do not add the four appendix abstracts as dedicated grader fixtures. All four are manipulated GPT-3.5 experimental stimuli, they provide no legitimate-writing control or clear desired output, and this card already preserves the focused current-checker results.
- C04 and C09 rejected 2026-07-18 via DR-127: no B1 wording or threshold change; the pooled and distractor nulls remain source-record context only.

## Project coverage

This is the authoritative review table. C04, C09, and C16 record Mae's rulings; every other recommendation remains pending.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The three-step method yields focal forms that significantly increased in PubMed from 2020 to 2024, lacked an obvious external explanation after author screening, and were significantly overused in paired GPT-3.5 abstracts. | Direct peer-reviewed corpus method; about 7,300 significant increases were screened to 50 unexplained candidates and intersected with generated-text overuse. Manual exclusion and unreported multiplicity handling limit inference. The released `brute_force_div.py` builds chi-square rows from word count and total token count rather than word and non-word counts, and uses an occurrences-per-million value as a count for absent 2020 words, so its significance output does not independently validate the paper. | H24 and `pattern-opportunities.md` are partly covered because they call for register-specific, increasing vocabulary evidence. | The live product does not implement the source's corpus-comparison procedure or distinguish statistical candidate recognition from a document threshold. The released significance calculation requires independent recomputation before product use. | Record the method under H24; test-adapt only after independently recomputing the statistics and then running a matched biomedical-abstract evaluation with multiplicity, sampling, and time controls. | pending | not started |
| C02: The 21 focal forms are `delves`, `delved`, `delving`, `showcasing`, `delve`, `boasts`, `underscores`, `comprehending`, `intricacies`, `surpassing`, `intricate`, `underscoring`, `garnered`, `showcases`, `emphasizing`, `underscore`, `realm`, `surpasses`, `groundbreaking`, `advancements`, and `aligns`. | Direct Table 2 result. Increases range from 266.97% to 6,697.14% in PubMed; the list contains inflected forms rather than lemmata. | B1 is partly covered: focused execution found 10 exact forms through the local matcher; the Kobak aggregate profile contains 20; B2 surfaces `boasts`; A4 surfaces some `showcasing` and `groundbreaking` contexts. | Coverage is fragmented across rules with different meanings. The project does not preserve the complete source-specific list or its opm values, and local B1 misses 11 exact forms as direct vocabulary matches. | Preserve the exact list and opm table as source metadata; do not expand active rules until matched-register evaluation compares benefit and false positives. | pending | not started |
| C03: From 10,000 sampled 2020 PubMed abstracts, a two-stage GPT-3.5-turbo-instruct process produced 9,953 paired generated abstracts of about 200 words. | Direct method. The generation simulates likely 2022-to-early-2024 use by summarizing then regenerating an abstract; 47 items received no response, attributed by the authors to topic sensitivity. | `dev/TESTING.md` is fully covered in requiring explicit generation provenance and matched inputs. | The source's generated condition is not observed AI assistance and is prompt-, model-, and date-specific. | Record the simulation boundary whenever C01-C02 are cited; do not generalize the result to arbitrary assisted prose. | pending | not started |
| C04: The 21 forms are plausible contributors to aggregate recent change in Scientific English, not a validated single-document authorship test. | Direct author conclusion plus scope inference from the study design. Each word passes corpus-level conditions; no classifier threshold, document probability, sensitivity, specificity, or false-positive rate is reported. | The evidence preamble and process product boundary are fully covered because they reject one-word authorship claims. | B1's rendered wording that `three or more in one paragraph is a fingerprint` is stronger than this source supports. | Reword B1's threshold claim as an operational project heuristic unless separate validation supports it; retain the explicit no-authorship boundary. | rejected | not applicable |
| C05: Focal-word frequencies in GPT-3.5 abstracts exceed frequencies in PubMed, arXiv, Leipzig, and Wikipedia comparison corpora, casting doubt on simple initial-training-frequency explanations. | Direct comparison across four corpora, but actual proprietary training data are unavailable and corpus dates/registers differ. This is a null for a simple explanation, not proof about training data. | H24 is partly covered through register and corpus-date metadata. | No live project field separates measured output overuse from mechanism inference. | Record the training-data result as a bounded null; take no product action. | pending | not started |
| C06: International Corpus of English analysis finds no focal-word concentration in one English variety and does not support the proposed Nigerian-English evaluator explanation. | Direct appendix analysis; most ICE subcorpora are only about one million words, and actual evaluator populations are unknown. | The project's non-authorship and bias cautions are partly covered. | The source cannot support demographic writing tells or a nationality mechanism. | Record the null and explicitly do not promote demographic or English-variety patterns. | pending | not started |
| C07: Llama 2 base/chat entropy differs for human and GPT-3.5 abstracts: base 1.616 versus 1.633, chat 1.051 versus 0.886. Appendix D reports Llama 3 Base human/AI 1.862/1.928 and Chat 1.174/1.165, plus Llama 3.1 Base 1.854/1.838 and Chat 1.731/1.653. | Direct model comparisons, with the Llama 2 values reproduced by outputs embedded in the released notebook. Llama 3.1 Base reverses the usual base-model direction. The authors could not test 70B models because of quota limits. The pattern is consistent with fine-tuning or RLHF contributing, but Llama is a ChatGPT proxy and entropy may reflect features other than focal words. | No exact project check; H25 is partly covered as mechanism and model-family context. | The study does not isolate RLHF, focal words, architecture, or algorithms; the released notebook is not a controlled ablation; the model-size boundary is untested. | Record as mechanism hypothesis only; preserve the Llama 3.1 Base counterexample and 70B limit; do not attach the result to user-facing word findings without an ablation. | pending | not started |
| C08: The exploratory preference study recruited 201 India-based Prolific participants and retained 1,822 ratings, including 607 critical ratings averaging 20.2 per critical item. | Direct study method. The sample was 140 male and 61 female, mean age 31.3 (SD 10.6); self-assessed English proficiency and first languages were collected; average compensation was $15 per hour. Attention, speed, and completion exclusions were applied; the exclusion rate was unexpectedly high, and the split analysis fell below the planned sample size. | `dev/TESTING.md` is partly covered in requiring sample and uncertainty reporting. | The live source note currently omits the participant, exclusion, item, compensation, and power boundaries. | Preserve these boundaries with any preference result; take no rule action. | pending | not started |
| C09: Across all critical items, participants slightly preferred no-focal-word abstracts, but the result was not significant at p = 0.174; the distractor intercept was 0.500, indicating no significant side preference. | Direct pooled comparison following the authors' original analysis plan plus the reported distractor null. The paper reports a pre-study power analysis but no preregistration. | Not covered in the live source mapping. | Omitting the pooled and distractor nulls makes the later `delve` subset look more general and the procedure less qualified than it is. | Add both nulls to source guidance; do not claim that focal-word removal improves perceived quality. | rejected | not applicable |
| C10: `delve`-initial items significantly favored no-focal-word versions at p = 0.023, while other items slightly favored focal-word versions non-significantly at p = 0.651; the conditions differed at p = 0.03. | Direct exploratory split after stimulus generation revealed many first-sentence `delve` cases. The authors suspect public awareness, but do not measure that mechanism. | B1 is partly covered for surfacing `delve`; no check distinguishes first-sentence public-tell awareness. | This is not a general preference for plain vocabulary and does not validate a severity threshold. | Record `delve`-initial wariness as dated exploratory context; do not promote a special first-sentence rule without replication. | pending | not started |
| C11: Forced-word generation is confounded; inserting `surpasses` where no comparison exists can make a stimulus worse for semantic rather than lexical reasons. | Direct author limitation and counterexample. The study calls the generation approach suboptimal and asks for a larger follow-up. | The closed-source and preserve-meaning guidance in `process.md` is fully covered. | A word-removal evaluation could reward factual repair rather than lexical improvement if meaning is not controlled. | Require semantic-equivalence and unforced-generation controls in any H24 evaluation. | pending | not started |
| C12: GPT-4o-mini shows a similar overall profile but no longer overuses `boasts`, uses `delve` less, and uses `underscore` much more; 500 abstracts per role prompt show no noticeable role difference. | Direct appendix comparison. GPT-4o-mini abstracts reuse GPT-3.5 summaries, and the authors name intervention, RLHF, and methodology as competing explanations. | H25 is partly covered; source-card metadata supports model and date fields. | The live B1 list and severity are not model-version-specific, and the role result is an informal null without a reported test. | Track model/version/date at the source-list level and treat the role finding as a spot-check null; run current-model evaluation before any active change. | pending | not started |
| C13: Almost all focal forms were already increasing before ChatGPT, so LLMs may accelerate rather than originate lexical change. | Direct trend observation plus author interpretation. It supplies a human look-alike and historical baseline. | H24 is partly covered by time-sensitive evidence language. | A flat blacklist obscures pre-existing human trends and feedback loops. | Make pre-2023 trend and corpus-date context mandatory for any source-specific vocabulary profile. | pending | not started |
| C14: The identification method is transferable, but the reported results are bounded to English biomedical scientific abstracts and dated models. | Direct scope statement and future-work limit. The paper proposes other disciplines, domains, languages, and LLMs as untested work. | `dev/TESTING.md` is fully covered in calling for register, genre, model, prompt, and provenance variation. | The 21 forms are not validated across general prose, fiction, journalism, marketing, or non-English text. | Keep the evidence tier register-specific and do not promote generic coverage without new direct sources. | pending | not started |
| C15: Training data, fine-tuning, architecture, algorithms, context priming, RLHF, and other settings are non-exclusive possible causes, while model secrecy blocks direct discrimination. | Direct framework and limitation. The paper reports negative or mixed indirect probes, not a settled causal model. | No project rule needs a mechanism; the process boundary is fully covered. | Existing prose that says words appear more because of a specific mechanism would overclaim. | Keep mechanism fields separate from measured lexical results; take no product action. | pending | not started |
| C16: Appendix examples contrast focal-word and no-focal-word abstracts; the focal versions often contain clusters and sometimes unsupported inflation, but they are generated experimental stimuli. | Direct examples, not prevalence samples. Focused live execution on the complete focal excerpts found the `delve`-initial excerpt below B1 and aggregate thresholds despite nine Kobak style types, while the non-`delve` excerpt triggered B1 through `intricate`, `showcase`, and `highlight the potential` and scored 2/4 on `overall-signal-stacking`. Neither excerpt triggered A4 or B2. | B1 is partly covered and `overall-signal-stacking` is partly covered. | Current outcomes depend on distinct-type lists, paragraph boundaries, overlapping phrase entries, and unrelated semantics rather than the paper's corpus method. | Do not add dedicated grader fixtures for these manipulated stimuli; retain the focused outputs in this source record only. | rejected | not applicable |
| C17: The paper interprets lexical overrepresentation as part of language change and speculates that rushed evaluator labour and form-as-quality heuristics could shape RLHF. | Author interpretation combined with cited labour and language-change sources; the paper does not observe RLHF workers or establish the labour mechanism. | No direct project coverage is needed. | These claims are social and causal context, not prose-pattern evidence. | Record as indirect context and require direct review of cited labour sources before any policy or mechanism claim. | pending | not started |
| C18: The supporting repository preserves code, notebook outputs, filtered ratings, items, and small samples, but not a complete paper environment or full corpora. | Reviewer inspection of all 39 tracked files at current commit. The repository is post-publication, reports AI-assisted polishing/refactoring, has no dependency lockfile or fixed random seeds, and contains a 2022-versus-2020 path discrepancy in `brute_force_div.py`. Its chi-square code uses word and total-token counts rather than word and non-word counts, and substitutes an occurrences-per-million value for an absent-word count. | The source-ingest provenance fields are fully covered by the refreshed snapshot and attachments. | Current repository success cannot be presented as a full independent reproduction; the publication-time code revision is unidentified; the significance results need independent recomputation. | Preserve the repository as supplementary provenance, label the reproduction and statistical-code limits, independently recompute before product use, and request no product change. | pending | not started |

## Recommendations

- C01: Record the three-step method under H24; test-adapt only after independently recomputing its significance results and then running a matched biomedical-abstract evaluation with multiplicity, sampling, and time controls.
- C02: Preserve the exact 21-form list and opm table as source metadata; do not expand active rules before matched-register false-positive evaluation.
- C03: Keep the GPT-3.5 simulation boundary attached to all uses of the focal-word result.
- C04: No B1 wording, threshold, or severity change from DR-127.
- C05: Record the initial-training-frequency null without converting it into a training-data conclusion.
- C06: Record the English-variety null and do not promote demographic patterns.
- C07: Keep RLHF as a mechanism hypothesis only; preserve the Llama 3.1 Base counterexample and untested 70B boundary.
- C08: Preserve participant, demographic, compensation, exclusion, item, and power boundaries.
- C09: Keep the pooled preference and distractor-side nulls in this source record; no product change.
- C10: Record `delve`-initial wariness as dated exploratory context only.
- C11: Require semantic-equivalence and unforced-generation controls in future tests.
- C12: Track model/version/date and retest current models before rule changes.
- C13: Require pre-2023 trend context for source-specific vocabulary profiles.
- C14: Keep the evidence register-specific.
- C15: Keep mechanism claims separate from measured lexical results.
- C16: Do not add dedicated grader fixtures; retain the focused appendix results in this source record only.
- C17: Keep labour and language-change claims indirect until their cited sources receive direct review.
- C18: Treat the code archive as supplementary provenance, not a reproduced result, and independently recompute the significance statistics before product use.

## Evaluation of approved changes

- C01: not applicable - pending recommendation; no product change requested.
- C02: not applicable - pending recommendation; no product change requested.
- C03: not applicable - pending recommendation; no product change requested.
- C04: not applicable - rejected via DR-127; B1 wording, threshold, and severity remain unchanged.
- C05: not applicable - pending recommendation; no product change requested.
- C06: not applicable - pending recommendation; no product change requested.
- C07: not applicable - pending recommendation; no product change requested.
- C08: not applicable - pending recommendation; no product change requested.
- C09: not applicable - rejected via DR-127; both nulls remain preserved in this source record with no product change.
- C10: not applicable - pending recommendation; no product change requested.
- C11: not applicable - pending recommendation; no product change requested.
- C12: not applicable - pending recommendation; no product change requested.
- C13: not applicable - pending recommendation; no product change requested.
- C14: not applicable - pending recommendation; no product change requested.
- C15: not applicable - pending recommendation; no product change requested.
- C16: not applicable - rejected 2026-07-18; no fixtures or product change made.
- C17: not applicable - pending recommendation; no product change requested.
- C18: not applicable - pending recommendation; no product change requested.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/juzek_ward_reviewer
- **Findings resolved:** 5 initial findings resolved: chi-square implementation defect added to C01/C18; Appendix D Llama 3/3.1 values, reversal, and 70B limit added to C07; unreported preregistration implication removed from C09; focused Appendix C coverage corrected in C16; participant boundaries and distractor null added to C08-C09. The same reviewer completed a focused recheck with 0 residual findings.
- **Unresolved findings:** none
