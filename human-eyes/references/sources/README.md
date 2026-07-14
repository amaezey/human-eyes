# Source references
These files track the sources cited by human-eyes and how each one currently relates to the skill catalogue.

Each source card starts with the headings in [TEMPLATE.md](TEMPLATE.md). A reviewed card appends project coverage, recommendations, decisions, and implementation status.

Use [pattern-opportunities.md](pattern-opportunities.md) to track source claims promoted into pattern additions, hypotheses, process guidance, metadata conventions, or explicit non-promotions.

First-pass extracted: 2026-05-05.
Second-pass reviewed: 2026-05-05. The 72 cards present at that review include source notes, evidence-tier metadata, a skill-use audit, pattern/rule mappings, associated hypotheses, and follow-up questions. The 2026-07-14 Wikipedia refresh added the three requested direct-source cards listed below. New source cards should include extraction date and, when relevant, model family, model version, corpus date range, or source-page update date so time-sensitive AI tells do not become stale blacklists.

## Source review procedure

Use this procedure for a new source, an updated source, or new evidence cited by an existing source.

### 1. Read and preserve the source

1. Read the source itself rather than relying on another source's summary.
2. Save the accessible full text under `snapshots/` so the reviewed material remains available.
3. Record the original URL, title, author, publication date, retrieval date, and a stable identifier such as a revision ID or DOI when one exists.
4. Record the extraction method, snapshot path, and SHA-256 hash of the saved snapshot.
5. For a changing web page, preserve the reviewed revision and record the revisions compared.
6. Record any material that could not be accessed or preserved.
7. Open relevant cited sources directly. Give each source its own card and snapshot when its findings will be used by the project.
8. Add the source card, original URL, snapshot path, and extraction method to [snapshots/MANIFEST.md](snapshots/MANIFEST.md).

### 2. Create or update the source card

Start with [TEMPLATE.md](TEMPLATE.md). In this step, complete the source and evidence sections using these criteria. Complete the project-dependent sections in Step 3.

#### Metadata

- Title, author or owner, publication date, URL, retrieval date, source type, stable identifier, snapshot path, extraction method, and SHA-256 hash of the saved snapshot.
- Model, model version, corpus date, genre, platform, and language when relevant.

#### Summary

- What the source is, what it examines, and what it contributes to human-eyes.
- The source's method, sample, comparison, and stated scope in plain language.

#### Main insights

- Every relevant phrase, construction, structural habit, formatting habit, vocabulary item, tonal tendency, workflow residue, evaluation finding, rewriting finding, process finding, provenance finding, qualification, and counterexample.
- Which claims come directly from the source and which come from material it cites.
- Exact examples where the source supplies them.

#### Evidence and claims to extract

For every relevant claim, record:

- **Claim:** the phrase, construction, writing habit, model behaviour, evaluation result, process, or provenance issue identified by the source.
- **Source type:** peer-reviewed empirical research, academic preprint, corpus analysis, controlled experiment, qualitative study, first-party documentation, data journalism, practitioner observation, vendor analysis, or catalogue source.
- **Evidence basis:** the material supporting the claim, such as measured text, generated examples, interviews, editorial experience, repeated observations, isolated examples, or another cited source.
- **AI-use finding:** what the evidence shows about how AI uses, overuses, misuses, introduces, or changes the identified pattern or behaviour.
- **Scope:** the sample size, models and versions, dates, genre, platform, language, text length, comparison group, and method relevant to the finding.
- **Evidence directness:** whether the source supplies the underlying evidence itself or reports a claim from another source.
- **Support and uncertainty:** corroborating evidence, conflicting findings, qualifications, exceptions, and unanswered questions.
- **Human comparison, when available:** what human examples show about frequency, context, deliberate use, and appropriate handling.
- **Project relevance:** whether the claim adds evidence for an existing pattern, identifies a missing variation, introduces a new pattern, challenges current behaviour, informs evaluation or rewriting, or requires no project change.

### 3. Compare the source with the project

