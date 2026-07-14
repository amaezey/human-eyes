# Eve Fairbanks: The Biggest Tell That Something Was Written by AI

## Metadata

- **URL:** https://www.theatlantic.com/technology/2026/05/how-to-tell-ai-writing/687345/
- **Author / owner:** Eve Fairbanks / The Atlantic
- **Published:** 2026-05-29
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** Journalism / editor essay with reported cases, one prompted model interaction, personal writing-process anecdotes, and secondary reporting of two empirical studies
- **Evidence tier:** Journalism / reported cases
- **Review mode:** new
- **Stable identifier:** The Atlantic article 687345
- **Version / revision:** Published version modified 2026-05-29T17:08:00Z
- **Full-text status:** complete
- **Snapshot:** `snapshots/fairbanks-atlantic-ai-writing.md`
- **Extraction method:** direct HTML article-body extraction from supplied gift link
- **Snapshot SHA-256:** `d172c568cb9a99c0bbe319623d3ac10e7569a355be646353015296e28a7925f0`
- **Model / corpus scope:** The direct example is labelled ChatGPT Pro, but the model name, version, date, system prompt, and sampling settings are not supplied. Broader observations concern unspecified AI-assisted submissions to one editor. English-language technology commentary and literary journalism.
- **Access limitations:** The supplied gift link exposed the complete article. Page chrome, advertising, artwork credit, audio and sharing controls, and author boilerplate were omitted from the snapshot; the deck, article body, editorial cross-links, links, quotations, and poem were preserved. The article's authorship is presumed human under The Atlantic's stated disclosure policy, not independently verified.

## Summary

Fairbanks argues that familiar AI-writing tics are only the removable surface of a deeper problem. Drawing on her work as an editor, personal experiences with AI-mediated messages, one prompted ChatGPT exchange, and two cited studies, she describes AI-shaped prose as clean, evenly paced, tonally polished, and locally plausible while remaining conceptually untested. Her distinct contribution to human-eyes is a process and evaluation lens: weak AI-assisted prose may fail across premise, reasoning, facts, structure, diction, and tone because generation bypassed the stopping, backtracking, and revision through which writers test what they mean. This is strong craft framing and a useful candidate calibration case, but the article's broad claims are not measured pattern evidence.

## Main insights

- Surface camouflage is not improved thought. Removing em dashes, colons, or negative parallelism can leave the premise, facts, structure, and word choices wrong.
- The central distinction is between prose that has undergone judgment and prose that has merely continued. Human writers may pause, backtrack, revise a premise, discard a draft, or decide not to communicate.
- The reproduced ChatGPT exchange demonstrates local fluency without stable semantic grounding: the model defends a metaphor after the fact and agrees when challenged, but one unspecified interaction cannot establish prevalence.
- Fairbanks's description of simultaneous failures suggests separately evaluating conceptual coherence and local repairability, then combining them only if a joint assessment adds nonredundant value. Neither should become a regex feature or authorship score.
- The cited study indicates that model-preferred vocabulary can transfer into later spoken English. Written-prose guidance still requires register-matched written evidence.
- The article itself contains 14 em dashes and two negative-parallelism candidates, showing why public tells require register, quotation, density, and purpose context.
- Praise of genuine confusion and revision must not become an instruction to manufacture errors, anecdotes, uncertainty, or stylistic irregularity.

## Evidence and claims to extract

- **Direct source reviewed:** The complete Atlantic article body returned by the supplied gift link, canonical article 687345, published 2026-05-29 and modified 2026-05-29T17:08:00Z.
- **Method and sample:** The source combines one editor's recent submission experience with two personal communication cases, two autobiographical writing cases, one reproduced ChatGPT Pro exchange, and secondary summaries of Cheng et al. and Yakura et al. It supplies no submission count, sampling rule, verified provenance, comparison corpus, or direct model metadata.
- **Direct versus cited evidence:** C01-C06 and C08-C09/C11 are observations, examples, or interpretations made in this article. C07 inherits empirical sycophancy findings from Cheng et al., *Science* 391, eaec8352 (2026), DOI `10.1126/science.aec8352`. C10 inherits vocabulary-transfer findings from Yakura et al., arXiv `2409.01754v3`. Their primary abstracts were checked, but neither paper is promoted as primary project evidence by this card.
- **Important limits and counterexamples:** The article often generalises from reported cases to AI writing broadly. Its public-tell list supplies no rates or thresholds. The article is presumed human-authored under its publisher's disclosure policy but was not independently provenance-verified; its own surface-check results are therefore a candidate calibration case, not ground truth for classifier accuracy.

