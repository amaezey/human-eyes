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

## Skill-use audit

- **Good use:** Use the source for dated public-salience context, qualitative prompt-resistance and generated-response examples, human false-positive and cue-avoidance concerns, product-surface mediation, and the need to separate candidate features from authorship claims.
- **Misuse / overclaim:** Do not cite it for an any-occurrence or density threshold, model-wide prevalence, a training-data mechanism, an official vendor position, reliable prompt-compliance rates, or a document-level authorship verdict.
- **Unsupported use:** Do not treat typo absence as current H8 coverage, infer that all models resist no-dash instructions, claim that Gmail commonly inserts em dashes, or adopt unconditional comma substitution as safe rewriting guidance.
- **Underused evidence:** The live project acknowledges deliberate human punctuation but still gives any unsuppressed U+2014 occurrence a strong warning. Csutoras adds no threshold, but its explicit unreliability conclusion, human-style citations, and product-surface example strengthen the case for matched genre and provenance controls.
- **Patterns left on the table:** No new deterministic pattern is justified. The exact response fragment exposes existing coverage boundaries: C7 and H15 flag their respective forms, while D1/D3 miss the curly-apostrophe `You’re absolutely right` and `Want me to...` / appreciation variants. Useful open work is matched C7 calibration, source/product/model/date metadata, treatment of writing-assistance tools as an alternate provenance path, and keeping indirect cleanliness observations outside placeholder-residue evidence.

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

## Questions / follow-up

- Independent source-record review passed; the pending recommendations are decision-ready, but no product change was requested.
- If prompt-compliance evidence is later used for a product decision, obtain complete dated outputs, exact models and versions, prompts, repetitions, and comparison conditions rather than relying on these screenshots.
- If typo absence becomes a proposed signal, ingest the underlying Ippolito research separately and test matched human/model text; Csutoras is only a conduit for the MIT Technology Review summary.
- If Gmail or writing-assistance provenance matters, collect repeated, versioned suggestions across explicit surfaces; this one cropped screenshot cannot establish prevalence or model identity.
- No product/checker changes were requested or made.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | Medium post ID `684fbcc9f559`; living page capture through update dated 2025-09-27 | `snapshots/archive/csutoras-em-dash-dilemma/2026-05-05-dad5117e.md` | 2026-05-05 | `dad5117eb7324eb2f67f19cbb30beeb4986bd0bfbbb69687ca3045f1d6f43d45` |
| current | Medium post ID `684fbcc9f559` | `snapshots/csutoras-em-dash-dilemma.md` | 2026-07-15 | `17967a871fb13e078deb6607bddaaec8193dd9182300a3c75afc0b05366ac0fa` |

The current page adds one 2026-06-22 paragraph and a Gmail grammar-suggestion screenshot. The Jina extraction also moved one body paragraph ahead of Medium's injected subscription module and changed a tracking parameter in the author-profile link; neither is a substantive article revision. The refreshed snapshot removes the subscription module, preserves and transcribes every source image, and wraps the complete current body in the source-ingest provenance contract.

## Decision history

- DR-109 rejected 2026-07-26 (C13): the C7 dated-fingerprint wording stays as written; no citation changes.
- The previous card had no stable claim IDs, recommendation decisions, implementation states, snapshot digest, or review gate.
- Its useful C7 caution remains but is narrowed to dated practitioner context. Its H8 machine-cleanliness mapping is retired because live H8 is placeholder residue and cannot support typo-absence claims.
- C01-C17 are stable IDs assigned in this update. All recommendations begin at `pending` / `not started`; no prior user-approved source-specific implementation was found.
- C16 approved 2026-07-17: the curly-apostrophe `You’re absolutely right` variant now matches D1/D3 (commit 61360d6). The decision covers the apostrophe-typography miss only; the fragment's other unlisted variants (`I appreciate you doing it`, `Want me to...`) remain non-promoted. All other rows remain pending.