1. Work through every relevant claim and example in the source card.
2. Locate the exact existing implementation or documentation that might cover it.
3. Inspect and, when necessary, run the current check rather than treating similar documentation as proof of coverage.
4. Identify what is already covered, partly covered, not covered, or challenged.
5. Assess how the evidence adds to, strengthens, qualifies, or challenges the project.
6. Use deterministic surface-only output for deterministic coverage inspection. A complete Audit requires the full work-bundle process described in [dev/TESTING.md](../../../dev/TESTING.md).
7. Keep the source's claims, the evidence assessment, and the project comparison distinguishable in the card and final report.

Complete these existing template sections during the project comparison:

#### Skill-use audit

- Good uses of the source in human-eyes.
- Claims the source cannot support on its own.
- Evidence the project currently underuses.
- Patterns, examples, qualifications, and challenges not yet represented in the project.

#### Matched patterns / rules

- Every existing check or agent assessment the source supports, extends, qualifies, or challenges.

#### Associated hypotheses

- Every existing hypothesis the source informs and any new hypothesis it suggests.

#### Questions / follow-up

- Missing access, unresolved source questions, evidence still to retrieve, and project decisions still required.

Append this section for the project comparison:

#### Project coverage

For every relevant claim or example, record:

- The exact existing check, agent assessment, guidance, test, source card, or hypothesis that might cover it.
- Whether the claim is fully covered, partly covered, not covered, or challenges current project behaviour.
- What the current implementation actually finds when tested.
- What is missing from the implementation, evidence mapping, explanation, or tests.
- How the difference could be incorporated into human-eyes.
- Whether frequency, clustering, genre, quotation, formatting, or deliberate use should affect the proposed implementation.

### 4. Make recommendations

Propose how each difference identified in the project comparison could be incorporated. Add these sections to the source card:

#### Recommendations

Give one recommendation for every reviewed claim:

- Extend an existing check.
- Add examples or tests to an existing check.
- Add a new check.
- Add or change an agent assessment.
- Add editing or rewriting guidance.
- Add genre-specific handling.
- Reconsider an existing check.
- Run evaluation work before choosing an implementation.
- Record the evidence without changing the product.
- Take no further action.

For each recommendation, record:

- The proposed change.
- Why it follows from the source and coverage review.
- The checks, assessments, guidance, tests, or documentation affected.
- The testing required.
- The user's decision: pending, approved, or rejected.
- The implementation status: not started, in progress, implemented, or not applicable.

Keep recommendations separate from completed changes.

#### Evaluation of approved changes

Use the applicable product metrics from `STRATEGY.md`:

- **Catalogue coverage:** known examples and meaningful variations of the catalogued AI-writing tell are found by the relevant checks or assessments.
- **Check accuracy:** the check identifies the construction it names without matching unrelated or superficially similar text.
- **Treatment in context:** the audit explains whether frequency, genre, quotation, formatting, or deliberate use changes how the finding should be understood or revised.
- **Pattern accumulation in matched samples:** where relevant, matched human and AI samples show whether AI writing accumulates the pattern more heavily. This evaluates the catalogue and does not determine who wrote an individual document.

### 5. Report the review

Start with a direct explanation of:

- What the source added.
- What was already known.
- How much the project currently covers.
- What is genuinely new.
- What challenges existing checks or assumptions.
- Whether the source produced a large, moderate, or small change in understanding.
- Which decisions the user needs to make.

Then provide one complete table:

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|

Use this as the authoritative review table rather than splitting the result across inconsistent summaries.

### 6. Stop for decisions

Unless the user requested implementation, stop after the source card, evaluation, recommendations, and decision list.

After the user approves recommendations:

1. Implement only the approved changes.
2. Add or update the required tests.
3. Run the relevant evaluation and regression checks in [dev/TESTING.md](../../../dev/TESTING.md).
4. Update the source card and review table with the actual implementation status.
5. Report what changed, what remains, and what was not adopted.

## Evidence tiers
- **Peer-reviewed / academic empirical:** strongest for pattern evidence, usually still aggregate, register-scoped, or corpus-scoped rather than proof for a single document.
- **First-party model docs:** useful for model behaviour, capability, policy, and version-drift context; not prose-pattern proof unless the document names the behaviour directly.
- **Journalism / reported cases:** useful for incidents, public salience, provenance, harms, and social context; weaker for reusable pattern thresholds.
- **Practitioner / teacher / editor essays:** useful for manual review prompts, genre branches, craft language, and examples; weaker for hard severity or detector claims.
- **Vendor / detector pages:** useful for product framing, uncertainty UX, and candidate features; weak for pattern validity unless independently corroborated.
- **Conduit / catalogue sources:** Wikipedia, Vollmer, and the original skill are discovery maps. Prefer their upstream sources for evidence and cite the conduit only for provenance.

