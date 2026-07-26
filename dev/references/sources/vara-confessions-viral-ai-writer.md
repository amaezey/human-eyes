# Vauhini Vara: Confessions of a Viral AI Writer

## Metadata

- **URL:** https://www.wired.com/story/confessions-viral-ai-writer-chatgpt/
- **Author / owner:** Vauhini Vara
- **Published:** 2023-09-21T06:00:00.000-04:00
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** journalism and first-person practitioner observation
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** WIRED page with `NewsArticle.dateModified` 2023-09-21T06:00:00.000-04:00; prior 2026-05-05 snapshot digest `00932aaf662418362caeb2a16341d8df810329c180a1c4b4729bece30952a3b0`
- **Full-text status:** complete
- **Snapshot:** `snapshots/vara-confessions-viral-ai-writer.md`
- **Extraction method:** direct canonical HTML retrieved with `curl`; Beautiful Soup selection of rendered `article p` elements cross-checked against `NewsArticle.articleBody` JSON-LD and browser-rendered article
- **Snapshot SHA-256:** `b9b619071270f93e1558b9ad0c535da7fcc21a633c6c18d6929b4534a1b23d72`
- **Model / corpus scope:** Vara's 2020 GPT-3 access and iterative co-writing of fiction and “Ghosts”; unversioned ChatGPT interactions in 2023; one unversioned Sudowrite novel-generator trial based partly on OpenAI models; interviews and reported examples from individual writers; English literary prose and chatbot responses; no corpus, matched human comparison, controlled prompts, frequency estimate, or detector evaluation
- **Access limitations:** No substantive access limitation. Direct HTML exposed all 57 substantive paragraphs. The page gives no product build, API model name, prompt log, complete generated outputs for most trials, sampling parameters, exact dates for the ChatGPT/Sudowrite interactions, or primary evidence for cited research and policy claims. Decorative illustrations and page chrome were omitted; six claim-bearing inline targets, including “Ghosts” and its This American Life adaptation, are inventoried in the snapshot.

## Summary

Vara's WIRED essay combines a first-person history of iterative GPT-3-assisted literary writing, selected generated passages, single-user ChatGPT and Sudowrite trials, writer interviews, and argument about authorship, training, access, and corporate power. It directly contributes bounded examples of both successful and failed generated prose, repeated cliché substitution, safe/polite register, a corny redemption arc, balanced chatbot framing, ignored no-list instructions, and model/time drift. It is not a corpus study and cannot establish prevalence, a threshold, a causal fine-tuning mechanism, general model behaviour, or authorship from surface prose.

## Main insights

- Iterative human selection and rewriting matter: Vara repeatedly deleted generated text, added facts, and prompted again before GPT-3 produced language she kept.
- The same source supplies a counterexample to a simple “AI prose is bad” rule: Vara judged one GPT-3 sentence among the best lines in “Ghosts,” while later disclosing that the sentimental hand-holding event had not happened.
- The later ChatGPT examples are model- and time-bounded: familiar language and plots persisted across retries, a balanced conclusion softened the issue, and six repeated attempts to prohibit lists still returned numbered pros/cons.
- The essay's “corporate, safe, AP English” explanation is Sil Hamilton's causal hypothesis; Joanne Jang's direct response was only that a good chatbot follows instructions.
- Fiction and literary-output claims have prompt, genre, version, human-editing, and taste boundaries. A single Sudowrite trial and writer interviews are useful review prompts, not measured pattern rates.
- Assistance disclosure, human choice, reader accessibility, consent, training-data bias, labor, and corporate incentives are process/provenance issues rather than prose-authorship signals.

## Evidence and claims to extract

