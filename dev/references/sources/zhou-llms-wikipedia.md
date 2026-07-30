# Zhou, Cho, and Terveen: LLMs in Wikipedia

## Metadata

- **URL:** https://arxiv.org/abs/2509.07819
- **Author / owner:** Moyan Zhou, Soobin Cho, and Loren Terveen
- **Published:** 2025-09-09
- **Retrieved:** 2026-07-17
- **Extracted:** 2026-07-17
- **Source type:** Academic empirical preprint; qualitative semi-structured interview study
- **Evidence tier:** Peer-reviewed / academic empirical (preprint; this version is not identified as peer reviewed)
- **Review mode:** update
- **Stable identifier:** arXiv:2509.07819v1; arXiv-issued DataCite DOI 10.48550/arXiv.2509.07819
- **Version / revision:** Current review: arXiv v1 submitted 2025-09-09; prior record: the same v1 PDF in a 2026-07-14 complete-text snapshot
- **Full-text status:** complete
- **Snapshot:** `snapshots/zhou-llms-wikipedia.md`
- **Extraction method:** Official arXiv v1 PDF downloaded with `curl`; all 19 pages extracted from the embedded text layer with Poppler `pdftotext -layout`; PDF metadata and image inventory checked with `pdfinfo` and `pdfimages -list`; pages 1, 10, and 19 rendered with `pdftoppm` and visually compared; arXiv abstract, export API metadata, and experimental HTML checked for identity, version, and structure
- **Snapshot SHA-256:** `b129295c355db9c62346b4f966c39274ef81346fdf95c5704a137da0611389ce`
- **Model / corpus scope:** Sixteen Wikipedia editors who had used LLMs in editing; 11 recorded interviews and five email interviews; participant table lists ChatGPT for 14 participants and leaves P14-P15's model cells blank, with additional Gemini, You.com, Grok, Claude, and Llama entries; a result quotation also names Perplexity; English-language paper about multilingual Wikipedia workflows, with participant language, Wikipedia edition, exact interview dates, tool builds, prompts, and output corpus not reported
- **Access limitations:** No substantive source material is missing. The 19-page PDF has no embedded raster images and required no OCR. Both tables, quotations, limitations, and references through [98] are preserved. The arXiv page assigns DataCite DOI 10.48550/arXiv.2509.07819, but the manuscript's ACM reference contains a placeholder publication DOI and no publication DOI is identified. The official PDF was re-fetched and its SHA-256, `ceab9a00f3eb70815f40e0ab859e0a812374e58e8505092a0110755faaabb99b`, matches the prior snapshot's recorded PDF digest.

## Summary

This 19-page arXiv v1 qualitative preprint reports semi-structured interviews with 16 Wikipedia editors who had used LLMs in their editing. It identifies generation, search, and refinement uses; reports that experienced editors described broader topics, more perspectives, confidence, and self-perceived quality while newcomers described lower entry barriers but heavier reliance on LLM guidance; and records direct participant observations about promotional tone, absent or unreliable sources, fabricated facts and references, and damaged wikilinks or wikitext. Its strongest human-eyes contribution is a Wikipedia-specific review boundary: evaluation, verification, and modification are editorial safeguards, not authorship tells, and extensive editing can make LLM-assisted work acceptable while human editors can still be falsely accused. The study supplies no output corpus, rates, comparison group, prevalence estimate, causal estimate, detector validation, or document-level threshold. Its newcomer participation model and three assistant-design proposals are author synthesis and design implications, not tested product outcomes.

## Main insights

- The authors received an IRB exemption, excluded two graduate-student pilots, obtained participant consent, conducted 16 interviews with anonymous reporting, used email for five interviews, observed saturation after interview 13, and derived 1,524 open codes with ATLAS.ti through collaborative thematic analysis; the sample was purposive, snowball-assisted, and limited to editors who had used LLMs.
- Reported uses fall into generation, search, and refinement, including examples, editing guidance, article creation, code, sources, images, information, copyediting, formatting, and translation.
- Experienced editors described new topics and tasks, alternative perspectives, confidence in unfamiliar areas, and improved contribution quality. These are participant perceptions and anecdotes, not controlled performance measurements.
- Newcomers described lower research, language, and technical barriers, but some relied on LLMs to draft articles or fill gaps before they had developed Wikipedia policy and editorial judgment.
- Participants directly described overly positive or promotional Wikipedia prose, including `it's one of the best`, `there are so many possibilities`, `puffery peacock terms`, and unspecified English expressions not typically found in Wikipedia, especially in text generated from scratch; the last observation supplies no lexical examples.
- Participants reported missing sources, click-driven commercial sources, fabricated sources, invented facts, and hallucination, with an explicit qualification that obscure content and less common programming languages can be harder for the tools.
- Editors described three safeguards: evaluate readability, coherence, consistency, and whether a suggestion improves the writing; verify every claim and source; then modify tone, style, context, links, references, and wikitext.
- Community response was not a reliable authorship test. Newcomers reported call-outs and rejection, including criticism of one article as `promotional and essay-like`; experienced editors reported approval after substantial editing, and an experienced editor reported a false accusation.
- The authors interpret these reports as a participation paradox: LLMs lower entry barriers while moving newcomers prematurely into high-stakes editorial judgment and interrupting gradual social learning.
- The proposed assistant designs scaffold complex work into steps, teach community norms through feedback and examples, and adapt guidance to editor expertise. The source does not test these designs.
- The paper explicitly does not quantify prevalence or generalisability and excludes editors who never used LLMs or stopped using them, creating adoption-confidence and selection boundaries.

