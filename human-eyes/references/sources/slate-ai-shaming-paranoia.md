# Laurie Clarke: ChatGPT Shaming Is Making Our Writing So Much Worse

## Metadata

- **URL:** https://slate.com/technology/2025/08/chatgpt-artificial-intelligence-shaming-paranoia-writing.html
- **Author / owner:** Laurie Clarke / Slate
- **Published:** 2025-08-20 at 10:30 AM; `article:published_time` and NewsArticle `datePublished` are 2025-08-20T14:30:00+00:00; conflicting Permutive `publishedTime` is 2025-08-19T04:26:58+00:00
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** journalism with first-person observation, reported interviews, linked examples, and cited research
- **Evidence tier:** Journalism / reported cases
- **Review mode:** update
- **Stable identifier:** Slate article component `slate.com/_components/article/instances/cmeisilvf0053r3m7oafbb0n4@published`
- **Version / revision:** current published component `cmeisilvf0053r3m7oafbb0n4`; previous legacy extraction SHA-256 `849a05903ab87f0270eecc5ee9c000f127f67100302367dbbe13559c5e5887eb`
- **Full-text status:** complete
- **Snapshot:** `snapshots/slate-ai-shaming-paranoia.md`
- **Extraction method:** direct Slate HTML fetched with `curl -L --compressed`, transcribed to Markdown, and checked against both Jina Reader renderings and the archived 2026-05-05 extraction; the full hero illustration was preserved separately
- **Snapshot SHA-256:** `406c6f78c1c9af10b780472acd86327fd90ef8f6d5daf7db72c3de426f5a62b4`
- **Model / corpus scope:** August 2025 English-language cultural journalism about public reactions to ChatGPT-associated prose across email, Medium, LinkedIn, online publishing, brands, SEO, and student writing; qualitative first-person and interview reporting, not a sampled model-output corpus or authorship study
- **Access limitations:** none for the Slate article: the canonical page returned HTTP 200 and exposed the complete headline, deck, byline/date, hero illustration/caption, and 21 body paragraphs. The article's linked posts and papers were not recursively ingested; their findings remain indirect unless separately reviewed.

## Summary

Clarke's 1,261-word Slate article combines her own reaction to accusations of AI-written prose with interviews, linked public examples, expert commentary, and summaries of academic work. It documents a social feedback loop in which writers remove em dashes, words, metaphors, formal conventions, or even corrections to avoid looking machine-written. For human-eyes it is strongest as dated journalism about false-positive harm, anti-AI camouflage, and public-tell drift. It supplies no representative sample, model comparison, detector evaluation, causal test, frequency estimate, or threshold, and its cited academic findings cannot become direct project evidence through this card.

## Main insights

- Clarke describes second-guessing punctuation, voice, polish, and whether to correct a typo because polished prose can attract AI accusations.
- The article reports people purging em dashes, words associated with ChatGPT, the `not just X, Y` construction, metaphors, and formal writing conventions despite claiming human authorship.
- Gallagher's mistaken suspicion of a 2019 paper is a concrete false-positive anecdote; it does not measure a false-positive rate.
- Smith and McCarty report leaving or recommending small errors as authenticity cues, while brands reportedly request em-dash removal because they fear search-ranking penalties.
- Clarke treats triads, transitions such as `however`, metaphors, and polished grammar as legitimate writing practices that can be degraded by indiscriminate tell removal.
- The student-writing, workplace-stigma, and spoken-vocabulary findings are summaries of linked research, not findings established by Clarke's reporting method.
- Ippolito says public tells are transient because training-data recipes change; the claim supports time/version metadata and caution, not a timetable or model-wide rule.
- The article preserves countervailing possibilities: more personalised prose may be welcome, and reviewing a habitual device can improve word choice when the goal is craft rather than camouflage.

## Evidence and claims to extract

