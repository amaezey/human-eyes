# Walsh, Preus, and Gronski: Does ChatGPT Have a Poetic Style?

## Metadata

- **URL:** https://arxiv.org/abs/2410.15299
- **Author / owner:** Melanie Walsh, Anna Preus, and Elizabeth Gronski
- **Published:** submitted 2024-10-20; arXiv v2 revised 2024-10-30; presented at CHR 2024, held 2024-12-04 through 2024-12-06
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** peer-reviewed conference paper with an associated code repository
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** update
- **Stable identifier:** arXiv:2410.15299v2; DOI 10.48550/arXiv.2410.15299
- **Version / revision:** complete arXiv v2 paper, revised 2024-10-30, plus associated three-file code repository at paper-era commit `c378f2472d3bcb2fd440b030284dd942dbc86e04`; prior capture was the arXiv v2 abstract page retrieved 2026-05-05
- **Full-text status:** complete
- **Snapshot:** `snapshots/walsh-ai-poetry.md`
- **Extraction method:** official arXiv v2 PDF download; Poppler `pdftotext -layout`; PDF metadata and rendered-page checks; experimental arXiv HTML cross-check; GitHub recursive-tree inspection and commit-pinned tarball preservation
- **Snapshot SHA-256:** `f783fb8fbc97d72331a465e1ae70f4e224cfa3cc2a46dd641eda07619d3ac49f`
- **Model / corpus scope:** 2,880 English poems from the moving API alias `gpt-3.5-turbo` and 2,880 from `gpt-4`, generated zero-shot across 24 form/style labels, 40 subject labels, and three prompt templates, compared with 3,874 poem/form pairs representing 3,692 unique human poems from the Poetry Foundation and Academy of American Poets; exact API model snapshots, generation dates, sampling settings, and complete generated corpus were not released
- **Access limitations:** none for the 20-page paper, five tables, eight figures, notes, references, and complete three-file code repository at the reviewed commit. The generated-poetry corpus was promised for later release but is absent, the human corpus is linked to a separate prior-work repository rather than packaged here, and the released code has no locked environment or complete reproducible run path.

## Summary

This CHR 2024 paper compares 5,760 zero-shot GPT-3.5/GPT-4 English poems with 3,692 unique poems from two curated poetry sites. It measures form length, stanza structure, pronouns, distinctive words, rhyme, and meter, and reports a dated poetry-specific pattern: the model outputs are more regular than the selected human corpus, with heavy quatrain and rhyme use, first-person-plural concentration, distinctive openings, and model-specific vocabulary. Its strongest human-eyes contribution is bounded evidence for the poetry branch of H10 and for genre-, model-, prompt-, and corpus-aware evaluation. It does not validate a prose rule, a current-model claim, a quality verdict, a single-poem authorship inference, or the live F1 spectral-word threshold.

## Main insights