## Evidence and claims to extract

- **Direct source reviewed:** Complete 19-page arXiv v1 PDF of *LLMs in Wikipedia: Investigating How LLMs Impact Participation in Knowledge Communities*, including abstract, sections 1-6, participant Table 1, use-case Table 2, limitations, conclusion, and references through [98].
- **Method and sample:** After an institutional IRB exemption, two graduate-student pilot interviews were used to refine the protocol and excluded from analysis. The authors obtained participant consent, described recording, privacy, and anonymity, and conducted 16 semi-structured interviews with Wikipedia editors recruited through a Wikimedia project page, targeted outreach, and snowball referrals. Eleven recorded Zoom interviews lasted 42:22-77:29 with a 1:03:18 average; five interviews used email; participants received no compensation; saturation was observed after interview 13. The authors used ATLAS.ti for inductive thematic analysis, jointly open-coded three interviews to establish a shared standard, asynchronously coded the rest into 1,524 codes, and collaboratively grouped and named themes. There is no non-user comparison group, output corpus, blind quality rating, prevalence sample, or causal design. Exact interview dates, Wikipedia editions, participant languages, LLM builds, prompts, settings, and output lengths are not reported.
- **Direct versus cited evidence:** C01-C15 and C20 concern the paper's method, participant reports, tables, stated limits, or direct qualitative synthesis. C16 is the authors' discussion-level interpretation. C17-C19 are proposed design implications, not evaluated interventions. C21 records inherited context only: the paper cites [3] for NPOV limits, [46] for a 14-million-abstract vocabulary result, [65] and [95] for writing workflows, [34] and [98] for good-faith newcomer harm from bots, and [84] for Wikimedia's AI-editor strategy. None is a new result of this study, none was recursively ingested here, and none is promoted through this card.
- **Important limits and counterexamples:** Experienced editors reported beneficial uses and accepted edits; one experienced editor reported a false accusation; LLM-assisted editing is broader than copy-pasting a whole generated article; participants self-selected as LLM users; participant reports do not establish prevalence, tool accuracy, causality, authorship, or objective contribution quality; model entries are incomplete and versionless; direct findings are Wikipedia-workflow- and expertise-specific.

## Matched patterns / rules

- A4 `no-promotional-language`: adjacent construction family only. Focused execution on the three source examples returned clear because the live implementation matches nine fixed hype terms plus five product-performance expressions, not `one of the best`, `so many possibilities`, or `puffery peacock terms`.
- A5 `no-vague-attributions`: not coverage for source absence, reliability, fabrication, or claim-citation support. Focused execution on the source-derived examples returned clear; the live matcher covers unnamed-authority phrasing.
- D1 `no-collaborative-artifacts` and `context_leakage`: not supported by this study. The paper concerns human editorial workflows, not conversational residue in finished prose.
- H7 `neutrality_collapse`: adjacent to stance review but not NPOV coverage. It flags hedging or balance that erases a source stance; the participant reports concern overly positive Wikipedia tone and neutralising it.
- H10 `genre_specific`: relevant architecture but no Wikipedia value or branch exists in `human-eyes/scripts/judgement.json`; the academic and journalism branches cover some citation review but do not test Wikipedia policies, source quality, wikilinks, references, or wikitext.
- `human-eyes/references/process.md`: partly covers evaluation and preservation through complete Audit, factual-source closure, quotation/citation preservation, and protected qualifications; it does not implement the paper's Wikipedia-specific three-stage workflow or validate external sources.

## Associated hypotheses

- H9 field-guide voice with similar-species disambiguation: relevant to distinguishing whole-draft reliance, legitimate assistance, extensive human editing, and false accusations.
- H12 genre-aware threshold calibration: relevant because Wikipedia has norms, markup, sourcing, and tone requirements absent from the live genre registry.
- H25 model-family versus generic-AI residue: relevant because the study's participant tool labels are incomplete and versionless and cannot support generic model behaviour.