## Project coverage

This is the authoritative review table. Focused results below use the live surface-only grader on the current raw Markdown and exact screenshot transcriptions. They are deterministic surface checks, not a complete human-eyes Audit.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: While moderating several large subreddits, Csutoras noticed posts that felt unusually polished or off and repeatedly associated one public tell with them: the em dash. | First-person practitioner observation with no named subreddits, dates, post sample, comparison group, annotation method, counts, or verified provenance. | **partly covered:** C7 names em dashes as a review cue, while the root product boundary rejects authorship inference. | The observation cannot estimate prevalence, specificity, or whether the posts used AI; "polished or off" is not an operational criterion. | Retain only as dated public-salience and moderation context; do not use it for severity, thresholds, or authorship claims. | pending | not started |
| C02: The author says em dashes persisted despite settings, hard-coded instructions, repeated reminders, warnings, threats, and a "Critical Error" label, across different models and forums. | Direct self-report, but the number of models, versions, sessions, trials, outputs, prompt wording beyond one screenshot, and success/failure rate are absent. | **partly covered:** C7 detects U+2014 in supplied text; H25 requires model/version distinctions. The project has no prompt-compliance experiment. | A pattern check does not establish how often models ignore instructions, and this source cannot generalise across models. | Record as qualitative prompt-resistance context; require versioned repeated trials before any compliance or model-family conclusion. | pending | not started |
| C03: Image 2 explicitly bans em dashes and Image 3 shows one generated response acknowledging a violation while itself containing an em dash. | Direct preserved screenshots. The model, product, timestamp, prompt/output continuity, full conversation, and omitted outputs are unknown, so this is one visible example rather than a rate. | **fully covered for candidate recognition, not behaviour frequency:** live `check_em_dashes` flags the exact Image 3 transcription with `Found 1 em dash(es)`. | The checker cannot verify the screenshot's provenance or infer model compliance, and raw Markdown image links contain no OCR text. | Preserve the screenshot as a bounded example; do not turn it into a fixture or compliance claim without source-bound metadata and complete outputs. | pending | not started |
| C04: Csutoras explains the behaviour by saying em dashes are widespread in human-written training data and became a default flow learned by models. | Author interpretation with no corpus, architecture evidence, model documentation, training-data access, measurement, or cited primary study. | **not covered:** correctly, C7 detects punctuation without encoding a training-data mechanism; H25 warns against genericising model-specific residue. | The mechanism could be plausible but is not established here and cannot explain every model or product surface. | Explicitly do not promote the training-data/default-flow explanation as project evidence or checker rationale. | pending | not started |
| C05: Two OpenAI Community discussions are presented as support that em dashes were not specially flagged during training and reflect a deep bias in written flow. | Indirect community-user discussion, not official OpenAI documentation. Current direct checks of both linked pages found complaints and training-data speculation, but not the first page's exact "not flagged" wording; the second page also contains human-use counterexamples and unsupported numerical claims. | **not covered:** no project mechanism claim depends on these forum posts. H25 and the source-ingest directness rules require official or empirical support for model mechanisms. | The article's paraphrase is not verifiable as official training evidence and the forum content is heterogeneous. | Keep the links as public-discourse provenance only; do not promote their causal or numerical claims. | pending | not started |
| C06: Some people avoid em dashes because they fear being perceived as using AI; a Hacker News commenter calls the mark a GPT-ism, while Adam Cecil reports long-standing deliberate human use. | Indirect individual comments, not prevalence evidence. Direct checks of the linked Hacker News thread and Night Water post confirm the quotations; the same thread immediately contains dissent, automatic-input explanations, and professional/historical human-use examples. | **partly covered:** C7's tolerance note, H9, and the deliberate-punctuation opportunity row acknowledge human look-alikes; root row 49 rejects authorship proof. | The live check still strongly warns on any unsuppressed occurrence, and the source cannot estimate the size or direction of avoidance effects. | Preserve both avoidance and deliberate-human-use examples; evaluate C7 only with matched genre, intent, and human controls. | pending | not started |
| C07: The article explicitly concludes that an em dash is not a reliable standalone giveaway of AI writing. | Direct author conclusion consistent with the source's human counterexamples, but not based on a controlled detection study. | **challenges current behaviour:** root row 49 says the cue cannot prove authorship and the catalogue notes legitimate use, yet live C7 fails any unsuppressed U+2014 as a `strong_warning`. | This source supports caution but supplies no replacement density threshold, genre boundary, or error rate. | Keep the explicit unreliability conclusion with the citation and add it only to the existing matched C7 calibration question; do not infer a new threshold. | pending | not started |
| C08: Through MIT Technology Review, the article relays Daphne Ippolito's claims that common-word frequency, especially "the," and typo scarcity can distinguish model text, while human writing is variable and contains mistakes or quirks. | Indirect here. Direct inspection of the linked 2022 MIT Technology Review article confirmed the attribution and its link to Ippolito et al.'s underlying research; that research was not ingested in this work unit. | **not covered:** no live typo-absence check exists. The former H8 mapping was wrong because H8 is `no-placeholder-residue`, not machine cleanliness. Root process guidance correctly avoids provenance inference from surface polish. | Csutoras is a conduit, not direct empirical evidence; typo absence can also reflect editing, genre, tools, and professional human copy. | Retire the H8 mapping. Record the indirect claim as follow-up only; require separate primary-source ingestion and matched controls before any rule proposal. | pending | not started |
| C09: A Hard Fork story about a teacher wrongly failing an entire class for ChatGPT use motivated the author's interest in reverse-engineering tells. | Unlinked, unnamed secondary anecdote in this article; no case record or verification is supplied here. | **fully covered as a boundary, not as case evidence:** root README and `references/process.md` prohibit authorship verdicts from pattern findings. | This source cannot establish the incident details or detector performance. | Retain only as motivation for non-accusatory handling; do not promote the reported case as verified evidence without separate direct review. | pending | not started |
| C10: Csutoras generalises that AI is changing how people write, talk, and think: writers back away from dashes, readers second-guess prose, and humans fear sounding robotic. | Author interpretation built from a few public comments and personal observation; no survey, longitudinal corpus, or causal design. | **partly covered:** H9, H12, and the deliberate-punctuation guidance recognise social false-positive pressure and genre/intent controls. | The source cannot establish population prevalence, causality, or effects beyond punctuation discourse. | Record as sociolinguistic framing only; do not use it to claim measured language change or justify anti-AI camouflage. | pending | not started |
| C11: The 2025-09-27 update reports a consistently working Claude project workflow that drafts, moves output into a holding area, and replaces every em dash with a comma in the final output. | Direct one-author workflow self-report. Claude model/version, project instructions, sample count, failures, source texts, and grammatical or meaning-preservation evaluation are absent. | **partly covered:** C7 detects the target glyph and project rewrite guidance requires context-appropriate punctuation plus complete meaning-preservation checks; H25 requires model metadata. | Mechanical all-to-comma substitution can produce grammatical or semantic damage, and the report cannot establish reliability. | Record as easy post-processing/evasion context; do not adopt unconditional comma substitution or a Claude-specific efficacy claim. | pending | not started |
| C12: The 2025-08-21 update says no AI company had officially acknowledged or fixed the problem and community reports continued without an effective solution. | Dated author assertion without a documented vendor search, official links, forum sample, or definition of a fix. It predates the author's September workaround and does not distinguish official product changes from user workflows. | **not covered:** appropriately, the project does not encode an official-vendor-status claim. H25 treats model and product drift as date-bound. | The negative universal claim cannot be verified from this page and is stale by design on a living source. | Keep as a dated self-report only; do not use it as current vendor-status or capability evidence. | pending | not started |
| C13: The 2026-06-22 update says Gmail's AI-assisted copy adjustments suggest em dashes; the screenshot shows one "Correct grammar" proposal replacing two commas with two em dashes. | Direct single screenshot, but the composition is cropped and the Gmail version, account setting, locale, underlying model, trigger, surrounding sentence, and repeatability are unknown. | **partly covered:** live C7 flags the exact proposed fragment with `Found 2 em dash(es)`; H25 covers product-surface and version distinctions. | The example shows a writing-assistance surface can introduce the cue, but cannot establish frequency, causal model identity, or that the whole suggestion is preferable. | Record as a product-surface/provenance counterexample; require repeated versioned observations before broader Gmail or model claims. | pending | not started |
| C14: The raw current Medium Markdown contains zero U+2014 characters, while the two transcribed source screenshots contain one and two respectively. | Reviewer observation from the complete preserved source and focused live checks; not a claim Csutoras makes. | **fully covered within text inputs:** `check_em_dashes` passes the raw Jina Markdown with `No em dashes found` and flags the exact transcribed fragments. | Image links alone do not expose screenshot punctuation to a text checker. That is an input-modality boundary, not a missed textual candidate or authorship result. | Record the boundary and preserve transcriptions for evidence review; do not add OCR or change product behaviour from this single source. | pending | not started |
| C15: The original close says the problem remained unresolved and the author stopped fighting it; the later September update narrows that claim by reporting a post-processing workaround rather than an official model fix. | Direct chronological qualification within the living page. The updates are displayed out of date order and supply no revision identifier beyond their labels. | **fully covered:** source-ingest provenance archives both page states and H25 requires dated evidence; no product behaviour depends on the original universal wording. | Without versioned outputs, neither persistence nor resolution can be generalised beyond the author's experience. | Preserve both states and treat conclusions as date-bound; take no product action. | pending | not started |
| C16: The single preserved generated-response fragment contains `You’re absolutely right`, `I appreciate you doing it`, one em dash, `honestly:`, and `Want me to...`. | Direct screenshot transcription of one response fragment from an unknown model and product. The date, prompt/output continuity, full turn, surrounding outputs, selection process, and frequency are unknown, so the fragment demonstrates visible candidates but no prevalence or model tendency. | **partly covered:** the exact-fragment surface run flags C7 `no-em-dashes` once (`Found 1 em dash(es)`), H15 `no-performed-candour` once (`honestly:`), and C5 `no-curly-quotes` with 11 glyphs. D1 `no-collaborative-artifacts` returns clear; folded D3 has no separate check. Inspection of the exact D1/D3 artifacts shows their ASCII `You're absolutely right` form does not match the preserved curly-apostrophe variant, and neither D1 nor D3 lists `I appreciate you doing it` or `Want me to...`. The semantic `performed_candour` record is contextual and was not run in this surface-only check. | Existing candidate coverage is uneven, and the fragment cannot validate a phrase family, threshold, authorship inference, or model-wide behaviour. | Record the bounded coverage result and exact misses; require broader sourced examples and false-positive controls before changing D1/D3 or promoting any response-fragment evidence. | approved | implemented |
| C17: Before focusing on the em dash, Csutoras says he had removed almost every other “recognizable AI signature.” | Direct author self-report with no named cues, examples, baseline text, method, count, comparison, or retained outputs. It supports cue-removal/evasion context only. | **not covered as an empirical result:** the project recognises post-processing and cue-evasion limits, but no check can verify removal of unnamed features from unavailable before/after outputs. | Naming or mapping other cues would invent evidence the source does not provide; the account cannot establish completeness or efficacy. | Preserve only as an unmeasured cue-evasion self-report; do not infer which cues were removed or use it to evaluate checker recall. | pending | not started |