- The study uses 2,880 poems per GPT model across 24 styles, 40 subjects, and three zero-shot prompt templates, compared with 3,874 poem/form pairs representing 3,692 unique human poems.
- For fixed-length human forms within ten lines of the convention, the authors manually removed prefatory dedications, dates, epigraphs, and similar material. They retained prefatory text elsewhere and judged qualitatively that it was not extensive. This asymmetric preprocessing can affect human line, stanza, and form comparisons.
- GPT-4 adhered more consistently than GPT-3.5 to conventional sonnet, villanelle, and sestina lengths; some human poems deliberately exceeded those lengths through formal play or multiple forms.
- Both model groups produced median 25-line limericks instead of a conventional five-line unit, usually by concatenating multiple limericks. The authors interpret this as knowing the form but not when to stop.
- A generic `a poem` prompt produced a 36-line median in both model groups, and the overall median across styles was 32 lines.
- Quatrains made up 66.8% of GPT-3.5 stanzas and 59.6% of GPT-4 stanzas, versus 16.7% of the selected human stanzas; 70.4%, 63.3%, and 18.4% of poems respectively contained at least one quatrain.
- First-person plural pronouns were more frequent and first-person singular pronouns less frequent in model poems. Removing holiday and occasion prompts reduced the plural difference only slightly. The paper's inclusivity and no-first-person-experience explanations are hypotheses, not tested mechanisms.
- `In` was the most distinctive first word for both model corpora. `Upon` was next for GPT-4, with `beneath`, `behold`, and `within` also associated with its iambic openings. The paper shows ranks but not the Z-scores or per-word rates.
- GPT-3.5 vocabulary clustered around `embrace`, `grace`, `dance`, and `dreams`; at least one appeared in 87% of its poems. Either `echo` or `whisper` appeared in 75% of GPT-4 poems. The corpus needed to reproduce these percentages is unavailable. The released notebook instead runs a case-sensitive substring query for `echo|whisper|dance|dream|embrace` and reports 91.5625% for GPT-3.5, 86.8403% for GPT-4, and a substantial 25.1936% human look-alike rate.
- Quantitative rhyme analysis found at least one selected end-rhyme pattern in 90.2% of GPT-3.5 poems, 89.5% of GPT-4 poems, and 65.0% of human poem/form pairs; mean rhymed-line shares were 63.87%, 65.20%, and 29.45%. Every model sonnet and ballad, and every model aubade and pastoral despite those unfixed forms not requiring rhyme, contained at least one selected end rhyme.
- Manual annotation of 144 poems per model and 138 human poems found end-rhyme patterns in over 80% of sampled model poems versus around 50% of human poems, and dominant iambic meter in over 60% versus just under 40%. The model-specific iambic estimates were about 74% for GPT-3.5 and 53% for GPT-4.
- Rhyme analysis is pronunciation-dependent and counts only AA, ABAB, ABBA, and ABCB patterns through the CMU Pronouncing Dictionary. Meter is harder to label in imperfect model poems. The paper reports no annotator-agreement statistic.
- The default quatrain, iambic, and rhyme combination can survive a conflicting form request; the published limerick example instead has five AABB-rhymed quatrains in mostly iambic meter.
- Prompt construction matters. The authors added figurative and specific templates after observing prompt-word repetition and vagueness, and say unpublished author-name experiments became more complex. They report no template-level causal comparison or author-name results.
- The paper intentionally does not evaluate whether the poems are good or bad. Its claim of less creativity is interpretive and should not be collapsed into its direct structure, frequency, and prosody measurements.
- The human comparison corpus is English-language, selectively tagged, non-representative, American/canonical-prestige weighted, and potentially different from popular, commercial, or colloquial poetry in model training.
- Human prefatory material was removed only for near-conventional fixed-length forms and retained elsewhere, so packaging treatment is not uniform across the human structure baseline.
- The generated corpus is not released, exact API snapshots and settings are absent, and the code package is not end-to-end reproducible. These limits prevent independent recomputation and make the findings dated, model-alias-specific aggregate evidence.

## Evidence and claims to extract

- **Direct source reviewed:** all 20 pages of arXiv:2410.15299v2, including the abstract, six numbered sections, five tables, eight figures and captions, acknowledgments, five notes, and 41 references; the experimental arXiv HTML; and all three files in the associated repository at commit `c378f2472d3bcb2fd440b030284dd942dbc86e04`.
- **Method and sample:** 5,760 generated English poems, split evenly between `gpt-3.5-turbo` and `gpt-4`, with 120 poems per style per model and 72 poems per subject per model. The 24 labels span fixed, unfixed, meter, stanza, and generic-poem prompts. The comparison corpus contains 3,874 poem/form pairs or 3,692 unique Poetry Foundation and Academy of American Poets poems. For human poems in conventionally fixed forms and within ten lines of the expected length, prefatory dedications, dates, epigraphs, and similar text were manually removed; prefatory text remained elsewhere based on a qualitative judgment that it was not extensive. Direct analyses cover line/stanza parsing, normalized pronouns, weighted log-odds with a minimum of ten poems, a CMU-dictionary rhyme procedure, and manual prosody annotation of 426 poems.
- **Direct versus cited evidence:** C01-C15 and C17-C18 record this paper's design, direct measurements, examples, author interpretations, release state, and limitations. C16 records memorization and training-data context inherited from prior work, including the cited 41% estimate; it is not direct evidence from this experiment. The paper's alignment with prior under-diversity and biomedical-vocabulary studies is also cited context rather than a result measured here.
- **Important limits and counterexamples:** selected non-representative human corpora; asymmetric human prefatory-text removal that can affect line, stanza, and form comparisons; English poetry only; moving API aliases with no snapshot IDs, dates, temperature, seed, or other settings; no released generated corpus; no significance intervals or tests presented for the main descriptive differences; no annotator-agreement statistic; pronunciation and rhyme-scheme restrictions; first-word ranks without numeric scores; strict human formal-play counterexamples; GPT-4's lower manual iambic estimate; the holiday/occasion control that only slightly reduces first-person-plural use; a 25.1936% human rate in the notebook's broader five-word substring query; prompt sensitivity; an inconclusive memorization effect; no direct quality evaluation; and no basis for single-poem authorship inference.

