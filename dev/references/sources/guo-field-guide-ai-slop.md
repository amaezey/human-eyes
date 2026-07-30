# Charlie Guo: The Field Guide to AI Slop

## Metadata

- **URL:** https://www.ignorance.ai/p/the-field-guide-to-ai-slop
- **Author / owner:** Charlie Guo
- **Published:** 2025-10-22T14:02:46.371Z
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** Practitioner essay and field guide
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Substack post 176806840
- **Version / revision:** publisher `updated_at` 2025-10-22T14:05:50.030Z; prior reviewed capture extracted 2026-05-05 with no stable identifier recorded
- **Full-text status:** complete
- **Snapshot:** `snapshots/guo-field-guide-ai-slop.md`
- **Extraction method:** Canonical HTML and public Substack post JSON API fetched with `curl`; first-party `body_html` converted to Markdown with Python 3 and BeautifulSoup 4; all six original images downloaded and visually checked; three content-bearing images transcribed; current Jina Reader extraction used as a text cross-check
- **Snapshot SHA-256:** `258d51d673320ec94c6768983d3714a56c6c5e7a3f8a4015e3adceace2717497`
- **Model / corpus scope:** Dated English-language practitioner observations about ChatGPT, Claude, Gemini, GPT-4o, and GPT-5 across social posts, blogs, long-form articles, workplace messages, professional lists, and creative writing; four source-supplied ChatGPT metaphor examples and one source-labelled AI ukulele example have no prompt, model version, generation date, or comparison sample; the cited Reddit chart covers selected top-post self-text from six technology/startup subreddits rather than a matched human/AI corpus
- **Access limitations:** None for the direct source. The article supplies no raw generation records, detector outputs, authorship labels, systematic human comparison, or data behind most practitioner observations. Its linked Graphite, Originality, Slack, AP-NORC, MIT, Gary Provost, Churchill, and New Yorker materials remain indirect evidence here. The linked em-dash repository was inspected only to verify its implementation and limits; it is not recursively ingested by this record.

## Summary

Guo's dated practitioner field guide names red herrings, stylistic tics, structural patterns, content problems, human look-alikes, detector harms, and an authenticity feedback loop. Its direct evidence is an unlabelled illustrative ukulele passage, four unscoped ChatGPT metaphor examples, the author's repeated observations and personal AI-assisted writing practice, plus two reproduced charts and several cited reports. The complete refresh restores 13 headings and the fifth footnote omitted by the prior Jina snapshot, preserves all six images and first-party source files, and checks the linked em-dash implementation. The source is useful for craft prompts, exact examples, coverage challenges, and false-positive disambiguation; it does not validate prevalence, causality, thresholds, model attribution, detector performance, or document authorship.

## Main insights

- Guo explicitly separates three “yellow flags” from stronger intuitions: academic vocabulary, polished spelling/grammar, and contraction avoidance all have ordinary professional, editing-tool, or second-language explanations.
- The named style and formatting families are em dashes, repeated parallelism, triads, abrupt profundity, mid-paragraph question-answer templates, generic transitions, mechanical bolding, decorative Unicode, excessive lists, and emoji-led professional lists.
- The named rhythm and content families are similar sentence lengths, repeated paragraph cadence, stable tense or point of view, generic metaphors, incoherent throughlines, semantic padding, and polished prose with little underneath.
- Guo repeatedly qualifies the catalogue: one occurrence can be legitimate, human writers use all of these devices, intention and repetition matter, model and prompt effects drift, and even a text with all the tells can be human-written.
- The source's reproduced Reddit chart is weaker than its prose implies. The linked repository warns of top-post time bias; the implementation drops empty/removed self-text, groups by month, plots two-month rolling means, excludes January 2025, and displays May-December 2024 rather than a full plotted year. It measures U+2014 occurrence, not AI use or authorship.
- The categorical detector claims and broad training/RLHF explanations are cited, speculative, or interpretive rather than demonstrated in the article. The model-specific emoji comparison is explicitly anecdotal and system-prompt-confounded.
- The strongest non-pattern contribution is the authenticity warning: fear of accusation can cause human writers to suppress legitimate style. Guo's preferred response is specificity, particular knowledge, tangible experience, voice, and point of view, not detector-directed camouflage.

## Evidence and claims to extract

- **Direct source reviewed:** Complete first-party Substack post 176806840, publisher `updated_at` 2025-10-22T14:05:50.030Z, including 50 root article paragraphs, a five-paragraph block quotation, two lists with eight items, 13 headings, six figures, four captions, 28 links, and five footnotes. The canonical HTML, JSON API record, six original images, current Jina output, and the linked em-dash repository implementation at commit `e40a2fbcfdfb82c9f7fcc21d373405972bcecb6f` were checked.
- **Method and sample:** Practitioner observation with an unreported observation count and no controlled comparison; one source-labelled AI ukulele passage of unspecified provenance; four ChatGPT metaphor outputs with no prompt or model version; one reproduced Graphite/Axios chart; one linked Reddit analysis whose six displayed subreddits contain 489-965 retained top-post self-text records across nine stored months, with only May-December 2024 plotted after January 2025 exclusion. Platform scope is English-language web, workplace, social, professional, and creative-writing contexts.
- **Direct versus cited evidence:** C01, C03-C07, C09-C24, and C27-C30 are direct examples, observations, interpretation, or personal disclosure in Guo's post. C02, C08, C25, and parts of C26 inherit claims from charts, reports, or links; the em-dash code and CSV were inspected, while the other cited materials remain indirect and unresolved for promotion. No claim is a controlled measurement performed by Guo.
- **Important limits and counterexamples:** No ground-truth authorship validation, prevalence estimate, threshold, matched human sample, uncertainty, prompt record, generation record, model-version control, genre control, or longitudinal replication is supplied. Guo provides strong human look-alikes and ends with an explicit non-authorship warning. The article's own em-dash chart description compresses an eight-month displayed range into “over a year,” and the source calls polished emptiness an AI “signature” before acknowledging human weak writing and rejecting conclusive inference.

## Matched patterns / rules

- B1 `no-ai-vocabulary-clustering`, with register and single-word cautions
- B3 `no-negative-parallelisms`
- B4 `no-forced-triads`
- C1 `no-boldface-overuse`
- E1 `no-filler-phrases`, partial lexical coverage only
- G1 `no-rhetorical-questions`
- G2 `generic_metaphors` agent assessment
- G3 `no-excessive-lists`
- G4 `no-unicode-flair`
- G5 `no-dramatic-transitions`
- H3 `tonal_uniformity` and `structural_monotony` agent assessments, adjacent rather than exact
- H10 `genre_specific` fiction and marketing/email branches, adjacent rather than exact
- G7 `no-manufactured-insight`, exact documented candidate with a straight-versus-curly apostrophe implementation gap
- C7 `no-em-dashes`, challenged by the source's occurrence-versus-density and human-use cautions
- G9 `sentence-length-variance` and `paragraph-length-uniformity`
- `formulaic_parallelism`, `semantic_redundancy`, `underspecified_language`, and `faux_specificity` agent assessments
- `overall-signal-stacking` and the project-wide no-authorship boundary

## Associated hypotheses

- H3 drop detection framing entirely
- H4 single-source registry and traceable source attribution
- H9 field-guide voice with similar-species disambiguation per pattern
- H10 user-reported false-positive intake
- H11 manufactured insight is register-coded in long-form essay
- H12 genre-aware threshold calibration
- H21 low information density and wrong sentence subject
- H22 long-tail compression and grammatical standardisation
- H24 register-specific vocabulary density
- H25 model-family versus generic-AI residue