- **Direct source reviewed:** The complete current Slate page at published component `cmeisilvf0053r3m7oafbb0n4`, including headline, deck, Laurie Clarke byline, displayed/structured publication time, hero illustration and caption, 21 body paragraphs, and 13 inline source links. The direct HTML, two Jina renderings, and archived legacy extraction were compared.
- **Method and sample:** Qualitative cultural journalism in English. Evidence consists of Clarke's first-person account; interviews with Thomas Smith, Larissa McCarty, Jessica Reif, and Daphne Ippolito; attributed material from John Gallagher and Jack McNamara; linked public examples; and summaries of external papers. The article supplies no interview count beyond the named people, sampling frame, model/version test, comparison group, output corpus, or quantitative analysis.
- **Direct versus cited evidence:** C01, C04-C06, C10-C12 draw on Clarke's observations, analysis, or direct interviews. C02-C03 mix Clarke's synthesis with linked posts and attributed examples. C07-C09 report external research and remain indirect; Reif's interview in C08 explains the reported Duke result but does not turn the study result into this article's own measurement.
- **Important limits and counterexamples:** The article's claims are dated to the public discourse of August 2025. It does not establish that any named feature is unique to AI, that avoiding a feature changes detector or SEO outcomes, or that bylined published prose proves a no-AI production history. Gallagher's 2019 false positive, the article's own six em dashes and triads, Smith's refusal to abandon em dashes, Clarke's decision to correct her typo, and the possibility of useful introspection all counter simple feature-to-authorship or always-remove rules.

## Skill-use audit

- **Good use:** Use as dated journalism for the social cost of detector-like language, public false-positive examples, anti-camouflage cautions, deliberate-choice preservation, and the need to attach model/date/register boundaries to public tells.
- **Misuse / overclaim:** Do not cite the article as proof that em dashes, `delve`, triads, `however`, metaphors, good grammar, or the `not just X, Y` construction are or are not AI-generated. Do not infer authorship from the Slate byline or treat reported anxiety as a measured error rate.
- **Unsupported use:** Pattern severity, occurrence or density thresholds, detector accuracy, SEO-ranking effects, prevalence, causal writing-quality effects, model mechanisms, a stable AI vocabulary list, or generic claims about all students, writers, brands, or models.
- **Underused evidence:** The live product boundary rejects authorship claims, but the rewrite/report path does not yet explicitly warn against performative errors or deleting deliberate punctuation solely to appear human. Whether to add that wording remains Mae's pending decision.
- **Patterns left on the table:** The source's strongest contribution is not a new tell. It is the harm boundary between craft-motivated revision and anti-AI camouflage, plus a dated expert warning that public tells drift.

## Matched patterns / rules

- `human-eyes/scripts/patterns.json` and `human-eyes/scripts/grade.py`: #7 `no-ai-vocabulary-clustering`, #9 `no-negative-parallelisms`, #10 `no-forced-triads`, #30 `generic_metaphors` in `human-eyes/scripts/judgement.json`, #31 `no-excessive-lists`, #41 `genre_specific`, #49 `no-em-dashes`, and `overall-signal-stacking`.
- `human-eyes/references/process.md`: preserve argument, stance, genre, factual qualifications, quotations, and deliberate devices; do not make authorship statements.
- `dev/hypotheses.md`: H3 drop detection framing, H24 register-specific vocabulary density, and H25 model-family versus generic-AI residue.
- Focused deterministic evidence on the 21 body paragraphs: #49 flagged six em dashes; #7 was below threshold at two watched terms in the worst paragraph and three in the article; #10 surfaced two candidates while #10a stayed below its four-candidate density threshold; #9 surfaced one candidate (`promises to improve, not everyone is fearful of the future`); sentence-length variance and paragraph-length uniformity were clear. The exact illustrative sentence `It’s not just X, it’s Y.` separately triggered #9. These are surface-only results, not a complete Audit and not authorship evidence.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H24: Register-specific vocabulary density.
- H25: Model-family versus generic-AI residue.

## Questions / follow-up

- Should rewrite/report guidance explicitly distinguish craft-motivated revision from anti-AI camouflage and warn against adding mistakes or deleting deliberate punctuation merely to appear human?
- Should the linked Duke workplace-stigma study or Yakura et al. spoken-language study receive its own direct source review before any project evidence mapping is strengthened?

## Update provenance

| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |
|---|---|---|---|---|
| previous | legacy extraction SHA-256 `849a05903ab8` (no stable identifier recorded in the legacy card) | `snapshots/archive/slate-ai-shaming-paranoia/2026-05-05-849a05903ab8.md` | 2026-05-05 | `849a05903ab87f0270eecc5ee9c000f127f67100302367dbbe13559c5e5887eb` |
| current | Slate article component `slate.com/_components/article/instances/cmeisilvf0053r3m7oafbb0n4@published` | `snapshots/slate-ai-shaming-paranoia.md` | 2026-07-17 | `406c6f78c1c9af10b780472acd86327fd90ef8f6d5daf7db72c3de426f5a62b4` |

