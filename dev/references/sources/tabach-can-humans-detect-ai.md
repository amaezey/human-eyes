# Tabach: Can Humans Detect AI? Mining Textual Signals of AI-Assisted Writing Under Varying Scrutiny Conditions

## Metadata

- **URL:** https://arxiv.org/abs/2604.23471
- **Author / owner:** Daniel Tabach
- **Published:** 2026-04-25
- **Retrieved:** 2026-07-15
- **Extracted:** 2026-07-15
- **Source type:** academic empirical preprint; controlled experiment
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** arXiv:2604.23471v1; DOI 10.48550/arXiv.2604.23471
- **Version / revision:** v1, submitted 2026-04-25
- **Full-text status:** complete
- **Snapshot:** `snapshots/tabach-can-humans-detect-ai.md`
- **Extraction method:** authoritative arXiv PDF downloaded and preserved; all 25 pages converted from the embedded text layer with Poppler `pdftotext -layout`; experimental arXiv HTML and rendered PDF pages 1, 13, and 25 used to verify structure and content
- **Snapshot SHA-256:** `790d7b67c23a3822f8aa17111702e224fda84470d79d8befbc789f2760f9b90b`
- **Model / corpus scope:** English opinion pieces about remote work, 200 to 400 words each; 21 writers from the author's personal and Georgia Tech-adjacent networks produced 41 validated documents while using a Sonnet chatbot of unspecified version; 9 control writers and 12 warning-condition writers; 251 judges supplied 1,999 forced-choice pair evaluations; collection and evaluation dates are not reported
- **Access limitations:** No full-text access limitation. The 25-page authoritative PDF is preserved at `snapshots/attachments/tabach-can-humans-detect-ai-arxiv-v1.pdf` with SHA-256 `da5b64eb45d99dd7f0ea227021aad07534b5369db80f446c1d4fef2e28673ebf`. Figure graphics are present in the PDF; the Markdown snapshot preserves their captions, recoverable labels, and surrounding interpretations but not rasterized graphics. Table 7 omits its middle 21 document rows in the source itself. Code and data are available only by request to the author.
- **Queue-title mismatch:** The user queue title was `Can Humans Detect AI?`; the work at the authoritative URL is titled `Can Humans Detect AI? Mining Textual Signals of AI-Assisted Writing Under Varying Scrutiny Conditions`. This card ingests the actual work at the URL.

## Summary

This preprint studies whether warning people that an AI detector will inspect their work changes how their AI-assisted writing is perceived. Twenty-one writers produced 41 short English opinion pieces with access to the same Sonnet chatbot; 251 judges then made 1,999 forced choices between one warned and one unwarned document of the same stance. Judges chose the warned document as human 54.13% of the time, but measured overlap, lexical, sentence, pronoun, hedging, and contraction features showed heavy descriptive overlap between conditions. The study therefore supplies evidence about perceived humanness under a warning condition, not ordinary human ability to distinguish human from AI text. Its statistical inference is limited by repeated judgements of the same documents and judges, a small writer sample, descriptive Phase 1 analysis, substantial judge-session attrition, unreported planned analyses, and no mixed-effects model.

## Main insights

- The judge task was deliberately deceptive: both conditions had chatbot access, so the outcome is warned versus unwarned perceived humanness, not human versus AI detection accuracy.
- The warned document won 54.13% of forced choices. The effect is small, and the reported binomial p-value treats clustered observations as independent.
- Warning-condition writers descriptively took more turns and spent longer. Their mean session token count was higher but their median was slightly lower, with the higher mean driven by a few long sessions. Phase 1 was too small for inferential tests, and both groups retained similarly high overlap with chatbot output.
- Type-token ratio, sentence-length measures, first-person pronouns, hedging, and contractions showed heavy overlap between the two conditions. This descriptive non-separation, without inferential tests, limits their use as explanations of perceived humanness within this setting.
- Slower and more confident judges leaned further toward the warned condition, while the fastest quartile was near chance. Selective document expansion produced a larger difference in only 92 responses, which the author says may be noise. Fatigue showed no clear effect.
- One highly human-rated warned participant never used the chatbot. Removing that participant weakened but did not erase the aggregate result, and the document pool therefore contains mixed levels of actual AI use.
- The paper's general AI-versus-human feature directions are inherited from cited sources. This experiment does not directly validate those directions because it does not compare an AI group with a human group.