## Recommendations

- C01: Retain only as dated public-salience and moderation context; do not use it for severity, thresholds, or authorship.
- C02: Record qualitative prompt resistance; require versioned repeated trials before compliance or model-family claims.
- C03: Preserve the bounded screenshot example; do not promote it as a fixture or compliance rate without complete metadata.
- C04: Do not promote the source's training-data/default-flow mechanism.
- C05: Keep the community links as public-discourse provenance only; do not promote causal or numerical claims.
- C06: Preserve both avoidance and deliberate-human-use examples; evaluate C7 with matched genre, intent, and human controls.
- C07: Keep the explicit unreliability conclusion in the existing C7 calibration question; do not derive a threshold.
- C08: Retire the incorrect H8 mapping and require separate primary-source ingestion before any typo-absence rule proposal.
- C09: Retain the wrongful-accusation anecdote only as motivation for the existing non-authorship boundary.
- C10: Record as sociolinguistic framing; do not claim measured language change or encourage anti-AI camouflage.
- C11: Record as post-processing/evasion context; do not adopt unconditional comma replacement or a Claude-specific efficacy claim.
- C12: Keep as a dated self-report only; do not use it as current vendor-status evidence.
- C13: Record the Gmail screenshot as one product-surface counterexample; require repeated versioned observations before broader claims.
- C14: Record the text-versus-image input boundary; do not add OCR or change product behaviour from this source.
- C15: Preserve both living-page states and treat persistence/resolution claims as date-bound; take no product action.
- C16: Record the bounded exact-fragment coverage and misses; require broader sourced examples and false-positive controls before changing D1/D3.
- C17: Preserve only as an unmeasured cue-evasion self-report; do not invent the unnamed cues or use it to assess recall.