The archived file is byte-identical to both the pre-refresh working-tree snapshot and the copy at its introducing commit `f28a370`. The legacy card and manifest did not record a digest, so there was no recorded SHA-256 field to compare; the computed legacy digest above is now the update baseline. The current refresh corrects the author from Katy Waldman to Laurie Clarke and reconciles the legacy card's unqualified 2025-08-19 date: the rendered dateline, `article:published_time`, NewsArticle `datePublished`, and both Jina renderings use 2025-08-20, while the page's Permutive data contains a conflicting 2025-08-19 timestamp. It also adds the missing deck/byline/image provenance and all 13 links, removes the newsletter prompt from the substantive body, and otherwise preserves the same 21 article paragraphs with spacing/Markdown cleanup. No source claim was removed.

## Decision history

- The legacy card contained prose associations with H3, H9, #49, false-positive harm, and possible preserve guidance, but no claim-keyed user decisions or implementation statuses. The current evidence refresh reopens those associations as C01-C12 with `pending` / `not started`; nothing is carried forward as approved or implemented.
- C05 decided 2026-07-17: #49 remains fail-on-any (deliberate stance). The proposed register-matched #49 evaluation is closed with no product change. Recorded on C05 because it is the row that challenges #49's any-occurrence behaviour; C10 (transient-tell drift) was named in the decision batch but does not concern #49 thresholds and stays pending.
- C10 approved 2026-07-17 (DR-148): endorsed as drift context for H24/H25, grounds for periodically re-checking tells; no product change.
- C01 and C04 rejected 2026-07-18 via DR-121: finding-grounded revision and deliberate-choice preservation already bar tell-purging, while `SKILL.md` already forbids manufacturing irregularity to appear human. No extra report warning or typo rule was added.

## Project coverage