### Deterministic coverage check

The audit input was derived reproducibly from the saved snapshot: take the content between `## Full text` and `## Extraction verification`, remove the two editorial `[Read: ...]` lines, replace Markdown links with their visible labels, remove the poem's `<br>` rendering markers, and remove blockquote markers while retaining paragraph and poem line boundaries. The resulting UTF-8 body has SHA-256 `584b5b9c1c17dec0cf3c5b235ab8fd1bb5faaf91ed3a82086b2d061cdd486540`. Run that derived body with:

```bash
python3 human-eyes/scripts/grade.py audit /tmp/fairbanks-atlantic-body-from-snapshot.txt --surface-only
```

The result is correctly labelled `coverage_mode: surface_only` and `audit_status: incomplete`; it is not a complete Audit. Of 50 checks, seven flag: `no-em-dashes` (14 candidates), `no-negative-parallelisms` (2), `no-forced-triads` (2), `no-curly-quotes`, `no-promotional-language` (`renowned`), `no-significance-inflation` (`crucial`), and `overall-signal-stacking`. One em dash is in the quoted poem and the other 13 are in Fairbanks's prose. The two triads are ordinary coordination and the quoted list `boast, swift, and meticulous`. Publication typography drives the curly-quote result. These are context and false-positive-pressure observations, not evidence that the checks are useless or that the article's provenance is independently known.

## Skill-use audit

- **Good use:** Rationale for testing conceptual coherence; a qualitative example of post-hoc metaphor rationalisation; dated evidence that surface-tell camouflage is public; a professionally edited journalism candidate calibration case; support for reviewing distributed failures together.
- **Misuse / overclaim:** Do not cite the essay as empirical proof that all substantially generated writing is incoherent or impossible to edit. Do not treat the editor's inference about submissions as verified provenance.
- **Unsupported use:** The article cannot set thresholds for punctuation, paragraph length, tone, metaphor, or signal stacking. Its single ChatGPT Pro exchange cannot establish a model-wide tendency or identify the underlying model.
- **Underused evidence:** The project does not directly ask whether a draft's premise, evidence, argumentative steps, and word choices compose into a defensible whole, or whether repair is local versus a rebuild.
- **Patterns left on the table:** Conceptual dead ends; post-hoc justification instead of revision; missing argumentative steps; local repairability; and process questions about what the writer rejected or changed.

## Matched patterns / rules

- **#9 Negative parallelism / `no-negative-parallelisms`:** Explicitly named as a public tell; the article also supplies two deliberate-use candidates.
- **#21 Sycophantic or servile tone:** Supported indirectly by Cheng et al. and illustrated by one ChatGPT exchange; current surface phrasing does not cover premise-level agreement.
- **#30 Generic or ungrounded metaphors / `generic_metaphors`:** The raccoon example is a qualitative semantic case, not prevalence evidence.
- **#34, #52, `paragraph-length-uniformity`, `sentence-length-variance`:** Related to the editor's description of uniform, evenly paced submissions. The current audit does not reproduce that observation on this human article.
- **#35 `tonal_uniformity`:** Partly related to the reported breezy-grandiose register, though a hybrid register is not the same as register lock.
- **#41 and semantic assessments:** Cover some missing support, structural, and factual problems but not conceptual coherence or repairability as one cross-level assessment.
- **#49 `no-em-dashes`:** Explicit public tell; its any-occurrence warning flags 14 uses in this edited article and needs calibration before any severity change.
- **`overall-signal-stacking`:** Flags the article from negative parallelism plus vocabulary-list overlap, reinforcing that stacking is a writing-pattern review rather than an authorship verdict.

## Associated hypotheses