Second-pass sources whose exact pages were found but whose inherited mappings need caution:
- [AI for Lifelong Learners: Tells beyond the em-dash](ai-lifelong-learners-em-dash.md) - exact post reviewed from screenshot sequence supplied 2026-05-05; useful practitioner evidence, but not a detector-threshold source.
- [Aranya / Poetly: AI poetry and process](aranya-poetly-ai-poetry.md) - exact post reviewed; source came from `README.md` and `dev/research/vollmer.md`; it supports poetry-process questions more than the inherited aphorism-density / negate-and-redefine / mood-word-accumulation mapping.
- [Sean Trott: LLM signature analysis](trott-llm-signature-analysis.md) - exact post reviewed; source came from `README.md` and `dev/research/vollmer.md`; it supports predictability and calibration cautions, not surface-tell shortcuts.
- [SEO Engine: Signs of AI writing](seoengine-ai-writing-signs.md) - exact article reviewed from local clipping supplied 2026-05-05; it is useful as a vendor/practitioner checklist, but its numeric detector, model-frequency, and ranking-impact claims need upstream corroboration.

Deep extraction exists for:
- [Wikipedia: Signs of AI writing](../../../dev/research/wikipedia-signs-of-ai-writing.md)
- [Matthew Vollmer: I Asked the Machine to Tell on Itself](../../../dev/research/vollmer.md)

## Foundation
- [blader/humanizer](blader-humanizer.md)
- [Wikipedia: Signs of AI writing](wikipedia-signs-of-ai-writing.md)
- [Matthew Vollmer: I Asked the Machine to Tell on Itself](vollmer-machine-tell-on-itself.md)

