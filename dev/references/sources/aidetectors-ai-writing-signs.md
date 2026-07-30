# AI Detectors: How to Tell If Text Is Written by AI: 9 Signs to Look For

## Metadata

- **URL:** https://www.aidetectors.io/blog/how-to-tell-if-text-is-ai-written
- **Author / owner:** AI Detectors
- **Published:** 2026 page context; exact date not stated in the preserved page
- **Retrieved:** 2026-05-05
- **Extracted:** 2026-05-05
- **Contract updated:** 2026-07-15; the preserved extraction was brought into the source-ingest contract without a fresh article scrape
- **Source type:** vendor-authored practitioner guide
- **Evidence tier:** Vendor / detector pages
- **Review mode:** update
- **Stable identifier:** none found
- **Version / revision:** living webpage as retrieved 2026-05-05; previous record was the same preserved article body before source-ingest contract framing
- **Full-text status:** complete
- **Snapshot:** `snapshots/aidetectors-ai-writing-signs.md`
- **Extraction method:** preserved Jina Reader URL-to-Markdown extraction; no fresh scrape
- **Snapshot SHA-256:** `de47b2e3453befb7e82690b2cfbea85ba9ddb1a2177b4065cf1cef57d7fd7e22`
- **Model / corpus scope:** undated vendor observations framed as applying to ChatGPT, Claude, Gemini, and other LLMs in student essays, marketing copy, social posts, and unspecified articles; no model versions, prompts, sample, comparison corpus, language, platform, text-length distribution, annotation method, or measurement dates are supplied; the page mentions GPT-5 and Claude 3.5 without documenting tests
- **Access limitations:** none for the preserved article body; the page supplies no footnotes, datasets, test outputs, methodology, or sources for its reliability, frequency, threshold, detector-performance, model-family, or model-progress claims

## Summary

This AI-detector vendor article presents nine manual signs of AI-shaped prose, illustrated with short constructed examples, then recommends combining several signs with detector tools, author conversation, and document metadata. Its useful contribution is a compact practitioner vocabulary for sentence rhythm, hedging, specificity, stance, transition density, voice, paragraph shape, and source grounding, plus explicit cautions against treating one em dash or one signal as proof. It reports no study, measured sample, human comparison corpus, or validation method, so its numerical thresholds, comparative rates, reliability labels, model-family claims, and promised detection performance are unverified vendor assertions rather than empirical evidence.

## Main insights

- The nine named signs are uniform sentence length, excessive hedging, em-dash overuse, generic examples, overly balanced perspectives, transition-word overload, technically perfect but personality-free prose, repetitive paragraph structure, and missing or nonspecific citations.
- The strongest reusable material is qualitative and contextual: inspect clusters, preserve legitimate human punctuation and qualification, examine specificity and stance, verify named sources, and consider writing process rather than treating one surface cue as authorship proof.
- The article repeatedly overstates its evidence. It calls sentence uniformity the most reliable manual signal, gives a 15-20-word band, claims transition words occur two to three times as often, proposes a 30% em-dash threshold and three- or five-sign suspicion thresholds, calls detector output data-backed confirmation, says the signs catch most cases, and attributes stable traits to model families without showing data.
- Several human comparisons are categorical rather than measured: humans supposedly vary sentence length, draw on lived experience, take sides, accept imperfections, and structure paragraphs organically. These are useful review questions, not universal human-writing rules.
- The page itself supplies important counterweight: em dashes are valid punctuation, one signal is insufficient, edited or newer-model output can be harder to spot, and non-native or formal academic human writing may exhibit the same cues.

## Evidence and claims to extract

- **Direct source reviewed:** Complete preserved article titled "How to Tell If Text Is Written by AI: 9 Signs to Look For," including all nine sections, constructed examples, caveat, confirmation workflow, FAQs, final thoughts, and promotional footer, retrieved 2026-05-05.
- **Method and sample:** Practitioner checklist and vendor marketing copy based on unspecified observation. No sample size, models or versions tested, dates of generated text, prompts, genres by claim, languages, human comparison group, annotators, detector runs, statistical analysis, or article-length controls are disclosed.
- **Direct versus cited evidence:** C01-C13 are direct statements or examples from this page, but none are supported by a disclosed measurement. The article mentions unspecified "studies" and "research" only as examples of vague attribution; it does not cite upstream research for its own claims.
- **Important limits and counterexamples:** Constructed examples show what the author means but cannot establish prevalence, reliability, causality, a threshold, or an authorship verdict. The page acknowledges legitimate human em-dash use, non-native and formal-academic look-alikes, editing and model drift, imperfect detectors, and the need for multiple signals. Its commercial interest in detection and citation-verification tools further limits its value as independent validation.

## Matched patterns / rules

- G9 `sentence-length-variance`; H13 sentence-length mean; H22 long-tail compression and grammatical standardisation
- E1 `no-filler-phrases`, E2 `no-excessive-hedging`, and H12 genre-aware threshold calibration
- C7 `no-em-dashes`; deliberate-punctuation and human-look-alike guidance
- H6 `faux_specificity`
- H7 `neutrality_collapse` and E3 `no-false-concession-hedges`
- E1 `no-filler-phrases` and E8 `no-formulaic-openers` as partial coverage of `It is worth noting`; E6 `no-soft-scaffolding` as an uncovered neighbour for the broader transition-overload claim
- H3 `tonal_uniformity` and the rewrite process's voice-preservation requirements
- G13 `structural_monotony`, H2 `no-tidy-paragraph-endings`, and `paragraph-length-uniformity`
- A5 `no-vague-attributions` and H10 `genre_specific` citation/source verification
- `overall-signal-stacking`, product non-authorship boundary, H3 detection-framing review, H7 advisory catalogue, H9 similar-species disambiguation, H12 genre calibration, and H25 model-family versus generic-AI residue

## Associated hypotheses

- H3: Drop detection framing entirely
- H7: Five-check gating grader plus advisory catalogue
- H9: Field-guide voice with similar-species disambiguation per pattern
- H12: Genre-aware threshold calibration
- H13: Sentence-length mean as a grader check
- H22: Long-tail compression and grammatical standardisation
- H25: Model-family versus generic-AI residue
