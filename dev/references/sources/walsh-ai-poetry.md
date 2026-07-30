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