## Evaluation of approved changes

- C01: not applicable - pending source-record recommendation; no product change requested.
- C02: not applicable - pending source-record recommendation; no product change requested.
- C03: not applicable - pending source-record recommendation; focused live check found one U+2014 in the exact Image 3 transcription.
- C04: not applicable - pending source-record recommendation; no product change requested.
- C05: not applicable - pending source-record recommendation; both community links were checked only to classify directness.
- C06: not applicable - pending source-record recommendation; no product change requested.
- C07: not applicable - pending source-record recommendation; no product change requested.
- C08: not applicable - pending source-record recommendation; live H8 was inspected and is placeholder residue, not typo absence.
- C09: not applicable - pending source-record recommendation; no product change requested.
- C10: not applicable - pending source-record recommendation; no product change requested.
- C11: not applicable - pending source-record recommendation; no product change requested.
- C12: not applicable - pending source-record recommendation; no product change requested.
- C13: not applicable - pending source-record recommendation; focused live check found two U+2014 characters in the exact Gmail suggestion transcription.
- C14: not applicable - pending source-record recommendation; focused live check passed the raw current Markdown with `No em dashes found`.
- C15: not applicable - pending source-record recommendation; prior and current snapshot hashes were verified.
- C16: passed - commit 61360d6 made D1/D3 match the curly-apostrophe variant; direct invocation of `check_collaborative_artifacts("You’re absolutely right!")` returned `passed=False` with match `you’re absolutely right` on 2026-07-17.
- C17: not applicable - pending source-record recommendation; no product change requested and no unnamed cue was inferred.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/csutoras_finish_fresh/csutoras_readonly_review`; focused final re-review passed
- **Reviewer isolation:** fresh source-dedicated agent; one source only; not reused
- **Findings resolved:** Added C16 for the complete generated-response fragment, its unknown-model and one-fragment limits, exact C5/D1/D3/C7/H15 coverage, and the D1/D3 variant misses; added C17 for the author's unmeasured removal of other unnamed cues without inventing them; corrected the Jina route comparison; fully transcribed every legible Gmail screenshot string with explicit crop and occlusion boundaries; refreshed and rechecked the snapshot digest.
- **Unresolved findings:** none