- **Direct source reviewed:** Complete canonical WIRED article at the URL above, publisher page version whose JSON-LD records both publication and modification at 2023-09-21T06:00:00.000-04:00. The rendered 60 paragraph elements comprise 57 substantive paragraphs and three issue/contact prompts; all substantive paragraphs were preserved and checked.
- **Method and sample:** First-person retrospective covering Vara's 2020 GPT-3 access, iterative fiction and grief-essay work, a spring outreach that met overwhelming silence and mostly anti-algorithm replies before she broadened her search, later unversioned 2023-era ChatGPT use, one Sudowrite novel-generator prompt, six repeated no-list attempts, selected exact outputs, interviews with writers and product/research figures, and reported or cited claims. The sample is anecdotal, selected, English-language, and literary/chatbot focused; it is not a representative writer survey and has no matched control or statistical analysis.
- **Direct versus cited evidence:** C01-C04, C06-C07, C10, C14, and C17-C21 are Vara's direct experience, selected outputs, observation, or explicit interpretation; C08 and C11-C13 report named interviewees or creative works; C05 combines Hamilton's hypothesis with Jang's narrower reply; C09 and C15-C16 include author argument and cited claims whose underlying evidence is not reproduced or directly reviewed here.
- **Important limits and counterexamples:** The article does not identify the later ChatGPT model/version, preserve most prompts/outputs, quantify frequency, establish human base rates, or test detection. GPT-3 produced both factual/experiential failures and prose Vara considered excellent. The strong line C02 was emotionally effective but invented a sentimental event. The page distinguishes generated wording, human revision, author judgment, interviewee opinion, and cited research; none proves who wrote an unseen document.

## Skill-use audit

- **Good use:** Bounded literary-process and provenance context; examples for cliché substitution, safe/polite register, over-resolved fiction, balanced chatbot framing, list-format persistence, model drift, and semantic/experiential verification after assistance.
- **Misuse / overclaim:** Do not use the essay as a prevalence study, detector validation, model-general causal account, threshold, proof that fine-tuning causes a style, proof that all generated writing is bland, or evidence of authorship.
- **Unsupported use:** The source does not validate G2 generic/ungrounded metaphors as a general AI feature, H3 tonal uniformity across a whole unseen text, H6 faux specificity as an authorship rule, H7 stance erasure under rewriting, G3 listification rates, a model-collapse claim, or any current-model fingerprint.
- **Underused evidence:** The project does not bind prose-pattern review to assistance history, prompt, model/version, human selection depth, disclosed role, or source-versus-output comparison. It also lacks a dedicated evaluation lane for instruction-format persistence in preserved response sets.
- **Patterns left on the table:** Distinguish general cliché from G2's narrower ungrounded-metaphor construct; test safe/polite/optimistic fiction outcomes against genre-matched human and model controls; preserve unexpected successful generations and accessibility/reader-use cases as counterevidence; record unknown model/version and human editing depth.

## Matched patterns / rules

- `tonal_uniformity` / H3 in `human-eyes/scripts/judgement.json` and `human-eyes/scripts/patterns.json`
- `neutrality_collapse` / H7 in `human-eyes/scripts/judgement.json` and `human-eyes/scripts/patterns.json`
- G2 `generic_metaphors`, G3 `no-excessive-lists`, H10 `genre_specific`, and E4 `no-generic-conclusions`
- `human-eyes/references/process.md` meaning, stance, genre, deliberate-choice, closed-source, and no-authorship boundaries
- H3 detector framing, H12 register-specific thresholds, and H25 model-family/version residue

## Associated hypotheses

- H3, because mixed-quality and mixed-authorship examples reinforce review without authorship accusation.
- H12, because the examples are literary fiction, memoir, haiku, and chatbot responses rather than one generic prose register.
- H25, because the essay explicitly contrasts 2020 GPT-3 with later unversioned ChatGPT and warns against collapsing model/time conditions.

## Questions / follow-up

- If Mae wants product adoption, first preserve controlled prompt/output sets for cliché substitution, fiction endings, balanced conclusions, and no-list compliance across named model versions and dates, with genre-matched human and deliberate-use controls.
- Directly ingest Hamilton's research, the model-collapse research, and the cited policy/training-data sources before using them as project evidence.
- Decide whether assistance role and human-editing depth belong in source/evaluation provenance; no product change is made in this refresh.

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | none found | `snapshots/archive/vara-confessions-viral-ai-writer/2026-05-05-00932aaf.md` | 2026-05-05 | `00932aaf662418362caeb2a16341d8df810329c180a1c4b4729bece30952a3b0` |
| current | none found | `snapshots/vara-confessions-viral-ai-writer.md` | 2026-07-17 | `b9b619071270f93e1558b9ad0c535da7fcc21a633c6c18d6929b4534a1b23d72` |

