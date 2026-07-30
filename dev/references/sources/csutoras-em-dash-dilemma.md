# Brent Csutoras: The em-dash dilemma

## Metadata

- **URL:** https://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559
- **Author / owner:** Brent Csutoras
- **Published:** 2025-04-29T18:45:36Z; page updates dated 2025-08-21, 2025-09-27, and 2026-06-22
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** practitioner observation and commentary
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** Medium post ID `684fbcc9f559`
- **Version / revision:** living Medium post as retrieved 2026-07-15, including the latest displayed update dated 2026-06-22; prior capture retrieved 2026-05-05 and lacking that update
- **Full-text status:** complete
- **Snapshot:** `snapshots/csutoras-em-dash-dilemma.md`
- **Extraction method:** complete current Jina Reader Markdown through both HTTP- and HTTPS-target routes to the canonical Medium page; route responses differ only in the `URL Source:` scheme, and the preserved raw file is the HTTPS-target response
- **Snapshot SHA-256:** `17967a871fb13e078deb6607bddaaec8193dd9182300a3c75afc0b05366ac0fa`
- **Model / corpus scope:** English Medium practitioner essay based on one author's undated experience across unnamed models, prompts, settings, forums, and subreddit moderation; two source screenshots show an explicit no-em-dash instruction and one generated acknowledgement of a violation, but no model, version, product surface, date, generation settings, full output, number of trials, comparison group, or coding method is supplied. A 2025 update names Claude without a model/version and a 2026 screenshot appears to show one Gmail grammar suggestion.
- **Access limitations:** none for the complete current article and four source images. Medium exposed no revision number. Direct HTML, `?format=json`, and `/p/684fbcc9f559` were Cloudflare-blocked, while two current Jina Reader routes agreed on the article body. The LinkedIn post and cited pages are not constituent source text; relevant citation claims were checked only to classify directness and were not recursively ingested.

## Summary

Csutoras describes repeated difficulty suppressing em dashes in generated text, public anxiety about treating the punctuation as an AI sign, and a later three-stage workflow that mechanically replaces dashes with commas. The living page now adds a June 2026 screenshot in which a Gmail grammar popover suggests a pair of em dashes. The source contributes dated practitioner examples of prompt noncompliance, cue evasion, product-surface mediation, and human false positives. It does not supply a model version, trial count, output corpus, human comparison, prevalence measure, validated mechanism, threshold, or authorship test. Its own explicit conclusion is that an em dash is not reliable standalone evidence.

## Main insights

- The source's two original screenshots directly preserve an explicit no-em-dash instruction and one generated response acknowledging that it violated the instruction. That single response fragment also contains `You’re absolutely right`, `I appreciate you doing it`, `honestly:`, and `Want me to...`; it does not identify the model, date, product, or surrounding outputs and cannot establish prevalence.
- The author also says he had removed almost every other “recognizable AI signature” before the em dash persisted. This is an unmeasured self-report, and the source does not name those other cues.
- The author's persistence and training-data explanations are interpretations, not measured model-behaviour or architecture evidence. The cited community pages are user discussions, not official training documentation.
- The article explicitly rejects em dashes as a reliable standalone giveaway and supplies strong human-look-alike context through the cited Night Water writer and a Hacker News thread containing both avoidance and dissent.
- The cited MIT Technology Review article accurately reports Daphne Ippolito's observations about frequent common words, typo scarcity, and human variability, but those are indirect here and do not establish a machine-cleanliness rule in this project.
- The September 2025 update reports a Claude workflow that replaces all em dashes with commas after drafting. It is one unmeasured self-report, and the article does not assess grammatical or meaning preservation.
- The new June 2026 Gmail screenshot is a single product-surface example of a grammar suggestion inserting two em dashes. It does not identify the underlying model or establish frequency, but it cautions against attributing visible punctuation only to a text generator.
- The current textual Medium extraction contains zero U+2014 characters; one original screenshot contains one and the Gmail screenshot contains two. The live text check therefore passes the raw extracted Markdown and flags the transcribed screenshot strings, illustrating the input-modality boundary rather than a detector result.
- The old H8 mapping was incorrect: live H8 is placeholder residue, not machine cleanliness. No current check implements typo absence as a provenance signal.

## Evidence and claims to extract

- **Direct source reviewed:** Complete living Medium post `684fbcc9f559` as retrieved 2026-07-15, including 22 body paragraphs, three dated update blocks, every article-body link, and all four source images. The prior exact snapshot bytes were archived before replacement.
- **Method and sample:** First-person practitioner account based on unspecified subreddit observations and unspecified experiments across unnamed models, settings, prompts, and forums. Two screenshots show prompt and output fragments; one later update names an unspecified Claude configuration and another shows a cropped Gmail grammar suggestion. No sample size, repeated trials, dates for the original experiments, complete outputs, control texts, model versions, or formal analysis are reported.
- **Direct versus cited evidence:** C01-C03 are the author's observations, with C03 directly supported by preserved screenshots. C04 and C10 are author interpretation. C05, C06, C08, and C09 are inherited from linked or unnamed material and remain indirect here. C07 is the author's explicit limitation. C11-C13 and C15 are dated self-reports or page updates. C14 is this review's deterministic/provenance observation, not a source claim. C16 inventories additional visible features in the single preserved generated-response fragment; C17 is the author's unmeasured self-report about removing other unnamed cues.
- **Important limits and counterexamples:** The source cannot estimate em-dash prevalence or prompt-compliance rates. Model and product metadata are missing. Human writers deliberately use em dashes, and the cited Hacker News discussion immediately supplies dissent and long-standing human-use examples. The article's training-data mechanism is not established by the linked community discussions. Mechanical comma substitution is not evaluated for grammatical or semantic preservation. The Gmail screenshot is one cropped suggestion. The source supports review caution and dated context, not authorship inference.

## Matched patterns / rules

- C7 `no-em-dashes`; `human-eyes/scripts/grade.py::check_em_dashes`; root pattern row 49; catalogue tolerance note and action guidance
- D1 `no-collaborative-artifacts` and folded D3 sycophantic/servile tone; exact-fragment surface result misses the curly-apostrophe and `Want me to...` variants
- H15 `no-performed-candour`; exact-fragment surface result flags `honestly:`; semantic `performed_candour` remains a separate contextual review record mapped to G7
- C5 `no-curly-quotes`; exact-fragment surface result counts 11 curly quotation/apostrophe glyphs
- Product boundary in root `README.md` and `human-eyes/references/process.md`: findings do not establish authorship
- H7 advisory catalogue, H9 similar-species disambiguation, H12 genre-aware threshold calibration, and H25 model-family versus generic-AI residue
- H8 `no-placeholder-residue` only to retire the prior incorrect machine-cleanliness mapping; it does not detect typo absence
- `pattern-opportunities.md` rows for deliberate punctuation, source date/model metadata, and non-promotion of indirect cleanliness claims

## Associated hypotheses

- H7: Five-check gating grader plus advisory catalogue
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H25: Model-family versus generic-AI residue