## Skill-use audit

- **Good use:** support a poetry-only manual review of default quatrains, unrequested/high-density rhyme, first-person-plural clustering, strict form compliance, repeated full-form units, distinctive openings, and dated vocabulary clusters; support H12/H24/H25 evaluation design and explicit model, prompt, genre, and corpus metadata.
- **Misuse / overclaim:** turning aggregate corpus differences into a single-poem verdict, current-model claim, quality score, universal poetry rule, global prose rule, causal training/alignment mechanism, or claim that formal compliance is intrinsically bad.
- **Unsupported use:** the live F1 three-count threshold, substring and inflection double-counting, `mood-word accumulation without concrete perception`, process-trace or revision-depth claims, exact current `gpt-4` or `gpt-3.5-turbo` behaviour, author imitation, a memorization effect, or an authorship classifier.
- **Underused evidence:** exact quatrain and rhyme baselines; human formal-play counterexamples; the long-limerick multiple-unit failure; first-word candidates; the holiday/occasion pronoun control; GPT-4's lower iambic estimate; measurement limits; prompt sensitivity; and code/data reproducibility gaps.
- **Patterns left on the table:** repeated complete-form units and stopping failure, poetry-specific opening-word distributions, and form-sensitive regularity could be evaluated as agent-assessment prompts. None is ready for a deterministic rule or threshold without released data and matched, dated controls.

## Matched patterns / rules

- H10 `genre_specific` in `human-eyes/scripts/judgement.json`: the poetry branch directly names default quatrains, unrequested/high-density rhyme, first-person-plural clustering, mood-word accumulation, and form compliance. It covers the core families but omits the source's model/date scope, human baselines, formal-play counterexamples, long-limerick repetition, prompt control, and measurement limits. Its `without concrete perception`, process-trace, surprise, breakage, and revision-depth wording is not supported by this paper.
- F1 `no-ghost-spectral-density` in `human-eyes/scripts/grade.py` and `human-eyes/scripts/patterns.json`: adjacent only to `echo` and `whisper`. A focused surface-only run on `In the echoes, whispers rise.` flags four words because singular and plural substrings are double-counted. A second run on the paper's published four-line `echoing hallways` and `whisperer` example remains clear with `Ghost/spectral words: 2`. The paper reports corpus-level word presence, not atmospheric function or a three-count threshold, so C08 challenges using Walsh as support for this check.
- H12 `Genre-aware threshold calibration`: directly informed by the poetry-only register, form-conditioned results, selected human comparison, and deliberate formal counterexamples.
- H24 `Register-specific vocabulary density`: directly informed by dated poetry-only word distributions, while the unavailable corpus and absent exact scores block promotion.
- H25 `Model-family versus generic-AI residue`: directly informed by GPT-3.5/GPT-4 differences, moving aliases, missing snapshot IDs, and prompt sensitivity.
- `human-eyes/references/process.md`: the closed-source, genre-preservation, deliberate-device, and no-authorship boundaries are consistent with this source's aggregate design and limits.

## Associated hypotheses

- H12: Genre-aware threshold calibration.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.
- H22: Long-tail compression and grammatical standardisation, adjacent only; the paper measures poetic regularity and variation, not the prose syntactic features proposed by H22.

## Questions / follow-up