The prior bytes match the computed previous digest and are archived unchanged. Compared with the prior snapshot, the current capture restores four substantive rendered paragraphs omitted by the old JSON-LD-only body: the opening context, Vara's spring outreach to writers, the Sudowrite-reader/mother example, and the AI-literature sameness/model-collapse passage. The remaining article prose is materially unchanged; current provenance fields, completeness checks, subtitle, and exact access notes were added.

## Decision history

- C04, C07, C17, C18 approved 2026-07-26 via DR-23, DR-24: Mae queued this work for later rather than ruling on its shape now. No checker, registry, or test change has been made and implementation has not started.
- The previous 2026-05-05 card had no stable claim IDs, authoritative coverage table, user-decision fields, or implementation statuses, so it contains no approved or implemented decision to carry forward.
- The inherited mapping that removed H6/H7 and added “G2 cliche-ridden prose” and H3 is reopened. General cliché is not the live G2 construct, and the refreshed complete source contains direct bounded examples relevant to H6 and H7 while still not validating either as an authorship rule.
- Every current recommendation is therefore `pending` / `not started`; no checker, registry, hypothesis, test, or guidance change was made.

## Project coverage

This is the authoritative review table. Focused deterministic evidence came from `python3 human-eyes/scripts/grade.py audit tmp/vara-confessions-viral-ai-writer/focused-examples.md --surface-only --format json`; it returned `coverage_mode: surface_only`, `audit_status: incomplete`, only curly-punctuation and `crucial` significance findings, zero list items, no generic conclusion, zero tidy endings, sentence-length SD 9.4, and a B5 short-text skip. This establishes deterministic coverage only, not a complete Audit.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: GPT-3 first falsely cured Vara's deceased sister, then invented a running/fundraising life; she repeatedly deleted failures, added facts and prose, and prompted again until the fourth or fifth attempt felt closer to her experience. | Direct first-person process evidence from one writer using 2020 GPT-3; no full prompt/output log or comparison. | `references/process.md` requires preservation of argument, facts, examples, stance, point of view, genre, and deliberate choices: partly covered. | The live process is rewrite-focused and does not describe iterative co-writing provenance or selection depth; the exact factual/experiential failures are not fixtures. | Record as process and factual-verification context; if provenance metadata is pursued, test a graduated assistance/selection-depth field without treating it as an authorship flag. | pending | not started |
| C02: GPT-3 produced the hand sentence Vara considered among the best lines in “Ghosts,” yet she later says the real relationship was not sentimental in that way. | Direct selected output plus author interpretation and experiential correction; one literary case, not a quality measure. | H6 `faux_specificity`, H10 fiction review, and `process.md` factual/meaning preservation are adjacent: partly covered. Focused surface output found no relevant deterministic construction. | The example is both a successful literary sentence and an invented experiential detail, challenging one-sided “generic AI prose” treatment; H6 does not bind text to known life facts. | Add only as a future paired source/output counterexample for semantic and experiential verification; do not promote to a phrase rule. | pending | not started |
| C03: In a first fiction trial, Vara judged GPT-3's climax haunting, but editors rejected the disclosed machine-assisted story; the later explicitly AI-engaged “Ghosts” was published, adapted, anthologized, and positively received. | Direct first-person successful-output and publication history plus reported reception; selection effects and no comparator. | H10 journalism watchlist checks undisclosed generated content; product boundary avoids authorship claims: partly covered. | No graduated distinction among assistance, co-writing, disclosure, acceptance, and quality, and editorial acceptance is not a prose-quality measure. | Record as a mixed quality/provenance/reception counterexample; require broader policy evidence before any disclosure guidance change. | pending | not started |
| C04: Writers and Vara found later generated prose boring and cliché-ridden; asking ChatGPT to remove clichés produced a different set of clichés. | Direct repeated-use observation plus named but unquantified writer reports; model/version, prompts, outputs, dates, counts, and human comparison absent. | G2 is specifically generic/ungrounded metaphors, not general cliché; H10 fiction watchlist names generic fidelity and over-resolved endings: not covered for the stated construct. | The inherited G2 mapping conflates general cliché with ungrounded metaphor and has no controlled coverage. | Correct the source mapping; keep general cliché substitution as a model/date/genre-controlled evaluation candidate, not a new rule. | approved | not started |
| C05: Sil Hamilton hypothesizes that fine-tuning ChatGPT as a chatbot caused corporate, safe, AP-English prose; Joanne Jang says a good chatbot's purpose is to follow instructions. | Named interviewee hypothesis and a narrower first-party product-manager response; no experiment, training record, or direct causal confirmation. | H25 records model/version residue: partly covered as provenance framing only. | The live project has no evidence for the fine-tuning causal story, and the two interview responses are not equivalent. | Record Hamilton's explanation as indirect and unresolved; ingest direct research before using the mechanism in guidance. | pending | not started |
| C06: Vara characterizes ChatGPT's voice as polite, predictable, inoffensive, and upbeat, contrasting those properties with strong literary characters, plots, styles, and endings. | Author synthesis from her use and interviews; qualitative, literary, unversioned, no rate or matched human comparison. | `tonal_uniformity`/H3 checks whether a whole text holds one register, and H10 reviews fiction craft: partly covered. | Safe/polite/optimistic qualities are not identical to whole-text register lock; the source does not validate severity. | Keep as bounded literary-review context and evaluate against genre-matched samples before changing H3/H10. | pending | not started |
| C07: Given a gross-out prompt, Sudowrite proposed a corny redemption arc ending with “maybe, just maybe” making things right. | Direct single prompt/output excerpt and author judgment; unversioned product based partly on OpenAI models, no repeat trials. | H10 fiction branch covers over-resolved endings; E4 covers a narrow generic-positive phrase set. Focused surface output reported no generic conclusion or tidy ending: partly covered. | Current deterministic checks miss this exact safe-redemption example; one case cannot establish a generic check. | Preserve as a fiction fixture candidate with deliberate redemption, comic, and human controls; do not add a phrase rule. | approved | not started |
| C08: Matthew Sims says existing writing tools are limited and that creative-prose fine-tuning would require costly taste judgments by knowledgeable labelers. | Named interviewee proposal and feasibility judgment; hypothetical, no implemented system or outcome. | No live prose check; H25 is adjacent only as model/training provenance: not covered. | The source does not test whether the proposal works or define “creative.” | Record only; obtain direct system/evaluation evidence before any project use. | pending | not started |
| C09: Vara argues that model training text reflects a narrow white, male, anglophone slice of the internet and cannot articulate an individual consciousness. | Author argument drawing on unstated/cited background; no dataset audit in the article. | Detector-bias cautions and H25 provide broad provenance boundaries: partly covered conceptually, not evidentially. | Underlying training-data evidence is not preserved, and consciousness is not an operational prose construct. | Do not promote to a pattern or model-general claim; directly review upstream dataset evidence if needed. | pending | not started |
| C10: Vara still uses ChatGPT for research but stopped using it to generate prose in place of her own because she values individual consciousness and factual personal voice. | Direct current-practice statement and author value judgment; one writer, no outcome comparison. | `process.md` protects source facts, point of view, stance, and deliberate choices: fully covered as an editing boundary. | It does not imply that every writer should make the same tool choice. | Record only as a bounded process example; take no product action. | pending | not started |
| C11: Jenny Xie describes ChatGPT as an idea-jogging tool comparable to an encyclopedia, thesaurus, Google, or YouTube, from which she selects small pieces. | Named interviewee report; no preserved prompts, outputs, frequency, or outcome assessment. | `references/process.md` preserves source meaning during rewriting but does not define assistance roles: not covered. | No live framework records brainstorming versus prose substitution, and the article does not validate benefits. | Keep as process-role context; require broader evidence before guidance. | pending | not started |
| C12: Lillian-Yvonne Bertram uses divergent GPT-3 models to expose limitations in corporate models' narrative imagination about Black stories. | Vara's report of a forthcoming creative work; outputs and work not preserved here, so indirect. | H10 fiction review and H25 model-specific residue are adjacent: not covered for this cited work. | The source cannot support claims about the models' exact differences without direct review of Bertram's work. | Record as an indirect follow-up; ingest the primary work before project use. | pending | not started |
| C13: Sheila Heti's Chai experiments unexpectedly shifted existential chatbot conversations toward sexual desire and mistaken identity. | Vara's summary of a named published five-part series; indirect, selected, no full text here. | No relevant live prose-pattern coverage: not covered. | This is creative-process framing, not a reusable surface tell. | Take no further action unless the primary series is separately ingested. | pending | not started |
| C14: Reader-created stories and Sudowrite users supply accessibility and democratization counterexamples; Vara's father claimed a ChatGPT haiku with repeated “delight,” and she could not decide whether the repetition was ungainly or subversive because the reader-owned literary relationship was a closed loop. | Direct observation and exact selected output plus named participant/interviewee claims; no representative sample or outcome measure. The haiku is an explicit interpretation null rather than proof of bad repetition. | H3's non-accusatory framing and product no-authorship boundary are conceptually aligned: partly covered. | The project has no formal accessibility/disclosure policy; the evidence cannot establish broad benefit, and repetition requires deliberate-use and reader-context controls. | Preserve as accessibility, reader-use, and interpretation counterevidence in future policy/evaluation review; do not turn use, disclosure, or repeated wording into a prose flag. | pending | not started |
| C15: The essay links AI writing to consent, compensation, labor, bias, capital cost, corporate capture, and pressure on writers; Vara's consent-based alternative model fails in her thought experiment because resources are prohibitive, writer access would need policing, and forbidding individual profit is impracticable. | Author argument and qualified thought experiment plus named organizations and reported statements; underlying labor, policy, and economic evidence is not directly reviewed here. | Source/provenance and no-authorship boundaries are adjacent; no prose checker is appropriate: not covered as product evidence. | These stakes and the failed alternative cannot justify a surface pattern, severity, or authorship inference. | Record the argument and its failure conditions as framing only; separately ingest primary policy/economic sources before guidance. | pending | not started |
| C16: Vara says AI-dominated literature could converge in values, biases, and style and cites research suggesting AI-trained-on-AI data could cause model collapse. | Author prediction plus cited research not identified in the snapshot text as a direct study record; no experiment here. | H25 model/version drift is adjacent as provenance context only: not covered evidentially. | The source does not establish current prose sameness, prevalence, or a checker threshold; model collapse is inherited evidence. | Do not promote; directly ingest the upstream research before using the claim. | pending | not started |
| C17: After an explicit “Please answer without giving me a list,” ChatGPT returned numbered pros-and-cons responses on six repeated runs. | Direct repeated first-person trial; exact returned outputs, model/version, date, sampling, and session independence are absent. | G3 `no-excessive-lists` detects rendered list formatting, not prompt noncompliance. Focused preserved excerpts contained no list blocks and returned zero list items: not covered for instruction persistence. | No response corpus is preserved, so the observation cannot set a frequency or threshold. | Preserve as a candidate for a named-model repeated-response compliance fixture with prose/list controls; no rule change. | approved | not started |
| C18: ChatGPT answered a social-cost question with a balanced “striking a balance” conclusion that Vara calls dispassionate and both-sides-ist. | Direct exact output excerpt plus author interpretation; one unversioned interaction, no human control or original stance-bearing draft. | `neutrality_collapse`/H7 identifies balanced framing, while `process.md` protects stance: partly covered. Focused deterministic output found only `crucial` significance inflation, not a generic conclusion. | H7 is not source-versus-rewrite bound here; the excerpt supports a bounded balanced-output example, not systematic stance erasure. | Add as a future prompt/output fixture for H7 and false-balance evaluation with legitimate-neutrality controls; do not change severity. | approved | not started |
| C19: Vara contrasts an earlier GPT-3 that produced moving prose with later ChatGPT that produced clichés and rigid list responses. | Direct longitudinal user interpretation; model builds, exact dates, prompts, and settings are incomplete. | H25 explicitly separates model family/version/date residue from generic AI claims: fully covered conceptually. | The card can record only GPT-3 versus unversioned ChatGPT, not a reproducible model fingerprint. | Record model/time uncertainty and take no checker action; use only as drift rationale. | pending | not started |
| C20: The essay contains successful, failed, revised, selected, disclosed, and reader-owned AI-assisted writing, so no single surface example proves authorship or quality. | Synthesis of direct counterexamples within the source; interpretive boundary rather than measured result. | `references/process.md` and the product boundary explicitly prohibit authorship inference: fully covered. | No gap for a prose rule; source identity and assistance history remain external provenance. | Take no further product action; retain as the card's decision-integrity boundary. | pending | not started |
| C21: Vara's spring outreach to writer friends and acquaintances met overwhelming silence, and most respondents were anti-algorithm; only after broadening her search did she find a few experimenters. | Direct negative and selection result about an informal outreach; no invitation text, denominator, response count, sampling frame, or representative writer survey. | No live prose check or hypothesis measures writer adoption: not covered. | The named experimenter examples are selected after sparse/negative initial response and cannot establish common practice or adoption rates. | Preserve the selection boundary in this card; take no product action and do not generalize prevalence. | pending | not started |