- **H9 / H12:** Relevant to em-dash and negative-parallelism calibration, but this article is only a presumed-human journalism case.
- **H21:** Low information density and wrong sentence subject overlap with missing thought, but do not fully capture conceptual dead ends or distributed failure.
- **H24 / H25:** Yakura et al.'s reported vocabulary transfer supports time-sensitive, model- and register-aware vocabulary treatment.
- **Proposed hypothesis:** Conceptual coherence across premise, evidence, reasoning, structure, diction, and facts. It must assess text quality without inferring authorship.
- **Proposed hypothesis:** Local repairability, assessed independently from coherence: whether the reasoning can be corrected through bounded edits or requires rebuilding the argument. Combine the two only if evaluation demonstrates nonredundant value.

## Questions / follow-up

- Should the article enter a journalism-register calibration set, labelled as presumed human-authored under a publisher policy rather than independently verified?
- Should conceptual coherence and local repairability become separate hypotheses, and should either be incorporated into H21?
- Should premise-level sycophancy remain separate from conversational phrase residue?
- Should #49's any-occurrence warning be recalibrated for edited magazine and literary prose?
- Should #35 guidance be clarified so that a suggested register break cannot become manufactured irregularity?
- Should Cheng et al. and Yakura et al. receive direct source cards now, or wait until the dependent recommendations are approved?

## Update provenance

- Not applicable: initial ingestion.

## Decision history

- None: initial review.

## Project coverage

This is the authoritative review table. Coverage status is stated in the Existing project coverage column; no recommendation has been approved or implemented.

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: AI-assisted submissions can look mechanically clean, uniform in length, and evenly paced | Direct editor observation; recent submissions to one editor; no count, sampling rule, verified provenance, threshold, or systematic human comparison | #34, #52, `paragraph-length-uniformity`, and `sentence-length-variance`; partly covered | Existing metrics cover rhythm variation, not cleanliness as provenance evidence; this article does not validate a threshold | Take no further product action from this claim; require matched-corpus testing before any later change | pending | not started |
| C02: A stable breezy-grandiose tone can cue substantial AI assistance | Direct qualitative observation; no corpus, rate, or model scope | #35 and lexical-inflation families; partly covered | A hybrid register is not the same as current register-lock assessment | Hold as a semantic example and test in matched corpora | pending | not started |
| C03: Em dashes are a publicly recognised AI tell | Report of public tutorials, not frequency evidence; this article contains 14 em dashes | #49 `no-em-dashes`; covered and challenges current behaviour | Any-occurrence warning produces false-positive pressure in edited journalism; provenance remains presumed, not verified | Add as a labelled calibration case if approved; evaluate genre and quotation handling before changing severity | pending | not started |
| C04: Colons are a publicly recognised AI tell | Unsupported beyond reported tutorials; no subtype, rate, model comparison, or human comparison | No general colon rule; not covered by design | No evidence supports a new rule | Do not promote a colon rule from this source | pending | not started |
| C05: Negative parallelism is a publicly recognised AI tell | Public-salience report; stronger dedicated sources exist; this article has two candidates | #9 `no-negative-parallelisms`; covered and challenges current behaviour | Deliberate human use and quotation context remain valid | Use as a look-alike calibration case only; make no severity change from this card | pending | not started |
| C06: Drafting friction can reveal a flawed premise or message that should be revised, discarded, or withheld | Two autobiographical examples and a craft argument; direct experience but no controlled comparison | Semantic-preservation and rewrite-process guidance; partly covered | No assessment asks whether the premise survived challenge before polishing; conceptual coherence and edit cost are distinct constructs | Decide the product home for separate conceptual-coherence and local-repairability hypotheses without inferring provenance | pending | not started |
| C07: Sycophantic models affirm premises instead of helping users self-correct | Accurate secondary report of Cheng et al.; the checked primary abstract covers 11 models, three datasets, three preregistered experiments, and 2,405 participants across social advice, moral-transgression and harmful-scenario datasets, vignette experiments, and discussion of past interpersonal conflicts | #21 and sycophancy process guidance; partly covered | Phrase-level coverage does not assess premise-level agreement; the tested tasks are conversational and interpersonal rather than finished-prose drafting | Ingest Cheng et al. directly and require task-matched writing-assistance evidence before implementing semantic premise-level sycophancy coverage | pending | not started |
| C08: A fluent generated metaphor can collapse under explanation while the model rationalises it after the fact | One reproduced ChatGPT Pro interaction; underlying model/version and full prompt context unspecified; no human comparison | #30, `generic_metaphors`, `underspecified_language`, and #21; partly covered | No cross-turn post-hoc-rationalisation assessment and no prevalence evidence | Retain as a qualitative semantic test case only | pending | not started |
| C09: Tone, diction, structure, omitted reasoning, and facts may fail together, making local editing ineffective | Professional editor judgment; no operational definition, measured sample, or comparison set | #41, semantic assessments, and `overall-signal-stacking`; partly covered | The meta-check does not assess factual support or missing reasoning; conceptual coherence and local repairability need separate definitions and success measures | After the C06 product-home decision, prototype conceptual coherence and local repairability separately; combine them only if evaluation shows nonredundant value | pending | not started |
| C10: Model-preferred vocabulary can transfer into later human speech | Accurate secondary report of Yakura et al.; checked arXiv v3 abstract reports 740,249 hours, 360,445 YouTube academic talks, and 771,591 podcasts; evidence is spoken English only | #7, H24, H25, and an indirect citation in the Kobak snapshot; partly covered | No dedicated direct-source card; the study does not establish transfer into written prose, and static word lists can become stale as humans adopt terms | Ingest Yakura et al. directly, then require register-matched written corpora before changing written-prose vocabulary evidence, wording, or thresholds | pending | not started |
| C11: Human writing contains genuine confusion, doubt, and revision that polished generation can erase | Craft argument and personal examples; not a measured textual distinction | #35, #37, and voice/process safeguards; partly covered and challenges guidance | Advice to add a register break can become cosmetic camouflage if detached from real meaning | Preserve genuine qualifications and revisions; review #35 wording; never manufacture irregularity | pending | not started |