This is the authoritative review table. `Surface scan` below means `python3 human-eyes/scripts/grade.py audit <article-body> --surface-only`; it is deterministic evidence only and is not a complete human-eyes Audit.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Clarke describes considering leaving a typo, questioning an em dash and impersonal voice, and interrogating digital prose because polish can attract AI suspicion. | Direct first-person journalistic observation; one writer, no frequency or causal estimate. It establishes experienced self-consciousness, not how typical it is. | `human-eyes/references/process.md` protects deliberate devices and bans authorship statements; H3 addresses detection framing. **Partly covered.** | The product boundary is explicit, but report/rewrite guidance does not directly name anti-AI camouflage or performative mistakes. | Pending Mae, test-adapt one bounded anti-camouflage sentence in report/rewrite guidance; verify user interpretation and regression against deliberate-choice preservation before any implementation. | rejected | not applicable |
| C02: Clarke reports people purging em dashes, `delve`, `nestled`, `boast`, `meticulous`, and the `not just X, Y` construction despite claiming human authorship. | Journalistic synthesis with linked public examples and one linked vocabulary article; no defined sample, verified production histories, model comparison, or prevalence. | #7, #9, and #49 recognise the named categories. The exact `It’s not just X, it’s Y.` snippet triggered #9; the article body triggered #49 six times while #7 stayed below threshold at two terms in its worst paragraph and three total. H24/H25 cover register, date, and model drift. **Partly covered.** | The live checks can surface the forms, but this source cannot validate their severity or thresholds and warns that user-facing treatment may cause camouflage. | Record as public-tell and harm context only. Do not change #7/#9/#49 thresholds from this article; evaluate any anti-camouflage wording under C01/C05 separately. | pending | not started |
| C03: Gallagher says his oversensitive AI radar marked an academic article as AI-written before he noticed it was published in 2019. | Attributed anecdote linked to Gallagher's own post; direct evidence of one mistaken judgement, not a detector false-positive rate. | H3 and the `human-eyes/references/process.md` product boundary reject authorship verdicts; #41 requires source and date verification in journalism/academic contexts. **Fully covered as a caution, not as measured error evidence.** | No implementation gap supported by one anecdote; the linked post would need separate review for any broader claim. | Record only as a dated human-look-alike and source-date check; take no further product action from this anecdote. | pending | not started |
| C04: Smith says he leaves some typos as reassuring authorship cues; McCarty welcomes and recommends small public errors; the article also reports movement toward informal stream-of-consciousness prose. | Two direct interviews plus Clarke's broader qualitative synthesis; no audience experiment, sample, or writing-quality measurement. Smith also refuses to give up em dashes, a counterexample to uniform tell purging. | The process protects source facts and deliberate form and forbids invented experience; there is no typo-as-human rule. **Partly covered.** | No explicit guidance says not to manufacture errors as proof of humanity. The source cannot establish that typos improve authenticity or should be preserved generally. | Pending Mae, treat performative errors as a report/rewrite harm warning only; do not add typos or informal prose as a human-authorship signal. | rejected | not applicable |
| C05: Smith reports that brands asked him to remove all em dashes because they feared AI-looking prose would be downgraded by Google's opaque SEO system. | Direct interview report about client requests and their stated fear; Google ranking effect was not tested or verified. | #49 flags every U+2014 as a `strong_warning`; live `grade.py` requires a fix at both Balanced and All, so disclosure preservation does not apply. The article body itself contains six em dashes and triggers #49. **Challenges current behaviour as qualitative human-look-alike and camouflage evidence.** | The source does not set a better threshold, but it exposes a risk that any-occurrence removal reinforces an unverified SEO/authorship belief. | Pending Mae, include this source in a register-matched #49 evaluation with verified human controls and test anti-camouflage wording; do not alter severity or thresholds from this article alone. | rejected | not applicable |
| C06: Clarke says triads and `however` are established conventions, while McCarty avoids her own metaphors because they can look too good or ChatGPT-like. | Clarke's craft interpretation plus a direct interview; no frequency comparison or model test. The claim is about indiscriminate removal, not that every triad, transition, or metaphor is good. | #10 surfaces triads but explicitly preserves meaningful or deliberate uses; #10a requires four candidates in 300+ words; #30 flags only generic/ungrounded metaphors; the process preserves deliberate devices and deletes only metaphors without a concrete referent. The body had two #10 candidates and did not trip #10a. **Fully covered.** | `however` is not a standalone live rule, so this source identifies no implementation miss. It cannot validate a keep/remove threshold. | Record only as human-look-alike and purposeful-use context; take no further product action. | pending | not started |
| C07: Clarke reports a student paradox in which polished prose is demanded but can arouse suspicion, and cites a Hult paper saying Montclair advised faculty that AI essays may be atypically correct. | Clarke's interpretation plus an external paper and quoted institutional advice reported through that paper; indirect evidence here. No student sample is presented in the article. | #41's student watchlist checks evidence, reasoning, level shifts, draft history, and whether surface polish masks weak reasoning rather than treating polish alone as authorship proof. H3 supplies the framing boundary. **Fully covered as process caution.** | The quoted institutional guidance and paper findings require direct source review before promotion. | Do not promote the grammar claim from this card. Record the student-writing caution and require direct review of the linked Hult source for any stronger use. | pending | not started |
| C08: Clarke links AI-shaming literature and reports a 2025 Duke study finding anticipated social penalties for disclosed AI use; Reif attributes the stigma partly to generative AI not being seen as specialised skill. | Study result is indirect; Reif's direct interview supplies author interpretation. The article does not reproduce the study's sample, design, estimates, nulls, or limitations. | H3 is adjacent; the library has detector-bias and false-positive sources, but no inspected project implementation directly depends on this workplace-stigma result. **Not covered as direct evidence.** | The source-record boundary prevents transferring the Duke result into project evidence without reviewing the paper. | Leave the Duke finding indirect and unresolved. Pending Mae, ingest the linked study separately only if workplace-stigma evidence is needed for a project decision. | pending | not started |
| C09: Clarke reports a 2025 Max Planck study finding post-ChatGPT increases in AI-favoured words, including `delve`, in spontaneous podcast and YouTube speech. | Indirect summary of Yakura et al., arXiv `2409.01754`; this card does not inspect the paper's corpus, method, effect sizes, word list, revisions, or limits. | H24 calls for repeated, time-sensitive, register-specific vocabulary evidence. The Fairbanks card and Kobak snapshot already record this study only as indirect provenance. **Partly covered as an unresolved citation, not direct evidence.** | No direct Yakura source card establishes the spoken-language result for project use. | Do not duplicate-promote the claim. Pending Mae, directly ingest Yakura et al. before using the result to change #7, H24, or human-comparison language. | pending | not started |
| C10: Ippolito says AI tells are only transiently useful because companies continually revise training-data recipes. | Direct attributed expert interview, qualitative and forward-looking; no measured decay rate, named model series, or tested tell is supplied. | H24 requires corpus dates/register and H25 separates model-family/version drift from generic AI claims; current source metadata records date and scope. **Fully covered.** | No implementation gap established; the quote cannot determine refresh intervals or a model-independent rule. | Record as journalism-level drift context for H24/H25; take no further product action. | approved | not applicable |
| C11: Smith welcomes more personalised prose and attributes prior slick, impersonal style partly to SEO; he hopes writers will prioritise ideas over form. | Direct interview opinion and reported observation; no causal SEO analysis or quality outcome. It qualifies the article's harm account with a possible benefit. | The process protects stance, genre, and deliberate form and tells rewrites to repair only identified problems. H3 supports non-detector framing. **Partly covered.** | The project does not need a new pattern; the SEO-causality claim is unsupported for implementation. | Preserve as a counterexample/qualification in this card; take no further product action. | pending | not started |
| C12: Gallagher uses perceived ChatGPT tics as prompts to inspect his reliance on lists and word choice; Clarke ultimately corrects the typo but becomes less bothered by future organic errors. | Gallagher material is attributed and linked; Clarke's conclusion is direct first-person evidence. Both reject a simple always-purge or always-preserve rule. | #31 distinguishes unnecessary listification from appropriate lists; the process requires context-specific changes and preservation of deliberate choices. **Fully covered.** | No gap supported beyond the optional C01/C05 anti-camouflage wording. | Record only as the craft-versus-camouflage boundary; take no further action apart from Mae's pending C01/C05 decision. | pending | not started |