## Recommendations

- C01: Record the false cure, invented running/fundraising life, iterative co-writing, and selection depth as process and factual-verification context; any provenance-field proposal requires a separate policy decision and evaluation.
- C02: Preserve the hand sentence as a paired semantic/experiential counterexample; do not promote it to a phrase rule.
- C03: Record the haunting first fiction climax, disclosed editorial rejection, later “Ghosts” reception, and their mixed-quality/provenance boundary; require broader evidence before changing disclosure guidance.
- C04: Correct the inherited G2 mapping and evaluate general cliché substitution separately with model/date/genre controls.
- C05: Keep Hamilton's causal explanation indirect and unresolved until direct research is reviewed.
- C06: Keep safe/polite/optimistic voice as bounded literary context; evaluate before changing H3 or H10.
- C07: Preserve the Sudowrite excerpt as a controlled fiction-fixture candidate, not a new deterministic phrase rule.
- C08: Record the hypothetical fine-tuning/taste-cost proposal only.
- C09: Do not promote training-data or consciousness arguments to a prose pattern; review primary evidence if needed.
- C10: Record Vara's tool-choice boundary and take no product action.
- C11: Keep idea-jogging as unvalidated process-role context.
- C12: Treat Bertram's work as indirect and ingest it separately before project use.
- C13: Take no further action on the Heti summary without primary-source ingestion.
- C14: Preserve accessibility, reader-use, and the haiku interpretation null as counterevidence; require deliberate-use and reader-context controls and never make use, disclosure, or repetition a prose flag.
- C15: Keep consent, labor, economic, and corporate claims plus the alternative-model resource, access-policing, and profit failure conditions as framing pending direct-source review.
- C16: Do not promote the model-collapse/sameness claim without ingesting the upstream research.
- C17: Build only a future named-model response-set evaluation for no-list compliance; make no rule change from the anecdote.
- C18: Use the exact balanced conclusion only as a future H7/false-balance fixture with legitimate-neutrality controls.
- C19: Record incomplete model/version/date metadata and use the case only as drift rationale.
- C20: Retain the no-authorship and mixed-quality boundary; take no further product action.
- C21: Preserve the outreach nonresponse/anti-use and broader-search selection boundary; do not generalize writer adoption and take no product action.

