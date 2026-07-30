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