## Recommendations

- C01: Pending Mae, test-adapt bounded anti-camouflage wording in report/rewrite guidance before any implementation.
- C02: Record as public-tell/harm context; do not change #7/#9/#49 thresholds from this article.
- C03: Record the 2019 false-positive anecdote only; make no product change.
- C04: Do not add or preserve mistakes as authorship signals; consider only bounded harm guidance under C01.
- C05: Pending Mae, include the source in a register-matched #49 evaluation and test anti-camouflage wording; make no immediate severity or threshold change.
- C06: Record the purposeful-use counterexamples; make no product change.
- C07: Keep the grammar/student claim indirect until the linked Hult source is reviewed.
- C08: Keep the Duke result indirect; ingest it separately only if Mae needs workplace-stigma evidence.
- C09: Keep Yakura et al. indirect; directly ingest it before changing #7 or H24.
- C10: Map the expert drift warning to H24/H25 as journalism-level context; make no product change.
- C11: Preserve the possible personalised-prose benefit as a qualification; make no product change.
- C12: Record the craft-versus-camouflage distinction; make no product change beyond the pending C01/C05 decision.

## Evaluation of approved changes

- C01: not applicable - rejected 2026-07-18 via DR-121; finding-grounded revision and deliberate-choice preservation already bar tell-purging, so no new report warning was added.
- C02: not applicable - pending decision; no product change implemented.
- C03: not applicable - pending decision; no product change implemented.
- C04: not applicable - rejected 2026-07-18 via DR-121; the existing rule against manufacturing irregularity remains and no typo-specific product change was made.
- C05: not applicable - rejected 2026-07-17; #49 remains fail-on-any as a deliberate stance and no product change was made.
- C06: not applicable - pending decision; no product change implemented.
- C07: not applicable - pending decision; no product change implemented.
- C08: not applicable - pending decision; no product change implemented.
- C09: not applicable - pending decision; no product change implemented.
- C10: not applicable - pending decision; no product change implemented.
- C11: not applicable - pending decision; no product change implemented.
- C12: not applicable - pending decision; no product change implemented.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: `/root/slate_source_reviewer` (fresh, single-source, strictly read-only review plus focused re-check)
- **Findings resolved:** 2 - recorded the conflicting Permutive 2025-08-19 publication timestamp alongside the displayed/NewsArticle 2025-08-20 date, and corrected C05 to state that live #49 requires a fix at Balanced and All because it is a `strong_warning`. Focused re-check found 0 residual findings.
- **Unresolved findings:** none