## Evaluation of approved changes

- C01: not applicable - recommendation pending; no product change implemented.
- C02: not applicable - recommendation pending; no product change implemented.
- C03: not applicable - recommendation pending; no product change implemented.
- C04: not applicable - recommendation pending; no product change implemented.
- C05: not applicable - recommendation pending; no product change implemented.
- C06: not applicable - recommendation pending; no product change implemented.
- C07: not applicable - recommendation pending; no product change implemented.
- C08: not applicable - recommendation pending; no product change implemented.
- C09: not applicable - recommendation pending; no product change implemented.
- C10: not applicable - recommendation pending; no product change implemented.
- C11: not applicable - recommendation pending; no product change implemented.
- C12: not applicable - recommendation pending; no product change implemented.
- C13: not applicable - recommendation pending; no product change implemented.
- C14: not applicable - recommendation pending; no product change implemented.
- C15: not applicable - recommendation pending; no product change implemented.
- C16: not applicable - recommendation pending; no product change implemented.
- C17: not applicable - recommendation pending; no product change implemented.
- C18: not applicable - recommendation pending; no product change implemented.
- C19: not applicable - recommendation pending; no product change implemented.
- C20: not applicable - recommendation pending; no product change implemented.
- C21: not applicable - recommendation pending; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/vara_source_reviewer`; fresh source-dedicated read-only review plus two focused re-checks
- **Findings resolved:** Five initial findings resolved: corrected H8/H28 coverage, added C21's outreach nonresponse/selection boundary, restored central GPT-3 success/failure examples, added haiku and alternative-model qualifications, joined `early-generation`, inventoried claim-bearing links, and recomputed provenance. One focused-recheck finding resolved by synchronizing C01, C03, C14, and C15 recommendation bullets with the authoritative table.
- **Unresolved findings:** none