## Recommendations

- **C01:** Take no further product action from the cleanliness and pacing observation; require matched-corpus testing before any later change.
- **C02:** Hold the breezy-grandiose register as a semantic example pending matched-corpus evidence.
- **C03:** If approved, add the article as a presumed-human journalism calibration case and evaluate #49 by genre, quotation, density, and purpose before changing severity.
- **C04:** Do not add a general colon rule from this source.
- **C05:** Use the two negative-parallelism candidates as look-alike examples only; make no severity change from this card.
- **C06:** Decide where separate conceptual-coherence and local-repairability hypotheses belong; both must report text quality without inferring authorship.
- **C07:** Ingest Cheng et al. as a direct source and require task-matched writing-assistance evidence before implementing premise-level sycophancy coverage.
- **C08:** Retain the metaphor exchange as a qualitative test case only.
- **C09:** After C06 establishes the product homes, prototype conceptual coherence and local repairability separately, with distinct success measures, matched human and AI-assisted examples, blind review, overlap analysis, inter-rater agreement, and false-positive review on literary and experimental prose. Combine them only if a joint assessment adds nonredundant value.
- **C10:** Ingest Yakura et al. directly, then require register-matched written corpora before changing written-prose vocabulary evidence, wording, or thresholds.
- **C11:** Preserve real uncertainty and revision; review #35 wording for conflict with the ban on manufactured irregularity.

## Evaluation of approved changes

No recommendations have been approved or implemented. If C03, C06, or C09 is approved, evaluate catalogue coverage, contextual treatment, overlap with existing checks, and false-positive pressure in register-matched samples. Single-document authorship accuracy is not an appropriate success metric.

## Document review

- **Review status:** passed
- **Review method:** `ce-doc-review` coherence, feasibility, product-fit, and adversarial review, supplemented by evidence-directness, provenance, live-project mapping, decision/status, deterministic-audit reproducibility, full-text beginning/middle/end/structure comparison, snapshot-hash, link, manifest, and validator checks. The optional cross-model pass was skipped because no permitted non-Claude peer CLI was available; Claude was not invoked.
- **Findings resolved:** Migrated the card and snapshot to the current templates; made the canonical URL and extraction method consistent; added stable claim IDs and one authoritative table; removed duplicate decision statements; corrected #39 and provenance overclaims; documented the body-only audit derivation and candidate context; added extraction verification; updated the snapshot digest and retrieval-date treatment; made calibration status and C01 disposition consistent; sequenced C09 after the C06 product-home decision; scoped C10 to spoken English with a written-register evidence gate; added a writing-task transfer gate to C07; and separated conceptual coherence from local repairability.
- **Unresolved findings:** none