## Evidence and claims to extract

- **Direct source reviewed:** arXiv:2604.23471v1, all 25 PDF pages including the abstract, Sections 1 through 6.1, figures, tables, two footnotes, 22 references, Appendices A through D, and the code/data note.
- **Method and sample:** Alternating participant IDs assigned conditions, despite the abstract describing the warning as random. Participants wrote one for and one against remote work piece, usually producing two documents, with a 200 to 400 word target and a soft 15-minute timer. Sonnet model version, system prompt, and exact collection dates are not reported; source-to-session attribution for the four judge-recruitment channels was untraced because every channel used the same survey link. The final writer sample was 21 people and 41 validated documents. Of 315 judge sessions started, 251 supplied at least one answer and only 76 completed fully; partial sessions contributed to the 1,999 pair responses. Each response compared 150-word previews after a forced 10-second reveal, with optional full-text expansion. Observations repeat by judge and document.
- **Direct versus cited evidence:** C01 through C08 and C10 through C14 are direct designs, results, author interpretations, or stated limitations from this study. C09 separates feature directions inherited from cited studies from this paper's direct descriptive condition comparison. The claim that feature-based AI detectors extract typical AI signals is an author interpretation, not an evaluated comparison with a named detector.
- **Important limits and counterexamples:** The writer sample is small, education-skewed, personally recruited, and limited to one English topic and one short opinion genre. The warning had no real consequence. Condition assignment was deterministic rather than random. The binomial test assumes independent pair responses despite clustering by 251 judges and 41 reused documents; the author says its p-value may be anti-conservative and plans a crossed mixed-effects model. Phase 1 differences are descriptive only. One warned writer used no chatbot, six documents were at or near zero overlap, and one of those six resulted from a missing assistant response caused by a Streamlit bug. The overlap score cannot recover idea, structural, or earlier interaction dependence. The paper does not report the planned self-reported reliance or belief-alignment analyses. No source document texts or code are publicly preserved at the URL.

## Matched patterns / rules

- `STRATEGY.md`: human-eyes examines writing patterns and does not determine whether a human or AI wrote a document.
- `human-eyes/references/process.md`: the product boundary prohibits authorship inference and requires a complete Audit before editing.
- `sentence-length-variance` and `vocabulary-diversity` in `human-eyes/scripts/patterns.json` and their implementations in `human-eyes/scripts/grade.py`.
- `no-excessive-hedging` in `human-eyes/scripts/patterns.json` and `human-eyes/scripts/grade.py`; this check targets stacked lexical constructions, not the paper's broad hedge-word rate.
- `genre_specific` and `referential_clarity` in `human-eyes/scripts/judgement.json`; neither is a generic first-person or pronoun-frequency detector.
- `dev/TESTING.md`: matched-corpus provenance, genre/register breadth, complete Audits, weak/reversed-pair reporting, and the prohibition on presenting surface-only output as a human-versus-AI benchmark.
- H3, H12, H13, H22, and H28 in `dev/hypotheses.md`: detection framing, genre-aware calibration, sentence-length mean, long-tail structural variation, and higher-level comparison dimensions.
- Related source cards: `russell-karpinska-iyyer-detectors.md`, `waltzer-teachers-detect-ai-essays.md`, `wang-et-al-human-like-text-liked-by-humans.md`, and `xia-stanczak-roth-detector-generalization.md`.

## Associated hypotheses

- H3: Drop detection framing entirely.
- H12: Genre-aware threshold calibration.
- H13: Sentence-length mean as a grader check.
- H22: Long-tail compression and grammatical standardisation.
- H28: Originality, clarity, and formality as comparison dimensions.
- Proposed evaluation hypothesis: human judgements of AI-assisted prose may respond to interaction history or unmeasured document-level qualities that fixed surface-feature summaries do not capture.