- Can the authors release the 5,760 generated poems, exact generation timestamps and API model snapshot IDs, generation settings, cleaned analysis inputs, environment lockfile, manual prosody labels, and per-word score tables?
- Should Mae retain H10's source-supported five poetry prompts while separating them from unsupported `without concrete perception`, process-trace, surprise, breakage, and revision-depth wording?
- Should Mae approve a source-bound correction/evaluation for F1's substring double-counting and poetry controls before any claim that `echo` or `whisper` supports that deterministic check?
- Should repeated complete-form units and form-conditioned opening distributions enter a matched poetry evaluation, with deliberate formal play and human rhyme as controls, before any product change?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | arXiv:2410.15299v2 abstract-page capture | `snapshots/archive/walsh-ai-poetry/2026-05-05-9c90a78d.md` | 2026-05-05 | `9c90a78d87cf0397dfe21a1dfa66cd2eb676d7a5cb8c822db5f577e011ffed2b` |
| current | arXiv:2410.15299v2; DOI 10.48550/arXiv.2410.15299 | `snapshots/walsh-ai-poetry.md` | 2026-07-17 | `f783fb8fbc97d72331a465e1ae70f4e224cfa3cc2a46dd641eda07619d3ac49f` |

The pre-contract card and manifest did not record a digest for the previous snapshot. Its current on-disk SHA-256 matches the `HEAD` Git blob byte-for-byte, and the exact bytes were archived before replacement. The source revision remains arXiv v2; the update replaces an abstract-page capture with the complete paper and paper-era code, and adds reproducibility, measurement, counterexample, and project-coverage analysis rather than claiming a new paper revision.

## Decision history

- The 2026-05-05 pre-contract card had no stable claim IDs, user-decision states, implementation statuses, evaluation records, snapshot digest, or independent source-record review. It broadly mapped the source to H10, H12, and poetry-only rhyme, quatrain, first-person-plural, and vocabulary prompts. Those useful mappings are reopened and qualified as C01-C18. No prior approved or implemented decision exists to preserve or retire.
- The previous card correctly warned against prose generalization and treating `echo` or `whisper` as standalone support for F1. C08 retains and deepens that boundary with a live-code inspection and focused surface-only result.
- C08 approved 2026-07-17: F1 token-boundary counting fix. Implemented in commit 13e235f. All other rows remain pending.
- C02, C03, C07, C10, C14 approved 2026-07-17 (DR-112): Mae narrowed the H10 poetry watchlist to what this study measured, quatrain/rhyme density, strict form compliance, repeated complete-form units, first-person-plural clustering, opening-word distributions, and vocabulary clusters. Implemented in commit b020a61 (`human-eyes/scripts/judgement.json`).

## Project coverage

