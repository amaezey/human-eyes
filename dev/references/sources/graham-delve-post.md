# Paul Graham on "delve" (April 2024)

## Metadata

- **URL:** https://x.com/paulg/status/1777030573220933716; follow-up: https://x.com/paulg/status/1777035484826349575
- **Author / owner:** Paul Graham
- **Publisher / platform:** X for the two direct posts; secondary reporting from Benzinga, Cryptopolitan, Entrepreneur, Guardian TechScape as quoted by Simon Willison, and Business Insider as syndicated by AOL
- **Published:** 2024-04-07
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-15
- **Source type:** practitioner social-media posts with journalism amplification
- **Evidence tier:** Practitioner / teacher / editor essays
- **Review mode:** update
- **Stable identifier:** X post 1777030573220933716; follow-up X post 1777035484826349575
- **Version / revision:** current preserved snapshot retrieved 2026-07-14 and candidate contract update extracted 2026-07-15; previous pre-contract extraction dated 2026-07-14
- **Full-text status:** complete
- **Snapshot:** `snapshots/graham-delve-post.md`
- **Extraction method:** existing snapshot compiled from X page titles surfaced in web search and cross-checked against Benzinga, Cryptopolitan, Entrepreneur, Business Insider via AOL, and Simon Willison quoting Guardian TechScape; no refetch in this contract update
- **Snapshot SHA-256:** `9fa2c196cbdc98a0c28ee0ada68997debe94ebba3e1f8f55538ff9839817c53f`
- **Model / corpus scope:** ChatGPT circa April 2024; one cold-email anecdote; later reporting about academic publishing, Nigerian and other postcolonial Englishes, and founder-email register; English; no controlled sample from Graham
- **Access limitations:** x.com blocked anonymous access; post wording comes from indexed X page titles and secondary corroboration rather than direct page retrieval; the attached chart image and the exact URLs for the secondary articles were not preserved, so the chart contents and all inherited measurements remain indirect; no other known omissions from the preserved material

## Summary

Paul Graham's two April 2024 X posts turned one occurrence of "delve" in a cold email into a public shorthand for ChatGPT-written prose. The preserved record also captures the immediate dialect objection, later frequency claims, and an RLHF-origin hypothesis through secondary coverage. For human-eyes, the source is useful as historical and practitioner evidence about salience, register, and the risks of single-word authorship claims. It does not supply a controlled comparison, threshold, or severity basis. Separate academic records for excess vocabulary remain in the Juzek and Ward and Kobak source cards.

## Main insights

- Graham treated one occurrence of "delve" in one cold email as enough to infer ChatGPT authorship, but supplied no method, comparison group, or error analysis.
- Reported comments expanded the concern to written-only formal vocabulary such as "burgeoning" and described unedited model output as an inauthentic register.
- Graham later said AI should be used "in the right way", qualifying the object-code and inauthenticity criticism as an objection to unedited or register-inappropriate use rather than all AI use.
- Nigerian and other postcolonial English speakers were reported as human look-alikes, while other commenters pointed to historical use predating ChatGPT: "delve" can be ordinary formal vocabulary, so a single-word rule risks penalising dialect and register.
- Quantitative claims in the preserved record come from journalism, Philip Shapira's chart, PubMed reporting, and AI Phrase Finder, not from Graham's anecdote.
- The proposed Nigerian RLHF-annotator mechanism is a reported hypothesis, not an established causal result in this source.
- The source is model- and date-sensitive. It concerns public reactions to ChatGPT in 2024 and cannot establish that the word's presence or absence has the same meaning for later models.

## Evidence and claims to extract