## Academic vocabulary, grammar, behaviour, domains, limits, and stylometry
- [Kobak et al.: Delving into LLM-assisted writing in biomedical publications through excess vocabulary](kobak-llm-excess-vocabulary.md)
- [Juzek and Ward: Why Does ChatGPT Delve So Much?](juzek-ward-delve.md)
- [Juzek and Ward: Word Overuse and Alignment in Large Language Models](juzek-ward-word-overuse-alignment.md)
- [Reinhart et al.: Do LLMs write like humans?](reinhart-llm-write-like-humans.md)
- [Geng and Trotta: Human-LLM Coevolution](geng-trotta-human-llm-coevolution.md)
- [Geng and Trotta: Is ChatGPT Transforming Academics' Writing Style?](geng-trotta-transforming-academic-style.md)
- [Sussman and Carter: AI-mediated political communication](sussman-carter-ai-mediated-communication.md)
- [Zhou, Cho, and Terveen: LLM use in Wikipedia workflows](zhou-llms-wikipedia.md)
- [Dik, Erdem, and Dik: GPTZero by essay length](dik-gptzero-accuracy.md)
- [Kousha and Thelwall: How much are LLMs changing academic papers after ChatGPT?](kousha-thelwall-academic-papers.md)
- [Sun et al.: Idiosyncrasies in Large Language Models](sun-idiosyncrasies-llms.md)
- [Ju, Blix, and Williams: Domain Regeneration](ju-blix-williams-domain-regeneration.md)
- [Abdulhai et al.: How LLMs Distort Our Written Language](abdulhai-llms-distort-written-language.md)
- [Russell, Karpinska, and Iyyer: Frequent ChatGPT users as detectors](russell-karpinska-iyyer-detectors.md)
- [Nature: Signs of AI-generated text found in biomedical abstracts](nature-biomedical-abstracts.md)
- [Przystalski et al.: Stylometry recognizes human and LLM-generated texts](przystalski-stylometry.md)
- [Zaitsu et al.: Stylometry can reveal AI authorship](zaitsu-stylometry.md)
- [Bisztray et al.: I Know Which LLM Wrote Your Code Last Summer](bisztray-code-stylometry.md)
- [Creo and Ranganath: Show, Don't TELL: Explainable AI-Generated Text Detection](creo-ranganath-tell-explainable-detection.md)
- [Walsh et al.: AI poetry computational analysis](walsh-ai-poetry.md)
- [Neil Clarke: A Concerning Trend](clarke-clarkesworld-concerning-trend.md)
- [Russell et al.: StoryScope narrative idiosyncrasies in AI fiction](russell-storyscope-ai-fiction.md)
- [Waltzer et al.: Can teachers detect AI-generated student essays?](waltzer-teachers-detect-ai-essays.md)
- [Murray and Tersigni: Can instructors detect AI-generated papers?](murray-tersigni-ai-generated-papers.md)
- [Jiang and Hyland: Engagement markers in ChatGPT-generated argumentative essays](jiang-hyland-engagement-markers.md)
- [Dhillon et al.: MFA students vs LLMs fiction](dhillon-mfa-students-llms-fiction.md)
- [Spero and Emi: Pangram AI-generated text classifier technical report](spero-emi-pangram-classifier.md)
- [Liang et al.: GPT detectors are biased against non-native English writers](liang-detector-bias.md)
- [Lu et al.: Synergizing Stylometrics with Semantics](lu-et-al-stylometrics-semantics.md)
- [Zhu et al.: Exons-Detect](exons-detect.md)
- [Stowe et al.: Identifying bias in machine-generated text detection](stowe-detector-bias.md)
- [Wang et al.: Is Human-Like Text Liked by Humans?](wang-et-al-human-like-text-liked-by-humans.md)
- [Xia, Stańczak, and Roth: Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis](xia-stanczak-roth-detector-generalization.md)
- [Gao et al.: When Personalization Tricks Detectors](gao-personalization-tricks-detectors.md)
- [Ta et al.: FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning](faid-fine-grained-ai-text-detection.md)
- [El Attar et al.: A Systematic Analysis of Linguistic Features in AI-Generated Text Detection Across Domains and Models](el-attar-linguistic-features-ai-text-detection.md)
- [Tolstykh et al.: GigaCheck, object-centric span localization for LLM-generated content](tolstykh-et-al-gigacheck.md)
- [Tabach: Can Humans Detect AI? Mining Textual Signals of AI-Assisted Writing Under Varying Scrutiny Conditions](tabach-can-humans-detect-ai.md)
- [Suvanto et al.: Interpretable Text Classification Applied to the Detection of LLM-generated Creative Writing](suvanto-interpretable-llm-creative-writing.md)

## Journalism and trade press
- [Eve Fairbanks: The Biggest Tell That Something Was Written by AI](fairbanks-atlantic-ai-writing.md)
- [Matthew Gault / 404 Media: AI fiction is easy to detect](gault-404media-ai-fiction.md)
- [Sam Kriss: Why Does A.I. Write Like ... That?](kriss-nyt-ai-write-like-that.md)
- [Merrill, Chen, and Kumer: What are the clues that ChatGPT wrote something?](merrill-wapo-chatgpt-clues.md)
- [Benj Edwards: OpenAI suppressing em dashes](edwards-ars-em-dash.md)
- [Brian Phillips: the em-dash defense](phillips-ringer-em-dash.md)
- [Wendy Belcher: 10 Ways AI Is Ruining Your Students' Writing](belcher-ai-ruining-student-writing.md)
- [Hua Hsu: What college students lose when ChatGPT writes their essays](hsu-students-lose-chatgpt.md)
- [Karolina Rudnicka: Each AI chatbot has its own distinctive writing style](rudnicka-chatbot-writing-style.md)
- [Slate: ChatGPT, AI shaming, and the paranoia of writing](slate-ai-shaming-paranoia.md)
- [Jonathan Bailey: Em dashes, hyphens, and spotting AI writing](bailey-em-dash-hyphens.md)
- [Futurism: Sports Illustrated published AI-generated writers](futurism-sports-illustrated-ai-writers.md)
- [Gizmodo: CNET AI-generated finance articles](pbs-cnet-ai-finance-articles.md)

## Practitioner essays and writer blogs
- [Linda Caroll: Good Writing, AI Slop, and the Dragon](caroll-good-writing-ai-slop.md)
- [Charlie Guo: The Field Guide to AI Slop](guo-field-guide-ai-slop.md)
- [Shreya Shankar: AI Writing](shankar-ai-writing.md)
- [Blake Stockton: Don't Write Like AI series](stockton-dont-write-like-ai.md)
- [Vauhini Vara: Confessions of a Viral AI Writer](vara-confessions-viral-ai-writer.md)
- [Laura Preston: HUMAN_FALLBACK](preston-human-fallback.md)
- [Laura Preston: An Age of Hyperabundance](preston-hyperabundance.md)
- [Ted Chiang: ChatGPT Is a Blurry JPEG of the Web](chiang-blurry-jpeg.md)
- [Ted Chiang: Why A.I. Isn't Going to Make Art](chiang-why-ai-isnt-art.md)
- [Robin Sloan: human-AI writing notes](sloan-human-ai-writing.md)
- [Sean Trott: LLM signature analysis](trott-llm-signature-analysis.md)
- [Aranya / Poetly: AI poetry and process](aranya-poetly-ai-poetry.md)
- [David J. Germain: Writing dialog with ChatGPT](germain-chatgpt-dialog.md)
- [Brent Csutoras: The em-dash dilemma](csutoras-em-dash-dilemma.md)
- [Fred Rohrer: promotional register and n-gram analysis](rohrer-promotional-register.md)
- [Paul Graham on "delve" (April 2024)](graham-delve-post.md)
- [@hosseeb: How to avoid AI voice](qureshi-avoiding-ai-voice.md)

## Vendor, first-party, and practitioner guides
- [OpenAI: GPT-4 System Card](openai-gpt-4-system-card.md)
- [OpenAI: Sycophancy in GPT-4o rollback](openai-sycophancy-rollback.md)
- [Anthropic: Claude Sonnet system prompts](anthropic-sonnet-prompts.md)
- [GPTZero: AI Vocabulary](gptzero-ai-vocabulary.md)
- [GPTZero: Perplexity and burstiness](gptzero-perplexity-burstiness.md)
- [Grammarly: Common AI words and phrases](grammarly-common-ai-words.md)
- [Gmelius: Can customers tell an email is written using generative AI?](gmelius-email-ai-isms.md)
- [Bynder: AI marketing identification study](bynder-ai-marketing-study.md)
- [Pangram AI content detector](pangram-classifier.md)
- [Copyleaks AI content detector](copyleaks-detector.md)
- [ZeroGPT AI detector](zerogpt-detector.md)
- [Originality.AI detector](originality-ai-detector.md)
- [NetusAI: stylometry and AI detectors](netusai-stylometry.md)
- [Turnitin AI writing detection](turnitin-ai-writing-detection.md)
- [AI Detectors: How to tell if text is AI written](aidetectors-ai-writing-signs.md)
- [SEO Engine: Signs of AI writing](seoengine-ai-writing-signs.md)
- [SAGE: AI detection for peer reviewers](sage-ai-detection-peer-reviewers.md)
- [Hastewire: How teachers spot ChatGPT use](hastewire-teachers-spot-chatgpt.md)
- [Copy Posse: 5 signs your email was written by AI](copyposse-email-ai-signs.md)
- [AI for Lifelong Learners: Tells beyond the em-dash](ai-lifelong-learners-em-dash.md)
- [theclaymethod/unslop](theclaymethod-unslop.md)
- [chitalian/offensive-ai-speak (avoid-ai-speak skill)](chitalian-offensive-ai-speak.md)
- [hardikpandya/stop-slop](hardikpandya-stop-slop.md)
- [jalaalrd/anti-ai-slop-writing](jalaalrd-anti-ai-slop-writing.md)
- [NousResearch/autonovel: ANTI-SLOP](nousresearch-autonovel-anti-slop.md)
- [Onur Solmaz: kill-ai-smell skill and ai-smell stylometric corpus](solmaz-kill-ai-smell.md)
- ["You're absolutely right!": Claude Code issue #3382](claude-code-youre-absolutely-right.md)
- [Byk3y/no-slop](byk3y-no-slop.md)
- [Paech et al.: AntiSlop Sampler and Antislop](paech-antislop-sampler.md)