This is the authoritative review table. Every recommendation remains pending for Mae; no product files changed in this review.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: The experiment compares 2,880 poems per model across 24 styles, 40 subjects, and three zero-shot templates with 3,874 human poem/form pairs representing 3,692 unique poems. | Direct paper and released notebook design; English poetry; selected site corpora; moving API aliases and exact run settings absent. Near-conventional fixed-form human poems had prefatory text removed, while other human poems retained it. | H12 and H10 are genre-aware; partly covered as scope context, not as an executable corpus comparison. | Project source summaries do not preserve the exact pair-versus-unique accounting, prompts, preprocessing asymmetry, or model-setting gaps. | Record the exact design and provenance only; verify metadata/card and snapshot. | pending | not started |
| C02: GPT-4 follows conventional sonnet, villanelle, and sestina lengths more consistently than GPT-3.5, while some human poems deliberately exceed the convention. | Direct line-count distributions and qualitative human counterexamples; fixed-form human prefatory text was removed only within ten lines of conventional length; no claim that strict compliance is universally bad. | H10 poetry says `form compliance without surprise, breakage, or revision depth`; partly covered. | The live wording adds normative qualities the paper did not measure and omits preprocessing, deliberate human multiples, and formal play. | Evaluate and, if approved, narrow H10 to form compliance without pressure plus deliberate-form controls; no deterministic rule. | approved | implemented |
| C03: Both model groups have a 25-line median for limerick prompts because they often concatenate multiple five-line limericks; the authors interpret this as not knowing when to stop. | Direct model length distribution and inspection; the stopping explanation is author interpretation. Human limerick packaging may have been trimmed under the near-conventional fixed-form rule. | H10 catches rhyme and regular-stanza families; partly covered. | No prompt covers repeated complete-form units or separates deliberate sequence poems from unwanted continuation; human preprocessing is not surfaced. | Add a matched poetry-evaluation candidate for repeated full-form units with deliberate-sequence controls before any assessment change. | approved | implemented |
| C04: Generic `a poem` prompts have a 36-line median in both model groups, and the overall median across styles is 32 lines. | Direct model descriptive result; the human `a poem` comparator is an aggregation, not a prompt-equivalent group, and non-fixed human prefatory text generally remained. | No exact check or assessment; not covered. | A length threshold would confound prompt, form, packaging, and deliberate long poems. | Record only; take no product action without matched form- and prompt-conditioned distributions. | pending | not started |
| C05: Quatrains account for 66.8% of GPT-3.5 stanzas, 59.6% of GPT-4 stanzas, and 16.7% of human stanzas; poem-level rates are 70.4%, 63.3%, and 18.4%. | Direct Table 3 counts across the study corpora; aggregate, dated, and corpus-dependent. Asymmetric human prefatory-text removal can affect stanza counts. | H10 directly names default quatrains; partly covered. | The assessment lacks preprocessing, quantitative source context, model/date metadata, form conditioning, and deliberate regular-stanza controls. | Retain as a poetry-only manual prompt; add source-bound evidence and matched-control evaluation before any threshold. | pending | not started |
| C06: Model poems use more first-person plural and fewer first-person singular pronouns; removing holiday/occasion prompts only slightly reduces the plural difference. | Direct normalized corpus comparison and control; plotted magnitudes are visually estimable but not numerically labelled or tabulated, and no inferential test is reported. Inclusivity and no-lived-experience explanations are speculative. | H10 names first-person-plural clustering; partly covered. | It lacks subject-prompt controls, a density definition, singular comparison, and explicit rejection of the proposed mechanisms. | Retain as a clustering prompt with subject, density, genre, and human-look-alike controls; do not promote the mechanism. | pending | not started |
| C07: `In` is the most distinctive first word for both model corpora; GPT-4 also favors iambic `Upon`, `beneath`, `behold`, and `within`, while human first words show no analogous distinctive pattern and are mostly articles and pronouns. | Direct weighted-log-odds ranks with minimum ten-poem vocabulary; no published Z-scores or per-word counts; the human result is the source's comparison control. | Exact code and catalogues contain none of these openings; not covered. | No matched current-model replication, and a flat opener blacklist would overreach despite the source's human comparison. | Preserve as a dated poetry evaluation candidate only; require released counts and matched controls before adoption. | approved | implemented |
| C08: At least one of `embrace`, `grace`, `dance`, or `dreams` occurs in 87% of GPT-3.5 poems; `echo` or `whisper` occurs in 75% of GPT-4 poems. | Direct paper report; corpus unavailable. The notebook instead uses case-sensitive substring query `echo\|whisper\|dance\|dream\|embrace` and reports 91.5625% GPT-3.5, 86.8403% GPT-4, and 25.1936% human, so it does not reproduce the token sets or exact figures. | H10 mood-word accumulation is adjacent; F1 checks spectral substrings. A synthetic two-inflected-token run is flagged as four, while the paper's four-line `echoing`/`whisperer` example remains clear at two; challenges current behaviour. | The paper does not measure `without concrete perception`, atmospheric function, a three-count threshold, or single-poem specificity. F1 double-counts singular/plural substrings and the source example stays below its threshold. | Do not promote a flat list. Pending Mae approval, evaluate/correct F1 token boundaries and deduplication and add poetry/register controls; keep Walsh under H10/H24 only. | approved | implemented |
| C09: Prosody measurement is pronunciation- and context-dependent, and model meter can be imprecise or resist one label. | Direct method limitation; selected CMU pronunciations and expert manual annotation. | H10 names rhyme but not measurement validity; partly covered. | Current guidance does not state dialect, pronunciation, imperfect-meter, or annotation uncertainty controls. | Require these controls in any poetry rhyme/meter evaluation; no checker threshold from this source. | pending | not started |
| C10: In the manual sample, over 80% of model poems versus around 50% of human poems rhyme, and over 60% versus just under 40% have dominant iambic meter; GPT-4 is about 53% versus GPT-3.5 about 74%. | Direct expert annotations of 144 poems per model and 138 human poems; no agreement statistic or uncertainty interval. | H10 covers unrequested rhyme but not iambic meter explicitly; partly covered. | No model-specific source note, annotation reliability, form conditioning, or current replication. | Record as bounded manual evidence and evaluate with blinded multi-annotator, form-matched samples before changing H10. | approved | implemented |
| C11: Selected end-rhyme patterns occur in 90.2% of GPT-3.5, 89.5% of GPT-4, and 65.0% of human poem/form pairs; mean rhymed-line shares are 63.87%, 65.20%, and 29.45%. Every model sonnet, ballad, aubade, and pastoral has at least one selected end rhyme. | Direct Table 5, form-conditioned result, and released code for AA, ABAB, ABBA, and ABCB schemes; CMU-dictionary and repeated-word method limits apply. Aubade and pastoral are unfixed forms that do not require rhyme. | H10 names unrequested rhyme or high rhyme density; partly covered. | No live density definition, scheme/form control, repeated-word handling, dialect control, or threshold evaluation. | Use the study to design a matched poetry rhyme-density evaluation; do not import its aggregate or form rates as document thresholds. | pending | not started |
| C12: A GPT-4 limerick prompt yields five mostly iambic AABB quatrains, showing the source's default mode can survive a conflicting form request. | Direct published example and author annotation; selected example, not a prevalence estimate beyond aggregate companion results. | H10 covers quatrains, rhyme, and form compliance; partly covered. | The live branch does not distinguish a bounded example from an authorship or quality conclusion. | Retain as a source-attributed example for evaluation only, with human formal-play and intentional-rule-breaking controls. | pending | not started |
| C13: Prompt wording materially shapes outputs; figurative and specific templates were added after observed repetition/vagueness, and author-name prompts reportedly shifted results. | Direct design rationale and author observation; no template-level causal estimates or author-name results. | H12/H25 recognize prompt and model variation; partly covered. | H10's process/revision wording is unrelated, and the paper does not validate a repetition or vagueness threshold. | Record prompt construction as a required evaluation variable; take no prose-pattern action from the unpublished observation. | pending | not started |
| C14: The study does not evaluate good/bad poetry; its broad creativity language goes beyond the measured regularity, frequency, and prosody features. | Explicit scope statement plus author interpretation; no human quality ratings. | `process.md` preserves genre and forbids authorship statements; partly covered. | Source summaries can still blur regularity with inferiority, creativity, or origin. | Add explicit non-quality and non-authorship boundaries to source/index summaries; no score or rule change. | approved | implemented |
| C15: The human corpus is English-only, selectively tagged, non-representative, American/canonical-prestige weighted, and may differ from popular/commercial model poetry. | Direct limitations and author interpretation; no representative target population is defined. | H12 covers register calibration; partly covered. | Current H10 wording does not name comparison-corpus selection, era, institution, prestige, or form distribution. | Require matched genre, form, era, length, institution, and prompt controls in any adoption evaluation. | pending | not started |
| C16: The paper cites prior work estimating 41% likely GPT-4 memorization in the human sample and says any effect on form classification is inconclusive. | Indirect cited result from Walsh, Preus, and Antoniak; not tested here and no generation effect established. | No direct project conclusion from this card; not covered as evidence. | Using the 41% figure would require direct review of the cited paper and would still not establish generation causality. | Record as indirect and unresolved; do not promote without a separate source ingestion/direct review. | pending | not started |
| C17: The generated corpus is unreleased and the code package lacks a locked, complete reproduction path; exact published vocabulary results cannot be recomputed. | Direct release statements plus complete three-file repository inspection at the paper-era commit. | Source-ingest provenance process covers access limits; fully covered as recordkeeping. | The prior card called the abstract sufficient and omitted reproducibility defects. | Preserve PDF, code, tree, hashes, and exact limits; take no product action. | pending | not started |
| C18: Findings are bounded to dated GPT-3.5/GPT-4 aliases, zero-shot English poetry, selected prompts, and selected human sites; exact snapshots/settings are unknown. | Direct paper and code scope; high version and prompt drift risk. | H12, H24, and H25 cover genre, vocabulary, and model-specific evidence; partly covered. | Root/source summaries do not currently state the dated-alias and no-current-model boundary. | Update source summaries with the scope and require model snapshot/date/prompt metadata in future evaluation; no general prose or authorship inference. Rejected 2026-07-26 (DR-110): no mandatory model, version and date field was added for imported dated examples. | rejected | not applicable |