- **Direct source reviewed:** preserved text for X posts 1777030573220933716 and 1777035484826349575, reconstructed from indexed X page titles and corroborated quotations, plus the secondary reports preserved in `snapshots/graham-delve-post.md`.
- **Method and sample:** two short practitioner posts prompted by one cold email, plus secondary news and commentary published from April 2024 to 2025; ChatGPT circa April 2024; English; cold-email, academic-publication, and founder-email contexts; no controlled human comparison or sample size beyond the one reported email.
- **Direct versus cited evidence:** C01 comes from the preserved wording of Graham's two posts. C02 and C03 are Graham comments reported by secondary outlets, including his later qualification that AI should be used "in the right way"; Benzinga's disclosure concern is the outlet's interpretation rather than a preserved Graham claim. C04 records reported public counterexamples from Nigerian and other postcolonial English speakers, reported historical use predating ChatGPT, and dictionary senses quoted by Entrepreneur. C05 inherits quantitative claims and a legitimate-use qualification from reporting on Shapira's chart, PubMed, and AI Phrase Finder. C06 is a hypothesis preserved through Simon Willison's quotation of Guardian TechScape and a reported Tony Zador post. C07 is a scope inference from the source dates and later coverage, not a measured source result.
- **Important limits and counterexamples:** x.com was not directly accessible; the chart image and exact secondary article URLs were not preserved; the quantitative, dialect, and causal claims are indirect; Graham gives no threshold, corpus, comparison, or validation; Nigerian and other postcolonial English use and historical usage predating ChatGPT are explicit human look-alikes; no claim supports an individual-document authorship verdict.

## Skill-use audit

- **Good use:** historical provenance for the public salience of "delve", a practitioner example of register-based suspicion, and a cautionary case showing why human-eyes uses clustering and context rather than one-word authorship claims.
- **Misuse / overclaim:** citing Graham as proof that "delve", "burgeoning", or any isolated vocabulary item establishes AI authorship, or using the anecdote to set checker severity or thresholds.
- **Unsupported use:** generic claims across later models, languages, genres, or dialects; numeric frequency claims without the upstream sources; a causal claim about Nigerian RLHF annotators; any standalone checker or authorship verdict.
- **Underused evidence:** the live catalogue does not cite this episode as historical provenance and does not state the specific Nigerian and postcolonial-English look-alike within pattern B1.
- **Patterns left on the table:** none ready for promotion. The written-versus-spoken register prompt, dialect caveat, and model-drift question require Mae's decision and stronger direct evidence before any product change.

## Matched patterns / rules

- Pattern B1, `no-ai-vocabulary-clustering`: `delve` is in `AI_VOCABULARY`. The live registered check masks the quoted word in Graham's exact cold-email sentence and passes with `Max AI words per paragraph: 0 (0 total in text)`; a bare `delve` control passes with `Max AI words per paragraph: 1 (1 total in text)`. The focused `delve` plus `burgeoning` example also passes with one local listed word because `burgeoning` is not in `AI_VOCABULARY`. The three-local-term control, `delve`, `intricate`, and `vibrant`, fails with `Worst paragraph has 3 AI words`.
- `overall-signal-stacking`: `delve` and `burgeoning` occur in `kobak-excess-words.csv`, but the aggregate requires much broader vocabulary evidence or structural co-occurrence. The one-word and two-word focused examples each pass at 0/4. The three-local-term control passes at 1/4 because vocabulary contributes one point and no structural component fires.
- `STRATEGY.md`: human-eyes examines catalogue patterns and does not determine authorship.
- `human-eyes/references/patterns.md`: vocabulary is density and clustering evidence, not one-word proof.
- H1, H3, H9, H24, and H25 in `dev/hypotheses.md`: register calibration, non-detector framing, look-alike disambiguation, register-specific vocabulary density, and model-specific drift.
- `liang-detector-bias.md`, `juzek-ward-delve.md`, `kobak-llm-excess-vocabulary.md`, and `gptzero-ai-vocabulary.md`: direct cards for detector-bias caution, measured excess-vocabulary evidence, and separately scoped vendor vocabulary evidence.

## Associated hypotheses

- H1: continuous calibrated register-distance score per pattern.
- H3: drop detection framing entirely.
- H9: similar-species disambiguation field per pattern.
- H24: register-specific vocabulary density.
- H25: model-family versus generic-AI residue.

## Questions / follow-up

- Mae must decide whether pattern B1 should name the Nigerian and postcolonial-English look-alike directly or whether the caveat should remain centralised in detector-bias guidance.
- Mae must decide whether the direct Guardian TechScape item, Philip Shapira chart, and AI Phrase Finder analysis warrant separate ingestion before any of their inherited claims are used for a project change.
- Mae must decide whether H24 and H25 should receive an evaluation task for public-tell drift before this source is mapped beyond historical provenance.

## Update provenance

The pre-contract snapshot was preserved byte-for-byte in the archive. No source refetch or snapshot replacement occurred because the existing snapshot already contained the complete captured text. The current card adds contract metadata, stable claim IDs, live-project comparison, pending recommendations, and an independent-review gate.

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | snapshot SHA-256 9fa2c196cbdc98a0c28ee0ada68997debe94ebba3e1f8f55538ff9839817c53f | `snapshots/archive/graham-delve-post/2026-07-14-9fa2c196.md` | 2026-07-14 | `9fa2c196cbdc98a0c28ee0ada68997debe94ebba3e1f8f55538ff9839817c53f` |
| current | X post 1777030573220933716; follow-up X post 1777035484826349575 | `snapshots/graham-delve-post.md` | 2026-07-14 | `9fa2c196cbdc98a0c28ee0ada68997debe94ebba3e1f8f55538ff9839817c53f` |

## Decision history

- The pre-contract card contained no claim IDs, user decisions, or implementation statuses. There are no prior decisions to preserve or retire. C01 to C07 were assigned in this update, and every recommendation remains pending with implementation not started.

## Project coverage