## Recommendations

- C01: Record the exact design and provenance only.
- C02: Evaluate and, if approved, narrow H10's form-compliance wording to the source-supported construction with deliberate-form controls.
- C03: Test repeated complete-form units separately from deliberate poetic sequences before changing the assessment.
- C04: Record the length result without adopting a threshold.
- C05: Retain default quatrains as a poetry-only manual prompt and add matched-control evidence before any threshold.
- C06: Retain first-person-plural clustering with density, subject, genre, and human-look-alike controls; reject the untested mechanism.
- C07: Preserve opening-word ranks as a dated evaluation candidate, not a blacklist.
- C08: Keep Walsh out of F1 threshold evidence; pending approval, evaluate and correct substring double-counting and add poetry/register controls.
- C09: Require pronunciation, dialect, context, and annotation-validity controls in prosody evaluation.
- C10: Record the manual prosody result and require a blinded, form-matched replication before changing H10.
- C11: Use the quantitative rhyme result to design evaluation, not a document threshold.
- C12: Retain the limerick as a bounded source example with intentional human controls.
- C13: Treat prompt construction as a required variable and take no pattern action from unpublished observations.
- C14: State explicitly that the source does not establish quality, creativity, or authorship.
- C15: Require matched form, era, length, institution, register, and prompt controls.
- C16: Keep the memorization result indirect until its source is separately reviewed.
- C17: Preserve the reproducibility limits and attachments; no product action.
- C18: Add dated model-alias and no-current-model boundaries to source summaries and future evaluation metadata.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change implemented.
- C02: passed - H10 poetry watchlist wording narrowed to `strict form compliance` in commit b020a61 (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C03: passed - `repeated complete-form units` added to the H10 poetry watchlist in commit b020a61 (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C04: not applicable - recommendation pending; no product change implemented.
- C05: not applicable - recommendation pending; no product change implemented.
- C06: not applicable - recommendation pending; no product change implemented.
- C07: passed - `opening-word distributions skewed to stock openers` added to the H10 poetry watchlist in commit b020a61 (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C08: passed - F1 token-boundary counting fix landed in commit 13e235f (`human-eyes/scripts/grade.py` plus regression tests in `dev/evals/tests/test_grade.py`); `python3 -m unittest dev.evals.tests.test_grade` passes on 2026-07-17.
- C09: not applicable - recommendation pending; no product change implemented.
- C10: passed - H10 poetry watchlist wording covers `default quatrains and rhyme density` in commit b020a61 (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C11: not applicable - recommendation pending; no product change implemented.
- C12: not applicable - recommendation pending; no product change implemented.
- C13: not applicable - recommendation pending; no product change implemented.
- C14: passed - unmeasured normative wording (`without surprise, breakage, or revision depth`, `without concrete perception`, `without a reason`) removed from the H10 poetry watchlist in commit b020a61 (`human-eyes/scripts/judgement.json`); `python3 -m unittest dev.evals.tests.test_judgement_json` passes on 2026-07-17.
- C15: not applicable - recommendation pending; no product change implemented.
- C16: not applicable - recommendation pending; no product change implemented.
- C17: not applicable - recommendation pending; no product change implemented.
- C18: not applicable - ruled 2026-07-26; no product change.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: /root/walsh_source_reviewer; fresh, source-dedicated, strictly read-only five-lens review plus focused re-check
- **Findings resolved:** 7 initial findings: complete commit-pinned access routes; human prefatory-text preprocessing across structural claims and limits; non-numeric Figure 5 wording; human first-word control; exact notebook query semantics and all three rates; both focused F1 surface-only outcomes; and the form-conditioned sonnet, ballad, aubade, and pastoral rhyme result. Focused re-check found 0 remaining findings.
- **Unresolved findings:** none