This is the authoritative review table. Focused deterministic checks were run through the live registered checker against Graham's exact cold-email wording, a bare `delve` control, the reported `delve` and `burgeoning` pair, and a three-term vocabulary cluster.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Graham treated one use of "delve" in a cold email as a sign that ChatGPT wrote the text. | Practitioner observation from one email, preserved through indexed X page-title text and corroborated quotations. It is an anecdotal authorship inference with no comparison group, threshold, or error analysis. Reported human look-alikes appear in C04. | Fully covered as a vocabulary candidate with a contrary safety boundary: `delve` is in `AI_VOCABULARY`, but the live `no-ai-vocabulary-clustering` check masks the quoted word in Graham's exact sentence and passes with `Max AI words per paragraph: 0`; a bare `delve` control passes with one local hit; aggregate signal stacking scores 0/4; `patterns.md` rejects one-word proof; and `STRATEGY.md` rejects authorship classification. | The live catalogue does not record Graham's role in the tell's public history. His single-word inference cannot support a checker, severity, or authorship conclusion. | Record Graham as historical provenance for pattern B1 only. Keep the one-word pass behaviour, severity, and non-authorship language unchanged. Verification if approved: source-card and index review only, with no checker or registry diff. | pending | not started |
| C02: Graham reportedly framed "delve" and "burgeoning" as written-only formal vocabulary that people use to sound clever. | Secondary reports of Graham's comments, based on two named examples and no spoken or written corpus. The claim may describe one register judgement but cannot establish prevalence or universal unnaturalness. | Partly covered: `delve` is a local pattern B1 term; both words are style entries in `kobak-excess-words.csv`; H1 and H24 anticipate register calibration. A focused check on both words passes pattern B1 with one local listed word and scores aggregate signal stacking 0/4 with two Kobak style terms. | `burgeoning` is not in the local pattern B1 list, and no live assessment tests a written-versus-spoken register distinction. This source provides too little evidence to fill either gap. | Record the distinction as practitioner context only. Do not add `burgeoning`, create a register checker, or change severity without direct corpus evidence and matched spoken, written, dialect, and genre controls. | pending | not started |
| C03: Graham reportedly described unedited AI output as object code instead of source code, said inauthentic founder emails felt like being lied to, and qualified that criticism by saying AI should be used "in the right way". | Secondary reporting of practitioner craft judgements across 2024 and 2025. The comments identify revision and register concerns, while the qualification distinguishes misuse from all AI use. Benzinga's broader concern about editing and disclosure is the outlet's interpretation, not a preserved Graham claim. The record supplies no examples suitable for a reusable rule, prevalence estimate, or human comparison. | Partly covered at product level: `STRATEGY.md` targets cumulative craft patterns in AI-assisted prose, and the catalogue surfaces concrete vocabulary, structure, voice, and residue problems. No checker or agent assessment measures whether output was edited, used in the right way, or authentic to a sender. | Revision depth, authenticity, and disclosure are process or provenance questions, not surface findings that this anecdote can operationalise. | Record the craft framing and qualification in this card only. Do not add a checker, assessment, or provenance verdict from this source. Any future revision-depth proposal needs source-bound examples and legitimate edited and unedited controls. | pending | not started |
| C04: Nigerian and other postcolonial-English speakers challenged "delve" as ordinary formal vocabulary, and commenters pointed to historical use predating ChatGPT; the reported responses raised the risk that a single-word verdict can penalise dialect and register. | Indirect counterevidence reported across several outlets and attributed to public responses. It supplies reported human look-alikes and a reported historical counterexample but no controlled frequency estimate. Entrepreneur also quoted ordinary Merriam-Webster senses, a careful or detailed search and digging or labour, without directly reviewing the dictionary page. Liang et al. supplies separate direct detector-bias evidence, though not a `delve` frequency study. | Partly covered: `STRATEGY.md` rejects authorship verdicts; `patterns.md` requires clustering and context; H3, H9, and H24 cover non-detector framing, look-alikes, and register calibration; `liang-detector-bias.md` records non-native-writer false-positive risk. Pattern B1 does not name this specific dialect or historical-use example. | A user reading pattern B1 can see that one word is not proof but cannot see the Nigerian and postcolonial-English look-alike, the reported historical counterexample, or the workplace-disadvantage concern that made this episode important. | Mae should decide whether to add an explicit dialect and register caveat to pattern B1 and its guidance, or keep the caution centralised in detector-bias material. Any approved wording needs review by relevant human evidence and legitimate-use fixtures; no severity or threshold change follows from this source. | pending | not started |
| C05: Secondary coverage attached frequency claims to the episode: Shapira's chart was reported as showing nearly 18,000 published-paper and article instances from 2020 to 2024 and a sharp post-2022 rise; Guardian TechScape reported PubMed use at 10 to 100 times the level of a few years earlier; and AI Phrase Finder ranked "delve" ninth in a ten-word analysis while acknowledging that the word can fit a request for comprehensive investigation. | Indirect quantitative claims and a legitimate-use qualification from reporting on an unpreserved chart, journalism, and a vendor list. The chart image, exact secondary article URLs, and upstream analyses were not directly reviewed here. These claims are not Graham's measured evidence and cannot set a document threshold. | Partly covered through stronger direct-source routes: `juzek-ward-delve.md` and `kobak-llm-excess-vocabulary.md` hold scientific and biomedical excess-vocabulary evidence; pattern B1 and `overall-signal-stacking` use clustering and Kobak data; GPTZero evidence is separately scoped as tentative. Those records do not establish the inherited figures in this snapshot. | The Philip Shapira count and trend, PubMed multiplier, AI Phrase Finder ranking, and vendor qualification are not directly reviewed project evidence. This card should not duplicate or strengthen those quantitative mappings. | Use the direct academic and vendor cards for supported frequency claims and retain this card only for historical amplification. Take no checker, threshold, severity, hypothesis, or guidance action from the inherited numbers. | pending | not started |
| C06: Guardian TechScape, as quoted by Simon Willison, and a reported Tony Zador post proposed that African RLHF annotators helped produce ChatGPT's preference for vocabulary associated with Nigerian English. | Indirect causal hypothesis preserved through commentary and another commentator's quotation. This record does not contain the direct Guardian page, the direct Zador page, annotation data, model training records, or a causal experiment. Juzek and Ward separately treat RLHF as plausible rather than established. | Partly covered as an open research question: H24 and H25 separate register-specific and model-specific vocabulary, and `juzek-ward-delve.md` records RLHF as a plausible contributor. No live checker relies on the proposed mechanism. | The project lacks a directly reviewed source capable of establishing this training explanation, and the current source cannot resolve it. | Do not promote the mechanism into checker rationale or guidance. If Mae wants to use it beyond historical context, ingest the direct Guardian item and relevant upstream research as separate sources before making a project recommendation. | pending | not started |
| C07: The meaning of "delve" as a tell is time-sensitive and model-specific, so its absence cannot prove human authorship and its presence cannot carry a stable universal weight. | Scope inference from the April 2024 ChatGPT context, later 2025 reporting, and known public salience. The source does not measure model drift or establish a decay curve. | Partly covered: H24 requires time-sensitive register-specific vocabulary evidence, H25 separates model and version residue, source cards carry dates and model scope, and `STRATEGY.md` rejects authorship classification. The live local vocabulary list remains static. | No completed evaluation shows how public-tell salience or model tuning changes `delve` frequency across time, models, prompts, or registers. | Keep the card's 2024 scope explicit and make no live rule change. Mae should decide whether to schedule H24 and H25 evaluation with dated, model-labelled, register-matched human and AI samples before any future weighting decision. | pending | not started |

## Recommendations

- C01: Record Graham as historical provenance for pattern B1 only; retain the one-word pass behaviour and existing non-authorship boundary.
- C02: Keep the written-versus-spoken distinction as practitioner context; do not add `burgeoning`, a register checker, or a severity change without direct matched evidence.
- C03: Record the object-code and founder-email comments, including Graham's "right way" qualification, as craft context only; do not create a checker, assessment, or provenance verdict.
- C04: Mae should decide whether pattern B1 needs an explicit Nigerian and postcolonial-English dialect caveat or whether the caution remains centralised in detector-bias guidance.
- C05: Use Juzek and Ward, Kobak, and the separate GPTZero record for frequency evidence; take no product action from inherited numbers in this card.
- C06: Do not promote the RLHF-origin hypothesis. Ingest direct upstream sources separately before any project recommendation if Mae wants to pursue it.
- C07: Keep the 2024 model and date scope explicit; make no rule change unless Mae first approves a dated H24 and H25 drift evaluation.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change implemented.
- C02: not applicable - recommendation pending; no product change implemented.
- C03: not applicable - record-only recommendation pending; no product change implemented.
- C04: not applicable - recommendation pending; no product change implemented.
- C05: not applicable - record-only recommendation pending; no product change implemented.
- C06: not applicable - recommendation pending; no product change implemented.
- C07: not applicable - recommendation pending; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: Codex CLI fresh process, did not perform the extraction
- **Findings resolved:** corrected the live checker evidence for Graham's quoted sentence and distinguished it from the bare-word control; added the omitted qualification that Graham supported using AI "in the right way"; added the reported pre-ChatGPT historical-use counterexample, dictionary senses, vendor legitimate-use qualification, and workplace-disadvantage concern; restored the exact inherited frequency figures with indirect-evidence limits; tightened the RLHF attribution chain; recorded the unpreserved secondary URLs; verified the snapshot and archive hash and inspected the live checker outputs, registries, guidance, tests, hypotheses, and cited source cards
- **Unresolved findings:** none
